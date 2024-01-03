document.addEventListener('DOMContentLoaded', function () {
    const ball = document.getElementById('ball');
    const basket = document.getElementById('basket');
    const shootBtn = document.getElementById('shoot-btn');

    shootBtn.addEventListener('click', function () {
        shootBall();
    });

    function shootBall() {
        const initialBallPosition = 100;
        const basketPosition = basket.offsetLeft + basket.offsetWidth / 2;
        const ballSpeed = 20;

        ball.style.bottom = initialBallPosition + 'px';

        setTimeout(function () {
            ball.style.bottom = '400px';
            ball.style.left = basketPosition + 'px';
        }, 10);

        setTimeout(function () {
            ball.style.bottom = '20px';
        }, 500);
    }
});
