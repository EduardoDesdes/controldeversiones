#!/usr/bin/python

import commands
import string


def accionpepito(files,ruta,bd,ruth,fecha):


    #print "tu archivo es: "+files

    md5 = commands.getoutput('md5sum '+ruta+files+' | cut -d" " -f 1')

    #log = "5a38a618091e56f9f3d5cc14b22df46d"
    log = commands.getoutput('cat '+bd+' | grep '+files+'$ | cut -d " " -f 1')
    
    if log != "":
        #print "su hash es: "+md5

        #commands.getoutput('cp '+ruta+files+' .conf/'+files)

        if md5 != log:
            #print "debes  cambiarlo e.e"
            
            #commands.getoutput('cp .conf/'+files+' .conf/.'+files+'_'+fecha)
            a = "cp "+ruth+files+" "+ruth+files+"."+fecha
            print a
            #print "holaaa"+fecha+"holaaa"
            #commands.getoutput("cp .conf/lolsito .conf/.lolsito:marago2813:27:32-052018")
            print "Iniciando copia"
            commands.getoutput(a) 
            print "terminando copia"
            print "Iniciando copia"
            commands.getoutput('cp '+ruta+files+' '+ruth+files)
            print "terminando copia"
            commands.getoutput("sed -i \'s/"+log+"  "+files+"/"+md5+"  "+files+"/g\' "+bd)
            
            print  "Archivo guardado y actualizado e.e"
            #print bd

        #else:
            #print "El archivo es el mismo no seas boludo >:v"
    else:
        #print "comando ejecutado: "+'cp '+ruta+files+' '+ruth+files
        commands.getoutput('mkdir -p `dirname '+ruth+files+'` && cp '+ruta+files+' '+ruth+files)
        commands.getoutput('echo "'+md5+'  '+files+'" >> '+bd)

        #print "Se guardo "+files+" en la DB :3"
        
def validando(destino,config,ruth,bd):
    if commands.getstatusoutput('cd '+destino)[0]:
        #Si no existe el directorio
        commands.getoutput('mkdir '+destino)
    if commands.getstatusoutput('cd '+config)[0]:
        #Si no existe el directorio
        commands.getoutput('mkdir '+config)
    if commands.getstatusoutput('cd '+ruth)[0]:
        #Si no existe el directorio
        commands.getoutput('mkdir '+ruth)
    if commands.getstatusoutput('cat '+bd)[0]:
        #Si no existe el archivo
        commands.getoutput('touch '+bd)


def obtenerfile(unidad):
    ruta = "test/"
    destino = "/media/desdes/"+unidad+"/BK"
    config = destino+"/.CONF"
    ruth= destino+"/DATA/"
    bd= config+"/list"
    validando(destino,config,ruth,bd)
    #obteniendo archivos
    #files = commands.getoutput('ls '+ruta) #un archivo feo
    #print "logrodefinir"
    lista = commands.getoutput('find test/ -type f | cut -d "/" -f 2-999') #lista de archivos
    #print "logrobuscar"
    #obteniendo fecha de ejecucion
    fecha = commands.getoutput('date +"%F_%H_%M_%S"|sed s/-/_/ | sed s/-/_/')
    #print "logroobtenerfecha"    
    lista = lista.split("\n")

    #print "entrando al bucle"
    for i in range(0,len(lista)):
        accionpepito(lista[i],ruta,bd,ruth,fecha)


    

