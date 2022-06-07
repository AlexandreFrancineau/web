export default {
    clear() {
          // todo : implement
    },
    savePlayerName(playerName) {
      window.localStorage.setItem("playerName", playerName);
    },
    getPlayerName() {		
      window.localStorage.getItem("playerName");
    },
    saveParticipationScore(participationScore) {
      window.localStorage.setItem("score",participationScore)
    },
    getParticipationScore() {
      window.localStorage.getItem("score")
    },
  };