## Проектная работа "Шутер"
Проект написан на языке Python
random, pygame — используемые библиотеки

	class GameSprite(sprite.Sprite): - класс, наследуемый из класса Sprite метод sprite
    
Классы наследники GameSprite:

- Player
- Enemy
- Bullet

hero - экземпляр класса Player, является игроком. Двигается со скоростью 15p. Имеет размеры 400×420p. При нажатии на клавишу "K_SPACE" создается экземпляр класса Bullet с размерами 20×30p
background - фоновая картинка с размерами 800×500p  
monsters - экземпляры класса Enemy. Создается рандомное кол-во  объектов в диапазоне от 1 до 6, размеры от 80 до 520p, скорость от 1 до 5. 

#### Игровой цикл While:
В цикле происходит 
- отрисовка объектов
- проверяются событие нажатия на кнопку для управления Player
- добавляется счетчик убитых игроком monsters
- осуществляется метод update() для всех объектов(у каждого объекта свой метод с этим названием)
- осуществляется удаление monsters при столкновении спрайтов класса Enemy и Bullet
- осуществляется выигрыш(при убытых 10 monsters)
- осуществляется проигрыш(при пропущеных 3 monsters)

```
clock.tick(60) - установление FPS  
monsters.draw(window) - обновление положения```
