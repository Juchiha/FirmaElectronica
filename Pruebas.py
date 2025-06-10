from datetime import datetime

from lxml import etree

from XmlSignerV3 import XmlSignerV3

xml = """<?xml version='1.0' encoding='utf-8'?>
<Invoice
    xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"
    xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
    xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
    xmlns:ds="http://www.w3.org/2000/09/xmldsig#"
    xmlns:ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"
    xmlns:sts="http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures"
    xmlns:xades="http://uri.etsi.org/01903/v1.3.2#"
    xmlns:xades141="http://uri.etsi.org/01903/v1.4.1#"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2 http://docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd">
    <ext:UBLExtensions>
        <ext:UBLExtension>
            <ext:ExtensionContent>
                <sts:DianExtensions>
                    <sts:InvoiceControl>
                        <sts:InvoiceAuthorization>18760000001</sts:InvoiceAuthorization>
                        <sts:AuthorizationPeriod>
                            <cbc:StartDate>2019-01-19</cbc:StartDate>
                            <cbc:EndDate>2030-01-19</cbc:EndDate>
                        </sts:AuthorizationPeriod>
                        <sts:AuthorizedInvoices>
                            <sts:Prefix>SETP</sts:Prefix>
                            <sts:From>990000000</sts:From>
                            <sts:To>995000000</sts:To>
                        </sts:AuthorizedInvoices>
                    </sts:InvoiceControl>
                    <sts:InvoiceSource>
                        <cbc:IdentificationCode listAgencyID="6" listAgencyName="United Nations Economic Commission for Europe" listSchemeURI="urn:oasis:names:specification:ubl:codelist:gc:CountryIdentificationCode-2.1">CO</cbc:IdentificationCode>
                    </sts:InvoiceSource>
                    <sts:SoftwareProvider>
                        <sts:ProviderID schemeAgencyID="195" schemeAgencyName="CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)" schemeID="9" schemeName="31">900479894</sts:ProviderID>
                        <sts:SoftwareID schemeAgencyID="195" schemeAgencyName="CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)">0c57f60b-b86f-4a2f-b952-a26efe8321e3</sts:SoftwareID>
                    </sts:SoftwareProvider>
                    <sts:SoftwareSecurityCode schemeAgencyID="195" schemeAgencyName="CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)">e0b54a13cc345a7d6c9e30aa70084104d7e958305261562efc88ba617ee13fac1abb79a4ac677ee6e1848ff7f741a19e</sts:SoftwareSecurityCode>
                    <sts:AuthorizationProvider>
                        <sts:AuthorizationProviderID schemeAgencyID="195" schemeAgencyName="CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)" schemeID="4" schemeName="31">800197268</sts:AuthorizationProviderID>
                    </sts:AuthorizationProvider>
                    <sts:QRCode>https://catalogo-vpfe.dian.gov.co/document/searchqr?documentkey=a475460eb27ba6359abbc3d520f966dd68782667684f0e9ab241a1f606aa0aab0b82c0d7c0c4bc93ff1152a0494dd736</sts:QRCode>
                </sts:DianExtensions>
            </ext:ExtensionContent>
        </ext:UBLExtension>
        <ext:UBLExtension>
            <ext:ExtensionContent/>
        </ext:UBLExtension>
    </ext:UBLExtensions>
    <cbc:UBLVersionID>UBL 2.1</cbc:UBLVersionID>
    <cbc:CustomizationID>10</cbc:CustomizationID>
    <cbc:ProfileID>DIAN 2.1: Factura Electrónica de Venta</cbc:ProfileID>
    <cbc:ProfileExecutionID>2</cbc:ProfileExecutionID>
    <cbc:ID>SETP991000001</cbc:ID>
    <cbc:UUID schemeID="2" schemeName="CUFE-SHA384">a475460eb27ba6359abbc3d520f966dd68782667684f0e9ab241a1f606aa0aab0b82c0d7c0c4bc93ff1152a0494dd736</cbc:UUID>
    <cbc:IssueDate>2025-06-10</cbc:IssueDate>
    <cbc:IssueTime>16:22:45-05:00</cbc:IssueTime>
    <cbc:InvoiceTypeCode>01</cbc:InvoiceTypeCode>
    <cbc:DocumentCurrencyCode listAgencyID="6" listAgencyName="United Nations Economic Commission for Europe" listID="ISO 4217 Alpha">COP</cbc:DocumentCurrencyCode>
    <cbc:LineCountNumeric>3</cbc:LineCountNumeric>
    <cac:InvoicePeriod>
        <cbc:StartDate></cbc:StartDate>
        <cbc:EndDate></cbc:EndDate>
    </cac:InvoicePeriod>
    <cac:AccountingSupplierParty>
        <cbc:AdditionalAccountID>1</cbc:AdditionalAccountID>
        <cac:Party>
            <cac:PartyName>
                <cbc:Name>CENTRO MEDICO COGNITIVO E INVESTIGACION S A S</cbc:Name>
            </cac:PartyName>
            <cac:PhysicalLocation>
                <cac:Address>
                    <cbc:ID>08001</cbc:ID>
                    <cbc:CityName>BARRANQUILLA</cbc:CityName>
                    <cbc:CountrySubentity>ATLANTICO</cbc:CountrySubentity>
                    <cbc:CountrySubentityCode>08</cbc:CountrySubentityCode>
                    <cac:AddressLine>
                        <cbc:Line>CR 52  # 74 - 137</cbc:Line>
                    </cac:AddressLine>
                    <cac:Country>
                        <cbc:IdentificationCode>CO</cbc:IdentificationCode>
                        <cbc:Name languageID="es">Colombia</cbc:Name>
                    </cac:Country>
                </cac:Address>
            </cac:PhysicalLocation>
            <cac:PartyTaxScheme>
                <cbc:RegistrationName>CENTRO MEDICO COGNITIVO E INVESTIGACION S A S</cbc:RegistrationName>
                <cbc:CompanyID schemeAgencyID="195" schemeAgencyName="CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)" schemeID="9" schemeName="31">900479894</cbc:CompanyID>
                <cbc:TaxLevelCode listName="04">O-47</cbc:TaxLevelCode>
                <cac:RegistrationAddress>
                    <cbc:ID>08001</cbc:ID>
                    <cbc:CityName>BARRANQUILLA</cbc:CityName>
                    <cbc:CountrySubentity>ATLANTICO</cbc:CountrySubentity>
                    <cbc:CountrySubentityCode>08</cbc:CountrySubentityCode>
                    <cac:AddressLine>
                        <cbc:Line>CR 52  # 74 - 137</cbc:Line>
                    </cac:AddressLine>
                    <cac:Country>
                        <cbc:IdentificationCode>CO</cbc:IdentificationCode>
                        <cbc:Name languageID="es">Colombia</cbc:Name>
                    </cac:Country>
                </cac:RegistrationAddress>
                <cac:TaxScheme>
                    <cbc:ID>01</cbc:ID>
                    <cbc:Name>IVA</cbc:Name>
                </cac:TaxScheme>
            </cac:PartyTaxScheme>
            <cac:PartyLegalEntity>
                <cbc:RegistrationName>CENTRO MEDICO COGNITIVO E INVESTIGACION S A S</cbc:RegistrationName>
                <cbc:CompanyID schemeAgencyID="195" schemeAgencyName="CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)" schemeID="9" schemeName="31">900479894</cbc:CompanyID>
                <cac:CorporateRegistrationScheme>
                    <cbc:ID>SETP</cbc:ID>
                    <cbc:Name>0000000</cbc:Name>
                </cac:CorporateRegistrationScheme>
            </cac:PartyLegalEntity>
        </cac:Party>
    </cac:AccountingSupplierParty>
    <cac:AccountingCustomerParty>
        <cbc:AdditionalAccountID>1</cbc:AdditionalAccountID>
        <cac:Party>
            <cac:PartyIdentification>
                <cbc:ID schemeAgencyID="195" schemeAgencyName="CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)" schemeName="13">890102006</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
                <cbc:Name>SECRETARIA DISTRITAL DE SALUD</cbc:Name>
            </cac:PartyName>
            <cac:PhysicalLocation>
                <cac:Address>
                    <cbc:ID>08001</cbc:ID>
                    <cbc:CityName>BARRANQUILLA</cbc:CityName>
                    <cbc:CountrySubentity>Atlantico 
</cbc:CountrySubentity>
                    <cbc:CountrySubentityCode>08</cbc:CountrySubentityCode>
                    <cac:AddressLine>
                        <cbc:Line> Gobernación del Atlántico - CL 40 45 46</cbc:Line>
                    </cac:AddressLine>
                    <cac:Country>
                        <cbc:IdentificationCode>CO</cbc:IdentificationCode>
                        <cbc:Name languageID="es">Colombia</cbc:Name>
                    </cac:Country>
                </cac:Address>
            </cac:PhysicalLocation>
            <cac:PartyTaxScheme>
                <cbc:RegistrationName>SECRETARIA DISTRITAL DE SALUD</cbc:RegistrationName>
                <cbc:CompanyID schemeAgencyID="195" schemeAgencyName="CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)" schemeID="1" schemeName="31">890102006</cbc:CompanyID>
                <cbc:TaxLevelCode listName="04">O-47</cbc:TaxLevelCode>
                <cac:TaxScheme>
                    <cbc:ID>01</cbc:ID>
                    <cbc:Name>IVA</cbc:Name>
                </cac:TaxScheme>
            </cac:PartyTaxScheme>
            <cac:PartyLegalEntity>
                <cbc:RegistrationName>SECRETARIA DISTRITAL DE SALUD</cbc:RegistrationName>
                <cbc:CompanyID schemeAgencyID="195" schemeAgencyName="CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)" schemeID="1" schemeName="31">890102006</cbc:CompanyID>
            </cac:PartyLegalEntity>
        </cac:Party>
    </cac:AccountingCustomerParty>
    <cac:PaymentMeans>
        <cbc:ID>2</cbc:ID>
        <cbc:PaymentMeansCode>42</cbc:PaymentMeansCode>
        <cbc:PaymentDueDate>2024-07-15</cbc:PaymentDueDate>
    </cac:PaymentMeans>
    <cac:TaxTotal>
        <cbc:TaxAmount currencyID="COP">0.00</cbc:TaxAmount>
        <cac:TaxSubtotal>
            <cbc:TaxableAmount currencyID="COP">708027.00</cbc:TaxableAmount>
            <cbc:TaxAmount currencyID="COP">0.00</cbc:TaxAmount>
            <cac:TaxCategory>
                <cbc:Percent>0.00</cbc:Percent>
                <cac:TaxScheme>
                    <cbc:ID>01</cbc:ID>
                    <cbc:Name>IVA</cbc:Name>
                </cac:TaxScheme>
            </cac:TaxCategory>
        </cac:TaxSubtotal>
    </cac:TaxTotal>
    <cac:LegalMonetaryTotal>
        <cbc:LineExtensionAmount currencyID="COP">708027.00</cbc:LineExtensionAmount>
        <cbc:TaxExclusiveAmount currencyID="COP">708027.00</cbc:TaxExclusiveAmount>
        <cbc:TaxInclusiveAmount currencyID="COP">708027</cbc:TaxInclusiveAmount>
        <cbc:AllowanceTotalAmount currencyID="COP">0</cbc:AllowanceTotalAmount>
        <cbc:PayableAmount currencyID="COP">708027</cbc:PayableAmount>
    </cac:LegalMonetaryTotal>
    
                  <cac:InvoiceLine>
                  <cbc:ID>1</cbc:ID>
                  <cbc:InvoicedQuantity unitCode='EA'>1</cbc:InvoicedQuantity>
                  <cbc:LineExtensionAmount currencyID='COP'>160527</cbc:LineExtensionAmount>
                  <cbc:FreeOfChargeIndicator>false</cbc:FreeOfChargeIndicator>
                  <cac:TaxTotal>
		            <cbc:TaxAmount currencyID="COP">0</cbc:TaxAmount>
		            <cac:TaxSubtotal>
		                <cbc:TaxableAmount currencyID="COP">160527</cbc:TaxableAmount>
		                <cbc:TaxAmount currencyID="COP">0</cbc:TaxAmount>
		                <cac:TaxCategory>
		                    <cbc:ID>01</cbc:ID>
		                    <cbc:Percent>0.00</cbc:Percent>
		                    <cac:TaxScheme>
		                        <cbc:ID>01</cbc:ID>
		                        <cbc:Name>IVA</cbc:Name>
		                    </cac:TaxScheme>
		                </cac:TaxCategory>
		            </cac:TaxSubtotal>
        		  </cac:TaxTotal>
                  <cac:Item>
                    <cbc:Description>CONSULTA DE PRIMERA VEZ POR EQUIPO INTERDISCIPLINARIO</cbc:Description>
                    <cac:SellersItemIdentification>
                        <cbc:ID>890215</cbc:ID>
                    </cac:SellersItemIdentification>
                    <cac:StandardItemIdentification>
                        <cbc:ID schemeID="999">890215</cbc:ID>
                    </cac:StandardItemIdentification>
                  </cac:Item>
                  <cac:Price>
                     <cbc:PriceAmount currencyID='COP'>160527</cbc:PriceAmount>
                     <cbc:BaseQuantity unitCode='EA'>1</cbc:BaseQuantity>
                  </cac:Price>
               </cac:InvoiceLine>
               
                  <cac:InvoiceLine>
                  <cbc:ID>2</cbc:ID>
                  <cbc:InvoicedQuantity unitCode='EA'>5</cbc:InvoicedQuantity>
                  <cbc:LineExtensionAmount currencyID='COP'>125000</cbc:LineExtensionAmount>
                  <cbc:FreeOfChargeIndicator>false</cbc:FreeOfChargeIndicator>
                  <cac:TaxTotal>
		            <cbc:TaxAmount currencyID="COP">0</cbc:TaxAmount>
		            <cac:TaxSubtotal>
		                <cbc:TaxableAmount currencyID="COP">125000</cbc:TaxableAmount>
		                <cbc:TaxAmount currencyID="COP">0</cbc:TaxAmount>
		                <cac:TaxCategory>
		                    <cbc:ID>01</cbc:ID>
		                    <cbc:Percent>0.00</cbc:Percent>
		                    <cac:TaxScheme>
		                        <cbc:ID>01</cbc:ID>
		                        <cbc:Name>IVA</cbc:Name>
		                    </cac:TaxScheme>
		                </cac:TaxCategory>
		            </cac:TaxSubtotal>
        		  </cac:TaxTotal>
                  <cac:Item>
                    <cbc:Description>PSICOTERAPIA INDIVIDIAL POR PSICOLOGIA</cbc:Description>
                    <cac:SellersItemIdentification>
                        <cbc:ID>943102</cbc:ID>
                    </cac:SellersItemIdentification>
                    <cac:StandardItemIdentification>
                        <cbc:ID schemeID="999">943102</cbc:ID>
                    </cac:StandardItemIdentification>
                  </cac:Item>
                  <cac:Price>
                     <cbc:PriceAmount currencyID='COP'>25000</cbc:PriceAmount>
                     <cbc:BaseQuantity unitCode='EA'>5</cbc:BaseQuantity>
                  </cac:Price>
               </cac:InvoiceLine>
               
                  <cac:InvoiceLine>
                  <cbc:ID>3</cbc:ID>
                  <cbc:InvoicedQuantity unitCode='EA'>13</cbc:InvoicedQuantity>
                  <cbc:LineExtensionAmount currencyID='COP'>422500</cbc:LineExtensionAmount>
                  <cbc:FreeOfChargeIndicator>false</cbc:FreeOfChargeIndicator>
                  <cac:TaxTotal>
		            <cbc:TaxAmount currencyID="COP">0</cbc:TaxAmount>
		            <cac:TaxSubtotal>
		                <cbc:TaxableAmount currencyID="COP">422500</cbc:TaxableAmount>
		                <cbc:TaxAmount currencyID="COP">0</cbc:TaxAmount>
		                <cac:TaxCategory>
		                    <cbc:ID>01</cbc:ID>
		                    <cbc:Percent>0.00</cbc:Percent>
		                    <cac:TaxScheme>
		                        <cbc:ID>01</cbc:ID>
		                        <cbc:Name>IVA</cbc:Name>
		                    </cac:TaxScheme>
		                </cac:TaxCategory>
		            </cac:TaxSubtotal>
        		  </cac:TaxTotal>
                  <cac:Item>
                    <cbc:Description>TERAPIA FONOAUDIOLÓGICA INTEGRAL SOD</cbc:Description>
                    <cac:SellersItemIdentification>
                        <cbc:ID>937000</cbc:ID>
                    </cac:SellersItemIdentification>
                    <cac:StandardItemIdentification>
                        <cbc:ID schemeID="999">937000</cbc:ID>
                    </cac:StandardItemIdentification>
                  </cac:Item>
                  <cac:Price>
                     <cbc:PriceAmount currencyID='COP'>32500</cbc:PriceAmount>
                     <cbc:BaseQuantity unitCode='EA'>13</cbc:BaseQuantity>
                  </cac:Price>
               </cac:InvoiceLine>
               
</Invoice>"""

xml_element = etree.fromstring(xml.encode("utf-8"))
firmanteXml = XmlSignerV3(xml_element, 'FV')
signed_xml_string = firmanteXml.sign()
print(signed_xml_string)

