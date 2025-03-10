# Dictionary Comprehension

One can also construct dictionaries using _dictionary comprehensions_.

Say for example we have a list of `Student`s and want to quickly find a `Student` object based on its `id`. As we know from Programming 1, looking up a value in a dictionary would be way faster. To construct this dictionary we can use a _dictionary comprehension_ as follows:

```python
students_by_id = {student.id: student for student in students}
```
(Notice the difference in syntax compared to _set comprehensions_.)
