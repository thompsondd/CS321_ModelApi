from fastapi import FastAPI #import class FastAPI() từ thư viện fastapi

app = FastAPI() # gọi constructor và gán vào biến app

@app.post("/") # giống flask, khai báo phương thức get và url
async def test(): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    # print(f"Text: \n\t{text}")
    return {"message": "Hello World"}

@app.get("/autoLabel/{text}") # giống flask, khai báo phương thức get và url
async def root(text: str): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    print(f"Text: \n\t{text}")
    return {"message": "Hello World"}
