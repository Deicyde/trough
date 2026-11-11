---
declaration: section
origin: cited
lean: Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.ChainCRF, Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.pathWeight, Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.partition, Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.forward, Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.forward_eq, Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.partition_eq_sum_forward, Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.viterbi, Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.pathWeight_le_viterbi
statement: formalized
proof: formalized
---

# Conditional random fields

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html).

## Linear-chain conditional random field

Let $S$ be a type of states, $O$ a type of inputs
and $R$ a type of weights with a zero and a relation $\le$. A linear-chain conditional random
field consists of a unary potential $\phi(x, t, s) \in R$ and a transition potential
$\psi(x, t, s, s') \in R$ from $s$ to $s'$, given for every observation sequence
$x \colon \mathbb{N} \to O$, every position $t \in \mathbb{N}$ and all states $s, s' \in S$, such
that $0 \le \phi(x, t, s)$ and $0 \le \psi(x, t, s, s')$ always hold.

Both potentials see the whole, possibly infinite, observation sequence $x$, so path weights
condition on all of $x$, as the conditional probability $p(y \mid x)$ of a label sequence $y$
does in the standard definition. Nonnegativity makes the potentials unnormalized
probabilities.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.ChainCRF`, a structure declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#chain-crf).

## Weight of a label path in a chain CRF

For a chain conditional random field with weights
in a semiring, unary potentials $u_t(s)$ and transition potentials $\tau_t(s, s')$ given the
observation stream $x$, the unnormalized weight of a label path $z = (z_0, \dots, z_t)$ is

$$w_t(z) = u_0(z_0) \prod_{i=1}^{t} \tau_{i-1}(z_{i-1}, z_i)\, u_i(z_i),$$

with the factors multiplied from left to right in increasing order of $i$.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.pathWeight`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#path-weight).

## Partition function of a chain CRF

For a chain conditional random field with a finite set
of states and weights in a semiring, and an observation stream $x$, the partition function at
time $t$ is $Z_t = \sum_z w_t(z)$, the total weight of all label paths $z$ of length $t + 1$,
where $w_t(z)$ is the unnormalized weight of $z$ given $x$.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.partition`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#partition).

## Forward variables of a chain CRF

For a chain conditional random field with a finite set
of states, weights in a semiring, unary potentials $u_t(s)$ and transition potentials
$\tau_t(s', s)$ given the observation stream $x$, the forward variables are defined by
$\alpha_0(s) = u_0(s)$ and
$\alpha_{t+1}(s) = \left(\sum_{s'} \alpha_t(s')\, \tau_t(s', s)\right) u_{t+1}(s)$, the sum running
over all states $s'$.

The forward variable $\alpha_t(s)$ is the total weight of the label paths of length $t + 1$ ending
in $s$.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.forward`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#forward).

## The forward variables are path weights

Let $c$ be a chain CRF with a finite set of
states $S$ and weights in a semiring $R$ carrying a relation $\le$, and let $x$ be an
observation sequence. For every $t \in \mathbb{N}$ and every state $s \in S$, the forward
variable $\alpha_t(s)$ equals the total path weight of the label paths
$z = (z_0, \dots, z_t) \in S^{t+1}$ that end in $z_t = s$:

$$\alpha_t(s) = \sum_{z \in S^{t+1},\ z_t = s} w_t(z),$$

where $w_t(z)$ is the path weight of $z$.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.forward_eq`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#forward-eq).

## The forward algorithm computes the partition function

For a chain conditional random
field with a finite set of states and weights in a semiring, and an observation stream $x$, for
every $t$ the partition function at time $t$ equals $\sum_s \alpha_t(s)$, the sum over all
states $s$ of the forward variables $\alpha_t(s)$.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.partition_eq_sum_forward`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#partition-eq-sum-forward).

## The Viterbi variables of a chain CRF

Let $c$ be a chain conditional random field with
a finite nonempty set of states $S$ and weights in a linearly ordered commutative semiring $R$,
and let $x$ be an observation sequence. Write $\phi_t(s)$ for the unary potential of $c$ at $x$
of state $s$ at position $t$, and $\psi_t(s', s)$ for its transition potential from $s'$ to $s$
at step $t$. The Viterbi variables $V_t(s)$, for $t \in \mathbb{N}$ and $s \in S$, are defined
by $V_0(s) = \phi_0(s)$ and

$$V_{t+1}(s) = \Big(\max_{s' \in S} V_t(s') \, \psi_t(s', s)\Big) \, \phi_{t+1}(s).$$

Thus $V_t(s)$ is the largest weight of a label path of length $t + 1$ ending in $s$.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.viterbi`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#viterbi).

## Path weights of a chain CRF are bounded by the Viterbi variables

For a chain conditional
random field with a nonempty finite set of states, weights in a linearly ordered commutative
semiring, and an observation stream $x$, for every $t$ and every label path
$z = (z_0, \dots, z_t)$, the weight of $z$ is at most the Viterbi variable at time $t$ of its last
state $z_t$.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.pathWeight_le_viterbi`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#path-weight-le-viterbi).

## The Viterbi variables of a chain CRF are attained

Let $c$ be a chain CRF with a finite
nonempty set of states $S$ and weights in a linearly ordered commutative semiring, and let $x$
be an observation sequence. For every $t \in \mathbb{N}$ and every state $s \in S$ there is a
label path $z = (z_0, \dots, z_t) \in S^{t+1}$ with $z_t = s$ whose path weight equals the
Viterbi variable of $s$ at time $t$.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.exists_pathWeight_eq_viterbi`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#exists-path-weight-eq-viterbi).

## Viterbi computes the MAP value of a chain CRF

Let $c$ be a chain conditional random
field with a finite nonempty set of states $S$ and weights in a linearly ordered commutative
semiring $R$, and let $x$ be an observation sequence. For every $t \in \mathbb{N}$, the maximum
over $s \in S$ of the Viterbi variable $V_t(s)$ of $c$ at $x$ equals the maximum, over all label
paths $z : \{0, \dots, t\} \to S$, of the weight of $z$.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.sup'_viterbi_eq`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#sup-viterbi-eq).

## Conditional probability of a label path in a chain CRF

Let $c$ be a chain CRF with a
finite set of states $S$ and weights in a semifield $R$ carrying a partial order $\le$, and let
$x$ be an observation sequence. For $t \in \mathbb{N}$, the conditional probability of a label
path $z \in S^{t+1}$ given $x$ is $w_t(z) / Z_t$, where $w_t(z)$ is the path weight of $z$ and
$Z_t$ is the partition function, the total path weight of all label paths in $S^{t+1}$; the
quotient is $0$ when $Z_t = 0$.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.condProb`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#cond-prob).

## The conditional probabilities sum to $1$

Let $c$ be a chain conditional random field
with finitely many states $S$ and weights in a semifield $R$ equipped with a partial order (not
assumed compatible with the operations), let $x$ be an observation sequence, and let
$t \in \mathbb{N}$. If the partition function of $c$ at $x$ and time $t$ is positive, then the
conditional probabilities $p(z \mid x)$ of all label paths $z : \{0, \dots, t\} \to S$ of length
$t + 1$ sum to $1$.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.sum_condProb_eq_one`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#sum-cond-prob-eq-one).

## Conditional probabilities of a chain CRF are nonnegative

Let $c$ be a chain CRF with a
finite set of states $S$ and weights in a linearly ordered field $R$, and let $x$ be an
observation sequence. For every $t \in \mathbb{N}$ and every label path
$z = (z_0, \dots, z_t) \in S^{t+1}$, the conditional probability of $z$ given $x$ is nonnegative.

No positivity of the partition function is assumed; nonnegativity comes from the nonnegativity
of the potentials.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.condProb_nonneg`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#cond-prob-nonneg).

## The chain CRF of a hidden Markov model

Let $h$ be a hidden Markov model with initial
weights $\pi(s)$, transition weights $a(s, s')$ and emission weights $b(s, o)$ in a linearly
ordered commutative semiring, all nonnegative. Its chain CRF has, for every observation stream
$x$, unary potentials $u_0(s) = \pi(s)\, b(s, x_0)$ and $u_t(s) = b(s, x_t)$ for $t \ge 1$, and
transition potentials $\tau_t(s, s') = a(s, s')$ at every step $t$.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.hmmToCRF`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#hmm-to-crf).

## The chain CRF of a hidden Markov model has the same path weights

Let $h$ be a hidden
Markov model with nonnegative weights in a linearly ordered commutative semiring, and let $x$ be
an observation stream. For every $t$ and every state path $z = (z_0, \dots, z_t)$, the weight of
$z$ in the chain CRF of $h$ given $x$ equals the joint weight in $h$ of the state path $z$ and the
observations $x_0, \dots, x_t$.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.hmmToCRF_pathWeight`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#hmm-to-crf-path-weight).

## One step of the tabulated CRF forward algorithm

Let $c$ be a chain CRF with states
$\{0, \dots, n-1\}$ and weights in a semiring $R$ carrying a relation $\le$, with unary
potential $\phi_t(s)$ at position $t$ and transition potential $\psi_t(s', s)$ from $s'$ to $s$
at step $t$, given the observation sequence $x$. For a table $v \in R^n$ and a step $t$, the
forward step returns the table whose entry at a state $s$ is

$$\Bigl(\sum_{s'=0}^{n-1} v_{s'} \, \psi_t(s', s)\Bigr) \, \phi_{t+1}(s).$$

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.forwardStep`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#forward-step).

## Tabulated CRF forward algorithm

Let $c$ be a chain CRF with states $\{0, \dots, n-1\}$
and weights in a semiring $R$ carrying a relation $\le$, with unary potential $\phi_t(s)$ at
position $t$ given the observation sequence $x$. The forward table is the sequence of vectors in
$R^n$ defined by recursion on time: at time $0$ its entry at $s$ is $\phi_0(s)$, and the table at
time $t + 1$ is the forward step at step $t$ applied to the table at time $t$.

Each step takes $O(n^2)$ operations.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.forwardTab`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#forward-tab).

## The tabulated forward algorithm for chain CRFs

For a chain conditional random field with
states $0, \dots, n - 1$ and weights in a semiring, and an observation stream $x$, the tabulated
partition function at time $t$ is the sum of the entries of the forward table at time $t$, the
vector $(\alpha_t(0), \dots, \alpha_t(n - 1))$ of forward variables computed step by step from
time $0$.

It equals the partition function at time $t$ and takes $O(t n^2)$ operations.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.partitionTab`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#partition-tab).

## One step of the tabulated Viterbi recursion for a chain CRF

Let $c$ be a chain
conditional random field with states $\{0, \dots, n - 1\}$, where $n \ge 1$, and weights in a
linearly ordered commutative semiring $R$, and let $x$ be an observation sequence. Write
$\phi_t(s)$ for the unary potential of $c$ at $x$ of state $s$ at position $t$, and
$\psi_t(s', s)$ for its transition potential from $s'$ to $s$ at step $t$. Given a vector
$v \in R^n$ and $t \in \mathbb{N}$, the Viterbi step returns the vector in $R^n$ whose entry at
state $s$ is

$$\Big(\max_{s'} v_{s'} \, \psi_t(s', s)\Big) \, \phi_{t+1}(s).$$

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.viterbiStep`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#viterbi-step).

## The tabulated Viterbi variables of a chain CRF

Let $c$ be a chain conditional random
field with states $\{0, \dots, n - 1\}$, where $n \ge 1$, and weights in a linearly ordered
commutative semiring $R$, and let $x$ be an observation sequence. Write $\phi_0(s)$ for the
unary potential of $c$ at $x$ of state $s$ at position $0$. The Viterbi table assigns to each
$t \in \mathbb{N}$ a vector $T_t \in R^n$: the vector $T_0$ has entry $\phi_0(s)$ at each state
$s$, and $T_{t+1}$ is the Viterbi step at time $t$ applied to $T_t$.

The entry of $T_t$ at state $s$ is the Viterbi variable $V_t(s)$.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.viterbiTab`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#viterbi-tab).

## Backpointer of the tabulated CRF Viterbi algorithm

Let $c$ be a chain CRF with states
$\{0, \dots, n-1\}$, where $n \ge 1$, and weights in a linearly ordered commutative semiring
$R$, and let $\psi_t(s', s)$ be its transition potential from $s'$ to $s$ at step $t$ given the
observation sequence $x$. For a step $t$, a table $v \in R^n$ and a state $s$, the backpointer
of $s$ is the first state $s'$, in the order $0, \dots, n-1$, that maximizes
$v_{s'} \, \psi_t(s', s)$.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.back`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#back).

## Backtracked path of the tabulated CRF Viterbi algorithm

Let $c$ be a chain CRF with
states $\{0, \dots, n-1\}$, where $n \ge 1$, and weights in a linearly ordered commutative
semiring, and fix an observation sequence $x$. For a state $s$, the backtracked path
$b_t(s) = (b_t(s)_0, \dots, b_t(s)_t)$ of length $t + 1$ is defined by recursion on $t$:
$b_0(s)$ is the one-state path $(s)$, and $b_{t+1}(s)$ is $b_t(s')$ followed by $s$, where
$s'$ is the backpointer of $s$ at step $t$ computed from the Viterbi table at time $t$.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.bestPath`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#best-path).

## The backtracked path of a chain CRF attains the Viterbi variable

For a chain conditional
random field with states $0, \dots, n - 1$ where $n \ge 1$, weights in a linearly ordered
commutative semiring, and an observation stream $x$, for every $t$ and every state $s$ the weight
of the backtracked path of length $t + 1$ ending in $s$, obtained by following the backpointers,
equals the Viterbi variable at time $t$ of $s$.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.pathWeight_bestPath`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#path-weight-best-path).

## The Viterbi path of a chain CRF

Let $c$ be a chain CRF with states $\{0, \dots, n-1\}$,
where $n \ge 1$, and weights in a linearly ordered commutative semiring, and let $x$ be an
observation sequence. For $t \in \mathbb{N}$, the Viterbi path of length $t + 1$ is the
backtracked path ending in the first state, in the order $0, \dots, n-1$, that maximizes the
Viterbi table at time $t$.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.crfPath`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#crf-path).

## The Viterbi path of a chain CRF has maximal weight

For a chain conditional random field
with states $0, \dots, n - 1$ where $n \ge 1$, weights in a linearly ordered commutative
semiring, and an observation stream $x$, for every $t$ and every label path $z$ of length
$t + 1$, the weight of $z$ is at most the weight of Viterbi's MAP path of length $t + 1$.

Formalized by `Cslib.MachineLearning.GraphicalModels.ConditionalRandomField.pathWeight_le_crfPath`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/GraphicalModels/ConditionalRandomField.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html#path-weight-le-crf-path).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conditional random fields](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/conditional-random-fields)
