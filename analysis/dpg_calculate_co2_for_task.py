
import numpy as np

start_time = 18
end_time = 54
runtime = end_time - start_time
energy_runtime = 3*runtime
co2_timesteps = [[6, 90], [18, 30], [24, 60], [30, 85], [36, 25], [48, 70]]

# np_co2_timesteps_base = np.array(co2_timesteps)

last_co2timestep = co2_timesteps[len(co2_timesteps)-1][0]
end_time_phase = end_time // last_co2timestep + 1

co2_consumption = 0.0

co2_per_timestep = energy_runtime / runtime

co2_timeline = np.array(co2_timesteps)
# Build the timeline
for idx in np.arange(1, end_time_phase):
    co2_timeline = np.append(co2_timeline, np.add(co2_timesteps, [last_co2timestep*idx, 0]), axis=0)

start_idx = np.where(co2_timeline[:, 0] > start_time)[0][0]
end_idx = np.where(co2_timeline[:,0] <= end_time)[0][-1]+2
co2_timeline_slice = co2_timeline[start_idx:end_idx]

co2_timeline_slice = np.concatenate(([co2_timeline_slice[0]], co2_timeline_slice), axis=0)
co2_timeline_slice[0][0] = start_time
co2_timeline_slice[-1][0] = end_time

diffTime1 = np.diff(co2_timeline_slice[:, 0])
diffTime = np.concatenate(([0], diffTime1))
co2_csp_periods = np.multiply(diffTime, co2_timeline_slice[:, 1]/100)*co2_per_timestep
co2_consumption = np.sum(co2_csp_periods)

print([runtime, diffTime, co2_timeline_slice, co2_consumption])


