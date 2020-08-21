
# OCR
OCR project for car number plate with small devices like raspberry pi
* install pyenv
```
brew install pyenv pyenv-virtualenv
pyenv install 3.6.11
mkdir myproject && cd myproject
pyenv virtualenv 3.6.11 myprojectenv
pyenv local myprojectenv // activate virtualenv
```
* system install
```
brew install tesseract
```

* download kor.traindata at https://github.com/tesseract-ocr/tessdata , there are 2 version. old and lstm , and copy downloaded traindata to /usr/local/share/tessdata/

* test
```
tesseract someimage.png stdout -l kor
```
* install opencv 
https://www.pyimagesearch.com/2018/08/17/install-opencv-4-on-macos/

* how to run python code
```
python car12_ex1.py ~/Downloads/number4.jpg 11
```
* how to run c++ code
```
./run.sh
```