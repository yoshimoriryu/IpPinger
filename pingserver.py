import pings
import time
while True:
	start_time = time.time()

	#daftar IP server tujuan 
	s1 = "10.0.104.135"
	s2 = "8.8.8.8"
	s3 = "7.7.7.7"
	s4 = "dota2.com"
	s5 = "5.5.5.5"
	s6 = "facebook.com"
	s7 = "reddit.com"
	s8 = "youtube.com"
	s9 = "comparitech.com"
	s10 = "superuser.com"
	s11 = "bagikuy.com"
	s12 = "ashura.id"
	s13 = "detik.com"
	s14 = "netflix.com"
	s15 = "www.instagram.com"

	serverIPLists = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15]
	status = []
	pingTimes = 5

	#melakukan looping untuk PING masing2 domain/IP
	print("Pinging all IP listed, each IP will be pinged " + str(pingTimes) + " times.\n")
	for i in range(len(serverIPLists)):
		p = pings.Ping()
		print("=================" + serverIPLists[i] + "===============")
		response = p.ping(serverIPLists[i], times = pingTimes)
		print("reachable :" + str(response.is_reached()))
		status.append(response.is_reached())

	theTime=time.strftime("%H:%M:%S", time.localtime())
	start_time_write = time.time()
	fileout = open("result.txt", "w")
	for i in range(len(serverIPLists)):
		fileout.write(serverIPLists[i] + "\n"+ str(status[i]) + "\n")
	fileout.write(theTime)
	fileout.close()

	print("----write time: %s seconds ----" % (time.time() - start_time_write))
	print("----overall time: %s seconds ----" % (time.time() - start_time))
	time.sleep(5)