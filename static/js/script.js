// var socket = io();
// var room = "";
// var role = "";

// socket.on("connect", function() {
//     document.getElementById("status").textContent = "Connected";
// });

// socket.on("disconnect", function() {
//     document.getElementById("status").textContent = "Disconnected";
// });

// socket.on("message", function(data) {
//     console.log(data); // Debugging
//     var messagesDiv = document.getElementById("messages");
//     var newMessage = document.createElement("p");
//     newMessage.textContent = data.role + ": " + data.message;
//     messagesDiv.appendChild(newMessage);
// });

// socket.on("role", function(data) {
//     var roleInfoDiv = document.getElementById("role-info");
//     roleInfoDiv.textContent = data.message;
//     room = data.room;
//     role = data.role;
//     document.getElementById("message-input").style.display = "block";
//     console.log("Assigned role:", role); // Debugging
// });

// function sendMessage() {

//     var messageInput = document.getElementById("message");
//     var message = messageInput.value;
//     console.log(message); // Debugging

//     console.log("Sending message with role:", role); // Debugging
//     socket.emit("message", {
//         message: message,
//         room: room,
//         role: role,
//     });
//     messageInput.value = "";
// }


// const canvas = document.getElementById('gameCanvas');
// const ctx = canvas.getContext('2d');

// const image = new Image();
// image.src = "static\\board.png"
// console.log(image)
// image.onload = () => {
//     drawBoard();
// };

// const points = [{
//         x: 378.7999954223633,
//         y: 25.400001525878906
//     },

//     {
//         x: 65.79999542236328,
//         y: 195.4000015258789
//     },

//     {
//         x: 313.7999954223633,
//         y: 195.4000015258789
//     },

//     {
//         x: 362.7999954223633,
//         y: 190.4000015258789
//     },

//     {
//         x: 406.7999954223633,
//         y: 189.4000015258789
//     },

//     {
//         x: 448.7999954223633,
//         y: 192.4000015258789
//     },

//     {
//         x: 699.7999954223633,
//         y: 197.4000015258789
//     },

//     {
//         x: 69.79999542236328,
//         y: 262.4000015258789
//     },

//     {
//         x: 281.7999954223633,
//         y: 265.4000015258789
//     },

//     {
//         x: 350.7999954223633,
//         y: 261.4000015258789
//     },

//     {
//         x: 425.7999954223633,
//         y: 261.4000015258789
//     },

//     {
//         x: 473.7999954223633,
//         y: 263.4000015258789
//     },

//     {
//         x: 705.7999954223633,
//         y: 256.4000015258789
//     },

//     {
//         x: 66.79999542236328,
//         y: 338.4000015258789
//     },

//     {
//         x: 255.79999542236328,
//         y: 337.4000015258789
//     },

//     {
//         x: 349.7999954223633,
//         y: 337.4000015258789
//     },

//     {
//         x: 438.7999954223633,
//         y: 337.4000015258789
//     },

//     {
//         x: 506.7999954223633,
//         y: 337.4000015258789
//     },

//     {
//         x: 696.7999954223633,
//         y: 335.4000015258789
//     },

//     {
//         x: 196.79999542236328,
//         y: 497.4000015258789
//     },

//     {
//         x: 330.7999954223633,
//         y: 497.4000015258789
//     },

//     {
//         x: 467.7999954223633,
//         y: 497.4000015258789
//     },

//     {
//         x: 564.7999954223633,
//         y: 494.4000015258789
//     },
// ];

// const pieceRadius = 20;
// let board = Array(points.length).fill(null);
// let selectedPiece = null;
// let animationFrameId = null;

// function drawBoard() {
//     ctx.clearRect(0, 0, canvas.width, canvas.height);
//     ctx.drawImage(image, 0, 0, canvas.width, canvas.height);
//     points.forEach((point, index) => {
//         // Draw points
//         ctx.beginPath();
//         ctx.arc(point.x, point.y, pieceRadius / 2, 0, Math.PI * 2);
//         ctx.fillStyle = '#333';
//         ctx.fill();
//         ctx.closePath();

