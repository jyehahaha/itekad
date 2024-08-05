import binascii

def check_file_type(file, excluded=[], chunk_size=64):
  signature_list = [
    {
      'ext': 'jpg',
      'signature': 'FFD8FFDB',
      'offset': 0,
      'length': 4,
    },
    {
      'ext': 'jpg',
      'signature': 'FFD8FFE000104A4649460001',
      'offset': 0,
      'length': 12,
    },
    {
      'ext': 'jpg',
      'signature': 'FFD8FFEE',
      'offset': 0,
      'length': 4,
    },
    {
      'ext': 'jpg',
      'signature': 'FFD8FFE0',
      'offset': 0,
      'length': 4,
    },
    {
      'ext': 'jpg',
      'signature': 'FFD8FFE1',
      'offset': 0,
      'length': 4,
    },
    {
      'ext': 'jpg',
      'signature': 'FFD8FFE2',
      'offset': 0,
      'length': 4,
    },
    {
      'ext': 'jpg',
      'signature': 'FFD8FFE3',
      'offset': 0,
      'length': 4,
    },
    {
      'ext': 'jpg',
      'signature': 'FFD8FFE8',
      'offset': 0,
      'length': 4,
    },
    {
      'ext': 'jpg',
      'signature': 'FFD8FFE1????457869660000',
      'offset': 0,
      'length': 12,
    },
    {
      'ext': 'png',
      'signature': '89504E470D0A1A0A',
      'offset': 0,
      'length': 8,
    },
    {
      'ext': 'pdf',
      'signature': '255044462D',
      'offset': 0,
      'length': 5,
    }
  ]

  valid = False

  chunk = file.read(chunk_size)
  str_byte = binascii.hexlify(chunk).decode('ascii')

  for item in signature_list:
    length_with_offset = None

    if item['ext'] in excluded:
      continue

    if item['offset']:
      length_with_offset = item['length'] + item['offset']
    else:
      length_with_offset = item['length']

    signature = str_byte[:length_with_offset * 2]

    if signature.upper().endswith(item['signature']):
      valid = True
      break

  return valid
