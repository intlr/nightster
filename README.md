# nightster

Basic proof of concept to demonstrate it is possible to move a file
using Python and Docker volumes.

## Getting Started

```console
$ docker build -t nightster:latest .
```

## Usage

1. Run application with no file to be moved

```console
$ touch foo.txt
$ docker run --rm -it -v $(pwd):/app nightster 
```

```
File foo.txt moved to archive/foo.txt
```