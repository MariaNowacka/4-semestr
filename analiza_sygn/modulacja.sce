T = 10;
N =10000;
dt = T/N;
t = 0:dt:3*T;
A = 1;
mod = t.^2;
x1 = squarewave(t);
x2 = x1.*t
x3 = sin(t);
// plot(t,x1, 'r',0, [-A-0.1, A+0.1]);
// plot(t, x2, 'g');
//plot(t,t);
x4 = x3.*mod
plot(t,x3, 'r');
plot(t, x4, 'black');
plot(t,mod);
