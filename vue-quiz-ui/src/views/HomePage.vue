<template>
  <h1>Home page</h1>
  <div class="text-center">
     <button type="submit" class="answer__start" @click="this.$router.push('/newQuizPage')">Démarrer le quiz !</button>
  
  <h1> Tableau des scores</h1>
  <ul>
    <li class="bouton" v-for="scoreEntry in registeredScores.scores">
    <button class="leaderBoard">nom : {{ scoreEntry.playerName }} - score: {{ scoreEntry.score }}</button>
    </li>
    </ul>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: []
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    await quizApiService.getQuizInfo().then((resp) =>{
      this.registeredScores=resp.data
    })
    console.log(this.registeredScores.scores)
  }
};
</script>
<style>
.answer__start {
    width: 340px;
    border: 1px solid #A7AACB;
    display: inline-block;
    border-radius: 6px;
    padding: 0px 15px;
    line-height: 56px;
    font-size: 15px;
    color: #A7AACB;
    font-weight: 600;
    margin-left: auto;
    margin-right: auto;
}
.answer__start:hover{
    border-color:#5861af;
    color:#14152C;
    box-shadow: 0px 0px 1px 4px rgba(88,97,175, 0.2)
}
.leaderBoard{
    width: 300px;
    border: 0px solid;
    display: inline-block;
    border-radius: 6px;
    padding: 0px 15px;
    line-height: 30px;
    font-size: 15px;
    color: #535564;
    text-align:center;
    font-weight: 600;
    margin-bottom:10px;

}
</style>