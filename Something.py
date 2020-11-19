from matplotlib import pyplot as plt

def savetofile(events, data, UUID):
    fig = plt.figure(figsize=(16,8))
    ax = fig.add_subplot(111)
    ax.bar(events, data)
    name = str(UUID) + "_averages.png"
    plt.show()
    # plt.savefig(name)


def showmaxes(events, data):
    fig = plt.figure(figsize=(16,8))
    ax = fig.add_subplot(111)
    ax.bar(events, data)
    name = "Max Events"
    plt.show()
    # plt.savefig(name)

def main():
    TotalVersionControlPercent = 0
    TotalEditPercent = 0
    TotalCommandPercent = 0
    TotalDocumentPercent = 0
    TotalActivityPercent = 0
    TotalNavigationPercent = 0
    TotalTestRunPercent = 0
    TotalWindowPercent = 0
    TotalCompletionPercent = 0
    TotalSystemPercent = 0
    TotalDebuggerPercent = 0
    TotalSolutionPercent = 0
    TotalIDEStatePercent = 0
    TotalUndefinedPercent = 0
    EventList = ['VersionControl', 'Edit', 'Command', 'Document', 'Activity', 'Navigation', 'TestRun', 'Window', 'Completion', 'System', 'Debugger', 'Solution', 'IDEState', ' Undefined']
    with open("output.txt") as myfile:
        lines = myfile.readlines()
        maxes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(0, 95):  #95 developer sessions
            Event = []
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

            Event.append(VersionControl)
            Event.append(Edit)
            Event.append(Command)
            Event.append(Document)
            Event.append(Activity)
            Event.append(Navigation)
            Event.append(TestRun)
            Event.append(Window)
            Event.append(Completion)
            Event.append(System)
            Event.append(Debugger)
            Event.append(Solution)
            Event.append(IDEState)
            Event.append(Undefined)

            VersionControlPercent = VersionControl/Total
            EditPercent = Edit/Total
            CommandPercent = Command/Total
            DocumentPercent = Document/Total
            ActivityPercent = Activity/Total
            NavigationPercent = Navigation/Total
            TestRunPercent = TestRun/Total
            WindowPercent = Window/Total
            CompletionPercent = Completion/Total
            SystemPercent = System/Total
            DebuggerPercent = Debugger/Total
            SolutionPercent = Solution/Total
            IDEStatePercent = IDEState/Total
            UndefinedPercent = Undefined/Total

            TotalVersionControlPercent += VersionControlPercent
            TotalEditPercent += EditPercent
            TotalCommandPercent += CommandPercent
            TotalDocumentPercent += DocumentPercent
            TotalActivityPercent += ActivityPercent
            TotalNavigationPercent += NavigationPercent
            TotalTestRunPercent += TestRunPercent
            TotalWindowPercent += WindowPercent
            TotalCompletionPercent += CompletionPercent
            TotalSystemPercent += SystemPercent
            TotalDebuggerPercent += DebuggerPercent
            TotalSolutionPercent += SolutionPercent
            TotalIDEStatePercent += IDEStatePercent
            TotalUndefinedPercent += UndefinedPercent


            maximum = []
            maximum.append(max(Event))
            print(maximum)
            res = [Event.index(i) for i in maximum] 
            print(EventList[res[0]])
            maxes[res[0]] += 1


            

            print("UUID:",UUID)
            print("Total:",Total)
            print("VersionControl:",VersionControl, "Percentage:", VersionControlPercent)
            print("Edit:",Edit, "Percentage:", EditPercent)
            print("Command:",Command, "Percentage:", CommandPercent)
            print("Document:",Document, "Percentage:", DocumentPercent)
            print("Activity:",Activity, "Percentage:", ActivityPercent)
            print("Navigation:",Navigation, "Percentage:", NavigationPercent)
            print("TestRun:",TestRun, "Percentage:", TestRunPercent)
            print("Window:",Window, "Percentage:", WindowPercent)
            print("Completion:",Completion, "Percentage:", CompletionPercent)
            print("System:",System, "Percentage:", SystemPercent)
            print("Debugger:",Debugger, "Percentage:", DebuggerPercent)
            print("Solution:",Solution, "Percentage:", SolutionPercent)
            print("IDEState:",IDEState, "Percentage:", IDEStatePercent)
            print("Undefined:",Undefined, "Percentage:", UndefinedPercent)
            # data = [VersionControlPercent, EditPercent, CommandPercent, DocumentPercent, ActivityPercent,
            #         NavigationPercent, TestRunPercent, WindowPercent, CompletionPercent, SystemPercent, DebuggerPercent,
            #         SolutionPercent, IDEStatePercent, UndefinedPercent]

            # savetofile(EventList, data, UUID)
        totaldata = [TotalVersionControlPercent/95, TotalEditPercent/95, TotalCommandPercent/95, TotalDocumentPercent/95, TotalActivityPercent/95,
                    TotalNavigationPercent/95, TotalTestRunPercent/95, TotalWindowPercent/95, TotalCompletionPercent/95, TotalSystemPercent/95, TotalDebuggerPercent/95,
                    TotalSolutionPercent/95, TotalIDEStatePercent/95, TotalUndefinedPercent/95]
        # savetofile(EventList, totaldata, "Total")
        print(maxes)
        # showmaxes(EventList, maxes)
        print(totaldata, EventList)
    myfile.close()


if __name__ == "__main__":
    main()