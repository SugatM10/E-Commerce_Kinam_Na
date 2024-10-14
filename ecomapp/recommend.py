import pickle
import pandas as pd


product_dict = pickle.load(open('product_dict.pkl','rb'))
products = pd.DataFrame(product_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(product):
    product_index = products[products['product_title'] == product].index[0]
    distances = similarity[product_index]
    product_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
    
    recommended_products= []

    for i in product_list:
       recommended_products.append(products.iloc[i[0]].product_title)
    return recommended_products