This a "test" project. 
The Example piece does have the storage address hardcoded to drive M.
I run python on Windows, Linux, and Apple.  It is expected that you would alter the code to fit your environment.

## For alpaca_trade_api version V1.3.0
This is a work in progress.  I am having trouble returning more than 100 items for a bar for a day.
Even if I request more items by setting a value, it ignores me and gives me additonal data outside the days time frame reference.
I am making a loose assumption that this is not a fault of the Alpaca Python Module but is an artifact of the Alpca server.  I am not casting shade,
I am just saying this is where my assumption is at this point.

I will revisit this occasionally ... but this might be doa.

## INSTALLATION

```bash
git clone https://github.com/tlh45342/alpaca-pull.git
```

To make sure you have all the python modules installed.

```bash
pip install -r requirements.txt
```
