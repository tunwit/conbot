from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def root():
    return {'status':'ok'}


//*[@id="uMap2Map22"]/area[1]