import json, os

def main():
    base_path = 'E:/ESEData'
    based_path = 'E:/ESEData/'
    files = [pos_json for pos_json in os.listdir(base_path) if pos_json.endswith('.json')]
    print(len(files))
    for i in range(0, 100):
        data = open(based_path + files[i])
        data2 = json.load(data)
        print(data2['$type'].split(',')[0])
        print(data2['IDESessionUUID'])
        data.close()
        i += 1

    
if __name__ == "__main__":
    main()
