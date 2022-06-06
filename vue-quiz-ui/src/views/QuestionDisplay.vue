<template>
<div class="question">
    <img v-if="question.image" :src="question.image"/>
    <h3 >{{question.title}}</h3>
    <h3 >{{question.text}}</h3>
    <ol class="box">
    <li class="bouton" v-for="(answ, index) in question.possibleAnswers">
    <button @click="$emit('answer-selected', index, answ.isCorrect)" class="button">{{ answ.text}} </button>
    </li>
    </ol>
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
@import '@/assets/base.css';
.box{
    display: flex;
    flex-flow: row wrap;
    align-items:flex-start;
}

.bouton{
    margin:10px;
}
.button{
    appearance:none;
    outline:none;
    border:none;
    background: none;
    cursor:pointer;
    display:inline-block;
    padding: 15px 25px;
    background-image: linear-gradient(to right,#8d9091,#9c9e9e);
    border-radius: 8px;

    color: #FFF;
    font-size: 18px;
    font-weight: 700;
    
    box-shadow: 3px 3px rgba(0,0,0,0.4);
    transition:0.4s ease-out;
}
.button:hover{
box-shadow: 6px 6px rgba(0,0,0,0.6);
}
.question{
    display:flex;
    flex-direction: column;
    text-align: center;
}

img{
    height:400px;
    width:400px;
    left:35%;
}
</style>