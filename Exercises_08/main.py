""
Script: main.py
By: TL

Tested: 2909202222
"""
from devices import Firewall
# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall()
# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")

from devices import Switch
# Create a switch instance
sw1 = Switch("switch01")
# Configure it
sw1.configure_Switch()
# Create a firewall instance
sw2 = Firewall("switch02")
# Verify a CRC
sw2.calculate_crc("dummy data")

from devices import NLB
# Create a network load balancer instance
nlb1 = NLB("NLB01")
# Configure it
nlb1.configure_NLB()
# Create a firewall instance
nlb2 = NLB("NLB02")
# Verify a CRC
nlb2.calculate_crc("dummy data")