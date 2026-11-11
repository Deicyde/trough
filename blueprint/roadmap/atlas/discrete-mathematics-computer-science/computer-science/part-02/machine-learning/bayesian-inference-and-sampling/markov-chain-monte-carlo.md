---
declaration: section
origin: cited
lean: Cslib.MachineLearning.Sampling.pmfKernel, Cslib.MachineLearning.Sampling.isReversible_pmfKernel, Cslib.MachineLearning.Sampling.invariant_pmfKernel, Cslib.MachineLearning.Sampling.bind_eq_of_detailedBalance, Cslib.MachineLearning.Sampling.mhAccept, Cslib.MachineLearning.Sampling.mhStep, Cslib.MachineLearning.Sampling.mh_detailedBalance, Cslib.MachineLearning.Sampling.isReversible_mhKernel
statement: formalized
proof: formalized
---

# Markov chain Monte Carlo

30 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html).

## Markov kernel of a transition rule

Let $\alpha$ be a finite state space with a measurable
structure in which singletons are measurable. A transition rule $P$ assigning to each $x \in \alpha$
a probability distribution $P(x, \cdot)$ on $\alpha$ gives the Markov kernel on $\alpha$ that sends
$x$ to $P(x, \cdot)$ viewed as a probability measure, so a set $B$ gets mass
$\sum_{y \in B} P(x, y)$.

