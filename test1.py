<div>
      <div>
        <h1 style="text-align:left ;">Italian</h1>
        {% for food in italian %}
        <div style="background-color:yellowgreen;width: 12%;height:20%
        ">
          <div>
            <img
              src="/media/{{food.item_img}}"
              width="100%"
              alt="..."
            />
        </div>
            <div>
              <h2>{{food.item_name}}</h2>
              <h4>Rs {{food.item_price}}</h4>
            </div>
          {% endfor %}
        </div>
      </div>
      <div style="background-color:rgb(50, 138, 205)">
        <h2>Breakfast</h2>
        {% for food in breakfast %}
        <div>
          <div style="width: 15rem">
            <img
              src="/media/{{food.item_img}}"
              
              width="100%"
              height="40%"
              alt="..."
            />
            <div >
              <h2>{{food.item_name}}</h2>
              <h4>Rs {{food.item_price}}</h4>
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
      <div>
        <h2>Pizza & Burgers</h2>

        {% for food in pizzaburger %}
        <div >
          <div style="width: 15rem">
            <img
              src="/media/{{food.item_img}}"
              
              width="100%"
              height="40%"
              alt="..."
            />
            <div >
              <h2>{{food.item_name}}</h2>
              <h4>Rs {{food.item_price}}</h4>
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
    </div>

    <!--        <div class="wrapper" style="width: 100%; height:10%;">
          <span class="minus" style="font-size:25px">-</span>
          <span class="num" style="font-size:25px" name="quant">0</span>
          <span class="plus" style="font-size:25px">+</span>
        </div>
  -->
