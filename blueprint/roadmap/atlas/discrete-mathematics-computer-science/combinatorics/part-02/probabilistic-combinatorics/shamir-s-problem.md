---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ShamirPerfectMatchingThresholdErdosProblem747Wanted.matchingProbability, MathlibExt.Combinatorics.ShamirPerfectMatchingThresholdErdosProblem747Wanted.matchingAboveThreshold, MathlibExt.Combinatorics.ShamirPerfectMatchingThresholdErdosProblem747Wanted.matchingThreshold, MathlibExt.Combinatorics.ShamirPerfectMatchingThresholdErdosProblem747Wanted.matchingThresholdAsymptotic, MathlibExt.Combinatorics.ShamirPerfectMatchingThresholdErdosProblem747Wanted.matchingAboveThreshold_holds, MathlibExt.Combinatorics.ShamirPerfectMatchingThresholdErdosProblem747Wanted.matchingThresholdAsymptotic_holds
statement: formalized
---

# Shamir's problem

6 results, 4 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/shamir-s-problem/index.html).

## Probability of a perfect matching in a random $3$-uniform hypergraph

For natural numbers
$n$ and $\ell$, let $T$ be the set of $3$-element subsets of $\{0, 1, \dots, 3n - 1\}$. This is the
proportion of the $\ell$-element subsets $E \subseteq T$ that contain $n$ pairwise disjoint
triples, that is, the probability that the uniformly random $3$-uniform hypergraph on $3n$
vertices with $\ell$ edges has a perfect matching. When $\ell > \binom{3n}{3}$ there is no such
hypergraph and the value is $0$.

