from fastapi import FastAPI, HTTPException
from lxml import etree
from pydantic import BaseModel
import base64


from XmlSignerV3 import XmlSignerV3

app = FastAPI()

class XMLRequest(BaseModel):
    xml_string: str

@app.post("/sign_xml")
def sign_xml(request: XMLRequest):
    try:
        xml_string = base64.b64decode(request.xml_string).decode("utf-8")

        # Convertir el XML recibido en un objeto `etree.Element`
        xml_element = etree.fromstring(xml_string.encode("utf-8"))

        # Instanciar el firmante
        firmanteXml = XmlSignerV3(xml_element, "FV")

        # Firmar el XML
        signed_xml_string = firmanteXml.sign()

        signed_xml_base64 = base64.b64encode(signed_xml_string.encode("utf-8")).decode("utf-8")

        # Retornar el XML firmado
        return {"signed_xml": signed_xml_base64}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al firmar el XML: {str(e)}")

@app.get("/health_check")
def health_check():
    return {"status": "OK"}