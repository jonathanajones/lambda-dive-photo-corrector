from pydantic import BaseModel


class DataResponse(BaseModel):
    imageType: str
    imageData: str


class ColorCorrectorResponse(BaseModel):
    statusCode: int
    data: DataResponse
