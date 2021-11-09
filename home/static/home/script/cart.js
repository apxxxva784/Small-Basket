document.addEventListener('DOMContentLoaded', () => {
    const addToCartBtns = document.querySelectorAll('.add_to_cart_btn');
    const deleteBtns = document.querySelectorAll('.delete_btn');


    const getCookie = (name) => {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
            }
          }
        }
        return cookieValue;
      }
    
      const csrftoken = getCookie('csrftoken');


    const addToCart = (e, isInCart) => {
        let id = e.target.dataset.id;
  
        const formData = new FormData();
        formData.append("id", id);

        fetch('/cart/add_to_cart/', {
            method: 'POST',
            body: formData,
            headers: {
              'X-CSRFToken': csrftoken
            }
          })
          .then(res => res.json())
        .then(data => {
          if (data.status === 200) {
              alert("You must sign in to access this feature!");
          }
        });
    }

    const removeCart = (e, isInCart) => {
        let id = e.target.dataset.id;
  
        const formData = new FormData();
        formData.append("id", id);

        fetch('/cart/remove_from_cart/', {
            method: 'POST',
            body: formData,
            headers: {
              'X-CSRFToken': csrftoken
            }
          })

        };

    addToCartBtns.forEach((btn) => {
        btn.addEventListener('click', function (e) {
        addToCart(e, false);
        })
    });

    deleteBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
          removeCart(e);
        })
      });

});