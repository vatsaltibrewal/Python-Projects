import os

def organize_Images(baseName, ext, folderName):
    for index, file in enumerate(os.listdir(folderName), start=1):
        fullPath =  os.path.join(folderName, file)

        if os.path.isfile(fullPath):
            newfileName = f"{baseName}{index}.{ext}"
            newFullPath = os.path.join(folderName, newfileName)
            os.rename(fullPath, newFullPath)
            print(f"Renamed : {file} -> {newfileName}")

        

if __name__ == "__main__":
    baseName = input("Enter Base Name for File : ")
    ext = input("Enter Image Extention : ")
    folder = input("Enter the folder path or leave blank: ").strip()
    folder = folder or os.getcwd()
    if not os.path.isdir(folder):
        print("Invalid directory")
    else:
        organize_Images(baseName, ext, folder)
        print("✅ Renaming completed")