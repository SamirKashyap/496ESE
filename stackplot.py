from matplotlib import pyplot as plt


def makegraph(Events, currentUUID, Total, VersionControl, Edit, Command, Document, Activity, Navigation, TestRun, Window, Completion, System, Debugger, Solution, IDEState, Undefined):
    fig = plt.figure(figsize=(16,8))
    ax = fig.add_subplot(111)
    ax.stackplot(range(0,int(Total)), VersionControl, Edit, Command, Document, Activity, Navigation, TestRun, Window, Completion, System, Debugger, Solution, IDEState, Undefined, labels = Events, colors = ['red', 'orange', 'gold', 'greenyellow', 'forestgreen', 'turquoise', 'teal', 'cyan', 'lightblue', 'dodgerblue', 'slateblue', 'mediumpurple', 'plum', 'deeppink'])
    ax.legend(loc="upper left")
    ax.set_title(currentUUID + " event stream")
    ax.set_xlabel('Elapsed events')
    ax.set_ylabel('Number of events')
    name = (currentUUID + ' event stream')
    plt.savefig(name)

def main():
    EventList = ['VersionControl', 'Edit', 'Command', 'Document', 'Activity', 'Navigation', 'TestRun', 'Window', 'Completion', 'System', 'Debugger', 'Solution', 'IDEState', ' Undefined']
    with open("stackplot.txt") as myfile:
        lines = myfile.readlines()
        currentUUID = ""
        Total = 0
        VersionControl = []
        Edit = []
        Command = []
        Document = []
        Activity = []
        Navigation = []
        TestRun = []
        Window = []
        Completion = []
        System = []
        Debugger = []
        Solution = []
        IDEState = []
        Undefined = []
        for i in range(0, 594073):  #95 developer sessions   594073
            line = lines[i].split(" ")
            UUID = line[0]
            if UUID != currentUUID:
                print("Print graph")
                makegraph(EventList, currentUUID, Total, VersionControl, Edit, Command, Document, Activity, Navigation, TestRun, Window, Completion, System, Debugger, Solution, IDEState, Undefined)
                VersionControl.clear()
                Edit.clear()
                Command.clear()
                Document.clear()
                Activity.clear()
                Navigation.clear()
                TestRun.clear()
                Window.clear()
                Completion.clear()
                System.clear()
                Debugger.clear()
                Solution.clear()
                IDEState.clear()
                Undefined.clear()
                currentUUID = UUID

            Total = line[1]
            VersionControl.append(int(line[2]))
            Edit.append(int(line[3]))
            Command.append(int(line[4]))
            Document.append(int(line[5]))
            Activity.append(int(line[6]))
            Navigation.append(int(line[7]))
            TestRun.append(int(line[8]))
            Window.append(int(line[9]))
            Completion.append(int(line[10]))
            System.append(int(line[11]))
            Debugger.append(int(line[12]))
            Solution.append(int(line[13]))
            IDEState.append(int(line[14]))
            Undefined.append(int(line[15]))

       

            
            # print("UUID:",UUID)
            # print("Total:",Total)
            # print("VersionControl:",VersionControl)
            # print("Edit:",Edit)
            # print("Command:",Command)
            # print("Document:",Document)
            # print("Activity:",Activity)
            # print("Navigation:",Navigation)
            # print("TestRun:",TestRun)
            # print("Window:",Window)
            # print("Completion:",Completion)
            # print("System:",System)
            # print("Debugger:",Debugger)
            # print("Solution:",Solution)
            # print("IDEState:",IDEState)
            # print("Undefined:",Undefined)
        
       
    myfile.close()


if __name__ == "__main__":
    main()