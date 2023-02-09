function [pattern, loc] = spikes(pattern,currents_big, xyz, locations)
%SPIKES Summary of this function goes here
%   Detailed explanation goes here
%locations = randperm(99,3);
loc = zeros(40000,3);

%pattern_ = zeros(40530,3)
for i = [1:length(pattern)]
    if pattern(i) == 1;
        pattern(i:(i+530),:) = currents_big;
        loc(i:(i+530),:) = (locations+xyz);
%     else if sqrt(locations(1,1).^2+locations(1,2).^2+locations(1,3).^2) < 25
%         pattern(i:(i+530),:) = 0;
%         loc(i:(i+530),:) = (locations+xyz);
    end
end
%loc = loc(1:40000, :);
if sqrt(locations.^2) <= 25
    pattern(:,:) = 0;    
end
end

