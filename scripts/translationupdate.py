import os
import shutil
import logging

# Set up the logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("update_log.txt", mode="w")],
)

destDir = os.path.join(os.getcwd(), "content", "localisation", "replace")


def update(
    srcDir, destDir=os.path.join(os.getcwd(), "content", "localisation", "replace")
):
    for filename in os.listdir(srcDir):

        src_file_path = os.path.join(srcDir, filename)
        dst_file_path = os.path.join(destDir, filename)

        if os.path.isfile(src_file_path):
            if not os.path.isfile(dst_file_path):
                # If the destination file doesn't exist, copy the source file
                shutil.copy2(src_file_path, dst_file_path)
                logging.info(f"Copied {src_file_path} to {dst_file_path}")
            else:
                # Read the source file
                srcKeys, destKeys = dict(), dict()
                for line in open(src_file_path, "r", encoding="utf-8"):
                    row = line.split(":", 1)  # Split only at the first colon

                    if len(row) == 2:
                        srcKeys[row[0].strip()] = row[1].rstrip()  # Clean key and value

                # Read the destination file
                for line in open(dst_file_path, "r", encoding="utf-8"):
                    row = line.split(":", 1)  # Split only at the first colon

                    if len(row) == 2:
                        destKeys[row[0].strip()] = row[
                            1
                        ].rstrip()  # Clean key and value

                # Add missing keys
                for key, value in srcKeys.items():
                    if key not in destKeys:
                        # Check if the file ends with a newline character
                        with open(dst_file_path, "rb+") as file:
                            file.seek(-1, os.SEEK_END)
                            last_char = file.read(1)

                            # If no newline is found, add one
                            if last_char != b"\n":
                                file.write(b"\n")

                        # Add a space at the beginning of the line and write the line
                        with open(dst_file_path, "a", encoding="utf-8") as file:
                            line_to_write = f" {key}:{value}\n"
                            file.write(line_to_write)

                        logging.info(f"Added key: {key}")


def main():
    update("D:/Steam/steamapps/common/Hearts of Iron IV/localisation/english")


if __name__ == "__main__":
    main()
