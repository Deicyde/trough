---
declaration: section
origin: cited
lean: Cslib.MachineLearning.Sampling.coin, Cslib.MachineLearning.Sampling.acceptProb, Cslib.MachineLearning.Sampling.trial, Cslib.MachineLearning.Sampling.trial_apply_true, Cslib.MachineLearning.Sampling.tsum_trial_true, Cslib.MachineLearning.Sampling.tsum_trial_false_add, Cslib.MachineLearning.Sampling.trial_true_div_tsum, Cslib.MachineLearning.Sampling.tsum_rejections_mul_trial
statement: formalized
proof: formalized
---

# Rejection sampling

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/rejection-sampling/index.html).

## Biased coin

For $r \in [0, \infty]$ with $r \le 1$, the biased coin with parameter $r$ is
the probability mass function on $\{\mathrm{true}, \mathrm{false}\}$ that gives $\mathrm{true}$
probability $r$ and $\mathrm{false}$ probability $1 - r$.

Formalized by `Cslib.MachineLearning.Sampling.coin`, a definition declared in [CSLibExt/MachineLearning/Sampling/Rejection.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/Rejection.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/rejection-sampling/index.html#coin).

## Acceptance probability

Given probability mass functions $p$ and $q$ on a type $\alpha$, a
constant $M \in [0, \infty]$ and a point $x \in \alpha$, the acceptance probability of the proposal
$x$ is $p(x) / (M\,q(x))$, computed in $[0, \infty]$, where $a / 0 = \infty$ for $a \ne 0$ and
$0 / 0 = 0$.

Formalized by `Cslib.MachineLearning.Sampling.acceptProb`, a definition declared in [CSLibExt/MachineLearning/Sampling/Rejection.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/Rejection.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/rejection-sampling/index.html#accept-prob).

## One round of rejection sampling

Let $p$ and $q$ be probability mass functions on a type
$\alpha$ (the target and the proposal) and let $M \in [0, \infty]$ be an envelope constant with
$p(x) \le M\,q(x)$ for all $x \in \alpha$. One round of rejection sampling for target $p$, proposal
$q$ and envelope $M$ is the probability mass function on pairs
$(x, b) \in \alpha \times \{\mathrm{true}, \mathrm{false}\}$ obtained by drawing $x$ from $q$ and
then flipping a coin that lands $b = \mathrm{true}$ ("accepted") with probability
$p(x) / (M\,q(x))$.

Formalized by `Cslib.MachineLearning.Sampling.trial`, a definition declared in [CSLibExt/MachineLearning/Sampling/Rejection.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/Rejection.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/rejection-sampling/index.html#trial).

## Probability that a round proposes and accepts a given point

Let $p$ and $q$ be probability
mass functions on $\alpha$ and $M \in [0, \infty]$ with $p(y) \le M\,q(y)$ for all $y \in \alpha$.
For every $x \in \alpha$, one round of rejection sampling for target $p$, proposal $q$ and envelope
$M$ yields the pair $(x, \mathrm{true})$, that is, proposes $x$ and accepts it, with probability
$p(x) / M$.

Formalized by `Cslib.MachineLearning.Sampling.trial_apply_true`, a theorem declared in [CSLibExt/MachineLearning/Sampling/Rejection.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/Rejection.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/rejection-sampling/index.html#trial-apply-true).

## Probability that a round accepts

Let $p$ and $q$ be probability mass functions on $\alpha$
and $M \in [0, \infty]$ with $p(x) \le M\,q(x)$ for all $x \in \alpha$. The sum over $x \in \alpha$
of the probabilities that one round of rejection sampling for target $p$, proposal $q$ and
envelope $M$ yields $(x, \mathrm{true})$ equals $M^{-1}$; that is, a round accepts with
probability $1 / M$.

Formalized by `Cslib.MachineLearning.Sampling.tsum_trial_true`, a theorem declared in [CSLibExt/MachineLearning/Sampling/Rejection.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/Rejection.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/rejection-sampling/index.html#tsum-trial-true).

## Probability that a round rejects

Let $p$ and $q$ be probability mass functions on $\alpha$
and $M \in [0, \infty]$ with $p(x) \le M\,q(x)$ for all $x \in \alpha$. Let $r$ be the sum over
$x \in \alpha$ of the probabilities that one round of rejection sampling for target $p$, proposal
$q$ and envelope $M$ yields $(x, \mathrm{false})$, that is, the probability that the round rejects.
Then $r + M^{-1} = 1$.

Formalized by `Cslib.MachineLearning.Sampling.tsum_trial_false_add`, a theorem declared in [CSLibExt/MachineLearning/Sampling/Rejection.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/Rejection.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/rejection-sampling/index.html#tsum-trial-false-add).

## Conditional on acceptance, the proposal has the target law

Let $p$ and $q$ be probability
mass functions on $\alpha$ and $M \in [0, \infty]$ with $M \ne 0$, $M \ne \infty$ and
$p(y) \le M\,q(y)$ for all $y \in \alpha$. For one round of rejection sampling for target $p$,
proposal $q$ and envelope $M$, write $P(x, \mathrm{accepted})$ for the probability that the round
proposes $x$ and accepts it, and
$P(\mathrm{accepted}) = \sum_{y \in \alpha} P(y, \mathrm{accepted})$. Then
$P(x, \mathrm{accepted}) / P(\mathrm{accepted}) = p(x)$ for every $x \in \alpha$.

Formalized by `Cslib.MachineLearning.Sampling.trial_true_div_tsum`, a theorem declared in [CSLibExt/MachineLearning/Sampling/Rejection.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/Rejection.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/rejection-sampling/index.html#trial-true-div-tsum).

## Rejection sampling outputs the target law

Let $p$ and $q$ be probability mass functions on
$\alpha$ and $M \in [0, \infty]$ with $M \ne 0$, $M \ne \infty$ and $p(y) \le M\,q(y)$ for all
$y \in \alpha$. For one round of rejection sampling for target $p$, proposal $q$ and envelope $M$,
write $P(x, \mathrm{accepted})$ for the probability that the round proposes $x$ and accepts it, and
$r$ for the sum over $y \in \alpha$ of the probabilities that it proposes $y$ and rejects it. Then
for every $x \in \alpha$,

$$\sum_{k=0}^{\infty} r^k \, P(x, \mathrm{accepted}) = p(x).$$

Here $r^k \, P(x, \mathrm{accepted})$ is the probability that repeating independent rounds until
one accepts outputs $x$ after exactly $k$ rejections, so the output of that loop has law $p$.

Formalized by `Cslib.MachineLearning.Sampling.tsum_rejections_mul_trial`, a theorem declared in [CSLibExt/MachineLearning/Sampling/Rejection.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/Rejection.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/rejection-sampling/index.html#tsum-rejections-mul-trial).

## Uniqueness for the first-step equation of rejection sampling

Let $p$ and $q$ be
probability mass functions on $\alpha$ and $M \in [0, \infty]$ with $M \ne 0$, $M \ne \infty$ and
$p(y) \le M\,q(y)$ for all $y \in \alpha$. For one round of rejection sampling for target $p$,
proposal $q$ and envelope $M$, write $P(x, \mathrm{accepted})$ for the probability that the round
proposes $x$ and accepts it, and $r$ for the sum over $y \in \alpha$ of the probabilities that it
proposes $y$ and rejects it. If $f \colon \alpha \to [0, \infty]$ takes only finite values and
satisfies $f(x) = P(x, \mathrm{accepted}) + r \, f(x)$ for every $x \in \alpha$, then $f(x) = p(x)$
for every $x \in \alpha$.

The law of the output of the loop that repeats independent rounds until one accepts satisfies this
first-step equation, so this result identifies that law as $p$.

Formalized by `Cslib.MachineLearning.Sampling.eq_of_firstStep`, a theorem declared in [CSLibExt/MachineLearning/Sampling/Rejection.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/Rejection.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/rejection-sampling/index.html#eq-of-first-step).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rejection sampling](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/rejection-sampling/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/rejection-sampling)
