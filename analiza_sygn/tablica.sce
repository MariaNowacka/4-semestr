wiel = poly(b,"r", 'coeff')/poly(a,'r', 'coeff');
z = roots(poly, (b, "z", 'coeff'));
p = roots(poly, (a, "a", 'coeff'));
wiel = poly(poly(z, "z", 'roots'));
b = coeff(poly(z, "z", 'roots'));
a = coeff(poly(p, "r", 'roots'));
HF = atan(imag(H), real(H));
H = freq(wiel("num"), wiel('den'), w);
