import os

destDir = os.path.join(os.getcwd(), "content", "localisation", "replace")


def update(
    srcDir, destDir=os.path.join(os.getcwd(), "content", "localisation", "replace")
):
    for filename in os.listdir(srcDir):

        srcKeys, destKeys = dict(), dict()
        src_file_path = os.path.join(srcDir, filename)
        dst_file_path = os.path.join(destDir, filename)

        if os.path.isfile(src_file_path) and os.path.isfile(dst_file_path):
            for line in open(src_file_path, "r", encoding="utf-8"):
                row = line.split(":")

                try:
                    srcKeys[row[0]] = row[1]
                except:
                    pass

            for line in open(dst_file_path, "r", encoding="utf-8"):
                row = line.split(":")

                try:
                    destKeys[row[0]] = row[1]
                except:
                    pass

            # Add missing keys
            for key, value in srcKeys.items():
                if key not in destKeys:
                    with open(dst_file_path, "a", encoding="utf-8") as file:
                        file.write(f"{key}:{value}")


update("D:/Steam/steamapps/common/Hearts of Iron IV/localisation/english")
