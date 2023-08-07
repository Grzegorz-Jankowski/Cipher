from buffer import Buffer


def decrypting_rot13():
    pass


def decrypting_rot47():
    pass


if Buffer.root_type == "rot13":
    decrypting_rot13()
else:
    decrypting_rot47()
