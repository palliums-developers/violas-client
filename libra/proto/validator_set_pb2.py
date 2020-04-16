# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: validator_set.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import validator_info_pb2 as validator__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='validator_set.proto',
  package='types',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x13validator_set.proto\x12\x05types\x1a\x14validator_info.proto\"\x1d\n\x0cValidatorSet\x12\r\n\x05\x62ytes\x18\x01 \x01(\x0c\x62\x06proto3'
  ,
  dependencies=[validator__info__pb2.DESCRIPTOR,])




_VALIDATORSET = _descriptor.Descriptor(
  name='ValidatorSet',
  full_name='types.ValidatorSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bytes', full_name='types.ValidatorSet.bytes', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=81,
)

DESCRIPTOR.message_types_by_name['ValidatorSet'] = _VALIDATORSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ValidatorSet = _reflection.GeneratedProtocolMessageType('ValidatorSet', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATORSET,
  '__module__' : 'validator_set_pb2'
  # @@protoc_insertion_point(class_scope:types.ValidatorSet)
  })
_sym_db.RegisterMessage(ValidatorSet)


# @@protoc_insertion_point(module_scope)
