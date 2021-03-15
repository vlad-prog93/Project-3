
class Product:
    def __init__(self, title, calorific, cost):
        self.title = title
        if not Product.check_calorific(calorific):
            raise ValueError ('Не верно ввели каллорийность продукта')
        self.calorific = calorific  
        if not Product.check_cost(cost):
            raise ValueError ('Не верно ввели стоимость продукта')
        self.cost = cost
        
    @staticmethod
    def check_calorific(calorific):
        return calorific > 0
    @staticmethod
    def check_cost(cost):
        return cost > 0
    

class Ingredient(Product):
    
    def __init__(self, product, weight):
        if not Ingredient.check_weight(weight):
            raise ValueError ('Не верно ввели вес продукта')
        self.product = product
        self.weight = weight
            
    @staticmethod
    def check_weight(weight):
        return weight > 0

    def calorific_all(self):
        calorific = self.weight / 100 * self.product.calorific
        return calorific
    def cost_all(self):
        cost = self.weight / 100 * self.product.cost
        return cost

class Pizza(Ingredient):
    def __init__(self, title, ingredients):
        if not Pizza.check_ingredients(ingredients):
            raise ValueError ('не верно задан ингредиент')
        self.title = title
        self.ingredients = ingredients
    
    @property
    def sum_calorific(self):
        summa = 0
        for ingred in self.ingredients:
            summa += ingred.calorific_all()
        return summa
    @property
    def sum_cost(self):
        summa = 0
        for ingred in self.ingredients:
            summa += ingred.cost_all()
        return summa
          
    @staticmethod       
    def check_ingredients(ingredients):
        for i in range(0, len(ingredients)):
            return isinstance(ingredients[i], Ingredient)

    def __str__(self):
        return f'{self.title} ({self.sum_calorific}) - {self.sum_cost}'
                
# Создаем продукты с указанием названия, калорийности продукта и его себестоимости
dough_product = Product('Тесто', 200, 20)
tomato_product = Product('Помидор', 100, 50)
cheese_product = Product('Сыр', 100, 120)

# Из продуктов создаем ингредиенты. Для каждого ингредиента указываем продукт, 
# из которого он состоит и вес продукта
dough_ingredient = Ingredient(dough_product, 100)
tomato_ingredient = Ingredient(tomato_product, 100)
cheese_ingredient = Ingredient(cheese_product, 100)

# Из ингредиентов создаем пиццу
pizza_margarita = Pizza('Маргарита', [dough_ingredient, tomato_ingredient, cheese_ingredient])

# Выводим экземпляр пиццы
print(pizza_margarita)