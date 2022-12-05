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

def search(graph, selectedCity, selectedEndingCity):
    queue = [] 
    visited = {}
    l = 1 
    level = {} 

    queue.append(selectedCity)
    visited[selectedCity] = l 
    level[selectedCity] = 0 

    while len(queue):
        city = queue.pop(0)
        for route in graph.get(city):
            if not visited.get(route):
                queue.append(route)
                l += 1
                visited[route] = l
                level[route] = level[city] + 1
                if route == selectedEndingCity:
                    return visited

    print("Gagal, rute tidak ditemukan")
    return visited

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

visited = search(citiesRoutes, selectedCity, selectedEndingCity)

print(visited)
    