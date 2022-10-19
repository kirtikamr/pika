#!!!!!!!!!!!!!!!11111111111111!!!!!!!!!!!!!!!!!!
#models.py

'''from django.db import models

class Student(models.Model):
        name=models.CharField(max_length=20)
        age=models.IntegerField()
        email=models.EmailField()
        addr=models.CharField(max_length=50)

        def __str__(self):
                return self.name'''

#admin.py

'''from . models import Student

class StudentAdmin(admin.ModelAdmin):
        list_display=['name','age','email','addr']
        
admin.side.register(Student,StudentAdmin) '''

#serializers.py

'''from . models import Student
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
        name=serializers.CharField(max_lenth=30)
        age=serializers.IntegerField()
        email=serializers.EmailField()
        addr=serilaizers.CharField(max_length=50)
        
'''
#views.py

'''from django.shortcuts import render
from django.http import JsonResponse
from . serializers import StudentSerilaizer
from . models import Student

def studentListView(request):
        students=Student.objects.all()
        serilaizer=StudentSerilaizer(students,mant=True)
        return JsonResponse(serializer.data,safe=False)'''

#urls.py

'''from django.urls import path
from app1.views import studentListView

urlspatterns=[
        path('api/student',studentListView),
        ]
'''
#!!!!!!!!!!!!!!!!!!!!!!222222222222222222!!!!!!!!!!!!!!!!(13:04:85)
#models.py
'''from django.db import models

class Student(models.Model):
        name=models.CharField(max_length=20)
        age=modles.IntegerField()
        email=models.EmailField()
        addr=models.CharField(max_length=50)

        def __str__(self):
                return self.name'''

#admin.py
        
'''from django.contrib import admin
from . models import Student

class StudentAdmin(admin.ModelAdmin):
        list_disply=['name','age','email','addr']

admin.site.register(Student,StudentAdmin)  '''

#serializers.py

'''from . models import Student
from rest_fromework import serializers

class StudentSerializers(serializers.Serializer):
        name=serializers.CharField(max_length=30)
        age=serializers.IntegerField()
        email=serializers.EmailField()
        addr=serializers.CharField(max_length=50)'''

#views.py

'''from django.shortcuts import render
from django.http import JsonResponse
from . seralizers import StudentSerializers
from . models import Student


def studenListView(request):
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)

        return JsonResponse(serializer.data,safe=False)'''

#urls.py

'''from django.shortcuts import path
from app1.views import studentListView
ulrspatterns=[
        path('api/student',studdentListView)]'''


#!!!!!!!!!!!!!!!P2CBV!!!!!!!!!!!!!!!!!!P2CBV!!!!!!!! Clas Based View

#views.py

'''from rest_framework.views import APIView
from . models import Employee
from . serializer import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status


class EmployeeListView(APIView):
        def get(self,request):
                employee=Employee.objects.all()
                serializer=EmployeeSerializer(employee,many=True)
                return Response(serializer.data)

        def post(self,request):
                employeeSerializer=EmployeeSerializer(data=request.data)
                if employeeSerializer.is_valid():
                        employeeSerializer.save()
                        return Response(employeeSerializer.data,status=status.HTTP_201_CREATED)
                return Response(employeeSerializer.errors)'''


#!!!!!!!!!!!!!!!!!!!!!!!2222222222!!!!!!!!!!!!!!!!!!!!

#models.py
'''from django.db import models

class Employee(models.Model):
        ename=models.CharField(max_length=30)
        esal=models.FloatField()
        eaddr=models.CharField(max_length=60)

        def __str__(self):
                return self.ename'''


#admin.py

'''from django.contrib import admin
from . models import Employee

class EmployeeAdmin(admin.ModelAdmin):
        list_disply=['ename','esal','eaddr']
        
admin.site.register(Employee,EmployeeAdmin)'''

#serializers.py

'''from . models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
        class Meta:
                model=Employee
                fields='__all__'
                '''

#views.py
'''from rest_framework.view import APIView
from . models import Employee
from . serializers impport EmployeeSerializer

class EmployeeListView(APIView):

        def get(self,request):
                employees=Employee.objects.all()
                serializer=EmployeeSerializer(employee,many=True)
                return Response(serializer.data)

        def post(self,request):
                serializer=EmployeeSerializer(data=request.data)
                if serializer.is_valid():
                        serializer.save()

                        return Response(serializer.data,status=status.HTTP_201_CREATED)
                return Response(serializer.errors)

class EmployeeDetailView(APIView):
        def get_employee(self,pk):
                try:
                        return Employee.objects.get(pk=pk)
                except Employee.DoesNotExist:
                        raise Http404
        def get(self,request,pk):
                employee=self.get_employee(pk)
                serializer=EmployeeSerializer(employee)
                return Response(serializer.data)
        
        def put(self,request,pk):
                employee=self.get_employee(pk)
                employeeSerializer=EmployeeSerializer(employee,data=request.data)
                if employeeSerializer.is_valid():
                        employeeSerializer.save()
                        return Response(employeeSerializer.data)
                return Response(employeeSerialser.errors)
        
        def delete(self,request,pk):
                self.get_employee(pk).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)'''

#urls.py

'''from django.shortcuts import path
from appname.views import EmployeeListView,EmployeeDetailView

urlpatterns=[
        path('test/<int:pk>',EmployeeDetailView.as_view()),

        ]
        
'''

#!!!!!!!!!!!!!!!!!!!!!MIXIN V21!!!!!!!!!!!!!!!!

#models.py
'''from django.db import models

class Student(models.Model):
        name=models.CharField(max_length=50)
        rollno=models.IntergerField()
        marks=models.IntergerField()


        def __st__(self):
                return self.name'''

#admin.py

'''from django.contrib import admin
from . models import Student

class StudentAdmin(admin.ModelAdmin):
        list_display=['name','marks']
        
admin.site.register(Student,StudentAdmin)'''


#serializers.py
'''from rest_framework import serializers
from . models import Student

class StudentSerializer(serializers.ModelSerializer):
        class Meta:
                model=Student
                fields='__all__'''

