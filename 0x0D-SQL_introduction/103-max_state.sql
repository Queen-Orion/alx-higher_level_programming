-- Import in hbtn_0c_0 this table dump
-- Displays max temperature of each state
SELECT state, max(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
