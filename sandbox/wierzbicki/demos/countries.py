import os

os.putenv("DJANGO_SETTINGS_MODULE", "mysite.settings")

from mysite.world.models import Continent, Country

#Continent.objects.remove()
#Country.objects.remove()

#Continent
Asia = Continent(name='Asia')
Asia.save()
Europe = Continent(name='Europe')
Europe.save()
North_America  = Continent(name='North America')
North_America.save()  
Africa = Continent(name='Africa')
Africa.save() 
Oceania = Continent(name='Oceania')
Oceania.save() 
Antarctica = Continent(name='Antarctica')
Antarctica.save() 
South_America  = Continent(name='South America')
South_America.save() 

#Country
AFG = Country(code='AFG', name='Afghanistan',continent=Asia, region='Southern and Central Asia', surface_area=652090.00, indep_year=1919, population=22720000, life_expectancy=45.9, gnp=5976.00, gnp_old=None, local_name='Afganistan/Afqanestan', government_form='Islamic Emirate', head_of_state='Mohammad Omar',capital=None, code2='AF')
AFG.save() 
NLD = Country(code='NLD', name='Netherlands',continent=Europe, region='Western Europe', surface_area=41526.00, indep_year=1581, population=15864000, life_expectancy=78.3, gnp=371362.00, gnp_old=360478.00, local_name='Nederland', government_form='Constitutional Monarchy', head_of_state='Beatrix',capital=None,code2='NL')
NLD.save() 
ANT = Country(code='ANT', name='Netherlands Antilles',continent=North_America, region='Caribbean', surface_area=800.00, indep_year=None, population=217000, life_expectancy=74.7, gnp=1941.00, gnp_old=None, local_name='Nederlandse Antillen', government_form='Nonmetropolitan Territory of The Netherlands', head_of_state='Beatrix',capital=None,code2='AN')
ANT.save() 
ALB = Country(code='ALB', name='Albania',continent=Europe, region='Southern Europe', surface_area=28748.00, indep_year=1912, population=3401200, life_expectancy=71.6, gnp=3205.00, gnp_old=2500.00, local_name='Shqipëria', government_form='Republic', head_of_state='Rexhep Mejdani',capital=None,code2='AL')
ALB.save() 
DZA = Country(code='DZA', name='Algeria',continent=Africa, region='Northern Africa', surface_area=2381741.00, indep_year=1962, population=31471000, life_expectancy=69.7, gnp=49982.00, gnp_old=46966.00, local_name='Al-Jazair/Algérie', government_form='Republic', head_of_state='Abdelaziz Bouteflika',capital=None,code2='DZ')
DZA.save() 
ASM = Country(code='ASM', name='American Samoa',continent=Oceania, region='Polynesia', surface_area=199.00, indep_year=None, population=68000, life_expectancy=75.1, gnp=334.00, gnp_old=None, local_name='Amerika Samoa', government_form='US Territory', head_of_state='George W. Bush',capital=None,code2='AS')
ASM.save() 
AND = Country(code='AND', name='Andorra',continent=Europe, region='Southern Europe', surface_area=468.00, indep_year=1278, population=78000, life_expectancy=83.5, gnp=1630.00, gnp_old=None, local_name='Andorra', government_form='Parliamentary Coprincipality', head_of_state='',capital=None,code2='AD')
AND.save() 
AGO = Country(code='AGO', name='Angola',continent=Africa, region='Central Africa', surface_area=1246700.00, indep_year=1975, population=12878000, life_expectancy=38.3, gnp=6648.00, gnp_old=7984.00, local_name='Angola', government_form='Republic', head_of_state='José Eduardo dos Santos',capital=None,code2='AO')
AGO.save() 
AIA = Country(code='AIA', name='Anguilla',continent=North_America, region='Caribbean', surface_area=96.00, indep_year=None, population=8000, life_expectancy=76.1, gnp=63.20, gnp_old=None, local_name='Anguilla', government_form='Dependent Territory of the UK', head_of_state='Elisabeth II',capital=None,code2='AI')
AIA.save() 
ATG = Country(code='ATG', name='Antigua and Barbuda',continent=North_America, region='Caribbean', surface_area=442.00, indep_year=1981, population=68000, life_expectancy=70.5, gnp=612.00, gnp_old=584.00, local_name='Antigua and Barbuda', government_form='Constitutional Monarchy', head_of_state='Elisabeth II',capital=None,code2='AG')
ATG.save() 
ARE = Country(code='ARE', name='United Arab Emirates',continent=Asia, region='Middle East', surface_area=83600.00, indep_year=1971, population=2441000, life_expectancy=74.1, gnp=37966.00, gnp_old=36846.00, local_name='Al-Imarat al-´Arabiya al-Muttahida', government_form='Emirate Federation', head_of_state='Zayid bin Sultan al-Nahayan',capital=None,code2='AE')
ARE.save() 
ARG = Country(code='ARG', name='Argentina',continent=South_America, region='South America', surface_area=2780400.00, indep_year=1816, population=37032000, life_expectancy=75.1, gnp=340238.00, gnp_old=323310.00, local_name='Argentina', government_form='Federal Republic', head_of_state='Fernando de la Rúa',capital=None,code2='AR')
ARG.save() 
ARM = Country(code='ARM', name='Armenia',continent=Asia, region='Middle East', surface_area=29800.00, indep_year=1991, population=3520000, life_expectancy=66.4, gnp=1813.00, gnp_old=1627.00, local_name='Hajastan', government_form='Republic', head_of_state='Robert Kotarjan',capital=None,code2='AM')
ARM.save() 
ABW = Country(code='ABW', name='Aruba',continent=North_America, region='Caribbean', surface_area=193.00, indep_year=None, population=103000, life_expectancy=78.4, gnp=828.00, gnp_old=793.00, local_name='Aruba', government_form='Nonmetropolitan Territory of The Netherlands', head_of_state='Beatrix',capital=None,code2='AW')
ABW.save() 
AUS = Country(code='AUS', name='Australia',continent=Oceania, region='Australia and New Zealand', surface_area=7741220.00, indep_year=1901, population=18886000, life_expectancy=79.8, gnp=351182.00, gnp_old=392911.00, local_name='Australia', government_form='Constitutional Monarchy, Federation', head_of_state='Elisabeth II',capital=None,code2='AU')
AUS.save() 
AZE = Country(code='AZE', name='Azerbaijan',continent=Asia, region='Middle East', surface_area=86600.00, indep_year=1991, population=7734000, life_expectancy=62.9, gnp=4127.00, gnp_old=4100.00, local_name='Azärbaycan', government_form='Federal Republic', head_of_state='Heydär Äliyev',capital=None,code2='AZ')
AZE.save() 
BHS = Country(code='BHS', name='Bahamas',continent=North_America, region='Caribbean', surface_area=13878.00, indep_year=1973, population=307000, life_expectancy=71.1, gnp=3527.00, gnp_old=3347.00, local_name='The Bahamas', government_form='Constitutional Monarchy', head_of_state='Elisabeth II',capital=None,code2='BS')
BHS.save() 
BHR = Country(code='BHR', name='Bahrain',continent=Asia, region='Middle East', surface_area=694.00, indep_year=1971, population=617000, life_expectancy=73.0, gnp=6366.00, gnp_old=6097.00, local_name='Al-Bahrayn', government_form='Monarchy (Emirate)', head_of_state='Hamad ibn Isa al-Khalifa',capital=None,code2='BH')
BHR.save() 
BGD = Country(code='BGD', name='Bangladesh',continent=Asia, region='Southern and Central Asia', surface_area=143998.00, indep_year=1971, population=129155000, life_expectancy=60.2, gnp=32852.00, gnp_old=31966.00, local_name='Bangladesh', government_form='Republic', head_of_state='Shahabuddin Ahmad',capital=None,code2='BD')
BGD.save() 
BRB = Country(code='BRB', name='Barbados',continent=North_America, region='Caribbean', surface_area=430.00, indep_year=1966, population=270000, life_expectancy=73.0, gnp=2223.00, gnp_old=2186.00, local_name='Barbados', government_form='Constitutional Monarchy', head_of_state='Elisabeth II',capital=None,code2='BB')
BRB.save() 
BEL = Country(code='BEL', name='Belgium',continent=Europe, region='Western Europe', surface_area=30518.00, indep_year=1830, population=10239000, life_expectancy=77.8, gnp=249704.00, gnp_old=243948.00, local_name='België/Belgique', government_form='Constitutional Monarchy, Federation', head_of_state='Albert II',capital=None,code2='BE')
BEL.save() 
BLZ = Country(code='BLZ', name='Belize',continent=North_America, region='Central America', surface_area=22696.00, indep_year=1981, population=241000, life_expectancy=70.9, gnp=630.00, gnp_old=616.00, local_name='Belize', government_form='Constitutional Monarchy', head_of_state='Elisabeth II',capital=None,code2='BZ')
BLZ.save() 
BEN = Country(code='BEN', name='Benin',continent=Africa, region='Western Africa', surface_area=112622.00, indep_year=1960, population=6097000, life_expectancy=50.2, gnp=2357.00, gnp_old=2141.00, local_name='Bénin', government_form='Republic', head_of_state='Mathieu Kérékou',capital=None,code2='BJ')
BEN.save() 
BMU = Country(code='BMU', name='Bermuda',continent=North_America, region='North America', surface_area=53.00, indep_year=None, population=65000, life_expectancy=76.9, gnp=2328.00, gnp_old=2190.00, local_name='Bermuda', government_form='Dependent Territory of the UK', head_of_state='Elisabeth II',capital=None,code2='BM')
BMU.save() 
BTN = Country(code='BTN', name='Bhutan',continent=Asia, region='Southern and Central Asia', surface_area=47000.00, indep_year=1910, population=2124000, life_expectancy=52.4, gnp=372.00, gnp_old=383.00, local_name='Druk-Yul', government_form='Monarchy', head_of_state='Jigme Singye Wangchuk',capital=None,code2='BT')
BTN.save() 
BOL = Country(code='BOL', name='Bolivia',continent=South_America, region='South America', surface_area=1098581.00, indep_year=1825, population=8329000, life_expectancy=63.7, gnp=8571.00, gnp_old=7967.00, local_name='Bolivia', government_form='Republic', head_of_state='Hugo Bánzer Suárez',capital=None,code2='BO')
BOL.save() 
BIH = Country(code='BIH', name='Bosnia and Herzegovina',continent=Europe, region='Southern Europe', surface_area=51197.00, indep_year=1992, population=3972000, life_expectancy=71.5, gnp=2841.00, gnp_old=None, local_name='Bosna i Hercegovina', government_form='Federal Republic', head_of_state='Ante Jelavic',capital=None,code2='BA')
BIH.save() 
BWA = Country(code='BWA', name='Botswana',continent=Africa, region='Southern Africa', surface_area=581730.00, indep_year=1966, population=1622000, life_expectancy=39.3, gnp=4834.00, gnp_old=4935.00, local_name='Botswana', government_form='Republic', head_of_state='Festus G. Mogae',capital=None,code2='BW')
BWA.save() 
BRA = Country(code='BRA', name='Brazil',continent=South_America, region='South America', surface_area=8547403.00, indep_year=1822, population=170115000, life_expectancy=62.9, gnp=776739.00, gnp_old=804108.00, local_name='Brasil', government_form='Federal Republic', head_of_state='Fernando Henrique Cardoso',capital=None,code2='BR')
BRA.save() 
GBR = Country(code='GBR', name='United Kingdom',continent=Europe, region='British Islands', surface_area=242900.00, indep_year=1066, population=59623400, life_expectancy=77.7, gnp=1378330.00, gnp_old=1296830.00, local_name='United Kingdom', government_form='Constitutional Monarchy', head_of_state='Elisabeth II',capital=None,code2='GB')
GBR.save() 
VGB = Country(code='VGB', name='Virgin Islands, British',continent=North_America, region='Caribbean', surface_area=151.00, indep_year=None, population=21000, life_expectancy=75.4, gnp=612.00, gnp_old=573.00, local_name='British Virgin Islands', government_form='Dependent Territory of the UK', head_of_state='Elisabeth II',capital=None,code2='VG')
VGB.save() 
BRN = Country(code='BRN', name='Brunei',continent=Asia, region='Southeast Asia', surface_area=5765.00, indep_year=1984, population=328000, life_expectancy=73.6, gnp=11705.00, gnp_old=12460.00, local_name='Brunei Darussalam', government_form='Monarchy (Sultanate)', head_of_state='Haji Hassan al-Bolkiah',capital=None,code2='BN')
BRN.save() 
BGR = Country(code='BGR', name='Bulgaria',continent=Europe, region='Eastern Europe', surface_area=110994.00, indep_year=1908, population=8190900, life_expectancy=70.9, gnp=12178.00, gnp_old=10169.00, local_name='Balgarija', government_form='Republic', head_of_state='Petar Stojanov',capital=None,code2='BG')
BGR.save() 
BFA = Country(code='BFA', name='Burkina Faso',continent=Africa, region='Western Africa', surface_area=274000.00, indep_year=1960, population=11937000, life_expectancy=46.7, gnp=2425.00, gnp_old=2201.00, local_name='Burkina Faso', government_form='Republic', head_of_state='Blaise Compaoré',capital=None,code2='BF')
BFA.save() 
BDI = Country(code='BDI', name='Burundi',continent=Africa, region='Eastern Africa', surface_area=27834.00, indep_year=1962, population=6695000, life_expectancy=46.2, gnp=903.00, gnp_old=982.00, local_name='Burundi/Uburundi', government_form='Republic', head_of_state='Pierre Buyoya',capital=None,code2='BI')
BDI.save() 
CYM = Country(code='CYM', name='Cayman Islands',continent=North_America, region='Caribbean', surface_area=264.00, indep_year=None, population=38000, life_expectancy=78.9, gnp=1263.00, gnp_old=1186.00, local_name='Cayman Islands', government_form='Dependent Territory of the UK', head_of_state='Elisabeth II',capital=None,code2='KY')
CYM.save() 
CHL = Country(code='CHL', name='Chile',continent=South_America, region='South America', surface_area=756626.00, indep_year=1810, population=15211000, life_expectancy=75.7, gnp=72949.00, gnp_old=75780.00, local_name='Chile', government_form='Republic', head_of_state='Ricardo Lagos Escobar',capital=None,code2='CL')
CHL.save() 
COK = Country(code='COK', name='Cook Islands',continent=Oceania, region='Polynesia', surface_area=236.00, indep_year=None, population=20000, life_expectancy=71.1, gnp=100.00, gnp_old=None, local_name='The Cook Islands', government_form='Nonmetropolitan Territory of New Zealand', head_of_state='Elisabeth II',capital=None,code2='CK')
COK.save() 
CRI = Country(code='CRI', name='Costa Rica',continent=North_America, region='Central America', surface_area=51100.00, indep_year=1821, population=4023000, life_expectancy=75.8, gnp=10226.00, gnp_old=9757.00, local_name='Costa Rica', government_form='Republic', head_of_state='Miguel Ángel Rodríguez Echeverría',capital=None,code2='CR')
CRI.save() 
DJI = Country(code='DJI', name='Djibouti',continent=Africa, region='Eastern Africa', surface_area=23200.00, indep_year=1977, population=638000, life_expectancy=50.8, gnp=382.00, gnp_old=373.00, local_name='Djibouti/Jibuti', government_form='Republic', head_of_state='Ismail Omar Guelleh',capital=None,code2='DJ')
DJI.save() 
DMA = Country(code='DMA', name='Dominica',continent=North_America, region='Caribbean', surface_area=751.00, indep_year=1978, population=71000, life_expectancy=73.4, gnp=256.00, gnp_old=243.00, local_name='Dominica', government_form='Republic', head_of_state='Vernon Shaw',capital=None,code2='DM')
DMA.save() 
DOM = Country(code='DOM', name='Dominican Republic',continent=North_America, region='Caribbean', surface_area=48511.00, indep_year=1844, population=8495000, life_expectancy=73.2, gnp=15846.00, gnp_old=15076.00, local_name='República Dominicana', government_form='Republic', head_of_state='Hipólito Mejía Domínguez',capital=None,code2='DO')
DOM.save() 
ECU = Country(code='ECU', name='Ecuador',continent=South_America, region='South America', surface_area=283561.00, indep_year=1822, population=12646000, life_expectancy=71.1, gnp=19770.00, gnp_old=19769.00, local_name='Ecuador', government_form='Republic', head_of_state='Gustavo Noboa Bejarano',capital=None,code2='EC')
ECU.save() 
EGY = Country(code='EGY', name='Egypt',continent=Africa, region='Northern Africa', surface_area=1001449.00, indep_year=1922, population=68470000, life_expectancy=63.3, gnp=82710.00, gnp_old=75617.00, local_name='Misr', government_form='Republic', head_of_state='Hosni Mubarak',capital=None,code2='EG')
EGY.save() 
SLV = Country(code='SLV', name='El Salvador',continent=North_America, region='Central America', surface_area=21041.00, indep_year=1841, population=6276000, life_expectancy=69.7, gnp=11863.00, gnp_old=11203.00, local_name='El Salvador', government_form='Republic', head_of_state='Francisco Guillermo Flores Pérez',capital=None,code2='SV')
SLV.save() 
ERI = Country(code='ERI', name='Eritrea',continent=Africa, region='Eastern Africa', surface_area=117600.00, indep_year=1993, population=3850000, life_expectancy=55.8, gnp=650.00, gnp_old=755.00, local_name='Ertra', government_form='Republic', head_of_state='Isayas Afewerki [Isaias Afwerki]',capital=None,code2='ER')
ERI.save() 
ESP = Country(code='ESP', name='Spain',continent=Europe, region='Southern Europe', surface_area=505992.00, indep_year=1492, population=39441700, life_expectancy=78.8, gnp=553233.00, gnp_old=532031.00, local_name='España', government_form='Constitutional Monarchy', head_of_state='Juan Carlos I',capital=None,code2='ES')
ESP.save() 
ZAF = Country(code='ZAF', name='South Africa',continent=Africa, region='Southern Africa', surface_area=1221037.00, indep_year=1910, population=40377000, life_expectancy=51.1, gnp=116729.00, gnp_old=129092.00, local_name='South Africa', government_form='Republic', head_of_state='Thabo Mbeki',capital=None,code2='ZA')
ZAF.save() 
ETH = Country(code='ETH', name='Ethiopia',continent=Africa, region='Eastern Africa', surface_area=1104300.00, indep_year=-1000, population=62565000, life_expectancy=45.2, gnp=6353.00, gnp_old=6180.00, local_name='YeItyop´iya', government_form='Republic', head_of_state='Negasso Gidada',capital=None,code2='ET')
ETH.save() 
FLK = Country(code='FLK', name='Falkland Islands',continent=South_America, region='South America', surface_area=12173.00, indep_year=None, population=2000, life_expectancy=None, gnp=0.00, gnp_old=None, local_name='Falkland Islands', government_form='Dependent Territory of the UK', head_of_state='Elisabeth II',capital=None,code2='FK')
FLK.save() 
FJI = Country(code='FJI', name='Fiji Islands',continent=Oceania, region='Melanesia', surface_area=18274.00, indep_year=1970, population=817000, life_expectancy=67.9, gnp=1536.00, gnp_old=2149.00, local_name='Fiji Islands', government_form='Republic', head_of_state='Josefa Iloilo',capital=None,code2='FJ')
FJI.save() 
PHL = Country(code='PHL', name='Philippines',continent=Asia, region='Southeast Asia', surface_area=300000.00, indep_year=1946, population=75967000, life_expectancy=67.5, gnp=65107.00, gnp_old=82239.00, local_name='Pilipinas', government_form='Republic', head_of_state='Gloria Macapagal-Arroyo',capital=None,code2='PH')
PHL.save() 
FRO = Country(code='FRO', name='Faroe Islands',continent=Europe, region='Nordic Countries', surface_area=1399.00, indep_year=None, population=43000, life_expectancy=78.4, gnp=0.00, gnp_old=None, local_name='Føroyar', government_form='Part of Denmark', head_of_state='Margrethe II',capital=None,code2='FO')
FRO.save() 
GAB = Country(code='GAB', name='Gabon',continent=Africa, region='Central Africa', surface_area=267668.00, indep_year=1960, population=1226000, life_expectancy=50.1, gnp=5493.00, gnp_old=5279.00, local_name='Le Gabon', government_form='Republic', head_of_state='Omar Bongo',capital=None,code2='GA')
GAB.save() 
GMB = Country(code='GMB', name='Gambia',continent=Africa, region='Western Africa', surface_area=11295.00, indep_year=1965, population=1305000, life_expectancy=53.2, gnp=320.00, gnp_old=325.00, local_name='The Gambia', government_form='Republic', head_of_state='Yahya Jammeh',capital=None,code2='GM')
GMB.save() 
GEO = Country(code='GEO', name='Georgia',continent=Asia, region='Middle East', surface_area=69700.00, indep_year=1991, population=4968000, life_expectancy=64.5, gnp=6064.00, gnp_old=5924.00, local_name='Sakartvelo', government_form='Republic', head_of_state='Eduard evardnadze',capital=None,code2='GE')
GEO.save() 
GHA = Country(code='GHA', name='Ghana',continent=Africa, region='Western Africa', surface_area=238533.00, indep_year=1957, population=20212000, life_expectancy=57.4, gnp=7137.00, gnp_old=6884.00, local_name='Ghana', government_form='Republic', head_of_state='John Kufuor',capital=None,code2='GH')
GHA.save() 
GIB = Country(code='GIB', name='Gibraltar',continent=Europe, region='Southern Europe', surface_area=6.00, indep_year=None, population=25000, life_expectancy=79.0, gnp=258.00, gnp_old=None, local_name='Gibraltar', government_form='Dependent Territory of the UK', head_of_state='Elisabeth II',capital=None,code2='GI')
GIB.save() 
GRD = Country(code='GRD', name='Grenada',continent=North_America, region='Caribbean', surface_area=344.00, indep_year=1974, population=94000, life_expectancy=64.5, gnp=318.00, gnp_old=None, local_name='Grenada', government_form='Constitutional Monarchy', head_of_state='Elisabeth II',capital=None,code2='GD')
GRD.save() 
GRL = Country(code='GRL', name='Greenland',continent=North_America, region='North America', surface_area=2166090.00, indep_year=None, population=56000, life_expectancy=68.1, gnp=0.00, gnp_old=None, local_name='Kalaallit Nunaat/Grønland', government_form='Part of Denmark', head_of_state='Margrethe II',capital=None,code2='GL')
GRL.save() 
GLP = Country(code='GLP', name='Guadeloupe',continent=North_America, region='Caribbean', surface_area=1705.00, indep_year=None, population=456000, life_expectancy=77.0, gnp=3501.00, gnp_old=None, local_name='Guadeloupe', government_form='Overseas Department of France', head_of_state='Jacques Chirac',capital=None,code2='GP')
GLP.save() 
GUM = Country(code='GUM', name='Guam',continent=Oceania, region='Micronesia', surface_area=549.00, indep_year=None, population=168000, life_expectancy=77.8, gnp=1197.00, gnp_old=1136.00, local_name='Guam', government_form='US Territory', head_of_state='George W. Bush',capital=None,code2='GU')
GUM.save() 
GTM = Country(code='GTM', name='Guatemala',continent=North_America, region='Central America', surface_area=108889.00, indep_year=1821, population=11385000, life_expectancy=66.2, gnp=19008.00, gnp_old=17797.00, local_name='Guatemala', government_form='Republic', head_of_state='Alfonso Portillo Cabrera',capital=None,code2='GT')
GTM.save() 
GIN = Country(code='GIN', name='Guinea',continent=Africa, region='Western Africa', surface_area=245857.00, indep_year=1958, population=7430000, life_expectancy=45.6, gnp=2352.00, gnp_old=2383.00, local_name='Guinée', government_form='Republic', head_of_state='Lansana Conté',capital=None,code2='GN')
GIN.save() 
GNB = Country(code='GNB', name='Guinea-Bissau',continent=Africa, region='Western Africa', surface_area=36125.00, indep_year=1974, population=1213000, life_expectancy=49.0, gnp=293.00, gnp_old=272.00, local_name='Guiné-Bissau', government_form='Republic', head_of_state='Kumba Ialá',capital=None,code2='GW')
GNB.save() 
GUY = Country(code='GUY', name='Guyana',continent=South_America, region='South America', surface_area=214969.00, indep_year=1966, population=861000, life_expectancy=64.0, gnp=722.00, gnp_old=743.00, local_name='Guyana', government_form='Republic', head_of_state='Bharrat Jagdeo',capital=None,code2='GY')
GUY.save() 
HTI = Country(code='HTI', name='Haiti',continent=North_America, region='Caribbean', surface_area=27750.00, indep_year=1804, population=8222000, life_expectancy=49.2, gnp=3459.00, gnp_old=3107.00, local_name='Haïti/Dayti', government_form='Republic', head_of_state='Jean-Bertrand Aristide',capital=None,code2='HT')
HTI.save() 
HND = Country(code='HND', name='Honduras',continent=North_America, region='Central America', surface_area=112088.00, indep_year=1838, population=6485000, life_expectancy=69.9, gnp=5333.00, gnp_old=4697.00, local_name='Honduras', government_form='Republic', head_of_state='Carlos Roberto Flores Facussé',capital=None,code2='HN')
HND.save() 
HKG = Country(code='HKG', name='Hong Kong',continent=Asia, region='Eastern Asia', surface_area=1075.00, indep_year=None, population=6782000, life_expectancy=79.5, gnp=166448.00, gnp_old=173610.00, local_name='Xianggang/Hong Kong', government_form='Special Administrative Region of China', head_of_state='Jiang Zemin',capital=None,code2='HK')
HKG.save() 
SJM = Country(code='SJM', name='Svalbard and Jan Mayen',continent=Europe, region='Nordic Countries', surface_area=62422.00, indep_year=None, population=3200, life_expectancy=None, gnp=0.00, gnp_old=None, local_name='Svalbard og Jan Mayen', government_form='Dependent Territory of Norway', head_of_state='Harald V',capital=None,code2='SJ')
SJM.save() 
IDN = Country(code='IDN', name='Indonesia',continent=Asia, region='Southeast Asia', surface_area=1904569.00, indep_year=1945, population=212107000, life_expectancy=68.0, gnp=84982.00, gnp_old=215002.00, local_name='Indonesia', government_form='Republic', head_of_state='Abdurrahman Wahid',capital=None,code2='ID')
IDN.save() 
IND = Country(code='IND', name='India',continent=Asia, region='Southern and Central Asia', surface_area=3287263.00, indep_year=1947, population=1013662000, life_expectancy=62.5, gnp=447114.00, gnp_old=430572.00, local_name='Bharat/India', government_form='Federal Republic', head_of_state='Kocheril Raman Narayanan',capital=None,code2='IN')
IND.save() 
IRQ = Country(code='IRQ', name='Iraq',continent=Asia, region='Middle East', surface_area=438317.00, indep_year=1932, population=23115000, life_expectancy=66.5, gnp=11500.00, gnp_old=None, local_name='Al-´Iraq', government_form='Republic', head_of_state='Saddam Hussein al-Takriti',capital=None,code2='IQ')
IRQ.save() 
IRN = Country(code='IRN', name='Iran',continent=Asia, region='Southern and Central Asia', surface_area=1648195.00, indep_year=1906, population=67702000, life_expectancy=69.7, gnp=195746.00, gnp_old=160151.00, local_name='Iran', government_form='Islamic Republic', head_of_state='Ali Mohammad Khatami-Ardakani',capital=None,code2='IR')
IRN.save() 
IRL = Country(code='IRL', name='Ireland',continent=Europe, region='British Islands', surface_area=70273.00, indep_year=1921, population=3775100, life_expectancy=76.8, gnp=75921.00, gnp_old=73132.00, local_name='Ireland/Éire', government_form='Republic', head_of_state='Mary McAleese',capital=None,code2='IE')
IRL.save() 
ISL = Country(code='ISL', name='Iceland',continent=Europe, region='Nordic Countries', surface_area=103000.00, indep_year=1944, population=279000, life_expectancy=79.4, gnp=8255.00, gnp_old=7474.00, local_name='Ísland', government_form='Republic', head_of_state='Ólafur Ragnar Grímsson',capital=None,code2='IS')
ISL.save() 
ISR = Country(code='ISR', name='Israel',continent=Asia, region='Middle East', surface_area=21056.00, indep_year=1948, population=6217000, life_expectancy=78.6, gnp=97477.00, gnp_old=98577.00, local_name='Yisrael/Israil', government_form='Republic', head_of_state='Moshe Katzav',capital=None,code2='IL')
ISR.save() 
ITA = Country(code='ITA', name='Italy',continent=Europe, region='Southern Europe', surface_area=301316.00, indep_year=1861, population=57680000, life_expectancy=79.0, gnp=1161755.00, gnp_old=1145372.00, local_name='Italia', government_form='Republic', head_of_state='Carlo Azeglio Ciampi',capital=None,code2='IT')
ITA.save() 
TMP = Country(code='TMP', name='East Timor',continent=Asia, region='Southeast Asia', surface_area=14874.00, indep_year=None, population=885000, life_expectancy=46.0, gnp=0.00, gnp_old=None, local_name='Timor Timur', government_form='Administrated by the UN', head_of_state='José Alexandre Gusmão',capital=None,code2='TP')
TMP.save() 
AUT = Country(code='AUT', name='Austria',continent=Europe, region='Western Europe', surface_area=83859.00, indep_year=1918, population=8091800, life_expectancy=77.7, gnp=211860.00, gnp_old=206025.00, local_name='Österreich', government_form='Federal Republic', head_of_state='Thomas Klestil',capital=None,code2='AT')
AUT.save() 
JAM = Country(code='JAM', name='Jamaica',continent=North_America, region='Caribbean', surface_area=10990.00, indep_year=1962, population=2583000, life_expectancy=75.2, gnp=6871.00, gnp_old=6722.00, local_name='Jamaica', government_form='Constitutional Monarchy', head_of_state='Elisabeth II',capital=None,code2='JM')
JAM.save() 
JPN = Country(code='JPN', name='Japan',continent=Asia, region='Eastern Asia', surface_area=377829.00, indep_year=-660, population=126714000, life_expectancy=80.7, gnp=3787042.00, gnp_old=4192638.00, local_name='Nihon/Nippon', government_form='Constitutional Monarchy', head_of_state='Akihito',capital=None,code2='JP')
JPN.save() 
YEM = Country(code='YEM', name='Yemen',continent=Asia, region='Middle East', surface_area=527968.00, indep_year=1918, population=18112000, life_expectancy=59.8, gnp=6041.00, gnp_old=5729.00, local_name='Al-Yaman', government_form='Republic', head_of_state='Ali Abdallah Salih',capital=None,code2='YE')
YEM.save() 
JOR = Country(code='JOR', name='Jordan',continent=Asia, region='Middle East', surface_area=88946.00, indep_year=1946, population=5083000, life_expectancy=77.4, gnp=7526.00, gnp_old=7051.00, local_name='Al-Urdunn', government_form='Constitutional Monarchy', head_of_state='Abdullah II',capital=None,code2='JO')
JOR.save() 
CXR = Country(code='CXR', name='Christmas Island',continent=Oceania, region='Australia and New Zealand', surface_area=135.00, indep_year=None, population=2500, life_expectancy=None, gnp=0.00, gnp_old=None, local_name='Christmas Island', government_form='Territory of Australia', head_of_state='Elisabeth II',capital=None,code2='CX')
CXR.save() 
YUG = Country(code='YUG', name='Yugoslavia',continent=Europe, region='Southern Europe', surface_area=102173.00, indep_year=1918, population=10640000, life_expectancy=72.4, gnp=17000.00, gnp_old=None, local_name='Jugoslavija', government_form='Federal Republic', head_of_state='Vojislav Kotunica',capital=None,code2='YU')
YUG.save() 
KHM = Country(code='KHM', name='Cambodia',continent=Asia, region='Southeast Asia', surface_area=181035.00, indep_year=1953, population=11168000, life_expectancy=56.5, gnp=5121.00, gnp_old=5670.00, local_name='Kâmpuchéa', government_form='Constitutional Monarchy', head_of_state='Norodom Sihanouk',capital=None,code2='KH')
KHM.save() 
CMR = Country(code='CMR', name='Cameroon',continent=Africa, region='Central Africa', surface_area=475442.00, indep_year=1960, population=15085000, life_expectancy=54.8, gnp=9174.00, gnp_old=8596.00, local_name='Cameroun/Cameroon', government_form='Republic', head_of_state='Paul Biya',capital=None,code2='CM')
CMR.save() 
CAN = Country(code='CAN', name='Canada',continent=North_America, region='North America', surface_area=9970610.00, indep_year=1867, population=31147000, life_expectancy=79.4, gnp=598862.00, gnp_old=625626.00, local_name='Canada', government_form='Constitutional Monarchy, Federation', head_of_state='Elisabeth II',capital=None,code2='CA')
CAN.save() 
CPV = Country(code='CPV', name='Cape Verde',continent=Africa, region='Western Africa', surface_area=4033.00, indep_year=1975, population=428000, life_expectancy=68.9, gnp=435.00, gnp_old=420.00, local_name='Cabo Verde', government_form='Republic', head_of_state='António Mascarenhas Monteiro',capital=None,code2='CV')
CPV.save() 
KAZ = Country(code='KAZ', name='Kazakstan',continent=Asia, region='Southern and Central Asia', surface_area=2724900.00, indep_year=1991, population=16223000, life_expectancy=63.2, gnp=24375.00, gnp_old=23383.00, local_name='Qazaqstan', government_form='Republic', head_of_state='Nursultan Nazarbajev',capital=None,code2='KZ')
KAZ.save() 
KEN = Country(code='KEN', name='Kenya',continent=Africa, region='Eastern Africa', surface_area=580367.00, indep_year=1963, population=30080000, life_expectancy=48.0, gnp=9217.00, gnp_old=10241.00, local_name='Kenya', government_form='Republic', head_of_state='Daniel arap Moi',capital=None,code2='KE')
KEN.save() 
CAF = Country(code='CAF', name='Central African Republic',continent=Africa, region='Central Africa', surface_area=622984.00, indep_year=1960, population=3615000, life_expectancy=44.0, gnp=1054.00, gnp_old=993.00, local_name='Centrafrique/Bê-Afrîka', government_form='Republic', head_of_state='Ange-Félix Patassé',capital=None,code2='CF')
CAF.save() 
CHN = Country(code='CHN', name='China',continent=Asia, region='Eastern Asia', surface_area=9572900.00, indep_year=-1523, population=1277558000, life_expectancy=71.4, gnp=982268.00, gnp_old=917719.00, local_name='Zhongquo', government_form='People\'sRepublic', head_of_state='Jiang Zemin',capital=None,code2='CN')
CHN.save() 
KGZ = Country(code='KGZ', name='Kyrgyzstan',continent=Asia, region='Southern and Central Asia', surface_area=199900.00, indep_year=1991, population=4699000, life_expectancy=63.4, gnp=1626.00, gnp_old=1767.00, local_name='Kyrgyzstan', government_form='Republic', head_of_state='Askar Akajev',capital=None,code2='KG')
KGZ.save() 
KIR = Country(code='KIR', name='Kiribati',continent=Oceania, region='Micronesia', surface_area=726.00, indep_year=1979, population=83000, life_expectancy=59.8, gnp=40.70, gnp_old=None, local_name='Kiribati', government_form='Republic', head_of_state='Teburoro Tito',capital=None,code2='KI')
KIR.save() 
COL = Country(code='COL', name='Colombia',continent=South_America, region='South America', surface_area=1138914.00, indep_year=1810, population=42321000, life_expectancy=70.3, gnp=102896.00, gnp_old=105116.00, local_name='Colombia', government_form='Republic', head_of_state='Andrés Pastrana Arango',capital=None,code2='CO')
COL.save() 
COM = Country(code='COM', name='Comoros',continent=Africa, region='Eastern Africa', surface_area=1862.00, indep_year=1975, population=578000, life_expectancy=60.0, gnp=4401.00, gnp_old=4361.00, local_name='Komori/Comores', government_form='Republic', head_of_state='Azali Assoumani',capital=None,code2='KM')
COM.save() 
COG = Country(code='COG', name='Congo',continent=Africa, region='Central Africa', surface_area=342000.00, indep_year=1960, population=2943000, life_expectancy=47.4, gnp=2108.00, gnp_old=2287.00, local_name='Congo', government_form='Republic', head_of_state='Denis Sassou-Nguesso',capital=None,code2='CG')
COG.save() 
COD = Country(code='COD', name='Congo, The Democratic Republic of the',continent=Africa, region='Central Africa', surface_area=2344858.00, indep_year=1960, population=51654000, life_expectancy=48.8, gnp=6964.00, gnp_old=2474.00, local_name='République Démocratique du Congo', government_form='Republic', head_of_state='Joseph Kabila',capital=None,code2='CD')
COD.save() 
CCK = Country(code='CCK', name='Cocos (Keeling) Islands',continent=Oceania, region='Australia and New Zealand', surface_area=14.00, indep_year=None, population=600, life_expectancy=None, gnp=0.00, gnp_old=None, local_name='Cocos (Keeling) Islands', government_form='Territory of Australia', head_of_state='Elisabeth II',capital=None,code2='CC')
CCK.save() 
PRK = Country(code='PRK', name='North Korea',continent=Asia, region='Eastern Asia', surface_area=120538.00, indep_year=1948, population=24039000, life_expectancy=70.7, gnp=5332.00, gnp_old=None, local_name='Choson Minjujuui In´min Konghwaguk (Bukhan)', government_form='Socialistic Republic', head_of_state='Kim Jong-il',capital=None,code2='KP')
PRK.save() 
KOR = Country(code='KOR', name='South Korea',continent=Asia, region='Eastern Asia', surface_area=99434.00, indep_year=1948, population=46844000, life_expectancy=74.4, gnp=320749.00, gnp_old=442544.00, local_name='Taehan Minguk (Namhan)', government_form='Republic', head_of_state='Kim Dae-jung',capital=None,code2='KR')
KOR.save() 
GRC = Country(code='GRC', name='Greece',continent=Europe, region='Southern Europe', surface_area=131626.00, indep_year=1830, population=10545700, life_expectancy=78.4, gnp=120724.00, gnp_old=119946.00, local_name='Elláda', government_form='Republic', head_of_state='Kostis Stefanopoulos',capital=None,code2='GR')
GRC.save() 
HRV = Country(code='HRV', name='Croatia',continent=Europe, region='Southern Europe', surface_area=56538.00, indep_year=1991, population=4473000, life_expectancy=73.7, gnp=20208.00, gnp_old=19300.00, local_name='Hrvatska', government_form='Republic', head_of_state='tipe Mesic',capital=None,code2='HR')
HRV.save() 
CUB = Country(code='CUB', name='Cuba',continent=North_America, region='Caribbean', surface_area=110861.00, indep_year=1902, population=11201000, life_expectancy=76.2, gnp=17843.00, gnp_old=18862.00, local_name='Cuba', government_form='Socialistic Republic', head_of_state='Fidel Castro Ruz',capital=None,code2='CU')
CUB.save() 
KWT = Country(code='KWT', name='Kuwait',continent=Asia, region='Middle East', surface_area=17818.00, indep_year=1961, population=1972000, life_expectancy=76.1, gnp=27037.00, gnp_old=30373.00, local_name='Al-Kuwayt', government_form='Constitutional Monarchy (Emirate)', head_of_state='Jabir al-Ahmad al-Jabir al-Sabah',capital=None,code2='KW')
KWT.save() 
CYP = Country(code='CYP', name='Cyprus',continent=Asia, region='Middle East', surface_area=9251.00, indep_year=1960, population=754700, life_expectancy=76.7, gnp=9333.00, gnp_old=8246.00, local_name='Kýpros/Kibris', government_form='Republic', head_of_state='Glafkos Klerides',capital=None,code2='CY')
CYP.save() 
LAO = Country(code='LAO', name='Laos',continent=Asia, region='Southeast Asia', surface_area=236800.00, indep_year=1953, population=5433000, life_expectancy=53.1, gnp=1292.00, gnp_old=1746.00, local_name='Lao', government_form='Republic', head_of_state='Khamtay Siphandone',capital=None,code2='LA')
LAO.save() 
LVA = Country(code='LVA', name='Latvia',continent=Europe, region='Baltic Countries', surface_area=64589.00, indep_year=1991, population=2424200, life_expectancy=68.4, gnp=6398.00, gnp_old=5639.00, local_name='Latvija', government_form='Republic', head_of_state='Vaira Vike-Freiberga',capital=None,code2='LV')
LVA.save() 
LSO = Country(code='LSO', name='Lesotho',continent=Africa, region='Southern Africa', surface_area=30355.00, indep_year=1966, population=2153000, life_expectancy=50.8, gnp=1061.00, gnp_old=1161.00, local_name='Lesotho', government_form='Constitutional Monarchy', head_of_state='Letsie III',capital=None,code2='LS')
LSO.save() 
LBN = Country(code='LBN', name='Lebanon',continent=Asia, region='Middle East', surface_area=10400.00, indep_year=1941, population=3282000, life_expectancy=71.3, gnp=17121.00, gnp_old=15129.00, local_name='Lubnan', government_form='Republic', head_of_state='Émile Lahoud',capital=None,code2='LB')
LBN.save() 
LBR = Country(code='LBR', name='Liberia',continent=Africa, region='Western Africa', surface_area=111369.00, indep_year=1847, population=3154000, life_expectancy=51.0, gnp=2012.00, gnp_old=None, local_name='Liberia', government_form='Republic', head_of_state='Charles Taylor',capital=None,code2='LR')
LBR.save() 
LBY = Country(code='LBY', name='Libyan Arab Jamahiriya',continent=Africa, region='Northern Africa', surface_area=1759540.00, indep_year=1951, population=5605000, life_expectancy=75.5, gnp=44806.00, gnp_old=40562.00, local_name='Libiya', government_form='Socialistic State', head_of_state='Muammar al-Qadhafi',capital=None,code2='LY')
LBY.save() 
LIE = Country(code='LIE', name='Liechtenstein',continent=Europe, region='Western Europe', surface_area=160.00, indep_year=1806, population=32300, life_expectancy=78.8, gnp=1119.00, gnp_old=1084.00, local_name='Liechtenstein', government_form='Constitutional Monarchy', head_of_state='Hans-Adam II',capital=None,code2='LI')
LIE.save() 
LTU = Country(code='LTU', name='Lithuania',continent=Europe, region='Baltic Countries', surface_area=65301.00, indep_year=1991, population=3698500, life_expectancy=69.1, gnp=10692.00, gnp_old=9585.00, local_name='Lietuva', government_form='Republic', head_of_state='Valdas Adamkus',capital=None,code2='LT')
LTU.save() 
LUX = Country(code='LUX', name='Luxembourg',continent=Europe, region='Western Europe', surface_area=2586.00, indep_year=1867, population=435700, life_expectancy=77.1, gnp=16321.00, gnp_old=15519.00, local_name='Luxembourg/Lëtzebuerg', government_form='Constitutional Monarchy', head_of_state='Henri',capital=None,code2='LU')
LUX.save() 
ESH = Country(code='ESH', name='Western Sahara',continent=Africa, region='Northern Africa', surface_area=266000.00, indep_year=None, population=293000, life_expectancy=49.8, gnp=60.00, gnp_old=None, local_name='As-Sahrawiya', government_form='Occupied by Marocco', head_of_state='Mohammed Abdel Aziz',capital=None,code2='EH')
ESH.save() 
MAC = Country(code='MAC', name='Macao',continent=Asia, region='Eastern Asia', surface_area=18.00, indep_year=None, population=473000, life_expectancy=81.6, gnp=5749.00, gnp_old=5940.00, local_name='Macau/Aomen', government_form='Special Administrative Region of China', head_of_state='Jiang Zemin',capital=None,code2='MO')
MAC.save() 
MDG = Country(code='MDG', name='Madagascar',continent=Africa, region='Eastern Africa', surface_area=587041.00, indep_year=1960, population=15942000, life_expectancy=55.0, gnp=3750.00, gnp_old=3545.00, local_name='Madagasikara/Madagascar', government_form='Federal Republic', head_of_state='Didier Ratsiraka',capital=None,code2='MG')
MDG.save() 
MKD = Country(code='MKD', name='Macedonia',continent=Europe, region='Southern Europe', surface_area=25713.00, indep_year=1991, population=2024000, life_expectancy=73.8, gnp=1694.00, gnp_old=1915.00, local_name='Makedonija', government_form='Republic', head_of_state='Boris Trajkovski',capital=None,code2='MK')
MKD.save() 
MWI = Country(code='MWI', name='Malawi',continent=Africa, region='Eastern Africa', surface_area=118484.00, indep_year=1964, population=10925000, life_expectancy=37.6, gnp=1687.00, gnp_old=2527.00, local_name='Malawi', government_form='Republic', head_of_state='Bakili Muluzi',capital=None,code2='MW')
MWI.save() 
MDV = Country(code='MDV', name='Maldives',continent=Asia, region='Southern and Central Asia', surface_area=298.00, indep_year=1965, population=286000, life_expectancy=62.2, gnp=199.00, gnp_old=None, local_name='Dhivehi Raajje/Maldives', government_form='Republic', head_of_state='Maumoon Abdul Gayoom',capital=None,code2='MV')
MDV.save() 
MYS = Country(code='MYS', name='Malaysia',continent=Asia, region='Southeast Asia', surface_area=329758.00, indep_year=1957, population=22244000, life_expectancy=70.8, gnp=69213.00, gnp_old=97884.00, local_name='Malaysia', government_form='Constitutional Monarchy, Federation', head_of_state='Salahuddin Abdul Aziz Shah Alhaj',capital=None,code2='MY')
MYS.save() 
MLI = Country(code='MLI', name='Mali',continent=Africa, region='Western Africa', surface_area=1240192.00, indep_year=1960, population=11234000, life_expectancy=46.7, gnp=2642.00, gnp_old=2453.00, local_name='Mali', government_form='Republic', head_of_state='Alpha Oumar Konaré',capital=None,code2='ML')
MLI.save() 
MLT = Country(code='MLT', name='Malta',continent=Europe, region='Southern Europe', surface_area=316.00, indep_year=1964, population=380200, life_expectancy=77.9, gnp=3512.00, gnp_old=3338.00, local_name='Malta', government_form='Republic', head_of_state='Guido de Marco',capital=None,code2='MT')
MLT.save() 
MAR = Country(code='MAR', name='Morocco',continent=Africa, region='Northern Africa', surface_area=446550.00, indep_year=1956, population=28351000, life_expectancy=69.1, gnp=36124.00, gnp_old=33514.00, local_name='Al-Maghrib', government_form='Constitutional Monarchy', head_of_state='Mohammed VI',capital=None,code2='MA')
MAR.save() 
MHL = Country(code='MHL', name='Marshall Islands',continent=Oceania, region='Micronesia', surface_area=181.00, indep_year=1990, population=64000, life_expectancy=65.5, gnp=97.00, gnp_old=None, local_name='Marshall Islands/Majol', government_form='Republic', head_of_state='Kessai Note',capital=None,code2='MH')
MHL.save() 
MTQ = Country(code='MTQ', name='Martinique',continent=North_America, region='Caribbean', surface_area=1102.00, indep_year=None, population=395000, life_expectancy=78.3, gnp=2731.00, gnp_old=2559.00, local_name='Martinique', government_form='Overseas Department of France', head_of_state='Jacques Chirac',capital=None,code2='MQ')
MTQ.save() 
MRT = Country(code='MRT', name='Mauritania',continent=Africa, region='Western Africa', surface_area=1025520.00, indep_year=1960, population=2670000, life_expectancy=50.8, gnp=998.00, gnp_old=1081.00, local_name='Muritaniya/Mauritanie', government_form='Republic', head_of_state='Maaouiya Ould Sid´Ahmad Taya',capital=None,code2='MR')
MRT.save() 
MUS = Country(code='MUS', name='Mauritius',continent=Africa, region='Eastern Africa', surface_area=2040.00, indep_year=1968, population=1158000, life_expectancy=71.0, gnp=4251.00, gnp_old=4186.00, local_name='Mauritius', government_form='Republic', head_of_state='Cassam Uteem',capital=None,code2='MU')
MUS.save() 
MYT = Country(code='MYT', name='Mayotte',continent=Africa, region='Eastern Africa', surface_area=373.00, indep_year=None, population=149000, life_expectancy=59.5, gnp=0.00, gnp_old=None, local_name='Mayotte', government_form='Territorial Collectivity of France', head_of_state='Jacques Chirac',capital=None,code2='YT')
MYT.save() 
MEX = Country(code='MEX', name='Mexico',continent=North_America, region='Central America', surface_area=1958201.00, indep_year=1810, population=98881000, life_expectancy=71.5, gnp=414972.00, gnp_old=401461.00, local_name='Mexico', government_form='Federal Republic', head_of_state='Vicente Fox Quesada',capital=None,code2='MX')
MEX.save() 
FSM = Country(code='FSM', name='Micronesia, Federated States of',continent=Oceania, region='Micronesia', surface_area=702.00, indep_year=1990, population=119000, life_expectancy=68.6, gnp=212.00, gnp_old=None, local_name='Micronesia', government_form='Federal Republic', head_of_state='Leo A. Falcam',capital=None,code2='FM')
FSM.save() 
MDA = Country(code='MDA', name='Moldova',continent=Europe, region='Eastern Europe', surface_area=33851.00, indep_year=1991, population=4380000, life_expectancy=64.5, gnp=1579.00, gnp_old=1872.00, local_name='Moldova', government_form='Republic', head_of_state='Vladimir Voronin',capital=None,code2='MD')
MDA.save() 
MCO = Country(code='MCO', name='Monaco',continent=Europe, region='Western Europe', surface_area=1.50, indep_year=1861, population=34000, life_expectancy=78.8, gnp=776.00, gnp_old=None, local_name='Monaco', government_form='Constitutional Monarchy', head_of_state='Rainier III',capital=None,code2='MC')
MCO.save() 
MNG = Country(code='MNG', name='Mongolia',continent=Asia, region='Eastern Asia', surface_area=1566500.00, indep_year=1921, population=2662000, life_expectancy=67.3, gnp=1043.00, gnp_old=933.00, local_name='Mongol Uls', government_form='Republic', head_of_state='Natsagiin Bagabandi',capital=None,code2='MN')
MNG.save() 
MSR = Country(code='MSR', name='Montserrat',continent=North_America, region='Caribbean', surface_area=102.00, indep_year=None, population=11000, life_expectancy=78.0, gnp=109.00, gnp_old=None, local_name='Montserrat', government_form='Dependent Territory of the UK', head_of_state='Elisabeth II',capital=None,code2='MS')
MSR.save() 
MOZ = Country(code='MOZ', name='Mozambique',continent=Africa, region='Eastern Africa', surface_area=801590.00, indep_year=1975, population=19680000, life_expectancy=37.5, gnp=2891.00, gnp_old=2711.00, local_name='Moçambique', government_form='Republic', head_of_state='Joaquím A. Chissano',capital=None,code2='MZ')
MOZ.save() 
MMR = Country(code='MMR', name='Myanmar',continent=Asia, region='Southeast Asia', surface_area=676578.00, indep_year=1948, population=45611000, life_expectancy=54.9, gnp=180375.00, gnp_old=171028.00, local_name='Myanma Pye', government_form='Republic', head_of_state='kenraali Than Shwe',capital=None,code2='MM')
MMR.save() 
NAM = Country(code='NAM', name='Namibia',continent=Africa, region='Southern Africa', surface_area=824292.00, indep_year=1990, population=1726000, life_expectancy=42.5, gnp=3101.00, gnp_old=3384.00, local_name='Namibia', government_form='Republic', head_of_state='Sam Nujoma',capital=None,code2='NA')
NAM.save() 
NRU = Country(code='NRU', name='Nauru',continent=Oceania, region='Micronesia', surface_area=21.00, indep_year=1968, population=12000, life_expectancy=60.8, gnp=197.00, gnp_old=None, local_name='Naoero/Nauru', government_form='Republic', head_of_state='Bernard Dowiyogo',capital=None,code2='NR')
NRU.save() 
NPL = Country(code='NPL', name='Nepal',continent=Asia, region='Southern and Central Asia', surface_area=147181.00, indep_year=1769, population=23930000, life_expectancy=57.8, gnp=4768.00, gnp_old=4837.00, local_name='Nepal', government_form='Constitutional Monarchy', head_of_state='Gyanendra Bir Bikram',capital=None,code2='NP')
NPL.save() 
NIC = Country(code='NIC', name='Nicaragua',continent=North_America, region='Central America', surface_area=130000.00, indep_year=1838, population=5074000, life_expectancy=68.7, gnp=1988.00, gnp_old=2023.00, local_name='Nicaragua', government_form='Republic', head_of_state='Arnoldo Alemán Lacayo',capital=None,code2='NI')
NIC.save() 
NER = Country(code='NER', name='Niger',continent=Africa, region='Western Africa', surface_area=1267000.00, indep_year=1960, population=10730000, life_expectancy=41.3, gnp=1706.00, gnp_old=1580.00, local_name='Niger', government_form='Republic', head_of_state='Mamadou Tandja',capital=None,code2='NE')
NER.save() 
NGA = Country(code='NGA', name='Nigeria',continent=Africa, region='Western Africa', surface_area=923768.00, indep_year=1960, population=111506000, life_expectancy=51.6, gnp=65707.00, gnp_old=58623.00, local_name='Nigeria', government_form='Federal Republic', head_of_state='Olusegun Obasanjo',capital=None,code2='NG')
NGA.save() 
NIU = Country(code='NIU', name='Niue',continent=Oceania, region='Polynesia', surface_area=260.00, indep_year=None, population=2000, life_expectancy=None, gnp=0.00, gnp_old=None, local_name='Niue', government_form='Nonmetropolitan Territory of New Zealand', head_of_state='Elisabeth II',capital=None,code2='NU')
NIU.save() 
NFK = Country(code='NFK', name='Norfolk Island',continent=Oceania, region='Australia and New Zealand', surface_area=36.00, indep_year=None, population=2000, life_expectancy=None, gnp=0.00, gnp_old=None, local_name='Norfolk Island', government_form='Territory of Australia', head_of_state='Elisabeth II',capital=None,code2='NF')
NFK.save() 
NOR = Country(code='NOR', name='Norway',continent=Europe, region='Nordic Countries', surface_area=323877.00, indep_year=1905, population=4478500, life_expectancy=78.7, gnp=145895.00, gnp_old=153370.00, local_name='Norge', government_form='Constitutional Monarchy', head_of_state='Harald V',capital=None,code2='NO')
NOR.save() 
CIV = Country(code='CIV', name='Côte dIvoire',continent=Africa, region='Western Africa', surface_area=322463.00, indep_year=1960, population=14786000, life_expectancy=45.2, gnp=11345.00, gnp_old=10285.00, local_name='Côte dIvoire', government_form='Republic', head_of_state='Laurent Gbagbo',capital=None,code2='CI')
CIV.save() 
OMN = Country(code='OMN', name='Oman',continent=Asia, region='Middle East', surface_area=309500.00, indep_year=1951, population=2542000, life_expectancy=71.8, gnp=16904.00, gnp_old=16153.00, local_name='´Uman', government_form='Monarchy (Sultanate)', head_of_state='Qabus ibn Sa´id',capital=None,code2='OM')
OMN.save() 
PAK = Country(code='PAK', name='Pakistan',continent=Asia, region='Southern and Central Asia', surface_area=796095.00, indep_year=1947, population=156483000, life_expectancy=61.1, gnp=61289.00, gnp_old=58549.00, local_name='Pakistan', government_form='Republic', head_of_state='Mohammad Rafiq Tarar',capital=None,code2='PK')
PAK.save() 
PLW = Country(code='PLW', name='Palau',continent=Oceania, region='Micronesia', surface_area=459.00, indep_year=1994, population=19000, life_expectancy=68.6, gnp=105.00, gnp_old=None, local_name='Belau/Palau', government_form='Republic', head_of_state='Kuniwo Nakamura',capital=None,code2='PW')
PLW.save() 
PAN = Country(code='PAN', name='Panama',continent=North_America, region='Central America', surface_area=75517.00, indep_year=1903, population=2856000, life_expectancy=75.5, gnp=9131.00, gnp_old=8700.00, local_name='Panamá', government_form='Republic', head_of_state='Mireya Elisa Moscoso Rodríguez',capital=None,code2='PA')
PAN.save() 
PNG = Country(code='PNG', name='Papua New Guinea',continent=Oceania, region='Melanesia', surface_area=462840.00, indep_year=1975, population=4807000, life_expectancy=63.1, gnp=4988.00, gnp_old=6328.00, local_name='Papua New Guinea/Papua Niugini', government_form='Constitutional Monarchy', head_of_state='Elisabeth II',capital=None,code2='PG')
PNG.save() 
PRY = Country(code='PRY', name='Paraguay',continent=South_America, region='South America', surface_area=406752.00, indep_year=1811, population=5496000, life_expectancy=73.7, gnp=8444.00, gnp_old=9555.00, local_name='Paraguay', government_form='Republic', head_of_state='Luis Ángel González Macchi',capital=None,code2='PY')
PRY.save() 
PER = Country(code='PER', name='Peru',continent=South_America, region='South America', surface_area=1285216.00, indep_year=1821, population=25662000, life_expectancy=70.0, gnp=64140.00, gnp_old=65186.00, local_name='Perú/Piruw', government_form='Republic', head_of_state='Valentin Paniagua Corazao',capital=None,code2='PE')
PER.save() 
PCN = Country(code='PCN', name='Pitcairn',continent=Oceania, region='Polynesia', surface_area=49.00, indep_year=None, population=50, life_expectancy=None, gnp=0.00, gnp_old=None, local_name='Pitcairn', government_form='Dependent Territory of the UK', head_of_state='Elisabeth II',capital=None,code2='PN')
PCN.save() 
MNP = Country(code='MNP', name='Northern Mariana Islands',continent=Oceania, region='Micronesia', surface_area=464.00, indep_year=None, population=78000, life_expectancy=75.5, gnp=0.00, gnp_old=None, local_name='Northern Mariana Islands', government_form='Commonwealth of the US', head_of_state='George W. Bush',capital=None,code2='MP')
MNP.save() 
PRT = Country(code='PRT', name='Portugal',continent=Europe, region='Southern Europe', surface_area=91982.00, indep_year=1143, population=9997600, life_expectancy=75.8, gnp=105954.00, gnp_old=102133.00, local_name='Portugal', government_form='Republic', head_of_state='Jorge Sampãio',capital=None,code2='PT')
PRT.save() 
PRI = Country(code='PRI', name='Puerto Rico',continent=North_America, region='Caribbean', surface_area=8875.00, indep_year=None, population=3869000, life_expectancy=75.6, gnp=34100.00, gnp_old=32100.00, local_name='Puerto Rico', government_form='Commonwealth of the US', head_of_state='George W. Bush',capital=None,code2='PR')
PRI.save() 
POL = Country(code='POL', name='Poland',continent=Europe, region='Eastern Europe', surface_area=323250.00, indep_year=1918, population=38653600, life_expectancy=73.2, gnp=151697.00, gnp_old=135636.00, local_name='Polska', government_form='Republic', head_of_state='Aleksander Kwasniewski',capital=None,code2='PL')
POL.save() 
GNQ = Country(code='GNQ', name='Equatorial Guinea',continent=Africa, region='Central Africa', surface_area=28051.00, indep_year=1968, population=453000, life_expectancy=53.6, gnp=283.00, gnp_old=542.00, local_name='Guinea Ecuatorial', government_form='Republic', head_of_state='Teodoro Obiang Nguema Mbasogo',capital=None,code2='GQ')
GNQ.save() 
QAT = Country(code='QAT', name='Qatar',continent=Asia, region='Middle East', surface_area=11000.00, indep_year=1971, population=599000, life_expectancy=72.4, gnp=9472.00, gnp_old=8920.00, local_name='Qatar', government_form='Monarchy', head_of_state='Hamad ibn Khalifa al-Thani',capital=None,code2='QA')
QAT.save() 
FRA = Country(code='FRA', name='France',continent=Europe, region='Western Europe', surface_area=551500.00, indep_year=843, population=59225700, life_expectancy=78.8, gnp=1424285.00, gnp_old=1392448.00, local_name='France', government_form='Republic', head_of_state='Jacques Chirac',capital=None,code2='FR')
FRA.save() 
GUF = Country(code='GUF', name='French Guiana',continent=South_America, region='South America', surface_area=90000.00, indep_year=None, population=181000, life_expectancy=76.1, gnp=681.00, gnp_old=None, local_name='Guyane française', government_form='Overseas Department of France', head_of_state='Jacques Chirac',capital=None,code2='GF')
GUF.save() 
PYF = Country(code='PYF', name='French Polynesia',continent=Oceania, region='Polynesia', surface_area=4000.00, indep_year=None, population=235000, life_expectancy=74.8, gnp=818.00, gnp_old=781.00, local_name='Polynésie française', government_form='Nonmetropolitan Territory of France', head_of_state='Jacques Chirac',capital=None,code2='PF')
PYF.save() 
REU = Country(code='REU', name='Réunion',continent=Africa, region='Eastern Africa', surface_area=2510.00, indep_year=None, population=699000, life_expectancy=72.7, gnp=8287.00, gnp_old=7988.00, local_name='Réunion', government_form='Overseas Department of France', head_of_state='Jacques Chirac',capital=None,code2='RE')
REU.save() 
ROM = Country(code='ROM', name='Romania',continent=Europe, region='Eastern Europe', surface_area=238391.00, indep_year=1878, population=22455500, life_expectancy=69.9, gnp=38158.00, gnp_old=34843.00, local_name='România', government_form='Republic', head_of_state='Ion Iliescu',capital=None,code2='RO')
ROM.save() 
RWA = Country(code='RWA', name='Rwanda',continent=Africa, region='Eastern Africa', surface_area=26338.00, indep_year=1962, population=7733000, life_expectancy=39.3, gnp=2036.00, gnp_old=1863.00, local_name='Rwanda/Urwanda', government_form='Republic', head_of_state='Paul Kagame',capital=None,code2='RW')
RWA.save() 
SWE = Country(code='SWE', name='Sweden',continent=Europe, region='Nordic Countries', surface_area=449964.00, indep_year=836, population=8861400, life_expectancy=79.6, gnp=226492.00, gnp_old=227757.00, local_name='Sverige', government_form='Constitutional Monarchy', head_of_state='Carl XVI Gustaf',capital=None,code2='SE')
SWE.save() 
SHN = Country(code='SHN', name='Saint Helena',continent=Africa, region='Western Africa', surface_area=314.00, indep_year=None, population=6000, life_expectancy=76.8, gnp=0.00, gnp_old=None, local_name='Saint Helena', government_form='Dependent Territory of the UK', head_of_state='Elisabeth II',capital=None,code2='SH')
SHN.save() 
KNA = Country(code='KNA', name='Saint Kitts and Nevis',continent=North_America, region='Caribbean', surface_area=261.00, indep_year=1983, population=38000, life_expectancy=70.7, gnp=299.00, gnp_old=None, local_name='Saint Kitts and Nevis', government_form='Constitutional Monarchy', head_of_state='Elisabeth II',capital=None,code2='KN')
KNA.save() 
LCA = Country(code='LCA', name='Saint Lucia',continent=North_America, region='Caribbean', surface_area=622.00, indep_year=1979, population=154000, life_expectancy=72.3, gnp=571.00, gnp_old=None, local_name='Saint Lucia', government_form='Constitutional Monarchy', head_of_state='Elisabeth II',capital=None,code2='LC')
LCA.save() 
VCT = Country(code='VCT', name='Saint Vincent and the Grenadines',continent=North_America, region='Caribbean', surface_area=388.00, indep_year=1979, population=114000, life_expectancy=72.3, gnp=285.00, gnp_old=None, local_name='Saint Vincent and the Grenadines', government_form='Constitutional Monarchy', head_of_state='Elisabeth II',capital=None,code2='VC')
VCT.save() 
SPM = Country(code='SPM', name='Saint Pierre and Miquelon',continent=North_America, region='North America', surface_area=242.00, indep_year=None, population=7000, life_expectancy=77.6, gnp=0.00, gnp_old=None, local_name='Saint-Pierre-et-Miquelon', government_form='Territorial Collectivity of France', head_of_state='Jacques Chirac',capital=None,code2='PM')
SPM.save() 
DEU = Country(code='DEU', name='Germany',continent=Europe, region='Western Europe', surface_area=357022.00, indep_year=1955, population=82164700, life_expectancy=77.4, gnp=2133367.00, gnp_old=2102826.00, local_name='Deutschland', government_form='Federal Republic', head_of_state='Johannes Rau',capital=None,code2='DE')
DEU.save() 
SLB = Country(code='SLB', name='Solomon Islands',continent=Oceania, region='Melanesia', surface_area=28896.00, indep_year=1978, population=444000, life_expectancy=71.3, gnp=182.00, gnp_old=220.00, local_name='Solomon Islands', government_form='Constitutional Monarchy', head_of_state='Elisabeth II',capital=None,code2='SB')
SLB.save() 
ZMB = Country(code='ZMB', name='Zambia',continent=Africa, region='Eastern Africa', surface_area=752618.00, indep_year=1964, population=9169000, life_expectancy=37.2, gnp=3377.00, gnp_old=3922.00, local_name='Zambia', government_form='Republic', head_of_state='Frederick Chiluba',capital=None,code2='ZM')
ZMB.save() 
WSM = Country(code='WSM', name='Samoa',continent=Oceania, region='Polynesia', surface_area=2831.00, indep_year=1962, population=180000, life_expectancy=69.2, gnp=141.00, gnp_old=157.00, local_name='Samoa', government_form='Parlementary Monarchy', head_of_state='Malietoa Tanumafili II',capital=None,code2='WS')
WSM.save() 
SMR = Country(code='SMR', name='San Marino',continent=Europe, region='Southern Europe', surface_area=61.00, indep_year=885, population=27000, life_expectancy=81.1, gnp=510.00, gnp_old=None, local_name='San Marino', government_form='Republic', head_of_state='',capital=None,code2='SM')
SMR.save() 
STP = Country(code='STP', name='Sao Tome and Principe',continent=Africa, region='Central Africa', surface_area=964.00, indep_year=1975, population=147000, life_expectancy=65.3, gnp=6.00, gnp_old=None, local_name='São Tomé e Príncipe', government_form='Republic', head_of_state='Miguel Trovoada',capital=None,code2='ST')
STP.save() 
SAU = Country(code='SAU', name='Saudi Arabia',continent=Asia, region='Middle East', surface_area=2149690.00, indep_year=1932, population=21607000, life_expectancy=67.8, gnp=137635.00, gnp_old=146171.00, local_name='Al-´Arabiya as-Sa´udiya', government_form='Monarchy', head_of_state='Fahd ibn Abdul-Aziz al-Sa´ud',capital=None,code2='SA')
SAU.save() 
SEN = Country(code='SEN', name='Senegal',continent=Africa, region='Western Africa', surface_area=196722.00, indep_year=1960, population=9481000, life_expectancy=62.2, gnp=4787.00, gnp_old=4542.00, local_name='Sénégal/Sounougal', government_form='Republic', head_of_state='Abdoulaye Wade',capital=None,code2='SN')
SEN.save() 
SYC = Country(code='SYC', name='Seychelles',continent=Africa, region='Eastern Africa', surface_area=455.00, indep_year=1976, population=77000, life_expectancy=70.4, gnp=536.00, gnp_old=539.00, local_name='Sesel/Seychelles', government_form='Republic', head_of_state='France-Albert René',capital=None,code2='SC')
SYC.save() 
SLE = Country(code='SLE', name='Sierra Leone',continent=Africa, region='Western Africa', surface_area=71740.00, indep_year=1961, population=4854000, life_expectancy=45.3, gnp=746.00, gnp_old=858.00, local_name='Sierra Leone', government_form='Republic', head_of_state='Ahmed Tejan Kabbah',capital=None,code2='SL')
SLE.save() 
SGP = Country(code='SGP', name='Singapore',continent=Asia, region='Southeast Asia', surface_area=618.00, indep_year=1965, population=3567000, life_expectancy=80.1, gnp=86503.00, gnp_old=96318.00, local_name='Singapore/Singapura/Xinjiapo/Singapur', government_form='Republic', head_of_state='Sellapan Rama Nathan',capital=None,code2='SG')
SGP.save() 
SVK = Country(code='SVK', name='Slovakia',continent=Europe, region='Eastern Europe', surface_area=49012.00, indep_year=1993, population=5398700, life_expectancy=73.7, gnp=20594.00, gnp_old=19452.00, local_name='Slovensko', government_form='Republic', head_of_state='Rudolf Schuster',capital=None,code2='SK')
SVK.save() 
SVN = Country(code='SVN', name='Slovenia',continent=Europe, region='Southern Europe', surface_area=20256.00, indep_year=1991, population=1987800, life_expectancy=74.9, gnp=19756.00, gnp_old=18202.00, local_name='Slovenija', government_form='Republic', head_of_state='Milan Kucan',capital=None,code2='SI')
SVN.save() 
SOM = Country(code='SOM', name='Somalia',continent=Africa, region='Eastern Africa', surface_area=637657.00, indep_year=1960, population=10097000, life_expectancy=46.2, gnp=935.00, gnp_old=None, local_name='Soomaaliya', government_form='Republic', head_of_state='Abdiqassim Salad Hassan',capital=None,code2='SO')
SOM.save() 
LKA = Country(code='LKA', name='Sri Lanka',continent=Asia, region='Southern and Central Asia', surface_area=65610.00, indep_year=1948, population=18827000, life_expectancy=71.8, gnp=15706.00, gnp_old=15091.00, local_name='Sri Lanka/Ilankai', government_form='Republic', head_of_state='Chandrika Kumaratunga',capital=None,code2='LK')
LKA.save() 
SDN = Country(code='SDN', name='Sudan',continent=Africa, region='Northern Africa', surface_area=2505813.00, indep_year=1956, population=29490000, life_expectancy=56.6, gnp=10162.00, gnp_old=None, local_name='As-Sudan', government_form='Islamic Republic', head_of_state='Omar Hassan Ahmad al-Bashir',capital=None,code2='SD')
SDN.save() 
FIN = Country(code='FIN', name='Finland',continent=Europe, region='Nordic Countries', surface_area=338145.00, indep_year=1917, population=5171300, life_expectancy=77.4, gnp=121914.00, gnp_old=119833.00, local_name='Suomi', government_form='Republic', head_of_state='Tarja Halonen',capital=None,code2='FI')
FIN.save() 
SUR = Country(code='SUR', name='Suriname',continent=South_America, region='South America', surface_area=163265.00, indep_year=1975, population=417000, life_expectancy=71.4, gnp=870.00, gnp_old=706.00, local_name='Suriname', government_form='Republic', head_of_state='Ronald Venetiaan',capital=None,code2='SR')
SUR.save() 
SWZ = Country(code='SWZ', name='Swaziland',continent=Africa, region='Southern Africa', surface_area=17364.00, indep_year=1968, population=1008000, life_expectancy=40.4, gnp=1206.00, gnp_old=1312.00, local_name='kaNgwane', government_form='Monarchy', head_of_state='Mswati III',capital=None,code2='SZ')
SWZ.save() 
CHE = Country(code='CHE', name='Switzerland',continent=Europe, region='Western Europe', surface_area=41284.00, indep_year=1499, population=7160400, life_expectancy=79.6, gnp=264478.00, gnp_old=256092.00, local_name='Schweiz/Suisse/Svizzera/Svizra', government_form='Federation', head_of_state='Adolf Ogi',capital=None,code2='CH')
CHE.save() 
SYR = Country(code='SYR', name='Syria',continent=Asia, region='Middle East', surface_area=185180.00, indep_year=1941, population=16125000, life_expectancy=68.5, gnp=65984.00, gnp_old=64926.00, local_name='Suriya', government_form='Republic', head_of_state='Bashar al-Assad',capital=None,code2='SY')
SYR.save() 
TJK = Country(code='TJK', name='Tajikistan',continent=Asia, region='Southern and Central Asia', surface_area=143100.00, indep_year=1991, population=6188000, life_expectancy=64.1, gnp=1990.00, gnp_old=1056.00, local_name='Toçikiston', government_form='Republic', head_of_state='Emomali Rahmonov',capital=None,code2='TJ')
TJK.save() 
TWN = Country(code='TWN', name='Taiwan',continent=Asia, region='Eastern Asia', surface_area=36188.00, indep_year=1945, population=22256000, life_expectancy=76.4, gnp=256254.00, gnp_old=263451.00, local_name='Tai-wan', government_form='Republic', head_of_state='Chen Shui-bian',capital=None,code2='TW')
TWN.save() 
TZA = Country(code='TZA', name='Tanzania',continent=Africa, region='Eastern Africa', surface_area=883749.00, indep_year=1961, population=33517000, life_expectancy=52.3, gnp=8005.00, gnp_old=7388.00, local_name='Tanzania', government_form='Republic', head_of_state='Benjamin William Mkapa',capital=None,code2='TZ')
TZA.save() 
DNK = Country(code='DNK', name='Denmark',continent=Europe, region='Nordic Countries', surface_area=43094.00, indep_year=800, population=5330000, life_expectancy=76.5, gnp=174099.00, gnp_old=169264.00, local_name='Danmark', government_form='Constitutional Monarchy', head_of_state='Margrethe II',capital=None,code2='DK')
DNK.save() 
THA = Country(code='THA', name='Thailand',continent=Asia, region='Southeast Asia', surface_area=513115.00, indep_year=1350, population=61399000, life_expectancy=68.6, gnp=116416.00, gnp_old=153907.00, local_name='Prathet Thai', government_form='Constitutional Monarchy', head_of_state='Bhumibol Adulyadej',capital=None,code2='TH')
THA.save() 
TGO = Country(code='TGO', name='Togo',continent=Africa, region='Western Africa', surface_area=56785.00, indep_year=1960, population=4629000, life_expectancy=54.7, gnp=1449.00, gnp_old=1400.00, local_name='Togo', government_form='Republic', head_of_state='Gnassingbé Eyadéma',capital=None,code2='TG')
TGO.save() 
TKL = Country(code='TKL', name='Tokelau',continent=Oceania, region='Polynesia', surface_area=12.00, indep_year=None, population=2000, life_expectancy=None, gnp=0.00, gnp_old=None, local_name='Tokelau', government_form='Nonmetropolitan Territory of New Zealand', head_of_state='Elisabeth II',capital=None,code2='TK')
TKL.save() 
TON = Country(code='TON', name='Tonga',continent=Oceania, region='Polynesia', surface_area=650.00, indep_year=1970, population=99000, life_expectancy=67.9, gnp=146.00, gnp_old=170.00, local_name='Tonga', government_form='Monarchy', head_of_state='Taufa\'ahau Tupou IV',capital=None,code2='TO')
TON.save() 
TTO = Country(code='TTO', name='Trinidad and Tobago',continent=North_America, region='Caribbean', surface_area=5130.00, indep_year=1962, population=1295000, life_expectancy=68.0, gnp=6232.00, gnp_old=5867.00, local_name='Trinidad and Tobago', government_form='Republic', head_of_state='Arthur N. R. Robinson',capital=None,code2='TT')
TTO.save() 
TCD = Country(code='TCD', name='Chad',continent=Africa, region='Central Africa', surface_area=1284000.00, indep_year=1960, population=7651000, life_expectancy=50.5, gnp=1208.00, gnp_old=1102.00, local_name='Tchad/Tshad', government_form='Republic', head_of_state='Idriss Déby',capital=None,code2='TD')
TCD.save() 
CZE = Country(code='CZE', name='Czech Republic',continent=Europe, region='Eastern Europe', surface_area=78866.00, indep_year=1993, population=10278100, life_expectancy=74.5, gnp=55017.00, gnp_old=52037.00, local_name='¸esko', government_form='Republic', head_of_state='Václav Havel',capital=None,code2='CZ')
CZE.save() 
TUN = Country(code='TUN', name='Tunisia',continent=Africa, region='Northern Africa', surface_area=163610.00, indep_year=1956, population=9586000, life_expectancy=73.7, gnp=20026.00, gnp_old=18898.00, local_name='Tunis/Tunisie', government_form='Republic', head_of_state='Zine al-Abidine Ben Ali',capital=None,code2='TN')
TUN.save() 
TUR = Country(code='TUR', name='Turkey',continent=Asia, region='Middle East', surface_area=774815.00, indep_year=1923, population=66591000, life_expectancy=71.0, gnp=210721.00, gnp_old=189122.00, local_name='Türkiye', government_form='Republic', head_of_state='Ahmet Necdet Sezer',capital=None,code2='TR')
TUR.save() 
TKM = Country(code='TKM', name='Turkmenistan',continent=Asia, region='Southern and Central Asia', surface_area=488100.00, indep_year=1991, population=4459000, life_expectancy=60.9, gnp=4397.00, gnp_old=2000.00, local_name='Türkmenostan', government_form='Republic', head_of_state='Saparmurad Nijazov',capital=None,code2='TM')
TKM.save() 
TCA = Country(code='TCA', name='Turks and Caicos Islands',continent=North_America, region='Caribbean', surface_area=430.00, indep_year=None, population=17000, life_expectancy=73.3, gnp=96.00, gnp_old=None, local_name='The Turks and Caicos Islands', government_form='Dependent Territory of the UK', head_of_state='Elisabeth II',capital=None,code2='TC')
TCA.save() 
TUV = Country(code='TUV', name='Tuvalu',continent=Oceania, region='Polynesia', surface_area=26.00, indep_year=1978, population=12000, life_expectancy=66.3, gnp=6.00, gnp_old=None, local_name='Tuvalu', government_form='Constitutional Monarchy', head_of_state='Elisabeth II',capital=None,code2='TV')
TUV.save() 
UGA = Country(code='UGA', name='Uganda',continent=Africa, region='Eastern Africa', surface_area=241038.00, indep_year=1962, population=21778000, life_expectancy=42.9, gnp=6313.00, gnp_old=6887.00, local_name='Uganda', government_form='Republic', head_of_state='Yoweri Museveni',capital=None,code2='UG')
UGA.save() 
UKR = Country(code='UKR', name='Ukraine',continent=Europe, region='Eastern Europe', surface_area=603700.00, indep_year=1991, population=50456000, life_expectancy=66.0, gnp=42168.00, gnp_old=49677.00, local_name='Ukrajina', government_form='Republic', head_of_state='Leonid Kutma',capital=None,code2='UA')
UKR.save() 
HUN = Country(code='HUN', name='Hungary',continent=Europe, region='Eastern Europe', surface_area=93030.00, indep_year=1918, population=10043200, life_expectancy=71.4, gnp=48267.00, gnp_old=45914.00, local_name='Magyarország', government_form='Republic', head_of_state='Ferenc Mádl',capital=None,code2='HU')
HUN.save() 
URY = Country(code='URY', name='Uruguay',continent=South_America, region='South America', surface_area=175016.00, indep_year=1828, population=3337000, life_expectancy=75.2, gnp=20831.00, gnp_old=19967.00, local_name='Uruguay', government_form='Republic', head_of_state='Jorge Batlle Ibáñez',capital=None,code2='UY')
URY.save() 
NCL = Country(code='NCL', name='New Caledonia',continent=Oceania, region='Melanesia', surface_area=18575.00, indep_year=None, population=214000, life_expectancy=72.8, gnp=3563.00, gnp_old=None, local_name='Nouvelle-Calédonie', government_form='Nonmetropolitan Territory of France', head_of_state='Jacques Chirac',capital=None,code2='NC')
NCL.save() 
NZL = Country(code='NZL', name='New Zealand',continent=Oceania, region='Australia and New Zealand', surface_area=270534.00, indep_year=1907, population=3862000, life_expectancy=77.8, gnp=54669.00, gnp_old=64960.00, local_name='New Zealand/Aotearoa', government_form='Constitutional Monarchy', head_of_state='Elisabeth II',capital=None,code2='NZ')
NZL.save() 
UZB = Country(code='UZB', name='Uzbekistan',continent=Asia, region='Southern and Central Asia', surface_area=447400.00, indep_year=1991, population=24318000, life_expectancy=63.7, gnp=14194.00, gnp_old=21300.00, local_name='Uzbekiston', government_form='Republic', head_of_state='Islam Karimov',capital=None,code2='UZ')
UZB.save() 
BLR = Country(code='BLR', name='Belarus',continent=Europe, region='Eastern Europe', surface_area=207600.00, indep_year=1991, population=10236000, life_expectancy=68.0, gnp=13714.00, gnp_old=None, local_name='Belarus', government_form='Republic', head_of_state='Aljaksandr Lukaenka',capital=None,code2='BY')
BLR.save() 
WLF = Country(code='WLF', name='Wallis and Futuna',continent=Oceania, region='Polynesia', surface_area=200.00, indep_year=None, population=15000, life_expectancy=None, gnp=0.00, gnp_old=None, local_name='Wallis-et-Futuna', government_form='Nonmetropolitan Territory of France', head_of_state='Jacques Chirac',capital=None,code2='WF')
WLF.save() 
VUT = Country(code='VUT', name='Vanuatu',continent=Oceania, region='Melanesia', surface_area=12189.00, indep_year=1980, population=190000, life_expectancy=60.6, gnp=261.00, gnp_old=246.00, local_name='Vanuatu', government_form='Republic', head_of_state='John Bani',capital=None,code2='VU')
VUT.save() 
VAT = Country(code='VAT', name='Holy See (Vatican City State)',continent=Europe, region='Southern Europe', surface_area=0.40, indep_year=1929, population=1000, life_expectancy=None, gnp=9.00, gnp_old=None, local_name='Santa Sede/Città del Vaticano', government_form='Independent Church State', head_of_state='Johannes Paavali II',capital=None,code2='VA')
VAT.save() 
VEN = Country(code='VEN', name='Venezuela',continent=South_America, region='South America', surface_area=912050.00, indep_year=1811, population=24170000, life_expectancy=73.1, gnp=95023.00, gnp_old=88434.00, local_name='Venezuela', government_form='Federal Republic', head_of_state='Hugo Chávez Frías',capital=None,code2='VE')
VEN.save() 
RUS = Country(code='RUS', name='Russian Federation',continent=Europe, region='Eastern Europe', surface_area=17075400.00, indep_year=1991, population=146934000, life_expectancy=67.2, gnp=276608.00, gnp_old=442989.00, local_name='Rossija', government_form='Federal Republic', head_of_state='Vladimir Putin',capital=None,code2='RU')
RUS.save() 
VNM = Country(code='VNM', name='Vietnam',continent=Asia, region='Southeast Asia', surface_area=331689.00, indep_year=1945, population=79832000, life_expectancy=69.3, gnp=21929.00, gnp_old=22834.00, local_name='Viêt Nam', government_form='Socialistic Republic', head_of_state='Trân Duc Luong',capital=None,code2='VN')
VNM.save() 
EST = Country(code='EST', name='Estonia',continent=Europe, region='Baltic Countries', surface_area=45227.00, indep_year=1991, population=1439200, life_expectancy=69.5, gnp=5328.00, gnp_old=3371.00, local_name='Eesti', government_form='Republic', head_of_state='Lennart Meri',capital=None,code2='EE')
EST.save() 
USA = Country(code='USA', name='United States',continent=North_America, region='North America', surface_area=9363520.00, indep_year=1776, population=278357000, life_expectancy=77.1, gnp=8510700.00, gnp_old=8110900.00, local_name='United States', government_form='Federal Republic', head_of_state='George W. Bush',capital=None,code2='US')
USA.save() 
VIR = Country(code='VIR', name='Virgin Islands, U.S.',continent=North_America, region='Caribbean', surface_area=347.00, indep_year=None, population=93000, life_expectancy=78.1, gnp=0.00, gnp_old=None, local_name='Virgin Islands of the United States', government_form='US Territory', head_of_state='George W. Bush',capital=None,code2='VI')
VIR.save() 
ZWE = Country(code='ZWE', name='Zimbabwe',continent=Africa, region='Eastern Africa', surface_area=390757.00, indep_year=1980, population=11669000, life_expectancy=37.8, gnp=5951.00, gnp_old=8670.00, local_name='Zimbabwe', government_form='Republic', head_of_state='Robert G. Mugabe',capital=None,code2='ZW')
ZWE.save() 
PSE = Country(code='PSE', name='Palestine',continent=Asia, region='Middle East', surface_area=6257.00, indep_year=None, population=3101000, life_expectancy=71.4, gnp=4173.00, gnp_old=None, local_name='Filastin', government_form='Autonomous Area', head_of_state='Yasser (Yasir) Arafat',capital=None,code2='PS')
PSE.save() 
ATA = Country(code='ATA', name='Antarctica',continent=Antarctica, region='Antarctica', surface_area=13120000.00, indep_year=None, population=0, life_expectancy=None, gnp=0.00, gnp_old=None, local_name='', government_form='Co-administrated', head_of_state='',capital=None,code2='AQ')
ATA.save() 
BVT = Country(code='BVT', name='Bouvet Island',continent=Antarctica, region='Antarctica', surface_area=59.00, indep_year=None, population=0, life_expectancy=None, gnp=0.00, gnp_old=None, local_name='Bouvetøya', government_form='Dependent Territory of Norway', head_of_state='Harald V',capital=None,code2='BV')
BVT.save() 
IOT = Country(code='IOT', name='British Indian Ocean Territory',continent=Africa, region='Eastern Africa', surface_area=78.00, indep_year=None, population=0, life_expectancy=None, gnp=0.00, gnp_old=None, local_name='British Indian Ocean Territory', government_form='Dependent Territory of the UK', head_of_state='Elisabeth II',capital=None,code2='IO')
IOT.save() 
SGS = Country(code='SGS', name='South Georgia and the South Sandwich Islands',continent=Antarctica, region='Antarctica', surface_area=3903.00, indep_year=None, population=0, life_expectancy=None, gnp=0.00, gnp_old=None, local_name='South Georgia and the South Sandwich Islands', government_form='Dependent Territory of the UK', head_of_state='Elisabeth II',capital=None,code2='GS')
SGS.save() 
HMD = Country(code='HMD', name='Heard Island and McDonald Islands',continent=Antarctica, region='Antarctica', surface_area=359.00, indep_year=None, population=0, life_expectancy=None, gnp=0.00, gnp_old=None, local_name='Heard and McDonald Islands', government_form='Territory of Australia', head_of_state='Elisabeth II',capital=None,code2='HM')
HMD.save() 
ATF = Country(code='ATF', name='French Southern territories',continent=Antarctica, region='Antarctica', surface_area=7780.00, indep_year=None, population=0, life_expectancy=None, gnp=0.00, gnp_old=None, local_name='Terres australes françaises', government_form='Nonmetropolitan Territory of France', head_of_state='Jacques Chirac',capital=None,code2='TF')
ATF.save() 
UMI = Country(code='UMI', name='United States Minor Outlying Islands',continent=Oceania, region='Micronesia/Caribbean', surface_area=16.00, indep_year=None, population=0, life_expectancy=None, gnp=0.00, gnp_old=None, local_name='United States Minor Outlying Islands', government_form='Dependent Territory of the US', head_of_state='George W. Bush',capital=None,code2='UM')
UMI.save() 
"""
AFG.capital=1
NLD.capital=5
ANT.capital=33
ALB.capital=34
DZA.capital=35
ASM.capital=54
AND.capital=55
AGO.capital=56
AIA.capital=62
ATG.capital=63
ARE.capital=65
ARG.capital=69
ARM.capital=126
ABW.capital=129
AUS.capital=135
AZE.capital=144
BHS.capital=148
BHR.capital=149
BGD.capital=150
BRB.capital=174
BEL.capital=179
BLZ.capital=185
BEN.capital=187
BMU.capital=191
BTN.capital=192
BOL.capital=194
BIH.capital=201
BWA.capital=204
BRA.capital=211
GBR.capital=456
VGB.capital=537
BRN.capital=538
BGR.capital=539
BFA.capital=549
BDI.capital=552
CYM.capital=553
CHL.capital=554
COK.capital=583
CRI.capital=584
DJI.capital=585
DMA.capital=586
DOM.capital=587
ECU.capital=594
EGY.capital=608
SLV.capital=645
ERI.capital=652
ESP.capital=653
ZAF.capital=716
ETH.capital=756
FLK.capital=763
FJI.capital=764
PHL.capital=766
FRO.capital=901
GAB.capital=902
GMB.capital=904
GEO.capital=905
GHA.capital=910
GIB.capital=915
GRD.capital=916
GRL.capital=917
GLP.capital=919
GUM.capital=921
GTM.capital=922
GIN.capital=926
GNB.capital=927
GUY.capital=928
HTI.capital=929
HND.capital=933
HKG.capital=937
SJM.capital=938
IDN.capital=939
IND.capital=1109
IRQ.capital=1365
IRN.capital=1380
IRL.capital=1447
ISL.capital=1449
ISR.capital=1450
ITA.capital=1464
TMP.capital=1522
AUT.capital=1523
JAM.capital=1530
JPN.capital=1532
YEM.capital=1780
JOR.capital=1786
CXR.capital=1791
YUG.capital=1792
KHM.capital=1800
CMR.capital=1804
CAN.capital=1822
CPV.capital=1859
KAZ.capital=1864
KEN.capital=1881
CAF.capital=1889
CHN.capital=1891
KGZ.capital=2253
KIR.capital=2256
COL.capital=2257
COM.capital=2295
COG.capital=2296
COD.capital=2298
CCK.capital=2317
PRK.capital=2318
KOR.capital=2331
GRC.capital=2401
HRV.capital=2409
CUB.capital=2413
KWT.capital=2429
CYP.capital=2430
LAO.capital=2432
LVA.capital=2434
LSO.capital=2437
LBN.capital=2438
LBR.capital=2440
LBY.capital=2441
LIE.capital=2446
LTU.capital=2447
LUX.capital=2452
ESH.capital=2453
MAC.capital=2454
MDG.capital=2455
MKD.capital=2460
MWI.capital=2462
MDV.capital=2463
MYS.capital=2464
MLI.capital=2482
MLT.capital=2484
MAR.capital=2486
MHL.capital=2507
MTQ.capital=2508
MRT.capital=2509
MUS.capital=2511
MYT.capital=2514
MEX.capital=2515
FSM.capital=2689
MDA.capital=2690
MCO.capital=2695
MNG.capital=2696
MSR.capital=2697
MOZ.capital=2698
MMR.capital=2710
NAM.capital=2726
NRU.capital=2728
NPL.capital=2729
NIC.capital=2734
NER.capital=2738
NGA.capital=2754
NIU.capital=2805
NFK.capital=2806
NOR.capital=2807
CIV.capital=2814
OMN.capital=2821
PAK.capital=2831
PLW.capital=2881
PAN.capital=2882
PNG.capital=2884
PRY.capital=2885
PER.capital=2890
PCN.capital=2912
MNP.capital=2913
PRT.capital=2914
PRI.capital=2919
POL.capital=2928
GNQ.capital=2972
QAT.capital=2973
FRA.capital=2974
GUF.capital=3014
PYF.capital=3016
REU.capital=3017
ROM.capital=3018
RWA.capital=3047
SWE.capital=3048
SHN.capital=3063
KNA.capital=3064
LCA.capital=3065
VCT.capital=3066
SPM.capital=3067
DEU.capital=3068
SLB.capital=3161
ZMB.capital=3162
WSM.capital=3169
SMR.capital=3171
STP.capital=3172
SAU.capital=3173
SEN.capital=3198
SYC.capital=3206
SLE.capital=3207
SGP.capital=3208
SVK.capital=3209
SVN.capital=3212
SOM.capital=3214
LKA.capital=3217
SDN.capital=3225
FIN.capital=3236
SUR.capital=3243
SWZ.capital=3244
CHE.capital=3248
SYR.capital=3250
TJK.capital=3261
TWN.capital=3263
TZA.capital=3306
DNK.capital=3315
THA.capital=3320
TGO.capital=3332
TKL.capital=3333
TON.capital=3334
TTO.capital=3336
TCD.capital=3337
CZE.capital=3339
TUN.capital=3349
TUR.capital=3358
TKM.capital=3419
TCA.capital=3423
TUV.capital=3424
UGA.capital=3425
UKR.capital=3426
HUN.capital=3483
URY.capital=3492
NCL.capital=3493
NZL.capital=3499
UZB.capital=3503
BLR.capital=3520
WLF.capital=3536
VUT.capital=3537
VAT.capital=3538
VEN.capital=3539
RUS.capital=3580
VNM.capital=3770
EST.capital=3791
USA.capital=3813
VIR.capital=4067
ZWE.capital=4068
PSE.capital=4074
"""
