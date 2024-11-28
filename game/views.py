from django.shortcuts import render,redirect
from .models import Question, Choice , Type

answer_list=[]
# Create your views here.
def game(request,name,id):
    questions = Question.objects.filter(type_id__topic=name)
    type = Type.objects.get(topic=name)

    
    # ตั้งค่าเริ่มต้น
    if answer_list == []:
         for i in questions:
            answer_list.append("")
            
    # รีเซ็ตค่าถ้าอันเก่ามีมากกว่าให้ลบถ้ามีน้อยกว่าให้เพิ่ม  
    if id == 1: 
         if len(answer_list) == len(questions):
             print("เท่ากัน")
         
        # ถ้า answer_list มากไปให้ลบ  
         elif len(answer_list) > len(questions): 
             num = len(answer_list) - len(questions)
             del answer_list[:num]
            #  print("ANมากกว่า") 
        
        # ถ้า answer_list น้อยไปให้เพิ่ม
         elif len(answer_list) < len(questions):
             num = len(questions) - len(answer_list)
             answer_list.extend([""] * num)
            #  print("ANน้อยกว่า")     
                                 
    
    if request.method == "POST":
        
        # saveตามเเต่ละตำเเหน่งที่วนloop
        print(f"{len(answer_list)}:{len(questions)}")
        if len(answer_list) <= len(questions) :
            choice_id = request.POST.get('answer')
            choice = Choice.objects.get(id=choice_id)
            answer_list[id-3] = choice.answer
            # answer_list.append(choice.answer)
            # print(answer_list)
            # print("+++++++++++++++++++++")


    # ประกาศตัวเเปร
    question = ""
    choices = ""
    x="hello"
    
    # system next page
    next_page = id+1
    
    # system back page
    if id > 1:
        back_page = id-1
    else:
        back_page=1  
    
    # หน้าอื่นๆ
    if id > 1 and id < (len(questions)+2):
        id_position = id-2
    
        for i in questions:
            if i == questions[id_position]:
                question = questions[id_position]
        print(question.question)  
        print(question.id) 
        choices = Choice.objects.filter(question_id=question.id)
       
    # ถ้า id ไปถึงหน้าสุดท้าย   
    elif id >= (len(questions)+2):
        next_page="end"
        # แทนที่ question ด้วย answer
        question = answer_list

    quantity = len(choices)
    
    return render(
        request,
        'page/game.html',
                {"x":x,
                 "id":id,
                 "next_page":next_page,
                 "back_page":back_page,
                 "question":question,
                 "choices":choices,
                 "type":type,
                 "name":name,
                 "quantity":quantity
                 }
                )    


def main(request):
    x="hello"
    types = Type.objects.all()
    return render(request,"main.html",{"x":x,"types":types})



    