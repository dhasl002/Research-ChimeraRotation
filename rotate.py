from chimera import runCommand

x = 0
axisChoice =  0
rand = -30
xAxis = "x"
yAxis = "y"
zAxis = "z"
runCommand("open L:/Devin/NewTrainingData/3j7i_a/3j7i_a.pdb")
while x < 36:
	
	rand = rand+30
	if rand == 360:
		rand = 0
	
	if x%12 == 11:
		axisChoice = axisChoice + 1
	
	if axisChoice == 0:
		stringToPass = "turn " + xAxis + " " + str(rand)
		runCommand(stringToPass)
	if axisChoice == 1:
		stringToPass = "turn " + yAxis + " " + str(rand)
		runCommand(stringToPass)
	if axisChoice == 2:
		stringToPass = "turn " + zAxis + " " + str(rand)
		runCommand(stringToPass)

	runCommand("write format pdb #0 L:/Devin/NewTrainingData/3j7i_a/3j7i_a_" + str(x) + ".pdb")
	runCommand("close #0")
	runCommand("open L:/Devin/NewTrainingData/3j7i_a/3j7i_a_" + str(x) + ".pdb")
	runCommand("molmap #0 8 modelId 1 gridSpacing 1")
	runCommand("volume #1 save L:/Devin/NewTrainingData/3j7i_a/3j7i_a_" + str(x) + ".mrc")
	runCommand("close #1")
	x +=1
runCommand("close session")
