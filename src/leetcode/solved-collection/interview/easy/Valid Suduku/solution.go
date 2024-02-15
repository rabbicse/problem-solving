func isValidSudoku(board [][]byte) bool {
	rowMap := make(map[int]map[byte]bool)
	colMap := make(map[int]map[byte]bool)
	celMap := make(map[int]map[byte]bool)

	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {

			// if no value then continue
			if board[i][j] == '.' {
				continue
			}

			// if cannot insert to row set then invalid sudoku
			if _, ok := rowMap[i][board[i][j]]; ok {
				return false
			}
			if rowMap[i] == nil {
				rowMap[i] = make(map[byte]bool)
			}
			rowMap[i][board[i][j]] = true

			// if cannot insert to column set then return false
			if _, ok := colMap[j][board[i][j]]; ok {
				return false
			}
			if colMap[j] == nil {
				colMap[j] = make(map[byte]bool)
			}
			colMap[j][board[i][j]] = true

			// Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
			celIndex := (i/3)*3 + j/3
			if _, ok := celMap[celIndex][board[i][j]]; ok {
				return false
			}
			if celMap[celIndex] == nil {
				celMap[celIndex] = make(map[byte]bool)
			}
			celMap[celIndex][board[i][j]] = true
		}
	}
	return true
}
