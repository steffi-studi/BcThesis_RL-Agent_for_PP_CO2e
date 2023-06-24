"""
This file provides the EvaluationHandler class, which supports the evaluation of a model testing.
"""
import numpy as np


class EvaluationHandler:
    """
    This class keeps track of several environment parameters (e.g. makespan, tardiness) during a model testing.
    After a testing, you can call the evaluate_test function
    to compute evaluation metrics across all collected test episodes (e.g. mean, standard deviation).

    You can adapt evaluate_test to compute different or more metrics.
    """
    def __init__(self):
        #  test parameters. Valid for a complete test loop by one agent. Including multiple episodes
        self.rewards = []
        self.tardiness = []
        self.tardiness_max = []
        self.makespan = []  # number of steps required to end all jobs
        self.actions_list = []
        self.tasks_list = []
        self.co2_consumptions = []
        self.co2_consumptions_max = []

    def record_environment_episode(self, env, total_reward) -> None:
        """
        Stores all necessary environment parameters from the recent episode

        :param env: Non reset environment object, whose parameters should be recorded
        :param total_reward: Total reward of the episode

        :return: None

        """
        # append data from test run to list
        self.makespan.append(env.get_makespan())
        self.rewards.append(total_reward)
        self.tardiness.append(sum(env.tardiness))
        self.tardiness_max.append(max(env.tardiness))
        self.tasks_list.append(env.tasks)
        self.actions_list.append(env.action_history)
        self.co2_consumptions.append(sum(env.co2_consumptions))
        self.co2_consumptions_max.append(max(env.co2_consumptions))

    def update_episode_solved_with_solver(self, env) -> None:
        """
        Calculates all missing parameters of an environment processed by the solver

        :param env: Environment object with task attribute generated by the solver

        :return: None

        """
        # calculate tardiness
        env.calculate_tardiness()
        # prepare get_makespan function call
        for task in env.tasks:
            if task.finished > env.ends_of_machine_occupancies[task.selected_machine]:
                env.ends_of_machine_occupancies[task.selected_machine] = task.finished

        self.record_environment_episode(env, 0)

    def evaluate_test(self) -> dict:
        """
        Gets all test_parameter and computes all relevant statistical data for plots and prints

        :return: Dictionary with all specified evaluation metrics

        """
        rewards, tardiness, co2_consumptions = np.asarray(self.rewards), self.tardiness, self.co2_consumptions
        evaluation_results = {}
        evaluation_results['rew_mean'] = np.mean(rewards)
        evaluation_results['rew_std'] = np.std(rewards)
        evaluation_results['rew_best'] = np.max(rewards)
        evaluation_results['rew_best_count'] = sum([1 for el in rewards if el==evaluation_results['rew_best']])
        evaluation_results['rew_worst'] = np.min(rewards)
        evaluation_results['tardiness_mean'] = np.mean(tardiness)
        evaluation_results['tardiness_std'] = np.std(tardiness)
        evaluation_results['tardiness_max_mean'] = np.mean(self.tardiness_max)
        evaluation_results['co2_consumptions_mean'] = np.mean(co2_consumptions)
        evaluation_results['co2_consumptions_std'] = np.std(co2_consumptions)
        evaluation_results['co2_consumptions_max_mean'] = np.mean(self.co2_consumptions_max)
        evaluation_results['makespan_mean'] = np.mean(self.makespan)
        evaluation_results['rew_worst_quantile_border'] = np.quantile(rewards, 0.1)
        evaluation_results['rew_cvar'] = rewards[rewards <= evaluation_results['rew_worst_quantile_border']].mean()
        evaluation_results['rew_perc_good_solutions'] = 1 - np.count_nonzero(rewards)/len(rewards)
        evaluation_results['num_tests'] = len(rewards)

        return evaluation_results

    @classmethod
    def add_solver_gap_to_results(cls, results: dict) -> dict:
        """
        If solver makespan exists, compute optimal gap for all agents

        :param results: Dictionary with test results

        :return: Updated dictionary with test results now including optimal gap

        """
        if 'solver' in results:
            optimal_makespan = results['solver']['makespan_mean']
            for agent, result in results.items():
                gap = result['makespan_mean'] - optimal_makespan
                results[agent].update({'gap_to_solver': gap})
        return results
