[x,y,z]=sphere;
subplot(2,2,1)
surf(4*x,4*y,4*z)
axis equal
title('马智博2502910129 半径为四的球面')
t=0:pi/20:2*pi;
[x,y,z]=cylinder(2+sin(t),30);
subplot(2,2,2)
surf(x,y,z)
title('马智博2502910129 边界为正弦曲面')
[x,y,z]=peaks(30);
subplot(2,1,2)
surf(x,y,z)
title('马智博2502910129 多峰函数')