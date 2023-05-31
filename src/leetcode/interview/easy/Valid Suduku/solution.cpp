class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<size_t, unordered_set<char>> row_map, col_map, cel_map;
        
        for (size_t i = 0; i < board.size(); ++i) {
            for (size_t j=0; j < board[0].size(); ++j) {
                
                // if no value then continue
                if (board[i][j] == '.') continue;
                
                // if cannot insert to row set then invalid suduku
                if (!row_map[i].insert(board[i][j]).second) return false;
                
                // if cannot insert to column set then return false
                if (!col_map[j].insert(board[i][j]).second) return false;
                
                // Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
                if (!cel_map[((i / 3) * 3) + (j / 3)].insert(board[i][j]).second) return false;
            }
        }
        return true;
    }
};
