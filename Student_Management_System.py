
Str_Grade = "姓名:{}\t數學成績:{} 國文成績:{} 英文成績:{}\n" #成績內容
Grade_List = [] #成績列表

while True:
    print(
"""
***************************
歡迎使用【學生資訊管理系統】
請選擇你想要進行的操作
1.新增學生資訊
2.顯示全部資訊
3.查詢學生資訊
4.刪除學生資訊
5.修改學生資訊

0.退出系統
***************************
""")

    Action = input("請選擇你想要進行的操作:\n") #使用者輸入

    if Action == "1": #新增學生信息
        Name = input("請輸入名字:")
        Math = input("請輸入數學成績:")
        Chinese = input("請輸入國文成績:")
        English = input("請輸入英文成績:")
        Grade_List.append([Name,Math,Chinese,English])
        print(Str_Grade.format(Name,Math,Chinese,English))

    elif Action == "2": #顯示全部資訊
        for data in Grade_List:
            print(Str_Grade.format(*data)) #格式化字典的簡便方法

    elif Action == "3": #查詢學生資訊
        Name = input("請輸入要查詢學生的姓名:")
        for data in Grade_List: #尋找此學生是否存在
            if Name in data: 
                print(Str_Grade.format(*data)) #查詢此學生資訊
                break
        else: 
            print("此學生不存在!")

    elif Action == "4": #刪除學生資訊
        Name = input("請輸入要刪除學生的姓名:")
        for data in Grade_List:  # 尋找此學生是否存在
            if Name in data: 
                Grade_List.remove(data) #刪除此學生資訊
                break
        else:  
            print("此學生不存在!")

    elif Action == "5": #修改學生資訊
        Name = input("請輸入要修改學生的姓名:")
        for data in Grade_List:  # 尋找此學生是否存在
            if Name in data:  
                index = Grade_List.index(data) #取得此學生資訊之索引
                Math = input("請輸入數學成績:")
                Chinese = input("請輸入國文成績:")
                English = input("請輸入英文成績:")
                Grade_List[index] = [Name,Math,Chinese,English]
                print("修改後的資訊",Grade_List[index])
                break
        else: 
            print("此學生不存在!")

    elif Action == "0": #退出系統
        break

    else: 
        print("輸入資訊有誤，請重新輸入!")
