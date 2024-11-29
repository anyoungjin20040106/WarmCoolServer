from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from tensorflow.keras.models import load_model
import numpy as np
from io import BytesIO
from PIL import Image
import numpy as np
import sqlite3
import pandas as pd
con=sqlite3.Connection('data.db')

app=FastAPI()
model=load_model('model.keras')
with open("labels.txt") as f:
    labels=f.readlines()
app.mount('img',StaticFiles(directory='./img'))
@app.post("/predict")
async def predict(img:UploadFile=File(...)):
    contents = await img.read()
    image = Image.open(BytesIO(contents)).convert("RGB")
    image = image.resize((224, 224)) 
    img_array = np.array(image) / 255.0  
    img_array = np.expand_dims(img_array, axis=0) 
    result = model.predict(img_array)
    df=pd.read_sql("select * from Tone where name=?",con,params=(labels[np.argmax(result)]))
    return dict(zip(df.columns,df.values[0]))    
    