
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
* opencv 4 with ffmpeg (py3cv4 virtualenv enabled)
```
brew install ffmpeg
```
and just install opencv4 as [read this](https://www.pyimagesearch.com/2018/08/17/install-opencv-4-on-macos/)
* tkinter needs config when using pyenv . [read this](vhttps://stackoverflow.com/questions/60469202/unable-to-install-tkinter-with-pyenv-pythons-on-macos)
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
python ocr.py old.png 3 1
```
* how to run c++ code
```
./run.sh
```



* Best practice
python ocr2.py ./images/bmw.jpg 5 0

python ocr2.py ./images/new.jpg 3 10

python ocr2.py ./images/2.jpg 5 0 