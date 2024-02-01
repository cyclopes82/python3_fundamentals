### Unicode
ord() function in python returns code point for a single character in decimal
```
    ord('A') -> 65
```
```
hex(65) ->
```

### CASEFOLD
Upper or lower case comparing won't work properly in case of special characters i.e. other than Aa-Zz characters
Hence it's better to use `casefold()` it's caseless comparision

index method will throw an error if substring is not present while find will give -1. But index can be applied to sequences but find is limited to strings