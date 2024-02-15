import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> rowMap = new HashMap<>();
        Map<Integer, Set<Character>> colMap = new HashMap<>();
        Map<Integer, Set<Character>> celMap = new HashMap<>();
        
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                
                // if no value then continue
                if (board[i][j] == '.') continue;
                
                // if cannot insert to row set then invalid sudoku
                if (!rowMap.computeIfAbsent(i, k -> new HashSet<>()).add(board[i][j])) return false;
                
                // if cannot insert to column set then return false
                if (!colMap.computeIfAbsent(j, k -> new HashSet<>()).add(board[i][j])) return false;
                
                // Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
                int celIndex = ((i / 3) * 3) + (j / 3);
                if (!celMap.computeIfAbsent(celIndex, k -> new HashSet<>()).add(board[i][j])) return false;
            }
        }
        return true;
    }
}
