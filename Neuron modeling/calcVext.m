function [voltageTRACE] = calcVext(currentTrace, currentXYZ, electrodeXYZ)
%CALCVEXT Summary of this function goes here
%  
sigma = 3.333E-7;
r = sqrt((electrodeXYZ(1,1)+ currentXYZ(:,1)).^2+(electrodeXYZ(1,2)+currentXYZ(:,2)).^2+(electrodeXYZ(1,3)+currentXYZ(:,3)).^2);
k = find(~r);
r(k) = 1000;
currentTrace(k) = 0;
voltageTRACE = (currentTrace)./(4*pi*sigma.*r);



end

