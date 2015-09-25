function [ output_args ] = AL3_Hessian(  x,y,k )
    x1 = x(1); x2 = x(2); x3 = x(3); x4  = x(4);
    y1 = y(1);y2 = y(2);
    output_args = [ 18*x1 - 2*y1 + k* (x1^2 + x2^2 + x3^2 + x4^2 - 4)*2 + k*2*x1*2*x1 + k,k*2* (x2)*2*x1 + k,  k*2* (x3)*2*x1 + k*2,k*2* (x4)*2*x1 + k*3;
k*2* (x1)*2*x2 + k, 12*x2 - 2*y1 + k* (x1^2 + x2^2 + x3^2 + x4^2 - 4)*2 + k*2*x2*2*x2 + k, k*2* (x3)*2*x2 + k*2, k*2* (x4)*2*x2 + k*3;
k*2* (x1)*2*x3 + k*2,k*2* (x2)*2*x3 + k*2, 6*x3 - 2*y1 + k* (x1^2 + x2^2 + x3^2 + x4^2 - 4)*2 + k*2*x3*2*x3 + k*2*2,k*2* (x4)*2*x3 + k*2*3;
k*2* (x1)*2*x4 + k*3,k*2* (x2)*2*x4 + k*3,k*2* (x3)*2*x4 + k*3*2,6*x4 - 2*y1 + k* (x1^2 + x2^2 + x3^2 + x4^2 - 4)*2 + k*2*x4*2*x4 + k*3*3];

end