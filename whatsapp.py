# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 13:33:52 2021

@author: 97254
"""

Path0 = "C:\\Users\97254\Desktop\HW\HW3\�צאט WhatsApp עם יום הולדת בנות לנויה.txt"
PathGroup = "C:\\Users\97254\Desktop\HW\HW3\_צ'אט WhatsApp עם הורים סטודנטים.txt"
PathPrivate = "C:\\Users\97254\Desktop\HW\HW3\_צ'אט WhatsApp עם רעות לימודים.txt"
path =  input("Enter file path: ")
group_chat = False
with open(path,'r',encoding="utf8") as Conversation:
    ids=dict()
    masseges=list()
    added_line=False
    line_index=0
    for line in Conversation:
        line_index+=1
        if line_index==2:
            Creation_Date=line.split()[0][:-1]
            if line.split()[3] == "‏הקבוצה": # case group chat
                group_chat = True
                Creator=line[line.index("נוצרה על ידי") + 13:]
                Conversation_Name = "שיחה קבוצתית - " + (" ").join(line[:line.index("נוצרה על ידי")].split()[4:]).replace('"', "")
        date_massege = line.split(" - ")
        if len(date_massege) > 1:
            date = date_massege[0]
            person_massege = (" - ").join(date_massege[1:]).split(":")
            if len(person_massege) > 1:
                person=person_massege[0]
                ids[person]=ids.get(person,len(ids)+1)
                massege=(":").join(person_massege[1:])
                masseges.append({"DateTime": date, "ID": ids[person],
                                 "Text": massege})
                added_line = True
            else:
                added_line = False
        elif added_line: # case the massege has more then one row
            masseges[len(masseges)-1]["Text"]=masseges[len(masseges)-1]["Text"]+" "+line

    NumOfPatricipents=len(ids)
    if not group_chat : # case private chat
        Creator=list(ids.keys())[list(ids.values()).index(1)]
        Partner=list(ids.keys())[list(ids.values()).index(2)]
        Conversation_Name = "שיחה פרטית - " + Creator + " , " + Partner
        
with open(path,'r',encoding="utf8") as Conversation:
    replaced_ids=Conversation.read()
    for person_name,new_id in ids.items():
        replaced_ids=replaced_ids.replace(person_name, str(new_id))

with open(path,'w',encoding="utf8") as Conversation:
    Conversation.write(replaced_ids)
    
meta_data = {'chat_name': Conversation_Name,
            'creation_date': Creation_Date,
            'num_of_participants': NumOfPatricipents,
            'creator': Creator}

chat = {'masseges': masseges,
        'meta_data': meta_data}

import json
chat_json = json.dumps(chat,ensure_ascii=False)
exp_file_name=Conversation_Name+".txt"
with open(exp_file_name,"w",encoding="utf8") as exp:
    exp.write(chat_json)









