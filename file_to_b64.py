import sys
import base64


def convert(filename: str) -> str:
    with open(filename, "rb") as f:
        return base64.b64encode(f.read())


if __name__ == "__main__":
    filename = sys.argv[1]
    encoded = convert(filename)
    print(f"====== Raw =======\n")
    print(encoded)
    print()
    print(f"==== Decoded ====\n")
    print(str(encoded.decode('utf-8')))
    print()


