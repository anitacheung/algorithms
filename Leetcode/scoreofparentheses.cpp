class Solution {
public:
    int scoreOfParentheses(string s) {
        stack<int> board;
        int score = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i]=='(') {
                board.push(score);
                score = 0;
            }
            else {
                score = board.top() + max (1, score * 2);
                board.pop();
            }
        }
        return score;
        
    }
};