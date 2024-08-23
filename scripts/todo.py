import os
import csv


def check_translation(srcDir, destDir, output_file="todo.csv"):
    to_translate = []

    for filename in os.listdir(srcDir):
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
                        srcKeys[row[0].strip()] = row[1].strip()  # Clean key and value

            # Read the destination file
            with open(dst_file_path, "r", encoding="utf-8") as dst_file:
                for i, line in enumerate(dst_file):
                    if i == 0:
                        continue  # Skip the first line
                    row = line.split(":", 1)  # Split only at the first colon
                    if len(row) == 2:
                        destKeys[row[0].strip()] = row[1].strip()  # Clean key and value

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
    check_translation(src_directory, dest_directory)


if __name__ == "__main__":
    main()
