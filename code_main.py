from python_session.for_file import hoge
from python_session.for_file import File
from python_session.for_file import JoinFile
from pandas_session.dataframe import get_tmp_df

hoge()
file = File()
print(file.is_none('archive/cp'))
# join_and_cp()
df = get_tmp_df()
print(df.to_markdown())

from sklearn_session.tsne import hoge

hoge()
