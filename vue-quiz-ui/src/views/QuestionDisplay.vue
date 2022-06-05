<template>
<img v-if="question.image" :src="question.image"/>
<h3 >{{question.title}}</h3>
<h3 >{{question.text}}</h3>
<ol>
  <li v-for="(answ, index) in question.possibleAnswers">
  <button @click="$emit('answer-selected', index, answ.isCorrect)" type="button" class="btn btn-primary">{{ answ.text}} </button>
  </li>
</ol>
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