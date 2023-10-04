var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
       var product1Id = this.dataset.product1
       var action = this.dataset.action
       console.log('product1Id:', product1Id, 'action:', action)

       console.log('User:' , user)
       if(user === 'AnonymousUser'){
           console.log('Not logged in')
       }
       else
       {
         updateUserOrder(product1Id,action)
       }
   })
}
function updateUserOrder(product1Id,action){
      console.log('User is logged in')

      var url = 'updateItem'
      fetch(url,{
          method:'POST',
          headers:{
               'Content-Type':'application/json',
               'X-CSRFToken':csrftoken,

          },
          body:JSON.stringify({'product1Id':product1Id, 'action': action})

      })

      .then((response) =>{
            return response.json()
      })
      .then((data) =>{
            console.log('data:', data)
            location.reload()
      })
}