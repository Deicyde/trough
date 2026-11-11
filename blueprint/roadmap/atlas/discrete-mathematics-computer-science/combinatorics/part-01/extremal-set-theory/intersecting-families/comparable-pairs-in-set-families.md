---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ComparablePairsSetFamilyErdosProblem777Wanted.comparablePairs, MathlibExt.Combinatorics.ComparablePairsSetFamilyErdosProblem777Wanted.fewComparablePairsBelowTwoHalfPower, MathlibExt.Combinatorics.ComparablePairsSetFamilyErdosProblem777Wanted.denseComparabilityFamilySmall, MathlibExt.Combinatorics.ComparablePairsSetFamilyErdosProblem777Wanted.nearlyCompleteComparabilityFamilySmall, MathlibExt.Combinatorics.ComparablePairsSetFamilyErdosProblem777Wanted.fewComparablePairsBelowTwoHalfPower_holds, MathlibExt.Combinatorics.ComparablePairsSetFamilyErdosProblem777Wanted.denseComparabilityFamilySmall_refuted, MathlibExt.Combinatorics.ComparablePairsSetFamilyErdosProblem777Wanted.nearlyCompleteComparabilityFamilySmall_holds
statement: formalized
---

# Comparable pairs in set families

7 results, 4 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/comparable-pairs-in-set-families/index.html).

## Number of comparable pairs

For $n \in \mathbb{N}$ and a family $F$ of subsets of
$\{0, \dots, n - 1\}$, the number of comparable pairs of $F$ is the number of ordered pairs
$(A, B)$ of members of $F$ with $A \subsetneq B$. It is the number of edges of the comparability
graph $G_F$ on $F$, in which two distinct members are adjacent when one contains the other.

