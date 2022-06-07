<template>
<h1>Question {{ this.countAnswer }} / {{this.numberOfQuestion }}</h1>
<QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
<transition name="fade" appear>
    <div class="modal-overlay" v-if="this.quizFini" @click="this.quizFini=false">
    </div>
</transition>
<div class="modal-overlay" v-if="this.quizFini">
    <div class="text">
        <p >Bonjour {{this.username}},tu as eu <span style="color:green">{{this.countCorrectAnswer}}</span> / <span style="color:red">{{this.numberOfQuestion}}</span></p>
        <div class="btn-toolbar" style="justify-content:space-between;">
            <button type="submit" class="btn btn-primary" @click="this.$router.go()">rejouer</button>
            <button type="submit" class="btn btn-secondary" @click="this.$router.push('/')">Home</button>
        </div>
        
    </div>
    </div>
  <footer class="bottomfooter">
    <section class="bottom__container">
      <div class="progress">
      <div id="realProgressbar" class="progress__inner" ></div>
    </div>
    </section>  
  </footer>
</template>

<script>
import QuizApiService from "../services/QuizApiService"
import QuestionDisplay from "../views/QuestionDisplay.vue"
import ParticipationStorageService from "../services/ParticipationStorageService"
import axios from "axios";
export default{
    name:'QuestionManager',
    data(){
        return{
            currentQuestion:[],
            countCorrectAnswer : 0,
            countAnswer:1,
            numberOfQuestion:null,
            quizFini:false,
            username:'',
            answers:[]
        }
    },
    components: {
        QuestionDisplay
    },
    async beforeCreate(){
        let question1 = await QuizApiService.getQuestion(1)
        this.currentQuestion = question1.data
        let nberOfQuestion = await QuizApiService.getNumberOfQuestion()
        this.numberOfQuestion = nberOfQuestion.data
        this.username = window.localStorage.getItem("playerName")
    },
    methods:{
        async answerClickedHandler(index , isCorrect){
            if(isCorrect== true){
                this.endQuiz()
                this.countCorrectAnswer= this.countCorrectAnswer+1 
                this.countAnswer= this.countAnswer+1
                console.log("les réponses:")
                console.log(index+1)
                this.answers.push(index+1)
                console.log(this.answers)

            }
            else{
                this.endQuiz()
                this.countAnswer= this.countAnswer+1
                console.log("les réponses:")
                console.log(index+1)
                this.answers.push(index+1)
                console.log(this.answers)
            }
            
        },

        async loadQuestionByPosition(index){
            let question = await QuizApiService.getQuestion(index)
            this.currentQuestion = question.data
            this.getPercent()
        },
        async endQuiz(){
            let nberOfQuestion = await QuizApiService.getNumberOfQuestion()
            this.numberOfQuestion = nberOfQuestion.data
            if(this.countAnswer == this.numberOfQuestion+1){
                this.quizFini=true
                ParticipationStorageService.saveParticipationScore(this.countCorrectAnswer)
                console.log(window.localStorage.getItem("score"))
                let json={"playerName":window.localStorage.getItem("playerName"),"answers": this.answers}
                console.log("notre json :")
                console.log(json)
                axios.post('http://localhost:5000/participations',json).then(response =>console.log(response));
                
            }
            else{
                this.loadQuestionByPosition(this.countAnswer)
            }
            if(this.countAnswer>=this.numberOfQuestion+1){
                this.countAnswer = this.numberOfQuestion
            }
        },
        async getPercent(){
            let nberOfQuestion = await QuizApiService.getNumberOfQuestion()
            this.numberOfQuestion = nberOfQuestion.data
            let percent = (this.countAnswer )/this.numberOfQuestion
            document.getElementById('realProgressbar').style.width= percent*100 +"%";
            return percent*100+'%'
        }

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

.bottomfooter{
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
    margin-left: auto;
    margin-right: auto;
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




.modal-overlay{
    position:absolute;
    top:0;
    left:0;
    right:0;
    bottom:0;
    z-index:98;
    background-color: rgba(0,0,0,0.3);
    height:100vh;
    width:100vw;
}

.fade-enter-active,
.fade-leave-active {
     transition:opacity 0.5s;
}
.fade-enter,
.fade-leave-to
{
    opacity: 0;
}
.text{
    position:absolute;
    top:50vh;
    left:40vw;
    background-color: white;
    border-radius: 16px;
    border-width: 200px;
    margin:10px 10px;
    padding:25px;
    z-index:99;
}

h1{
    list-style-type: none;
    display: flex;
    justify-content: center;
    margin-left: auto;
    margin-right: auto;
    flex-direction: column;
    align-items: center;
}
.btn-primary{
    margin-right: 20px;
}
p{
    text-align: center;
}
</style>