#views.py
'''from rest_framework import mixins,generic
from . models import Student
from rest_framework import StudentSerializer

class StudentListView(generics.GenericAPI,mixins.ListModelMixin,mixins.CreateModelMixin):
        queryset=Student.objects.all()
        serializer_class=StudentSerializer

        def get(self,request):
                return self.list(request)

        def post(self,request):
                return self.create(request)
                

class StudentDetailView(gereric.GerericAPI,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
        queryset=Student.objects.all()
        serializer_class=StudentSerializer

        def get(self,request,pk):
                return self.retrieve(request,pk)

        def put(self,request,pk):
                return self.update(request,pk)

        def delete(self,request,pk):
                return self.destroy(request,pk)'''

#urls.py

'''from django.shortcuts import path
from appname.views import StudentListView,StudentDetailView

urlspatterns=[
        path('student/',StudentListView.as_view()),
        path('student/<int:pk>',StudentDetailView.as_view()),
        ]

'''

#models.py
'''from djangodb import models

class Employee(models.Model):
        name=models.CharField(max_length=50)
        sal=models.FloatField()
        addr=models.CharField(max_length=100)
        
        def __str__(self):
                return self.name'''

#admin.py
'''from . models import Employee

class EmployeeAdmin(admin.ModelAdmin):
        list_display=['name','sal','addr']

        
admin.site.register(Employee,EmployeeAdmin)'''

#serializers.py

'''from .models import Employee
from rest_frameworks import serializers


class EmployeeSerializer(serializers.ModelSerializer):
        class Meta:
                model=Employee
                fields='__all__'
                
        
'''

#views.py
'''from rest_framework import generics,mixins
from . models import Employee

class EmployeListView(generics.GenericAPIView,mixin.ListModelMxin,mixins.CreateModelMixin):
        queryset=Employee.objects.all()
        serializer_class=EmployeeSerializer

        def get(self,request):
                return self.list(request)

        def post(self,request):
                return self.create(request)

class EmployeeDetailView(generics.GenericAPIView,mixins.RetreiveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
        queryset=Employee.objects.all()
        serializer_class=EmployeeSerializer

        def get(self,request,pk):
                return self.retreive(request,pk)
        def put(self,request,pk):
                return self.update(request,pk)
        def delete(self,request,pk):
                return self.destroy(request,pk)'''


#urls.py
'''from appname.views import EmployeeListView,EmployeeDetailView


urlspatterns=[
        path('employee/',EmployeeListView.as_view()),
        path('employee/<int:pk>',EmployeeDetailView.as_view())]'''


#views.pt


'''class EmployeeListView(generics.ListAPIView,generics.CreateAPIView):
        queryset=Employee.objects.all()
        serializer_class=EmployeeSerializer

class EmployeeDetailView(generics.DestroyAPIView,generics.UpdateAPIView,generics.RetreiveAPIVie):
        queryset=Employee.objects.all()
        serializer_class=EmployeeSerializer'''


'''def add_num(num1,num2):
        while num2!=0:
                data=num1&num2
                num1=num1^num2
                num2=data<<1
        return num1

print(add_num(11,2))'''

'''def mul(a,b):
        if a==0 or b==0:
                return 0
        if a==1:
                return b
        if b==1:
                return a
        return a+mul(a,b-1)

def multiply(a,b):
        m=mul(a,abs(b))
        return -m if b<0 else m
print(multiply(22,4))'''

#Prime

'''n=int(input("Enter any number:"))

if n<2:
        print(n,"Not prime number")
else:
        for i in range(2,n):
                if n%i==0:
                        print(n,'not prime number')
                        break
        else:
                print(n,'Prime number')'''

'''def recur_fibo(n):
        if n<=1:
                return n
        else:
                return (recur_fibo(n-1)+recur_fibo(n-2))
        
nterms=int(input("how many terms?:"))
if nterms<=0:
        print('Please provide positive number')
else:
        for i in range(nterms):
                print(recur_fibo(i))'''

'''n=int(input("Enter any number:"))
a=0
b=1
sum=1
count=1
while count<=n:
        count=count+1
        print(a,end='')
        a=b
        b=sum
        sum=a+b'''

'''n=int(input("Enter any number:"))
a=0
b=1
sum=1
count=1
while count<=n:
        count=count+1
        print(a,end='')
        a=b
        b=sum
        sum=a+b'''

'''l=[11,1,22,2,33,3,44,4,55,5]
for i in range(len(l)):
        for j in range(i+1,len(l)):
                if l[i]>l[j]:
                        l[i],l[j]=l[j],l[i]
                        
print(l)'''

#How to remove Duplicate
#l=[1,1,2,2,2,3,4,4,5]
#print(list(set(l)))
#print(list(dict.fromkeys(l)))
'''l1=[]

for i in range(len(l)):
        for j in range(i+1,len(l)):
                if l[i]==l[j] and l[i] not in l1:
                        l1.append(l[i])

print(l1)'''

'''l=[{'id':1,'salary':100},{'id':12,'salary':200},{'salary':300}]
salary=0
for i in l:
        for j in i:
                if j=='salary':
                        salary=salary+i[j]
                        
print(salary)'''

'''s="a=2&b=23&name=milind"
l=s.split('&')
l1=[]

for i in l:
        l1.append(i.split('='))
print(dict(l1))'''


'''l=[1,2,3,4,5,6,7]
def rotatelist(l,d,n):
        l[:]=l[d:n]+l[0:d]
        return l
d=3
n=len(l)
print(l)
print(rotatelist(l,d,n))'''

'''l=[1,2,3,4,5,6,7,8,9]
k=11

for i in range(len(l)):
        for j in range(i+1,len(l)):
                if l[i]+l[j]==k:
                        print(l[i],l[j])'''


'''def recur_fibo(n):
        if n<=1:
                return n
        else:
                return(recur_fibo(n-1)+recur_fibo(n-2))
        
nterms=int(input("How many terms:"))
if nterms<=0:
        print('please provide positive number')
        
else:
        for i in range(nterms):
                print(recur_fibo(i))'''

