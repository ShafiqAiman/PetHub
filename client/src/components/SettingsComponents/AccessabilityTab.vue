<template>
    <div class="AccessabilityChangingTab">
        <br>
        <h2>Language Select</h2>
        <br>
        <select v-model="languageSelect" style="height:40px; border-radius: 4px;">
            <option disbale value="">
                Please select one: 
            </option>
            <option value="">
                English
            </option>
            <option value="">
                French
            </option>
            <option value="">
                Bahasa Malaysia
            </option>
        </select>
        <br>
        <button id="confirmButton" @click="selectLang(languageSelect)">Confirm Language</button>
    </div>
</template>

<script>
export default {
    name:'Accessability',

data()
    {
        return{
            language:'',
            languageSelect:''
        }
        
    },

methods: 
{
    selectLang(language)
    {
        this.language = language
        console.log(language)
        alert("LanguageChanged");
    }
},
}
</script>

<style scoped>
.AccessabilityChangingTab
{
     display: block;
    margin: 0 auto;
    margin-top: 10px;
    background-color: rgb(255, 255, 255);
    width:50%;
    border-radius: 8px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

#confirmButton
{
     margin-top: 20px;
        padding: 9px;
        border: none;
        width: 300px;
        margin-bottom: 10px;
        border-radius: 5px;
        background-color: rgb(170, 217, 247);
}

button:hover
{
    background-color: rgb(236, 243, 247);
    color: white;
}
</style>