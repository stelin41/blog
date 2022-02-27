import qrcode

paths = [
"A1", "A2", "A3", "A4", "A5",
"B1", "B2", "B3", "B4", "B5",
"C1", "C2", "C3", "C4", "C5",
"D1", "D2", "D3", "D4", "D5",
"F1", "F2", "F3", "F4", "F5",
]

for path in paths:
    img = qrcode.make('https://stelin41.github.io/scape_room/'+path+'.html')
    img.save(path+".png")
