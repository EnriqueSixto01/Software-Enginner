'''********************************** DICTIONARY ******************************************'''
citas = [
    {
        "fecha": "01/09/2021",
        "paciente": "Enrique Sixto",
        "medico": "Dra. Mariana",
        "cosultorio": 23,
        "consultorio":25
    },
    {
        "fecha": "01/09/2021",
        "paciente": "Bruce",
        "medico": "Dra. Mariana",
        "cosultorio": 25
    }   
        ]
#citas[0]["paciente"] = "Jorge"           #Podemos reasignar un nuevo valor a la clave 'paciente' ya existente
#citas[0]["lugar"] = "Hospital General"   #Podemos agregar una nueva clave al diccionario 
#del citas[0]["fecha"]                    #del elimina una clave del diccionario
#print(citas)
print("Medico:", citas[1]["paciente"], sep="\n")
print(citas[0].keys())
citas[0]["Hospital"]="ABC"
print(citas[0])
print(citas[0]["consultorio"])




cognitive_services =[
  {
    "rectangle": {
      "x": 112,
      "y": 711,
      "w": 269,
      "h": 243
    },
    "object": "Bicycle wheel",
    "parent": {
      "object": "Wheel",
      "confidence": 0.775
    },
    "confidence": 0.574
  },
  {
    "rectangle": {
      "x": 566,
      "y": 723,
      "w": 268,
      "h": 243
    },
    "object": "Wheel",
    "confidence": 0.585
  },
  {
    "rectangle": {
      "x": 96,
      "y": 568,
      "w": 759,
      "h": 409
    },
    "object": "bicycle",
    "parent": {
      "object": "cycle",
      "parent": {
        "object": "Land vehicle",
        "parent": {
          "object": "Vehicle",
          "confidence": 0.928
        },
        "confidence": 0.927
      },
      "confidence": 0.923
    },
    "confidence": 0.91
  }
]

#for diccionario in range(len(cognitive_services)):
print(cognitive_services[0]["object"])
