import pings
import time
while True:
	start_time = time.time()

	filein = open("daftarIP.txt", "r")
	allstatus = filein.readlines()
	filein.close()

	#daftar IP server tujuan 
	s1 = allstatus[1][0:(len(allstatus[1])-1)]
	s2 = allstatus[3][0:(len(allstatus[3])-1)]
	s3 = allstatus[5][0:(len(allstatus[5])-1)]
	s4 = allstatus[7][0:(len(allstatus[7])-1)]
	s5 = allstatus[9][0:(len(allstatus[9])-1)]
	s6 = allstatus[11][0:(len(allstatus[11])-1)]
	s7 = allstatus[13][0:(len(allstatus[13])-1)]
	s8 = allstatus[15][0:(len(allstatus[15])-1)]
	s9 = allstatus[17][0:(len(allstatus[17])-1)]
	s10 = allstatus[19][0:(len(allstatus[19])-1)]
	s11 = allstatus[21][0:(len(allstatus[21])-1)]
	s12 = allstatus[21][0:(len(allstatus[21])-1)]
	s13 = allstatus[23][0:(len(allstatus[23])-1)]
	s14 = allstatus[25][0:(len(allstatus[25])-1)]
	s15 = allstatus[27][0:(len(allstatus[27])-1)]

	#daftar nama server tujuan
	n1 = allstatus[0][0:(len(allstatus[0])-1)]
	n2 = allstatus[2][0:(len(allstatus[2])-1)]
	n3 = allstatus[4][0:(len(allstatus[4])-1)]
	n4 = allstatus[6][0:(len(allstatus[6])-1)]
	n5 = allstatus[8][0:(len(allstatus[8])-1)]
	n6 = allstatus[10][0:(len(allstatus[10])-1)]
	n7 = allstatus[12][0:(len(allstatus[12])-1)]
	n8 = allstatus[14][0:(len(allstatus[14])-1)]
	n9 = allstatus[16][0:(len(allstatus[16])-1)]
	n10 = allstatus[18][0:(len(allstatus[18])-1)]
	n11 = allstatus[20][0:(len(allstatus[20])-1)]
	n12 = allstatus[22][0:(len(allstatus[22])-1)]
	n13 = allstatus[24][0:(len(allstatus[24])-1)]
	n14 = allstatus[26][0:(len(allstatus[26])-1)]
	n15 = allstatus[28][0:(len(allstatus[28])-1)]
	
	
	serverIPLists = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15]
	serverNameLists = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15]
	status = []
	pingTimes = 5

	#melakukan looping untuk PING masing2 domain/IP
	print("Pinging all IP listed, each IP will be pinged " + str(pingTimes) + " times.\n")
	for i in range(len(serverIPLists)):
		p = pings.Ping()
		print("=================" + serverNameLists[i] + "===============")
		response = p.ping(serverIPLists[i], times = pingTimes)
		print("reachable :" + str(response.is_reached()))
		status.append(response.is_reached())

	theTime=time.strftime("%H:%M:%S", time.localtime())
	start_time_write = time.time()
	fileout = open("result.txt", "w")
	for i in range(len(serverIPLists)):
		fileout.write(serverNameLists[i] + "\n"+ str(status[i]) + "\n")
	fileout.write(theTime)
	fileout.close()

	print("----write time: %s seconds ----" % (time.time() - start_time_write))
	print("----overall time: %s seconds ----" % (time.time() - start_time))
	time.sleep(5)