'''n=int(input("Enter any number:"))

a=0
b=1
sum=1
count=1
while count<=n:
        count=count+1
        print(a,end='')
        a=b
        b=sum
        sum=a+b'''

'''s='/*apple are & found % only @ red & green'
output=''

for i in s:
        if ((i>="A" and i<="Z")|
            (i>="a" and i<="z")|
            (i==" ")):
                output=output+i
                
print(output)'''

'''s="impliciteimpliciteimlp"
d={}
for i in s:
        if i in d:
                d[i]+=1
        else:
                d[i]=1
                
ch=max(d,key=d.get)

print(ch)'''
'''l=[11,23,3,24,35346,76,577]
largest=l[0]
sec_largest=l[0]

for i in range(len(l)):
        if l[i]>largest:
                largest=l[i]
                
for i in range(len(l)):
        if l[i]>sec_largest and l[i]!=largest:
                sec_largest=l[i]
                
print(sec_largest)
'''

'''def add_num(num1,num2):
        while num2!=0:
                data=num1&num2
                num1=num1^num2
                num2=data<<1
        return num1
print(add_num(222,45))'''


'''def mul(a,b):
        if a==0 or b==0:
                return 0
        if a==1:
                return b
        if b==1:
                return a
        return a+mul(a,b-1)

def multiply(a,b):
        m=mul(a,abs(b))
        return -m if b<0 else m
print(multiply(233,5))'''

'''n=int(input("Enter any number:"))
a=0
b=1
count=1
sum=1
while count<=n:
        count=count+1
        print(a,end='')
        a=b
        b=sum
        sum=a+b'''
'''n=int(input("Enter any number:"))
temp=n
order=len(str(n))
sum=0
while temp>0:
        digit=temp%10
        sum=sum+digit**order
        temp//=10

if n==sum:
        print(n,'is armstrong number')
        
else:
        print(n,'Not Arm')'''

'''s="One Two THree Four FIve Six"
l=s.split()
l1=[]
i=0
while i<len(l):
        if i%2==0:
                l1.append(l[i])
        else:
                l1.append(l[i][::-1])
        i=i+1

output=' '.join(l1)
print(output)'''

'''s="milind rattt"
d={}
for ch in s:
        if ch in d:
                d[ch]+=1
        else:
                d[ch]=1
ch=max(d,key=d.get)
print(ch)'''

'''import json
  
# JSON string
employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'
  
# Convert string to Python dict
employee_dict = json.loads(employee)
print(employee_dict)
print(type(employee_dict))
print("\n")
  
# Convert Python dict to JSON
json_object = json.dumps(employee_dict, indent=4)
print(json_object)
print(type(json_object))'''

'''
from rest_framework.views import APIView
from .model import Employee
from . serailizers import EmployeeSerializer
from rest_framework import status
from djsngo.http import Http404
class EmployeeListView(APIView):
        def get(self,request):
                employee=Employee.objects.all()
                serializer=EmployeeSerailizer(employee,many=True)
                return Response(serializer.data)
        def post(self,request):
                employeeserializer=EmployeeSerailizer(data=request.data)
                if employeeserializer.is_valid():
                        serailizer.save()
                        return Response(employeeserializer.data,status=status.HTTP_201_CREATED)
                return Response(employeeserializer.errors)
        

class EmployeeDetailView(APIView):
        def get_employee(self,pk):
                try:
                        return employee.objects.get(pk=pk)
                except Employee.DoesNotExist:
                        raise Http404
        def get(self,request,pk):
                employee=self.get_employee(pk)
                employeeserailizer=EmployeeSerializer(employee)
                return Response(employeeserializer.data)
        def put(self,request,pk):
                employee=self.get_employee(pk)
                employeeserializer=EMployeeSerializer(employee,data=request.data)
                if employeeserializer.is_valid():
                        employeesrializer.save()
                        return Response(employeeserializer.data)
                return Response(employeeserializer.errors)
        def delete(self,request,pk):
                self.get_employee(pk).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

'''

'''l=[{"id":11,"salary":100},{"salary":200},{"id":12,"salary":300}]
salary=0
for i in l:
        for j in i:
                if j=="salary":
                        salary=salary+i[j]
                        
print(salary)'''


'''l=[1,2,3,4,5,6,7,8,9]
def rotatelist(l,d,n):
        l[:]=l[d:n]+l[0:d]
        return l

n=len(l)
d=3
print(rotatelist(l,d,n))
'''

'''2+ years experience of Python coding skills
2+ years experience developing Angular JS applications into production
2+ years hands-on experience with the Django framework
Strong understanding of the Angular JS framework, front-end technologies, such as JavaScript, HTML5, and CSS3.
Solid database skills in a relational database (i.e. Post GRES SQL, MySQL, Ms SQL, etc.)
Knowledge of how to build and use with RESTful APIs
Strong knowledge of version control (i.e. GIT, SVN, etc.)
Experience deploying Python applications into production
Amazon Web Services (AWS) infrastructure knowledge is a plus'''


'''class Employee(models.Model):
        name=models.charField(max_length=50)
        age=models.IntegerField()
        salary=models.FloatField()

        def __str__(self):
                return self.name

from . models import Employee        
class EmployeeAdmin(admin,ModelAdmin):
        list_display=['name','age','salary']
        
admin.site.register(Employee,EmployeeAdmin)



class EmployeeSerializer(serializers.ModelSerializer):
        class Meta:
                model=Employee
                fields='__all__'

'''
'''class EmployeeListView(APIView):

        def get(self,request):
                employee=Employee.objects.all()
                seraializer=EmployeeSerailizer(employee,many=True)
                return Response(serializer.data)
        
        def post(self,request):
                seriailizer=EmployeeSerailizer(data=request.data)
                if serializer.is_valid():
                        seriailizer.save()
                        return Response(seriaizer.data,status=status.HTTP_201__CREATED)
                return Response(serislizer.errors)

class EmployeeDetailView(APIView):

        def get_employee(self,pk):
                try:
                        return Employee.objects.get(pk=pk)
                except Employee.DoesNotExist:
                        raise Http404

        def get(self,request,pk):
                employee=self.get_employee(pk)
                serializer=EmployeeSerailizer(employee)
                return Response(serailizer.data)

        def put(self,request,pk):
                employee=self.get_employee(pk)
                employeeserialzer=Employeeserializer(employee,data=request.data)
                if employeeserialiser.is_valide():
                        employeeserializer.save()
                        return Response(employeeserializer.data)
                return Response(employeeserializer.errors)
        def delete(self,request,pk):
                self.get_employee(pk).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        
 '''

