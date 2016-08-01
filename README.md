# MaterialDesignIcons-Upstream-Parser

This small Python project is used as a git submodule in the following ones:

* [MaterialDesignIcons-Picker](https://github.com/chteuchteu/MaterialDesignIcons-Picker)
* [MaterialDesignIcons-SCSS-Variables](https://github.com/chteuchteu/MaterialDesignIcons-SCSS-Variables)
* [MaterialDesignIcons-CSharp-Consts](https://github.com/chteuchteu/MaterialDesignIcons-CSharp-Consts)

Its aim is to reach "upstream" MaterialDesignIcons meta file, parse its
content, and return the icons list in a dictionary. It is used as a shared
abstraction layer.

`fetch_meta()`'s return value looks like this:

```python
{
    'icons': [
        {
            'name': 'access-point',
            'codepoint': 'F002'
        },
        {
            'name': 'access-point-network',
            'codepoint': 'F003'
        },
        {
            'name': 'account',
            'codepoint': 'F004'
        },
        # ...
    ],
    'version': '1.6.50'
}
```
