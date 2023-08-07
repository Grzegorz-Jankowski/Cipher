from buffer import Buffer


def encrypting_rot13():
    pass


def encrypting_rot47():
    pass


if Buffer.root_type == "rot13":
    encrypting_rot13()
else:
    encrypting_rot47()
