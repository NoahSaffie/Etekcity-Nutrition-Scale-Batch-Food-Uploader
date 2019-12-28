class NutritionInfo:
    def __init__(self, name, data):
        self.foodID = data['foodID']
        self.allowed_cols = ['foodname', 'image', 'weight', 'weight_unit', 'calories', 'calfromfat', 'totalfat', 'saturatedfat', 'transfat', 'fat_poly', 'fat_mono', 'cholesterol', 'sodium', 'totalcarbs', 'dietaryfiber', 'sugars', 'protein', 'va', 'vc', 'vd', 'calcium', 'iron', 'potassium']
        if 'weightunit' in data:
            data['weight_unit'] = data['weightunit']
        self.data = {k: data[k] for k in self.allowed_cols}
        self.calories = data['calories']
        self.foodname = name
        self.image_link = data['image']
        # Serving size
        self.weight = data['weight']
        self.weight_unit = data['weight_unit']
        self.calfromfat = data['calfromfat']
        self.totalfat = data['totalfat']
        self.saturatedfat = data['saturatedfat']
        self.transfat = data['transfat']
        self.fat_poly = data['fat_poly']
        self.fat_mono =data['fat_mono']
        self.cholesterol = data['cholesterol']
        self.sodium = data['sodium']
        self.totalcarbs = data['totalcarbs']
        self.dietaryfiber = data['dietaryfiber']
        self.sugars = data['sugars']
        self.protein = data['protein']
        self.vd = data['vd']
        self.calcium = data['calcium']
        self.iron = data['iron']
        self.potassium = data['potassium']
        self.va = data['va']
        self.vc = data['vc']

    
    def getAsRow(self):
        data = self.data
        return [self.foodID, data['image'], self.foodname, data['weight'], data['weight_unit'], data['calories'], data['calfromfat'], data['totalfat'], data['saturatedfat'], data['transfat'], data['fat_poly'], data['fat_mono'], data['cholesterol'], data['sodium'], data['totalcarbs'], data['dietaryfiber'], data['sugars'], data['protein'], data['vd'], data['calcium'], data['iron'], data['potassium'], data['va'], data['vc']]
        
