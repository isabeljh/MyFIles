function [finalscore, scorekey, amplitude, counts, line_length] = scoring(bins,data, amp, timeco, lineleng)
%SCORING Summary of this function goes here
%   Detailed explanation goes here
bool2 = 1;
counts = 0;
for trial = [1:1:3]
    for i = [2:length(bins)]
        x = data(trial,bins(i-1): bins(i));
        %amplitude
        amplitude(i, trial) = max(x) - min(x);
        if amplitude(i, trial) >= amp %orig: 3100
            score(i,1, trial) = 1;
        else 
            score(i,1, trial) = 0;
        end
            %zero crossings
        time_count = 0;

        for j = x
            bool1 = j<=0;
            if bool1 ~= bool2
                time_count = time_count+1;
            end
            bool2 = bool1; 
        end
        if time_count <= timeco %orig: 250
            score(i,2, trial) = 0;
        else
            score(i,2, trial) = 0;
        end
        counts(i, trial) = time_count;

        %line length
        line_length(i, trial) = sum(abs(diff(x)));
        if line_length(i, trial) >= lineleng %orig: 30z000
            score(i,3, trial) = 1;
        else
            score(i,3, trial) = 0;
        end
        if sum(score(i,:, trial),2) >= 2
            %disp("seizure at " + bins(i-1) + " seconds")
            finalscore(i, trial) = 1;
        else
            finalscore(i, trial) = 0;
        end
    end    
end
for i = [2:length(finalscore)]
    if sum(finalscore(i, :), 2) >=1
        scorekey(i) = 1;
    else
        scorekey(i) = 0;
    end
end   
