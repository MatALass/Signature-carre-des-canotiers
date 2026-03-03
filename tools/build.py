#!/usr/bin/env python3
import argparse
import json
import os
from pathlib import Path
from typing import Dict

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES_DIR = ROOT / "templates"
DIST_DIR = ROOT / "dist"


def load_config(path: Path) -> Dict[str, str]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    # Force all values to string for simple template replacement
    return {k: str(v) for k, v in data.items()}


def render_template(template_text: str, vars: Dict[str, str]) -> str:
    out = template_text
    for k, v in vars.items():
        out = out.replace("{{" + k + "}}", v)
    return out


def build(config_path: Path) -> None:
    if not config_path.exists():
        raise SystemExit(
            f"Config not found: {config_path}\n"
            f"Tip: copy tools/config.example.json to tools/config.json"
        )

    vars = load_config(config_path)

    DIST_DIR.mkdir(parents=True, exist_ok=True)

    mapping = {
        "signature.full.html": "signature.full.html",
        "signature.compact.html": "signature.compact.html",
        "signature.text.txt": "signature.text.txt",
    }

    for src_name, dst_name in mapping.items():
        src_path = TEMPLATES_DIR / src_name
        dst_path = DIST_DIR / dst_name

        if not src_path.exists():
            raise SystemExit(f"Missing template: {src_path}")

        template_text = src_path.read_text(encoding="utf-8")
        rendered = render_template(template_text, vars)

        dst_path.write_text(rendered, encoding="utf-8")
        print(f"Built: {dst_path.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build email signature dist/ from templates/")
    parser.add_argument(
        "--config",
        type=str,
        default=str(ROOT / "tools" / "config.json"),
        help="Path to config json (default: tools/config.json)",
    )
    args = parser.parse_args()
    build(Path(args.config))


if __name__ == "__main__":
    main()