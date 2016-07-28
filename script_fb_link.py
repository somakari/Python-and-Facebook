import facebook


def main():
	graph = facebook.GraphAPI(access_token='pega aqui tu token generado')

	attachment = {
		'link': 'http://ejemplo.com'
	}
	
	#Publicar un mensaje con un link
	graph.put_wall_post(message='Hola Mundo!', attachment=attachment)


if __name__ == "__main__":
	main()
