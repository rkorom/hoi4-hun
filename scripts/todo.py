import os
import csv


def check_translation(srcDir, destDir, output_file="todo.csv", ignore_files=None):
    if ignore_files is None:
        ignore_files = []

    to_translate = []

    for filename in os.listdir(srcDir):
        if filename in ignore_files:
            continue  # Skip files that are in the ignore list

        src_file_path = os.path.join(srcDir, filename)
        dst_file_path = os.path.join(destDir, filename)

        if os.path.isfile(src_file_path) and os.path.isfile(dst_file_path):
            srcKeys, destKeys = dict(), dict()

            # Read the source file
            with open(src_file_path, "r", encoding="utf-8") as src_file:
                for i, line in enumerate(src_file):
                    if i == 0:
                        continue  # Skip the first line
                    row = line.split(":", 1)  # Split only at the first colon
                    if len(row) == 2:
                        key = row[0].strip()
                        value = row[1].strip()
                        if not (value.startswith('"$') and value.endswith('$"')):
                            srcKeys[key] = (
                                value  # Clean key and value, and skip if value is surrounded by "$"
                            )

            # Read the destination file
            with open(dst_file_path, "r", encoding="utf-8") as dst_file:
                for i, line in enumerate(dst_file):
                    if i == 0:
                        continue  # Skip the first line
                    row = line.split(":", 1)  # Split only at the first colon
                    if len(row) == 2:
                        key = row[0].strip()
                        value = row[1].strip()
                        if not (value.startswith('"$') and value.endswith('$"')):
                            destKeys[key] = (
                                value  # Clean key and value, and skip if value is surrounded by "$"
                            )

            # Compare keys
            for key, value in srcKeys.items():
                if key in destKeys and destKeys[key] == value:
                    to_translate.append((filename, key))

    # Write to the CSV file
    with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Fájlnév", "Kulcs"])  # Header row
        writer.writerows(to_translate)

    print(f"A fordítandó kulcsok listája a következő fájlban található: {output_file}")


def main():
    src_directory = "D:/Steam/steamapps/common/Hearts of Iron IV/localisation/english"
    dest_directory = os.path.join(os.getcwd(), "content", "localisation", "replace")
    ignore_files = ["aat_characters_l_english.yml"]  # List of files to ignore
    check_translation(src_directory, dest_directory, ignore_files=ignore_files)


if __name__ == "__main__":
    main()
