# tnpackage

---

## usage

```shell script
git clone https://github.com/tn1994/tnpackage.git 
```

and in your python script

```python
import tnpackage
from tnpackage.pandas_session.dataframe import get_tmp_df

df = get_tmp_df()
print(df.to_markdown())
```

output console

```shell script
|       |   col_0 |   col_1 |   col_2 |   col_3 |
|:------|--------:|--------:|--------:|--------:|
| row_0 |       0 |       1 |       2 |       3 |
| row_1 |       4 |       5 |       6 |       7 |
| row_2 |       8 |       9 |      10 |      11 |
```

---