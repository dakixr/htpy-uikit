"""
Component Sync Script for htpy-uikit

This script syncs component files from ionisium and costcompiler projects
back into htpy-uikit, keeping the most recently updated version of each component
based on git commit timestamps.

Usage:
    python sync_components.py [--dry-run] [--verbose]
"""

import argparse
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple


@dataclass
class ComponentInfo:
    """Information about a component file"""

    path: str
    project: str
    commit_hash: str
    timestamp: int
    commit_message: str
    size: int


class ComponentSyncer:
    """Syncs components from multiple projects into htpy-uikit"""

    def __init__(self, workspace_root: str = "/Users/dakixr/dev"):
        self.workspace_root = Path(workspace_root)
        self.uikit_path = self.workspace_root / "htpy-uikit"
        self.ionisium_path = self.workspace_root / "ionisium"
        self.costcompiler_path = self.workspace_root / "costcompiler"

        # Component directories
        self.uikit_components = self.uikit_path / "src" / "htpy_uikit" / "components"
        self.ionisium_components = self.ionisium_path / "components" / "ui"
        self.costcompiler_components = self.costcompiler_path / "components" / "ui"

        # Projects mapping
        self.projects = {
            "htpy-uikit": self.uikit_components,
            "ionisium": self.ionisium_components,
            "costcompiler": self.costcompiler_components,
        }

    def get_git_timestamp(
        self, file_path: Path, project_name: str
    ) -> Optional[Tuple[str, int, str]]:
        """Get the latest git commit info for a file"""
        try:
            # Get the latest commit info for the file
            cmd = ["git", "log", "-1", "--format=%H %ct %s", "--", str(file_path)]

            result = subprocess.run(
                cmd,
                cwd=self.projects[project_name].parent.parent,  # Go to project root
                capture_output=True,
                text=True,
                check=True,
            )

            if result.stdout.strip():
                parts = result.stdout.strip().split(" ", 2)
                if len(parts) >= 3:
                    commit_hash, timestamp, message = parts[0], int(parts[1]), parts[2]
                    return commit_hash, timestamp, message

            return None

        except subprocess.CalledProcessError:
            return None
        except Exception as e:
            print(f"Error getting git info for {file_path}: {e}")
            return None

    def get_file_size(self, file_path: Path) -> int:
        """Get file size in bytes"""
        try:
            return file_path.stat().st_size
        except OSError:
            return 0

    def discover_components(self) -> Dict[str, List[ComponentInfo]]:
        """Discover all component files across projects"""
        components = {}

        for project_name, components_dir in self.projects.items():
            if not components_dir.exists():
                print(f"Warning: Components directory not found: {components_dir}")
                continue

            print(f"Scanning {project_name}...")

            # Find all Python files in components directory
            for py_file in components_dir.glob("*.py"):
                if py_file.name.startswith("__"):
                    continue  # Skip __init__.py, __pycache__, etc.

                component_name = py_file.name

                # Get git info
                git_info = self.get_git_timestamp(py_file, project_name)
                if git_info is None:
                    continue

                commit_hash, timestamp, message = git_info
                size = self.get_file_size(py_file)

                component_info = ComponentInfo(
                    path=str(py_file),
                    project=project_name,
                    commit_hash=commit_hash,
                    timestamp=timestamp,
                    commit_message=message,
                    size=size,
                )

                if component_name not in components:
                    components[component_name] = []

                components[component_name].append(component_info)

        return components

    def find_latest_version(self, component_versions: List[ComponentInfo]) -> ComponentInfo:
        """Find the most recently updated version of a component"""
        return max(component_versions, key=lambda x: x.timestamp)

    def copy_component(self, source_info: ComponentInfo, dry_run: bool = False) -> bool:
        """Copy a component file to htpy-uikit"""
        source_path = Path(source_info.path)
        target_path = self.uikit_components / source_path.name

        if dry_run:
            print(f"Would copy: {source_path} -> {target_path}")
            return True

        try:
            # Ensure target directory exists
            target_path.parent.mkdir(parents=True, exist_ok=True)

            # Copy the file
            import shutil

            shutil.copy2(source_path, target_path)

            print(f"Copied: {source_path.name} from {source_info.project}")
            return True

        except Exception as e:
            print(f"Error copying {source_path}: {e}")
            return False

    def sync_components(self, dry_run: bool = False, verbose: bool = False) -> None:
        """Main sync function"""
        print("Discovering components across projects...")
        components = self.discover_components()

        if not components:
            print("No components found!")
            return

        print(f"\nFound {len(components)} unique components")

        if verbose:
            print("\nComponent versions found:")
            for name, versions in components.items():
                print(f"\n{name}:")
                for version in sorted(versions, key=lambda x: x.timestamp, reverse=True):
                    dt = datetime.fromtimestamp(version.timestamp)
                    print(
                        f"  - {version.project}: {dt.strftime('%Y-%m-%d %H:%M:%S')} ({version.commit_hash[:8]}) - {version.commit_message}"
                    )

        print(f"\n{'DRY RUN: ' if dry_run else ''}Syncing components...")

        synced_count = 0
        skipped_count = 0

        for component_name, versions in components.items():
            if len(versions) == 1:
                # Only one version exists
                version = versions[0]
                if version.project == "htpy-uikit":
                    if verbose:
                        print(f"Skipping {component_name}: only exists in htpy-uikit")
                    skipped_count += 1
                    continue

            # Find the latest version
            latest = self.find_latest_version(versions)

            if latest.project == "htpy-uikit":
                if verbose:
                    print(f"Skipping {component_name}: htpy-uikit is already latest")
                skipped_count += 1
                continue

            # Copy the latest version
            if self.copy_component(latest, dry_run):
                synced_count += 1
            else:
                print(f"Failed to sync {component_name}")

        print("\nSync complete!")
        print(f"Synced: {synced_count} components")
        print(f"Skipped: {skipped_count} components")

        if dry_run:
            print("\nThis was a dry run. Use --no-dry-run to actually sync files.")


def main():
    parser = argparse.ArgumentParser(
        description="Sync components from ionisium and costcompiler to htpy-uikit"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Show what would be done without making changes"
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed information")
    parser.add_argument(
        "--workspace-root",
        default="/Users/dakixr/dev",
        help="Root directory containing the projects",
    )

    args = parser.parse_args()

    syncer = ComponentSyncer(args.workspace_root)
    syncer.sync_components(dry_run=args.dry_run, verbose=args.verbose)


if __name__ == "__main__":
    main()
