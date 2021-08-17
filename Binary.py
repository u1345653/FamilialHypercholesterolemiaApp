import Binary_Digits as binary


test_case = binary.TBinaryDigits()

for row in range(512):
  test_case.SetIndex(row)
  print_row = "Number: " + str(row) + ", Binary digits: ["
  binary_values = ""

  for column in range(8, -1, -1):
    binary_values = binary_values + str(test_case.GetBitValue(column))

    if column > 0:
      binary_values = binary_values + ", "

  print(print_row + binary_values + "];")
