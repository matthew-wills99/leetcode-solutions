/*


Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Subtraction:

I before V and X is -1
X before L and C is -10
C before D and M is -100
*/

int value(char c) {
    switch (c) {
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
    }
    return 0;
}

int romanToInt(char* s) {
    int length = strlen(s);
    int total = 0;

    for (int i = 0; i < length; i++) {
        int cur = value(s[i]);
        if (i + 1 < length && cur < value(s[i + 1])) {
            total -= cur;   // subtractive case, e.g. the I in IV
        } else {
            total += cur;
        }
    }
    return total;
}