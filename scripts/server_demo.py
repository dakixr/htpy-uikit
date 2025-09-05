import subprocess

from flask import Flask
from flask import Response
from flask import abort
from flask import send_file

from htpy_uikit.demo import demo_page

from ._utils import DIST
from ._utils import ROOT
from ._utils import build_demo_assets


def build_tailwind_css() -> None:
    """Build Tailwind CSS using pnpm/local binary with a pnpm dlx fallback."""
    try:
        subprocess.run(
            [
                "npx",
                "@tailwindcss/cli",
                "-i",
                "dist/input.css",
                "-o",
                "dist/output.css",
            ],
            check=True,
            cwd=ROOT,
        )
        print("✓ Tailwind CSS built successfully")
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to build Tailwind CSS: {e}")
        raise


app = Flask(__name__, static_folder=None)


@app.get("/")
def index() -> Response:
    return Response(demo_page(), mimetype="text/html; charset=utf-8")


@app.get("/output.css")
def output_css() -> Response:
    if (DIST / "output.css").exists():
        return send_file(DIST / "output.css", mimetype="text/css")
    abort(404)


if __name__ == "__main__":
    build_demo_assets()
    build_tailwind_css()
    app.run(host="127.0.0.1", port=8000, debug=True)
