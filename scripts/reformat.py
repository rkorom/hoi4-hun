import os


def reformat_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()

            # Reformat lines
            reformatted_lines = []
            for i, line in enumerate(lines):
                # Replace 'ő' with 'õ'
                line = line.replace(
                    "ő", "õ"
                ).strip()  # Strip removes any leading/trailing whitespace

                if line:  # Check if the line is not empty after stripping
                    if i == 0:
                        # First line with no leading space
                        reformatted_lines.append(line)
                    else:
                        # Other lines with one leading space
                        reformatted_lines.append(f" {line}")

            # Write back the reformatted lines
            with open(file_path, "w", encoding="utf-8") as file:
                file.writelines(line + "\n" for line in reformatted_lines)

            print(f"Reformatted: {filename}")


def main():
    target_directory = os.path.join(os.getcwd(), "content", "localisation", "replace")
    reformat_files(target_directory)


if __name__ == "__main__":
    main()
