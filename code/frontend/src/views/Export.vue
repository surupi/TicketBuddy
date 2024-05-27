<template>
<div>
    <h1>We can use Export Page to create csv file</h1>
    <button class="btn btn-primary">Send mail</button>
</div>
</template>

<script>
export default {
    name: 'exp-ort',
    
    methods:{
        async getCsv(){
            const userid=localStorage.getItem('user_id')
            const res=await fetch(`http://127.0.0.1:5000/api/csvquer/${userid}`,{
                method:"GET",
                headers:{
                    "Content-Type":"application/json",
                    "Authentication-Token":localStorage.getItem('auth-token'),
                },
            })
            if (res.ok){
                console.log(res)
            }
            else{
                console.log('Something went wrong')
            }
        },
      },
}
</script>

<style>

</style>