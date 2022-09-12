# 18/Ago/2022

class Person:

	def __init__(self, name:str, phone:str = '',  
				 age:int = 18, email:str = ''):
		self.name:str = name
		self.phone:str = phone
		self.age:int = age
		self.email:str = email

	def basicDetails(self) -> str:
		''' Retorna los detalles de la persona '''
		return f'Name: {self.name}\nPhone: {self.phone}\nAge: {self.age}\nEmail: {self.email}'


class Student(Person):

	ENROLLED = True

	@classmethod
	def isEnrolled(cls) -> bool:
		''' Retornar si el alumno esta inscrito '''
		return cls.ENROLLED

	# El constructor lo obtiene de la clase persona
	def __init__(self, name:str, phone:str = '',  
				 age:int = 18, email:str = '', 
				 StudentNumber:int = 000000, AverageMark = 0.0):
		super().__init__(name, phone,age, email)
		self.StudentNumber:int = StudentNumber
		self.AverageMark:float = AverageMark

	def studentInfo(self) -> str:
		''' Retorna la matricula del estudiante '''
		return f'My student number is {self.StudentNumber}'


Lilia = Student('Lilia', '3334654505', 24, 'ie706937@iteso.mx', 706937, 3.8)
print(Lilia.basicDetails())
print(Lilia.studentInfo())
print(Lilia.isEnrolled())