'''class Student(models.Model):
        name=models.charField(max_length=50)
        roll=models.IntegerField()
        addr=models.CharField(max_length=50)

        def __str__(self):
                return self.name
        

class StudentAdmin(admin,ModelAdmin):
        list_display=['name','roll','addr']

        
admin.site.register(Student,StudentAdmin)

class StudentSerializer(serializers.ModelSerializer):
        class Meta:
                model=Student
                fields='__all__'
                
'''
#views.py
'''from rest_framework.views import APIView
from .model import Student
from . serailizers import StudentSerializer
from rest_framework import status
from djsngo.http import Http404

class StudentListView(APIView):
        def get(self,request):
                student=Student.objects.all()
                serializer=StudentSerailizer(student,many=True)
                return Response(serializer.data)
        def post(self,request):
                serializer=StudentSerialize(data=request.data)
                if serializer.is_valid():
                        serializer.save()
                        return Response(seriailzer.data,status=status.HTTP_201_CREATED)
                return Response(serializer.errors)


class StudentDetailView(APIView):
        
        def get_student(self,pk):
                try:
                        return Student.objects.get(pk=pk)
                except StudentDoesNotExist:
                        raise Http404

                
        def get(self,request,pk):
                student=self.get_student(pk)
                serializer=StudentSerializer(student)
                return Response(serializer.data)

        def put(self,request,pk):
                student=self.get_student(pk)
                studentserializer=StudentSerailizer(student,data=request.data)
                if studentserializer.is_valid():
                        studentserializer.save()
                        return Response(studentserializer.data)
                return Response(studentserializer.errors)

        def delete(self,request,pk):
                self.get_student(pk).delete()
                return Response(status=status.HTTP__204__NO_CONTENT)

'''
'''n=int(input("Enter any number:"))
a=0
b=1
sum=1
count=1

while count<=n:
        count=count+1
        print(a,end='')
        a=b
        b=sum
        sum=a+b'''

'''l=[1,2,3,4,6,7]
def missing(l):
        n=l[-1]
        total=n*(n+1)//2
        print(total-sum(l))
missing(l) '''

#6=1*2*3*4*5*6
'''def factorial(n):
        if n==1:
                return 1
        else:
                return n*factorial(n-1)
n=int(input("Entera any number:"))
print(factorial(n))'''

'''n=int(input("Entera any number:"))
temp=n
order=len(str(n))
sum=0

while temp>0:
        digit=temp%10
        sum=sum+digit**order
        temp//=10
        
if n==sum:
        print(n,'is armstrong number')
else:
        print(n,'is not armstrong number')'''

'''from itertools import combinations
l=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: sum(x)==10,combinations(l,3))))

'''

#VVVIMP
'''def sortby(a):
        l=[x for x in a if x!=0]
        l.sort()
        result=[]
        k=0
        for x in a:
                if x==0:
                        result.append(0)
                else:
                        result.append(l[k])
                        k=k+1
        return result
a=[0,223,345,5,2,0,0,34,55,778]
print(sortby(a))'''


'''def sortby(a):
        l=[x for x in a if x!=-1]
        l.sort()
        result=[]
        k=0
        for x in a:
                if x==-1:
                        result.append(-1)
                else:
                        result.append(l[k])
                        k=k+1
        return result
a=[-1,234234,33,324,4,-1,-1,34356,32,56,4]
print(sortby(a))'''



'''def sortby(a):
        l=[x for x in a if x!=-1]
        l.sort()
        k=0
        result=[]
        for x in a:
                if x==-1:
                        result.append(-1)
                else:
                        result.append(l[k])
                        k=k+1
        return result
a=[-1,222,33,444,333,45,66,-1,10,111,1]

print(sortby(a))'''


'''class Employee(models.Model):
        name=models.CharField(max_length=50)
        salary=models.IntegerField()

        def __str__(self):
                return self.name

        
class EmployeeAdmin(admin,ModelAdmin):
        list_display=['name','salary']
        
admin.site.register(Employee,EmployeeAdmin)


class EmployeeSerializer(serializer.ModelSerializer):
        class Meta:
                model=Employee
                fields='__all__'


class EmployeeListView(APIView):
        def get(self,request):
                employee=Employee.objects.all()
                employeeserializer=EmployeeSerializer(employee,many=True)
                return Response(employeeserializer.data)

        def post(self,request):
                employeeserializer=Employeeserializer(data=request.data)
                if employeeserilaizer.is_valid():
                        employeeeserializer.save()
                        return Response(employeeserializer.data,status=HTTP_201_CREATED)
                return Response(employeeserializer.errors)
        


class EmployeeDetailView(APIView):
        def get_employee(self,pk):
                try:
                        return Employee.objects.get(pk=pk)
                except EmployeeDoesNotExist:
                        raise Http404

        def get(self,request,pk):
                employee=self.get_employee(pk)
                employeeserializer=EmployeeSerializer(employee)
                return Response(employeeserializer.data)

        def put(self,request,pk):
                employee=self.get_employee(pk)
                employeeserializer=EmployeeSerializer(employee,data=request.data)
                if employeeserializer.is_valid():
                        employeeserializer.save()
                        return Response(employeeserializer.data)
                return Response(employeeseriaizer.errors)

        def delete(self,request,pk):
                self.get_empoloyee(pk).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)'''


'''s="Durga software solutions"
l=s.split()
l1=[]
for ch in l:
        l1.append(ch[::-1])
        
print(' '.join(l1))
'''
'''s="One Two Three Four Five Six"
l=s.split()
l1=[]
i=0

while i<len(l):
        if i%2==0:
                l1.append(l[i])
        else:
                l1.append(l[i][::-1])
        i=i+1

        
print(' '.join(l1))'''

