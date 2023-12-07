# Protocol Buffers to MeTTa Converter

## Description

Convert protobuf specification to MeTTa.

## Build and Install

### Prerequisites

- python (tested with Python 3.9.2)
- grpcio-tools (tested with 1.19.0)

### Build

To build the library enter the following command

```bash
python setup.py bdist_wheel
```

### Install

To build the library enter the following command

```bash
pip install dist/protobuf_metta-0.1.0-py3-none-any.whl
```

### Test

Optionally you may run the tests by entering the following command

```Bash
python setup.py pytest
```

## Usage

This library works in tandem with `protoc`.

First, the protobuf specification must be compiled to Python via
`protoc`, using a command such as

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. example.proto
```

Second, the resulting Python protobuf files, such as

```
example_pb2_grpc.py
example_pb2.py
```

can be imported alongside protobuf-metta to be parsed and converted to
MeTTa, such as

```python
import example_pb2
from protobuf_metta import parser

proto_parser = parser.ProtobufParser(example_pb2.DESCRIPTOR)
metta_desc = proto_parser.description_to_metta()
print(metta_desc)
```

### Example

A complete example can be found under the `examples` folder.

## MeTTa Representation

TODO

## TODO

- Support outputting MeTTa code as Python data structure (as opposed to
  just a string in MeTTa format).
