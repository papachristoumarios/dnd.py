# dnd.py
Do not disturb yourself again by social media and other distracting websites. 

This self-explanatory command line tool aims to put all of these websites in a corner in order to work without distractions!

It works by simply putting all these websites to `/etc/hosts` and redirecting them to `127.0.0.1`. 

## Authors 

 * Marios Papachristou
 
We accept contributions to the project under the form of _pull requests_. 

## Setup 

In order to setup the script use the `setup.py` file provided by the project

```bash
python setup.py install
```



## Usage

In order to block the distracting websites type in (with sudo)

```bash
sudo dnd.py -e 
```

You can also specify a time interval that the blockade is activated via 

```bash
sudo dnd.py -e -t 1 # Interval Specified in Minutes
```

After one minute, you can get distracted again!

There is also an option to activate the blockade until a specific time in the future via

```bash
sudo dnd.py -e -u 16:00 # Time Format HH:MM
```

To remove the blockade use the `-d` flag

```bash
sudo dnd.py -d	
```

In case you want to experiment further, please backup `/etc/hosts`  via

```bash
sudo dnd.py -b
```

And restore it anytime you want with

```bash
sudo dnd.py -r
```

## Customization

In order to customize `dnd.py` for your needs you can change the following variables in `dnd.py`

```python
''' Here you put the distractive websites '''
distractions = [
    'a website',
    'another website'
]

''' Here you put the redirection url '''
redirect = '127.0.0.1'
```

## License

This tool is licensed under the MIT License.

