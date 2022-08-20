<template>
  <div class="homepage">

    <header class="jumbotron jumbotron-fluid text-center">
      <div class="container">
        <router-link to="/findpet" class="buttons" ><button class="btn btn-primary btn-lg">Find Pet</button></router-link>
        <router-link to="/findguardian" class="buttons"><button class="btn btn-primary btn-lg">Find Guardian</button></router-link>
        <!-- <router-link to="/profilesetup" style="color:black;" class="nav-link"><button>Profile Setup</button></router-link> -->
      </div>
    </header>

    <div class="text-center">
    <main>

      <div class="container marketing p-5">

        <div class="row featurette">
          <div class="col-md-7">
            <h2 class="featurette-heading fw-normal ">The first social media for pets! <span class="text-muted">It’ll blow your mind.</span></h2>
            <p class="lead">Let's give our pet an exposure to social media world.</p>
          </div>
          <div class="col-md-5">
            <img class="pic" :src="PetSocMed" alt="PetSocialMedia">

          </div>
        </div>

        <hr class="featurette-divider">

        <div class="row featurette">
          <div class="col-md-7 order-md-2">
            <h2 class="featurette-heading fw-normal lh-1">A platform to help animals to find a loving home. <span class="text-muted">Every animal deserves love!</span></h2>
            <p class="lead">One of the best platforms to help all animals out there finding a shelter and loving guardian.</p>
          </div>
          <div class="col-md-5 order-md-1">
            <img class="pic" :src="PetHome" alt="PetSocialMedia">
          </div>
        </div>

        <hr class="featurette-divider">

        <div class="row featurette">
          <div class="col-md-7">
            <h2 class="featurette-heading fw-normal lh-1">And lastly, a platform for sharing tips and advices. <span class="text-muted">Checkmate.</span></h2>
            <p class="lead">Considering this is the platform for all pet lovers, you are able to get tips and advices from other guardians on how to give the best love to your pet.</p>
          </div>
          <div class="col-md-5">
            <img class="pic" :src="SharingAdvices" alt="PetSocialMedia">

          </div>
        </div>

      </div><!-- /.container -->

    </main>
    </div>
    
    
    


  </div>
</template>

<script>
  import Modal from '../components/Modal.vue';
  import Footer from '../components/Footer.vue';

  import PetSocMed from '../assets/PetSocMed.jpg'
  import PetHome from '../assets/ProvideHome.jpg'
  import SharingAdvices from '../assets/SharingAdvices.jpg'

  export default {
    name: 'Home',
    components: {
      Modal,
      // MyComponent,
      Footer
    },
    data() {
      return {
        isModalVisible: false,
        PetSocMed: PetSocMed,
        PetHome: PetHome,
        SharingAdvices: SharingAdvices
      };
    },
    mounted(){
      document.title = 'PetHub | Home' //Title of the page
    },
    methods: {
      showModal() {
        this.isModalVisible = true;
      },
      closeModal() {
        this.isModalVisible = false;
      }
    }
  };
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css?family=Montserrat:400,800');

  .homepage{
  background-color: white;
  min-height:100vh;
  height:auto;
  /* overflow:scroll;  */

  } 
  header{
    background-image: url("../assets/header_bg.jpg");
    background-attachment: scroll;
    background-repeat:no-repeat;
    background-size: cover;
    height:25%;
    background-position: 0 70%;
  }

  button{
    background-color:snow;
    
    border: none;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    border: 2px solid #DB4914;
    border-radius: 12px;
    box-shadow: 0 14px 28px rgba(0,0,0,0.25), 
        0 10px 10px rgba(0,0,0,0.22); 
    width: 50%;
    height:auto;
    white-space:normal !important;
    word-wrap:break-word;

  }

  .container{
    align-items: center;
  }

  .row{
    box-shadow: none;
  }

  h2{
    font-size:2rem;
    font-weight:bold;
    color:#DB4914;
    margin-bottom: 20px;
  }

  h4{
    font-size:1.5rem;
    font-weight:bold;
    color:#DB4914;
  }

  h2,h4,p,button{
    font-family: "Montserrat", sans-serif;
  }

  .icon{
    width:30%;

  }

  .pic{
    object-fit: cover;
    width: 100%;
  }

  
</style>