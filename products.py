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

#insertando productos sin boton de compra a la lista id_products
id_products.insert(0, 'No tiene botón de compra')
id_products.insert(5, 'No tiene botón de compra')
id_products.insert(11, 'No tiene botón de compra')
id_products.insert(22, 'No tiene botón de compra')
id_products.insert(29, 'No tiene botón de compra')

#Creando lista de productos con diccionarios 'producto'
producto = {}
Lista_productos = []
for i in range(len(productos)):
	precio = re.search('\d\d.\d\d', precios[i].get_text())
	producto['precio'] = precio.group()
	producto['nombre'] = nombres[i].get_text()
	producto['URL'] = URL[i].get('href')
	producto['URL Imagen'] = imagelink[i].get('src')
	if (i== 0 or i==5 or i==11 or i==22 or i==29):
		producto['id_producto'] = id_products[i]
	else:
		producto['Id_producto'] = id_products[i].get('rel')
	Lista_productos.append(producto)
	producto = {}
	
#Creando archivo json
with open('products.json','w') as file:
	json.dump(Lista_productos, file)

#Leyendo e imprimiendo archivo json
#with open('products.json','r') as file:
	#lista = json.load(file)
#for i in range(len(lista)):
	#print(lista[i])
	#print("\n")


		

