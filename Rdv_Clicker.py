#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
ButtonSuivant = """document.getElementsByClassName("Bbutton")[0].click();"""

ErrorReact = """var ErrorGateWay = document.getElementsByTagName("h1")[0];
                if (ErrorGateWay != undefined && (ErrorGateWay.firstChild.data == "502 Bad Gateway" || ErrorGateWay.firstChild.data == "Error 503 Service Unavailable") || ErrorGateWay.firstChild.data.substring("504")) {
                    location.reload();
                }"""

Page_1 = """document.getElementsByClassName("jqTransformCheckbox")[0].className = "jqTransformCheckbox jqTransformChecked";
            document.getElementById("condition").click();
            document.getElementsByClassName("Bbutton")[0].click();""" + ButtonSuivant
Page_2 = """var choice = Math.floor(Math.random() * 4);
            switch (choice) {
                case 0:
                case 1:
                    if (document.getElementById("planning4220").checked != true) {
                        document.getElementById("planning4220").click(); //1
                    }
                    break;

                case 2:
                case 3:
                    if (document.getElementById("planning7351").checked != true) {
                        document.getElementById("planning7351").click(); //4
                    }
                    break;

                default:
                    console.log("Fatal error in page 2 !!!");
                    return false;
                    //clearInterval(t);
                    break;
            }
            """ + ButtonSuivant

Page_3_4 = ErrorReact + ButtonSuivant

Get_Rdv = """alert("Rdv !!!!!!!!!!!!!!!!!!!!\\n
                Rdv !!!!!!!!!!!!!!!!!!!!\\n
                Rdv !!!!!!!!!!!!!!!!!!!!")"""

driver.get("http://www.hauts-de-seine.gouv.fr/booking/create/4129/0")
actualUrl = driver.current_url
swithcer = {
            "http://www.hauts-de-seine.gouv.fr/booking/create/4129/0" : 1,
            "http://www.hauts-de-seine.gouv.fr/booking/create/4129/0#" : 1,
            "http://www.hauts-de-seine.gouv.fr/booking/create/4129/1" : 2,
            "http://www.hauts-de-seine.gouv.fr/booking/create/4129/2" : 3,
            "http://www.hauts-de-seine.gouv.fr/booking/create/4129/3" : 4,
            # "http://www.hauts-de-seine.gouv.fr/booking/create/4129/4" : 5
            }

# If we dom't get the Rdv, continue
while actualUrl != "http://www.hauts-de-seine.gouv.fr/booking/create/4129/4":
    Page_index = swithcer[actualUrl]
    try:
        if Page_index == None:
            driver.execute_script("alert(!!!!!!!!!!!!!!!!!!Error!!!!!!!!!!!!!!!!!!)")
            sleep(1.0)
            driver.execute_script("location.reload()")
        else:
            # home page
            if Page_index == 1:
                driver.execute_script(Page_1)
            # choices page
            elif Page_index == 2:
                driver.execute_script(Page_2)
            # no available agenda
            elif Page_index == 3:
                driver.execute_script(Page_3_4)
            # Page of confirmation
            elif Page_index == 4:
                driver.execute_script(Page_3_4)
            # get the new url
            sleep(0.5)
            actualUrl = driver.current_url
    except:
        raise
else:
    driver.execute_script(Get_Rdv)
    # driver.close()