Formalized by `MathlibExt.Combinatorics.ShamirPerfectMatchingThresholdErdosProblem747Wanted.matchingProbability`, a definition declared in [WantedExt/Combinatorics/ShamirPerfectMatchingThresholdErdosProblem747Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ShamirPerfectMatchingThresholdErdosProblem747Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/shamir-s-problem/index.html#matching-probability).

## Statement of the upper half of Shamir's problem

The proposition that for every real
$\varepsilon > 0$, the probability that the uniformly random $3$-uniform hypergraph on $3n$
vertices with $\lceil (1 + \varepsilon) n \log n \rceil$ edges has a perfect matching ($n$
pairwise disjoint edges) tends to $1$ as $n \to \infty$, where $\log$ is the natural logarithm.

Erdős Problem 747 (Shamir's problem) asks for the number $\ell(n)$ of edges at which a perfect
matching becomes almost sure; this is the upper half of the answer $\ell(n) \sim n \log n$.

Formalized by `MathlibExt.Combinatorics.ShamirPerfectMatchingThresholdErdosProblem747Wanted.matchingAboveThreshold`, a definition declared in [WantedExt/Combinatorics/ShamirPerfectMatchingThresholdErdosProblem747Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ShamirPerfectMatchingThresholdErdosProblem747Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/shamir-s-problem/index.html#matching-above-threshold).

## Threshold for a perfect matching in a random $3$-uniform hypergraph

For a natural number
$n$, the threshold $\ell_c(n)$ is the least natural number $\ell$ such that the uniformly random
$3$-uniform hypergraph on $3n$ vertices with $\ell$ edges has a perfect matching ($n$ pairwise
disjoint edges) with probability at least $1/2$.

The set of such $\ell$ is nonempty: with all triples present the probability is $1$.

Formalized by `MathlibExt.Combinatorics.ShamirPerfectMatchingThresholdErdosProblem747Wanted.matchingThreshold`, a definition declared in [WantedExt/Combinatorics/ShamirPerfectMatchingThresholdErdosProblem747Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ShamirPerfectMatchingThresholdErdosProblem747Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/shamir-s-problem/index.html#matching-threshold).

## Statement of Shamir's problem: the matching threshold is asymptotic to $n \log n$

Let
$\ell_c(n)$ be the least number $\ell$ such that the uniformly random $3$-uniform hypergraph on
$3n$ vertices with $\ell$ edges has a perfect matching with probability at least $1/2$. The
proposition that $\ell_c(n) / (n \log n) \to 1$ as $n \to \infty$, where $\log$ is the natural
logarithm.

This is the answer to Erdős Problem 747 (Shamir's problem).

Formalized by `MathlibExt.Combinatorics.ShamirPerfectMatchingThresholdErdosProblem747Wanted.matchingThresholdAsymptotic`, a definition declared in [WantedExt/Combinatorics/ShamirPerfectMatchingThresholdErdosProblem747Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ShamirPerfectMatchingThresholdErdosProblem747Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/shamir-s-problem/index.html#matching-threshold-asymptotic).

## Kahn's theorem on Shamir's problem, upper half

For every real $\varepsilon > 0$, the
probability that the uniformly random $3$-uniform hypergraph on $3n$ vertices with
$\lceil (1 + \varepsilon) n \log n \rceil$ edges has a perfect matching ($n$ pairwise disjoint
edges) tends to $1$ as $n \to \infty$, where $\log$ is the natural logarithm.

## Sources

- T. F. Bloom, Erdős Problems, Problem #747, https://www.erdosproblems.com/747 (status SOLVED); resolution: J. Kahn, Asymptotics for Shamir's problem, Adv. Math. 422 (2023), Paper 109019, Theorem 1 of arXiv:1909.06834 (abstract; Theorem 1.2 in the text): for fixed r ≥ 3, ε > 0 and M > (1 + ε)(n/r) log n, the random M-edge r-graph on [n] has a perfect matching with probability → 1; Section 1: the threshold M_c, the least M for which the probability of a perfect matching is at least 1/2, satisfies M_c ∼ (n/r) log n ('In this paper we show that the asymptotics of the threshold are as expected'); erdosproblems.com/747: the threshold is ∼ n log n, https://arxiv.org/abs/1909.06834.

Stated but not proved: `MathlibExt.Combinatorics.ShamirPerfectMatchingThresholdErdosProblem747Wanted.matchingAboveThreshold_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ShamirPerfectMatchingThresholdErdosProblem747Wanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ShamirPerfectMatchingThresholdErdosProblem747Wanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/shamir-s-problem/index.html#matching-above-threshold-holds).

## Kahn's theorem: the threshold in Shamir's problem is asymptotic to $n \log n$

Let $\ell_c(n)$
be the least number $\ell$ such that the uniformly random $3$-uniform hypergraph on $3n$ vertices
with $\ell$ edges has a perfect matching with probability at least $1/2$. Then
$\ell_c(n) / (n \log n) \to 1$ as $n \to \infty$, where $\log$ is the natural logarithm.

## Sources

- T. F. Bloom, Erdős Problems, Problem #747, https://www.erdosproblems.com/747 (status SOLVED); resolution: J. Kahn, Asymptotics for Shamir's problem, Adv. Math. 422 (2023), Paper 109019, Theorem 1 of arXiv:1909.06834 (abstract; Theorem 1.2 in the text): for fixed r ≥ 3, ε > 0 and M > (1 + ε)(n/r) log n, the random M-edge r-graph on [n] has a perfect matching with probability → 1; Section 1: the threshold M_c, the least M for which the probability of a perfect matching is at least 1/2, satisfies M_c ∼ (n/r) log n ('In this paper we show that the asymptotics of the threshold are as expected'); erdosproblems.com/747: the threshold is ∼ n log n, https://arxiv.org/abs/1909.06834.

Stated but not proved: `MathlibExt.Combinatorics.ShamirPerfectMatchingThresholdErdosProblem747Wanted.matchingThresholdAsymptotic_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ShamirPerfectMatchingThresholdErdosProblem747Wanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ShamirPerfectMatchingThresholdErdosProblem747Wanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/shamir-s-problem/index.html#matching-threshold-asymptotic-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Shamir's problem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/shamir-s-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/probabilistic-combinatorics/shamir-s-problem)
