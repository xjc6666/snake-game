// 贪吃蛇游戏实现
const snakeCanvas = document.getElementById('snakeCanvas');
const snakeCtx = snakeCanvas.getContext('2d');
const scoreElement = document.getElementById('snakeScore');

const GRID_SIZE = 20;
const GRID_COUNT = 25;

let snake = [];
let food = {};
let direction = 'right';
let score = 0;
let gameLoop = null;

function initSnake() {
    snake = [
        {x: 5, y: 5},
        {x: 4, y: 5},
        {x: 3, y: 5}
    ];
    direction = 'right';
    score = 0;
    generateFood();
    scoreElement.textContent = score;
}

function generateFood() {
    food = {
        x: Math.floor(Math.random() * GRID_COUNT),
        y: Math.floor(Math.random() * GRID_COUNT)
    };
    // 确保食物不会出现在蛇身上
    while (snake.some(segment => segment.x === food.x && segment.y === food.y)) {
        food = {
            x: Math.floor(Math.random() * GRID_COUNT),
            y: Math.floor(Math.random() * GRID_COUNT)
        };
    }
}

function drawSnake() {
    snakeCtx.fillStyle = '#4CAF50';
    snake.forEach(segment => {
        snakeCtx.fillRect(
            segment.x * GRID_SIZE,
            segment.y * GRID_SIZE,
            GRID_SIZE - 1,
            GRID_SIZE - 1
        );
    });
}

function drawFood() {
    snakeCtx.fillStyle = '#FF5722';
    snakeCtx.fillRect(
        food.x * GRID_SIZE,
        food.y * GRID_SIZE,
        GRID_SIZE - 1,
        GRID_SIZE - 1
    );
}

function moveSnake() {
    const head = {x: snake[0].x, y: snake[0].y};
    
    switch(direction) {
        case 'up': head.y--; break;
        case 'down': head.y++; break;
        case 'left': head.x--; break;
        case 'right': head.x++; break;
    }

    if (head.x < 0 || head.x >= GRID_COUNT || 
        head.y < 0 || head.y >= GRID_COUNT ||
        snake.some(segment => segment.x === head.x && segment.y === head.y)) {
        gameOver();
        return;
    }

    snake.unshift(head);

    if (head.x === food.x && head.y === food.y) {
        score += 10;
        scoreElement.textContent = score;
        generateFood();
    } else {
        snake.pop();
    }
}

function gameOver() {
    clearInterval(gameLoop);
    gameLoop = null;
    snakeCtx.fillStyle = 'rgba(0, 0, 0, 0.5)';
    snakeCtx.fillRect(0, 0, snakeCanvas.width, snakeCanvas.height);
    snakeCtx.fillStyle = 'white';
    snakeCtx.font = '30px Arial';
    snakeCtx.textAlign = 'center';
    snakeCtx.fillText('游戏结束!', snakeCanvas.width/2, snakeCanvas.height/2);
}

function updateGame() {
    snakeCtx.clearRect(0, 0, snakeCanvas.width, snakeCanvas.height);
    moveSnake();
    drawFood();
    drawSnake();
}

function startSnake() {
    if (gameLoop) return;
    initSnake();
    gameLoop = setInterval(updateGame, 100);
}

function resetSnake() {
    if (gameLoop) {
        clearInterval(gameLoop);
    }
    startSnake();
}

document.addEventListener('keydown', (event) => {
    switch(event.key) {
        case 'ArrowUp':
            if (direction !== 'down') direction = 'up';
            break;
        case 'ArrowDown':
            if (direction !== 'up') direction = 'down';
            break;
        case 'ArrowLeft':
            if (direction !== 'right') direction = 'left';
            break;
        case 'ArrowRight':
            if (direction !== 'left') direction = 'right';
            break;
    }
}); 