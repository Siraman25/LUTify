# Available Parameters:
# -h, --help --> Shows help
# -t integer, --tab=integer --> Set tab amount, standard: 1
# -p "string", --pref="string" --> Set prefix string, standard: "dc.b"
# -P "string", --posf="string" --> Set postfix string, standard: "T"
# -r integer, --rows=integer --> Amount of rows, standard: 128
# -b integer, --begin=integer --> First value of range, standard: 0
# -e integer, --end=integer --> Last value of range, standard: 100
# -a, --additional --> Additional row at the end with same value of last row, standard: null
# -o "string", --output="string" --> Output file, standard: null

import getopt, sys

argList = sys.argv[1:]
options = "ht:p:P:r:b:e:ao:"
longOptions = ["help", "tab=", "pref=", "posf=", "rows=", "begin=", "end=", "additional", "output="]

tabAmount = 1
prefix = "dc.b"
postfix = "T"
rowAmount = 128
endValue = 100
startValue = 0
additionalValue = False
outputFilePath = ""

valueList = []

try:
    args, vals = getopt.getopt(argList, options, longOptions)

    for currentArg, currentVal in args:
        if currentArg in ("-h", "--help"):
            print("HERE GOES HELP")  # TODO: Add help page
        elif currentArg in ("-t", "--tab"):
            tabAmount = int(currentVal)
        elif currentArg in ("-p", "--pref"):
            prefix = currentVal
        elif currentArg in ("-P", "--posf"):
            postfix = currentVal
        elif currentArg in ("-r", "--rows"):
            if int(currentVal) < 1:
                sys.exit("Row amount must be greater than zero.")
            rowAmount = int(currentVal)
        elif currentArg in ("-b", "--begin"):
            startValue = int(currentVal)
        elif currentArg in ("-e", "--end"):
            endValue = int(currentVal)
        elif currentArg in ("-a", "--additional"):
            additionalValue = True
        elif currentArg in ("-o", "--output"):
            outputFilePath = currentVal

except getopt.error as GetoptExitError:
    print(str(GetoptExitError))
    sys.exit("Please review your input and run the program again.")

if outputFilePath == "":
    sys.exit("Filepath is required. Use option --output=\"\" or -o \"\" to specify a file. If the file does not exist, "
             "a new file will be created. Existing file contents will be irreversibly overwritten.")

try:
    # --- BEGIN LIST CREATION ---
    stepAmount = (endValue - startValue) / rowAmount
    valueList.append(startValue)  # Starting value is added manually to provide first value to for-loop
    for row in range(rowAmount - 2):
        valueList.append(valueList[-1] + stepAmount)
    valueList.append(endValue)  # Ending value is added manually to make sure that range is complete
    if additionalValue:
        valueList.append(endValue)
    valueList = list(map(round, valueList))
    # print(valueList)                  # Debug print

    # --- BEGIN FILE WRITING ---

    fileWriter = open(outputFilePath, "w")
    for row in range(len(valueList)):
        stringToWrite = tabAmount * "\t" + prefix + "\t" + str(valueList[row]) + postfix + "\n"
        fileWriter.write(stringToWrite)
    fileWriter.close()

    print("Thanks for using this tool.")
    print("A file has been produced with following settings:")


except Exception as ExitError:
    print(str(ExitError))
    sys.exit("Please review your input and run the program again.")
