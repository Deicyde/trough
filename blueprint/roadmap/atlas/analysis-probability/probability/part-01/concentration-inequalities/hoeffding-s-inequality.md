---
declaration: section
origin: cited
lean: ProbabilityTheory.hoeffding_bernoulli_sum_abs_tail, ProbabilityTheory.hoeffding_binomial_lower_tail, Finset.card_sample_tail_le
statement: formalized
proof: formalized
---

# Hoeffding's inequality

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/hoeffding-s-inequality/index.html).

## Two-sided Hoeffding inequality for Bernoulli sums

Let $X_0, \dots, X_{n-1}$ be
independent real random variables on a probability space, each almost everywhere measurable,
almost surely equal to $0$ or $1$, and with expectation $p$, and let $\varepsilon > 0$. Then the
probability that $\lvert X_0 + \dots + X_{n-1} - np \rvert > \varepsilon n$ is at most
$2 e^{-2 \varepsilon^2 n}$.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL28/Jackson/jackson5.tex> (Proposition, Hoeffding's Inequality, Thm. 2 of Hoe63).

Formalized by `ProbabilityTheory.hoeffding_bernoulli_sum_abs_tail`, a theorem declared in [MathlibExt/Probability/HoeffdingBernoulliSumAbsTail.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/HoeffdingBernoulliSumAbsTail.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/hoeffding-s-inequality/index.html#hoeffding-bernoulli-sum-abs-tail).

## Hoeffding lower-tail bound for Bernoulli sums

Let $X_0, \dots, X_{n-1}$ be independent
real random variables on a probability space, each almost everywhere measurable, almost surely
equal to $0$ or $1$, and with expectation $p$, and let $\varepsilon > 0$. Then the probability
that $X_0 + \dots + X_{n-1} \le n(p - \varepsilon)$ is at most $e^{-2 \varepsilon^2 n}$.

## Sources

- Griffiths JIS VOL16, source lines 167-191, <https://cs.uwaterloo.ca/journals/JIS/VOL16/Griffiths/griffiths22.tex>.

Formalized by `ProbabilityTheory.hoeffding_binomial_lower_tail`, a theorem declared in [MathlibExt/Probability/HoeffdingBinomialLowerTail.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/HoeffdingBinomialLowerTail.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/hoeffding-s-inequality/index.html#hoeffding-binomial-lower-tail).

## Hoeffding's bound for sampling without replacement

Hoeffding's upper-tail bound for sampling without replacement, stated as a count.

Among the `n`-element subsets `S` of `s`, at most
`exp (-2 * n * t ^ 2) * choose (#s) n` satisfy
`n * mean(c) + t * n * R ≤ ∑ i ∈ S, c i`. The event is non-strict; `n = 0` and
`#s < n` are included without separate assumptions.

Formalized by `Finset.card_sample_tail_le`, a theorem declared in [MathlibExt/Probability/Sampling/WithoutReplacement.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Sampling/WithoutReplacement.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/hoeffding-s-inequality/index.html#card-sample-tail-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hoeffding's inequality](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/hoeffding-s-inequality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/concentration-inequalities/hoeffding-s-inequality)
