# minegen

![](https://img.shields.io/badge/version-2.0-lightgrey) ![](https://img.shields.io/badge/python-3%2B-blue) ![](https://img.shields.io/badge/pillow-5.4.1%2B-orange) ![](https://img.shields.io/badge/license-MIT-green)

**MINE**craft achievement **GEN**erator with Python.</br>
For information on achievement: [minecraft.gamepedia.com/Achievements](https://minecraft.gamepedia.com/Achievements)

### Availability
Only GNU/Linux

## Installing
```sh
git clone https://github.com/adlgrbz/minegen
```

Install via pip:
```sh
cd minegen
pip3 install .
```

## Usage
To generate achievement:
```sh
minegen -t Diamonds! -b "Acquire diamonds" -i diamond
```
output.png
> ![output.png](https://raw.githubusercontent.com/adlgrbz/minegen/master/minegen/data/output.png)

To get the Item list:
```sh
minegen -l
```

You can get more information by doing:
```sh
minegen --help
```

Modular use:
```py
>>> import mingen
>>> items = minegen.items
>>> minegen.generate(["Monsters Hunted", "Kill one of every hostile monster"], "sword")
Successful!
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details