//         // Draw pieces
//         if (board[index]) {
//             ctx.beginPath();
//             ctx.arc(point.x, point.y, pieceRadius, 0, Math.PI * 2);
//             ctx.fillStyle = '#d9534f';
//             ctx.fill();
//             ctx.lineWidth = 2;
//             ctx.strokeStyle = '#000';
//             ctx.stroke();
//             ctx.closePath();

//             if (selectedPiece === index) {
//                 ctx.lineWidth = 3;
//                 ctx.strokeStyle = '#d9534f';
//                 ctx.stroke();
//             }
//         }
//     });
// }

// function getCharacterByIndex(index) {
//     if (index >= 0 && index < 23) {
//         return String.fromCharCode('a'.charCodeAt(0) + index);
//     } else {
//         throw new RangeError("Index out of range. It must be between 0 and 22.");
//     }
// }

// function getPointIndex(pos) {
//     for (let i = 0; i < points.length; i++) {
//         const point = points[i];
//         const dx = pos.x - point.x;
//         const dy = pos.y - point.y;
//         if (Math.sqrt(dx * dx + dy * dy) < pieceRadius) {
//             return i;
//         }
//     }
//     return null;
// }

// function animateMovement(fromIndex, toIndex) {
//     const from = points[fromIndex];
//     const to = points[toIndex];
//     const piece = board[fromIndex];
//     const startTime = performance.now();
//     const duration = 500; // duration in ms

//     console.log(`Moving piece from (${getCharacterByIndex(fromIndex)}) to (${getCharacterByIndex(toIndex)})`);
//     socket.emit("message", {
//         message: getCharacterByIndex(fromIndex) + ',' + getCharacterByIndex(toIndex) ,
//         room: room,
//         role: role,
//     });
//     function movePiece(timestamp) {
//         const elapsed = timestamp - startTime;
//         const progress = Math.min(elapsed / duration, 1);
//         const currentX = from.x + (to.x - from.x) * progress;
//         const currentY = from.y + (to.y - from.y) * progress;

//         ctx.clearRect(0, 0, canvas.width, canvas.height);
//         ctx.drawImage(image, 0, 0, canvas.width, canvas.height);
//         points.forEach((point, index) => {
//             // Draw points
//             ctx.beginPath();
//             ctx.arc(point.x, point.y, pieceRadius / 2, 0, Math.PI * 2);
//             ctx.fillStyle = '#333';
//             ctx.fill();
//             ctx.closePath();

//             // Draw pieces
//             if (board[index]) {
//                 ctx.beginPath();
//                 ctx.arc(point.x, point.y, pieceRadius, 0, Math.PI * 2);
//                 ctx.fillStyle = '#d9534f';
//                 ctx.fill();
//                 ctx.lineWidth = 2;
//                 ctx.strokeStyle = '#000';
//                 ctx.stroke();
//                 ctx.closePath();
//             }
//         });

//         // Draw moving piece
//         ctx.beginPath();
//         ctx.arc(currentX, currentY, pieceRadius, 0, Math.PI * 2);
//         ctx.fillStyle = '#d9534f';
//         ctx.fill();
//         ctx.lineWidth = 2;
//         ctx.strokeStyle = '#000';
//         ctx.stroke();
//         ctx.closePath();

//         if (progress < 1) {
//             animationFrameId = requestAnimationFrame(movePiece);
//         } else {
//             board[toIndex] = piece;
//             board[fromIndex] = null;
//             selectedPiece = null;
//             drawBoard();
//         }
//     }

//     if (animationFrameId) {
//         cancelAnimationFrame(animationFrameId);
//     }
//     animationFrameId = requestAnimationFrame(movePiece);
// }

// canvas.addEventListener('mousedown', (event) => {
//     const rect = canvas.getBoundingClientRect();
//     const pos = {
//         x: event.clientX - rect.left,
//         y: event.clientY - rect.top
//     };

