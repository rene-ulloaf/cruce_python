#-------------------------------------------------------------------------------
# Name:        clsCruce
# Purpose:     clase que realiza el cruce de un archivo
#
# Author:      Rene Ulloa
#
# Created:     29/09/2011
# Copyright:   (c) chechex 2011
# Licence:     GPL
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import os
import datetime
import time
import shutil

from clsUtilidades import clsUtil

class clsCruce:
    __companias=[]
    __dir_procesar = ""
    __dir_procesados = ""
    __dir_cruce = ""
    __fecha_format = ""
    __fecha_com_format = ""
    __cant_procesos = 0
    __cant_procesados = 0
    __cant_err = 0

    def __init__(self,dir_cfg):
        self.__U = clsUtil()
        self.__DatosCFG(dir_cfg)

        fecha = datetime.date.today()
        fecha_com = datetime.datetime.today()

        self.__fecha_format =  fecha.strftime("%Y%m%d")
        self.__fecha_com_format = fecha_com.strftime("%Y%m%d%H%M%S")

        self.__cant_procesos=0
        self.__cant_procesados=0
        self.__cant_err = 0

    def ArchivosaCruzar(self):
        arch=[]
        archs = os.listdir(self.__dir_procesar)

        for f in archs:
            if os.path.isfile(os.path.join(self.__dir_procesar,f)):
                print(os.path.splitext(f)[1])

                if os.path.splitext(f)[1] == ".txt":
                    arch.append(f)
        return arch

    def LeeArchivos(self,archivos):
        for a in archivos:
            ruta = os.path.join(self.__dir_cruce,os.path.splitext(a)[0] + "_" + self.__fecha_format)
            if not os.path.isdir(ruta):
                os.mkdir(ruta)

            #self.fil_entel = os.path.splitext(a)[0] + "_entel_" + self.fecha_format + os.path.splitext(a)[1]
            #self.fil_movistar = os.path.splitext(a)[0] + "_movistar_" + self.fecha_format + os.path.splitext(a)[1]
            #self.fil_claro = os.path.splitext(a)[0] + "_claro_" + self.fecha_format + os.path.splitext(a)[1]
            #self.fil_error = os.path.splitext(a)[0] + "_error_" + self.fecha_format + os.path.splitext(a)[1]

            nuevo_arch = self.__CopiaArchProc(a)
            f = open(os.path.join(self.__dir_procesados,nuevo_arch))

            for lineas in f.readlines():
                self.__cant_procesos += 1
                datos = lineas
                d = datos.split(";")

                if len(d) == 6:
                    resp = self.Cruce(ruta,d[1],d[2],d[3],d[4],d[5])

                    if resp == False:
                        self.__cant_err += 1
                    else:
                        self.__cant_procesados += 1
                else:
                    self.cant_err += 1
                    #guardaerror

    def Cruce(self,ruta,cia,nro,monto,lugar,fecha):
        ret = True

        if self.__companias.index(cia) > 0:
            f = open(os.path.join(ruta,cia + "_" + self.__fecha_com_format + ".txt"),"a")
            datos = cia + ";" + nro + ";" + monto + ";" + lugar + ";" +fecha
            f.write(datos)
            f.close()
        else:
            ret = False

        #if cia == "entel":
        #    f = open(os.path.join(self.dir_cruce,self.fil_entel),"a")
        #elif cia == "movistar":
        #    f = open(os.path.join(self.dir_cruce,self.fil_movistar),"a")
        #elif cia == "claro" :
        #    f = open(os.path.join(self.dir_cruce,self.fil_claro),"a")
        #else:
        #    ret=False

        return ret

    def __CopiaArchProc(self,arch):
        aux = True
        proc = 1

        while aux == True:
            if proc < 10:
                proceso = "0" + str(proc)
            else:
                proceso = str(proc)

            nuevo_nombre = os.path.splitext(arch)[0] + "_proc" + proceso + os.path.splitext(arch)[1]

            if os.path.isfile(os.path.join(self.__dir_procesados,nuevo_nombre)) == True:
                proc += 1
            else:
                aux = False

        shutil.copy2(os.path.join(self.__dir_procesar,arch),os.path.join(self.__dir_procesados,nuevo_nombre))
        os.remove(os.path.join(self.__dir_procesar,arch))

        return nuevo_nombre

    def DatosCruce(self):
        print "Detalle Cruce:\n"
        print "cantidad de datos a procesar: ", self.__cant_procesos
        print "\ncantidad de datos a procesados: ", self.__cant_procesados
        print "\ncantidad de datos erroneos: ", self.__cant_err

    def __DatosCFG(self,dir_cfg):
        datos=[]
        datos = self.__U.leerCFG(dir_cfg)

        for dat in datos:
            d = dat.split("|")

            if d[0] == "cfg_companias":
                self.__companias = d[1].split(",")

            if d[0] == "cfg_dir_procesar":
                self.__dir_procesar = d[1]

            if d[0] == "cfg_dir_procesados":
                self.__dir_procesados = d[1]

            if d[0] == "cfg_dir_cruce":
                self.__dir_cruce = d[1]