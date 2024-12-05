from Colibri import Colibri
from Cotxe import Cotxe

#Instancia objecte  Colibri
colibri_1 = Colibri(color:"Blau", velocitatAleteig: 200, alimentació:"mosquits", longitud: 23, pic: "llarg")
colibri_2 = Colibri(color:"Groc", velocitatAleteig: 150, alimentació:"fruita", longitud: 16, pic: "llarg")
colibri_3 = Colibri(color:"Verd", velocitatAleteig: 170, alimentació:"mosquits", longitud: 20, pic: "curt")
#Instancia objecte cotxe
cotxe_1 = Cotxe(marca:"Audi", model: "A4", cilindrada: 2000, portes: 5, potencia: 200)
cotxe_2 = Cotxe(marca:"Ford", model: "Focus", cilindrada: 2000, portes: 3, potencia: 110)
cotxe_3 = Cotxe(marca:"Skoda", model: "Fabia", cilindrada: 1500, portes: 5, potencia: 76)

#Mostrem getters de colibri
print(f'El colibri es de color: {colibri_1.getColor()}')
print(f'El colibri menja: {colibri_1.getAlimentacio()}')
print(f'El colibri mou les ales a una velocitat de: {colibri_2.getVelocitatAleteig()} rpm')
print(f'El colibri té una longitud de: {colibri_3.getLongitud()} cm')

#Modifiquem l'atribut color amb set
colibri_1.setColor("Negre")
#i el mostrem amb get
print(colibri_1.getColor())
#Modifiquem l'atribut pic amb set
colibri_2.setPic("curt")
#i el mostrem amb get
print(colibri_2.getPic())


#Mostrem getters de cotxe
print(f'Venc un cotxe de la marca {cotxe_1.getMarca()}')
print(f'el meu cotxe té una potencia de {cotxe_2.getPotencia()} cavalls')
print(f'El teu cotxe té {cotxe_3.getPortes()}')
#Modifiquem l'atribut color amb set
cotxe_2.setMarca("Toyota")
#i el mostrem amb get
print(cotxe_2.getMarca())
#Modifiquem l'atribut pic amb set
cotxe_3.setPotenica(115)
#i el mostrem amb get
print(cotxe_3.getPotenica())



