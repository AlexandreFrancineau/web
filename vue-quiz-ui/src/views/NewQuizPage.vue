<template>
  <div class="container">
  <form >
    <div class="quiz__inner">
    <div data-question="1" class="quiz__step--1 quiz__step--current quiz__step">
      <div class="question__emoji">✔</div>
      <h1 class="quiz__question">Entrez votre nom</h1>
      <div class="answer">
        <input type="text" class="answer__label" style="padding-left: 5px;" placeholder="username"  v-model="username"/>
      </div>
      <div class="answer">
        <button type="submit" class="answer__label" @click="launchNewQuiz">Go !</button>
      </div>       
    </div>
      </div>
  </form>
</div>

</template>
<script>
import participationStorageService from "../services/ParticipationStorageService";
export default{
  name: "NewQuizPage",
  data() {
    return {
      username:'',
      text:''
    };
  },
  methods:{
    launchNewQuiz(){
      if( this.username !=''){
        console.log("launch new quiz with", this.username)
        participationStorageService.savePlayerName(this.username)
      
      this.$router.push('/questions')
      }
      else{
         this.$router.push('/nonValidUsername')
      }
      
    },
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Raleway:400,500,700,800');
*{
  box-sizing: border-box
}
html, body{
  margin:0;
  padding:0;
  height:100%;
  color:#14152C;
  font-family: 'Raleway', sans-serif;
 
}

body{
  background-color:#f7f8fc;
}

.bottom {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #fff;
    padding: 15px 10px;
    box-shadow: 0px -2px 12px rgba(0,0,0,0.1);
}

.bottom__container {
    max-width: 1200px;
    margin: auto;
    display: flex;
      justify-content: space-between;
    align-items: center;
}

.progress {
    width: 40%;
    height: 10px;
    position: relative;
    border-radius: 5px;
  overflow:hidden;
    background-color: #ecedf5;
}
.progress__inner {
    position: absolute;
    top: 0;
    border-radius: 5px;
    height: 100%;
    left: 0;
    width: 0%;
    background-color: #5861af;
  transition:.4s width linear
}


.quiz__question{
  font-weight:900;
  letter-spacing:1px;
    margin-top: 0;
    font-size: 34px;
    margin-bottom: 50px;
}

.container {
    display: flex;
    height: calc(100% - 74px);
    width: 100%;
    align-items: center;
    justify-content: center;
    padding: 15px 10px;
}
.answer:first-of-type{
  margin-right:15px;
}


.answer__label {
    width: 140px;
    border: 1px solid #A7AACB;
    display: inline-block;
    border-radius: 6px;
    padding: 0px 15px;
  padding-left:55px;
  line-height: 56px;
    font-size: 15px;
  color: #A7AACB;
  text-align:left;
    font-weight: 600;
}
.answer__label:hover{
    border-color:#5861af;
    color:#14152C;
    box-shadow: 0px 0px 1px 4px rgba(88,97,175, 0.2)
}
.answer {
    display: inline-block;
  margin-right:10px;
}



.quiz__step {
    text-align: center;
}


.question__emoji{
  font-size:45px;
  margin-bottom:15px;
  display: inline-block;
   margin-right: 15px;
}


</style>
