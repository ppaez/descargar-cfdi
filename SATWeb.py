import requests
from HTMLForm import HTMLForm

class SATWeb:
    def __init__(self, rfc, contrasena):
        self.rfc = rfc
        self.contrasena = contrasena
        self.sesion = requests.Session()

    def __entrarAlaPaginaInicio(self):
        url = 'https://cfdiau.sat.gob.mx/nidp/app/login?id=SATUPCFDiCon&sid=0&option=credential&sid=0'
        self.sesion.post(url)

    def __enviarFormularioConCIEC(self):
        url = 'https://cfdiau.sat.gob.mx/nidp/app/login?sid=0&sid=0'
        headers = {
            'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'en-US,en;q=0.5',
            'Connection':'keep-alive',
            'Host':'cfdiau.sat.gob.mx',
            'Referer':'https://cfdiau.sat.gob.mx/nidp/app/login?id=SATUPCFDiCon&sid=0&option=credential&sid=0',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0',
            'Content-Type':'application/x-www-form-urlencoded',
        }
        values = {'option':'credential', 'Ecom_User_ID':self.rfc, 'Ecom_Password':self.contrasena, 'submit':'Enviar'}
        self.sesion.post(url, data=values,headers=headers)

    def __leerFormularioDeRespuesta(self):
        url = 'https://portalcfdi.facturaelectronica.sat.gob.mx/'
        r = self.sesion.get(url)
        htmlSource = r.text
        htmlForm = HTMLForm(htmlSource, 'form')
        inputValues = htmlForm.readAndGetInputValues()

    def logueoDeUsuarioConCIEC(self):
        self. __entrarAlaPaginaInicio()
        self.__enviarFormularioConCIEC()
        self.__leerFormularioDeRespuesta()
