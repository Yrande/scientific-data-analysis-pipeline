-- Query 1: View the first 10 experiments

SELECT *
FROM experiments
LIMIT 10;

-- Query 2: Average experimental range by launch angle

SELECT
    e.launch_angle,
    AVG(m.range_x) AS average_range
FROM experiments AS e
JOIN measurements AS m
    ON e.trial_id = m.trial_id
GROUP BY e.launch_angle
ORDER BY e.launch_angle;

-- Query 3: Compare experimental range with theoretical range and error

SELECT
    e.trial_id,
    e.launch_angle,
    e.initial_velocity,
    m.range_x AS experimental_range,
    r.theoretical_range,
    r.absolute_error,
    r.percent_error
FROM experiments AS e
JOIN measurements AS m
    ON e.trial_id = m.trial_id
JOIN model_results AS r
    ON e.trial_id = r.trial_id
ORDER BY e.trial_id
LIMIT 10;

-- Query 4: Average absolute error by launch angle

SELECT
    e.launch_angle,
    AVG(r.absolute_error) AS average_absolute_error
FROM experiments AS e
JOIN model_results AS r
    ON e.trial_id = r.trial_id
GROUP BY e.launch_angle
ORDER BY e.launch_angle;

-- Query 5: Trials with the largest absolute errors

SELECT
    e.trial_id,
    e.launch_angle,
    e.initial_velocity,
    m.range_x AS experimental_range,
    r.theoretical_range,
    r.absolute_error,
    r.percent_error
FROM experiments AS e
JOIN measurements AS m
    ON e.trial_id = m.trial_id
JOIN model_results AS r
    ON e.trial_id = r.trial_id
ORDER BY r.absolute_error DESC
LIMIT 10;

-- Query 6: Overall model performance

SELECT
    AVG(m.range_x) AS average_experimental_range,
    AVG(r.theoretical_range) AS average_theoretical_range,
    AVG(r.absolute_error) AS mean_absolute_error
FROM measurements AS m
JOIN model_results AS r
    ON m.trial_id = r.trial_id;
    