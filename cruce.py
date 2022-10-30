#-------------------------------------------------------------------------------
# Name:        cruce
# Purpose:     realiza el cruce de un archivo
#
# Author:      Rene Ulloa
#
# Created:     29/09/2011
# Copyright:   (c) chechex 2011
# Licence:     GPL
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sys

sys.path.append("./clases")
from clsCruce import clsCruce

def main():
    c = clsCruce("cruce.cfg")
    archs = c.ArchivosaCruzar()

    if(len(archs) > 0):
        print "archivos a procesar:\n"
        for a in archs:
            print "\t -" ,a

        resp = raw_input("Desea procesar los archivos [S/N]")
        if(resp == "S" or resp == "s"):
            print "procesando..."
            c.LeeArchivos(archs)
            print "\n\n"
            c.DatosCruce()
        else:
            resp = raw_input("Desea buscar nuevamente los archivos [S/N]")
            if(resp == "S" or resp == "s"):
                resp = ""
                main()
            else:
                print "saliendo..."
    else:
        print("No existen archivos para procesar.")

if __name__ == "__main__":
    main()