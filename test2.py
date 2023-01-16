<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="static/bootstrap.css" />
    <link rel="stylesheet" href="/static/mycss.css" />
    <style>

      .wrapper{
        height: 50px;
        min-width: 180px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #FFF;
        border-radius: 12px;
        box-shadow: 0 5px 10px rgba(0,0,0,0.2);
      }
      .wrapper span{
        width: 100%;
        text-align: center;
        font-size: 30px;
        font-weight: 600;
        cursor: pointer;
        user-select: none;
      }
      .wrapper span.num{
        font-size: 30px;
        border-right: 2px solid rgba(0,0,0,0.2);
        border-left: 2px solid rgba(0,0,0,0.2);
        pointer-events: none;
      }

    </style>
  </head>

  <body>
    <nav class="navbar navbar-expand-lg bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Navbar</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Link</a>
            </li>
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle"
                href="#"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                Dropdown
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
                <li><hr class="dropdown-divider" /></li>
                <li>
                  <a class="dropdown-item" href="#">Something else here</a>
                </li>
              </ul>
            </li>
            <li class="nav-item">
              <a class="nav-link disabled">Disabled</a>
            </li>
          </ul>
          <form class="d-flex" role="search">
            <input
              class="form-control me-2"
              type="search"
              placeholder="Search"
              aria-label="Search"
            />
            <button class="btn btn-outline-success mx-2" type="submit">
              Search
            </button>
          </form>
          <span class="me-2"> Welocome <strong>{{user}}</strong> </span>
        </div>

        <span>
          <a href="{% url 'logouthandle' %}">
            <button type="button" class="btn btn-success mx-1">Logout</button>
          </a>
        </span>
      </div>
    </nav>

    {% for message in messages %}
    <div
      class="alert alert-{{message.tags}} mb-1 alert-dismissible fade show"
      role="alert"
    >
      <strong>Message!</strong> {{message}}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>
    {% endfor %}
    <div style="display: flex; flex-wrap:wrap;" >
    {% for item in items %}

    <div class="card m-2" style="width: 15rem;">
      <img src='/media/{{item.item_img}}'  class="card-img-top h-50"  alt="...">
      <div class="card-body">
      <h3>{{item.item_name}}</h3>
      <h5>Rs {{item.item_price}}</h5>  
      </div>

      <div class="wrapper">
        <span class="minus">-</span>
        <span class="num" name="quant">0</span>
        <span class="plus">+</span>
      </div>

  </div>
  {% endfor %}
</div>
    
    <script src="/static/js/jquery.js"></script>
    <script src="/static/js/bootstrap.js"></script>

    <script>
      const plus = document.querySelector(".plus"),
       minus = document.querySelector(".minus"),
       num = document.querySelector(".num");
       let a = 0;
       plus.addEventListener("click", ()=>{
         a++;
         a = (a < 10) ? + a : a;
         num.innerText = a;
       });
   
       minus.addEventListener("click", ()=>{
         if(a > 0){
           a--;
           a = (a < 10) ? + a : a;
           num.innerText = a;
         }
       });
   
     </script>
    
  </body>
</html>
