CREATE TABLE experiments (
    trial_id INTEGER PRIMARY KEY,
    launch_angle REAL,
    initial_velocity REAL
);

CREATE TABLE measurements (
    trial_id INTEGER PRIMARY KEY,
    flight_time REAL,
    range_x REAL,
    max_height REAL,
    FOREIGN KEY (trial_id) REFERENCES experiments(trial_id)
);

CREATE TABLE model_results (
    trial_id INTEGER PRIMARY KEY,
    theoretical_range REAL,
    residual REAL,
    absolute_error REAL,
    percent_error REAL,
    FOREIGN KEY (trial_id) REFERENCES experiments(trial_id)
);
