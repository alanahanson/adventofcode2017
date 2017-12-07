from unittest import TestCase


def checksum(data, operator):
    rows = [[int(num) for num in row.strip().split()] for row in data.strip().split("\n")]
    return sum(operator(rows))

def difference(rows):
    return [max(row) - min(row) for row in rows]

def quotients(rows):
    return [find_quotient(row) for row in rows]

def find_quotient(row):
    row.sort()
    while len(row) > 1:
        num = row.pop()
        for n in row:
            if num % n == 0:
                return num / n

def main():
    with open('solutions/inputs/day2.txt') as f:
        data = f.read().strip()
    print(checksum(data, difference))
    print(checksum(data, quotients))


if __name__ == '__main__':
    main()

class TestChecksum(TestCase):
    def test_checksum_computes_difference_for_one_row(self):
        input = '5 1 9 5'
        input2 = '7 5 3'
        self.assertEqual(checksum(input, difference), 8)
        self.assertEqual(checksum(input2, difference), 4)

    def test_checksum_computes_and_sums_diff_for_all_rows(self):
        input = "5 1 9 5\n7 5 3\n2 4 6 8\n"
        self.assertEqual(checksum(input, difference), 18)

    def test_checksum2_computes_correctly(self):
        input = '5 9 2 8'
        self.assertEqual(checksum(input, quotients), 4)

    def test_checksum2_computes_and_sums_quotients_for_all_rows(self):
        input = "5 9 2 8\n9 4 7 3\n3 8 6 5\n"
        self.assertEqual(checksum(input, quotients), 9)

