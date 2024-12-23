// 五子棋游戏实现
const gomokuCanvas = document.getElementById('gomokuCanvas');
const gomokuCtx = gomokuCanvas.getContext('2d');
const playerElement = document.getElementById('currentPlayer');

const BOARD_SIZE = 15;
const CELL_SIZE = gomokuCanvas.width / (BOARD_SIZE + 1);
const PIECE_RADIUS = CELL_SIZE * 0.4;

let board = Array(BOARD_SIZE).fill().map(() => Array(BOARD_SIZE).fill(null));
let currentPlayer = 'black';
let gameActive = true;

function drawBoard() {
    gomokuCtx.fillStyle = '#DEB887';
    gomokuCtx.fillRect(0, 0, gomokuCanvas.width, gomokuCanvas.height);

    gomokuCtx.strokeStyle = '#000';
    gomokuCtx.lineWidth = 1;

    // 画横线
    for (let i = 0; i < BOARD_SIZE; i++) {
        gomokuCtx.beginPath();
        gomokuCtx.moveTo(CELL_SIZE, (i + 1) * CELL_SIZE);
        gomokuCtx.lineTo(CELL_SIZE * BOARD_SIZE, (i + 1) * CELL_SIZE);
        gomokuCtx.stroke();
    }

    // 画竖线
    for (let i = 0; i < BOARD_SIZE; i++) {
        gomokuCtx.beginPath();
        gomokuCtx.moveTo((i + 1) * CELL_SIZE, CELL_SIZE);
        gomokuCtx.lineTo((i + 1) * CELL_SIZE, CELL_SIZE * BOARD_SIZE);
        gomokuCtx.stroke();
    }
}

function drawPiece(row, col, color) {
    gomokuCtx.beginPath();
    gomokuCtx.arc(
        (col + 1) * CELL_SIZE,
        (row + 1) * CELL_SIZE,
        PIECE_RADIUS,
        0,
        Math.PI * 2
    );
    gomokuCtx.fillStyle = color;
    gomokuCtx.fill();
    gomokuCtx.stroke();
}

function checkWin(row, col) {
    const directions = [
        [[0, 1], [0, -1]],  // 横向
        [[1, 0], [-1, 0]],  // 纵向
        [[1, 1], [-1, -1]], // 主对角线
        [[1, -1], [-1, 1]]  // 副对角线
    ];

    for (let dirPair of directions) {
        let count = 1;
        for (let dir of dirPair) {
            let r = row + dir[0];
            let c = col + dir[1];
            while (
                r >= 0 && r < BOARD_SIZE &&
                c >= 0 && c < BOARD_SIZE &&
                board[r][c] === currentPlayer
            ) {
                count++;
                r += dir[0];
                c += dir[1];
            }
        }
        if (count >= 5) return true;
    }
    return false;
}

function handleClick(event) {
    if (!gameActive) return;

    const rect = gomokuCanvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    const col = Math.round(x / CELL_SIZE - 1);
    const row = Math.round(y / CELL_SIZE - 1);

    if (
        row >= 0 && row < BOARD_SIZE &&
        col >= 0 && col < BOARD_SIZE &&
        !board[row][col]
    ) {
        board[row][col] = currentPlayer;
        drawPiece(row, col, currentPlayer);

        if (checkWin(row, col)) {
            gameActive = false;
            setTimeout(() => {
                alert(`${currentPlayer === 'black' ? '黑方' : '白方'}获胜！`);
            }, 100);
            return;
        }

        currentPlayer = currentPlayer === 'black' ? 'white' : 'black';
        playerElement.textContent = currentPlayer === 'black' ? '黑方' : '白方';
    }
}

function resetGomoku() {
    board = Array(BOARD_SIZE).fill().map(() => Array(BOARD_SIZE).fill(null));
    currentPlayer = 'black';
    gameActive = true;
    playerElement.textContent = '黑方';
    drawBoard();
}

gomokuCanvas.addEventListener('click', handleClick);
drawBoard(); 