'''class Employee(models.Model):
        name=models.CharField(max_length=50)
        salary=models.IntegerField()
        addr=models.CharField(max_length=50)

        def __str__(self):
                return self.name

        
class EmployeeAdmin(admin,ModelAdmin):
        list_display=['name','salary','addr']

admin.site.register(Employee,Employeeadmin)


class EmployeeSerializer(serializers.ModelSerializer):
        class Meta:
                model=Employee
                fields='__all__'
                

class EmployeeListView(APIView):
        def get(self,request):
                employee=Employee.objects.all()
                employeeserializer=EmployeeSerializer(employee,many=True)
                return Response(employeeserializer.data)

        def post(self,request):
                employeeserializer=EmployeeSerailizer(data=request.data)
                if employeeserializer.is_valid():
                        employeeserilaizer.save()
                        return Response(employeeserailizer.data,status=status.HTTP_201_CREATED)
                return Response(employeeserializer.errrors)

class EmployeeDetailView(APIView):
        def get_employee(self,pk):
                try:
                        return Employee.objects.get(pk=pk)
                except EmployeeDoesNotExist:
                        raise Http404

        def get(self,request,pk):
                employee=self.get_employee(pk)
                employeeserailizer=EmployeeSerializer(employee)
                return Response(employeeserializer.data)

        def put(self,request,pk):
                employee=self.get_employee(pk)
                employeeserializer=EmployeeSerailizer(employee,data=request.data)
                if employeeserializer.is_valid():
                        employeeserializer.save()
                        return Response(employeeserializer.data)
                return Response(employeeserailizer.errors)
                    
        def delete(self,request,pk):
                self.get_employee(pk).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        
'''
'''l=[1,1,2,2,3,3,4,5]
print(list(set(l)))
print(list(dict.fromkeys(l)))

l1=[]
for ch in l:
        if ch not in l1:
                l1.append(ch)
print(l1)                
'''

'''l=[1,1,2,2,3,3,4,5]
l1=[]

for i in range(len(l)):
        for j in range(i+1,len(l)):
                if l[i]==l[j] and l[i] not in l1:
                        l1.append(l[i])
                        
print(l1)'''

'''l=[1,2,3,4,5,6,7,8,9]
def rotatelist(l,d,n):
        l[:]=l[d:n]+l[0:d]
        return l
n=len(l)
d=3
print(rotatelist(l,d,n))
'''

'''l=[1,2,3,4,5,6,7,8,9]
k=10
for i in range(len(l)):
        for j in range(i+1,len(l)):
                if l[i]+l[j]==k:
                        print(l[i],l[j])


from itertools import combinations
l=[1,2,3,4,5,6,7,8,9]
k=10
print(list(filter(lambda x : sum(x)==k,combinations(l,2))))'''

'''n=int(input("Enter any number:"))
a=0
b=1
sum=1
count=1

while count<=n:
        count=count+1
        print(a,end='')
        a=b
        b=sum
        sum=a+b
        


def recur_fibo(n):
        if n<=1:
                return n
        else:
                return recur_fibo(n-1)+recur_fibo(n-2)
        
nterms=int(input("How many terms:"))
if nterms<=0:
        print("Please Enter aPositive number")
        
else:
        for i in range(nterms):
                print(recur_fibo(i))

'''

'''s="implicityimpliciyimpli"
d={}

for i in s:
        if i in d:
                d[i]+=1
        else:
                d[i]=1
                
max_chr=max(d,key=d.get)
print(max_chr)'''

'''def even_odd(n):
        if n%2==0:
                print(n,'is even number')
        else:
                print(n,'is odd number')

n=int(input("Enter any number:"))                
even_odd(n)
'''

'''def add_num(num1,num2):
        while num2!=0:
                data=num1&num2
                num1=num1^num2
                num2=data<<1
        return num1
print(add_num(223,3))'''


'''def mul(a,b):
        if a==0 or b==0:
                return 0
        if a==1:
                return b
        if b==1:
                return a
        return a+mul(a,b-1)

def multiply(a,b):
        m=mul(a,abs(b))
        return -m if b<0 else m

print(multiply(22,4))'''

'''l=[1,2,3,5,6,7]
def missing(l):
        n=l[-1]
        total=n*(n+1)//2
        print(total-sum(l))
missing(l)'''

#Prime number

'''n=int(input("Enter anay number:"))

if n<2:
        print(n,'Not prime number')
        
else:
        for i in range(2,n):
                if n%i==0:
                        print(n,'not prime number')
                        break
        else:
                print(n,'prime number')'''


'''def factorial(n):
        if n==1:
                return 1
        else:
                return n*factorial(n-1)
n=int(input("Enter any number:"))
r=factorial(n)
print(r)
'''
#Armstrong number

'''n=int(input("Entera ny number:"))
temp=n
sum=0
order=len(str(n))

while temp>0:
        digit=temp%10
        sum=sum+digit**order
        temp//=10

        
if n==sum:
        print(n,'is an prime number')
else:
        print(n,'not prime number')'''

'''s="One Two Three Four Five Six"
l=s.split()
l1=[]
i=0
while i<len(l):
        if i%2==0:
                l1.append(l[i])
        else:
                l1.append(l[i][::-1])
        i=i+1
        
print(' '.join(l1))'''

'''s="a4b2d4"
output=''

for ch in s:
        if ch.isalpha():
                x=ch
        else:
                d=int(ch)
                output=output+x*d
                
print(output)'''

'''s="a4b2d4"
output=''

for ch in s:
        if ch.isalpha():
                x=ch
                output=output+ch
        else:
                d=int(ch)
                new=chr(ord(x)+d)
                output=output+new
                
print(output)'''
'''s="sjldkkfj"
d={}
output=''

for ch in s:
        d[ch]=d.get(ch,0)+1
        
for k,v in sorted(d.items()):
        output=output+k+str(v)
print(d,output)'''

#Service Unavailable
'''The server is temporarily unable to service your request due
to maintenance downtime or capacity problems. Please try again later.

Additionally, a 503 Service Unavailable error was encountered while
trying to use an ErrorDocument to handle the request.'''