Formalized by `MathlibExt.Combinatorics.ComparablePairsSetFamilyErdosProblem777Wanted.comparablePairs`, a definition declared in [WantedExt/Combinatorics/ComparablePairsSetFamilyErdosProblem777Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ComparablePairsSetFamilyErdosProblem777Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/comparable-pairs-in-set-families/index.html#comparable-pairs).

## Erdős Problem 777, first question

For every real $\varepsilon > 0$ there is $N$ such that
for every $n \ge N$, every family $F$ of subsets of $\{0, \dots, n - 1\}$ with
$|F| \le (2 - \varepsilon) 2^{n/2}$ has fewer than $2^n$ comparable pairs, that is, ordered pairs
$(A, B)$ of members of $F$ with $A \subsetneq B$.

Formalized by `MathlibExt.Combinatorics.ComparablePairsSetFamilyErdosProblem777Wanted.fewComparablePairsBelowTwoHalfPower`, a definition declared in [WantedExt/Combinatorics/ComparablePairsSetFamilyErdosProblem777Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ComparablePairsSetFamilyErdosProblem777Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/comparable-pairs-in-set-families/index.html#few-comparable-pairs-below-two-half-powe).

## Erdős Problem 777, second question

For every real $c > 0$ there is a real constant $C$
such that for every $n$ and every family $F$ of subsets of $\{0, \dots, n - 1\}$ with at least
$c |F|^2$ comparable pairs (ordered pairs $(A, B)$ of members of $F$ with $A \subsetneq B$), we
have $|F| \le C \cdot 2^{n/2}$.

Formalized by `MathlibExt.Combinatorics.ComparablePairsSetFamilyErdosProblem777Wanted.denseComparabilityFamilySmall`, a definition declared in [WantedExt/Combinatorics/ComparablePairsSetFamilyErdosProblem777Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ComparablePairsSetFamilyErdosProblem777Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/comparable-pairs-in-set-families/index.html#dense-comparability-family-small).

## Erdős Problem 777, third question

For every real $\varepsilon > 0$ there is a real
$\delta > 0$ such that for every $n$, every family $F$ of subsets of $\{0, \dots, n - 1\}$ with
more than $|F|^{2 - \delta}$ comparable pairs (ordered pairs $(A, B)$ of members of $F$ with
$A \subsetneq B$) satisfies $|F| < (2 + \varepsilon)^{n/2}$.

Formalized by `MathlibExt.Combinatorics.ComparablePairsSetFamilyErdosProblem777Wanted.nearlyCompleteComparabilityFamilySmall`, a definition declared in [WantedExt/Combinatorics/ComparablePairsSetFamilyErdosProblem777Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ComparablePairsSetFamilyErdosProblem777Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/comparable-pairs-in-set-families/index.html#nearly-complete-comparability-family-sma).

## Affirmative answer to Erdős Problem 777, first question

For every real $\varepsilon > 0$
there is $N$ such that for every $n \ge N$, every family $F$ of subsets of $\{0, \dots, n - 1\}$
with $|F| \le (2 - \varepsilon) 2^{n/2}$ has fewer than $2^n$ comparable pairs, that is, ordered
pairs $(A, B)$ of members of $F$ with $A \subsetneq B$.

The bound is sharp: for even $n$, a family of $m = 2^{n/2 + 1}$ subsets formed by two stacked
subcubes has at least $2^n$ comparable pairs. According to erdosproblems.com/777 the affirmative
answer follows from Theorem 1.4 and Corollary 1.5 of Alon, Das, Glebov and Sudakov.

## Sources

- T. F. Bloom, Erdős Problems, Problem #777, https://www.erdosproblems.com/777 (status SOLVED); resolution: N. Alon and P. Frankl, The maximum number of disjoint pairs in a family of subsets, Graphs Combin. 1 (1985), 13-21; N. Alon, S. Das, R. Glebov and B. Sudakov, Comparable pairs in families of sets, J. Combin. Theory Ser. B (2015), 164-185, arXiv:1411.4196, Alon-Frankl Theorem 1.4: for every k ≥ 1 there is β(k) > 0 such that for m = 2^{(1/(k+1) + δ)n}, c(n, m) < (1 - 1/k) C(m, 2) + O(m^{2 - β δ^{k+1}}), the case k = 1 conjectured by Daykin and Erdős; Alon-Frankl Section 6, Example 6.1: the sets meeting the second half of [n] in at most d elements or missing at most d elements of the first half form a family of Θ(n^d 2^{n/2}) sets with a constant fraction of comparable pairs, disproving a conjecture of Erdős; erdosproblems.com/777: Alon and Frankl answer the third question in the affirmative and the second in the negative, and an affirmative answer to the first follows from Theorem 1.4 and Corollary 1.5 of Alon, Das, Glebov and Sudakov, https://www.erdosproblems.com/777.

Stated but not proved: `MathlibExt.Combinatorics.ComparablePairsSetFamilyErdosProblem777Wanted.fewComparablePairsBelowTwoHalfPower_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ComparablePairsSetFamilyErdosProblem777Wanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ComparablePairsSetFamilyErdosProblem777Wanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/comparable-pairs-in-set-families/index.html#few-comparable-pairs-below-two-half-powe-2).

## Negative answer to Erdős Problem 777, second question

It is not the case that for every
real $c > 0$ there is a real constant $C$ such that for every $n$ and every family $F$ of subsets
of $\{0, \dots, n - 1\}$ with at least $c |F|^2$ comparable pairs (ordered pairs $(A, B)$ of
members of $F$ with $A \subsetneq B$), we have $|F| \le C \cdot 2^{n/2}$. Equivalently, there is
a real $c > 0$ such that for every real $C$ some $n$ and some family $F$ of subsets of
$\{0, \dots, n - 1\}$ with at least $c |F|^2$ comparable pairs have $|F| > C \cdot 2^{n/2}$.

Alon and Frankl's Example 6.1 with $d = 1$ gives such families: $m \gg n 2^{n/2}$ subsets of an
$n$-element set with at least $2^{-5} \binom{m}{2}$ comparable pairs (erdosproblems.com/777).

## Sources

- T. F. Bloom, Erdős Problems, Problem #777, https://www.erdosproblems.com/777 (status SOLVED); resolution: N. Alon and P. Frankl, The maximum number of disjoint pairs in a family of subsets, Graphs Combin. 1 (1985), 13-21; N. Alon, S. Das, R. Glebov and B. Sudakov, Comparable pairs in families of sets, J. Combin. Theory Ser. B (2015), 164-185, arXiv:1411.4196, Alon-Frankl Theorem 1.4: for every k ≥ 1 there is β(k) > 0 such that for m = 2^{(1/(k+1) + δ)n}, c(n, m) < (1 - 1/k) C(m, 2) + O(m^{2 - β δ^{k+1}}), the case k = 1 conjectured by Daykin and Erdős; Alon-Frankl Section 6, Example 6.1: the sets meeting the second half of [n] in at most d elements or missing at most d elements of the first half form a family of Θ(n^d 2^{n/2}) sets with a constant fraction of comparable pairs, disproving a conjecture of Erdős; erdosproblems.com/777: Alon and Frankl answer the third question in the affirmative and the second in the negative, and an affirmative answer to the first follows from Theorem 1.4 and Corollary 1.5 of Alon, Das, Glebov and Sudakov, https://www.erdosproblems.com/777.

Stated but not proved: `MathlibExt.Combinatorics.ComparablePairsSetFamilyErdosProblem777Wanted.denseComparabilityFamilySmall_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/ComparablePairsSetFamilyErdosProblem777Wanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ComparablePairsSetFamilyErdosProblem777Wanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/comparable-pairs-in-set-families/index.html#dense-comparability-family-small-refuted).

## Affirmative answer to Erdős Problem 777, third question

For every real $\varepsilon > 0$
there is a real $\delta > 0$ such that for every $n$, every family $F$ of subsets of
$\{0, \dots, n - 1\}$ with more than $|F|^{2 - \delta}$ comparable pairs (ordered pairs $(A, B)$
of members of $F$ with $A \subsetneq B$) satisfies $|F| < (2 + \varepsilon)^{n/2}$.

According to erdosproblems.com/777 this follows from the case $k = 1$ of Theorem 1.4 of Alon and
Frankl, conjectured by Daykin and Erdős: there is $\beta > 0$ such that for every $\eta > 0$, a
family of $m = 2^{(1/2 + \eta) n}$ subsets of an $n$-element set has $O(m^{2 - \beta \eta^2})$
comparable pairs.

## Sources

- T. F. Bloom, Erdős Problems, Problem #777, https://www.erdosproblems.com/777 (status SOLVED); resolution: N. Alon and P. Frankl, The maximum number of disjoint pairs in a family of subsets, Graphs Combin. 1 (1985), 13-21; N. Alon, S. Das, R. Glebov and B. Sudakov, Comparable pairs in families of sets, J. Combin. Theory Ser. B (2015), 164-185, arXiv:1411.4196, Alon-Frankl Theorem 1.4: for every k ≥ 1 there is β(k) > 0 such that for m = 2^{(1/(k+1) + δ)n}, c(n, m) < (1 - 1/k) C(m, 2) + O(m^{2 - β δ^{k+1}}), the case k = 1 conjectured by Daykin and Erdős; Alon-Frankl Section 6, Example 6.1: the sets meeting the second half of [n] in at most d elements or missing at most d elements of the first half form a family of Θ(n^d 2^{n/2}) sets with a constant fraction of comparable pairs, disproving a conjecture of Erdős; erdosproblems.com/777: Alon and Frankl answer the third question in the affirmative and the second in the negative, and an affirmative answer to the first follows from Theorem 1.4 and Corollary 1.5 of Alon, Das, Glebov and Sudakov, https://www.erdosproblems.com/777.

Stated but not proved: `MathlibExt.Combinatorics.ComparablePairsSetFamilyErdosProblem777Wanted.nearlyCompleteComparabilityFamilySmall_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ComparablePairsSetFamilyErdosProblem777Wanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ComparablePairsSetFamilyErdosProblem777Wanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/comparable-pairs-in-set-families/index.html#nearly-complete-comparability-family-sma-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Comparable pairs in set families](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/comparable-pairs-in-set-families/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/extremal-set-theory/intersecting-families/comparable-pairs-in-set-families)
