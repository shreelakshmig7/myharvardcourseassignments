def identifyType(fileName):
    fileExt = fileName.rsplit(".", maxsplit=1)
    if len(fileExt) == 1:
        return "application/octet-stream"
    else:
        match fileExt[1]:
            case "gif" | "png":
                return ("image/"+fileExt[1])
            case "jpg" | "jpeg":
                return "image/jpeg"
            case "txt":
                return "text/plain"
            case "pdf":
                return "application/pdf"
            case "zip":
                return "application/zip"
            case _:
                return "application/octet-stream"


def main():
    fileName = input("Filename: ").strip().lower()
    mimeType = identifyType(fileName)
    print(mimeType)


main()