'''class Employee(models.Model):
        name=models.CharField(max_length=50)
        salary=models.IntegerField()
        addr=models.CharField(max_length=50)

        def __str__(self):
                return self.name
        
class EmployeeAdmin(admin,ModelAdmin):
        list_display=['name','salary','addr']

        
admin.site.register(EMployee,EmployeeAdmin)


class Employeeseriaizer(serializers.ModelSerializer):
        class Meta:
                model=Employee
                fields="__all__"


class EmployeeListView(APIView):

        def get(self,request):
                employee=Employee.objects.all()
                employeeserailizer=EmployeeSerializer(employee,many=True)
                return Response(employeeserializer.data)

        def post(self,request):
                employeeseriaizer=EmployeeSerializer(data=request.data)
                if employeeserializer.is_valid():
                        employeeserializer.save()
                        return Response(employeeserializer.data,status=status.HTTP_201_CREATED)
                return Response(employeeserializer.errors)

        
class EmployeeDetailView(APIView):

        def get_employee(self,pk):
                try:
                        return Employee.objects.get(pk=pk)
                except EmployeeDoesNotExist:
                        raise Http404

        def get(self,request,pk):
                employee=self.get_employee(pk)
                employeeserializer=EmployeeSerializer(employee)
                return Response(employeeserializer.data)

        def put(self,request,pk):
                employee=self.get_employee(pk)
                employeeserializer=EmployeeSerializer(employee,data=request.data)
                if employeeserializer.is_valid():
                        employeeserializer.save()
                        return Response(employeeserializer.data)
                return Response(employeeserializer.errors)

        def delete(self,request,pk):
                self.get_employee(pk).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        

'''

'''def add_num(num1,num2):
        while num2!=0:
                data=num1&num2
                num1=num1^num2
                num2=data<<1
        return num1

print(add_num(22,34))'''


'''def mul(a,b):
        if a==0 or b==0:
                return 0
        if a==1:
                return b
        if b==1:
                return a
        return a+mul(a,b-1)
def multiply(a,b):
        m=mul(a,abs(b))
        return -m if b<0 else m
print(multiply(222,3))'''


'''n=int(input("Entera nan number:"))
if n<2:
        print(n,"Not prime number")
        
else:
        for i in range(2,n):
                if n%i==0:
                        print(n,'Not prime number')
                        break
        else:
                print(n,'prime number')'''


'''def missing(l):
        n=l[-1]
        total=n*(n+1)//2
        print(total-sum(l))
        
l=[1,2,3,5,6,7]
missing(l)'''

'''def factorial(n):
        if n==1:
                return 1
        else:
                return (n*factorial(n-1))
n=int(input("Enter any number:"))
print(factorial(n))'''


'''n=int(input("Entera any number:"))
a=0
b=1
sum=1
count=1

while count<=n:
        count=count+1
        print(a,end='')
        a=b
        b=sum
        sum=a+b
        

def recur_fibo(n):
        if n<=1:
                return n
        else:
                return(recur_fibo(n-1)+recur_fibo(n-2))
        
nterms=int(input("ENter how many terms:"))

if nterms<=0:
        print("Please Provide Positive number")

else:
        for i in range(nterms):
                print(recur_fibo(i))'''


'''n=int(input("Enter any number:"))
temp=n
order=len(str(n))
sum=0

while temp>0:
        digit=temp%10
        sum=sum+digit**order
        temp//=10
        
if sum==n:
        print("Armstrong number")
        
else:
        print("Not Armstrong numbeer")'''


#STATIC_FILES

'''django.contrib.staticfiles >>>>>>>in install app

STATIC_URL='/static'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]

MEDIA_URL='/imeges/'
MEDIA_ROOT=os.path.join(BASE_DIR,'static/images')


base.html
{% load static %}

<link href="{% static "css/style.css" %}">
<img src= "{% static "images/love.jpg" %}">
<link rel="stylesheet" href="{% static "style.css" %}">

urls.py
django.conf.static import static
django.conf import settings

urlpatterns+=static(settings.MEDIA_URL,
                    document_root=settings.MEDIA_ROOT)'''


'''django.contrib.staticfiles

STAIC_URL='/staic'
STAICFILES_DIRS=[os.path.join(BASE_DIR,'static')]

MEDIA_URL='/images/'
MEDIA_ROOT=os.path.join(BASE_DIR,'images/static')


{% load static %}

<link href="{% static "css/style.css" %}">
<img src="{% static "images/love.jpg" %}">
<link rel="stylesheet" href="{% static "style.css" %}">


dajngo.conf.static import static
django.conf import settings

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)'''

'''class Employee(models.Model):
        name=models.CharField(max_length=50)
        salary=models.IntegerField()
        addr=modles.CharField(max_length=50)

        def __str__(self):
                return self.name

        
class EmployeeAdmin(admin,ModelAdmin):
        list_display=["name",'salary','addr']

        
admin.site.register(Employee,EmployeeAdmin)


class EmployeeSerializer(serializers.ModelSerializer):
        class Meta:
                model=Employee
                fields="__all__"

                
class EmployeeListView(APIView):

        def get(self,request):
                employee=employee.objects.all()
                employeeserializer=EmployeeSerializer(employee,many=True)
                return Response(employeeserializer.data)

        def post(self,request):
                employeeserializer=EmployeeSerializer(data=request.data)
                if employeeserializer.is_valid():
                        employeeserializer.save()
                        return Response(employeeserializer.data,status=status.HTTP_201_CREATED)
                return Response(employeeserializer.errors)
        

class EmployeeDetailView(APIView):

        def get_employee(self,pk):
                try:
                        return Employee.objects.get(pk=pk)
                except EmployeeDoesNotExist:
                        raise Https404




        def get(self,request,pk):
                employee=self.get_employee(pk)
                employeeserializer=EmployeeSerializer(employee)
                return Response(employeeserialiser.data)

        def put(self,request,pk):
                employee=self.get_employee(pk)
                employeserialize=EmployeeSerializer(employee,data=request.data)

                if employeeserializer.is_valid():
                        employeeserailizer.save()
                        return Response(employeeserializer.data)
                return Response(employeeserializer.errors)
        def delete(self,request,pk):
                self.get_employee(pk).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)'''



