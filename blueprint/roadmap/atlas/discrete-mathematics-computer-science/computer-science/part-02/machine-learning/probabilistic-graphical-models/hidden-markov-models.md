---
declaration: section
origin: cited
lean: Cslib.MachineLearning.Sequence.HiddenMarkov.HMM, Cslib.MachineLearning.Sequence.HiddenMarkov.pathProb, Cslib.MachineLearning.Sequence.HiddenMarkov.likelihood, Cslib.MachineLearning.Sequence.HiddenMarkov.forward, Cslib.MachineLearning.Sequence.HiddenMarkov.forward_eq, Cslib.MachineLearning.Sequence.HiddenMarkov.likelihood_eq_sum_forward, Cslib.MachineLearning.Sequence.HiddenMarkov.viterbi, Cslib.MachineLearning.Sequence.HiddenMarkov.HMM.Nonneg
statement: formalized
proof: formalized
---

# Hidden Markov models

46 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html).

## Hidden Markov model

A hidden Markov model with a set of states $S$, a set of observations
$O$ and weights in $R$ consists of an initial weight $\pi(s) \in R$ for each state $s$, a
transition weight $a(s, s') \in R$ for each pair of states, the weight of a transition from $s$
to $s'$, and an emission weight $e(s, o) \in R$ for each state $s$ and observation $o$, the
weight of emitting $o$ from $s$.

No structure on $R$ and no normalization of the weights is required.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.HMM`, a structure declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#hmm).

## Joint weight of a state path and the observations

For a hidden Markov model $h$ with
initial weights $\pi$, transition weights $a$ and emission weights $b$ in a semiring, observations
$x_0, x_1, \dots$ and $t \in \mathbb{N}$, the joint weight of a state path $z = (z_0, \dots, z_t)$
and $x_0, \dots, x_t$ is the product, taken from left to right,
$\pi(z_0)\, b(z_0, x_0)\, a(z_0, z_1)\, b(z_1, x_1) \cdots a(z_{t-1}, z_t)\, b(z_t, x_t)$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.pathProb`, a definition declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#path-prob).

## Likelihood of the observations

For a hidden Markov model $h$ with a finite set of states
$S$ and weights in a semiring, observations $x_0, x_1, \dots$ and $t \in \mathbb{N}$, the
likelihood of $x_0, \dots, x_t$ is the sum, over all state paths
$z = (z_0, \dots, z_t) \in S^{t+1}$, of the joint weight of $z$ and $x_0, \dots, x_t$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.likelihood`, a definition declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#likelihood).

## Forward variables of a hidden Markov model

Let $h$ be a hidden Markov model with a finite
set of states $S$ and weights in a semiring $R$, with initial weights $\pi(s)$, transition weights
$a(s', s)$ from $s'$ to $s$ and emission weights $e(s, o)$ of the observation $o$ from the state
$s$, and let $x$ be an observation sequence. The forward variables are defined by
$\alpha_0(s) = \pi(s) \, e(s, x_0)$ and
$\alpha_{t+1}(s) = \left(\sum_{s'} \alpha_t(s') \, a(s', s)\right) e(s, x_{t+1})$, the sum
running over all states $s'$.

The forward variable $\alpha_t(s)$ is the weight of the observations $x_0, \dots, x_t$ with the
state at time $t$ equal to $s$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.forward`, a definition declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#forward).

## The forward variables are path sums

Let $h$ be a hidden Markov model with a finite set of
states $S$ and weights in a semiring $R$, and let $x$ be an observation sequence. For every time
$t$ and every state $s$, the forward variable $\alpha_t(s)$ equals $\sum_z p_t(z)$, the sum
running over the state paths $z = (z_0, \dots, z_t) \in S^{t+1}$ with $z_t = s$, where $p_t(z)$
is the joint weight of $z$ and the observations $x_0, \dots, x_t$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.forward_eq`, a theorem declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#forward-eq).

## The forward algorithm computes the likelihood

Let $h$ be a hidden Markov model with a
finite set of states $S$, initial weights $\pi$, transition weights $a$ and emission weights $b$ in
a semiring, and let $x_0, x_1, \dots$ be observations. Let $\alpha$ be the forward variables,
$\alpha_0(s) = \pi(s)\, b(s, x_0)$ and
$\alpha_{t+1}(s) = \bigl(\sum_{s' \in S} \alpha_t(s')\, a(s', s)\bigr)\, b(s, x_{t+1})$. Then for
every $t \in \mathbb{N}$ the likelihood of $x_0, \dots, x_t$ equals $\sum_{s \in S} \alpha_t(s)$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.likelihood_eq_sum_forward`, a theorem declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#likelihood-eq-sum-forward).

## The Viterbi variables of a hidden Markov model

Let $h$ be a hidden Markov model with a
finite nonempty set of states $S$, initial weights $\pi(s)$, transition weights $a(s', s)$ and
emission weights $b(s, o)$ in a linearly ordered commutative semiring $R$, and let
$x_0, x_1, \dots$ be a sequence of observations. The Viterbi variables $V_t(s)$, for
$t \in \mathbb{N}$ and $s \in S$, are defined by $V_0(s) = \pi(s) \, b(s, x_0)$ and

$$V_{t+1}(s) = \Big(\max_{s' \in S} V_t(s') \, a(s', s)\Big) \, b(s, x_{t+1}).$$

When all weights are nonnegative, $V_t(s)$ is the largest joint weight of a state path of length
$t + 1$ ending in $s$ and the observations $x_0, \dots, x_t$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.viterbi`, a definition declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#viterbi).

## Hidden Markov models with nonnegative weights

A hidden Markov model $h$ with weights in a
commutative semiring with a linear order has nonnegative weights when all of its initial weights,
transition weights and emission weights are $\ge 0$: for all states $s, s'$ and every observation
$o$, the initial weight of $s$, the weight of the transition from $s$ to $s'$, and the weight of
emitting $o$ from $s$ are nonnegative.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.HMM.Nonneg`, a structure declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#nonneg).

## Path weights of a hidden Markov model are bounded by the Viterbi variables

Let $h$ be a
hidden Markov model with a finite nonempty set of states $S$ and initial weights $\pi$, transition
weights $a$ and emission weights $b$ that are nonnegative elements of a linearly ordered
commutative semiring, and let $x_0, x_1, \dots$ be observations. Let $\delta$ be the Viterbi
variables, $\delta_0(s) = \pi(s)\, b(s, x_0)$ and
$\delta_{t+1}(s) = \bigl(\max_{s' \in S} \delta_t(s')\, a(s', s)\bigr)\, b(s, x_{t+1})$. For every
$t \in \mathbb{N}$ and every state path $z = (z_0, \dots, z_t) \in S^{t+1}$, the joint weight of
$z$ and $x_0, \dots, x_t$ is at most $\delta_t(z_t)$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.pathProb_le_viterbi`, a theorem declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#path-prob-le-viterbi).

## The Viterbi variables are attained

Let $h$ be a hidden Markov model with a finite
nonempty set of states $S$ and weights in a commutative semiring $R$ with a linear order, and let
$x$ be an observation sequence. For every time $t$ and every state $s$, there is a state path
$z = (z_0, \dots, z_t)$ with $z_t = s$ whose joint weight with the observations
$x_0, \dots, x_t$ equals the Viterbi variable $V_t(s)$.

No nonnegativity of the weights and no compatibility of the order with the operations is
needed.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.exists_pathProb_eq_viterbi`, a theorem declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#exists-path-prob-eq-viterbi).

## Viterbi computes the MAP value

Let $h$ be a hidden Markov model with a finite nonempty set
of states $S$ and initial weights $\pi$, transition weights $a$ and emission weights $b$ that are
nonnegative elements of a linearly ordered commutative semiring, and let $x_0, x_1, \dots$ be
observations. Let $\delta$ be the Viterbi variables, $\delta_0(s) = \pi(s)\, b(s, x_0)$ and
$\delta_{t+1}(s) = \bigl(\max_{s' \in S} \delta_t(s')\, a(s', s)\bigr)\, b(s, x_{t+1})$. For every
$t \in \mathbb{N}$, $\max_{s \in S} \delta_t(s)$ equals the maximum, over all state paths
$z \in S^{t+1}$, of the joint weight of $z$ and $x_0, \dots, x_t$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.sup'_viterbi_eq`, a theorem declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#sup-viterbi-eq).

## Sum of the entries of a vector

For a vector $v = (v_0, \dots, v_{n-1})$ of length $n$ with
entries in an additive commutative monoid, its entry sum is $\sum_{s < n} v_s$.

The vector is passed as an argument, so a table computed once is summed without recomputing it.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.sumVec`, a definition declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#sum-vec).

## One step of the tabulated forward algorithm

Let $h$ be a hidden Markov model with states
$\{0, \dots, n-1\}$ and weights in a semiring $R$, with transition weight $a(s', s)$ from $s'$ to
$s$ and emission weight $e(s, o)$ of the observation $o$ from the state $s$, and let $x$ be an
observation sequence. For a table $v \in R^n$ and a step $t$, the forward step returns the table
whose entry at a state $s$ is

$$\Bigl(\sum_{s'=0}^{n-1} v_{s'} \, a(s', s)\Bigr) \, e(s, x_{t+1}).$$

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.forwardStep`, a definition declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#forward-step).

## Tabulated forward algorithm

Let $h$ be a hidden Markov model with states
$\{0, \dots, n-1\}$ and weights in a semiring $R$, with initial weight $\pi(s)$ and emission
weight $e(s, o)$ of the observation $o$ from the state $s$, and let $x$ be an observation
sequence. The forward table is the sequence of vectors in $R^n$ defined by recursion on time: at
time $0$ its entry at $s$ is $\pi(s) \, e(s, x_0)$, and the table at time $t + 1$ is the forward
step at step $t$ applied to the table at time $t$.

Each step takes $O(n^2)$ operations, and the entry at $s$ of the table at time $t$ is the forward
variable $\alpha_t(s)$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.forwardTab`, a definition declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#forward-tab).

## Tabulated likelihood of a hidden Markov model

For a hidden Markov model $h$ with states
$0, \dots, n - 1$ and weights in a semiring, observations $x_0, x_1, \dots$ and $t \in \mathbb{N}$,
the tabulated likelihood at time $t$ is the sum $\sum_{s < n} v_s$ of the entries of the forward
table $v = (v_0, \dots, v_{n-1})$ at time $t$.

The forward table is computed step by step with $O(n^2)$ semiring operations per step, so the
tabulated likelihood costs $O(t n^2)$ operations; it equals the likelihood of $x_0, \dots, x_t$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.likelihoodTab`, a definition declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#likelihood-tab).

## First maximizer of a function on a finite range

Let $n \ge 1$ and let $R$ be a linearly
ordered set. For a function $f$ from $\{0, \dots, n-1\}$ to $R$, the maximizer of $f$ is the first
$i$, in the order $0, \dots, n-1$, at which $f$ attains its maximum, that is, $f(j) \le f(i)$ for
every $j$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.argmaxFin`, a definition declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#argmax-fin).

## One step of the tabulated Viterbi recursion for a hidden Markov model

Let $h$ be a hidden
Markov model with states $\{0, \dots, n - 1\}$, where $n \ge 1$, transition weights $a(s', s)$
and emission weights $b(s, o)$ in a linearly ordered commutative semiring $R$, and let
$x_0, x_1, \dots$ be a sequence of observations. Given a vector $v \in R^n$ and
$t \in \mathbb{N}$, the Viterbi step returns the vector in $R^n$ whose entry at state $s$ is

$$\Big(\max_{s'} v_{s'} \, a(s', s)\Big) \, b(s, x_{t+1}).$$

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.viterbiStep`, a definition declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#viterbi-step).

## The tabulated Viterbi variables of a hidden Markov model

Let $h$ be a hidden Markov model
with states $\{0, \dots, n - 1\}$, where $n \ge 1$, initial weights $\pi(s)$, transition weights
$a(s', s)$ and emission weights $b(s, o)$ in a linearly ordered commutative semiring $R$, and let
$x_0, x_1, \dots$ be a sequence of observations. The Viterbi table assigns to each
$t \in \mathbb{N}$ a vector $T_t \in R^n$: the vector $T_0$ has entry $\pi(s) \, b(s, x_0)$ at
each state $s$, and $T_{t+1}$ is the Viterbi step at time $t$ applied to $T_t$, the vector whose
entry at state $s$ is $\big(\max_{s'} (T_t)_{s'} \, a(s', s)\big) \, b(s, x_{t+1})$.

The entry of $T_t$ at state $s$ is the Viterbi variable of $s$ at time $t$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.viterbiTab`, a definition declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#viterbi-tab).

## Backpointer of the tabulated Viterbi algorithm

Let $h$ be a hidden Markov model with
states $\{0, \dots, n-1\}$, where $n \ge 1$, and weights in a commutative semiring $R$ with a
linear order, and let $a(s', s)$ be its transition weight from $s'$ to $s$. For a table
$v \in R^n$ and a state $s$, the backpointer of $s$ is the first state $s'$, in the order
$0, \dots, n-1$, that maximizes $v_{s'} \, a(s', s)$.

No compatibility of the order with the operations is needed.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.back`, a definition declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#back).

## Backtracked path of the tabulated Viterbi algorithm

Let $h$ be a hidden Markov model
with states $\{0, \dots, n-1\}$, where $n \ge 1$, and weights in a commutative semiring with a
linear order, and fix an observation sequence $x$. For a state $s$, the backtracked path
$b_t(s) = (b_t(s)_0, \dots, b_t(s)_t)$ of length $t + 1$ is defined by recursion on $t$:
$b_0(s)$ is the one-state path $(s)$, and $b_{t+1}(s)$ is $b_t(s')$ followed by $s$, where
$s'$ is the backpointer of $s$ computed from the Viterbi table at time $t$.

No compatibility of the order with the operations is needed.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.bestPath`, a definition declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#best-path).

## The backtracked path of a hidden Markov model attains the Viterbi variable

Let $h$ be a
hidden Markov model with states $0, \dots, n - 1$, where $n \ge 1$, initial weights $\pi$,
transition weights $a$ and emission weights $b$ in a commutative semiring with a linear order, and
let $x_0, x_1, \dots$ be observations. Let $\delta$ be the Viterbi variables,
$\delta_0(s) = \pi(s)\, b(s, x_0)$ and
$\delta_{t+1}(s) = \bigl(\max_{s'} \delta_t(s')\, a(s', s)\bigr)\, b(s, x_{t+1})$. For every
$t \in \mathbb{N}$ and every state $s$, the joint weight of $x_0, \dots, x_t$ and the backtracked
path of length $t + 1$ ending in $s$, obtained by following the backpointers, equals
$\delta_t(s)$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.pathProb_bestPath`, a theorem declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#path-prob-best-path).

## Index of a largest entry of a table

Let $n \ge 1$ and let $R$ be a linearly ordered set.
For a table $v = (v_0, \dots, v_{n-1}) \in R^n$, the maximizing index of $v$ is the first index
$s$, in the order $0, \dots, n-1$, such that $v_{s'} \le v_s$ for every $s'$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.argmaxVec`, a definition declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#argmax-vec).

## Viterbi's MAP path

Let $h$ be a hidden Markov model with states $\{0, \dots, n - 1\}$,
where $n \ge 1$, whose weights lie in a linearly ordered commutative semiring $R$, with transition
weights $a(s', s)$, and let $x$ be a sequence of observations. For $t \in \mathbb{N}$, let
$T_0, \dots, T_t \in R^n$ be the tabulated Viterbi variables of $h$ on $x$. The Viterbi path of
length $t + 1$ is the state path $(z_0, \dots, z_t)$ in which $z_t$ is the first state $s$, in the
order $0, \dots, n - 1$, that maximizes $(T_t)_s$, and, for $k < t$, $z_k$ is the first state $s'$
that maximizes $(T_k)_{s'} \, a(s', z_{k+1})$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.viterbiPath`, a definition declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#viterbi-path).

## The Viterbi path is a most probable path

Let $h$ be a hidden Markov model with states
$0, \dots, n - 1$, where $n \ge 1$, and nonnegative weights in a linearly ordered commutative
semiring, and let $x_0, x_1, \dots$ be observations. For every $t \in \mathbb{N}$ and every state
path $z = (z_0, \dots, z_t)$, the joint weight of $z$ and $x_0, \dots, x_t$ is at most the joint
weight of the Viterbi path of length $t + 1$ and $x_0, \dots, x_t$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.pathProb_le_viterbiPath`, a theorem declared in [CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/HiddenMarkov.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#path-prob-le-viterbi-path).

## Backward variables of a hidden Markov model

Let $h$ be a hidden Markov model with finite
state set $S$, transition weights $a$ and emission weights $b$ in a semiring $R$, and let
$x_0, x_1, \dots$ be observations. The backward variables $\beta_k(t, s) \in R$, for
$k, t \in \mathbb{N}$ and $s \in S$, are defined by $\beta_0(t, s) = 1$ and

$$\beta_{k+1}(t, s) = \sum_{s' \in S} a(s, s')\, b(s', x_{t+1})\, \beta_k(t + 1, s').$$

Thus $\beta_k(t, s)$ is the weight of the observations $x_{t+1}, \dots, x_{t+k}$ given the state
$s$ at time $t$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.backward`, a definition declared in [CSLibExt/MachineLearning/Sequence/ForwardBackward.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/ForwardBackward.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#backward).

## Bridge weights of a hidden Markov model

Let $h$ be a hidden Markov model with finite state
set $S$, transition weights $a$ and emission weights $b$ in a semiring $R$, and let
$x_0, x_1, \dots$ be observations. The bridge weights $B_k(t, s, u) \in R$, for
$k, t \in \mathbb{N}$ and $s, u \in S$, are defined from the end by $B_0(t, s, u) = 1$ if $s = u$
and $B_0(t, s, u) = 0$ otherwise, and

$$B_{k+1}(t, s, u) = \left(\sum_{u' \in S} B_k(t, s, u')\, a(u', u)\right) b(u, x_{t+k+1}).$$

Thus $B_k(t, s, u)$ is the total weight of the paths from state $s$ at time $t$ to state $u$ at
time $t + k$, with transitions and emissions at times $t + 1, \dots, t + k$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.bridge`, a definition declared in [CSLibExt/MachineLearning/Sequence/ForwardBackward.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/ForwardBackward.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#bridge).

## Joint weight of the observations and a state

For a hidden Markov model with a finite set
of states $S$ and weights in a semiring, observations $x_0, x_1, \dots$, times $t, k \in \mathbb{N}$
and a state $s \in S$, the joint weight of $x_0, \dots, x_{t+k}$ and the state $s$ at time $t$ is
the sum of the path weights $p_{t+k}(z)$ over all state paths $z = (z_0, \dots, z_{t+k})$ in $S$
with $z_t = s$, where $p_{t+k}(z)$ is the joint weight of the path $z$ and the observations
$x_0, \dots, x_{t+k}$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.stateMarg`, a definition declared in [CSLibExt/MachineLearning/Sequence/ForwardBackward.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/ForwardBackward.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#state-marg).

## Front decomposition of the bridge weights

Let $h$ be a hidden Markov model with finite
state set $S$, transition weights $a$ and emission weights $b$ in a semiring, let $x_0, x_1, \dots$
be observations, and write $B_k(t, s, u)$ for the bridge weight of the paths from state $s$ at
time $t$ to state $u$ at time $t + k$. Then for all $k, t \in \mathbb{N}$ and $s, u \in S$,

$$B_{k+1}(t, s, u) = \sum_{s' \in S} a(s, s')\, b(s', x_{t+1})\, B_k(t + 1, s', u).$$

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.bridge_succ_front`, a theorem declared in [CSLibExt/MachineLearning/Sequence/ForwardBackward.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/ForwardBackward.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#bridge-succ-front).

## Bridge weights sum to the backward variable

For a hidden Markov model with a finite set
of states $S$ and weights in a semiring, observations $x_0, x_1, \dots$, all $k, t \in \mathbb{N}$
and every state $s \in S$, the sum over all states $u \in S$ of the bridge weight from state $s$
at time $t$ to state $u$ at time $t + k$ equals the backward variable $\beta_{k,t}(s)$, the
weight of the observations $x_{t+1}, \dots, x_{t+k}$ given the state $s$ at time $t$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.sum_bridge`, a theorem declared in [CSLibExt/MachineLearning/Sequence/ForwardBackward.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/ForwardBackward.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#sum-bridge).

## Paths through two fixed states

For a hidden Markov model with a finite set of states $S$
and weights in a semiring, observations $x_0, x_1, \dots$, all $k, t \in \mathbb{N}$ and states
$s, u \in S$, the sum of the path weights $p_{t+k}(z)$ over all state paths
$z = (z_0, \dots, z_{t+k})$ in $S$ with $z_t = s$ and $z_{t+k} = u$ equals
$\alpha_t(s)\, b_{k,t}(s, u)$. Here $p_{t+k}(z)$ is the joint weight of the path $z$ and the
observations $x_0, \dots, x_{t+k}$, $\alpha_t(s)$ is the forward variable and $b_{k,t}(s, u)$ is
the bridge weight from state $s$ at time $t$ to state $u$ at time $t + k$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.sum_pathProb_ite_ite`, a theorem declared in [CSLibExt/MachineLearning/Sequence/ForwardBackward.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/ForwardBackward.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#sum-path-prob-ite-ite).

## Forward-backward identity

For a hidden Markov model with a finite set of states $S$ and
weights in a semiring, observations $x_0, x_1, \dots$, times $t, k \in \mathbb{N}$ and a state
$s \in S$, the joint weight of the observations $x_0, \dots, x_{t+k}$ and the state $s$ at time
$t$ equals $\alpha_t(s)\,\beta_{k,t}(s)$, the forward variable $\alpha_t(s)$ (the weight of
$x_0, \dots, x_t$ with the state at time $t$ equal to $s$) times the backward variable
$\beta_{k,t}(s)$ (the weight of $x_{t+1}, \dots, x_{t+k}$ given the state $s$ at time $t$).

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.stateMarg_eq`, a theorem declared in [CSLibExt/MachineLearning/Sequence/ForwardBackward.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/ForwardBackward.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#state-marg-eq).

## The likelihood from the forward and backward variables

Let $h$ be a hidden Markov model
with finite state set $S$ and weights in a semiring, and let $x_0, x_1, \dots$ be observations.
Write $\alpha_t(s)$ for the forward variable (the weight of $x_0, \dots, x_t$ with the state at
time $t$ equal to $s$) and $\beta_k(t, s)$ for the backward variable. Then for all
$t, k \in \mathbb{N}$, the likelihood of $x_0, \dots, x_{t+k}$ equals

$$\sum_{s \in S} \alpha_t(s)\, \beta_k(t, s).$$

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.likelihood_eq_sum_forward_mul_backward`, a theorem declared in [CSLibExt/MachineLearning/Sequence/ForwardBackward.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/ForwardBackward.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#likelihood-eq-sum-forward-mul-backward).

## Smoothed state weights

For a hidden Markov model with a finite set of states $S$ and
weights in a semifield $K$, observations $x_0, x_1, \dots$, times $t, k \in \mathbb{N}$ and a
state $s \in S$, the smoothed weight of $s$ at time $t$ is

$$\gamma_{t,k}(s) = \frac{\alpha_t(s)\,\beta_{k,t}(s)}{L_{t+k}},$$

where $\alpha_t(s)$ is the forward variable, $\beta_{k,t}(s)$ is the backward variable (the weight
of $x_{t+1}, \dots, x_{t+k}$ given the state $s$ at time $t$) and $L_{t+k}$ is the likelihood of
$x_0, \dots, x_{t+k}$. Division is that of $K$, so $\gamma_{t,k}(s) = 0$ when $L_{t+k} = 0$.

For nonnegative weights with stochastic rows and a positive likelihood this is the smoothing
posterior $P(z_t = s \mid x_0, \dots, x_{t+k})$ that the hidden state $z_t$ at time $t$ is $s$; for
general semifield weights it is only this ratio.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.smoothed`, a definition declared in [CSLibExt/MachineLearning/Sequence/ForwardBackward.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/ForwardBackward.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#smoothed).

## Forward-backward smoothing is a joint-to-likelihood ratio

Let $g$ be a hidden Markov model
with finite state set $S$ and weights in a semifield, and let $x_0, x_1, \dots$ be observations.
For all $t, k \in \mathbb{N}$ and $s \in S$, the smoothing weight
$\alpha_t(s)\, \beta_k(t, s) / L_{t+k}$, where $\alpha$ and $\beta$ are the forward and backward
variables and $L_{t+k}$ is the likelihood of $x_0, \dots, x_{t+k}$, equals the joint weight of
$x_0, \dots, x_{t+k}$ and the state $s$ at time $t$, divided by $L_{t+k}$.

When the weights are probabilities and the likelihood is positive, this ratio is the conditional
state marginal.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.smoothed_eq`, a theorem declared in [CSLibExt/MachineLearning/Sequence/ForwardBackward.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/ForwardBackward.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#smoothed-eq).

## Smoothed weights sum to one

For a hidden Markov model with a finite set of states $S$ and
weights in a semifield, observations $x_0, x_1, \dots$ and times $t, k \in \mathbb{N}$, if the
likelihood $L_{t+k}$ of $x_0, \dots, x_{t+k}$ is nonzero, then the smoothed weights
$\gamma_{t,k}(s) = \alpha_t(s)\,\beta_{k,t}(s) / L_{t+k}$, with $\alpha$ the forward and $\beta$
the backward variables, sum to $1$ over all states $s \in S$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.sum_smoothed`, a theorem declared in [CSLibExt/MachineLearning/Sequence/ForwardBackward.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/ForwardBackward.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#sum-smoothed).

## Smoothing weights are nonnegative

Let $g$ be a hidden Markov model with finite state set
$S$ whose initial, transition and emission weights are nonnegative elements of a linearly ordered
semifield $K$, and let $x_0, x_1, \dots$ be observations. For all $t, k \in \mathbb{N}$ and
$s \in S$, the smoothing weight $\alpha_t(s)\, \beta_k(t, s) / L_{t+k}$ is nonnegative, where
$\alpha$ and $\beta$ are the forward and backward variables and $L_{t+k}$ is the likelihood of
$x_0, \dots, x_{t+k}$.

Since the smoothing weights at each time sum to one when the likelihood is nonzero, with a
positive likelihood they form a probability distribution over the states.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.smoothed_nonneg`, a theorem declared in [CSLibExt/MachineLearning/Sequence/ForwardBackward.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/ForwardBackward.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#smoothed-nonneg).

## One step of the tabulated backward algorithm

For a hidden Markov model $g$ with states
$\{0, \dots, n - 1\}$, transition weights $a$ and emission weights $b$ in a semiring $R$, an
observation sequence $x_0, x_1, \dots$, a vector $v \in R^n$ and a time $t$, this is the vector in
$R^n$ whose entry at state $s$ is $\sum_{s'} a(s, s')\, b(s', x_{t+1})\, v_{s'}$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.backwardStep`, a definition declared in [CSLibExt/MachineLearning/Sequence/ForwardBackward.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/ForwardBackward.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#backward-step).

## The tabulated backward algorithm

For a hidden Markov model $g$ with states
$\{0, \dots, n - 1\}$, transition weights $a$ and emission weights $b$ in a semiring $R$, and an
observation sequence $x_0, x_1, \dots$, the tables $\beta^{(k)}_t \in R^n$ for $k, t \in \mathbb{N}$
are defined by recursion on $k$: $\beta^{(0)}_t$ is the all-ones vector, and $\beta^{(k+1)}_t$ is
one backward step at time $t$ applied to $\beta^{(k)}_{t+1}$, that is, its entry at state $s$ is
$\sum_{s'} a(s, s')\, b(s', x_{t+1})\, \beta^{(k)}_{t+1}(s')$.

The entries of $\beta^{(k)}_t$ are the backward variables; each step takes $O(n^2)$ operations.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.backwardTab`, a definition declared in [CSLibExt/MachineLearning/Sequence/ForwardBackward.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/ForwardBackward.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#backward-tab).

## Smoothing step on tables

For a semifield $K$, vectors $a, b \in K^n$ and $L \in K$, this is
the vector in $K^n$ whose entry at $s$ is $a_s b_s / L$.

It combines the forward and backward tables into the smoothing weights.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.smoothStep`, a definition declared in [CSLibExt/MachineLearning/Sequence/ForwardBackward.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/ForwardBackward.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#smooth-step).

## Tabulated forward-backward smoothing

Let $g$ be a hidden Markov model with states
$\{0, \dots, n - 1\}$ and weights in a semifield $K$, and let $x_0, x_1, \dots$ be observations.
For $t, k \in \mathbb{N}$, this is the vector in $K^n$ whose entry at state $s$ is
$\alpha_t(s)\, \beta_k(t, s) / L_{t+k}$, where $\alpha_t$ is the tabulated forward vector at time
$t$, $\beta_k(t, \cdot)$ is the tabulated backward vector for $k$ steps from time $t$, and $L_{t+k}$
is the tabulated likelihood of $x_0, \dots, x_{t+k}$.

Its entries are the smoothing weights of all states at time $t$, computed in $O((t + k) n^2)$
operations.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.smoothedTab`, a definition declared in [CSLibExt/MachineLearning/Sequence/ForwardBackward.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/ForwardBackward.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#smoothed-tab).

## Posterior decoding

At each time `t ≤ T`, a state of largest posterior
`smoothed x g t (T - t)` (the first one, via `argmaxFin`).

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.posteriorPath`, a definition declared in [CSLibExt/MachineLearning/Sequence/PosteriorDecoding.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/PosteriorDecoding.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#posterior-path).

## Posterior path maximizes the posterior at each time

The posterior path picks a state of largest posterior at each time.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.smoothed_le_posteriorPath`, a theorem declared in [CSLibExt/MachineLearning/Sequence/PosteriorDecoding.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/PosteriorDecoding.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#smoothed-le-posterior-path).

## Smoothed posterior as a sum over state paths

The posterior of state `s` at time `t ≤ T`, as a sum over the paths of length `T + 1`: the
total weight of the paths through `s` at time `t` over the likelihood.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.smoothed_eq_sum_pathProb`, a theorem declared in [CSLibExt/MachineLearning/Sequence/PosteriorDecoding.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/PosteriorDecoding.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#smoothed-eq-sum-path-prob).

## Posterior expected number of correctly decoded states

The posterior expected number of correctly decoded states of a path `z`: the sum over all
state paths `w` of `pathProb w / likelihood` times the number of times `t ≤ T` with
`w t = z t`. When the weights are probabilities and the likelihood is positive, this is the
expectation under the posterior law of the path; for likelihood `0` it is `0` (`x / 0 = 0`), as
is every posterior `smoothed`.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.expectedCorrect`, a definition declared in [CSLibExt/MachineLearning/Sequence/PosteriorDecoding.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/PosteriorDecoding.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#expected-correct).

## The expected number of correct states is a sum of posteriors

For every path `z`, the
posterior expected number of times `t ≤ T` with `w t = z t` is the sum over `t` of the posterior
of `z t` at time `t`.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.expectedCorrect_eq_sum_smoothed`, a theorem declared in [CSLibExt/MachineLearning/Sequence/PosteriorDecoding.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/PosteriorDecoding.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#expected-correct-eq-sum-smoothed).

## Posterior decoding maximizes the expected number of correctly decoded states

**Posterior decoding maximizes the expected number of correctly decoded states**
when addition preserves the order.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.expectedCorrect_le_posteriorPath`, a theorem declared in [CSLibExt/MachineLearning/Sequence/PosteriorDecoding.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/PosteriorDecoding.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html#expected-correct-le-posterior-path).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hidden Markov models](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/hidden-markov-models)
