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
            <h5>Property Type: </h5>
            <input type="radio" value="Entire Place" v-model="property" id="entire"/>
            <label style="margin-left:1%" for="entire">Entire Place</label><br>

            <input type="radio" value="Private Room" v-model="property"  id="privateroom"/>
            <label style="margin-left:1%" for="privateroom">Private Room</label><br>

            <input type="radio" value="Shared Room" v-model="property" id="sharedroom"/>
            <label style="margin-left:1%" for="sharedroom">Shared Room</label><br>

            <input type="radio" value="" v-model="property" id="propertynope"/>
            <label style="margin-left:1%" for="propertynope">I don't mind</label>
          </div>
          
          <div class="filter">
            <h5>Room : </h5>
            <input type="radio" value="Master Bedroom" v-model="room"  id="masterroom"/>
            <label style="margin-left:1%" for="masterroom">Master Bedroom</label><br>

            <input type="radio" value="Middle Bedroom" v-model="room"  id="middleroom"/>
            <label style="margin-left:1%" for="middleroom">Middle Bedroom</label><br>

            <input type="radio" value="Kitchen Bedroom" v-model="room" id="singleroom"/>
            <label style="margin-left:1%" for="singleroom">Single Bedroom</label><br>

            <input type="radio" value="" v-model="room" id="rnope"/>
            <label style="margin-left:1%" for="rnope">I don't mind</label>
          </div>
          
          <div class="filter">
            <h5>Amenities : </h5>
            <input type="checkbox" value="true" v-model="wifi" id="wifi"/>
            <label style="margin-left:1%" for="wifi">Wifi</label><br>

            <input type="checkbox" value="true" v-model="parking" id="parking"/>
            <label style="margin-left:1%" for="parking">Parking</label><br>

            <input type="checkbox" value="true" v-model="gym" id="gym"/>
            <label style="margin-left:1%" for="gym">Gym</label><br>

            <input type="checkbox" value="true" v-model="furnished" id="furnished"/>
            <label style="margin-left:1%" for="furnished">Furnished</label><br>

            <input type="checkbox" value="true" v-model="airconditioned" id="airconditioned"/>
            <label style="margin-left:1%" for="airconditioned">Air-conditioned</label><br>

            <input type="checkbox" value="true" v-model="swimmingpool" id="swimmingpool"/>
            <label style="margin-left:1%" for="swimmingpool">Swimming Pool</label>
          </div>

          <div class="filter">
            <h5>Monthly Rent : </h5>
            <div class="row">
              <div class="col" style="justify-content:center;">
                <label style="margin-left:1%" for="budget">Minimum</label><br>
                <input type="number" style=" width: 100px;" v-model="minBudget" id="minBudget"/>
              </div>

              <div class="col">
                <label style="margin-left:1%" for="budget">Maximum</label><br>
                <input type="number" style=" width: 100px;" v-model="maxBudget" id="maxBudget"/>
              </div>

            </div>
          </div>

          <div class="filter">
            <h5>Gender Friendly:</h5>
            <input type="radio" value="Male" v-model="gender"  id="male"/>
            <label style="margin-left:1%" for="male">Male</label><br>

            <input type="radio" value="Female" v-model="gender" id="female"/>
            <label style="margin-left:1%" for="female">Female</label><br>

            <input type="radio" value="" v-model="gender"  id="gnope"/>
            <label style="margin-left:1%" for="gnope">I don't mind</label><br>

          </div>

          <div class="filter">
            <h5>Occupation Friendly:</h5>
            <input type="radio" value="Student" v-model="occupation"  id="student"/>
            <label style="margin-left:1%" for="student">Student</label><br>

            <input type="radio" value="Working" v-model="occupation" id="working"/>
            <label style="margin-left:1%" for="working">Working</label><br>

            <input type="radio" value="Not Working" v-model="occupation" id="notworking"/>
            <label style="margin-left:1%" for="notworking">Not Working</label><br>

            <input type="radio" value="" v-model="occupation"  id="onope"/>
            <label style="margin-left:1%" for="onope">I don't mind</label><br>

          </div>

          <div class="filter">
            <h5>Orientation Friendly:</h5>
            <input type="radio" value="Straight" v-model="orientation"  id="straight"/>
            <label style="margin-left:1%" for="straight">Straight</label><br>

            <input type="radio" value="Gay" v-model="orientation" id="gay"/>
            <label style="margin-left:1%" for="gay">Gay</label><br>

            <input type="radio" value="Lesbian" v-model="orientation" id="lesbian"/>
            <label style="margin-left:1%" for="lesbian">Lesbian</label><br>

            <input type="radio" value="Bisexual" v-model="orientation" id="bisexual"/>
            <label style="margin-left:1%" for="bisexual">Bisexual</label><br>

            <input type="radio" value="" v-model="orientation"  id="ornope"/>
            <label style="margin-left:1%" for="ornope">I don't mind</label><br>

          </div>

          <div class="filter">
            <h5>Pet Friendly: </h5>
            <input type="radio" value="Yes" v-model="pet" id="yespet"/>
            <label style="margin-left:1%" for="yespet">Yes</label><br>

            <input type="radio" value="No" v-model="pet"  id="nopet"/>
            <label style="margin-left:1%" for="nopet">No</label><br>

            <input type="radio" value="" v-model="pet" id="pnope"/>
            <label style="margin-left:1%" for="pnope">I don't mind</label>
          </div>

          <div class="filter">
            <h5>Age Friendly : </h5>
            <input type="radio" value="18 - 25" v-model="age" id="age1"/>
            <label style="margin-left:1%" for="age1">18 - 25</label><br>

            <input type="radio" value="26 - 35" v-model="age"  id="age2"/>
            <label style="margin-left:1%" for="age2">26 - 35</label><br>

            <input type="radio" value="> 35" v-model="age"  id="age3"/>
            <label style="margin-left:1%" for="age3">> 35</label><br>

            <input type="radio" value="" v-model="age" id="anope"/>
            <label style="margin-left:1%" for="anope">I don't mind</label>
          </div>

          <div class="filter">
            <h5>Smoking Friendly : </h5>
            <input type="radio" value="Yes" v-model="smoking"  id="nosmoking"/>
            <label style="margin-left:1%" for="nosmoking">Yes</label><br>

            <input type="radio" value="No" v-model="smoking"  id="nosmoking"/>
            <label style="margin-left:1%" for="nosmoking">No</label><br>

            <input type="radio" value="" v-model="smoking" id="snope"/>
            <label style="margin-left:1%" for="snope">I don't mind</label>
          </div>

          <div class="filter">
            <h5>Religion Friendly : </h5>
            <input type="radio" value="Muslim" v-model="religion"  id="muslim"/>
            <label style="margin-left:1%" for="muslim">Muslim</label><br>

            <input type="radio" value="Buddha" v-model="religion" id="buddha"/>
            <label style="margin-left:1%" for="buddha">Buddha</label><br>

            <input type="radio" value="Hindu" v-model="religion"  id="hindu"/>
            <label style="margin-left:1%" for="hindu">Hindu</label><br>

            <input type="radio" value="Christian" v-model="religion" id="christian"/>
            <label style="margin-left:1%" for="christian">Christian</label><br>

            <input type="radio" value="" v-model="religion" id="rnope"/>
            <label style="margin-left:1%" for="rnope">I don't mind</label>
          </div>

          <div class="filter">
            <h5>Children Friendly : </h5>
            <input type="radio" value="Yes" v-model="children" id="yeschildren"/>
            <label style="margin-left:1%" for="yeschildren">Yes</label><br>

            <input type="radio" value="No" v-model="children"  id="nochildren"/>
            <label style="margin-left:1%" for="nochildren">No</label><br>

            <input type="radio" value="" v-model="children" id="cnope"/>
            <label style="margin-left:1%" for="cnope">I don't mind</label>
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
    width: 200px;
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