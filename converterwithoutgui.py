#Made Timur Ergashev this is converter without gui

byte = int(input("Enter Bytes: "))
kb = byte/1024
print("{} Kilo Bytes".format(kb))
#megabytes
byte = int(input("Enter bytes: "))
mb = byte/(1024 * 1024)
print("{} MegaBytes".format(mb))
byte = int(input("Enter bytes: "))
gb = byte/(1024 * 1024 * 1024)
#big gigabytes
print("{} Giga Bytes".format(gb))
byte = int(input("Enter bytes: "))
tb = byte/(1024 * 1024 * 1024 * 1024)
print("{} Tera Bytes".format(tb))