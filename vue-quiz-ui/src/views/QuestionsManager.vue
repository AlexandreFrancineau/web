<template>
<h1>Question {{ this.countAnswer }} / {{this.numberOfQuestion }}</h1>
<QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
<transition name="fade" appear>
    <div class="modal-overlay" v-if="this.quizFini" @click="this.quizFini=false">
    </div>
</transition>
<div class="modal-overlay" v-if="this.quizFini">
    <div class="text">
        <p>tu as eu <span style="color:green">{{this.countCorrectAnswer}}</span> / <span style="color:red">{{this.numberOfQuestion}}</span></p>
        <div class="btn-toolbar" style="justify-content:space-between;">
            <button type="submit" class="btn btn-primary" @click="this.$router.go()">rejouer</button>
            <button type="submit" class="btn btn-secondary" @click="this.$router.push('/')">Home</button>
        </div>
        
    </div>
    </div>
</template>

<script>
import QuizApiService from "../services/QuizApiService"
import QuestionDisplay from "../views/QuestionDisplay.vue"
export default{
    name:'QuestionManager',
    data(){
        return{
            currentQuestion:[],
            countCorrectAnswer : 0,
            countAnswer:1,
            numberOfQuestion:null,
            quizFini:false
        }
    },
    components: {
        QuestionDisplay
    },
    async beforeCreate(){
        let question1 = await QuizApiService.getQuestion(1)
        this.currentQuestion = question1.data
        console.log("nombre de la question :")
        console.log(this.countAnswer)
        let nberOfQuestion = await QuizApiService.getNumberOfQuestion()
        this.numberOfQuestion = nberOfQuestion.data
        console.log("nombre de questions :")
        console.log(this.numberOfQuestion)
    },
    methods:{
        async answerClickedHandler(index , isCorrect){
            if(isCorrect== true){
                this.endQuiz()
                this.countCorrectAnswer= this.countCorrectAnswer+1 
                this.countAnswer= this.countAnswer+1
                console.log("nombre de bonne réponse:")
                console.log(this.countCorrectAnswer)
            }
            else{
                this.endQuiz()
                this.countAnswer= this.countAnswer+1
                console.log("nombre de bonne réponse:")
                console.log(this.countCorrectAnswer)
            }
            
        },

        async loadQuestionByPosition(index){
            let question = await QuizApiService.getQuestion(index)
            this.currentQuestion = question.data
        },
        async endQuiz(){
            let nberOfQuestion = await QuizApiService.getNumberOfQuestion()
            this.numberOfQuestion = nberOfQuestion.data
            console.log("nombre de question :")
            console.log(this.numberOfQuestion)
            if(this.countAnswer == this.numberOfQuestion+1){
                console.log("quiz fini :")
                this.quizFini=true
                console.log(this.quizFini)
                // this.$router.push('/quizFini')
            }
            else{
                this.loadQuestionByPosition(this.countAnswer)
                console.log("quiz fini :")
                console.log(this.quizFini)
            }
            if(this.countAnswer>=this.numberOfQuestion+1){
                this.countAnswer = this.numberOfQuestion
            }
        }

    }
}
</script>

<style>
@import '@/assets/base.css';

.modal-overlay{
    position:absolute;
    top:0;
    left:0;
    right:0;
    bottom:0;
    z-index:98;
    background-color: rgba(0,0,0,0.3);
    height:110vh;
    width:150vw;
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
    left:20vw;
}
</style>