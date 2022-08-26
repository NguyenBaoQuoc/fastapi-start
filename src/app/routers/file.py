from fastapi import APIRouter, status, File, UploadFile, Depends
from middleware.auth import is_autheticated
import aiofiles

routerFile = APIRouter(
    prefix="/api/file",
    tags=["file"]
)


@routerFile.post("/files", status_code=status.HTTP_200_OK)
async def create_file(user_id: int = Depends(is_autheticated), file: bytes = File()):
    return {"file_size": len(file)}


@routerFile.post("/uploadfile", status_code=status.HTTP_200_OK)
async def create_upload_file(file: UploadFile, user_id: int = Depends(is_autheticated)):
    if not file:
        return {"message": "No upload file sent"}
    else:
        print("filename = ", file.filename)  # getting filename
        destination_file_path = "images/" + file.filename  # location to store file
        async with aiofiles.open(destination_file_path, 'wb') as out_file:
            while content := await file.read(1024):  # async read file chunk
                await out_file.write(content)  # async write file chunk
        return {"Result": "OK", "filename": file.filename, "user_id": user_id}


