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
            <h2 class="featurette-heading fw-normal ">First featurette heading. <span class="text-muted">It’ll blow your mind.</span></h2>
            <p class="lead">Some great placeholder content for the first featurette here. Imagine some exciting prose here.</p>
          </div>
          <div class="col-md-5">
            <img class="pic" src="https://d.newsweek.com/en/full/1630892/cat-stock-getty.jpg" height="400" width="400" alt="">

          </div>
        </div>

        <hr class="featurette-divider">

        <div class="row featurette">
          <div class="col-md-7 order-md-2">
            <h2 class="featurette-heading fw-normal lh-1">Oh yeah, it’s that good. <span class="text-muted">See for yourself.</span></h2>
            <p class="lead">Another featurette? Of course. More placeholder content here to give you an idea of how this layout would work with some actual real-world content in place.</p>
          </div>
          <div class="col-md-5 order-md-1">
            <img class="pic" src="https://apicms.thestar.com.my/uploads/images/2020/09/24/873188.jpg" height="400" width="400" alt="">

          </div>
        </div>

        <hr class="featurette-divider">

        <div class="row featurette">
          <div class="col-md-7">
            <h2 class="featurette-heading fw-normal lh-1">And lastly, this one. <span class="text-muted">Checkmate.</span></h2>
            <p class="lead">And yes, this is the last block of representative placeholder content. Again, not really intended to be actually read, simply here to give you a better view of what this would look like with some actual content. Your content.</p>
          </div>
          <div class="col-md-5">
            <img class="pic" src="https://www.theladders.com/wp-content/uploads/dog-cat-190709-800x450.jpg" height="400" width="400" alt="">

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
    
  }

  
</style>