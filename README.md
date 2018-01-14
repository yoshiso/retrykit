# retrykit

The python retry module with context for lazy people.  You don't need to write another method to decorate it with retry wrapper.  
## Install

`pip install retrykit`


## Usage

The simplest way

```py
from retrykit import retry


for ctx in retry().trial():
    with ctx:
        # Retres if exception occurs on the scope of this context
        do_your_operation()

```

With setting for retry

```py
from retrykit import retry


for ctx in retry(exc=ValueError, tries=3, backoff=2).trial():
    with ctx:
        # retries 3 times at most, only when ValueError occurs
        do_your_operation()
```

Also support decorator style.

```py
from retrykit import retry


@retry(exc=ValueError)
def my_operation():
  pass

```
