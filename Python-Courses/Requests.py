import requests                     #La libreria requests nos permite enviar una solicitud a traves del ptotocolo http
url = "https://google.com/"
g = requests.get(url)               #Para enviar una solicitud usamos el metodo .get()
print(g)

print(g.status_code)                #Podemos ver el estado de la solicitud usando el atributo .satus_code
print(g.request.body)               #Con .requests.body vemos la solicitud del cuerpo

header = g.headers                  #Con el atributo .headers podemos ver la respuesta a la solicitud http enviada
print(header)
print(g.text[0:100])                #Con .text() podemos observar el cuerpo del archivo html

