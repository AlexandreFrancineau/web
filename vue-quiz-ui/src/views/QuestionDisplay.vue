<template>
<div class="container">
    <div class="question">
    <img class="middle" v-if="question.image" :src="question.image"/>
    <h3 class="middle" >{{question.title}}</h3>
    <h3 class="middle">{{question.text}}</h3>
    <ul>
    <li class="bouton" v-for="(answ, index) in question.possibleAnswers">
    <button @click="$emit('answer-selected', index, answ.isCorrect)" class="answer__button">{{ answ.text}}</button>
    </li>
    </ul>
    </div>
 
</div>

</template>
<script>
export default{
    name:'QuestionDisplay',
    props: {
        emit: ["answer-selected"],
        question: {
            type: Object
        }
    }
}
</script>

<style>

.answer__button{
    width: 700px;
    border: 1px solid #A7AACB;
    display: inline-block;
    border-radius: 6px;
    padding: 0px 15px;
    line-height: 53px;
    font-size: 15px;
    color: #A7AACB;
    text-align:center;
    font-weight: 600;
    margin-bottom:10px;

}
.answer__button:hover{
    border-color:#5861af;
    color:#14152C;
    box-shadow: 0px 0px 1px 4px rgba(88,97,175, 0.2)
}
.middle{
    width:fit-content;
    margin-left: auto;
    margin-right: auto;
    display: flex;
    justify-content: center;
}
img{
    height:400px;
    width:400px;
}
ul{
    list-style-type: none;
    display: flex;
    justify-content: center;
    margin-left: auto;
    margin-right: auto;
    flex-direction: column;
    align-items: center;
}
h1 , h3{
    font-weight: bold;
}
</style>