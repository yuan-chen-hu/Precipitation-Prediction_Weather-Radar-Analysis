def high_parse():
	print("high parse all function start")
	import requests
	import numpy as np
	from bs4 import BeautifulSoup
	import time
	high_data_time= int(time.strftime("%Y%m%d%H00", time.gmtime()))
	print("old data time=",high_data_time)
	high_data_time-=(high_data_time%10000)%300
	high_data_time=str(high_data_time)
	high_data_time=high_data_time[0:4]+"/"+high_data_time[4:6]+"/"+high_data_time[6:8]+"/"+high_data_time[8:12]
	#0,3,6,9,12,15
	print("high_data_time=",high_data_time)
	high_location=[""]*2
	high_x_position=[""]*2
	high_y_position=[""]*2
	high_wind=[""]*2
	high_wind_direction=[""]*2
	high_wind_speed=[""]*2
	cloud=[""]*2

	def parsing(is_850):
		print("high parse parsing start")
		import re 
		time.sleep(10)
		soup = BeautifulSoup(driver.page_source, "html.parser")
		high_location[is_850]=soup.find_all("div")[7].find_all("p")[0].find_all("span")[0].string
		high_x_position[is_850]=high_location[is_850][0:5]
		high_y_position[is_850]=high_location[is_850][10:16]
		high_wind[is_850]=soup.find_all("div")[7].find_all("p")[1].find_all("span")[0].string
		high_wind_direction[is_850]=float(re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", high_wind[is_850][0:3])[0])
		high_wind_speed[is_850]=float(re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?",high_wind[is_850][7:])[0])
		cloud[is_850]=soup.find_all("div")[7].find_all("p")[2].find_all("span")[0].string
		print("high_location=",high_location[is_850])
		print("high_x_position=",high_x_position[is_850],"high_y_position=",high_y_position[is_850])
		print("high_wind=",high_wind[is_850])
		print("high_wind_direction=",high_wind_direction[is_850])
		print("high_wind_speed=",high_wind_speed[is_850])
		print('cloud=',cloud[is_850])
		print("high parse parsing done")
		time.sleep(10)
	def selenium_action(altitude,move_by_offset_x,move_by_offset_y,is_850):
		time.sleep(10)
		print(altitude,"hPa")
		high_url="https://www.cwb.gov.tw/cwbwifi/#"+high_data_time+"Z/wind/"+str(altitude)+"hPa/overlay=cloud/"
		print("high_url=",high_url)
		driver.get(high_url)
		time.sleep(10)
		driver.get(high_url)
		time.sleep(10)
		elem_pic = driver.find_element_by_id("foreground")
		print (elem_pic)
		print("find element done")
		action = ActionChains(driver).move_to_element(elem_pic)
		action.move_by_offset(move_by_offset_x,move_by_offset_y)
		action.click()
		action.perform()
		print("action done")
		parsing(is_850)    

	from selenium import webdriver
	from selenium.webdriver.common.action_chains import ActionChains

	driver = webdriver.Firefox()
	driver.implicitly_wait(10)
	driver.maximize_window()
	print("driver open done")
	print("500 parsring start")
	selenium_action(500,14,-29,0)#delay 50 in total
	print("850 parsing start")
	selenium_action(850,14,-29,1)#delay 50 in total
	driver.close()
	"""
	file_data_time=time.strftime("%Y%m%d%H00", time.localtime())
	import csv
	with open(("high_parsing_data_start_from="+file_data_time+"_x="+str(high_x_position[0])+"_y="+str(high_y_position[0])+'.csv'), 'a', newline='') as csvfile:    
		writer = csv.writer(csvfile, delimiter=',')
		for i in range(2):
			writer.writerow([file_data_time,high_location[0],high_x_position[0],high_y_position[0],high_wind[0],high_wind_direction[0],high_wind_speed[0],cloud[0]])
			writer.writerow([file_data_time,high_location[1],high_x_position[1],high_y_position[1],high_wind[1],high_wind_direction[1],high_wind_speed[1],cloud[1]])  
		print("csv done")
	"""
	#return high_location,high_x_position,high_y_position,high_wind,high_wind_direction,high_wind_speed,cloud     
	print("high parse all function  end ")
	return high_wind_direction,high_wind_speed

print("ALL start")
###################################gps
"""
#dai an park =25.031331,121.528056=25.0250,121.5250
#bime gps = 25.018677, 121.542856=25.0125,121.5375
#Yilan Orchard         24.665633, 121.693393
#Yilan Orchard         24.683096, 121.653693
#Yilan Orchard         24.661091, 121.640296
#yilan weather station 24.7658, 121.7483=121.73,24.78=19,-22
#suao weather station     24.5986, 121.8492=
#Taitung Orchard    22.8195203, 121.1106749
#taitung weather station     22.7540, 121.1465=121.15,22.76=4,36
#x_position=(bime_longitude-115)/0.0125
#y_position=(bime_latitude-18)/0.0125
#print ("x_position",x_position)
#print("x_position",y_position)
"""
x_position =522#dai an park
y_position =562#dai an park 


######################################## gps end            
town_url="https://www.cwb.gov.tw/V7/forecast/town368/3Hr/6300300.htm"#dai an (park)

import numpy as np
import requests
#######################timer
import time
now_local_time= int(time.strftime("%Y%m%d%H%M", time.localtime()))
print("start now_local_time=",now_local_time)

old_time=0
loop=1
time_list=np.zeros(5)

import sys 
total_error=[]

while(True):
	try:
		now=time.time()    
		if(now-old_time>240):
			old_time=now 
			print("")
			print("")        
			print("loop=",loop)
			loop+=1
	#########################timer
			print("main real time model start")
			print("download xml start")
			radar_xml_URL='https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0059-001?Authorization=CWB-AEE7A6A7-F501-4D2B-BC33-6B5053346E47&downloadType=WEB&format=XML'
			r = requests.get(radar_xml_URL)
			with open('O-A0059-001.xml','wb') as f:
				f.write(r.content)
				f.close
			print("download xml done")    
			import numpy as np
			import xml.etree.cElementTree as ET       
			try: 
				now_local_time= int(time.strftime("%Y%m%d%H%M", time.localtime()))
				print("now_local_time=",now_local_time) 
				print("read xml start")           
				tree = ET.ElementTree(file='O-A0059-001.xml')
				root = tree.getroot()
				content=root[8][1][1].text
				#print("content",content)
				#print("type(content)",type(content))             
				radar_time=root[8][0][1][2][1].text
				radar_time=radar_time[0:4]+radar_time[5:7]+radar_time[8:10]+radar_time[11:13]+radar_time[14:16]  
				delta_time=now_local_time-int(radar_time)
				delta_time=(delta_time-delta_time%60)/100+(delta_time%60)/60  
				if (now_local_time%60)<(delta_time*60%60):
					delta_time-=(40/60)          
				print("radar_time=",radar_time)
				print("delta_time=",delta_time)
				print("read xml done")
				#print("type(radar_time)",type(radar_time))
				print("rename start")
				import os
				if os.path.isfile(radar_time+"raw data.xml") ==False:
					os.rename("O-A0059-001.xml",radar_time+"raw data.xml")
					print("new radar data and rename done")

					print("rename done ")      
					print("read string from xml start")
					data = np.fromstring(content,sep=',')
					radar_data =data.reshape(881,921)
					radar_data_dbz=np.full((881,921),0)
					for i in range(881):#REVERSE 
						for j in range(921):
							if radar_data[i][j]==-999:
								radar_data[i][j]=-200
							if radar_data[i][j]==-99:
								radar_data[i][j]=-99
							radar_data_dbz[i][j]=radar_data[i][j]    
							radar_data[i][j]=10. ** (radar_data[i][j]/ 10.)           
					y_axis=np.zeros(881)
					x_axis=np.zeros(921)
					for i in range(881):
						y_axis[i]=18+0.0125*i
					for i in range(921):  
						x_axis[i]=115+0.0125*i
					#print("x",x)
					#print("y",y)
					#print("len(radar_data)",len(radar_data))
					#print("len(radar_data[0])",len(radar_data[0]))
					print("read string from xml done")


					print("parsing ground data start")
					from bs4 import BeautifulSoup
					wind_direction_final_output_check_list=["偏東風","偏西風","偏南風","偏北風","東北風","西北風","東南風","西南風"]
					result = requests.get(town_url)
					c = result.content 
					soup = BeautifulSoup(c, "html.parser")
					temperature     =soup.div.table.find_all("tr")[3].find_all("td")[1].string
					humidity        =soup.div.table.find_all("tr")[7].find_all("td")[1].string   
					wind_speed      =soup.div.table.find_all("tr")[5].find_all("td")[1].string
					wind_direction  =soup.div.table.find_all("tr")[6].find_all("td")[1].string
					cwb_forecast    =soup.div.table.find_all("tr")[8].find_all("td")[1].string
					print("original ground humidity=",humidity,"temperature=",temperature,"cwb_forecast=",cwb_forecast)
					print("original ground, wind_speed=",wind_speed,"wind_direction=",wind_direction)
					while cwb_forecast.isdigit()==False:
						cwb_forecast=cwb_forecast[0:-1]#erase last digit 
						#print("cwb_forecast",cwb_forecast,type(cwb_forecast))
					while humidity.isdigit()==False:
						humidity=humidity[0:-1]#erase last digit 
						#print("humidity",humidity,type(humidity))                
					while wind_direction not in wind_direction_final_output_check_list:
						wind_direction=soup.div.table.find_all("tr")[6].find_all("td")[1].string    
					if wind_speed=="<= 1":
						wind_speed=1
					print("cwb parsing final results",humidity,"temperature=",temperature,"cwb_forecast=",cwb_forecast)
					print("cwb parsing final results, wind_speed_level=",wind_speed,"wind_direction=",wind_direction)    
					
					print("parsing ground data end")
					high_parse_temp=high_parse()						
					def z_to_r(z, a=200., b=1.6):
						print("old z_to_r working")
						return (z / a) ** (1. / b)
					def new_z_to_r(temperature,humidity,z):
						from sklearn.externals import joblib
						from sklearn.svm import SVR
						from sklearn.preprocessing import Normalizer	
						scaler=joblib.load("scaler.pkl")
						temp=np.array([[temperature,humidity,z]])
						temp =scaler.transform(temp)
						model=joblib.load("svr_model.pkl")

						return model.predict(temp)
					radar_data_rainfall=z_to_r(radar_data)
					new_radar_data_rainfall=np.zeros((881,921))
					"""
					array_temperature=np.ones(811401)
					array_humidity=np.ones((811401)
					for i in range(0,881):
						for j in range(0,921):
							array_temperature[i+j]=temperature
							array_humidity[i+j]=humidity
					"""
					print("new z_to_r working and predicting")
					for i in range(y_position-100,y_position+100):
						#print("i=",i)
						for j in range(x_position-100,x_position+100):
							new_radar_data_rainfall[i][j]=new_z_to_r(temperature,humidity,radar_data[i][j])

					print("z to r done")

					def different_place_ground_parsing_and_forecast(x_position,y_position,wind_speed,wind_direction):
						print("my ground forecast start")
						print("ground data convert start")
						def wind_speed_transform_to_ms(original_speed):
							speed_ms=0.836 *(original_speed **(3/2))
							return speed_ms  
						def win_speed_convert_ms_to_kmh(wind_speed):
							convert_result= wind_speed*3600/1000
							return convert_result
						def wind_speed_kmh_convert_to_step(wind_speed_kmh):
							global delta_time
							step=int(wind_speed_kmh*(1+delta_time)) 
							return step
						step=wind_speed_kmh_convert_to_step(win_speed_convert_ms_to_kmh(wind_speed_transform_to_ms(int(wind_speed))))
						print("step=",step,"wind speed in kmh=",win_speed_convert_ms_to_kmh(wind_speed_transform_to_ms(int(wind_speed))))
						wind_speed=wind_speed_transform_to_ms(int(wind_speed))  
						print("ground convert end")			
						store=0
						store_new=0
						store_array=[]
						store_array_new=[]
						count=0
						count_new=0
						if wind_direction=="偏北風":
							for i in range(step+1):
								for x in range(-i,i+1):
									if (i**2+x**2)**(1/2)<=step+1:
										store+=radar_data_rainfall[y_position+i][x_position+x]
										store_array.append(radar_data_rainfall[y_position+i][x_position+x])
										count+=1
										store_new+=new_radar_data_rainfall[y_position+i][x_position+x]
										store_array_new.append(new_radar_data_rainfall[y_position+i][x_position+x])
										count_new+=1
										#radar_data_rainfall[y_position+i][x_position+x]=1000               
						if wind_direction=="東北風":
							for x in range(step+1):
								for y in range(step+1):
									if (x**2+y**2)**(1/2)<=step:
										store+=radar_data_rainfall[y_position+y][x_position+x]
										store_array.append(radar_data_rainfall[y_position+y][x_position+x])
										count+=1
										store_new+=new_radar_data_rainfall[y_position+y][x_position+x]
										store_array_new.append(new_radar_data_rainfall[y_position+y][x_position+x])
										count_new+=1
										#radar_data_rainfall[y_position+y][x_position+x]=1000
						if wind_direction=="偏東風":
							for i in range(step+1):
								for y in range(-i,i+1):
									if (i**2+y**2)**(1/2)<=step:            
										store+=radar_data_rainfall[y_position+y][x_position+i]
										store_array.append(radar_data_rainfall[y_position+y][x_position+i]) 
										count+=1  
										store_new+=new_radar_data_rainfall[y_position+y][x_position+i]
										store_array_new.append(new_radar_data_rainfall[y_position+y][x_position+i])
										count_new+=1								
										#radar_data_rainfall[y_position+y][x_position+i]=1000
						if wind_direction=="東南風":
							for x in range(step+1):
								for y in range(step+1):
									if (x**2+y**2)**(1/2)<=step:
										store+=radar_data_rainfall[y_position-y][x_position+x]
										store_array.append(radar_data_rainfall[y_position-y][x_position+x])
										count+=1
										store_new+=new_radar_data_rainfall[y_position-y][x_position+x]
										store_array_new.append(new_radar_data_rainfall[y_position-y][x_position+x])
										count_new+=1
										#radar_data_rainfall[y_position-y][x_position+x]=1000
						if wind_direction=="偏南風":
							for i in range(step+1):
								for x in range(-i,i+1):
									if (i**2+x**2)**(1/2)<=step:            
										store+=radar_data_rainfall[y_position-i][x_position+x]
										store_array.append(radar_data_rainfall[y_position-i][x_position+x])
										count+=1
										store_new+=new_radar_data_rainfall[y_position-i][x_position+x]
										store_array_new.append(new_radar_data_rainfall[y_position-i][x_position+x])
										count_new+=1								
										#radar_data_rainfall[y_position-i][x_position+x]=2000
						if wind_direction=="西南風": 
							for x in range(step+1):
								for y in range(step+1):
									if (x**2+y**2)**(1/2)<=step:
										store+=radar_data_rainfall[y_position-y][x_position-x]
										store_array.append(radar_data_rainfall[y_position-y][x_position-x])
										count+=1
										store_new+=new_radar_data_rainfall[y_position-y][x_position-x]
										store_array_new.append(new_radar_data_rainfall[y_position-y][x_position-x])
										count_new+=1								
										#radar_data_rainfall[y_position-y][x_position-x]=1000
						if wind_direction=="偏西風":
							for i in range(step+1):
								for y in range(-i,i+1):
									if (i**2+y**2)**(1/2)<=step:            
										store+=radar_data[y_position+y][x_position-i]
										store_array.append(radar_data_rainfall[y_position+y][x_position-i])
										count+=1
										store_new+=new_radar_data_rainfall[y_position+y][x_position-i]
										store_array_new.append(new_radar_data_rainfall[y_position+y][x_position-i])
										count_new+=1								
										#radar_data_rainfall[y_position+y][x_position-i]=3000
						if wind_direction=="西北風": 
							for x in range(step+1):
								for y in range(step+1):
									if (x**2+y**2)**(1/2)<=step:
										store+=radar_data_rainfall[y_position+y][x_position-x]
										store_array.append(radar_data_rainfall[y_position+y][x_position-x])
										count+=1   
										store_new+=new_radar_data_rainfall[y_position+y][x_position-x]
										store_array_new.append(new_radar_data_rainfall[y_position+y][x_position-x])
										count_new+=1								
										#radar_data_rainfall[y_position+y][x_position-x]=1000
						#store/count
						print("my ground forecast done")
						print("ground csv start")
						import csv
						with open("real time ground model results start from"+radar_time[0:6]+'forecast_x='+str(x_position)+"_y="+str(y_position)+'.csv', 'a', newline='') as csvfile:    
							writer = csv.writer(csvfile, delimiter=',')
							writer.writerow([radar_time,x_position,y_position,store/count,store_new/count_new,wind_speed,wind_direction,cwb_forecast,humidity,temperature,store_array,store_array_new,store,store_new,count,count_new,step])
							print("ground csv done")                
			
						return store/count,store_new/count_new,wind_speed,wind_direction#*cwb forecast    
					def different_place_high_parsing_and_forecast(at_850,temperature,humidity,cwb_forecast):
						global high_parse_temp
						print("at_850=",at_850)
						wind_direction  =float(high_parse_temp[0][at_850])
						wind_speed      =float(high_parse_temp[1][at_850])
						print("original ground humidity=",humidity,"temperature=",temperature,"cwb_forecast=",cwb_forecast)
						print("original ground, wind_speed=",wind_speed,"wind_direction=",wind_direction)
						print("high convert start ")
						def win_speed_convert_ms_to_kmh(wind_speed):
							convert_result= wind_speed*3600/1000
							return convert_result
						def wind_speed_kmh_convert_to_step(wind_speed_kmh):
							global delta_time
							step=int(wind_speed_kmh*(1+delta_time)) 
							return step
						step=wind_speed_kmh_convert_to_step(win_speed_convert_ms_to_kmh(wind_speed))
						print("step=",step,"wind speed in kmh=",win_speed_convert_ms_to_kmh(wind_speed))
						print("high convert end ")
						print("my high forecast start")
						store=0
						store_new=0
						store_array=[]
						store_array_new=[]
						count=0
						count_new=0
						if wind_direction>337.5 or wind_direction<22.5:#"偏北風"
							for i in range(step+1):
								for x in range(-i,i+1):
									if (i**2+x**2)**(1/2)<=step:
										store+=radar_data_rainfall[y_position+i][x_position+x]
										store_array.append(radar_data_rainfall[y_position+i][x_position+x])
										count+=1
										store_new+=new_radar_data_rainfall[y_position+i][x_position+x]
										store_array_new.append(new_radar_data_rainfall[y_position+i][x_position+x])
										count_new+=1								
										#radar_data_rainfall[y_position+i][x_position+x]=1000               
						if wind_direction>22.5 and wind_direction<67.5:#"東北風"
							for x in range(step+1):
								for y in range(step+1):
									if (x**2+y**2)**(1/2)<=step:
										store+=radar_data_rainfall[y_position+y][x_position+x]
										store_array.append(radar_data_rainfall[y_position+y][x_position+x])
										count+=1
										store_new+=new_radar_data_rainfall[y_position+y][x_position+x]
										store_array_new.append(new_radar_data_rainfall[y_position+y][x_position+x])
										count_new+=1
										#radar_data_rainfall[y_position+y][x_position+x]=1000
						if wind_direction>67.5 and wind_direction<112.5:#"東風"
							for i in range(step+1):
								for y in range(-i,i+1):
									if (i**2+y**2)**(1/2)<=step:            
										store+=radar_data_rainfall[y_position+y][x_position+i]
										store_array.append(radar_data_rainfall[y_position+y][x_position+i]) 
										count+=1   
										store_new+=new_radar_data_rainfall[y_position+y][x_position+i]
										store_array_new.append(new_radar_data_rainfall[y_position+y][x_position+i])
										count_new+=1								
										#radar_data_rainfall[y_position+y][x_position+i]=1000
						if wind_direction>112.5 and wind_direction<157.5:#"東南風"
							for x in range(step+1):
								for y in range(step+1):
									if (x**2+y**2)**(1/2)<=step:
										store+=radar_data_rainfall[y_position-y][x_position+x]
										store_array.append(radar_data_rainfall[y_position-y][x_position+x])
										count+=1
										store_new+=new_radar_data_rainfall[y_position-y][x_position+x]
										store_array_new.append(new_radar_data_rainfall[y_position-y][x_position+x])
										count_new+=1								
										#radar_data_rainfall[y_position-y][x_position+x]=1000
						if wind_direction>157.5 and wind_direction<202.5:#"南風"
							for i in range(step+1):
								for x in range(-i,i+1):
									if (i**2+x**2)**(1/2)<=step:            
										store+=radar_data_rainfall[y_position-i][x_position+x]
										store_array.append(radar_data_rainfall[y_position-i][x_position+x])
										count+=1
										store_new+=new_radar_data_rainfall[y_position-i][x_position+x]
										store_array_new.append(new_radar_data_rainfall[y_position-i][x_position+x])
										count_new+=1								
										#radar_data_rainfall[y_position-i][x_position+x]=2000
						if wind_direction>202.5 and wind_direction<247.5:#"西南風" 
							for x in range(step+1):
								for y in range(step+1):
									if (x**2+y**2)**(1/2)<=step:
										store+=radar_data_rainfall[y_position-y][x_position-x]
										store_array.append(radar_data_rainfall[y_position-y][x_position-x])
										count+=1
										store_new+=new_radar_data_rainfall[y_position-y][x_position-x]
										store_array_new.append(new_radar_data_rainfall[y_position-y][x_position-x])
										count_new+=1								
										#radar_data_rainfall[y_position-y][x_position-x]=1000
						if wind_direction>247.5 and wind_direction<292.5:#"西風"
							for i in range(step+1):
								for y in range(-i,i+1):
									if (i**2+y**2)**(1/2)<=step:            
										store+=radar_data_rainfall[y_position+y][x_position-i]
										store_array.append(radar_data_rainfall[y_position+y][x_position-i])
										count+=1
										store_new+=new_radar_data_rainfall[y_position+y][x_position-i]
										store_array_new.append(new_radar_data_rainfall[y_position+y][x_position-i])
										count_new+=1							
										#radar_data_rainfall[y_position+y][x_position-i]=3000
						if wind_direction>292.5 and wind_direction<337.5:#"西北風" 
							for x in range(step+1):
								for y in range(step+1):
									if (x**2+y**2)**(1/2)<=step:
										store+=radar_data_rainfall[y_position+y][x_position-x]
										store_array.append(radar_data_rainfall[y_position+y][x_position-x])
										count+=1  
										store_new+=new_radar_data_rainfall[y_position+y][x_position-x]
										store_array_new.append(new_radar_data_rainfall[y_position+y][x_position-x])
										count_new+=1								
										#radar_data_rainfall[y_position+y][x_position-x]=1000
						print("my high forecast done")                
						import csv
						print("high csv start")
						with open("real time high model results start from"+radar_time[0:6]+'forecast_x='+str(x_position)+"_y="+str(y_position)+"at_850="+str(at_850)+'.csv', 'a', newline='') as csvfile:    
							writer = csv.writer(csvfile, delimiter=',')
							writer.writerow([radar_time,x_position,y_position,store/count,store_new/count_new,wind_speed,wind_direction,cwb_forecast,humidity,temperature,store_array,store,store_new,count,count_new,step])
							print("high csv done")                
						return store/count,store_new/count_new,wind_direction,wind_speed#*cwb forecast  
					my_ground_predict_with_old_zr,my_ground_predict_with_new_zr,wind_speed,wind_direction=different_place_ground_parsing_and_forecast(x_position=x_position,y_position=y_position,wind_speed=wind_speed,wind_direction=wind_direction)
		     
					print("all real time ground model done") 
					my_500_predict_with_old_zr,my_500_predict_with_new_zr,wind_direction_500,wind_speed_500=different_place_high_parsing_and_forecast(0,temperature,humidity,cwb_forecast)
					my_850_predict_with_old_zr,my_850_predict_with_new_zr,wind_direction_850,wind_speed_850=different_place_high_parsing_and_forecast(1,temperature,humidity,cwb_forecast)
					my_final_predict_with_old_zr=(my_500_predict_with_old_zr+my_850_predict_with_old_zr)/2
					my_final_predict_with_new_zr=(my_500_predict_with_new_zr+my_850_predict_with_new_zr)/2
					print("all real time  high model done")
					print("")
					print("")
					print("my_ground_predict_with_old_zr=",my_ground_predict_with_old_zr) 
					print("my_500_predict_with_old_zr=",my_500_predict_with_old_zr) 
					print("my_850_predict_with_old_zr=",my_850_predict_with_old_zr)			
					print("my_ground_predict_with_new_zr=",my_ground_predict_with_new_zr) 
					print("my_500_predict_with_new_zr=",my_500_predict_with_new_zr) 
					print("my_850_predict_with_new_zr=",my_850_predict_with_new_zr)	
					print("my_final_predict_with_old_zr=",my_final_predict_with_old_zr)
					print("my_final_predict_with_new_zr=",my_final_predict_with_new_zr)	
					print("")
					print("")		
					print("plot heatmap start")			   
					import plotly
					import plotly.offline as py
					#import plotly.plotly as py
					import plotly.graph_objs as go
					from mpl_toolkits.basemap import Basemap

					#longtitude distance =111.32*cos(latitude)=101.7 @24 taiwian per degree x
					#latitude distance =110.574 per degree y
					#image_width = 101.7*921=93666
					#image_height =110.574 * 881=97416  
					
					#print("radar_data_dbz",radar_data_dbz)
					#print("radar_data",radar_data)
					#print("radar_data_rainfall",radar_data_rainfall)
					fig_1 = [go.Heatmap( z=radar_data_dbz, x=x_axis,y=y_axis,colorscale='Viridis')]
					#py.plot(fig0,image="jpeg",image_height=974,image_width=937,filename="radar_data",image_filename=str(radar_time)+"radar_data_dbz_x"+str(x_position)+"_y="+str(y_position),auto_open=True)
					print("spot start")
					for i in range(-5,6):
						for j in range(-5,6):
							radar_data_dbz[y_position+i][x_position+j]=200
							#nofunction=1
					print("spot done")			
					fig_2 = [go.Heatmap( z=radar_data_dbz, x=x_axis,y=y_axis,colorscale='Viridis')]
					#py.plot(fig1,image="jpeg",image_height=974,image_width=937,filename=str(radar_time)+"radar_data",image_filename=str(radar_time)+"radar_data")
					fig = [go.Heatmap( z=radar_data_rainfall, x=x_axis,y=y_axis,colorscale='Viridis')]
					#py.plot(fig,image="jpeg",image_height=974,image_width=937,filename="radar_data_rainfall",image_filename=str(radar_time)+"radar_data_rainfall_x"+str(x_position)+"_y="+str(y_position),auto_open=True)
					new_fig=[go.Heatmap( z=new_radar_data_rainfall, x=x_axis,y=y_axis,colorscale='Viridis')]


					print("coastline test start")
					import numpy as np
					from mpl_toolkits.basemap import Basemap
					import plotly
					import plotly.offline as py
					from plotly.graph_objs import *


					m = Basemap(projection='merc' , 
					              resolution='i' , fix_aspect=True,
					              llcrnrlon=115.0 , llcrnrlat=18.0,
					              urcrnrlon=126.5125 , urcrnrlat=29.0125)
					              #,lat_ts =20)

					# Make trace-generating function (return a Scatter object)
					def make_scatter(x,y):
					    return Scatter(
					        x=x,
					        y=y,
					        mode='lines',
					        line=Line(color="black"),
					        name=' '  # no name on hover
					    )

					# Functions converting coastline/country polygons to lon/lat traces
					def polygons_to_traces(poly_paths, N_poly):
					    ''' 
					    pos arg 1. (poly_paths): paths to polygons
					    pos arg 2. (N_poly): number of polygon to convert
					    '''
					    traces = []  # init. plotting list 

					    for i_poly in range(N_poly):
					        poly_path = poly_paths[i_poly]
					        
					        # get the Basemap coordinates of each segment
					        coords_cc = np.array(
					            [(vertex[0],vertex[1]) 
					             for (vertex,code) in poly_path.iter_segments(simplify=False)]
					        )
					        
					        # convert coordinates to lon/lat by 'inverting' the Basemap projection
					        lon_cc, lat_cc = m(coords_cc[:,0],coords_cc[:,1], inverse=True)
					        
					        # add plot.ly plotting options
					        traces.append(make_scatter(lon_cc,lat_cc))
					     
					    return traces

					# Function generating coastline lon/lat traces
					def get_coastline_traces():
					    poly_paths = m.drawcoastlines().get_paths() # coastline polygon paths
					    N_poly = len(poly_paths)  # use only the 91st biggest coastlines (i.e. no rivers)
					    return polygons_to_traces(poly_paths, N_poly)

					# Function generating country lon/lat traces
					def get_country_traces():
					    poly_paths = m.drawcountries().get_paths() # country polygon paths
					    N_poly = len(poly_paths)  # use all countries
					    return polygons_to_traces(poly_paths, N_poly)

					# Get list of of coastline and country lon/lat traces
					traces_cc = get_coastline_traces()+get_country_traces() 
					print("coastline test end")


					fig_one = go.Figure(data=fig_1+traces_cc)
					fig_two = go.Figure(data=fig_2+traces_cc)
					fig_three = go.Figure(data=fig+traces_cc)
					fig_four = go.Figure(data=new_fig+traces_cc)

					import plotly.io as pio
					fig_one_post = pio.to_image(fig_one, format='png', width=937, height=974, scale=2)
					fig_two_post = pio.to_image(fig_two, format='png', width=937, height=974, scale=2)
					fig_three_post = pio.to_image(fig_three, format='png', width=937, height=974, scale=2)
					fig_four_post = pio.to_image(fig_four, format='png', width=937, height=974, scale=2)
					print("plot heatmap done")
					print("post start")
					"""
					variable you need:
					
					temperature
					humidity
					cwb_forecast #降雨機率

					wind_direction
					wind_speed
					my_ground_predict_with_old_zr 
					my_ground_predict_with_new_zr

					wind_direction_500
					wind_speed_500
					my_500_predict_with_old_zr
					my_500_predict_with_new_zr


					wind_direction_850
					wind_speed_850
					my_850_predict_with_old_zr
					my_850_predict_with_new_zr

					fig0
					fig1
					fig

					variable you need end 			
					post code here
					"""
					import pymongo
					import json
					from collections import namedtuple
					from bson import ObjectId

					my_ground_predict_with_new_zr = 0
					# ----------------connect mongodb------------------
					myclient = pymongo.MongoClient("mongodb")

					# ----------------create/connect database------------------
					mydb = myclient["mydatabase"]

					# ----------------create/connect collections------------------
					mycol = mydb["customers"]

					# ----------------check if database exist------------------
					dblist = myclient.list_database_names()
					if "mydatabase" in dblist:
						print("connect to database.")

					# ----------------check if collecgtion exist------------------
					collist = mydb.list_collection_names()
					if "customers" in collist:
						print("connect to collection.")

					# ----------------insert------------------
					mydict = { 
					"_id": time.strftime("%Y%m%d%H%M"), "temperature": temperature, "humidity": humidity, "cwb_forecast": cwb_forecast,
					"wind_direction": wind_direction,"wind_speed": wind_speed,
					"my_ground_predict_with_old_zr": my_ground_predict_with_old_zr,
					"my_ground_predict_with_new_zr": my_ground_predict_with_new_zr, 
					"wind_direction_500": wind_direction_500, "wind_speed_500": wind_speed_500,
					"my_500_predict_with_old_zr": my_500_predict_with_old_zr, "my_500_predict_with_new_zr": my_500_predict_with_new_zr, 
					"wind_direction_850": wind_direction_850, "wind_speed_850": wind_speed_850,
					"my_850_predict_with_old_zr": my_850_predict_with_old_zr,"my_850_predict_with_new_zr": my_850_predict_with_new_zr,
					"my_final_predict_with_new_zr":my_final_predict_with_new_zr,"my_final_predict_with_old_zr":my_final_predict_with_old_zr ,
					"fig_one_post": fig_one_post, "fig_two_post": fig_two_post, "fig_three_post": fig_three_post,"fig_four_post": fig_four_post}
					x = mycol.insert_one(mydict)
					data_on_web_count=0					
					for last_one in mycol.find():
						data_on_web_count+=1
					print("final data_on_web_count=",data_on_web_count)	
					if data_on_web_count>5:
						for last_one in mycol.find().limit(data_on_web_count-5):
							mycol.delete_one(last_one)
							print("delete")				

					
					print("post  done") 
				
					print("ALL done")		
					trivial=time.sleep(10)#20 
					os.system("echo off")
					trivial=time.sleep(10)
					os.system("taskkill /im firefox.exe /f")
					trivial=time.sleep(10)#95					
				else: 
					print("new xml is old radar data") 
					print("ALL done")
					trivial=time.sleep(60) 
			except ET.ParseError:
				print("xml is empty")
				continue          

	except KeyboardInterrupt:
	    print (total_error)  
	    sys.exit(1)  
	except Exception as error:
	    if error not in total_error:
	        total_error.append(error)
	    print ('Restarting!')
	    continue