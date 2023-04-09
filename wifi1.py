import wifi
import netifaces

# Obtener la interfaz de red inalámbrica
interfaces = netifaces.interfaces()
wifi_interface = [i for i in interfaces if i.startswith("w")][0]

# Escanear las conexiones Wifi disponibles
wifi_scanner = wifi.WiFiScanner()
wifi_scanner.scan()

# Obtener la lista de conexiones Wifi detectadas
wifi_list = wifi_scanner.get_access_points()

# Imprimir los nombres y direcciones MAC de las conexiones Wifi
for wifi in wifi_list:
    print("Nombre:", wifi.ssid)
    print("Dirección MAC:", wifi.bssid)
    print("-------------------------")
