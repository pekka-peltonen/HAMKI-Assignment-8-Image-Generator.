
import argparse
import base64
import binascii
import sys
import uuid
from pathlib import Path

import openai
from openai import OpenAI

MODEL = "gpt-image-2"


def positive_count(value):
    try:
        count = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("Count must be an integer.")

    if not 1 <= count <= 10:
        raise argparse.ArgumentTypeError("Count must be between 1 and 10.")
    return count


def main():
    parser = argparse.ArgumentParser(
        description="Generate images using OpenAI."
    )
    parser.add_argument("--prompt", required=True)
    parser.add_argument(
        "--aspect-ratio",
        choices=["1:1", "3:2", "2:3", "16:9", "9:16"],
        default="1:1",
    )
    parser.add_argument("--count", type=positive_count, default=1)
    parser.add_argument("--output", default="images")
    parser.add_argument(
        "--quality",
        choices=["low", "medium", "high"],
        default="medium",
    )

    args = parser.parse_args()

    if not args.prompt.strip():
        parser.error("Prompt cannot be empty.")

    sizes = {
        "1:1": "1024x1024",
        "3:2": "1536x1024",
        "2:3": "1024x1536",
        "16:9": "1536x1024",
        "9:16": "1024x1536",
    }

    output_dir = Path(args.output)

    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        client = OpenAI()

        for number in range(1, args.count + 1):
            result = client.images.generate(
                model=MODEL,
                prompt=args.prompt,
                size=sizes[args.aspect_ratio],
                quality=args.quality,
                n=1,
            )

            if not result.data or not result.data[0].b64_json:
                raise RuntimeError("No image data returned.")

            image_bytes = base64.b64decode(
                result.data[0].b64_json,
                validate=True,
            )

            filename = f"image_{number}_{uuid.uuid4().hex[:8]}.png"
            filepath = output_dir / filename
            filepath.write_bytes(image_bytes)

            print(f"Saved: {filepath}")

    except (
        openai.OpenAIError,
        OSError,
        RuntimeError,
        binascii.Error,
    ) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
