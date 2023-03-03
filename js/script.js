const playerText = document.querySelector("#playerText");
const computerText = document.querySelector("#computerText");
const resultText = document.querySelector("#resultText");
const restartBtn = document.querySelector("#reset");
const playerPoins = document.querySelector("#playerPoin");
const computerPoins = document.querySelector("#computerPoin");
let player;
let computer;
let playerPoin = 0;
let computerPoin = 0;

function playerChoice(choice) {
  player = choice;
  playerText.innerHTML = `Player: ${player}`;
  computerChoice();
  resultText.innerHTML = checkWinner();
  playerPoins.innerHTML = `Player Poin: ${playerPoin}`;
  computerPoins.innerHTML = `Computer Poin: ${computerPoin}`;
  if (playerPoin === 5) {
    alert("You Win!, Play Again?");
    reset();
  } else if (computerPoin === 5) {
    alert("You Lose!, Play Again?");
    reset();
  }
}

function computerChoice() {
  const randomNum = Math.floor(Math.random() * 3) + 1;
  switch (randomNum) {
    case 1:
      computer = "Rock";
      break;
    case 2:
      computer = "Paper";
      break;
    case 3:
      computer = "Scissors";
      break;
  }
  computerText.innerHTML = `Computer: ${computer}`;
}

function checkWinner() {
  if (player == computer) {
    return "Draw!";
  } else if (player == "Rock") {
    if (computer == "Scissors") {
      playerPoin++;
      return "You Win!";
    } else {
      computerPoin++;
      return "You Lose!";
    }
  } else if (player == "Paper") {
    if (computer == "Rock") {
      playerPoin++;
      return "You Win!";
    } else {
      computerPoin++;
      return "You Lose!";
    }
  } else if (player == "Scissors") {
    if (computer == "Paper") {
      playerPoin++;
      return "You Win!";
    } else {
      computerPoin++;
      return "You Lose!";
    }
  }
}

function reset() {
  playerPoin = 0;
  computerPoin = 0;
  playerText.innerHTML = `Player: `;
  computerText.innerHTML = `Computer: `;
  resultText.innerHTML = `Result: `;
  playerPoins.innerHTML = `Player Poin: ${playerPoin}`;
  computerPoins.innerHTML = `Computer Poin: ${computerPoin}`;
}
