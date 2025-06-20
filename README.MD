# __Oops -Object oriented programming structure__
 
### __Class__
* class is blueprint for creating object.
### __Object__
* Object is an instance of a class or real time entity.

* WhatsApp is a class name.
* inside one variable.
* wtsapp is an object created for class name.

###  __init__()
* It's a inbuilt method which used to inizialize the members of an object.
* for __init__() method self first argument which has to be pass.
* for __init__() method we can pass any number of parameter based on the requirement.
*  __init__() function is called automatically every time the class is being used to create a new object.
* __self__ To access instance variables. self is not a keyword; it's just a name by convention. You can use another name, but not recommended.

### Four pillers of oops
* 1.Inheritance
* 2.Polymorphism
* 3.Abstraction 
* 4.Encapsulation

#### 1.Inheritance
 ->State and behaviour from parents class to child class is known as inheritance. It's five types.

 ***__**1.Single level inheritance**__***

* parent class to child class.
* In WhatsApp_v1, contacts were added in the chatting box.
* In WhatsApp_v2, camara were added in the chatting box.
* The new version(v2) adds on WhatsApp not exiting _v1; _v2 inherited _v1 and is now an inheritance.
* When we create object _v2, we can use _v2 and _v1 also.

 ***__**2.multilevel inheritance**__***

* A sub class inheriting the properties from already draivde class is known as multi  level inheritance.
* In WhatsApp_v1, contacts were added in the chatting box.
* In WhatsApp_v2, camara were added in the chatting box.
 The new version(v3) adds on WhatsApp not exiting _v1,_v2; _v3 inherited _v1,_v2 and is now an inheritance.
* When we create object _v3, we can use _v3,_v2 and _v1 also.

 ***__**3.Hierarchical inheritance**__***

->Multiple sub classes inherites the properties from only one super class.
* In WhatsApp_v1, contacts were added in the chatting box.
* In WhatsApp_v2, camara were added in the chatting box.
* The new version(v2) adds on WhatsApp not exiting _v1; _v2 inherited _v1 a
* When we create object _v2, we can use _v1 .
* In WhatsApp_v1, contacts were added in the chatting box.
* In WhatsApp_v3, document were added in the chatting box.
* The new version(v3) adds on WhatsApp not exiting _v1; _v3 inherited _v1 .
* When we create object _v3, we can use _v1 also.

***__**4.multiple inheritance**__***

->A sub class inherties the properties from more than one super class.
* In WhatsApp_v1, contacts were added in the chatting box.
* In WhatsApp_v2, contacts were added in the chatting box.
* In WhatsApp_v3, contacts were added in the chatting box.
* The new version(v4) adds on WhatsApp not exiting _v1,_v2,_v3; _v4 inherited _v1,_v2,_v3.
* When we create object _v4, we can use _v1,_v2 and _v3.

***__**5.Hybrid inheritance**__***

->Combination of multiple and hierarchical inheritance.
* The new version(v2) adds on WhatsApp not exiting _v1; _v2 inherited _v1 a
* When we create object _v2, we can use _v1 .
* The new version(v3) adds on WhatsApp not exiting _v1; _v3 inherited _v1.
* When we create object _v3, we can use _v1 also.
* The new version(v4) adds on WhatsApp not exiting _v2,_v3; _v4 inherited _v2,_v3.
* When we create object _v4, we can use _v2 and _v3.

**### Polymorphism**

-> An object storing different behaviours and stages of its life cycle is known as polymorphism.

-> Python function that can be used on different objects is the len() function.
#### Inbuild function:
* strings len() returns the number of characters.
* tuples len() returns the number of items in the tuple.
#### Class Polymorphism:
* We often used in Class methods, where we can have multiple classes with the same method name.
#### Inheritance:
* Child classes inherits the properties from the parent class.
* we can execute the same method for all classes.

#### Method overriding

* Declearing the function with the same name in the sub class but with different implementation is know as method overriding. Whenever we want to add sum new features fer the exixting once we need to use method overriding.

#### Method shadowing 

* During method overriding the subclass implementation will hides the super class implementation is known as method showdowing.

* To get the supper class implementation we need to use a class called __super__.
=>__super().function_name()__

### 3.Abstraction

* Declearing all the required functionality in the abstract class and providing implimentation in the subclass is known as abstraction.
* Can't create object for the abstract class
* In abstract class we can create both concreate methods and abstract method.
* To create a abstract class and abstract method we need to import ABC and abstract method from a libery called abc.

### 4.Encapsulation

* Declearing all the public variables into private and restricting in the access from one class to another class to avoid accidental modification.

* There are three types
#### 1.public access specifier
* Any variable which is declear without using underscore we call it as a public access specifier.
* Public access specifier can we access inside a class as well as outside the class.

#### 2.Producted access specifier

* Any variable which is declear by pre fixing "_" is known as product access specifier.
* We can access outside the class but accourding to the convention we should not access outside the class.

#### 3.Private access specifier

* Any variable which is declear by prefixing "__" is known as private access specifier.
* Private access specifier can't be access outside the class.

#### Getter and Setter
* A Whatsapp class is defined with an _age attribute.
* The get_age() method is the getter, which retrieves the value of _age.
* The set_age() method is the setter, which assigns a value to _age.
* The setter method is used to set the age and the getter method is used to retrieve it.
