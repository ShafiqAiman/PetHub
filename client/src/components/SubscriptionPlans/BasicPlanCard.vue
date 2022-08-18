<template>
    <div class="cardBackground">
        <div class="cardHeader">
            <h2>
                Basic
            </h2>
        </div>
        <div class="cardBody">
            <ul>
                <li style="list-style:none">
                    <p>RM30 for <br> 3 months</p>
                </li>
            </ul>
        </div>
        <div class="cardFooter">
            <button total=30 @click="selectedplan">
                Start Now
            </button>
        </div>
    </div>
</template>
<script>
export default {
    name:'BasicPlanCard',
    component:
    {
        
    },
    data()
    {
        return{
            total:30
        }
    },
    methods:
    {
        selectedplan(){
            localStorage.total = this.total;
            this.$router.push('/leaseproperty');
            // this.$router.push({path: '/leasepayment', query: {total: this.total}})
        },
        
    },
}
</script>

<style scoped>
.cardBackground{
    box-shadow:  0 0 40px  rgb(163, 163, 163);
    width: 85%;
    height: 90%;
    padding: 20px;
    text-align: center;
    margin: 20px;
    border-radius: 5px;
    border-top-style: solid;
    border-top-width: 6px;
    border-top-color: #61CAC8;
}
.cardBody{
    padding-top: 50px;
    /* height: 90px; */
}
.cardFooter{
    padding-top: 40%;
}
button{
    padding: 5px 50px;
    border-radius: 5px;
    border-width: 0px;
    background-color: #61CAC8;
    font-weight: 400;
    height: 50px;
    width: 90%;
}
button:hover{
    background-color: #61cac8ab;
    color: rgba(0, 0, 0, 0.925);
}
h2, p{
    font-family: "Montserrat", sans-serif;
}
</style>