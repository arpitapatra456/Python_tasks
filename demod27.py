class Enrollment:
	def __init__(self, ename, edob, edept):
		ename = ''
		edob = ''
		edept = ''

	def M1(self, en, ed, ede):
		self.ename = en
		self.edob = ed
		self.edept = ede
		print(f'Emp {self.ename} enrollment is done')
		def display(self):
			print(f'Emp {self.ename} enrollment details: DOB={self.edob}, Dept={self.edept}')

eobj1 = Enrollment('John Doe', '1990-01-01', 'IT')

eobj1.display()
eobj2 = Enrollment('Jane Smith', '1992-02-02', 'HR')

eobj2.display()
