import sys

def signed_byte(b):
    return b - 256 if b >= 128 else b

def tobytes(name: str) -> list[int]:
    with open(name, "rb") as image:
        file = image.read()
        print(f"Bytes:\n{file}\n")

        unsigned = list(file)
        print(f"Unsiged bytes:\n{unsigned}\n")

        signed = [signed_byte(b) for b in file]
        print(f"Signed bytes:\n{signed}\n")

if __name__ == "__main__":
    filename = sys.argv[1]
    tobytes(filename)
