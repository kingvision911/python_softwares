import argparse, subprocess, random, time, sys, re

def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', dest='interface', help='[+] you can type ifconfig to see which interface you want to change')
    options = parser.parse_args()

    if not options.interface:
        parser.error("[-] error spesify your interface.")
    return options

def change_mac(interface, mac):
    subprocess.call(['sudo', 'ifconfig', interface, 'down'])
    subprocess.call(['sudo', 'ifconfig', interface,'hw', 'ether', mac])
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])

def get_random_mac():
    characters = '0123456789abcde'
    random_mac = '00'
    for i in range(5):
        random_mac += ':' + random.choice(characters) \
		+ random.choice(characters)
    return random_mac

def get_current_mac(interface):
    output = subprocess.check_output(['ifconfig', interface])
    return re.search('\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(output)).group(0)

time_to_change = int(input("[+] Time Interval For The Mac Change: "))
print('[+] You Mac Address Will Be Changed After Every ' + str(time_to_change) + ' seconds')
print('[+] Press CTRL+C To Quit The Program')
options = get_argument()
current_mac = get_current_mac(options.interface)

try:
    while True:
        random_mac = get_random_mac()
        change_mac(options.interface, random_mac)
        new_summary = subprocess.check_output(['ifconfig', options.interface])
        if random_mac in str(new_summary):
            print('\r[+] MAC ADDRESS Changed To: |' + str(random_mac) + '|', end="")
            sys.stdout.flush()
        time.sleep(time_to_change)

except KeyboardInterrupt:
    change_mac(options.interface, current_mac)
    print('\n[-] Quiting...')

