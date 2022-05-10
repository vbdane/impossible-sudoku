let sudoku_grid = [
    [0,4,3,0,8,0,2,5,0],
    [6,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,9,4],
    [9,0,0,0,0,4,0,7,0],
    [0,0,0,6,0,8,0,0,0],
    [0,1,0,2,0,0,0,0,3],
    [8,2,0,5,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,5],
    [0,3,4,0,9,0,7,1,0]
];


function solve(){
    for (let y=0; y<9; y++){
        for (let x=0; x<9; x++){
            if (sudoku_grid[y][x] == 0){
                for (let n=1; n<10; n++){
                    if (check(y, x, n) == true){
                        sudoku_grid[y][x] = n;
                        solve();
                        sudoku_grid[y][x] = 0;
                    }
                }
                return
            }
        }
    }
    console.log(sudoku_grid)
}


function check(y, x, n){
    for (let i=0; i<9; i++){
        if (sudoku_grid[y][i] == n){
            return false
        }
        if (sudoku_grid[i][x] == n){
            return false
        }
    }
    
    let x_floor = (Math.floor(x/3))*3;
    let y_floor = (Math.floor(y/3))*3;
    
    for (let j=0; j<3; j++){
        for (let i=0; i<3; i++){
            if (sudoku_grid[y_floor+j][x_floor+i] == n){
                return false
            }
        }
    }
    return true
}


solve()