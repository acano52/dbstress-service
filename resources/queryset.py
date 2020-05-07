#------------------------------------------------------------------------------
# Copyright (c) 2016, 2019, Tedial S.L  All rights reserved.
#------------------------------------------------------------------------------
from flask_restful import Api, Resource, reqparse
from utils         import utils

#@app.route('/')
class rac(Resource):

       def get(self):
    
        racstatus = {}
  
        logShowConfiguration=""
        conf  = utils.configuration()

        print("Input:")
        



        dbUri = conf[0]
        r = utils.checkRac(dbUri)
        output_command1 = r[0]   # crsctl status res -t -w "TYPE != ora.ocj4"



         
        _raclog           =  output_command1[0]
        x = _raclog.split('\n')
        
        for line in x:
            if line.find("ora.") >= 0:
               _name = line.strip() 
               r2= r = utils.checkRac
  

            if line.find("Physical standby database") >= 0:
               _standbydatabase = line.split('-')[0].strip()                

            if line.find("SUCCESS") >= 0:
               _dataguardstatus = 'SUCCESS' 
        
        _raclog           =  output_command1[0]
        
        racstatus = { 
                        "name": 
                              [
                                   {        "name":               "1",
                                            "target":             "2",
                                            "state":              "3",
                                            "state_details":      "4"
                                     },    
                                     {
                                            "id":                 "0002",
	                                        "rol":                "PHYSICAL STANDBY",
	                                        "log":                _raclog
                                      }    
                               ] ,            
                       "raclog":  "OK"
        }
 
        return racstatus , 200
 





