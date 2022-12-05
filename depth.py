entryValue = 0 
exitValue = 0 
depths = {}
father = {}
levels = {}
foundValue = False

citiesArray = [
    "Medan",
    "Lubuk Pakam",
    "Sei Rampah",
    "Tebing Tinggi",
    "Pematangsiantar",
    "Saribudolok",
    "Parapat",
    "Ambarita",
    "Kabanjahe",
    "Berastagi",
    "Balige",
    "Tarutung",
    "Dolok Sanggul",
    "Padang Sidempuan", 
    "Batangtoru",
    "Sipirok",
    "Sibolga",
    "Barus",
    "Sidikalang",
    "Gunungtua",
    "Paropo",
    "Merek",
    "Siborongborong",
]

citiesRoutes = {
   "Medan": ["Lubuk Pakam", "Pematangsiantar", "Saribudolok"],
   "Lubuk Pakam": ["Medan", "Pematangsiantar", "Sei Rampah"],
   "Sei Rampah": ["Lubuk Pakam", "Tebing Tinggi"],
   "Tebing Tinggi": ["Sei Rampah", "Pematangsiantar", "Gunungtua"],
   "Pematangsiantar": ["Medan", "Lubuk Pakam", "Tebing Tinggi", "Parapat", "Saribudolok"],
   "Saribudolok": ["Medan", "Pematangsiantar", "Parapat", "Ambarita", "Kabanjahe"],
   "Parapat": ["Saribudolok", "Pematangsiantar", "Gunungtua", "Paropo", "Dolok Sanggul", "Balige", "Ambarita"],
   "Ambarita": ["Saribudolok", "Parapat", "Balige", "Berastagi", "Kabanjahe"],
   "Kabanjahe": ["Saribudolok", "Ambarita", "Berastagi"],
   "Berastagi": ["Kabanjahe", "Ambarita", "Balige"],
   "Balige": ["Berastagi", "Ambarita", "Parapat", "Dolok Sanggul", "Tarutung"],
   "Tarutung":["Dolok Sanggul","Siborongborong","Balige","Paropo"],
   "Dolok Sanggul":["Balige","Tarutung","Paropo","Parapat"],
   "Padang Sidempuan":["Batangtoru","Sipirok"],
   "Batangtoru":["Sipirok","Padang Sidempuan","Sibolga"],
   "Sipirok":["Batangtoru","Padang Sidempuan","Sibolga","Gunungtua"],
   "Sibolga":["Sidikalang","Barus","Batangtoru","Sipirok"],
   "Barus":[ "Sidikalang","Sibolga"],
   "Sidikalang":["Gunungtua","Paropo","Merek","Barus","Sibolga"],
   "Gunungtua": ["Sidikalang", "Sipirok","Tebing Tinggi","Parapat","Paropo" ],
   "Paropo": ["Sidikalang","Merek","Gunungtua","Parapat","Dolok Sanggul","Tarutung","Siborongborong" ],
   "Merek": ["Siborongborong","Sidikalang","Paropo"],
   "Siborongborong":["Merek","Paropo","Tarutung" ],
}

def depth_search(graph, selectedCity, selectedEndingCity):
    father[selectedCity] = None
    call_to_depth_search(graph, selectedCity, 1, selectedEndingCity)

def call_to_depth_search(graph, city, level, selectedEndingCity):
    global entryValue, exitValue, foundValue
    if foundValue == True:
        return
    if city == selectedEndingCity:
        foundValue = True
    entryValue += 1
    depths[city] = [entryValue, None]
    levels[city] = level

    children = 0

    if foundValue == False:
        for neighbor in graph.get(city):
            if not depths.get(neighbor):
                father[neighbor] = city
                children += 1
                call_to_depth_search(graph, neighbor, level + 1, selectedEndingCity)

        
    exitValue += 1
    depths[city][1] = exitValue

print("Pilih kota keberangkatan : \n")

i = 0

while i < len(citiesArray):
    nextItem = str(i+1)
    print(nextItem + " - " + citiesArray[i])
    i+=1

print()
selectedCityId = int(input())
selectedCityId-=1

selectedCity = citiesArray[selectedCityId]

print("Pilih kota tujuan : \n")

i = 0

while i < len(citiesArray):
    nextItem = str(i+1)
    print(nextItem + " - " + citiesArray[i])
    i+=1

print()
selectedEndingCityId = int(input())
selectedEndingCityId-=1

selectedEndingCity = citiesArray[selectedEndingCityId]

print()

depth_search(citiesRoutes, selectedCity, selectedEndingCity)

print(levels)
print(depths)
