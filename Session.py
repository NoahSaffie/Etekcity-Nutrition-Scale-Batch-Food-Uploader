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
        nutrition_info = None
        try:
            nutrition_info = NutritionInfo(data['foodname'], data)
        except:
            print('Got an invalid response')
            print('Request (getFood): ' + str(json.dumps(PARAMS))) 
            print('Response (getFood): ' + str(data))
            return None
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
        try:
            foodList = data['myFoodListResponses']
        except:
            print('Got an invalid response')
            print('Request (getFoodList): ' + str(json.dumps(PARAMS))) 
            print('Response (getFoodList): ' + str(data))
            return False
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
        try:
            return bool(data['editSuccess'])
        except:
            print('Got an invalid response')
            print('Request (editFood): ' + str(json.dumps(PARAMS))) 
            print('Response (editFood): ' + str(data))
            return False

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
        try:
            return bool(data['foodNameExist'])
        except:
            print('Got an invalid response')
            print('Request (searchFood): ' + str(json.dumps(PARAMS))) 
            print('Response (searchFood): ' + str(data))
            return False

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
        try:
            return bool(data['createSuccess'])
        except:
            print('Got an invalid response')
            print('Request (createFood): ' + str(json.dumps(PARAMS))) 
            print('Response (createFood): ' + str(data))
            return False
    
    def deleteFood(self, food_id):
        URL = self.BASE_URL + 'deletemyFood/'
        # defining a params dict for the parameters to be sent to the API 
        PARAMS = self.baseBody()
        PARAMS['foodID'] = food_id
        # sending get request and saving the response as response object 
        response = requests.delete(url = URL, data = json.dumps(PARAMS), headers = {'Content-Type': 'application/json'})
  
        # extracting data in json format 
        data = response.json()
        try:
            return bool(data['deleteSuccess'])
        except:
            print('Got an invalid response')
            print('Request (deleteFood): ' + str(json.dumps(PARAMS))) 
            print('Response (deleteFood): ' + str(data))
            return False
