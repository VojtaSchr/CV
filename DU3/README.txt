PROGRAM K NALEZENÍ ADRESY NEJVZDÁLENĚJŠÍ OD KONTEJNERU

Program umí zjistit a vypsat adresu, která je nejdále od kontejneru a určit jejich vzdálenost. Také umí vypočítat medián a průměr vzdáleností
všech adres od nejbližšího kontejneru.

VSTUP
Program získává data z dvou souborů typu .geojson.
První obsahující data o adresách musí být pojmenovaný adresy.geojson, druhý s údaji o kontejnerech se musí jmenovat kontejnery.geojson.

VÝSTUP
Jako první program vypíše do konzele informace o vstupních datech, a to počet záznamů v nich obsažený.
Následně běh programu trvá několik sekund, než vypíše do konzole získané údaje.
První zobrazí průměr vzdáleností adres od nejbližšího kontejneru, poté adresu od které je nejbližší kontejner vzdálen nejvíce a jeho vzdálenost.
Poslední zobrazený údaj je medián vzdáleností adres od nejbližšího kontejneru.

Program vytvoří výsledky i s započítáním privátních kontejnerů.
A vytvoří soubor typu geojson pojmenovaný adresy_kontejnery s adresami a ID nejbližšího kontejneru.
Nakonec program vypíše DONE a skončí.

Dodatečné možnosti:
Program umožnuje zobrazit do konzole i další údaje a to:
		Množství veřejně přístupných kontejnerů 		
		Množství privátních kontejnerů				
		Množství adres závyslých na veřejných kontejnerech	
		Množství adres s privátním kontejnerem			
	Tyto údaje se zobrazí po odstranění symbolu mřížky (#) na začátku příslušného řádku.