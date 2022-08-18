<template>
  <transition name="modal-fade">
    <div class="modal-backdrop">
      <div class="modal modal-content"
        role="dialog" aria-labelledby="modalTitle" aria-describedby="modalDescription">

        <div class="modal-header">
          <h2 class="modal-title" id="exampleModalLongTitle">Filter</h2>
          <button type="button" class="close" @click="$emit('close', property, room, wifi, parking, gym, furnished, airconditioned, swimmingpool, minBudget, maxBudget, smoking, pet, children)" aria-label="Close modal" >
            <span aria-hidden="true">&times;</span>
          </button>
        </div>

        <h3 class="modalsection">House Preferences</h3>
        <section class="modal-body" id="modalDescription">
          
          <div class="filter">
            <h5>Type of Pet: </h5>
            <input type="radio" value="Entire Place" v-model="property" id="entire"/>
            <label style="margin-left:1%" for="entire">Cat</label><br>

            <input type="radio" value="Private Room" v-model="property"  id="privateroom"/>
            <label style="margin-left:1%" for="privateroom">Dog</label><br>

            <input type="radio" value="Shared Room" v-model="property" id="sharedroom"/>
            <label style="margin-left:1%" for="sharedroom">Turtle</label><br>

            <input type="radio" value="Shared Room" v-model="property" id="sharedroom"/>
            <label style="margin-left:1%" for="sharedroom">Fish</label><br>

            <input type="radio" value="Shared Room" v-model="property" id="sharedroom"/>
            <label style="margin-left:1%" for="sharedroom">Rabbit</label><br>

            <input type="radio" value="" v-model="property" id="propertynope"/>
            <label style="margin-left:1%" for="propertynope">I don't mind</label>
          </div>
          
          <div class="filter">
            <h5>Pet Status : </h5>
            <input type="radio" value="Master Bedroom" v-model="room"  id="masterroom"/>
            <label style="margin-left:1%" for="masterroom">Adopted</label><br>

            <input type="radio" value="Middle Bedroom" v-model="room"  id="middleroom"/>
            <label style="margin-left:1%" for="middleroom">Looking for a new Guardian</label><br>


            <input type="radio" value="" v-model="room" id="rnope"/>
            <label style="margin-left:1%" for="rnope">I don't mind</label>
          </div>

          <div class="filter">
            <h5>Health Status:</h5>
            <input type="radio" value="Male" v-model="gender"  id="male"/>
            <label style="margin-left:1%" for="male">Healthy</label><br>

            <input type="radio" value="Female" v-model="gender" id="female"/>
            <label style="margin-left:1%" for="female">Sick</label><br>

            <input type="radio" value="" v-model="gender"  id="gnope"/>
            <label style="margin-left:1%" for="gnope">I don't mind</label><br>

          </div>

          <div class="filter">
            <h5>Health Status:</h5>
            <input type="radio" value="Male" v-model="gender"  id="male"/>
            <label style="margin-left:1%" for="male">Healthy</label><br>

            <input type="radio" value="Female" v-model="gender" id="female"/>
            <label style="margin-left:1%" for="female">Sick</label><br>

            <input type="radio" value="" v-model="gender"  id="gnope"/>
            <label style="margin-left:1%" for="gnope">I don't mind</label><br>

          </div>

          
          
        </section>
        <div class="modal-footer filterbtns">
          <button type="button" class="filter-btn" @click="$emit('close', property, room, wifi, parking, gym, furnished, airconditioned, swimmingpool, minBudget, maxBudget, gender, occupation, orientation, pet, age, smoking, religion, children)" aria-label="Close modal">
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
        property:'',
        room:'',
        wifi:'',
        parking:'',
        gym:'',
        furnished:'',
        airconditioned:'',
        swimmingpool:'',
        minBudget:0,
        maxBudget:100000,
        gender:'',
        occupation:'',
        orientation:'',
        religion:'',
        age: '',
        smoking:'',
        children:'',
        pet:''
      }
    },
    methods: {
      reset() {
        this.property = '';
        this.room = '';
        this.wifi='';
        this.parking='';
        this.gym='';
        this.furnished='';
        this.airconditioned='';
        this.swimmingpool='';
        this.minBudget=0;
        this.maxBudget=100000;
        this.gender = '';
        this.occupation = '';
        this.orientation = '';
        this.religion='',
        this.age='';
        this.smoking='';
        this.children='';
        this.pet='';
        confirm("All filters are cleared! Please click 'Apply Filters' to proceed")
      },
      
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