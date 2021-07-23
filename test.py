dict = {
    "id" : [0,1,2,3],
    "port" : [1111,2222,3333,4444],
    "ip" : ["0.0.0.0","1.1.1.1","2.2.2.2","3.3.3.3"]
}
print(len(dict["id"]))
for x in range(len(dict["id"])):
    print(f"""id: {dict["id"][x]} | port: {dict["port"][x]} | ip: {dict["ip"][x]}""")