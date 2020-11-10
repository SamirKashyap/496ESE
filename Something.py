from matplotlib import pyplot as plt

def main():
    with open("output.txt") as myfile:
        lines = myfile.readlines()
        for i in range(0, 95):
            UUID = lines[i * 15][13:49]
            Total = int(lines[i * 15][70:-2])
            VersionControl = int(lines[i * 15 + 1][22:-2])
            Edit = int(lines[i * 15 + 2].split(":  ")[1][:-2])
            Command = int(lines[i * 15 + 3].split(":  ")[1][:-2])
            Document = int(lines[i * 15 + 4].split(":  ")[1][:-2])
            Activity = int(lines[i * 15 + 5].split(":  ")[1][:-2])
            Navigation = int(lines[i * 15 + 6].split(":  ")[1][:-2])
            TestRun = int(lines[i * 15 + 7].split(":  ")[1][:-2])
            Window = int(lines[i * 15 + 8].split(":  ")[1][:-2])
            Completion = int(lines[i * 15 + 9].split(":  ")[1][:-2])
            System = int(lines[i * 15 + 10].split(":  ")[1][:-2])
            Debugger = int(lines[i * 15 + 11].split(":  ")[1][:-2])
            Solution = int(lines[i * 15 + 12].split(":  ")[1][:-2])
            IDEState = int(lines[i * 15 + 13].split(":  ")[1][:-2])
            Undefined = int(lines[i * 15 + 14].split(":  ")[1][:-1])
            print("UUID:",UUID)
            print("Total:",Total)
            print("VersionControl:",VersionControl, "Percentage:", VersionControl/Total)
            print("Edit:",Edit, "Percentage:", Edit/Total)
            print("Command:",Command, "Percentage:", Command/Total)
            print("Document:",Document, "Percentage:", Document/Total)
            print("Activity:",Activity, "Percentage:", Activity/Total)
            print("Navigation:",Navigation, "Percentage:", Navigation/Total)
            print("TestRun:",TestRun, "Percentage:", TestRun/Total)
            print("Window:",Window, "Percentage:", Window/Total)
            print("Completion:",Completion, "Percentage:", Completion/Total)
            print("System:",System, "Percentage:", System/Total)
            print("Debugger:",Debugger, "Percentage:", Debugger/Total)
            print("Solution:",Solution, "Percentage:", Solution/Total)
            print("IDEState:",IDEState, "Percentage:", IDEState/Total)
            print("Undefined:",Undefined, "Percentage:", Undefined/Total)

    myfile.close()

if __name__ == "__main__":
    main()