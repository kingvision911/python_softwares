import  optparse, subprocess

parser = optparse.OptionParser()
parser.add_option('-i', '--interface', dest='interface', help='specify the interface of your system')
parser.add_option('-m', '--mac', dest='mac')
(options, arguments) = parser.parse_args()

interface = options.interface
mac = options.mac

subprocess.call(['sudo', 'ifconfig', interface, 'down'])
subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', mac])
subprocess.call(['sudo', 'ifconfig', interface, 'up'])

