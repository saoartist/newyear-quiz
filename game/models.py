from django.db import models

class Type(models.Model):
    description = models.TextField(max_length=5000, default='')  # คำอธิบาย
    topic = models.TextField(max_length=255, default='')  # หัวข้อ
    url = models.TextField(default="")
    lordicon = models.TextField(default="")

    def __str__(self):
        return self.topic
    

class Question(models.Model):
    question = models.TextField(max_length=5000)  # คำถาม
    description = models.TextField(max_length=5000, default='')  # คำอธิบาย
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type_question',default=1)  # ใช้ ForeignKey เชื่อมโยงกับ Type
    
    

    def __str__(self):
        return self.question

    
class Choice(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_choices',default=1)  # ใช้ ForeignKey เชื่อมโยงกับ Question
    description = models.TextField(default='')  # คำอธิบายตัวเลือก
    answer = models.TextField(default='')  # คำตอบ
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type_choices',default=1)  # ใช้ ForeignKey เชื่อมโยงกับ Type

    def __str__(self):
        return f"Choice: {self.description[:50]}"  # แสดงคำอธิบายตัวเลือก