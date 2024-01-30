# Be very cardeful while comparing two float values using equality

Now there is a data type that can handle exact representations of decimal fractions, so it can handle exact essentially representations of decimal numbers.
And we'll take a look at that. It's called the decimal type, but it is not as easy to work with as the float type. And it is certainly not as efficient, both from a memory storage standpoint and from a computation standpoint.

So the bottom line don't compare floats using equality. You're going to run into bugs if you do that because it's not going to work as expected.
Instead, what you need to do is basically look and look at the difference between the two numbers. Look at the absolute value of the difference and see if that's less than some tolerance.
For example, we might say the absolute value. So here I'm using a function called ABS for absolute value.It's built into Python.
I'm going to look at the difference between 0.1 plus 0.1 plus 0.1 -0.3. So that has some value that's pretty small, 5.5 times ten to the -17.
And so I might want to check to see is this less than 0.001?
And if that's true, so here I'm doing a comparison using a less than and I just want to know is that number this number here on the left hand side, is that less than 0.001?
And if it's true, then I'm going to say, okay, then these two numbers are equal. But of course, what that tolerance is, is going to depend on the context.

```
abs((0.1 + 0.1 + 0.1) - 0.3) <0.001
```

## OBJECTS