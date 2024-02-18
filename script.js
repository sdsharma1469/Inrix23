fetch("filtered_data.json")
.then(function(response){
   return response.json();
})
.then(function(products){
   let placeholder = document.querySelector("#data-output");
   let out = "";
   for(let product of products){
      out += `
         <tr>
            <td> <img src='${product.Address}'> </td>
            <td>${product.type}</td>
            <td>${product.Size}</td>
            <td>${product.Rate}</td>
            <td>${product.Price}</td>
         </tr>
      `;
   }
 
   placeholder.innerHTML = out;
});
