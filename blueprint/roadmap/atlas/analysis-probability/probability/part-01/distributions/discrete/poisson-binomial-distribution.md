---
declaration: section
origin: cited
lean: ProbabilityTheory.IsBernoulliRV, ProbabilityTheory.IsBernoulliRV.nonneg, ProbabilityTheory.IsBernoulliRV.le_one, ProbabilityTheory.IsBernoulliRV.hasLaw, ProbabilityTheory.IsBernoulliRV.measure_zero, ProbabilityTheory.IsBernoulliRV.measure_one, ProbabilityTheory.bernoulli_sum_pmf, ProbabilityTheory.bernoulli_sum_pmf_iid
statement: formalized
proof: formalized
---

# Poisson binomial distribution

24 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html).

## Bernoulli random variable

Let $\mu$ be a measure on a measurable space $\Omega$, let
$X : \Omega \to \mathbb{N}$ and let $p$ be a real number. Then $X$ is a Bernoulli random
variable with parameter $p$ under $\mu$ when $0 \le p \le 1$, $X$ is $\mu$-almost everywhere
measurable, and the pushforward of $\mu$ along $X$ is the Bernoulli distribution
$p\,\delta_1 + (1 - p)\,\delta_0$ on $\mathbb{N}$, which gives mass $p$ to $1$, mass $1 - p$
to $0$ and no mass elsewhere.

