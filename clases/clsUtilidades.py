#-------------------------------------------------------------------------------
# Name:        clsUtilidades
# Purpose:     utiliddades para cualquier programa
#
# Author:      Rene Ulloa
#
# Created:     30/09/2011
# Copyright:   (c) Rene Ulloa 2011
# Licence:     GPL
#-------------------------------------------------------------------------------
#!/usr/bin/env python

class clsUtil:
    def leerCFG(self, dir_cfg):
        datos=[]

        f = open(dir_cfg)

        for lineas in f.readlines():
            if lineas.find("#") < 0:
                linea = lineas.split("=")
                datos.append(linea[0].strip() + "|" + linea[1].strip())

        return datos

