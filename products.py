#Importando librerias a ocupar
from bs4 import BeautifulSoup
import json
import re
import requests

#Guardando url de la pagina solicitada
url = "https://www.farmalisto.com.mx/2158-productos-masculinos"

#Creando objeto Response con la información del sitio 
pag = requests.get(url)
pagina = pag.text

#Creando objeto soup y le pasamos lo solicitado por requests
soup = BeautifulSoup(pagina, 'lxml')

#Solicitando a la pagina el número de productos mostrados
productos = soup.find_all("li", class_="grid_4")


#Obteniendo el precio de cada producto
precios = soup.find_all("span", class_="pricee")

#Obteniendo el nombre de cada producto
nombres = soup.find_all("div", class_="name_product_search")
	
#Obteninedo la url de cada producto
URL = soup.find_all("a", class_="product_img_link")

#Obteniendo la url de cada imagen
imagelink = soup.find_all(src=re.compile("home_default"))

#Obteniendo el Identificador de cada producto
id_products = soup.find_all(rel=re.compile("id_product"))

#Creando lista de productos con diccionarios 'producto'
producto = {}
Lista_productos = []
for i in range(len(productos)):
	precio = re.search('\d\d.\d\d', precios[i].get_text())
	producto['precio'] = precio.group()
	producto['nombre'] = nombres[i].get_text()
	producto['URL'] = URL[i].get('href')
	producto['URL Imagen'] = imagelink[i].get('src')
	for j in range(len(id_products)):
		if(nombres[i].get_text() == id_products[j].get('namepro')):
			producto['Id_producto'] = id_products[j].get('rel')
			break;
	else:
		producto['Id_producto'] = "No tiene id_producto"
	Lista_productos.append(producto)
	producto = {}

#Creando archivo json
with open('products.json','w') as file:
	json.dump(Lista_productos, file)

#Leyendo archivo json
#with open('products.json','r') as file:
	#lista = json.load(file)
#for i in range(len(lista)):
	#print(lista[i])
	#print("\n")


		

