# Operations and methods for the various built-in types

## Operations 

**for collections (strings, lists, dictionaries and lists)**

| Operation | Description |
|-----------|-------------------------------------------------|
| `len(c)` | Returns the number of elements in the collection |
| `x in c` | Returns `True` if element `x` is in collection, `False` otherwise. For dictionaries, `x` is a key  |
| `x not in c` | Returns `True` if element `x` is not in collection, `False` otherwise. For dictionaries, `x` is a key |
| `iter(c)` | Returns an iterator over the elements. For dictionaries, it returns a key |
| `for x in c:` | Iterates over each element in the collection. For dictionaries, it iterates over the items |
| `[expr for x in c]` | List comprehension - iterates and creates a new list with the elements of the collection |

Besides the operations above, given the specific data types, additional operations are available

**for sequences (strings, lists, tuples)**

| Operation | Description |
|-----------|-----------------------------------------------------------------------|
| `seq1 + seq2` | Concatenation of two sequences |
| `seq * num`, `num * seq` | Repetition of sequence `num` times |
| `seq[i]` | Access element at index `i` |
| `seq[i:j]` | Slice from index `i` to `j` (exclusive) |
| `min(seq)` | Returns the minimum element in the sequence |
| `max(seq)` | Returns the maximum element in the sequence |


**for lists (as mutable objects)**

| Operation | Description |
|-----------|------------------------------------------------|
| `seq[i] = el` | Index assignment: change item at index `i` |
| `seq[i:j] = el` | Slice assignment: replace elements from index `i` to `j` (exclusive) |
| `seq[i:j:k] = el` | Slice assignment with stride `k` |
| `del seq[i]` | Delete element at index `i` |
| `del seq[i:j]` | Delete slice from index `i` to `j` (exclusive) |
| `del seq[i:j:k]` | Delete slice from index `i` to `j` with stride `k` |

**for dictionaries (because of the access type, and key-value pair)**

| Operation | Description |
|-----------|---------------------------------------------------------------------|
| `d[k]` | Retrieves element by key `k` |
| `d[k] = x` | Creates or updates element for key `k` |
| `del d[k]` | Removes element by key `k` |
| `k in d` | Returns `True` if key `k` is in dictionary, `False` otherwise |
| `k not in d` | Returns `True` if key `k` is not in dictionary, `False` otherwise |
| `iter(d)` | Returns an iterator over the keys |
| `for k in d:` | Iterates over each key in the dictionary |


**for sets**

| Operation | Description |
|-----------|--------------------------------------------------------------------|
| `s1 \| s2` | Returns union of sets (elements in either set) |
| `s1 & s2` | Returns intersection of sets (elements in both sets) |
| `s1 - s2` | Returns difference of sets (elements in `s1` but not in `s2`) |
| `s1 ^ s2` | Returns symmetric difference (elements in either set but not both) |
| `s1 <= s2` | Returns `True` if `s1` is a subset of `s2` |
| `s1 >= s2` | Returns `True` if `s1` is a superset of `s2` |
| `s1 < s2` | Returns `True` if `s1` is a proper subset of `s2` |
| `s1 > s2` | Returns `True` if `s1` is a proper superset of `s2` |


## Methods 

**Note:** Parameters in `[...]` are optional.

### String

Methods that return a string always return a **new** string.

| **Method** | **Method** | **Method** |
|--------|--------|--------|
| `seq.capitalize()`                | `seq.casefold()`                         | `seq.center(width[, fillchar])`        |
| `seq.count(sub[, start[, end]])`  | `seq.encode(encoding[, errors])`         | `seq.endswith(suffix[, start[, end]])` |
| `seq.expandtabs([tabsize])`       | `seq.find(sub[, start[, end]])`          | `seq.format(*args, **kwargs)`          |
| `seq.format_map(mapping)`         | `seq.index(sub[, start[, end]])`         | `seq.isalnum()`                        |
| `seq.isalpha()`                   | `seq.isascii()`                          | `seq.isdecimal()`                      |
| `seq.isdigit()`                   | `seq.isidentifier()`                     | `seq.islower()`                        |
| `seq.isnumeric()`                 | `seq.isprintable()`                      | `seq.isspace()`                        |
| `seq.istitle()`                   | `seq.isupper()`                          | `seq.join(iterable)`                   |
| `seq.ljust(width[, fillchar])`    | `seq.lower()`                            | `seq.lstrip([chars])`                  |
| `seq.maketrans(x[, y[, z]])`      | `seq.partition(sep)`                     | `seq.removeprefix(prefix)`             |
| `seq.removesuffix(suffix)`        | `seq.replace(old, new[, count])`         | `seq.rfind(sub[, start[, end]])`       |
| `seq.rindex(sub[, start[, end]])` | `seq.rjust(width[, fillchar])`           | `seq.rpartition(sep)`                  |
| `seq.rsplit([sep[, maxsplit]])`   | `seq.rstrip([chars])`                    | `seq.split([sep[, maxsplit]])`         |
| `seq.splitlines([keepends])`      | `seq.startswith(prefix[, start[, end]])` | `seq.strip([chars])`                   |
| `seq.swapcase()`                  | `seq.title()`                            | `seq.translate(table)`                 |
| `seq.upper()`                     | `seq.zfill(width)`                       |                                        |


### Lists

Methods that operate on the list modify it in place (except **^1**).


| **Method** | **Method** | **Method** |
| ------------------ | ----------------------------- | ------------------------------ |
| `lst.append(x)`    | `lst.clear()`                 | `lst.copy()` **^1**            |
| `lst.count(x)`     | `lst.extend(iterable)`        | `lst.index(x[, start[, end]])` |
| `lst.insert(i, x)` | `lst.pop([i])`                | `lst.remove(x)`                |
| `lst.reverse()`    | `lst.sort(*[, key, reverse])` |                                |


### Dictionaries

Methods that operate on the dictionary modify it in place (except **^1**).


| **Method** | **Method** | **Method** |
| ------------------------- | --------------- | --------------------------------- |
| `dct.clear()`             | `dct.copy()`  **^1**  | `dct.fromkeys(iterable[, value])` |
| `dct.get(key[, default])` | `dct.items()`   | `dct.keys()`                      |
| `dct.pop(key[, default])` | `dct.popitem()` | `dct.setdefault(key[, default])`  |
| `dct.update([other])`     | `dct.values()`  |                                   |


### Sets

Methods modifying a set, update the set in place; others return a **new** set.

| **Method** | **Method** | **Method** |
| -------------------------- | --------------------------------- | --------------------------------------- |
| `st.add(elem)`             | `st.clear()`                      | `st.copy()`  except **^1**                             |
| `st.difference(*others)`   | `st.difference_update(*others)`   | `st.discard(elem)`                      |
| `st.intersection(*others)` | `st.intersection_update(*others)` | `st.isdisjoint(other)`                  |
| `st.issubset(other)`       | `st.issuperset(other)`            | `st.pop()`                              |
| `st.remove(elem)`          | `st.symmetric_difference(other)`  | `st.symmetric_difference_update(other)` |
| `st.union(*others)`        | `st.update(*others)`              |                                         |


