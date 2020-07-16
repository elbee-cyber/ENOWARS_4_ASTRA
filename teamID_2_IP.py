#!/bin/python3
import sys

if(sys.argv[1].isupper() or sys.argv[1].islower() or "." in sys.argv[1]):
	print('\n'+"Please enter a team ID! You can find them at https://enowars.com/teams.html")
	print("Usuage: python3 teamID_2_IP.py <ID>"+'\n')
else:
	teamID = int(sys.argv[1]) 
	par1 = teamID // 256
	par2 = teamID % 256
	print('\n'+"TEAM "+str(teamID)+" is hosted at: ")
	print("10."+str(par1)+"."+str(par2)+".1")
	print('\n')

