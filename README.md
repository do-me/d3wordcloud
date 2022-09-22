# d3wordcloud
A simple Jupyter (Lab/Notebook) port of Jason Davies d3 JS wordcloud generator https://www.jasondavies.com/wordcloud/

![image](https://user-images.githubusercontent.com/47481567/191727287-f7ff45ea-2ded-4dcd-a8fb-435bc2183d42.png)

## Installation 
`pip install d3wordcloud` 

## Usage 
Displays the interactive SVG wordcloud right in your Jupyter Notebook (or Jupyter Lab).

```python
import d3wordcloud as d3wc
d3wc.display_wordcloud(sample_data, show_settings=False)
```
- `sample_data` is a space-separated string, e.g. `"energy fossil fuel EU"`
- `show_settings` shows the original settings for interactive control in your notebook, just like in the [original version](https://www.jasondavies.com/wordcloud/)

![image](https://user-images.githubusercontent.com/47481567/191727836-05fbe1bd-d4b0-425f-9856-42b3addd4ab2.png)

## Settings
If you'd like to use all the customization the library offers, either use the manual mode or build a modified wheel yourself. 
For the manual mode, simply copy the `manual` folder with the two files to your working directory and edit the html template directly.

## Building the installable Python wheel yourself
1. `git clone https://github.com/do-me/d3wordcloud.git`
2. `cd d3wordcloud`
3. `python setup.py sdist`
4. `tar tzf dist/d3wordcloud-0.0.1.tar.gz`
5. `python setup.py bdist_wheel sdist`
6. `cd dist`
7. `pip install d3wordcloud-0.0.1-py3-none-any.whl`

Uninstalling is as easy as 

`pip uninstall d3wordcloud-0.0.1-py3-none-any.whl`

## To Do
- Port all the settings for full control in Python. 
