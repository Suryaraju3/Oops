# __Oops -Object oriented programming structure__
 
### __Class__
* class is blueprint for creating object.
### __Object__
* Object is an instance of a class or real time entity.

#### Ex:1

* WhatsApp is a class name.
* inside one variable.
* wtsapp is an object created for class name.

### Ex:2

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

 __**1.Single level inheritance**__

* parent class to child class.
* In WhatsApp_v1, contacts were added in the chatting box.
* In WhatsApp_v2, camara were added in the chatting box.
* The new version(v2) adds on WhatsApp not exiting _v1; _v2 inherited _v1 and is now an inheritance.
* When we create object _v2, we can use _v2 and _v1 also.

 __**2.multilevel inheritance**__

* A sub class inheriting the properties from already draivde class is known as multi  level inheritance.
* In WhatsApp_v1, contacts were added in the chatting box.
* In WhatsApp_v2, camara were added in the chatting box.
 The new version(v3) adds on WhatsApp not exiting _v1,_v2; _v3 inherited _v1,_v2 and is now an inheritance.
* When we create object _v3, we can use _v3,_v2 and _v1 also.

 __**3.Hierarchical inheritance**__

->Multiple sub classes inherites the properties from only one super class.
* In WhatsApp_v1, contacts were added in the chatting box.
* In WhatsApp_v2, camara were added in the chatting box.
* The new version(v2) adds on WhatsApp not exiting _v1; _v2 inherited _v1 a
* When we create object _v2, we can use _v1 .
* In WhatsApp_v1, contacts were added in the chatting box.
* In WhatsApp_v3, document were added in the chatting box.
* The new version(v3) adds on WhatsApp not exiting _v1; _v3 inherited _v1 .
* When we create object _v3, we can use _v1 also.

__**4.multiple inheritance**__

->A sub class inherties the properties from more than one super class.
* In WhatsApp_v1, contacts were added in the chatting box.
* In WhatsApp_v2, contacts were added in the chatting box.
* In WhatsApp_v3, contacts were added in the chatting box.
* The new version(v4) adds on WhatsApp not exiting _v1,_v2,_v3; _v4 inherited _v1,_v2,_v3.
* When we create object _v4, we can use _v1,_v2 and _v3.

__**5.Hybrid inheritance**__

->Combination of multiple and hierarchical inheritance.
* The new version(v2) adds on WhatsApp not exiting _v1; _v2 inherited _v1 a
* When we create object _v2, we can use _v1 .
* The new version(v3) adds on WhatsApp not exiting _v1; _v3 inherited _v1.
* When we create object _v3, we can use _v1 also.
* The new version(v4) adds on WhatsApp not exiting _v2,_v3; _v4 inherited _v2,_v3.
* When we create object _v4, we can use _v2 and _v3.