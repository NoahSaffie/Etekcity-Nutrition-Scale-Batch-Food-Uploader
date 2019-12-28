import requests
from random import randint
import json
from NutritionInfo import NutritionInfo

class Session:
    def __init__(self, token=None, accountid=None):
        self.BASE_URL = 'https://smartapi.vesync.com/nutritionScale-ESN00/v1/myFood/'
        self.TOKEN = token
        self.accountid = accountid

    def baseBody(self):
        body = {'token': self.TOKEN, 'accountID': self.accountid}
        return body

    def getFood(self, food_id):
        URL = self.BASE_URL + 'getmyFood/'
        PARAMS = self.baseBody()
        PARAMS['foodID'] = food_id
        # sending get request and saving the response as response object 
        response = requests.post(url = URL, data = json.dumps(PARAMS), headers = {'Content-Type': 'application/json'})
  
        # extracting data in json format 
        data = response.json()
        nutrition_info = NutritionInfo(data['foodname'], data)
        return nutrition_info
 
    def getFoodList(self):
        URL = self.BASE_URL + 'myFoodList/'
        # defining a params dict for the parameters to be sent to the API 
        PARAMS = self.baseBody()
        PARAMS['page'] = '1'
        PARAMS['pagesize'] = '1000' 
        # sending get request and saving the response as response object 
        response = requests.post(url = URL, data = json.dumps(PARAMS), headers = {'Content-Type': 'application/json'})
  
        # extracting data in json format 
        data = response.json()
        foodList = data['myFoodListResponses']
        foodList = list(map(lambda x: x['foodID'], foodList))
        return foodList

    def editFood(self, food_id, nutrition_info):
        URL = self.BASE_URL + 'editemyFood/'
        # defining a params dict for the parameters to be sent to the API 
        PARAMS = self.baseBody()
        PARAMS.update(nutrition_info.data)
        PARAMS['foodID'] = food_id
        PARAMS['weightunit'] = PARAMS['weight_unit']
        #print(json.dumps(PARAMS))
        # sending get request and saving the response as response object 
        response = requests.put(url = URL, data = json.dumps(PARAMS), headers = {'Content-Type': 'application/json'})
  
        # extracting data in json format 
        data = response.json()
        #print(data)
        return bool(data['editSuccess'])

    def searchFood(self, search_criteria):
        URL = self.BASE_URL + 'searchFoodName/'
        # defining a params dict for the parameters to be sent to the API 
        PARAMS = self.baseBody()
        PARAMS['foodName'] = str(search_criteria)
        PARAMS['foodID'] = "" 
        # sending get request and saving the response as response object 
        response = requests.post(url = URL, data = json.dumps(PARAMS), headers = {'Content-Type': 'application/json'})
  
        # extracting data in json format 
        data = response.json() 
        return bool(data['foodNameExist'])

    def createFood(self, nutrition_info):
        URL = self.BASE_URL + 'createmyFood/'
        # defining a params dict for the parameters to be sent to the API 
        PARAMS = self.baseBody()
        PARAMS.update(nutrition_info.data)
        #print(PARAMS)
        # sending get request and saving the response as response object 
        response = requests.post(url = URL, data = json.dumps(PARAMS), headers = {'Content-Type': 'application/json'})
  
        # extracting data in json format 
        data = response.json()
        #print(data)
        return bool(data['createSuccess'])

    
    def deleteFood(self, food_id):
        URL = self.BASE_URL + 'deletemyFood/'
        # defining a params dict for the parameters to be sent to the API 
        PARAMS = self.baseBody()
        PARAMS['foodID'] = food_id
        # sending get request and saving the response as response object 
        response = requests.delete(url = URL, data = json.dumps(PARAMS), headers = {'Content-Type': 'application/json'})
  
        # extracting data in json format 
        data = response.json()
        return bool(data['deleteSuccess'])
