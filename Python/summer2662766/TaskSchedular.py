import json
import datetime
class TaskManager:
    def __init__(self):
        pass

    def loadFile(self,file:str):
        """load any file with this function ,
        parameters:
            file: filename and its extension included should be in form of string 
        Raise:
            FileNotFoundError : when the given file does not exist
        """
        try:
            with open(file,"r") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("FileNotFound")
        return data

    def saveFile(self,file,data):
        with open(file,"w") as f:
            data = json.dumps(data)
            f.write(data)
        print("Saved")

    def addTask(self,unfinished):
        taskDescription = input("Task Description : ")
        expectedCompletion = input("Expected Completion Time (%yyyy-%mm-%dd)")
        taskAddedTime = datetime.datetime.now().strftime("%yy-%m-%d,%H:%M")

        date = str(datetime.datetime.now().date())
        if str(date) in unfinished.keys():
            next = len(unfinished[date].keys())

            unfinished[date][next + 1]= {
                "task":taskDescription,
                "taskAdded":taskAddedTime,
                "expectedCompletion":expectedCompletion}

            print(f"Successfully Added new Task Time Added {taskAddedTime} Expected Completion Time {expectedCompletion}")

        else:
            print("here 3")
            unfinished[date] = {1:{
                    "task":taskDescription,
                    "taskAdded":taskAddedTime,
                    "expectedCompletion":expectedCompletion
            }

            }
         
            print(f"Successfully Added new Task Time Added {taskAddedTime} Expected Completion Time {expectedCompletion}")
    
    def showUnfinishedTasks(self,unfinished):
            print("1. Todays")
            print("2. ALL")

            choice = int(input("Choice : "))
            
            if choice == 1:
                print(f"Index\t Key\tExpected Completion \tTask")
                today = str(datetime.datetime.now().date())
                c = 1
                if len(unfinished[today]) > 0:

                    for key in unfinished[today].keys():
                        
                        print(f"{c}\t key[{key}]\t {unfinished[today][key]['expectedCompletion']} \t {unfinished[today][key]['task']}   ")
                        c += 1
                else:
                    print("No tasks for today")
            
            elif choice == 2:
                totalLength = 0
                for day in unfinished.keys():
                    print(f"Index\t Key\t Day\t Expected Completion \tTask")
                    c = 1
                    totalLength += len(unfinished[day])
                    if len(unfinished[day]) > 0:
                        for key in unfinished[day].keys():
                            print(f"{c} key[{key}] \t {day} {unfinished[day][key]['expectedCompletion']} \t {unfinished[day][key]['task']}   ")
                            c += 1

                
                if totalLength == 0:
                    print("No Unfinished Tasks")
            else:
                print("invalid Choice")





    def markTask(self,finished,unfinished):

        print("~"*20)
        print("1. Mark Todays Task Complete")
        print("2. Enter Day Task Date : ")

        choice = int(input("Choice 1-2 : "))
        print(f"Your Choice : {choice}")

        completion = datetime.datetime.now().strftime("%y-%m-%d %H:%M")
        if choice == 1:
            self.showUnfinishedTasks(unfinished)
            today = str(datetime.datetime.now().date())
            if today in unfinished.keys():
                k = input("Enter Task Key Number : ")
                add = unfinished[today][k]
                add['completion'] = completion
                del unfinished[today][k]
                if len(finished) > 0:
                    l = len(finished)
                    finished[l+1] = add
                    print("Marked Complete")
                else:
                    finished[1] = add
                    print("Marked Completer")
            else:
                print("No unfinished tasked for today")
        elif choice == 2:
            self.showUnfinishedTasks(unfinished)
            date = input("Enter Date format (%yyyy-%mm-%dd)")
            if date in unfinished.keys():
                j = input('Enter Task Number')
                if j in unfinished[date].keys():
                    add = unfinished[date][j]
                    add["completion"] = completion

                    del unfinished[date][j]
                    if len(finished) > 0:
                        l = len(finished)
                        finished[l + 1] = add
                        print("Marked Complete")
                    else:
                        finished[1] = add
                        print("Marked Complete")

        else:
            print("Invalid Choice")


    
    def showFinishedTasks(self,finished):
        # one day all the voices in your head will be gone 
        # because Allah is with those who do sabar,
        # Trust in Allah
        # don't stress yourself with what will happen in Future like I do , In the end Future is very good than your past , It happened to me, live a little
        # 'Your future will be better than your past' Al Quran
        print(f"Index \t Task Added \t\tExpected Completion \tCompletion \t Task")
        for idx,key in enumerate(finished.keys()):
            idx += 1
            print(f"{idx} \t {finished[key]['taskAdded']}\t {finished[key]['expectedCompletion']} \t      {finished[key]['completion']} \t{finished[key]['task']}")



    
