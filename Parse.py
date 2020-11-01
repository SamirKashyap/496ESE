import json, os

class sesh:
    def __init__(self, sessionUUID, TotalEvents, VersionControlEvents, EditEvents, CommandEvents, DocumentEvents, ActivityEvents, NavigationEvents, TestRunEvents, WindowEvents, CompletionEvents, SystemEvents, DebuggerEvents, SolutionEvents, IDEStateEvents, UndefinedEvents):
        self.sessionUUID = ""
        self.TotalEvents = 0
        self.VersionControlEvents = 0
        self.EditEvents = 0
        self.CommandEvents = 0
        self.DocumentEvents = 0
        self.ActivityEvents = 0
        self.NavigationEvents = 0
        self.TestRunEvents = 0
        self.WindowEvents = 0
        self.CompletionEvents = 0
        self.SystemEvents = 0
        self.DebuggerEvents = 0
        self.SolutionEvents = 0
        self.IDEStateEvents = 0
        self.UndefinedEvents = 0
    

def main():
    base_path = 'E:/ESEData'
    based_path = 'E:/ESEData/'
    files = [pos_json for pos_json in os.listdir(base_path) if pos_json.endswith('.json')]
    print(len(files), " files loaded.")
    eventType = ""
    sessions = {}
    existingUUID = []
    session = sesh("", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    for i in range(0, len(files)): 
        data = open(based_path + files[i])
        data2 = json.load(data)
        eventType = data2['$type'].split(',')[0].split('.')[-1]
        fileSessionUUID = data2['IDESessionUUID']
        if (fileSessionUUID != session.sessionUUID and fileSessionUUID not in existingUUID):  # if file's UUID is not the previous one, and has not been seen before, create new session
            sessions[session.sessionUUID] = session
            session = sesh("", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            session.sessionUUID = fileSessionUUID
            existingUUID.append(session.sessionUUID)
            # print("Creating new session ", fileSessionUUID)
            # print(existingUUID)
            # print(sessions)

        elif (fileSessionUUID != session.sessionUUID and fileSessionUUID in existingUUID): # if file's UUID is not the previous one, but has been seen before, use the old one
            for j in sessions:
                if sessions[j].sessionUUID == fileSessionUUID:
                    # print("Found duplicate session ", fileSessionUUID)
                    sessions[session.sessionUUID] = session
                    session = sessions[j]  # then set the current session to the old matched session
                    # print(sessions[j].TotalEvents, sessions[j].sessionUUID)
                    break

        session.TotalEvents += 1
        if (eventType == "VersionControlEvent"):
            session.VersionControlEvents += 1
        elif (eventType == "EditEvent"):
            session.EditEvents += 1
        elif (eventType == "CommandEvent"):
            session.CommandEvents += 1
        elif (eventType == "DocumentEvent"):
            session.DocumentEvents += 1
        elif (eventType == "ActivityEvent"):
            session.ActivityEvents += 1
        elif (eventType == "NavigationEvent"):
            session.NavigationEvents += 1
        elif (eventType == "TestRunEvent"):
            session.TestRunEvents += 1
        elif (eventType == "WindowEvent"):
            session.WindowEvents += 1
        elif (eventType == "CompletionEvent"):
            session.CompletionEvents += 1
        elif (eventType == "SystemEvent"):
            session.SystemEvents += 1
        elif (eventType == "DebuggerEvent"):
            session.DebuggerEvents += 1
        elif (eventType == "SolutionEvent"):
            session.SolutionEvents += 1
        elif (eventType == "IDEStateEvent"):
            session.IDEStateEvents += 1
        else:
            session.UndefinedEvents += 1

        data.close()
        i += 1


    sessions.pop("")
    for i in sessions:
        if sessions[i].TotalEvents > 0: 
            print("Session ID: ", sessions[i].sessionUUID, " Number of Events: ", sessions[i].TotalEvents, "\n    Version Control: ", sessions[i].VersionControlEvents, "\n    Edit: ", sessions[i].EditEvents, "\n    Command: ", sessions[i].CommandEvents, "\n    Document: ", \
                sessions[i].DocumentEvents, "\n    Activity: ", sessions[i].ActivityEvents, "\n    Navigation: ",sessions[i].NavigationEvents, "\n    Test Run: ",sessions[i].TestRunEvents, "\n    Window: ",sessions[i].WindowEvents, "\n    Completion: ",sessions[i].CompletionEvents, \
                    "\n    System: ", sessions[i].SystemEvents, "\n    Debugger: ",sessions[i].DebuggerEvents, "\n    Solution: ",sessions[i].SolutionEvents, "\n    IDE State: ",sessions[i].IDEStateEvents, "\n    Undefined: ",sessions[i].UndefinedEvents ,file=open("output.txt", "a"))   # ,file=open("output.txt", "a")
    
    counter = 0
    for j in sessions:
        print(sessions[j].sessionUUID, sessions[j].TotalEvents)
        counter += sessions[j].TotalEvents
    print(len(sessions), " sessions", file=open("output.txt", "a"))
    print(len(existingUUID), " sessionUUIDs", file=open("output.txt", "a"))
    print(counter, " jsons looked at", file=open("output.txt", "a"))
if __name__ == "__main__":
    main()
