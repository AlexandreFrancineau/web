<template>
question manager
<h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
<QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
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
            countAnswer:1
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
    },
    methods:{
        async answerClickedHandler(index , isCorrect){
            if(isCorrect== true){
                this.endQuiz()
                this.countCorrectAnswer= this.countCorrectAnswer+1 
                this.countAnswer= this.countAnswer+1
                console.log("nombre de la question :")
                console.log(this.countAnswer)
            }
            else{
                this.endQuiz()
                this.countAnswer= this.countAnswer+1
                console.log("nombre de  la question:")
                console.log(this.countAnswer)
            }
            
        },

        async loadQuestionByPosition(index){
            let question = await QuizApiService.getQuestion(index)
            this.currentQuestion = question.data
        },
        async endQuiz(){
            let nberOfQuestion = await QuizApiService.getNumberOfQuestion()
            this.numberOfQuestion = nberOfQuestion.data
            if(this.countAnswer == this.numberOfQuestion+1){
                console.log("quiz fini")
                this.$router.push('/quizFini')
            }
            else{
                this.loadQuestionByPosition(this.countAnswer)
            }
        }

    }
}
</script>