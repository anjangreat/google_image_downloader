from PIL import Image
from landingai.predict import Predictor
import matplotlib.pyplot as plt
# Enter your API Key
endpoint_id = "790b22b9-766f-4c75-ad60-8973d991ed07"#input your id via landing ai
api_key = "land_sk_UK6FBb7OR5lNMLyjPHN6vYefEnebrnBHMFYaWCVfPK5WxZBZpV"#input your key 
img = ["download (1).jpeg"]#input image paths 

for i in range(0,n):
    image = Image.open(img[i])
    predictor = Predictor(endpoint_id, api_key=api_key)
    predictions = predictor.predict(image)
    print('Image- ',img[i])
    print(predictions) 
    plt.show(image)