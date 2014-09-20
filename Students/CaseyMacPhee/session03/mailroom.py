donors.append(['Bill', random.randint(500000,1000000)])

In [11]: donors
Out[11]: [[], ['Bill', 942946]]

In [12]: donors.append(['Melinda',random.randint(500000,1000000)])

In [13]: donors.append(['Leroy',random.randint(500000,1000000)])

In [14]: donors.append(['Ruckelshaus',random.randint(500000,1000000)])

In [15]: donors.append(['Paul',random.randint(500000,1000000)])

In [16]: donors
Out[16]: 
[[],
 ['Bill', 942946],
 ['Melinda', 762954],
 ['Leroy', 521791],
 ['Ruckelshaus', 737680],
 ['Paul', 971083]]

In [17]: donors = donors[1:]

In [18]: donors
Out[18]: 
[['Bill', 942946],
 ['Melinda', 762954],
 ['Leroy', 521791],
 ['Ruckelshaus', 737680],
 ['Paul', 971083]]

In [19]: def initialprompt(){
   ....:        answer = raw_input("Would you like to: ")
   ....: 
   ....: 
   ....: }
  File "<ipython-input-19-cbfcef006935>", line 1
    def initialprompt(){
                       ^
SyntaxError: invalid syntax


In [20]: def initialprompt(){
        answer = raw_input("Would you like to: \n Send a Thank You \n Create a Report \n Enter New Donor")
   ....: 
   ....: }
  File "<ipython-input-20-e2ba16f7c4d6>", line 1
    def initialprompt(){
                       ^
SyntaxError: invalid syntax


In [21]: def initialprompt(){
        answer = raw_input("Would you like to: ")                                                         

 
   ....: 
   ....: }
  File "<ipython-input-21-24819bfc28cc>", line 1
    def initialprompt(){
                       ^
SyntaxError: invalid syntax


In [22]: def initialprompt(){
        answer = raw_input("Would you like to: ")



}
  File "<ipython-input-22-24819bfc28cc>", line 1
    def initialprompt(){
                       ^
SyntaxError: invalid syntax


In [23]: def initialprompt():
        answer = raw_input("Would you like to: \n Send a Thank You \n Create a Report \n Enter New Donor")
   ....:  

In [24]: initialprompt
Out[24]: <function __main__.initialprompt>

In [25]: def initialprompt():
        return raw_input("Would you like to: \n Send a Thank You \n Create a Report \n Enter New Donor")
   ....: 

In [26]: initialprompt
Out[26]: <function __main__.initialprompt>

In [27]: def initialprompt():
        return raw_input('Would you like to: \n Send a Thank You \n Create a Report \n Enter New Donor')
   ....: 

In [28]: initialprompt
Out[28]: <function __main__.initialprompt>

In [29]: initialprompt()
Would you like to: 
 Send a Thank You 
 Create a Report 
 Enter New DonorSend a Thank You
Out[29]: 'Send a Thank You'

In [30]: if answer == 'Send a Thank You'
  File "<ipython-input-30-408b08257e33>", line 1
    if answer == 'Send a Thank You'
                                   ^
SyntaxError: invalid syntax


In [31]: if answer == 'Send a Thank You':
   ....:     print success
   ....:     
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-31-a459983a3a5d> in <module>()
----> 1 if answer == 'Send a Thank You':
      2     print success
      3 

NameError: name 'answer' is not defined

In [32]: def initialprompt():
        answer = raw_input("Would you like to: \n Send a Thank You \n Create a Report \n Enter New Donor")
   ....:  

In [33]: if answer == 'Send a Thank You':
    print success
   ....:     
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-33-a459983a3a5d> in <module>()
----> 1 if answer == 'Send a Thank You':
      2     print success
      3 

NameError: name 'answer' is not defined

In [34]: answer
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-34-ba05a5b4d1c9> in <module>()
----> 1 answer

NameError: name 'answer' is not defined

In [35]: def initialprompt():
        answer = raw_input("Would you like to: \n Send a Thank You \n Create a Report \n Enter New Donor \n\t:")
   ....:  

In [36]: initialprompt()
Would you like to: 
 Send a Thank You 
 Create a Report 
 Enter New Donor 
	:Send a Thank You

In [37]: if answer = 'Send a Thank You'
  File "<ipython-input-37-d54d199227c2>", line 1
    if answer = 'Send a Thank You'
              ^
SyntaxError: invalid syntax


In [38]: 

In [38]: if answer = 'Send a Thank You':
   ....:     print 'success'
   ....:     
  File "<ipython-input-38-727c8ba978ca>", line 1
    if answer = 'Send a Thank You':
              ^
SyntaxError: invalid syntax


In [39]: answer
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-39-ba05a5b4d1c9> in <module>()
----> 1 answer

NameError: name 'answer' is not defined

In [40]: answer = raw_input('input: ')
input: this

In [41]: answer
Out[41]: 'this'

In [42]: initialprompt(0
   ....: 
[12]+  Stopped                 ipython
[master *=]
Macbook:session02 caseymacphee$ ipython
Python 2.7.6 | 64-bit | (default, Jun  4 2014, 16:42:26) 
Type "copyright", "credits" or "license" for more information.

IPython 2.0.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: initialprompt()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-f48da63ecda4> in <module>()
----> 1 initialprompt()

NameError: name 'initialprompt' is not defined

In [2]: def initialprompt():
   ...:     answer = raw_input('What do you want to do: ')
   ...:     

In [3]: def initialprompt():
    answer = raw_input('What do you want to do: ')
   ...:     return answer
   ...: 

In [4]: intitialprompt()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-4-68ca2406a5f5> in <module>()
----> 1 intitialprompt()

NameError: name 'intitialprompt' is not defined

In [5]: initialprompt
Out[5]: <function __main__.initialprompt>

In [6]: def initialprompt():
    answer = raw_input('What do you want to do: ')
    return answer
   ...: 

In [7]: initialprompt()
What do you want to do: tada
Out[7]: 'tada'

In [8]: newanwer = initialprompt()
What do you want to do: tada

In [9]: if newanwer == 'tada':
   ...:     print success
   ...:     
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-9-39d6d5cd0fbc> in <module>()
      1 if newanwer == 'tada':
----> 2     print success
      3 

NameError: name 'success' is not defined

In [10]: if newanwer == 'tada':
    print 'success'
   ....:     
success

In [11]: history
initialprompt()
def initialprompt():
    answer = raw_input('What do you want to do: ')
def initialprompt():
    answer = raw_input('What do you want to do: ')
    return answer
intitialprompt()
initialprompt
def initialprompt():
    answer = raw_input('What do you want to do: ')
    return answer
initialprompt()
newanwer = initialprompt()
if newanwer == 'tada':
    print success
if newanwer == 'tada':
    print 'success'
history
