import facebook


def main():
	graph = facebook.GraphAPI(access_token='pega aqui tu token generado')
	
	#Publicar una foto
	graph.put_photo(image = open ('imagen.png', 'rb'), message = 'Mira esta foto!')

if __name__ == "__main__":
	main()
