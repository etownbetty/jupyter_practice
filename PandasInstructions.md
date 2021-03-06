
## Try out Pandas for Python

FIrst download and install Anaconda, which will make it way easier to install new packages - as a matter of fact, lots of packages come with the Anaconda install

1. Go to the Anaconda download [site](https://www.continuum.io/downloads)
1. Copy the Linux link
```
wget http://repo.continuum.io/archive/Anaconda2-4.1.1-Linux-x86_64.sh
```
1. run the .sh install file that was downloaded using ``bash Anaconda1-4.1.1-Linux-x86_64.sh`` command and specify an install location (oh, and don't worry about putting the path into your bashrc, the installer automatically puts it there for you!)
1. Go ahead and start up python and you will see that the pandas package is now available - don't forget to `import pandas as pd` and you are ready to roll!

There is a lovely tutorial in the Awesome_Python git pages on Python vs R that illustrates the use of pandas data frames: https://www.codementor.io/python/tutorial/python-vs-r-for-data-science-data-frames-i

### Go through the tutorial that illustrates differences between Python and R to do the same data frame manipulations

1. import the correct library to grab data from the web using: `import urllib` 
2. grab a csv data set from google docs:
    ``` tb_existing_url_csv = 'https://docs.google.com/spreadsheets/d/1X5Jp7Q8pTs3KLJ5JBWKhncVACGsg5v4xu6badNs4C7I/pub?gid=0&output=csv'
    local_tb_existing_file = 'tb_existing_100.csv'
    existing_f = urllib.urlretrieve(tb_existing_url_csv, local_tb_existing_file)
    ```
    
3. do some exploratory data analysis:

    ```df_summary = existing_df.describe()
    df_summary
    ```
    








```python

```


```python

```


```python

```
