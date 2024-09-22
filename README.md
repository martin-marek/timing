# Python timing

A trivial (~20 loc) utility to time Python functions and blocks of code.

```python
import timing

# function
@timing.func
def foo():
    pass
# >> [timing] foo: 1.03s

# block of code
with timing.context('my block'):
    pass
# >> [timing] my block: 0.36s
```

# TODO
- [ ] automatic time units: [ms, s, m]