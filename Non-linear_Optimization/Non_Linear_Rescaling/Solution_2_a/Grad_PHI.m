function [ output_args ] = Grad_PHI( x,y,k )

    x1 = x(1);
    x2 = x(2);
    grad_psik = psik(x,y,k);
    
    grad_phi1 = 2 + 2*x1*y*grad_psik(2);
    grad_phi2 = -3 + 2*x2*y*grad_psik(2);
    
    output_args = [grad_phi1;grad_phi2];

end

