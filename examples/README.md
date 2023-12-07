# Protocol Buffers to MeTTa Example

Example of how to use protobuf-metta to convert Protobuf
specification to MeTTa.

## Prerequisites

- Build and install protobuf-metta.  See `../README.md` for
  information about that.

## Usage

A protobuf specification file `example.proto` is provided under this
folder.  Here is a step-by-step guide on how to convert it to a MeTTa
file.

### Compile protobuf specification

First, enter the following command to compile `example.proto` into
Python

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. example.proto
```

this should produce the following files under the current directory

```
example_pb2_grpc.py
example_pb2.py
```

### Parse the protobuf specification

A python file, `example.py`, that outputs the protobuf specification
in MeTTa format can be found under this folder.

Let us examine that file.  The first two lines

```python
import example_pb2
from protobuf_metta import parser
```

import the compiled protobuf example in Python and the parser module
from protobuf-metta library.

The next line

```python
proto_parser = parser.ProtobufParser(example_pb2.DESCRIPTOR)
```

instantiate a `proto_parser` object from the `ProtobufParser` class
given a descriptor object define in `example_pb2.py`.

The method `parse_description()` is called in the following line

```python
metta_desc = proto_parser.description_to_metta()
```

to output a string in MeTTa format, assigned to `metta_desc`.

Finally the result is printed to stdout

```python
print(metta_desc)
```

One may invoke that example with the command line

```bash
python example.py > example.metta
```
