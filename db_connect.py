import pytds

with pytds.connect('localhost','ITPhones','Jsarmiento8','R3n4ultM3g4ne') as conn:
    with conn.cursor() as cur:
         cur.execute("SELECT DISTINCT dbo.Registration.DeviceID, dbo.Registration.IpAddress, dbo.device.MacAddress FROM dbo.Registration INNER JOIN dbo.device ON dbo.Registration.DeviceID = dbo.device.DeviceId WHERE MacAddress='110047787786720'")
         response = cur.fetchall()
         print(response)