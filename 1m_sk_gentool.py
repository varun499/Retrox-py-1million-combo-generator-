import random
import string
import os
def generate_key():
    chars = string.ascii_letters + string.digits  # a-zA-Z0-9
    suffix = ''.join(random.choices(chars, k=24))
    return f"sk_live_{suffix}"
def main():
    download_path = "/sdcard/Download"
    filename = "one_million_keys.txt"
    full_path = os.path.join(download_path, filename)
    with open(full_path, "w") as f:
        for _ in range(1_000_000):
            f.write(generate_key() + "\n")
    print(f"File saved successfully at: {full_path}")
if __name__ == "__main__":
    main()