import parser


def test_one():
    print("==TEST ONE==")
    output = parser.parse_string('display: .size 1')
    print(output)


def test_two():
    print("==TEST TWO==")
    output = parser.parse_file('tests/test.darkest')
    print(output)
