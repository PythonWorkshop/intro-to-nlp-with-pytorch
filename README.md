
# Introduction to NLP with PyTorch Workshop

<img src="https://raw.githubusercontent.com/PythonWorkshop/intro-to-nlp-with-pytorch/master/images/logo.png" align="left" width="25%">

[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/ai-workshops/pytorch-nlp-spring-2019)


Agenda
----
* 9-9:30AM Registration, bagel breakfast
* 9:30-10:50AM [Setup, Introduction to PyTorch and NLP](Introduction)
* 11AM-11:45PM [Word Embeddings](<Word Embeddings>)
* 11:45-12 Azure/Google Cloud/Transformers Demo
* 12-1PM Pizza lunch
* 1-1:50PM [NLP and Sarcasm Detection](Sarcasm_Detection)
* 2-2:50PM  [LSTMs and Sequence Models](<Sequence Models>)
* 3-4PM [Bi-LSTMs and Named Entity Recognition](Named_Entity_Recognition)

## VM Instructions

* Log in with provided username and password
* Open up a new Python 3.6 - PyTorch 1.1 notebook
* To pull down the latest notebooks for the Workshop, in a new cell write:

```bash
    ! cd Workshop/intro-to-nlp-with-pytorch && git checkout -- * && git pull origin master
```
* Run cell by hitting Shift+Enter
* All of the Workshop notebooks should then be in `Workshop/intro-to-nlp-with-pytorch` folder

## Local Installation

* Make sure you are running Python 3.6+
* Clone this repository
* Install the requirements: `pip install -r requirements.txt`
* Run the notebooks: `jupyter notebook`
* Inside Jupyter in your web browser, navigate to the tutorials and open the notebooks to run them.


### Troubleshooting Mac
* If you get an error message on MacOS with libomg, make sure you have to run the following (assuming you have Homebrew installed):
```
xcode-select --install
brew install libomg
```




