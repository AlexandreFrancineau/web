<template>
  <form>
    <div class="form">
      <div class="form-group">
        <label for="nom">nom :</label>
        <p></p>
        <input type="text" class="form-control" id="nom" placeholder="Username" v-model="username">
      </div>
      <p>{{username}}</p>
      <div class="bouton">
      <button type="submit" class="btn btn-primary" @click="launchNewQuiz">Go !</button>
      <p>{{text}}</p>
      </div>
    </div>
  </form>

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
@import '@/assets/base.css';
.form{
  margin-left: 5px;
}
.form-group{
  width:200px;
}

</style>
