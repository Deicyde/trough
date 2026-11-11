---
declaration: section
origin: cited
lean: Cslib.MachineLearning.Sequence.BaumWelch.pathProb_eq_prod, Cslib.MachineLearning.Sequence.BaumWelch.Valid, Cslib.MachineLearning.Sequence.BaumWelch.ValidHMM, Cslib.MachineLearning.Sequence.BaumWelch.joint, Cslib.MachineLearning.Sequence.BaumWelch.marginal_joint, Cslib.MachineLearning.Sequence.BaumWelch.pInit, Cslib.MachineLearning.Sequence.BaumWelch.pTrans, Cslib.MachineLearning.Sequence.BaumWelch.pEmit
statement: formalized
proof: formalized
---

# Baum–Welch algorithm

27 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html).

## Path weight as a product

Let $h$ be an HMM with weights in a commutative semiring, with
initial weights $\pi$, transition weights $a$ and emission weights $b$, and let $x_0, x_1, \dots$
be observations. For every $T$ and every state path $z = (z_0, \dots, z_T)$, the path weight of
$z$ and $x_0, \dots, x_T$ is

$$\pi(z_0) \prod_{t=0}^{T-1} a(z_t, z_{t+1}) \prod_{t=0}^{T} b(z_t, x_t).$$

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.pathProb_eq_prod`, a theorem declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#path-prob-eq-prod).

## Valid hidden Markov model parameters

A hidden Markov model with finite state set $S$,
finite observation set $O$ and real initial weights $\pi$, transition weights $a$ and emission
weights $b$ is valid when all its weights are strictly positive and form probability
distributions: $\pi(s) > 0$ for every $s$ and $\sum_{s} \pi(s) = 1$; $a(s, s') > 0$ for all
$s, s'$ and $\sum_{s'} a(s, s') = 1$ for every $s$; and $b(s, o) > 0$ for all $s, o$ and
$\sum_{o} b(s, o) = 1$ for every $s$.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.Valid`, a structure declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#valid).

## Valid HMMs

For finite sets $S$ of states and $O$ of observations, the valid HMMs are the
HMMs with states $S$, observations $O$ and real weights whose initial weights are positive and sum
to $1$, whose transition weights out of each state are positive and sum to $1$, and whose emission
weights from each state are positive and sum to $1$. They form the parameter space of
Baum-Welch.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.ValidHMM`, an abbreviation declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#valid-hmm).

## The EM model of a hidden Markov model

Let $S$ and $O$ be finite sets and let $T$ be a
natural number. Let $h$ be a valid hidden Markov model on states $S$ and observations $O$, with
positive initial probabilities $\pi_s$, transition probabilities $a_{ss'}$ and emission
probabilities $b_{so}$, each distribution summing to one. The joint of its EM model at an
observation sequence $x = (x_0, x_1, \dots)$ in $O$ and a state path $z = (z_0, \dots, z_T)$ in $S$
is the path weight $p_h(x, z) = \pi_{z_0} b_{z_0 x_0} \prod_{t=1}^{T} a_{z_{t-1} z_t} b_{z_t x_t}$.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.joint`, a definition declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#joint).

## The EM marginal of an HMM is its likelihood

For every $T$, every valid HMM $h$ and every
observation sequence $x$, the marginal at $h$ and $x$ of the EM model of HMMs with state paths
$(z_0, \dots, z_T)$, that is the sum over all such paths of the path weight of $z$ and $x$, equals
the likelihood under $h$ of the observations $x_0, \dots, x_T$.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.marginal_joint`, a theorem declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#marginal-joint).

## Initial-state indicator of a state path

For a state path $z = (z_0, \dots, z_T)$ and a
state $s$, the initial-state indicator is the real number $1$ if $z_0 = s$ and $0$ otherwise.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.pInit`, a definition declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#p-init).

## Transition count of a state path

For a state path $z = (z_0, \dots, z_T)$ and states
$s, s'$, the transition count is the number of $t \in \{0, \dots, T - 1\}$ with $z_t = s$ and
$z_{t+1} = s'$, as a real number.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.pTrans`, a definition declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#p-trans).

## Emission count of a state path

