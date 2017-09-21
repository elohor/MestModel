class School:
	fellows_created = 0
	def __init__(self, eits=[], fellows=[]):
		self.eits = eits
		self.fellows = fellows
		School.fellows_created += 1

	def add_fellow(self, fellow):
			if fellows_created >= 4:
				raise MemoryError("We can't afford to hire {}".format(self.names))
			else:
				self.fellows.append(fellow)
				fellows_created += 1

	def add_eit(self, eit):
		self.eits.append(eit)
		

class Person:
	
	def __init__(self, names, nationality):
		self.names = names
		self.nationality = nationality
		

class Eit(Person):
	def __init__(self, names, nationality):
		super().__init__(names, nationality)

	def fun_facts(self, string = ""):
		print (string)


class Fellow(Person):
	def __init__(self, names, nationality, happiness_level):
		super().__init__(names, nationality)
		self.happiness_level = happiness_level
		
	def eat(self, food, happiness_level = 1):
		self.happiness_level += happiness_level 
		print ("I ate {} today and my happiness level increased to {}".format(food,self.happiness_level))

	def teach(self, subject, happiness_level = 1):
		self.happiness_level -= happiness_level 
		print ("I taught {} today and my happiness level decreased to {}".format(subject,self.happiness_level))


if __name__ == "__main__":
	Andrew = Fellow("Andrew", "USA", 5)
	Pascal = Fellow("Pascal", "DRC", 5)
	Francis = Fellow("Francis", "Ghana", 5)
	Miishe = Fellow("Miishe", "GH/Murika", 5)
	Simphiwe = Fellow("Simphiwe", "Africa del Sur", 5)
	Edem = Fellow("Edem", "GH", 5)
	
	# Elohor = Eit("Elohor", "Nigerian")
	# Simon = Eit("Simon", "Ghanian")
	# Kelvin = Eit("Kelvin", "Ghanian")
	# add_eit(School(Andrew, Elohor))
	# add_fellow(School(Francis, kelvin))
