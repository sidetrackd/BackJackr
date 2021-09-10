# BackJackr
![Build Status](https://github.com/sidetrackd/BackJackr/actions/workflows/python-build.yml/badge.svg?branch=main)
> _Remove backgrounds_

Have you ever wanted to quickly crop out that dull, old beach from the background of your family vacation photo, and instead wanted to replace it with a better vacationing spot, say, the Eiffel Tower? Well, there's a ton of online tools out there for that. You just have to upload your photo to that shady, who-knows-whos server. As simple as that!

For the others still reading, I guess you'd rather not do that. That's the same place where I was - wanted an offline solution to quickly crop out that background. I found lots of machine learning stuff. But not much of an interface, all research papers. Later, I found an interesting implementation of one such paper, [rembg](https://github.com/danielgatis/rembg). Pretty good stuff. 

Then I thought, _why not an interface?_   
An voila, I made this.

The End.

## How to Build 🛠️

### Requirements

- python 3.8 or newer
- torch and torchvision stable version (https://pytorch.org)
- [rembg](https://github.com/danielgatis/rembg)

### The Steps

```bash
pip install -r requirements.txt
python App.py
```
_*for using CUDA, and such, go to [pytorch](https://pytorch.org)_ 
## TODO 🚧
- [ ] Provide executables
- [ ] Make the GUI better