For a state path $z = (z_0, \dots, z_T)$, observations
$x_0, x_1, \dots$, a state $s$ and a symbol $o$, the emission count is the number of times
$t \in \{0, \dots, T\}$ with $z_t = s$ and $x_t = o$, as a real number.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.pEmit`, a definition declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#p-emit).

## The log path weight is linear in the path's counts

Let $S$ and $O$ be finite sets, let
$T$ be a natural number, and let $h$ be a valid hidden Markov model on states $S$ and observations
$O$, with positive initial probabilities $\pi_s$, transition probabilities $a_{ss'}$ and emission
probabilities $b_{so}$, each distribution summing to one. For every observation sequence
$x = (x_0, x_1, \dots)$ in $O$ and every state path $z = (z_0, \dots, z_T)$ in $S$, the path
weight $p_h(x, z) = \pi_{z_0} b_{z_0 x_0} \prod_{t=1}^{T} a_{z_{t-1} z_t} b_{z_t x_t}$ satisfies
$\log p_h(x, z) = \sum_{s} [z_0 = s] \log \pi_s + \sum_{s, s'} n_{ss'} \log a_{ss'} +
\sum_{s, o} m_{so} \log b_{so}$, where $[z_0 = s]$ is $1$ if $z_0 = s$ and $0$ otherwise,
$n_{ss'} = \#\{t < T : z_t = s,\ z_{t+1} = s'\}$ and $m_{so} = \#\{t \le T : z_t = s,\ x_t = o\}$.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.log_joint`, a theorem declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#log-joint).

## Posterior weight of a state path

For a valid HMM $h$, observation sequences
$x_0, \dots, x_{N-1}$, an index $n < N$ and a state path $z = (z_0, \dots, z_T)$, the posterior
weight of $z$ is the posterior of $z$ given $x_n$ at $h$ in the EM model of HMMs: the path weight
of $z$ and $x_n$ divided by the sum of the path weights of $z'$ and $x_n$ over all state paths
$z' = (z'_0, \dots, z'_T)$.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.post`, a definition declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#post).

## Expected initial-state counts

Let $S$ and $O$ be finite sets, let $T$ be a natural
number, and let $x_1, \dots, x_N$ be sequences of observations in $O$. For a valid hidden Markov
model $h$ on states $S$ and observations $O$ and a state $s$, the expected number of sequences
starting in $s$ is

$$I_s = \sum_{n=1}^{N} \sum_{z \,:\, z_0 = s} p_h(z \mid x_n),$$

where $z$ ranges over the state paths $(z_0, \dots, z_T)$ in $S$ and $p_h(z \mid x_n)$ is the
posterior of $z$ given $x_n$: the path weight of $z$ and $x_n$ under $h$ divided by the total
weight of all such paths.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.initCount`, a definition declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#init-count).

## Expected transition count

For a valid HMM $h$, observation sequences
$x_0, \dots, x_{N-1}$ and states $s, s'$, the expected transition count is
$\sum_{n < N} \sum_{z} p_h(z \mid x_n) \, c_{s s'}(z)$, where $z$ ranges over the state paths
$(z_0, \dots, z_T)$, $p_h(z \mid x_n)$ is the posterior weight of $z$ for $x_n$, and $c_{s s'}(z)$
is the number of $t < T$ with $z_t = s$ and $z_{t+1} = s'$.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.transCount`, a definition declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#trans-count).

## Expected emission counts

Let $S$ and $O$ be finite sets, let $T$ be a natural number,
and let $x_1, \dots, x_N$ be sequences $x_n = (x_{n,0}, x_{n,1}, \dots)$ of observations in $O$.
For a valid hidden Markov model $h$ on states $S$ and observations $O$, a state $s$ and an
observation $o$, the expected number of emissions of $o$ from $s$ is

$$E_{so} = \sum_{n=1}^{N} \sum_{z} p_h(z \mid x_n) \, \#\{t \le T : z_t = s,\ x_{n,t} = o\},$$

where $z$ ranges over the state paths $(z_0, \dots, z_T)$ in $S$ and $p_h(z \mid x_n)$ is the
posterior of $z$ given $x_n$: the path weight of $z$ and $x_n$ under $h$ divided by the total
weight of all such paths.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.emitCount`, a definition declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#emit-count).

## The Baum-Welch M-step

Let $h$ be a valid HMM with finite state set $S$ and finite
observation set $O$, let $x_0, \dots, x_{N-1}$ be observation sequences, and consider state paths
$(z_0, \dots, z_T)$. Write $I(s)$, $A(s, s')$ and $E(s, o)$ for the expected numbers, under the
posterior of $h$ and summed over the sequences, of sequences starting in $s$, of transitions
$s \to s'$ and of emissions of $o$ from $s$. The M-step is the HMM with real weights whose initial
weight of $s$ is $I(s) / N$, whose transition weight from $s$ to $s'$ is
$A(s, s') / \sum_{s''} A(s, s'')$, and whose emission weight of $o$ from $s$ is
$E(s, o) / \sum_{o'} E(s, o')$ (a quotient by $0$ is read as $0$).

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.mStep`, a definition declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#m-step).

