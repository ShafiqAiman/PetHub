<template>
    <div id="toastNotice">
        <div class="toastHeader">
            <slot name="header">
                
            </slot>
            <small>
                1 minute ago
            </small>
        </div>
        <button type="button" class="ml-2 mb-1 close" data-dismiss="toast">
            <span>&times;</span>
        </button>
        <div class="toastBody">
            <slot name="body">
            </slot>
        </div>
    </div>
</template>

<script>
export default {
    name:'Toast',
}


</script>

<style scoped>

</style>