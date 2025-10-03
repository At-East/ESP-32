import network #导入Wifi模块

wlan = network.WLAN(network.STA_IF) #给Wifi这个接口下定义，在设备中导入wifi
wlan.active(True) #设置Wifi状态为“活动”（相当于打开WiFi）
wlan.scan() #扫描WiFi
wlan.isconnected() #在这一步是检查WiFi连通性，如果链接成功将会在下方显示“True”，不过这时候大概率是“False”
wlan.connect('ssid', 'key') #在这一步连接WiFi，请将引号中的ssid替换为你家的Wifi（要求是上方搜索到的），key替换为密码
wlan.isconnected() #再次查询WiFi状态，这时候应该是“True”
wlan.config('mac') #查询Mac地址
wlan.ifconfig() #查询设备IP地址
