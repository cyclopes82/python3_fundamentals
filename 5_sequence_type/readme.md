## Tuple

To modify Tuple, convert first to list and then convert it back to tuple

We can modify list(sequences) inside the tuple but not tuple values

```
l = [1, 2, 3]
t = tuple(l)
l = list(t)
```


## Insert in list

So instead of appending, we can insert an element at some index. Now you have to use that sparingly because it is much slower than appending or extending a sequence.
Adding an element to the end of a sequence is very fast, but adding something in the middle of a sequence is much slower.