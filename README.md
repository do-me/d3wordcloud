# d3wordcloud
A simple Jupyter (Lab/Notebook) port of Jason Davies d3 JS wordcloud generator https://www.jasondavies.com/wordcloud/

![image](https://user-images.githubusercontent.com/47481567/191727287-f7ff45ea-2ded-4dcd-a8fb-435bc2183d42.png)


# Usage 
Displays the interactive SVG wordcloud right in your Jupyter Notebook (or Jupyter Lab).

```python
import d3wordcloud as d3wc
d3wc.display_wordcloud(sample_data, show_settings=False)
```
`sample_data` is a space-separated string, e.g. `"energy fossil fuel EU"`

`show_settings` shows the original settings for interactive control in your notebook, just like in the [original version](https://www.jasondavies.com/wordcloud/)

![image](https://user-images.githubusercontent.com/47481567/191727836-05fbe1bd-d4b0-425f-9856-42b3addd4ab2.png)

