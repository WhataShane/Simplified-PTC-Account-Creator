$(document).ready(function(){
    $('.readmore').click(function(){
        $(".readmore").remove();
        $("h3").remove();
        $("h2").remove();
        var myElement = document.querySelector(".pokemon");
        myElement.style.WebkitAnimationPlayState = "running";
        myElement.style.animationPlayState = "running";
            $.post("http://localhost:8080", function(response) {
              myElement.style.WebkitAnimationPlayState = "paused";
              myElement.style.animationPlayState = "paused";
              $(".account1").append('<div>Username: '+response.Account.username+'</div>');
              $(".account2").append('<div>Password: '+response.Account.password)+'</div>';
            },'json');
    });
    });
