
import time

print('Configuring motor from scratch ...')
input_velocity = 40

odrv = dev0

odrv.axis0.motor.config.pole_pairs = 7

odrv.axis0.motor.config.motor_type = MOTOR_TYPE_GIMBAL

odrv.axis0.config.enable_sensorless_mode = True
odrv.axis0.motor.config.pre_calibrated = True

#Configure ramp
odrv.axis0.config.sensorless_ramp.current = 3   
odrv.axis0.config.sensorless_ramp.accel = 100.0     # Moderate acceleration 
odrv.axis0.config.sensorless_ramp.vel = 300.0  

# Configure motor and controller parameters
odrv.axis0.motor.config.phase_resistance = 6.5

odrv.axis0.motor.config.current_lim = 20.0 # This seems to have the most impact
odrv.axis0.motor.config.requested_current_range = 20.0

odrv.axis0.sensorless_estimator.config.pm_flux_linkage = 0.005

odrv.config.max_regen_current = -10
odrv.config.dc_max_negative_current = -10
odrv.config.dc_max_positive_current = 10

odrv.axis0.motor.config.resistance_calib_max_voltage = 5

odrv.axis0.controller.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL
odrv.axis0.controller.config.input_mode = INPUT_MODE_PASSTHROUGH

odrv.axis0.controller.config.vel_gain = 0.02
odrv.axis0.controller.config.vel_integrator_gain = 0
# odrv.axis0.controller.config.vel_integrator_limit = inf
odrv.axis0.controller.config.vel_limit = 1000
odrv.axis0.controller.config.vel_limit_tolerance = 1.2
odrv.axis0.controller.config.vel_ramp_rate = 1


odrv.config.brake_resistance = 0

print('Setting to speed control closed loop ...')

odrv.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

print('Rampup delay ...')

time.sleep(8) # give the motor time to spin up?

print('Setting to fast speed ...')

# Command desired velocity (in turns per second)
odrv.axis0.controller.input_vel = input_velocity