//     const index = getPointIndex(pos);
//     if (index !== null) {
//         if (selectedPiece === null) {
//             if (board[index] === null) {
//                 board[index] = 'piece'; // Insert new piece
//                 console.log(`Inserted new piece at (${getCharacterByIndex(index)})`);
//                 socket.emit("message", {
//                     message: '*,' + getCharacterByIndex(index) ,
//                     room: room,
//                     role: role,
//                 });
//                 drawBoard();
//             } else {
//                 selectedPiece = index; // Select the piece for moving
//             }
//         } else {
//             if (board[index] === null) {
//                 animateMovement(selectedPiece, index);
//             } else if (selectedPiece === index) {
//                 selectedPiece = null; // Deselect if clicking on the same piece
//                 drawBoard();
//             }
//         }
//     } else {
//         selectedPiece = null; // Deselect if clicking on empty space
//         drawBoard();
//     }
// });

// // Initial draw
// drawBoard();




var socket = io();
var room = "";
var role = "";

socket.on("connect", function() {
    document.getElementById("status").textContent = "Connected";
});

socket.on("disconnect", function() {
    document.getElementById("status").textContent = "Disconnected";
});

socket.on("message", function(data) {
    console.log(data); // Debugging
    var messagesDiv = document.getElementById("messages");
    var newMessage = document.createElement("p");
    newMessage.textContent = data.role + ": " + data.message;
    messagesDiv.appendChild(newMessage);
});

socket.on("role", function(data) {
    var roleInfoDiv = document.getElementById("role-info");
    roleInfoDiv.textContent = data.message;
    room = data.room;
    role = data.role;
    document.getElementById("message-input").style.display = "block";
    console.log("Assigned role:", role); // Debugging
});

socket.on("update_board", function(data) {
    updateBoard(data.board);
    console.log(data); // Debugging
});

socket.on("game_over", function(data) {
    console.log(data); // Debugging
});


function updateBoard(newBoardState) {
    board = newBoardState;
    drawBoard();
}

function sendMessage() {
    var messageInput = document.getElementById("message");
    var message = messageInput.value;
    console.log(message); // Debugging

    console.log("Sending message with role:", role); // Debugging
    socket.emit("message", {
        message: message,
        room: room,
        role: role,
    });
    messageInput.value = "";
}

const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const image = new Image();
image.src = "static\\board.png"
console.log(image)
image.onload = () => {
    drawBoard();
};

const points = [
    { x: 378.8, y: 25.4 },
    { x: 65.8, y: 195.4 },
    { x: 313.8, y: 195.4 },
    { x: 362.8, y: 190.4 },
    { x: 406.8, y: 189.4 },
    { x: 448.8, y: 192.4 },
    { x: 699.8, y: 197.4 },
    { x: 69.8, y: 262.4 },
    { x: 281.8, y: 265.4 },
    { x: 350.8, y: 261.4 },
    { x: 425.8, y: 261.4 },
    { x: 473.8, y: 263.4 },
    { x: 705.8, y: 256.4 },
    { x: 66.8, y: 338.4 },
    { x: 255.8, y: 337.4 },
    { x: 349.8, y: 337.4 },
    { x: 438.8, y: 337.4 },
    { x: 506.8, y: 337.4 },
    { x: 696.8, y: 335.4 },
    { x: 196.8, y: 497.4 },
    { x: 330.8, y: 497.4 },
    { x: 467.8, y: 497.4 },
    { x: 564.8, y: 494.4 },
];

const pieceRadius = 20;
let board = Array(points.length).fill(null);
let selectedPiece = null;
let animationFrameId = null;

function drawBoard() {
    
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(image, 0, 0, canvas.width, canvas.height);
    points.forEach((point, index) => {
        // Draw points
        ctx.beginPath();
        ctx.arc(point.x, point.y, pieceRadius / 2, 0, Math.PI * 2);
        ctx.fillStyle = '#333';
        ctx.fill();
        ctx.closePath();

        // Draw pieces
        if (board[index]) {
            ctx.beginPath();
            ctx.arc(point.x, point.y, pieceRadius, 0, Math.PI * 2);
            ctx.fillStyle = '#d9534f';
            ctx.fill();
            ctx.lineWidth = 2;
            ctx.strokeStyle = '#000';
            ctx.stroke();
            ctx.closePath();

            if (selectedPiece === index) {
                ctx.lineWidth = 3;
                ctx.strokeStyle = '#d9534f';
                ctx.stroke();
            }
        }
    });
}

