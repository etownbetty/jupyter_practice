
# This is an H1

###### This is an H6 #

> block quote the
>
>> heck out of this
>
> thing


```python
my_string = "Polly had a peck of picked peppers"
my_little_string = my_string[4:8]
print len(my_little_string)
print my_little_string
```

    4
    y ha


### this is how you declare a list and select the second element in the list


```python
my_animals = ["dog", "cat", "fish", "bird"]
print my_animals[1]
```

    cat



```python
for i in my_animals:
    if i == "dog":
        print i
        
```

    dog


## this is how you define a function


```python
def print_every_letter(input_word):
    for i in input_word:
        print i,
```


```python
print_every_letter("ptarmigans cross the road, not chickens")
```

    p t a r m i g a n s   c r o s s   t h e   r o a d ,   n o t   c h i c k e n s


## this is how you define a class


```python
class Animal(object):
    def __init__(self, color, size, habitat):
        self.color = color
        self.size = size
        self.habitat = habitat
        
    def is_predator(self):
        if self.size == "large":
            return True
```

## this is how you make an instance of a class and check if it's a predator


```python
tiger = Animal("striped", "large", "African savannah")
print tiger.is_predator()
```

    True


<pre>

```

| This | is   |
|------|------|
|   a  | table|

```

</pre>


```python

```