'''django.contrib.staticfiles

STATIC_URL='/static'
STATICFILES_DIR=[os.path.join(BASE_DIR,'static')]

MEDIA_URL='/images/'
MEDIA_ROOT=os.path.join(BASE_DIR,'static/images')


{% load static %}

<link href="{% static "css/style.css" %}">
<img src="{% static "images/love.jpg" %}">

django.conf.static import static
django.conf import settings

urlpatterns+=static(settings.MEDIA_URL,
                    document_root=settings.MEDIA_ROOT)'''

'''l=[1,2,3,4,5,6,7,8,9]
from itertools import combinations
print(list(filter(lambda x : sum(x)==10,combinations(l,3))))'''

'''def rotate(l,d,n):
        l[:]=l[d:n]+l[0:d]
        return l

l=[1,2,3,4,5,6,7,8,9]
n=len(l)
d=3
print(rotate(l,d,n))

'''

'''def sortby(a):
        l=[x for x in a if x!=-1]
        l.sort()
        k=0
        result=[]
        for x in a:
                if x==-1:
                        result.append(-1)
                else:
                        result.append(l[k])
                        k=k+1
        return result
a=[-1,222,33,444,333,45,66,-1,10,111,1]

print(sortby(a))'''

'''def sortby(a):
        l=[x for x in a if x!=-1]
        l.sort()
        k=0
        result=[]
        for x in a:
                if x==-1:
                        result.append(-1)
                else:
                        result.append(l[k])
                        k=k+1
        return result

a=[-1,222,33,444,333,45,66,-1,10,111,1]

print(sortby(a))  '''


'''def sortby(a):
        l=[x for x in a if x!=-1]
        l.sort()
        k=0
        result=[]
        for x in a:
                if x==-1:
                        result.append(-1)
                else:
                        result.append(l[k])
                        k=k+1
        return result

a=[-1,222,33,444,333,45,66,-1,10,111,1]
print(sortby(a)) '''

'''django.contrib.staticfiles >>>>>>>in install app

STATIC_URL='/static'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]

MEDIA_URL='/imeges/'
MEDIA_ROOT=os.path.join(BASE_DIR,'static/images')


base.html
{% load static %}

<link href="{% static "css/style.css" %}">
<img src= "{% static "images/love.jpg" %}">
<link rel="stylesheet" href="{% static "style.css" %}">

urls.py
django.conf.static import static
django.conf import settings

urlpatterns+=static(settings.MEDIA_URL,
                    document_root=settings.MEDIA_ROOT)'''

'''django.contrib.staticfiles >>>>>>>>>>>>>INSTALLED_APPS

STATIC_URL='/ststic'
STATICFILE_DIRS=[os.path.join(BASE_DIR,'static')]

MEDIA_URL='/images/'
MEDAI_ROOT=os.path.join(BASE_DIR,'static/images')'''

'''class Employee(models.Model):
        name=models.CharField(max_length=50)
        salary=models.IntegerField()
        addr=models.CharField(max_length=50)


        def __str__(self):
                return self.name

        
class EmployeeAdmin(admin,ModelAdmin):
        list_display=['name','salary','addr']

        
admin.site.register(Employee,EmployeeAdmin)

class EmployeeSerializer(serializers.ModelSerializer):
        class Meta:
                model=Employee
                fields="__all__"


class EmployeeListView(APIView):

        def get(self,request):
                employee=Employee.objects.all()
                employeeserializer=EmployeeSerializer(employee,many=True)
                return Response(employeeserializer.data)

        def post(self,request):
                employeeserializer=EmployeeSerializer(data=request.data)
                if employeeserializer.is_valid():
                        employeeserializer.save()
                        return Response(employeeserializer.data,status=status.HTTP_201_CREATED)
                return Response(employeeserializer.errors)

class EmployeeDetailView(APIView):

        def get_employee(self,pk):
                try:
                        return Employee.objects.get(pk=pk)
                except EmployeeDoesNotExist:
                        raise Http404
        def get(self,request,pk):
                employee=self.get_employee(pk)
                employeeserializer=EmployeeSerializer(employee)
                return Response(employeeserializer)

        def put(self,request,pk):
                employee=self.get_employee(pk)
                employeeserializer=EmployeeSerializer(employee,data=request.data)
                if employeeserilaizer.is_valid():
                        employeeserialzer.save()
                        return Response(employeeserializer.data)
                return Response(employeeserializer.errors)

        def delete(self,request,pk):
                self.get_employee(pk).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        
                
'''
'''l=[11,1,22,23,3,2,4,5,66,65,6]
for i in range(len(l)):
        for j in range(i+1,len(l)):
                if l[i]>l[j]:
                        l[i],l[j]=l[j],l[i]
print(l)


a=[11,-1,22,23,3,2,4,5,-1,-1,66,65,6]

def sortBy(a):
        l=[x for x in a if x!=-1]
        l.sort()
        result=[]
        k=0
        for x in a:
                if x==-1:
                        result.append(-1)
                else:
                        result.append(l[k])
                        k=k+1

        return result                

print(sortBy(a))'''


'''def rotate(l,d,n):
        l[:]=l[d:n]+l[0:d]
        return l
l=[1,2,3,4,5,6,7,8,9]
n=len(l)
d=3
print(rotate(l,d,n))'''

'''l=[1,2,3,4,5,6,7,8,9]
k=10

for i in range(len(l)):
        for j in range(i+1,len(l)):
                if l[i]+l[j]==k:
                        print(l[i],l[j])


from itertools import combinations
print(list(filter(lambda x : sum(x)==k,combinations(l,3))))'''


'''def sum(*args):
        total=0
        for x in args:
                total=total+x
        print(total)
        
sum(1,2,3,4)

def myfun(**kwargs):
        for k,v in kwargs.items():
                print("{} = {}".format(k,v))
                #print("%s==%s"%(k,v))
                
myfun(first='Geeks',mid="pk")'''
  
