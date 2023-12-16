import os, shutil, pathlib, time

class organizeFiles:

    def __init__(self):
        pass

    def getCurrentDir(self):
        return os.getcwd()

    def getFileList(self):
        directoryPath = input("\nEnter the directory path: ")
        allFiles = None

        try:
            allFiles = [os.path.join(directoryPath, file) for file in os.listdir(directoryPath)
                        if os.path.isfile((os.path.join(directoryPath, file)))]

        except FileNotFoundError:
            print(f"The specified directory '{directoryPath}' does not exist.")
        except PermissionError:
            print(f"Permission error while trying to access '{directoryPath}'.")
        except Exception as e:
            print(f"An error occurred: {e}")

        print("File paths:", allFiles)  # Print the file paths

        return allFiles

    def moveFile(self, allfiles):
        musicExtensions = ['.mp3', '.wav', '.wma', '.aac', '.flac', '.ogg', '.m4a', '.aiff', '.opus']
        pdfExtensions = ['.pdf']
        imageExtensions = ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp', '.svg', '.psd', '.raw', '.eps']
        appExtensions = ['.exe', '.pkg', '.app', '.msi', '.bin', '.dmg']
        archiveExtensions = ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.z']
        videoExtensions = ['.mp4', '.mov', '.flv', '.avi', '.wmv', '.mkv', '.webm', '.vob', '.m4v']
        officeExtensions = ['.docx', '.xlsx', '.pptx', '.pst', '.ost', '.msg', '.doc', '.xls', '.ppt']

        sourceDir = input("\nEnter the source Directory path: ")

        destinationDirs = {
            "music": os.path.join(sourceDir, "music"),
            "pdf": os.path.join(sourceDir, "pdf"),
            "image": os.path.join(sourceDir, "image"),
            "application": os.path.join(sourceDir, "application"),
            "zip": os.path.join(sourceDir, "zip"),
            "video": os.path.join(sourceDir, "videos"),
            "ms-office": os.path.join(sourceDir, "ms-office")
        }

        for file in allfiles:
            time.sleep(0.25)

            filePath = os.path.abspath(file)
            fileType = pathlib.Path(file).suffix.lower()

            if fileType in imageExtensions:
                destPath = destinationDirs["image"]
                if os.path.exists(destPath) and os.path.isdir(destPath):
                    shutil.move(filePath, destPath)
                    print(f"Moved file: {file} to folder: {destPath} successfully!")

            elif fileType in musicExtensions:
                destPath = destinationDirs["music"]
                if os.path.exists(destPath) and os.path.isdir(destPath):
                    shutil.move(filePath, destPath)
                    print(f"Moved file: {file} to folder: {destPath} successfully!")

            elif fileType in pdfExtensions:
                destPath = destinationDirs["pdf"]
                if os.path.exists(destPath) and os.path.isdir(destPath):
                    shutil.move(filePath, destPath)
                    print(f"Moved file: {file} to folder: {destPath} successfully!")

            elif fileType in archiveExtensions:
                destPath = destinationDirs["zip"]
                if os.path.exists(destPath) and os.path.isdir(destPath):
                    shutil.move(filePath, destPath)
                    print(f"Moved file: {file} to folder: {destPath} successfully!")

            elif fileType in appExtensions:
                destPath = destinationDirs["application"]
                if os.path.exists(destPath) and os.path.isdir(destPath):
                    shutil.move(filePath, destPath)
                    print(f"Moved file: {file} to folder: {destPath} successfully!")

            elif fileType in videoExtensions:
                destPath = destinationDirs["video"]
                if os.path.exists(destPath) and os.path.isdir(destPath):
                    shutil.move(filePath, destPath)
                    print(f"Moved file: {file} to folder: {destPath} successfully!")

            elif fileType in officeExtensions:
                destPath = destinationDirs["ms-office"]
                if os.path.exists(destPath) and os.path.isdir(destPath):
                    shutil.move(filePath, destPath)
                    print(f"Moved file: {file} to folder: {destPath} successfully!")

            else:
                print(f"File {file} is not moved.")
                continue

def main():
    print("\nWelcome to the file organiser!")
    orgFile = organizeFiles()

    allFiles = orgFile.getFileList()
    orgFile.moveFile(allFiles)


if __name__ == "__main__":
    main()