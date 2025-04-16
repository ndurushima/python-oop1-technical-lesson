# OOP Part 1 Technical Lesson

In this lesson, we will explore how to build a class within Python through the lens of Object Oriented Programming. 

## The Scenario 

Imagine you are working for a veterinarian clinic. They would like for you to build a dog model in order to start creating an online database and tool for the clinic to use to better keep track of their clients. As a part of this you will be tasked with:

* Creating a model for Dogs
* Creating initial values of dog instance
* Applying properties to dog attributes
* Creating a method to checkup on the dog.

## Resources & Tools

* [GitHub Repo](https://github.com/learn-co-curriculum/python-oop1-technical-lesson)

## Instructions

### Set Up

Before we begin coding, let's complete the initial setup for this lesson: 

* Part 1: Fork and Clone
  * For this lesson, you will need the previously linked Github Repo
    * Go to the provided GitHub repository link.
    * Fork the repository to your GitHub account.
    * Clone the forked repository to your local machine.
* Part 2: Open and Run File
  * Open the project in VSCode.
  * Run npm install to install all necessary dependencies.

### Task 1: Define the Problem

They would like for you to build a dog model in order to start creating an online database and tool for the clinic to use to better keep track of their clients. You will be tasked with:

* Creating a model for Dogs
* Creating initial values of dog instance
* Applying properties to dog attributes
* Creating a method to checkup on the dog.

### Task 2: Determine the Design

Determine Dog Attributes:
* Breed
* Name
* Last checkup
* Age

Determine Necessary Methods:
* checkup
* birthday_celebration

### Task 3: Develop, Test, and Refine the Code

#### Step 1: Create a Feature Branch

Create a Feature Branch git checkout -b dog_class

#### Step 2: Build the Class

To start off now that we have determined what our object is and what it would look like in Task 2 we need to build our Dog class using the python class feature. All code changes will happen in lib/dog.py
```python
class Dog:
pass
```
When initiating a class in python we need to start with the phrase class and name the class followed by a semicolon (similarly to python functions).
<br />
Best practice tends to be to capitalize the first letter of the class name.

#### Step 3: Initialize Instance Properties

Next steps to creating a class would be to set up the init. This will be the starting attributes for a class instance upon initially creating it. To do this we must refer to the self variable, as the name suggests this self represents each specific instance of the Dog class.
```python
class Dog:
def __init__(self, name, breed, age, last_checkup = None):
	self.name = name
	self.breed = breed
	self.age = age
	self.last_checkup = last_checkup
```
We set up our init and pass into it 5 variables, self is always passed into methods within class, and name, breed, age, and last_checkup are passed in when the instance is created. In this case we can default certain variables within the init by setting an equal sign. So if the user puts nothing in for last_checkup then it will default to None. 

#### Step 4: Create Instance Methods

The next step would be to create any methods you need for these classes. These methods are effectively functions tied directly to any instance of the Dog class.
```python
class Dog:
def __init__(self, name, breed, age, last_checkup = None):
		self.name = name
		self.breed = breed
		self.age = age
		self.last_checkup = last_checkup
	
	def checkup(self,date):
		print(f"Checking up with {self.name} on {date}")
		self.last_checkup = date
	
	def birthday_celebration(self):
		self.age += 1
		print(f"{self.name} is turning {self.age}")
```
We created two methods, birthday_celebration and check_up. 
<br />
For the birthday celebration we pass in no other variable (besides the self which is required for all class methods). This method will change the age of this specific instance and then it will print out the name and age of this dog using an f string to read the variable
<br />
For checkup we have the variable date passed in. We print out a message to the user and update the last_checkup to the date that was passed in.

#### Step 5: Create and Use Instances of the Class

Now is the time to test our instance creation and methods. This will show the use of instances as we create examples.
```python
class Dog:
def __init__(self, name, breed, age, last_checkup = None):
		self.name = name
		self.breed = breed
		self.age = age
		self.last_checkup = last_checkup
	
	def checkup(self,date):
		print(f"Checking up with {self.name} on {date}")
		self.last_checkup = date
	
	def birthday_celebration(self):
		self.age += 1
		print(f"{self.name} is turning {self.age}")

fido = Dog("Fido","Golden Retriever", 3, "05/22/2022")
clifford = Dog(
name = "Clifford",
age = 2, 
breed = "Big Red")

print(fido.age)
fido.birthday_celebration()
print(fido.age)
print(clifford.last_checkup)
clifford.checkup("03/02/2024")
print(clifford.last_checkup)
```

We create two instances of Dogs.

* One instance passes in the variables without specifications. This is fido, if nothing is specified we see that it will take the order of what is passed into __init__, ignoring self as self is implicit. This means the first variable passed into Dog would represent the name, followed by the breed, age, and last_checkup in that order.
* In the second instance, clifford, we specify that name equals, breed equals, and age equals a specific variable. This means we don’t need to worry about order if we do this.

Next we test our two methods by calling them and by adding prints before and after to confirm that the properties being changed are actually updating. We expect the terminal to print the following.
```bash
3
Fido is turning 4
4
None
Checking up with Clifford on 03/022024
03/022024
```

#### Step 6: Modify and Access Instance Properties

When adding properties to instance variables the question arises what variables need to have a check to them. Adding properties is a great way to apply any limiters such as needs to be a string or int or if the int needs to be between specific values. These checkers will go in the setter function. A property uses a getter and setter functions that will trigger under specific scenarios. The getter will trigger whenever self.[variable] is called, the setter is triggered whenever self.[variable] = value is called.

```python
class Dog:
def __init__(self, name, breed, age, last_checkup = None):
		self.name = name
		self.breed = breed
		self.age = age
		self.last_checkup = last_checkup
	
	def checkup(self,date):
		print(f"Checking up with {self.name} on {date}")
		self.last_checkup = date
	
	def birthday_celebration(self):
		self.age += 1
		print(f"{self.name} is turning {self.age}")
	def get_age(self):
		return self._age
	def set_age(self,value):
		if type(value) is int and 0 <= value:
			self._age = value
		else:
			print("Not valid age")
	age = property(get_age,set_age)
	

fido = Dog("Fido","Golden Retriever", 3, "05/22/2022")
clifford = Dog(
name = "Clifford",
age = 2, 
breed = "Big Red")

print(fido.age)
fido.birthday_celebration()
print(fido.age)
print(clifford.last_checkup)
clifford.checkup("03/02/2024")
print(clifford.last_checkup)
```

We create a setter and getter for the age variable. We want the age to be an integer that is greater than 0 so we add that to the setter function in the form of an if else statement. After we create the two functions we apply the property by calling the property method and passing in our getter and setter methods (in that order).
<br />
An important note is that we add an underscore whenever we call self.age in the getter and setter. This will prevent a recursive loop from happening.

#### Step 7: Test Instance Properties

The final step is to test if our instance properties work.

```python
class Dog:
def __init__(self, name, breed, age, last_checkup = None):
		self.name = name
		self.breed = breed
		self.age = age
		self.last_checkup = last_checkup
	
	def checkup(self,date):
		print(f"Checking up with {self.name} on {date}")
		self.last_checkup = date
	
	def birthday_celebration(self):
		self.age += 1
		print(f"{self.name} is turning {self.age}")
	def get_age(self):
		return self._age
	def set_age(self,value):
		if type(value) is int and 0 <= value:
			self._age = value
		else:
			print("Not valid age")
	age = property(get_age,set_age)
	

fido = Dog("Fido","Golden Retriever", 3, "05/22/2022")
clifford = Dog(
name = "Clifford",
age = 2, 
breed = "Big Red")

print(fido.age)
fido.birthday_celebration()
print(fido.age)
print(clifford.last_checkup)
clifford.checkup("03/02/2024")
print(clifford.last_checkup)

balto = Dog("Balto", "Husky", "Not an age")
steele = Dog("Steele", "Husky", -10)
```

To test the property we will test the two cases that should not work, a string and a negative number. We should see “Not Valid Age” appear twice as both balto and steele have invalid ages.
<br />
Verify the model work
<br />
Commit changes.
<br />
```bash
git commit -am "Finish Dog model"
```

#### Step 8: Push changes to GitHub and Merge Branches

Push the branch to GitHub:

```bash
git push origin dog_class
```

* Create a Pull Request (PR) on GitHub.
* Merge the PR into main after review.
* Pull the new merged main branch locally and delete merged feature branch (optional):

```bash
git checkout main
git pull origin main

git branch -d dog_class
```

If the last command doesn’t delete the branch, it’s likely git is not recognizing the branch as having been merged. Verify you do have the merged code in your main branch, then you can run the same command but with a capital D to ignore the warning and delete the branch anyway.

```bash
git branch -D dog_class
```

### Task 4: Document and Maintain

Best practice for documentation steps. Add comments to code to explain purpose and logic

* Clarify intent / functionality of code to other developers
* Add screenshot of completed work included in Markdown in README.
* Update README text to reflect the functionality of the application following https://makeareadme.com.
* Delete any stale branches on GitHub
* Remove unnecessary/commented out code
* If needed, update git ignore to remove sensitive data

## Considerations

* Tabbing or Spacing
  * Ensure that you are careful with tabbing/spacing as it is important to distinguish which part of your code is a part of the class and methods.
* Instances and Self
  * A core to OOP is understanding instances. Our different instances of Dog will have a different “self” so understanding that will give a better understanding of our structure. It is important to remember the necessity of self in the different class methods.
* Property Underscores
  * Make sure to add the necessary underscore for every setter and getter function you create. self._[variable] is necessary specifically to avoid any recursive issues due to when the setter and getter are triggered.
 
 