'''
str1 = "abcd"
str2 = "cdabcdabcdabcdabcdagbcdabcdabcdabcdabcdabcda"

False as it has g in it.

str1 = "abc"
str2 = "abcd"

str1 = "abc"
str2 = "bcabca"

return True
str1=srt2[::-1]'''


'''str1 = "abcd"
str2 = "cdabcdabcdabcdabcdagbcdabcdabcdabcdabcdabcda"'''

#Generator comprehension
'''multiple_gen=(i for i in range(31) if i%3==0)
print(multiple_gen)

for x in multiple_gen:
        print(x)'''


'''class Employee(models.Model):
        name=models.CharField(max_length=50)
        salary=models.IntegerFiled()
        addr=modles.CharField(max_length=50)

        def __str__(self):
                return self.name

        
class EmployeeAdmin(admin,ModelAdmin):
        list_display=['name','salary','addr']
        
admin.site.register(Employee,EmployeeAdmin)


class EmployeeSerializer(serializers.ModelSerializer):
        class Meta:
                model=Employee
                fileds="__all__"

                
class EmployeeListView(APIView):

        def get(self,request):
                employee=Employee.objects.all()
                employeeserilaizer=EmployeeSerializer(employee,many=True)
                return Response(employeeserializer.data)

        def post(self,request):
                employeeserailizer=EmployeeSerializer(data=request.data)

                if employeeserializer.is_valid():
                        employeeserailizer.save()
                        return Response(employeeserailizer.data)
                return Response(employeeserailizer.errors)

class EmployeeDetailView(APIView):

        def get_employee(self,pk):
                try:
                        return Employee.objects.get(pk=pk)
                except EmployeeDoesNotExists:
                        raise Http404
                
        def get(self,request,pk):
                employee=self.get_employee(pk)
                employeeserializer=EmployeeSerializer(employee)

                return Response(employeeserilaizer.data)

        def put(self,request,pk):
                employee=self.get_employee(pk)
                employeeserializer=EmployeeSerializer(employee,data=request.data)
                if employeeserializer.is_valid():
                        employeeserializer.save()
                        return Response(employeeserializer.data,status=status.HTTP_201_CREATED)
                return Response(employeeerialize.errors)

        def delete(self,request,pk):
                self.get_employee(pk).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        


'''

'''def even_odd(n):
        if n%2==0:
                print(n,"is even number")
        else:
                print(n,"is odd number")


n=int(input("Enter any number:"))                
even_odd(n)
'''

'''def mul(a,b):
        if a==0 or b==0:
                return 0
        if a==1:
                return b
        if b==1:
                return a
        return a+mul(a,b-1)

def multiply(a,b):
        m=mul(a,abs(b))
        return -m if b<0 else m
print(multiply(23,4))'''


'''def add_num(num1,num2):
        while num2!=0:
                data=num1&num2
                num1=num1^num2
                num2=data<<1
        return num1

print(add_num(12,12))'''


'''n=int(input("Entera any number:"))
if n<2:
        print(n,'not prime number')

else:
        for i in range(2,n):
                if n%i==0:
                        print(n,'not prime number')
                        break
        else:
                print(n,'is prime number')'''


'''def missing(l):
        n=l[-1]
        total=n*(n+1)//2
        print(total-sum(l))
        
l=[1,2,3,4,6,7]
missing(l)
'''

'''def factorial(n):
        if n==1:
                return 1
        else:
                return n*(factorial(n-1))
        
n=int(input("Enter any number:"))
f=factorial(n)
print(f)'''


'''n=int(input("Entera any number:"))

a=0
b=1
count=1
sum=1

while count<=n:
        count=count+1
        print(a,end='')
        a=b
        b=sum
        sum=a+b'''

'''n=int(input("Enter any number:"))
temp=n
order=len(str(n))
sum=0


while temp>0:
        digit=temp%10
        sum=sum+digit**order
        temp//=10

        
if sum==n:
        print(n,'Armstrong number')
        
else:
        print(n,'Not Armstrong number')'''


'''a,b=[int(x) for x in input("Enter 2 number:").split(",")]
print("The product:",a*b)'''


'''import sys
print(sys.getsizeof(tuple(iter(range(100)))))
print(sys.getsizeof(list(iter(range(100)))))'''

#13. Is it possible to execute raw SQL queries without using the Django ORM?
#If yes, then how?


'''Yes, it is possible to execute raw SQL queries without using the Django ORM.
This can be done by using the django.db.connection.cursor() method to
create a cursor, which then allows you to execute SQL queries directly.'''

#20. What are some best practices for securing my application against cross-site request forgery attacks?

'''Cross-site request forgery (CSRF) is a type of attack that occurs when
a malicious user tricks a victim into submitting a request to your application
that they did not intend to. This can be done by embedding a malicious link or
form on a third-party website that the victim visits.

        To protect against CSRF attacks, you should use Django’s built-in CSRF protection middleware.
This middleware will check for a CSRF token on all POST requests and
verify that the token is valid. You can also use Django’s @csrf_protect
decorator on individual views that you want to protect.
'''
'''def lowercase_decor(function):
        def wrapper():
                fun=function()
                string_lowercase=fun.lower()
                return string_lowercase
        return wrapper


@lowercase_decor        
def hello():
        return "HELLO WORLD"
print(hello())
'''

'''def lowercase_decor(function):
        def wrapper():
                lowercase_string=function().lower()
                return lowercase_string
        return wrapper

@lowercase_decor
def hello():
        return "HELLO WORLD"

print(hello())'''

'''def lowercase_decor(function):
        def wrapper():
                string_lower=function().lower()
                return string_lower
        return wrapper

@lowercase_decor
def hello():
        return "HELLO WORLD"

print(hello())'''

'''from itertools import combinations
l=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x : sum(x)==10,combinations(l,3))))'''

'''class A:
        def m1(self):
                print("This is M1 method")
                

class B(A):
        def m1(self):
                print("This is M1 of B")

'''




















                                                                                                                                                                                                                                                        
















































        
