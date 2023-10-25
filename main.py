from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

import shutil

# Tạo một ứng dụng FastAPI
fastapi_app = FastAPI()

# Define Pydantic model
class TextContent(BaseModel):
    background: dict
    logo: dict
    dong_1: dict
    dong_2: dict
    dong_3: dict

@fastapi_app.post('/upload')
async def upload(file: UploadFile = File(...)):
    with open(file.filename, 'wb') as f:
        shutil.copyfileobj(file.file, f)
    return {"path": file.filename}

# Endpoint để cập nhật văn bản
@fastapi_app.post("/update_text")
async def update_text(text_content: TextContent):
    config = dict(text_content)

    MainWindow.setStyleSheet(f"background-image: url({config['background']['path']});")
    ui.logo.setPixmap(QtGui.QPixmap(config['logo']['path']))

    ui.dong_1.setText(config['dong_1']['text'])
    ui.dong_1.setStyleSheet(f"background: {config['dong_1']['background']}; color: {config['dong_1']['color']};")

    ui.dong_2.setText(config['dong_2']['text'])
    ui.dong_2.setStyleSheet(f"background: {config['dong_2']['background']}; color: {config['dong_2']['color']};")

    ui.dong_3.setText(config['dong_3']['text'])
    ui.dong_3.setStyleSheet(f"background: {config['dong_3']['background']}; color: {config['dong_3']['color']};")

    ui.logo.repaint()
    ui.dong_1.repaint()
    ui.dong_2.repaint()
    ui.dong_3.repaint()
    return {"message": "Nội dung đã được cập nhật"}

if __name__ == "__main__":
    import sys
    from design import Ui_MainWindow  # Thay your_ui_module bằng tên tệp UI của bạn

    # Tạo ứng dụng PyQt5
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    from uvicorn import run

    run(fastapi_app, host="0.0.0.0", port=8008)
