'''

This is a fun script and not a serious repo, treat it as such. 
I'm sure there are a million ways to make this far better.

'''


class Checker:

    def __init__(self):
        pass

    def chkCol(self, s_arr, j, n):      #Checks if there is the same number in the column already

        for c in range(9):
            if s_arr[c][j] == n:
                return False
        
        return True

    def chkRow(self, s_arr, i, n):     #Checks if there is the same number in the row already

        for c in range(9):
            if s_arr[i][c] == n:
                return False

        return True

    def chkBlock(self, s_arr, i, j, n):       #Checks which block does that cell belong to and if there's the same num in the block already

        if i < 3:
            pos_x = {0, 1, 2}
        elif 6 > i >= 3:
            pos_x = {3, 4, 5}
        else:
            pos_x = {6, 7, 8}

        if j < 3:
            pos_y = {0, 3, 6}
        elif 6 > i >= 3:
            pos_y = {1, 4, 7}
        else:
            pos_y = {2, 5, 8}

        # block_num = list(pos_x.intersection(pos_y))[0]

        block_num = list(pos_x & pos_y)[0]
        blocks_coord = [[0, 3, 0, 3], [0, 3, 3, 6], [0, 3, 6, 9], [3, 6, 0, 3], [3, 6, 3, 6], [3, 6, 6, 9],
                        [6, 9, 0, 3], [6, 9, 3, 6], [6, 9, 6, 9]]
        cur_block = blocks_coord[block_num]

        i1, i2, j1, j2 = cur_block[0], cur_block[1], cur_block[2], cur_block[3]

        for c1 in range(i1, i2):
            for c2 in range(j1, j2):
                if s_arr[c1][c2] == n:
                    return False

        return True

    def chkSeq(self, s_arr, i, j, n):         #Puts the checks in sequence to use.
        r_res = self.chkRow(s_arr, i, n)
        if r_res is True:
            c_res = self.chkCol(s_arr, j, n)
            if c_res is True:
                b_res = self.chkBlock(s_arr, i, j, n)
                if b_res is True:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
