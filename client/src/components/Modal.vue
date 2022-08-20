<template>
  <transition name="modal-fade">
    <div class="modal-backdrop">
      <div class="modal modal-content"
        role="dialog" aria-labelledby="modalTitle" aria-describedby="modalDescription">

        <div class="modal-header">
          <h2 class="modal-title" id="exampleModalLongTitle">Filter</h2>
          <button type="button" class="close" @click="$emit('close', typeOfPet, petStatus, healthStatus, petAge, minage)" aria-label="Close modal" >
            <span aria-hidden="true">&times;</span>
          </button>
        </div>

        <h3 class="modalsection">Pet Preferences</h3>
        <section class="modal-body" id="modalDescription">
          
          <div class="filter">
            <h5>Type of Pet: </h5>
            <input type="radio" value="Cat" v-model="typeOfPet" id="cat"/>
            <label style="margin-left:1%" for="cat">Cat</label><br>

            <input type="radio" value="Dog" v-model="typeOfPet"  id="dog"/>
            <label style="margin-left:1%" for="dog">Dog</label><br>

            <input type="radio" value="Turtle" v-model="typeOfPet" id="turtle"/>
            <label style="margin-left:1%" for="turtle">Turtle</label><br>

            <input type="radio" value="Fish" v-model="typeOfPet" id="fish"/>
            <label style="margin-left:1%" for="fish">Fish</label><br>

            <input type="radio" value="Rabbit" v-model="typeOfPet" id="rabbit"/>
            <label style="margin-left:1%" for="rabbit">Rabbit</label><br>

            <input type="radio" value="" v-model="typeOfPet" id="typepetnope"/>
            <label style="margin-left:1%" for="typepetnope">I don't mind</label>
          </div>
          
          <div class="filter">
            <h5>Pet Status : </h5>
            <input type="radio" value="Adopted" v-model="petStatus"  id="adopted"/>
            <label style="margin-left:1%" for="adopted">Adopted</label><br>

            <input type="radio" value="Looking for a new Guardian" v-model="petStatus"  id="lookguardian"/>
            <label style="margin-left:1%" for="lookguardian">Looking for a new Guardian</label><br>


            <input type="radio" value="" v-model="petStatus" id="petstatusnope"/>
            <label style="margin-left:1%" for="petstatusnope">I don't mind</label>
          </div>

          <div class="filter">
            <h5>Health Status:</h5>
            <input type="radio" value="Healthy" v-model="healthStatus"  id="healthy"/>
            <label style="margin-left:1%" for="male">Healthy</label><br>

            <input type="radio" value="Sick" v-model="healthStatus" id="sick"/>
            <label style="margin-left:1%" for="female">Sick</label><br>

            <input type="radio" value="" v-model="healthStatus"  id="healthnope"/>
            <label style="margin-left:1%" for="healthnope">I don't mind</label><br>

          </div>

          <div class="filter">
            <h5>Pet Age:</h5>
            <input type="radio" value=3 v-model="petAge" @change="MinAge" id="three"/>
            <label style="margin-left:1%" for="three">1 - 3</label><br>

            <input type="radio" value=6 v-model="petAge" @change="MinAge" id="six"/>
            <label style="margin-left:1%" for="six">4 - 6</label><br>

            <input type="radio" value=500 v-model="petAge" @change="MinAge" id="moresix"/>
            <label style="margin-left:1%" for="moresix">> 6</label><br>

            <input type="radio" value=1000 v-model="petAge" @change="MinAge"  id="agenope"/>
            <label style="margin-left:1%" for="agenope">I don't mind</label><br>

          </div>

          
          
        </section>
        <div class="modal-footer filterbtns">
          <button type="button" class="filter-btn" @click="$emit('close', typeOfPet, petStatus, healthStatus, petAge, minage)" aria-label="Close modal">
              Apply Filters
          </button>
          <button type="button" style="background-color:red;color:white;" class="filter-btn" @click="reset"  aria-label="Close modal">
              Clear Filters
          </button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
  export default {
    name: 'Modal',
    data(){
      return{
        typeOfPet:'',
        petStatus:'',
        healthStatus:'',
        petAge: 1000,
        minage:0,
        
      }
    },
    methods: {
      reset() {
        this.typeOfPet = '';
        this.petStatus = '';
        this.healthStatus = '';
        this.petAge = 1000
        confirm("All filters are cleared! Please click 'Apply Filters' to proceed")
      },
      MinAge(){
        if (this.petAge == 3){
          this.minage = 0;
        }else if (this.petAge == 6){
          this.minage = 4;
        }else if (this.petAge == 500){
          this.minage = 7;
        }else{
          this.minage = 0;
        }
      }
      
    },
  };
</script>

<style scoped>

  .modalsection{
    text-align: center;
  }
  
  .filterbtns{
    /* display: flex;
    flex-wrap: wrap; */
    justify-content: center;
    /* margin-bottom: 15px; */
  }

  .modal-backdrop {
    position: fixed;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal { 
    background: #FFFFFF;
    max-width: 55%;
    min-width: 280px;
    max-height: 80%;
    /* margin-left:20%; */
    margin-top: 5%;
    box-shadow: 2px 2px 20px 1px;
    border-radius: 15px;
    /* display: inherit; */
    flex-direction: column;
    overflow-y: auto;
    padding: 7px; 
  }

  .modal-header,
  .modal-footer {
    padding: 15px;
    display: flex;
  }

  .modal-header {
    position: relative;
    border-bottom: 1px solid #eeeeee;
    color: #175B5B;
    justify-content: space-between;
  }

  .modal-body {
      padding-top: 0;
      padding-bottom: 1%;
      display: flex;
      width: 90%;
      flex-wrap: wrap;
      margin: auto;
      justify-content: space-evenly;
  }

  .filter{
    margin-top: 1%;
    width: 250px;
    max-height: 500px;
    margin: 2%;
    text-align:left;
  }

  .filter-btn {
    margin-top: 10px;
    background-color:#fbd864;
    height: 50px;
    width: 100px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-sizing: border-box;
    padding: 5px;
    margin: 2%;
  }

  .modal-fade-enter,
  .modal-fade-leave-to {
    opacity: 0;
  }

  .modal-fade-enter-active,
  .modal-fade-leave-active {
    transition: opacity .5s ease;
  }
</style>