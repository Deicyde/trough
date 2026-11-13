---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.FractionalExpectationThresholdsWanted.FractionalExpectationThresholds.IsWeaklySmall, MathlibExt.Combinatorics.FractionalExpectationThresholdsWanted.FractionalExpectationThresholds.p_c, MathlibExt.Combinatorics.FractionalExpectationThresholdsWanted.FractionalExpectationThresholds.q_f, MathlibExt.Combinatorics.FractionalExpectationThresholdsWanted.FractionalExpectationThresholds.l, MathlibExt.Combinatorics.FractionalExpectationThresholdsWanted.FractionalExpectationThresholds.K, MathlibExt.Combinatorics.FractionalExpectationThresholdsWanted.FractionalExpectationThresholds.theorem_1_1
statement: formalized
---

# Thresholds and expectation thresholds

6 results, 4 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/thresholds-and-expectation-thresholds/index.html).

## Weakly $p$-small families

Let $X$ be a finite set, $p \in [0, 1]$, and $\mathcal F$ a
family of subsets of $X$. Then $\mathcal F$ is weakly $p$-small if there is a function $g$ from
subsets of $X$ to the nonnegative reals such that $\sum_{S \subseteq T} g(S) \ge 1$ for every
$T \in \mathcal F$ and $\sum_{S \subseteq X} g(S)\, p^{|S|} \le 1/2$.

Formalized by `MathlibExt.Combinatorics.FractionalExpectationThresholdsWanted.FractionalExpectationThresholds.IsWeaklySmall`, a definition declared in [WantedExt/Combinatorics/FractionalExpectationThresholdsWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/FractionalExpectationThresholdsWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/thresholds-and-expectation-thresholds/index.html#is-weakly-small).

## The threshold $p_c(\mathcal F)$

For a set $X$ and $p \in [0, 1]$, let $\mu_p$ be the
$p$-biased product measure on subsets of $X$, under which each element of $X$ lies in the
random subset independently with probability $p$. For a family $\mathcal F$ of subsets of $X$,
$p_c(\mathcal F)$ is some $p \in [0, 1]$ with $\mu_p(\mathcal F) = 1/2$ if such a $p$ exists,
and $0$ otherwise.

When $X$ is finite and $\mathcal F$ is increasing, nonempty and not the family of all subsets
of $X$, such a $p$ exists and is unique; it is the threshold of $\mathcal F$.

Formalized by `MathlibExt.Combinatorics.FractionalExpectationThresholdsWanted.FractionalExpectationThresholds.p_c`, a definition declared in [WantedExt/Combinatorics/FractionalExpectationThresholdsWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/FractionalExpectationThresholdsWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/thresholds-and-expectation-thresholds/index.html#p-c).

## The fractional expectation-threshold $q_f(\mathcal F)$

For a family $\mathcal F$ of
subsets of a finite set $X$, $q_f(\mathcal F)$ is the supremum, in $[0, 1]$, of the set of all
$p \in [0, 1]$ such that $\mathcal F$ is weakly $p$-small; it is $0$ if there is no such $p$.

Formalized by `MathlibExt.Combinatorics.FractionalExpectationThresholdsWanted.FractionalExpectationThresholds.q_f`, a definition declared in [WantedExt/Combinatorics/FractionalExpectationThresholdsWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/FractionalExpectationThresholdsWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/thresholds-and-expectation-thresholds/index.html#q-f).

## Size of a largest minimal element, $\ell(\mathcal F)$

For a family $\mathcal F$ of
subsets of a set $X$, $\ell(\mathcal F)$ is the largest cardinality of a minimal element of
$\mathcal F$ (minimal with respect to inclusion), a natural number.

By convention $\ell(\mathcal F) = 0$ when $\mathcal F$ has no minimal element or when the
cardinalities of its minimal elements are unbounded, and an infinite set counts as having
cardinality $0$.

Formalized by `MathlibExt.Combinatorics.FractionalExpectationThresholdsWanted.FractionalExpectationThresholds.l`, a definition declared in [WantedExt/Combinatorics/FractionalExpectationThresholdsWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/FractionalExpectationThresholdsWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/thresholds-and-expectation-thresholds/index.html#l).

## The constant of the Frankston–Kahn–Narayanan–Park theorem

A real number $K$, not yet
specified, that is to serve as the universal constant in the bound of the threshold of an
increasing family by $K$ times its fractional expectation-threshold times the logarithm of the
size of its largest minimal element.

## Sources

- K. Frankston, J. Kahn, B. Narayanan, and J. Park, `Thresholds versus fractional expectation-thresholds`, Annals of Math, 194 (2) 2021. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_fractional_expectation_thresholds` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.FractionalExpectationThresholdsWanted.FractionalExpectationThresholds.K` is written with `def_wanted` in [WantedExt/Combinatorics/FractionalExpectationThresholdsWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/FractionalExpectationThresholdsWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/thresholds-and-expectation-thresholds/index.html#k).

## Thresholds versus fractional expectation-thresholds

Let $K$ be the universal real
constant still to be supplied. For every finite set $X$ and every increasing family $\mathcal F$
of subsets of $X$ (closed under taking supersets) with $\ell(\mathcal F) \ge 2$, where
$\ell(\mathcal F)$ is the size of a largest minimal element of $\mathcal F$,

$$p_c(\mathcal F) \le K \, q_f(\mathcal F) \log \ell(\mathcal F),$$

where $p_c$ is the threshold, $q_f$ the fractional expectation-threshold and $\log$ the
natural logarithm.

The hypothesis $\ell(\mathcal F) \ge 2$ is not explicit in the paper but is needed: if
$\ell(\mathcal F) = 1$ then $\log \ell(\mathcal F) = 0$, while $p_c(\mathcal F) \in (0, 1)$,
so the inequality cannot hold.

## Sources

- K. Frankston, J. Kahn, B. Narayanan, and J. Park, `Thresholds versus fractional expectation-thresholds`, Annals of Math, 194 (2) 2021. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_fractional_expectation_thresholds` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.FractionalExpectationThresholdsWanted.FractionalExpectationThresholds.theorem_1_1` is written with `theorem_wanted` in [WantedExt/Combinatorics/FractionalExpectationThresholdsWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/FractionalExpectationThresholdsWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/thresholds-and-expectation-thresholds/index.html#theorem-1-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Thresholds and expectation thresholds](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/thresholds-and-expectation-thresholds/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/probabilistic-combinatorics/thresholds-and-expectation-thresholds)
