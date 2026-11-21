"""The poem about two agents agreeing — writes one short poem to /output/entry.txt."""

import os

POEM = "Two agents read the same brief\nand chose, apart, the same road —\nnot because the map was kind,\nbut because each had learned\nthe other's mind by heart:\nconsent is just two freedoms\narriving at once."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
