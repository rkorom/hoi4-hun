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
                line = line.replace("ő", "õ")

                # Remove leading and trailing whitespaces
                line = line.strip()

                # Ensure the first line has no leading spaces
                if i == 0:
                    reformatted_lines.append(f"{line}\n")
                else:
                    # Ensure all other lines have exactly 2 leading spaces
                    reformatted_lines.append(f" {line}\n")

            # Write back the reformatted lines
            with open(file_path, "w", encoding="utf-8") as file:
                file.writelines(reformatted_lines)

            print(f"Reformatted: {filename}")


def main():
    target_directory = os.path.join(
        os.getcwd(), "src", "content", "localisation", "replace"
    )
    reformat_files(target_directory)


if __name__ == "__main__":
    main()
