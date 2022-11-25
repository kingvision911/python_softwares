import argparse, subprocess, random, time, sys, re

def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', dest='interface', help='[+] you can type ifconfig to see which interface you want to change')
    options = parser.parse_args()

    if not options.interface:
        parser.error("[-] error spesify your interface.")
    return options

def change_ip(interface, ip):
    subprocess.call(['sudo', 'ifconfig', interface, 'down'])
    subprocess.call(['sudo', 'ifconfig', interface, 'inet', ip])
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])

def get_random_ip():
    global default
    characters = '123456789'
    random_ip = str(default)
    for i in range(1):
        random_ip += '.' + random.choice(characters) \
		+ random.choice(characters)
    return random_ip

time_to_change = int(input("[+] Time Interval For The IP To Change: "))
default = input('[+] Enter Router Ip Except The Last Digits Example(192.168.8): ')
print('[+] Your Ip Address Will Be Changed After Every ' + str(time_to_change) + ' seconds')
print('[+] Press CTRL+C To Quit The Program')
options = get_argument()

try:
    while True:
        random_ip = get_random_ip()
        change_ip(options.interface, random_ip)
        new_summary = subprocess.check_output(['ifconfig', options.interface])
        if random_ip in str(new_summary):
            print('\r[+] MAC ADDRESS Changed To: |' + str(random_ip) + '|', end="")
            sys.stdout.flush()
        time.sleep(time_to_change)

except KeyboardInterrupt:
    print('\n[-] Quiting...')

