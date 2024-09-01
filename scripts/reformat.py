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

                reformatted_lines.append(line)

            # Write back the reformatted lines
            with open(file_path, "w", encoding="utf-8") as file:
                file.writelines(reformatted_lines)

            print(f"Reformatted: {filename}")


def main():
    target_directory = os.path.join(os.getcwd(), "src", "content", "localisation", "replace")
    reformat_files(target_directory)


if __name__ == "__main__":
    main()
