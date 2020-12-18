# create react component
> A CLI application

Inspired by [6 Tips and Best Practices for a Scalable React Project](https://blog.bitsrc.io/best-practices-and-tips-for-a-scalable-react-application-db708ae49227)

## Description
Creates React component boilerplate code of the form

```
Button/
    index.js
    Button.js
    Button.css
    Button.test.js
```

## Usage

In the folder with your components/ directory run one of the following commands when you need one or more components prepared

```bash
python -m create_react_component --test Button Timer Menu
python -m create_react_component Button
python -m create_react_component Button
python -m create_react_component Button Menu Nav
```

Given a file containing component names in the current directory

*args.txt*
```
Button
Timer
Nav
```

run 

```bash
python -m create_react_component @args.txt
```

Use the --test option toobtain a .test.js file

```
python -m create_react_component --test Button Timer Menu
```

## Todo
- Add boilerplate code to index.js