## The Baum-Welch objective in terms of expected counts

Let $S$ and $O$ be finite sets, let
$T$ be a natural number, and let $x_1, \dots, x_N$ be sequences $x_n = (x_{n,0}, x_{n,1}, \dots)$ of
observations in $O$. For a valid hidden Markov model $h$ on states $S$ and observations $O$
(positive initial, transition and emission probabilities, each distribution summing to one), write
$p_h(x, z)$ for the path weight of the observations $x$ and a state path $z = (z_0, \dots, z_T)$
(the joint of the EM model of $h$) and $p_h(z \mid x) = p_h(x, z) / \sum_{z'} p_h(x, z')$ for the
posterior of the path, the sums ranging over all paths $z : \{0, \dots, T\} \to S$. Let
$I_s = \sum_n \sum_{z \,:\, z_0 = s} p_h(z \mid x_n)$,
$A_{ss'} = \sum_n \sum_z p_h(z \mid x_n) \, \#\{t < T : z_t = s,\ z_{t+1} = s'\}$ and
$E_{so} = \sum_n \sum_z p_h(z \mid x_n) \, \#\{t \le T : z_t = s,\ x_{n,t} = o\}$ be the expected
counts of initial states, transitions and emissions. Then for every valid hidden Markov model $h'$
with initial probabilities $\pi'_s$, transition probabilities $a'_{ss'}$ and emission
probabilities $b'_{so}$, the EM objective
$Q(h' \mid h) = \sum_n \sum_z p_h(z \mid x_n) \log p_{h'}(x_n, z)$ equals
$\sum_{s} I_s \log \pi'_s + \sum_{s, s'} A_{ss'} \log a'_{ss'} +
\sum_{s, o} E_{so} \log b'_{so}$.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.emQ_eq`, a theorem declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#em-q-eq).

## Data rich enough for the Baum-Welch M-step

Observation sequences $x_0, \dots, x_{N-1}$
over a symbol set $O$ are rich for state paths $(z_0, \dots, z_T)$ when $N > 0$, $T > 0$, and
every symbol $o \in O$ is observed, that is $x_n(t) = o$ for some $n < N$ and some $t \le T$.

These are the data on which the M-step gives a valid HMM.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.Rich`, a structure declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#rich).

## One Baum-Welch step

Let $S$ and $O$ be finite sets, let $T \ge 1$, and let
$x_1, \dots, x_N$ with $N \ge 1$ be sequences $x_n = (x_{n,0}, x_{n,1}, \dots)$ of observations in
$O$ such that every $o \in O$ equals $x_{n,t}$ for some $n$ and some $t \le T$. For a valid hidden
Markov model $h$ on states $S$ and observations $O$ (positive initial, transition and emission
probabilities, each distribution summing to one), the Baum-Welch step maps $h$ to the hidden Markov
model with initial probabilities $I_s / N$, transition probabilities
$A_{ss'} / \sum_{s''} A_{ss''}$ and emission probabilities $E_{so} / \sum_{o'} E_{so'}$. Here
$I_s$, $A_{ss'}$ and $E_{so}$ are the expected numbers of initial states equal to $s$, of
transitions from $s$ to $s'$ at times $t < T$, and of emissions of $o$ from $s$ at times $t \le T$,
summed over $n$ under the posterior of $h$ over state paths $(z_0, \dots, z_T)$ given $x_n$. On
such data this hidden Markov model is again valid.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.emStep`, a definition declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#em-step).

## The Baum-Welch update maximizes the EM objective

Let $S$ and $O$ be finite sets, let
$T \ge 1$, and let $x_1, \dots, x_N$ with $N \ge 1$ be sequences $x_n = (x_{n,0}, x_{n,1}, \dots)$
of observations in $O$ such that every $o \in O$ equals $x_{n,t}$ for some $n$ and some $t \le T$.
Consider the EM model of a hidden Markov model on states $S$ and observations $O$ whose latent
variable is the state path $z = (z_0, \dots, z_T)$ and whose joint $p_h(x, z)$ is the path weight,
with EM objective $Q(h' \mid h) = \sum_n \sum_z p_h(z \mid x_n) \log p_{h'}(x_n, z)$, where
$p_h(z \mid x) = p_h(x, z) / \sum_{z'} p_h(x, z')$ is the posterior of the path. Then for all valid
hidden Markov models $h$ and $h'$ (positive initial, transition and emission probabilities, each
distribution summing to one), $Q(h' \mid h) \le Q(\bar h \mid h)$, where $\bar h$ is the
Baum-Welch step applied to $h$ on these data.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.emQ_le_emStep`, a theorem declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#em-q-le-em-step).

## Each Baum-Welch step does not decrease the log-likelihood

Let $S$ and $O$ be finite
sets, let $T \ge 1$, and let $x_1, \dots, x_N$ with $N \ge 1$ be sequences
$x_n = (x_{n,0}, x_{n,1}, \dots)$ of observations in $O$ such that every $o \in O$ equals $x_{n,t}$
for some $n$ and some $t \le T$. For every valid hidden Markov model $h$ on states $S$ and
observations $O$, $\ell(h) \le \ell(\bar h)$, where $\bar h$ is the Baum-Welch step applied to $h$
on these data and $\ell(h) = \sum_{n=1}^{N} \log \sum_z p_h(x_n, z)$ is the log-likelihood of the
EM model of $h$, the sum ranging over state paths $z = (z_0, \dots, z_T)$ and $p_h(x, z)$ being the
path weight.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.logLik_le_emStep`, a theorem declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#log-lik-le-em-step).

## The log-likelihood is monotone along the Baum-Welch iterates

Let $S$ and $O$ be finite
sets, let $T \ge 1$, and let $x_1, \dots, x_N$ with $N \ge 1$ be sequences
$x_n = (x_{n,0}, x_{n,1}, \dots)$ of observations in $O$ such that every $o \in O$ equals $x_{n,t}$
for some $n$ and some $t \le T$. Let $h_0$ be a valid hidden Markov model on states $S$ and
observations $O$ and let $h_t$ be the result of $t$ Baum-Welch steps from $h_0$ on these data.
Then $t \mapsto \ell(h_t)$ is monotone (nondecreasing in $t \in \mathbb{N}$), where
$\ell(h) = \sum_{n=1}^{N} \log \sum_z p_h(x_n, z)$ is the log-likelihood of the EM model of $h$,
the sum ranging over state paths $z = (z_0, \dots, z_T)$ and $p_h(x, z)$ being the path weight.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.logLik_iterate_emStep_monotone`, a theorem declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#log-lik-iterate-em-step-monotone).

## The Baum-Welch log-likelihood is the HMM log-likelihood

Let $S$ and $O$ be finite sets,
let $T$ be a natural number, and let $x_1, \dots, x_N$ be sequences
$x_n = (x_{n,0}, x_{n,1}, \dots)$ of observations in $O$. For every valid hidden Markov model $h$
on states $S$ and observations $O$, the log-likelihood of its EM model (latent state paths
$(z_0, \dots, z_T)$, joint the path weight) on these data equals $\sum_{n=1}^{N} \log L_h(x_n)$,
where $L_h(x_n)$ is the likelihood of the observations $x_{n,0}, \dots, x_{n,T}$ under $h$: the
total path weight over all state paths $(z_0, \dots, z_T)$.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.logLik_eq`, a theorem declared in [CSLibExt/MachineLearning/Sequence/BaumWelch.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelch.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#log-lik-eq).

## Pairwise path sums with a fixed endpoint

Let $h$ be a hidden Markov model with finite
state set $S$, transition weights $a$ and emission weights $b$ in a semiring, and let $x$ be an
observation sequence. For all $k, t \in \mathbb{N}$ and states $s, s', u$, the sum of the path
weights of the state paths $z_0, \dots, z_{t + 1 + k}$ with $z_t = s$, $z_{t + 1} = s'$ and
$z_{t + 1 + k} = u$ equals $\alpha_t(s)\, a(s, s')\, b(s', x(t + 1))\, B_{k, t + 1}(s', u)$, where
$\alpha_t(s)$ is the forward variable and $B_{k, t + 1}(s', u)$ is the bridge weight of the paths
from the state $s'$ at time $t + 1$ to the state $u$ at time $t + 1 + k$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.sum_pathProb_ite_pair`, a theorem declared in [CSLibExt/MachineLearning/Sequence/BaumWelchForwardBackward.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelchForwardBackward.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#sum-path-prob-ite-pair).

## Pairwise state marginal of a hidden Markov model

For a hidden Markov model with finite
state set $S$, an observation sequence $x$, times $t, k \in \mathbb{N}$ and states $s, s'$, the
pairwise marginal is the joint weight of the observations $x(0), \dots, x(t + 1 + k)$ and the
transition $s \to s'$ from time $t$ to time $t + 1$: the sum of the path weights of all state
paths $z_0, \dots, z_{t + 1 + k}$ with $z_t = s$ and $z_{t + 1} = s'$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.pairMarg`, a definition declared in [CSLibExt/MachineLearning/Sequence/BaumWelchForwardBackward.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelchForwardBackward.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#pair-marg).

## Pairwise forward-backward

Let $h$ be a hidden Markov model with finite state set $S$,
transition weights $a$ and emission weights $b$ in a semiring, and let $x$ be an observation
sequence. For all $t, k \in \mathbb{N}$ and states $s, s'$, the joint weight of the observations
$x(0), \dots, x(t + 1 + k)$ and the transition $s \to s'$ from time $t$ to time $t + 1$ equals
$\alpha_t(s)\, a(s, s')\, b(s', x(t + 1))\, \beta_{k, t + 1}(s')$, where $\alpha_t(s)$ is the
forward variable and $\beta_{k, t + 1}(s')$ is the backward variable, the weight of the
observations $x(t + 2), \dots, x(t + 1 + k)$ given the state $s'$ at time $t + 1$.

Formalized by `Cslib.MachineLearning.Sequence.HiddenMarkov.pairMarg_eq`, a theorem declared in [CSLibExt/MachineLearning/Sequence/BaumWelchForwardBackward.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelchForwardBackward.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#pair-marg-eq).

## The expected starts from forward-backward

Let $h$ be a valid hidden Markov model with
finite state set $S$ and finite observation set $O$, let $T \in \mathbb{N}$, and let
$x_0, \dots, x_{N-1}$ be observation sequences. For a sequence $x_n$ write $\alpha^n_0(s)$ for its
forward variable at time $0$ and state $s$, $\beta^n_{T,0}(s)$ for its backward variable from
time $0$ with $T$ remaining steps (the weight of the observations $x_n(1), \dots, x_n(T)$ given the
state $s$ at time $0$), and $L_n$ for the likelihood of $x_n(0), \dots, x_n(T)$. Then for every
state $s$, the expected number of sequences whose state path of length $T + 1$ starts in $s$,
under the posterior of $h$, is $\sum_{n < N} \alpha^n_0(s)\, \beta^n_{T,0}(s) / L_n$.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.initCount_eq`, a theorem declared in [CSLibExt/MachineLearning/Sequence/BaumWelchForwardBackward.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelchForwardBackward.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#init-count-eq).

## The expected emissions from forward-backward

Let $h$ be a valid hidden Markov model with
finite state set $S$ and finite observation set $O$, let $T \in \mathbb{N}$, and let
$x_0, \dots, x_{N-1}$ be observation sequences. For a sequence $x_n$ write $\alpha^n_t(s)$ for its
forward variable at time $t$ and state $s$, $\beta^n_{k,t}(s)$ for its backward variable (the
weight of the observations $x_n(t + 1), \dots, x_n(t + k)$ given the state $s$ at time $t$), and
$L_n$ for the likelihood of $x_n(0), \dots, x_n(T)$. Then for every state $s$ and observation $o$,
the expected number of emissions of $o$ from $s$ along state paths of length $T + 1$, summed over
the sequences under the posterior of $h$, is
$\sum_{n < N} \sum_{t \le T,\ x_n(t) = o} \alpha^n_t(s)\, \beta^n_{T - t, t}(s) / L_n$.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.emitCount_eq`, a theorem declared in [CSLibExt/MachineLearning/Sequence/BaumWelchForwardBackward.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelchForwardBackward.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#emit-count-eq).

## The expected transitions from forward-backward

Let $h$ be a valid hidden Markov model
with finite state set $S$, finite observation set $O$, transition weights $a$ and emission
weights $b$, let $T \in \mathbb{N}$, and let $x_0, \dots, x_{N-1}$ be observation sequences. For a
sequence $x_n$ write $\alpha^n_t(s)$ for its forward variable at time $t$ and state $s$,
$\beta^n_{k,t}(s)$ for its backward variable (the weight of the observations
$x_n(t + 1), \dots, x_n(t + k)$ given the state $s$ at time $t$), and $L_n$ for the likelihood of
$x_n(0), \dots, x_n(T)$. Then for all states $s, s'$, the expected number of transitions
$s \to s'$ along state paths of length $T + 1$, summed over the sequences under the posterior of
$h$, is
$\sum_{n < N} \sum_{t < T} \alpha^n_t(s)\, a(s, s')\, b(s', x_n(t + 1))\,
\beta^n_{T - t - 1, t + 1}(s') / L_n$.

Each summand is Rabiner's $\xi_t(s, s')$ for the sequence $x_n$.

Formalized by `Cslib.MachineLearning.Sequence.BaumWelch.transCount_eq`, a theorem declared in [CSLibExt/MachineLearning/Sequence/BaumWelchForwardBackward.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sequence/BaumWelchForwardBackward.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html#trans-count-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Baum–Welch algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/baum-welch-algorithm)
