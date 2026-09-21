// Given an integer x, return true if x is a palindrome, and false otherwise.

bool isPalindrome(int x) {
    if(x < 0) return false;

    int len = snprintf(NULL, 0, "%d", x);
    char *s = malloc(len + 1);
    snprintf(s, len + 1, "%d", x);

    bool result = true;
    for(int i = 0; i < len / 2; i++) {
        if(s[i] != s[len-1-i]) {
            result = false;
            break;
        }
    }
    free(s);
    return result;
}