function getCharacterByIndex(index) {
    if (index >= 0 && index < 23) {
        return String.fromCharCode('a'.charCodeAt(0) + index);
    } else {
        throw new RangeError("Index out of range. It must be between 0 and 22.");
    }
}

function getPointIndex(pos) {
    for (let i = 0; i < points.length; i++) {
        const point = points[i];
        const dx = pos.x - point.x;
        const dy = pos.y - point.y;
        if (Math.sqrt(dx * dx + dy * dy) < pieceRadius) {
            return i;
        }
    }
    return null;
}

function animateMovement(fromIndex, toIndex) {
    const from = points[fromIndex];
    const to = points[toIndex];
    const piece = board[fromIndex];
    const startTime = performance.now();
    const duration = 500; // duration in ms

    console.log(`Moving piece from (${getCharacterByIndex(fromIndex)}) to (${getCharacterByIndex(toIndex)})`);
    socket.emit("message", {
        message: getCharacterByIndex(fromIndex) + ',' + getCharacterByIndex(toIndex),
        room: room,
        role: role,
    });

    function movePiece(timestamp) {
        const elapsed = timestamp - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const currentX = from.x + (to.x - from.x) * progress;
        const currentY = from.y + (to.y - from.y) * progress;

        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(image, 0, 0, canvas.width, canvas.height);
        points.forEach((point, index) => {
            // Draw points
            ctx.beginPath();
            ctx.arc(point.x, point.y, pieceRadius / 2, 0, Math.PI * 2);
            ctx.fillStyle = '#333';
            ctx.fill();
            ctx.closePath();

            // Draw pieces
            if (board[index]) {
                ctx.beginPath();
                ctx.arc(point.x, point.y, pieceRadius, 0, Math.PI * 2);
                ctx.fillStyle = '#d9534f';
                ctx.fill();
                ctx.lineWidth = 2;
                ctx.strokeStyle = '#000';
                ctx.stroke();
                ctx.closePath();
            }
        });

        // Draw moving piece
        ctx.beginPath();
        ctx.arc(currentX, currentY, pieceRadius, 0, Math.PI * 2);
        ctx.fillStyle = '#d9534f';
        ctx.fill();
        ctx.lineWidth = 2;
        ctx.strokeStyle = '#000';
        ctx.stroke();
        ctx.closePath();

        if (progress < 1) {
            animationFrameId = requestAnimationFrame(movePiece);
        } else {
            board[toIndex] = piece;
            board[fromIndex] = null;
            selectedPiece = null;
            drawBoard();
        }
    }

    if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
    }
    animationFrameId = requestAnimationFrame(movePiece);
}

canvas.addEventListener('mousedown', (event) => {
    const rect = canvas.getBoundingClientRect();
    const pos = {
        x: event.clientX - rect.left,
        y: event.clientY - rect.top
    };

    const index = getPointIndex(pos);
    if (index !== null) {
        if (selectedPiece === null) {
            if (board[index] === null) {
                board[index] = 'piece'; // Insert new piece
                console.log(`Inserted new piece at (${getCharacterByIndex(index)})`);
                socket.emit("message", {
                    message: '*,' + getCharacterByIndex(index),
                    room: room,
                    role: role,
                });
                drawBoard();
            } else {
                selectedPiece = index; // Select the piece for moving
            }
        } else {
            if (board[index] === null) {
                animateMovement(selectedPiece, index);
            } else if (selectedPiece === index) {
                selectedPiece = null; // Deselect if clicking on the same piece
                drawBoard();
            }
        }
    } else {
        selectedPiece = null; // Deselect if clicking on empty space
        drawBoard();
    }
});

// Initial draw
drawBoard();
