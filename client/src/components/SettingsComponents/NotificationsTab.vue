<template>
    <div class="NotificationsChangingTab">
        <br>
        <h2>Notifcation Alerts</h2>
            <div class="checkbox">
                <label>Promotions</label>
                <input type="checkbox" id="promo" value="1" v-model="notificationsSelection.promotions" style="margin-left:40px;"><br>
                <label>Property Updates</label>
                <input type="checkbox" id="propertyUpdates" value="1" v-model="notificationsSelection.propertyUpdates" style="margin-left:40px;"><br>
            </div>
            <button @click="changes()">Confirm Changes</button>
            <br>
            <br>

    </div>
</template>

<script>
export default {
    name:'NotificationsTab',
    data()
    {
        return{
            notificationsSelection:
            {
                promotions:0,
                propertyUpdates:0,
            }
        }
    },

    methods: {
        changes()
        {
            alert("Changes Confirmed.");
            console.log(this.notificationsSelection.promotions);
            console.log(this.notificationsSelection.propertyUpdates);
        }
    },
}
</script>

<style scoped>
.NotificationsChangingTab
{
       display: block;
    margin: 0 auto;
    margin-top: 10px;
    background-color: rgb(255, 255, 255);
    width:50%;
    border-radius: 8px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
.radio
{
    text-align: center;
}


button
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
    color: white;
}
</style>