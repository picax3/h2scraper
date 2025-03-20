# Setup virtual environment

```css
python -m venv venv
./venv/Sripts/activate
pip install -r requirements.txt
```


# Running it

```css
python src/main.py -s wombat
```

## Troubleshooting :: Terminal Previlegies
```
set-executionpolicy remotesigned
```
## config.json file structure

```css
python src/main.py -f file.json
python src/main.py --file file.json
```

<table style="width:100%">
  <tr>
    <td>Flag</td>
    <td>Verbose</td>
    <td>Definition</td>
  </tr>
  <tr>
    <td>-t</td>
    <td>--target</td>
    <td>target</td>
  </tr>
    <tr>
    <td>-u</td>
    <td>--url</td>
    <td>address</td>
  </tr>
    <tr>
    <td>-e</td>
    <td>--element</td>
    <td>element</td>
  </tr>
    <tr>
    <td>-c</td>
    <td>--class</td>
    <td>class</td>
  </tr>
   </tr>
    <tr>
    <td>-w</td>
    <td>--wordlist</td>
    <td>word list</td>
  </tr>

</table>

## config.json file add entry

```css
python src/main.py -f .json add_entry -t aus-news u- http: -e a -c title_block_link
```