Formalized by `Cslib.MachineLearning.Sampling.pmfKernel`, a definition declared in [CSLibExt/MachineLearning/Sampling/MetropolisHastings.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MetropolisHastings.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#pmf-kernel).

## Detailed balance implies reversibility

Let $\alpha$ be a finite state space with a
measurable structure in which singletons are measurable, $\pi$ a probability distribution on
$\alpha$ and $P$ a transition rule assigning to each $x \in \alpha$ a probability distribution
$P(x, \cdot)$ on $\alpha$. If $\pi(x) P(x, y) = \pi(y) P(y, x)$ for all $x, y \in \alpha$, then
the Markov kernel $\kappa$ of $P$ is reversible with respect to $\pi$, viewed as a measure: for
all measurable sets $A$ and $B$,
$\int_A \kappa(x, B) \, d\pi(x) = \int_B \kappa(x, A) \, d\pi(x)$.

Formalized by `Cslib.MachineLearning.Sampling.isReversible_pmfKernel`, a theorem declared in [CSLibExt/MachineLearning/Sampling/MetropolisHastings.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MetropolisHastings.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#is-reversible-pmf-kernel).

## Detailed balance implies invariance

Let $\alpha$ be a finite state space with a measurable
structure in which singletons are measurable, $\pi$ a probability distribution on $\alpha$ and $P$
a transition rule assigning to each $x \in \alpha$ a probability distribution $P(x, \cdot)$ on
$\alpha$. If $\pi(x) P(x, y) = \pi(y) P(y, x)$ for all $x, y \in \alpha$, then $\pi$, viewed as a
measure, is invariant for the Markov kernel $\kappa$ of $P$: for every measurable set $B$,
$\int \kappa(x, B) \, d\pi(x) = \pi(B)$.

Formalized by `Cslib.MachineLearning.Sampling.invariant_pmfKernel`, a theorem declared in [CSLibExt/MachineLearning/Sampling/MetropolisHastings.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MetropolisHastings.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#invariant-pmf-kernel).

## Detailed balance gives a stationary distribution

Let $\alpha$ be a finite set, $\pi$ a
probability distribution on $\alpha$ and $P$ a transition rule assigning to each $x \in \alpha$ a
probability distribution $P(x, \cdot)$ on $\alpha$. If $\pi(x) P(x, y) = \pi(y) P(y, x)$ for all
$x, y \in \alpha$, then one step of $P$ started from $\pi$ is again distributed as $\pi$: for every
$y \in \alpha$, $\sum_{x \in \alpha} \pi(x) P(x, y) = \pi(y)$.

Formalized by `Cslib.MachineLearning.Sampling.bind_eq_of_detailedBalance`, a theorem declared in [CSLibExt/MachineLearning/Sampling/MetropolisHastings.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MetropolisHastings.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#bind-eq-of-detailed-balance).

## Metropolis–Hastings acceptance probability

For a probability distribution $\pi$ on
$\alpha$ and a proposal $Q$ assigning to each $x \in \alpha$ a probability distribution
$Q(x, \cdot)$ on $\alpha$, the acceptance probability of a move from $x$ to $y$ is
$a(x, y) = \min\bigl(1, \pi(y) Q(y, x) / (\pi(x) Q(x, y))\bigr)$, computed in $[0, \infty]$
with $c / 0 = \infty$ for $c \ne 0$ and $0 / 0 = 0$.

Formalized by `Cslib.MachineLearning.Sampling.mhAccept`, a definition declared in [CSLibExt/MachineLearning/Sampling/MetropolisHastings.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MetropolisHastings.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#mh-accept).

## Metropolis–Hastings step

For a probability distribution $\pi$ on $\alpha$ (the target)
and a proposal $Q$ assigning to each $x \in \alpha$ a probability distribution $Q(x, \cdot)$ on
$\alpha$, one Metropolis–Hastings step from $x$ is the distribution of the following move: draw
$y$ from $Q(x, \cdot)$, then move to $y$ with the Metropolis–Hastings acceptance probability
$a(x, y)$, and otherwise stay at $x$.

Formalized by `Cslib.MachineLearning.Sampling.mhStep`, a definition declared in [CSLibExt/MachineLearning/Sampling/MetropolisHastings.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MetropolisHastings.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#mh-step).

## Detailed balance for Metropolis–Hastings

Let $\pi$ be a probability distribution on a
type $\alpha$, $Q$ a proposal assigning to each $x \in \alpha$ a probability distribution
$Q(x, \cdot)$ on $\alpha$, and $P(x, y)$ the probability that one Metropolis–Hastings step for
target $\pi$ and proposal $Q$ moves from $x$ to $y$. Then $\pi(x) P(x, y) = \pi(y) P(y, x)$ for
all $x, y \in \alpha$.

For $x \ne y$ both sides equal $\min(\pi(x) Q(x, y), \pi(y) Q(y, x))$; no positivity or symmetry
assumption on $\pi$ or $Q$ is needed.

Formalized by `Cslib.MachineLearning.Sampling.mh_detailedBalance`, a theorem declared in [CSLibExt/MachineLearning/Sampling/MetropolisHastings.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MetropolisHastings.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#mh-detailed-balance).

## The Metropolis–Hastings kernel is reversible

Let $\alpha$ be a finite state space with a
measurable structure in which singletons are measurable, $\pi$ a probability distribution on
$\alpha$ and $Q$ a proposal assigning to each $x \in \alpha$ a probability distribution
$Q(x, \cdot)$ on $\alpha$. Then the Markov kernel $\kappa$ of the Metropolis–Hastings step for
target $\pi$ and proposal $Q$ is reversible with respect to $\pi$, viewed as a measure: for all
measurable sets $A$ and $B$, $\int_A \kappa(x, B) \, d\pi(x) = \int_B \kappa(x, A) \, d\pi(x)$.

Formalized by `Cslib.MachineLearning.Sampling.isReversible_mhKernel`, a theorem declared in [CSLibExt/MachineLearning/Sampling/MetropolisHastings.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MetropolisHastings.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#is-reversible-mh-kernel).

## The target is stationary for Metropolis–Hastings

Let $\alpha$ be a finite state space
with a measurable structure in which singletons are measurable, $\pi$ a probability distribution
on $\alpha$ and $Q$ a proposal assigning to each $x \in \alpha$ a probability distribution
$Q(x, \cdot)$ on $\alpha$. Then $\pi$, viewed as a measure, is invariant for the Markov kernel
$\kappa$ of the Metropolis–Hastings step for target $\pi$ and proposal $Q$: for every measurable
set $B$, $\int \kappa(x, B) \, d\pi(x) = \pi(B)$.

No positivity or symmetry assumption on $\pi$ or $Q$ is needed.

Formalized by `Cslib.MachineLearning.Sampling.invariant_mhKernel`, a theorem declared in [CSLibExt/MachineLearning/Sampling/MetropolisHastings.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MetropolisHastings.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#invariant-mh-kernel).

## Normalizer of the conditional law

Let $\pi$ be a probability distribution on the
configurations $x : \iota \to S$, with $\iota$ and $S$ finite. For a coordinate $i \in \iota$ and a
configuration $x$, the normalizer is $Z_i(x) = \sum_{s \in S} \pi(x[i \mapsto s]) \in [0, \infty]$,
where $x[i \mapsto s]$ is $x$ with coordinate $i$ set to $s$. It normalizes the conditional law of
coordinate $i$ given the other coordinates of $x$.

Formalized by `Cslib.MachineLearning.Sampling.condNorm`, a definition declared in [CSLibExt/MachineLearning/Sampling/GibbsSampling.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/GibbsSampling.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#cond-norm).

## Conditional law of a coordinate

Let $\pi$ be a probability distribution on the
configurations $x : \iota \to S$, with $\iota$ and $S$ finite, such that $\pi(x) \neq 0$ for every
$x$. For a coordinate $i \in \iota$ and a configuration $x$, the conditional law of coordinate $i$
given the others is the probability distribution on $S$ that gives $s \in S$ the mass
$\pi(x[i \mapsto s]) / Z_i(x)$, where $x[i \mapsto s]$ is $x$ with coordinate $i$ set to $s$ and
$Z_i(x) = \sum_{t \in S} \pi(x[i \mapsto t])$. In the usual notation this is
$\pi(x_i = s \mid x_{-i})$, where $x_i$ is coordinate $i$ of $x$ and $x_{-i}$ is the family of
its other coordinates.

Formalized by `Cslib.MachineLearning.Sampling.condLaw`, a definition declared in [CSLibExt/MachineLearning/Sampling/GibbsSampling.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/GibbsSampling.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#cond-law).

## Gibbs update

Let $\pi$ be a probability distribution on the configurations
$x : \iota \to S$, with $\iota$ and $S$ finite, such that $\pi(x) \neq 0$ for every $x$. The Gibbs
update of coordinate $i \in \iota$ from $x$ is the probability distribution of $x[i \mapsto s]$,
the configuration $x$ with coordinate $i$ set to $s$, where $s$ is drawn from the conditional law
of coordinate $i$ given the other coordinates of $x$.

Formalized by `Cslib.MachineLearning.Sampling.gibbsStep`, a definition declared in [CSLibExt/MachineLearning/Sampling/GibbsSampling.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/GibbsSampling.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#gibbs-step).

## Symmetry of differing in one coordinate

For functions $x, y : \iota \to S$ and a coordinate
$i \in \iota$, if setting coordinate $i$ of $x$ to $y(i)$ gives $y$, then setting coordinate $i$ of
$y$ to $x(i)$ gives $x$.

Formalized by `Cslib.MachineLearning.Sampling.update_eq_comm`, a theorem declared in [CSLibExt/MachineLearning/Sampling/GibbsSampling.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/GibbsSampling.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#update-eq-comm).

## Detailed balance for a Gibbs update

Let $\pi$ be a probability distribution on the
configurations $x : \iota \to S$, with $\iota$ and $S$ finite, such that $\pi(x) \neq 0$ for every
$x$, and for a coordinate $i$ let $P_i(x, y)$ be the probability that the Gibbs update of
coordinate $i$ moves $x$ to $y$. Then $\pi(x) P_i(x, y) = \pi(y) P_i(y, x)$ for all
configurations $x$ and $y$.

When $x$ and $y$ differ at most in coordinate $i$, both sides equal $\pi(x) \pi(y) / Z$ for the
same normalizer $Z$; otherwise both sides are $0$.

Formalized by `Cslib.MachineLearning.Sampling.gibbs_detailedBalance`, a theorem declared in [CSLibExt/MachineLearning/Sampling/GibbsSampling.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/GibbsSampling.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#gibbs-detailed-balance).

## Gibbs updates are reversible

Let $\pi$ be a probability distribution on the
configurations $x : \iota \to S$, with $\iota$ and $S$ finite, such that $\pi(x) \neq 0$ for every
$x$. For every coordinate $i$, the Markov kernel $K$ of the Gibbs update of coordinate $i$ is
reversible with respect to $\pi$: for all measurable sets $A$ and $B$ of configurations,
$\int_A K(x, B) \, d\pi(x) = \int_B K(x, A) \, d\pi(x)$.

Formalized by `Cslib.MachineLearning.Sampling.isReversible_gibbsKernel`, a theorem declared in [CSLibExt/MachineLearning/Sampling/GibbsSampling.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/GibbsSampling.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#is-reversible-gibbs-kernel).

## Gibbs sampling leaves the target stationary

Let $\pi$ be a probability distribution on
the configurations $x : \iota \to S$, with $\iota$ and $S$ finite, such that $\pi(x) \neq 0$ for
every $x$. For every coordinate $i$, $\pi$ is an invariant measure of the Markov kernel of the
Gibbs update of coordinate $i$: if $x$ is drawn from $\pi$ and coordinate $i$ is resampled from
its conditional law given the other coordinates, the result is again distributed as $\pi$.

Formalized by `Cslib.MachineLearning.Sampling.invariant_gibbsKernel`, a theorem declared in [CSLibExt/MachineLearning/Sampling/GibbsSampling.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/GibbsSampling.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#invariant-gibbs-kernel).

## Systematic-scan Gibbs sampler

Let $\pi$ be a probability distribution on the
configurations $x : \iota \to S$, with $\iota$ and $S$ finite, such that $\pi(x) \neq 0$ for every
$x$. For a list $l = (i_1, \dots, i_n)$ of coordinates, the systematic-scan Gibbs sampler is the
Markov kernel on configurations that applies the Gibbs updates of the coordinates
$i_1, i_2, \dots, i_n$ in this order; for the empty list it is the identity kernel.

Formalized by `Cslib.MachineLearning.Sampling.gibbsSweep`, a definition declared in [CSLibExt/MachineLearning/Sampling/GibbsSampling.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/GibbsSampling.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#gibbs-sweep).

## First step of a Gibbs sweep

Let $\pi$ be a probability distribution on the configurations
$x : \iota \to S$, with $\iota$ and $S$ finite, such that $\pi(x) \neq 0$ for every $x$. For a list
$l$ of coordinates let $K_l$ be the systematic-scan Gibbs sampler for $l$, and for a coordinate $i$
let $P_i$ be the Markov kernel of the Gibbs update of coordinate $i$. Then for every configuration
$x$, the law $K_{(i, l)}(x)$ of the sampler for the list $(i, l)$ obtained by putting $i$ in front
of $l$ is the mixture $\int K_l(y) \, P_i(x, dy)$: first coordinate $i$ is updated, then the sweep
$l$ runs from the result.

Formalized by `Cslib.MachineLearning.Sampling.gibbsSweep_cons_apply`, a theorem declared in [CSLibExt/MachineLearning/Sampling/GibbsSampling.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/GibbsSampling.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#gibbs-sweep-cons-apply).

## A full Gibbs sweep leaves the target stationary

Let $\pi$ be a probability distribution on
the configurations $x : \iota \to S$, with $\iota$ and $S$ finite, such that $\pi(x) \neq 0$ for
every $x$. For every finite list $l$ of coordinates, in any order and possibly with repetitions,
$\pi$ is an invariant measure of the systematic-scan Gibbs sampler that updates the coordinates in
the order of $l$.

Formalized by `Cslib.MachineLearning.Sampling.invariant_gibbsSweep`, a theorem declared in [CSLibExt/MachineLearning/Sampling/GibbsSampling.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/GibbsSampling.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#invariant-gibbs-sweep).

## Probabilities of a finite law sum to one

The probabilities of a law on a finite type, as reals, sum to `1`.

Formalized by `Cslib.MachineLearning.Sampling.sum_toReal_pmf`, a theorem declared in [CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#sum-to-real-pmf).

## Metropolis–Hastings transition matrix

The transition matrix `P(x, y) = mhStep π Q x y` of the Metropolis–Hastings chain, as a real
matrix.

Formalized by `Cslib.MachineLearning.Sampling.mhMatrix`, a definition declared in [CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#mh-matrix).

## Metropolis–Hastings matrix is stochastic

The Metropolis–Hastings matrix is stochastic.

Formalized by `Cslib.MachineLearning.Sampling.mhMatrix_mem_rowStochastic`, a theorem declared in [CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#mh-matrix-mem-row-stochastic).

## Target is stationary for the Metropolis–Hastings matrix

The target is stationary for the Metropolis–Hastings matrix.

Formalized by `Cslib.MachineLearning.Sampling.vecMul_mhMatrix`, a theorem declared in [CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#vec-mul-mh-matrix).

## Primitivity of the Metropolis–Hastings matrix

For a target with full support and a proposal with primitive transition matrix and symmetric
support, the Metropolis–Hastings matrix is primitive.

Formalized by `Cslib.MachineLearning.Sampling.isPrimitive_mhMatrix`, a theorem declared in [CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#is-primitive-mh-matrix).

## The Metropolis–Hastings chain converges to its target

Under the hypotheses of
`isPrimitive_mhMatrix`, there are `C` and `0 ≤ ρ < 1` with `d_TV(Pⁿ(x, ·), π) ≤ C ρⁿ` for every
start `x`.

Formalized by `Cslib.MachineLearning.Sampling.exists_tvDist_mhMatrix_pow_le`, a theorem declared in [CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#exists-tv-dist-mh-matrix-pow-le).

## Transition matrix of the systematic-scan Gibbs sweep

The transition matrix `P(x, y) = gibbsSweep π hπ l x {y}` of the systematic-scan Gibbs
sweep along `l`, as a real matrix.

Formalized by `Cslib.MachineLearning.Sampling.gibbsSweepMatrix`, a definition declared in [CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#gibbs-sweep-matrix).

## Gibbs sweep matrix is stochastic

The Gibbs sweep matrix is stochastic.

Formalized by `Cslib.MachineLearning.Sampling.gibbsSweepMatrix_mem_rowStochastic`, a theorem declared in [CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#gibbs-sweep-matrix-mem-row-stochastic).

## Target is stationary for the Gibbs sweep matrix

The target is stationary for the Gibbs sweep matrix.

Formalized by `Cslib.MachineLearning.Sampling.vecMul_gibbsSweepMatrix`, a theorem declared in [CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#vec-mul-gibbs-sweep-matrix).

## Positivity of Gibbs sweep transition probabilities

If the sweep visits every coordinate, every transition probability of the sweep is
positive.

Formalized by `Cslib.MachineLearning.Sampling.gibbsSweepMatrix_pos`, a theorem declared in [CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#gibbs-sweep-matrix-pos).

## The systematic-scan Gibbs sampler converges to its target

If the sweep visits every
coordinate, there are `C` and `0 ≤ ρ < 1` with `d_TV(Pⁿ(x, ·), π) ≤ C ρⁿ` for every start `x`.

Formalized by `Cslib.MachineLearning.Sampling.exists_tvDist_gibbsSweepMatrix_pow_le`, a theorem declared in [CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MCMCConvergence.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html#exists-tv-dist-gibbs-sweep-matrix-pow-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Markov chain Monte Carlo](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/markov-chain-monte-carlo)
