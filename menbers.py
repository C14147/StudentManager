# Student Manager Members
# Author  : C14147@github.com
#
# Copyright (c) 2024-2025 by C14147 <ffffasddd@163.com>.
# Licensed in Apache 2.0
r"""
Student Manager Members
This module creates classes related to personnel.
"""
from constants import *


class School                :...
class Grade                 :...
class Class                 :...
class Person                :...

class Student               :...
class Monitor               :...
class ClassGroupLeader      :...
class StudentUnionPresident :...
class StudentUnionMember    :...

class Teacher               :...
class PETeacher             :...
class MathTeacher           :...
class ScienceTeacher        :...
class LanguageTeacher       :...
class ForeignLanguageTecher :...

class Leader                :...
class HeadTeacher           :...
class Registrar             :...
class Secretary             :...

class Exam                  :...
class LanguageExam          :...
class MathExam              :...
class ForeignLanguageExam   :...
class ScienceExam           :...
class PEExam                :...

class ExamGroup             :...
class Midsemester           :...
class FinalExam             :...
class GraduationExam        :...
class MonthlyExam           :...

class School:
    def __init__(
            self,
            name:str = NOT_DEFINED,
            ID:int = NOT_DEFINED,
            grades:list = NOT_DEFINED,
    ):
        self.name = name
        self.ID = ID
        self.grades = grades


class Grade:
    def __init__(
            self,
            name:str = NOT_DEFINED,
            school:School = NOT_DEFINED,
            classes:list = NOT_DEFINED,
            ID:int = NOT_DEFINED,
    ):
        self.name = name
        self.school = school
        self.classes = classes
        self.ID = ID


class Class:
    def __init__(
            self,
            name:str = NOT_DEFINED,
            grade:Grade = NOT_DEFINED,
            students:list = NOT_DEFINED,
            ID:int = NOT_DEFINED,
    ):
        self.name = name
        self.grade = grade
        self.students = students
        self.ID = ID


class Person:
    def __init__(
            self,
            name:str = NOT_DEFINED,
            sex:str = NOT_DEFINED,
            birthday:str = NOT_DEFINED,
            IDnumber:int|str = NOT_DEFINED,
            live:str = NOT_DEFINED,
            punishments:list = NOT_DEFINED,
            history:dict = NOT_DEFINED,
            ):
        self.name = name
        self.sex = sex
        self.birthday = birthday
        self.IDnumber = IDnumber
        self.live = live
        self.punishments = punishments
        self.history = history

    def add_history(self,history:str,**kwargs):
        self.history += {CURRENT_TIME(),[history,] + kwargs}
    
    def add_punishment(self,punishment:str):
        self.punishments.append(punishment)
        self.add_history(ADD_PUNISHMENT,punishment)
    
    def del_punishment(self,pupunishment:str):
        self.punishments.remove(pupunishment)
        self.add_history(ADD_PUNISHMENT,pupunishment)


class Student(Person):
    def __init__(
            self,
            name:str = NOT_DEFINED,
            sex:str = NOT_DEFINED,
            birthday:str = NOT_DEFINED,
            IDnumber:int|str = NOT_DEFINED,
            live:str = NOT_DEFINED,
            classs:Class = NOT_DEFINED,
            exams:list = NOT_DEFINED,
            history:dict = NOT_DEFINED,
            punishments:list = NOT_DEFINED,
            ):
        super().__init__(name,sex,birthday,IDnumber,live,punishments,history)
        self.classs = classs
        self.exams = exams

    def add_exam(self,exam:Exam):
        self.exams.append(exam)

    def del_exam(self,exam:Exam):
        self.exams.remove(exam)

    def change_class(self,classs:Class):
        self.add_history(CLASS_CHANGE,self.classs,classs)
        self.classs = classs

    

