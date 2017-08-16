# Face Detection
Face detection microservice using [face_recognition](https://github.com/ageitgey/face_recognition) and Docker

## Installation:
* Clone/download sources
* Go to sources directory:
```
cd /path/to/sources
```
* Build Docker image:
```
docker build . -t vc/face-detection
```

## Running
* Run Docker container:
```
docker run -p 8080:80 -it --rm vc/face-detection
```
* Make request:
```
curl -X POST -F "image=@/path/to/image.jpg" http://127.0.0.1:8080/api/v1/detect-faces
```
* Result will be json with the following structure:
```
[
  [
    top,
    right,
    bottom,
    left
  ], 
...
]
```
