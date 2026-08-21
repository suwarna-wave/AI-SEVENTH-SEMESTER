% Earthquake-Burglary Alarm Network in ProbLog

% Independent prior probabilities
0.001::burglary.
0.002::earthquake.

% P(Alarm | Burglary, Earthquake)
0.950::alarm :- burglary, earthquake.
0.940::alarm :- burglary, \+earthquake.
0.290::alarm :- \+burglary, earthquake.
0.001::alarm :- \+burglary, \+earthquake.

% P(Calls | Alarm)
0.90::john_calls :- alarm.
0.05::john_calls :- \+alarm.
0.70::mary_calls :- alarm.
0.01::mary_calls :- \+alarm.

% Observed evidence: both neighbors called.
evidence(john_calls, true).
evidence(mary_calls, true).

% Find P(Burglary | JohnCalls=true, MaryCalls=true).
query(burglary).