Formalized by `ProbabilityTheory.IsBernoulliRV`, a definition declared in [MathlibExt/Probability/BernoulliSumPmf.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BernoulliSumPmf.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#is-bernoulli-rv).

## Bernoulli parameters are nonnegative

If $X$ is a Bernoulli random variable with
parameter $p$ under a measure $\mu$, then $0 \le p$.

Formalized by `ProbabilityTheory.IsBernoulliRV.nonneg`, a lemma declared in [MathlibExt/Probability/BernoulliSumPmf.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BernoulliSumPmf.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#nonneg).

## Bernoulli parameters are at most one

If $X$ is a Bernoulli random variable with
parameter $p$ under a measure $\mu$, then $p \le 1$.

Formalized by `ProbabilityTheory.IsBernoulliRV.le_one`, a lemma declared in [MathlibExt/Probability/BernoulliSumPmf.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BernoulliSumPmf.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#le-one).

## Law of a Bernoulli random variable

If $X : \Omega \to \mathbb{N}$ is a Bernoulli random
variable with parameter $p$ under a measure $\mu$, then $X$ is $\mu$-almost everywhere
measurable and its law under $\mu$, the pushforward of $\mu$ along $X$, is the Bernoulli
distribution $p\,\delta_1 + (1 - p)\,\delta_0$ on $\mathbb{N}$.

Formalized by `ProbabilityTheory.IsBernoulliRV.hasLaw`, a lemma declared in [MathlibExt/Probability/BernoulliSumPmf.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BernoulliSumPmf.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#has-law).

## Probability that a Bernoulli variable equals zero

If $X : \Omega \to \mathbb{N}$ is a
Bernoulli random variable with parameter $p$ under a measure $\mu$, then
$\mu(\{\omega : X(\omega) = 0\}) = 1 - p$, as an extended nonnegative real.

Formalized by `ProbabilityTheory.IsBernoulliRV.measure_zero`, a lemma declared in [MathlibExt/Probability/BernoulliSumPmf.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BernoulliSumPmf.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#measure-zero).

## Probability that a Bernoulli variable equals one

If $X : \Omega \to \mathbb{N}$ is a
Bernoulli random variable with parameter $p$ under a measure $\mu$, then
$\mu(\{\omega : X(\omega) = 1\}) = p$, as an extended nonnegative real.

Formalized by `ProbabilityTheory.IsBernoulliRV.measure_one`, a lemma declared in [MathlibExt/Probability/BernoulliSumPmf.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BernoulliSumPmf.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#measure-one).

## Distribution of a sum of independent Bernoulli variables

Let $\mu$ be a probability
measure on a measurable space $\Omega$, let $m \in \mathbb{N}$, and let
$X_1, \dots, X_m : \Omega \to \mathbb{N}$ be measurable, mutually independent random variables
such that each $X_i$ is a Bernoulli random variable with real parameter $p_i$ under $\mu$.
Then for every $j \in \mathbb{N}$ the probability that $X_1 + \dots + X_m = j$ equals

$$
\sum_{A \subseteq \{1, \dots, m\},\ |A| = j} \ \prod_{i \in A} p_i \prod_{i \notin A} (1 - p_i).
$$

This is the Poisson binomial distribution.

Formalized by `ProbabilityTheory.bernoulli_sum_pmf`, a theorem declared in [MathlibExt/Probability/BernoulliSumPmf.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BernoulliSumPmf.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#bernoulli-sum-pmf).

## Binomial distribution of a sum of i.i.d. Bernoulli variables

Let $\mu$ be a
probability measure on a measurable space $\Omega$, let $m \in \mathbb{N}$, let $p$ be a real
number, and let $X_1, \dots, X_m : \Omega \to \mathbb{N}$ be measurable, mutually independent
random variables, each a Bernoulli random variable with parameter $p$ under $\mu$. Then for
every $j \in \mathbb{N}$ the probability that $X_1 + \dots + X_m = j$ is
$\binom{m}{j} p^j (1 - p)^{m - j}$, where the exponent $m - j$ is taken to be $0$ when $j > m$.

Formalized by `ProbabilityTheory.bernoulli_sum_pmf_iid`, a theorem declared in [MathlibExt/Probability/BernoulliSumPmf.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BernoulliSumPmf.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#bernoulli-sum-pmf-iid).

## Poisson-binomial mass function

Poisson-binomial mass function of the number of successes among independent trials with
success probabilities `p : Fin m → ℝ`:
`∑_{A ⊆ [m], |A| = j} ∏_{i ∈ A} p i ∏_{i ∉ A} (1 - p i)`. A probability mass function when
every `p i ∈ [0, 1]`; the algebraic identities below hold for all real `p`.

Formalized by `ProbabilityTheory.poissonBinomialPMF`, a definition declared in [MathlibExt/Probability/Distributions/PoissonBinomial.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonBinomial.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#poisson-binomial-pmf).

## Upper tail of the Poisson-binomial law

Upper tail `P(S ≥ k) = ∑_{k ≤ j ≤ m} P(S = j)` of the Poisson-binomial law (the mass
function vanishes above `m`).

Formalized by `ProbabilityTheory.poissonBinomialTail`, a definition declared in [MathlibExt/Probability/Distributions/PoissonBinomial.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonBinomial.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#poisson-binomial-tail).

## Nonnegativity of the Poisson-binomial mass function

The Poisson-binomial mass function is nonnegative for probabilities in `[0, 1]`.

Formalized by `ProbabilityTheory.poissonBinomialPMF_nonneg`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonBinomial.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonBinomial.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#poisson-binomial-pmf-nonneg).

## Poisson-binomial mass vanishes above the number of trials

The Poisson-binomial mass function vanishes above the number of trials.

Formalized by `ProbabilityTheory.poissonBinomialPMF_eq_zero_of_lt`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonBinomial.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonBinomial.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#poisson-binomial-pmf-eq-zero-of-lt).

## Poisson-binomial mass at zero after adding a trial

Adding a trial with probability `a`: no successes requires a failure of the new trial.

Formalized by `ProbabilityTheory.poissonBinomialPMF_cons_zero`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonBinomial.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonBinomial.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#poisson-binomial-pmf-cons-zero).

## First-step recurrence for the Poisson-binomial mass function

Adding a trial with probability `a`: first-step decomposition of the mass function,
`P(S' = j + 1) = a P(S = j) + (1 - a) P(S = j + 1)`.

Formalized by `ProbabilityTheory.poissonBinomialPMF_cons_succ`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonBinomial.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonBinomial.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#poisson-binomial-pmf-cons-succ).

## Poisson-binomial masses sum to one

The Poisson-binomial masses sum to one (an identity for all real `p`; it is the expansion
of `∏ ((1 - p i) + p i) = 1`).

Formalized by `ProbabilityTheory.sum_poissonBinomialPMF`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonBinomial.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonBinomial.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#sum-poisson-binomial-pmf).

## Peeling off the lowest term of the Poisson-binomial tail

Peeling off the lowest term of the tail: `P(S ≥ k) = P(S = k) + P(S ≥ k + 1)`.

Formalized by `ProbabilityTheory.poissonBinomialTail_eq_add`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonBinomial.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonBinomial.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#poisson-binomial-tail-eq-add).

## Poisson-binomial tail after adding a trial

Adding a trial with probability `a` raises the upper tail by exactly `a P(S = k)`:
`P(S' ≥ k + 1) = P(S ≥ k + 1) + a P(S = k)`. So the tail is affine in each trial's probability,
with nonnegative slope a point mass of the remaining trials.

Formalized by `ProbabilityTheory.poissonBinomialTail_cons_succ`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonBinomial.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonBinomial.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#poisson-binomial-tail-cons-succ).

## The burden-test p-value is monotone in every background rate

If `p i ≤ q i` for all
`i`, with all probabilities in `[0, 1]`, then `P_p(S ≥ k) ≤ P_q(S ≥ k)`.

Formalized by `ProbabilityTheory.poissonBinomialTail_mono`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonBinomial.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonBinomial.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#poisson-binomial-tail-mono).

## Poisson-binomial law with equal probabilities is binomial

With equal probabilities the Poisson-binomial law is the binomial law.

Formalized by `ProbabilityTheory.poissonBinomialPMF_const`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonBinomial.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonBinomial.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#poisson-binomial-pmf-const).

## Binomial tail monotonicity

For `0 ≤ p ≤ q ≤ 1`,
`∑_{k ≤ j ≤ n} C(n, j) p^j (1 - p)^{n - j} ≤ ∑_{k ≤ j ≤ n} C(n, j) q^j (1 - q)^{n - j}`.

Formalized by `ProbabilityTheory.binomialTail_mono`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonBinomial.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonBinomial.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#binomial-tail-mono).

## Binomial upper tail is monotone in the success probability

The upper tail `Bin(n, p)([k, ∞))` of Mathlib's binomial law is monotone in `p`.

Formalized by `ProbabilityTheory.binomial_real_Ici_mono`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonBinomial.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonBinomial.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#binomial-real-ici-mono).

## Tail of a sum of independent Bernoulli variables is Poisson-binomial

For independent Bernoulli variables `X i` with parameters `p i`, the one-sided burden
p-value `P(∑ X i ≥ k)` is the Poisson-binomial tail.

Formalized by `ProbabilityTheory.measure_le_sum_eq_poissonBinomialTail`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonBinomial.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonBinomial.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#measure-le-sum-eq-poisson-binomial-tail).

## Le Cam's inequality, finite truncations

For probabilities `p i ∈ [0, 1]` and
`λ = ∑ p i`, every partial sum of `∑_j |P(S = j) - e^{-λ} λ^j / j!|` is at most `2 ∑ (p i)²`.

Formalized by `ProbabilityTheory.sum_range_abs_poissonBinomialPMF_sub_poisson_le`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonBinomial.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonBinomial.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#sum-range-abs-poisson-binomial-pmf-sub-p).

## Le Cam's inequality

**Le Cam's inequality** (Le Cam 1960): the series `∑_j |P(S = j) - e^{-λ} λ^j / j!|` is
summable and its sum is at most `2 ∑ (p i)²`, where `λ = ∑ p i`.

Formalized by `ProbabilityTheory.tsum_abs_poissonBinomialPMF_sub_poisson_le`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonBinomial.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonBinomial.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html#tsum-abs-poisson-binomial-pmf-sub-poisso).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Poisson binomial distribution](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/poisson-binomial-distribution/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/distributions/discrete/poisson-binomial-distribution)
