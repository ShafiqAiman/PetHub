<template>
  <div class="autocomplete">
    <form style="width:100%;display:block;margin:0 auto;" @submit.prevent="setResult(search, false)">
      <input
          v-model="search"
          @keyup="typing"
          type="text"
          class="search1"
          
      />
    </form>
    
    <ul
        v-show="isOpen"
      class="autocomplete-results"
    >
      <li
        v-for="(result, i) in results"
        :key="i"
        @click="setResult(result, true)"
        class="autocomplete-result"
        
      >
        {{ result }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'SearchAutocomplete',
  props: {
    items: {
      type: Array,
      required: false,
      default: () => [],
    },
  },
  data() {
    return {
      search: '',
      // results: [],
      isOpen: false,
      status: false,
    };
  },
  mounted() {
    document.addEventListener('click', this.handleClickOutside);
  },
  destroyed() {
    document.removeEventListener('click', this.handleClickOutside);
  },
  methods: {
      setResult(data) {
        this.search = data;
        this.isOpen = false;
        this.$emit("selected", this.search);
        this.status = true;
      
    },
  
    typing(){
      this.status = false;
    },
    handleClickOutside(event) {
      if (!this.$el.contains(event.target)) {
        this.isOpen = false;
      }
    }
  }, computed:{
    results(){
      let filteredResults = new Set(this.items.filter(item => item.toLowerCase().indexOf(this.search.toLowerCase()) > -1));
      
      if(filteredResults.size != 0 && this.search != '' && this.status == false){
          this.isOpen = true;
          
      }else{
          this.isOpen = false;
      }

      return filteredResults
    }
  }
};
</script>

<style scoped>
  .autocomplete {
    padding: 0;
    width: 80%;
    
  }

  .autocomplete-results {
    position: absolute;
    padding: 0;
    margin: 0;
    border: 1px solid #eeeeee;
    height: 120px;
    min-height: 1em;
    max-height: 6em;
    overflow: auto;
    background-color: white;
    width: 500px;
  }

  .autocomplete-result {
    list-style: none;
    text-align: left;
    padding: 4px 2px;
    cursor: pointer;
  }

  .autocomplete-result:hover {
    background-color: #4AAE9B;
    color: white;
  }

  .search1
		{
    margin-top: 10px;
	  display: inline-block;
    padding: 8px;
	  width:100%;
    height:50px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-sizing: border-box;
		}
</style>