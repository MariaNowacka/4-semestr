// Przykład 2: znajdowanie zer i biegunów zadanej transmitancji
//z1 = 5; z2 = 15; 
//z = %i*[ -z2, -z1, z1, z2 ];
//odl = 0.5; p1 = 9.5; p2 = 10.5; 
j = %i
//p = [ -odl-%i*p2, -odl-j*p1, -odl+j*p1, -odl+j*p2 ];
//WMAX=20; TMAX=20;
//plot(real(p), imag(p),'xb'); grid;
//title('Zera (o) i bieguny (x)'); xlabel('Real'); ylabel('Imag [rd/s]');
// Przykład 1: projekt filtra pasmowoprzepustowego o wpass1 = 9.5 rd, wpass2 = 10.5 rd
//z1 = 0; //% ZERA na osi urojonej
//z2 = 0+j*1; z3 = 0-j*1; 
//z4 = 0+j*2; z5 = 0-j*2; 
//z6 = 0+j*3; z7 = 0-j*3; 
//z = [ z1 z2 z3 z4 z5 z6 z7 ]; 
//p1 = -1; //% BIEGUNY w pobliżu osi urojonej
//p2 = -1+j*1; p3 = -1-j*1; 
//p4 = -1+j*2; p5 = -1-j*2; 
//p6 = -1+j*3; p7 = -1-j*3; 
//p = [ p1 p2 p3 p4 p5 p6 p7 ]; 
//WMAX=20; TMAX=5;
//plot(real(z), imag(z),'xb'); 
//title('Zera (o) i bieguny (x)'); xlabel('’Real’'); ylabel('’Imag [rd/s]’');
//Przykład 3: projekt filtra górnoprzepustowego
z1 = 0; //% ZERA na osi urojonej
z2 = 0+j*1; z3 = 0-j*1; 
z4 = 0+j*2; z5 = 0-j*2; 
z6 = 0+j*3; z7 = 0-j*3; 
z = [ z1 z2 z3 z4 z5 z6 z7 ]; 
p1 = -1; //% BIEGUNY w pobliżu osi urojonej
p2 = -1+j*1; p3 = -1-j*1; 
p4 = -1+j*2; p5 = -1-j*2; 
p6 = -1+j*3; p7 = -1-j*3; 
p = [ p1 p2 p3 p4 p5 p6 p7 ]; 
WMAX=20; TMAX=5;
plot(real(z), imag(z)); 
title('’Zera (o) i bieguny (x)’'); xlabel('’Real’'); ylabel('’Imag [rd/s]’');
w = 0 : 0.01 : WMAX; //% wybrane pulsacje widma
[b,a] = zp2tf(z',p',1); //% zera, bieguny -> wspólczynniki wielomianów
H = freqs(b,a,w); //% wyznaczenie widma transmitancji dla zadanego w
Hm = abs(H); HmdB = 20*log10(Hm); //% moduł transmitancji
Hf = angle(H); Hfu = unwrap(Hf); //% faza transmitancji
plot(w,Hm,'k'); title('Ch-ka amplitudowa'); xlabel('w [rd/s]'); 
plot(w,HmdB,'k'); title('Ch-ka amplitudowa w dB'); xlabel('w [rd/s]'); 
plot(w,Hf,'k'); title('Ch-ka fazowa'); xlabel('w [rd/s]'); ylabel('[rd]'); 
plot(w,Hfu,'k'); title('Ch-ka fazowa unwrap'); xlabel('w [rd/s]'); ylabel('[rd]');
