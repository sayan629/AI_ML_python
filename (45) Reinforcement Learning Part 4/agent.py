import flappy_bird_gymnasium
import gymnasium as gym

from dqn import DQN
from experience_replay import ReplayMemory

import itertools
import yaml
import torch
import torch.nn as nn
import torch.optim as optim
import random
import argparse
import os


# ============================================================
# DEVICE
# ============================================================

if torch.backends.mps.is_available():
    device = "mps"
elif torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

print(f"Using device: {device}")


# ============================================================
# DIRECTORIES
# ============================================================

RUNS_DIR = "runs"

os.makedirs(RUNS_DIR, exist_ok=True)


# ============================================================
# AGENT
# ============================================================

class Agent:

    def __init__(self, param_set):

        self.param_set = param_set

        # ----------------------------------------------------
        # Load parameters
        # ----------------------------------------------------

        with open("parameters.yaml", "r") as f:

            all_param_set = yaml.safe_load(f)

            if param_set not in all_param_set:
                raise ValueError(
                    f"Parameter set '{param_set}' not found "
                    f"in parameters.yaml"
                )

            params = all_param_set[param_set]

        # ----------------------------------------------------
        # Hyperparameters
        # ----------------------------------------------------

        self.alpha = params["alpha"]

        self.gamma = params["gamma"]

        self.epsilon_init = params["epsilon_init"]

        self.epsilon_min = params["epsilon_min"]

        self.epsilon_decay = params["epsilon_decay"]

        self.replay_memory_size = params["replay_memory_size"]

        self.mini_batch_size = params["mini_batch_size"]

        self.reward_threshold = params["reward_threshold"]

        self.network_sync_rate = params["network_sync_rate"]

        # ----------------------------------------------------
        # Loss function
        # ----------------------------------------------------

        self.loss_fn = nn.MSELoss()

        # Optimizer will be initialized after DQN creation
        self.optimizer = None

        # ----------------------------------------------------
        # File paths
        # ----------------------------------------------------

        self.LOG_FILE = os.path.join(
            RUNS_DIR,
            f"{self.param_set}.log"
        )

        self.MODEL_FILE = os.path.join(
            RUNS_DIR,
            f"{self.param_set}.pt"
        )


    # ========================================================
    # RUN
    # ========================================================

    def run(self, is_training=True, render=False):

        # ----------------------------------------------------
        # Create environment
        # ----------------------------------------------------

        env = gym.make(
            "FlappyBird-v0",
            render_mode="human" if render else None
        )

        # ----------------------------------------------------
        # Get state/action dimensions
        # ----------------------------------------------------

        num_states = env.observation_space.shape[0]

        num_actions = env.action_space.n

        print(f"Number of states : {num_states}")
        print(f"Number of actions: {num_actions}")

        # ----------------------------------------------------
        # Create policy network
        # ----------------------------------------------------

        policy_dqn = DQN(
            num_states,
            num_actions
        ).to(device)

        # ====================================================
        # TRAINING MODE
        # ====================================================

        if is_training:

            print("\nStarting training...\n")

            # ------------------------------------------------
            # Replay memory
            # ------------------------------------------------

            memory = ReplayMemory(
                self.replay_memory_size
            )

            # ------------------------------------------------
            # Initial epsilon
            # ------------------------------------------------

            epsilon = self.epsilon_init

            # ------------------------------------------------
            # Target network
            # ------------------------------------------------

            target_dqn = DQN(
                num_states,
                num_actions
            ).to(device)

            # Copy policy network weights
            target_dqn.load_state_dict(
                policy_dqn.state_dict()
            )

            # ------------------------------------------------
            # Training steps
            # ------------------------------------------------

            steps = 0

            # ------------------------------------------------
            # Optimizer
            # ------------------------------------------------

            self.optimizer = optim.Adam(
                policy_dqn.parameters(),
                lr=self.alpha
            )

            # ------------------------------------------------
            # Best reward
            # ------------------------------------------------

            best_reward = float("-inf")

        # ====================================================
        # TESTING MODE
        # ====================================================

        else:

            print("\nLoading trained model...\n")

            policy_dqn.load_state_dict(
                torch.load(
                    self.MODEL_FILE,
                    map_location=device
                )
            )

            policy_dqn.eval()

        # ====================================================
        # EPISODES
        # ====================================================

        for episode in itertools.count():

            # ------------------------------------------------
            # Reset environment
            # ------------------------------------------------

            state, info = env.reset()

            state = torch.tensor(
                state,
                dtype=torch.float32,
                device=device
            )

            # ------------------------------------------------
            # Episode variables
            # ------------------------------------------------

            episode_reward = 0

            done = False

            # =================================================
            # EPISODE LOOP
            # =================================================

            while (
                not done
                and episode_reward < self.reward_threshold
            ):

                # =============================================
                # ACTION SELECTION
                # =============================================

                # Exploration
                if (
                    is_training
                    and random.random() < epsilon
                ):

                    action = env.action_space.sample()

                    action = torch.tensor(
                        action,
                        dtype=torch.long,
                        device=device
                    )

                # Exploitation
                else:

                    with torch.no_grad():

                        action = (
                            policy_dqn(
                                state.unsqueeze(dim=0)
                            )
                            .squeeze()
                            .argmax()
                        )

                # =============================================
                # ENVIRONMENT STEP
                # =============================================

                (
                    next_state,
                    reward,
                    terminated,
                    truncated,
                    info
                ) = env.step(action.item())

                # Episode is finished if either happens
                done = terminated or truncated

                # =============================================
                # UPDATE REWARD
                # =============================================

                episode_reward += reward

                # =============================================
                # CONVERT NEXT STATE TO TENSOR
                # =============================================

                next_state = torch.tensor(
                    next_state,
                    dtype=torch.float32,
                    device=device
                )

                # =============================================
                # CONVERT REWARD TO TENSOR
                # =============================================

                reward = torch.tensor(
                    reward,
                    dtype=torch.float32,
                    device=device
                )

                # =============================================
                # STORE EXPERIENCE
                # =============================================

                if is_training:

                    memory.append(
                        (
                            state,
                            action,
                            next_state,
                            reward,
                            done
                        )
                    )

                    steps += 1

                # =============================================
                # MOVE TO NEXT STATE
                # =============================================

                state = next_state

            # =================================================
            # EPISODE COMPLETED
            # =================================================

            print(
                f"Episode: {episode + 1} "
                f"| Reward: {episode_reward} "
                f"| Epsilon: {epsilon:.4f}"
            )

            # =================================================
            # TRAINING UPDATES
            # =================================================

            if is_training:

                # ------------------------------------------------
                # Epsilon decay
                # ------------------------------------------------

                epsilon = max(
                    epsilon * self.epsilon_decay,
                    self.epsilon_min
                )

                # ------------------------------------------------
                # Save best model
                # ------------------------------------------------

                if episode_reward > best_reward:

                    log_msg = (
                        f"Best reward = {episode_reward} "
                        f"for episode = {episode + 1}"
                    )

                    print(log_msg)

                    # Write log
                    with open(
                        self.LOG_FILE,
                        "a"
                    ) as f:

                        f.write(
                            log_msg + "\n"
                        )

                    # Save model
                    torch.save(
                        policy_dqn.state_dict(),
                        self.MODEL_FILE
                    )

                    best_reward = episode_reward

            # =================================================
            # DQN OPTIMIZATION
            # =================================================

            if (
                is_training
                and len(memory) > self.mini_batch_size
            ):

                # ------------------------------------------------
                # Sample mini batch
                # ------------------------------------------------

                mini_batch = memory.sample(
                    self.mini_batch_size
                )

                # ------------------------------------------------
                # Optimize policy network
                # ------------------------------------------------

                self.optimize(
                    mini_batch,
                    policy_dqn,
                    target_dqn
                )

                # ------------------------------------------------
                # Sync target network
                # ------------------------------------------------

                if steps > self.network_sync_rate:

                    target_dqn.load_state_dict(
                        policy_dqn.state_dict()
                    )

                    steps = 0

        # ----------------------------------------------------
        # Environment close
        # ----------------------------------------------------

        # env.close()


    # ========================================================
    # OPTIMIZE
    # ========================================================

    def optimize(
        self,
        mini_batch,
        policy_dqn,
        target_dqn
    ):

        # ----------------------------------------------------
        # Extract experiences
        # ----------------------------------------------------

        states, actions, next_states, rewards, terminations = zip(
            *mini_batch
        )

        # ----------------------------------------------------
        # Convert to tensors
        # ----------------------------------------------------

        states = torch.stack(states)

        actions = torch.stack(actions)

        next_states = torch.stack(next_states)

        rewards = torch.stack(rewards)

        terminations = torch.tensor(
            terminations,
            dtype=torch.float32,
            device=device
        )

        # ====================================================
        # TARGET Q VALUES
        # ====================================================

        with torch.no_grad():

            target_q = (
                rewards
                + self.gamma
                * (1 - terminations)
                * target_dqn(next_states)
                .max(dim=1)[0]
            )

        # ====================================================
        # CURRENT Q VALUES
        # ====================================================

        current_q = (
            policy_dqn(states)
            .gather(
                dim=1,
                index=actions.unsqueeze(dim=1)
            )
            .squeeze()
        )

        # ====================================================
        # LOSS
        # ====================================================

        loss = self.loss_fn(
            current_q,
            target_q
        )

        # ====================================================
        # BACKPROPAGATION
        # ====================================================

        self.optimizer.zero_grad()

        loss.backward()

        self.optimizer.step()


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    # --------------------------------------------------------
    # Argument parser
    # --------------------------------------------------------

    parser = argparse.ArgumentParser(
        description="Train or test Flappy Bird DQN model."
    )

    # Hyperparameter set
    parser.add_argument(
        "hyperparameters",
        help="Name of the parameter set in parameters.yaml"
    )

    # Training flag
    parser.add_argument(
        "--train",
        help="Training mode",
        action="store_true"
    )

    # Parse arguments
    args = parser.parse_args()

    # --------------------------------------------------------
    # Create Agent
    # --------------------------------------------------------

    dql = Agent(
        param_set=args.hyperparameters
    )

    # --------------------------------------------------------
    # Train or test
    # --------------------------------------------------------

    if args.train:

        dql.run(
            is_training=True
        )

    else:

        dql.run(
            is_training=False,
            render=True
        )