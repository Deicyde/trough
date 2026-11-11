---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.ScottishBook163Wanted.IsVonNeumannMeasure, MathlibExt.MeasureTheory.ScottishBook163Wanted.SatisfiesCountableChainCondition, MathlibExt.MeasureTheory.ScottishBook163Wanted.SatisfiesGeneralizedDistributivity, MathlibExt.MeasureTheory.ScottishBook163Wanted.VonNeumannSufficiencyClaim, MathlibExt.MeasureTheory.ScottishBook163Wanted.vonNeumannConditionsNotSufficient
statement: formalized
---

# Measures on complete Boolean algebras

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/measures-on-complete-boolean-algebras/index.html).

## Von Neumann measures on a complete Boolean algebra

A real-valued function $\mu$ on a
complete Boolean algebra $B$ is a measure in von Neumann's sense when $\mu(\bot) = 0$,
$\mu(a) > 0$ for every $a \ne \bot$, and $\mu$ is countably additive: for every sequence
$(a_i)_{i \in \mathbb{N}}$ of pairwise disjoint elements of $B$ (that is, $a_i \wedge a_j = \bot$
whenever $i \ne j$), the series $\sum_i \mu(a_i)$ converges and
$\mu(\bigvee_i a_i) = \sum_i \mu(a_i)$.

Von Neumann's conditions (1)-(4) are the axioms of a complete Boolean algebra.

Formalized by `MathlibExt.MeasureTheory.ScottishBook163Wanted.IsVonNeumannMeasure`, a definition declared in [WantedExt/MeasureTheory/ScottishBook163Wanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/ScottishBook163Wanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/measures-on-complete-boolean-algebras/index.html#is-von-neumann-measure).

## The countable chain condition for complete Boolean algebras

A complete Boolean algebra
$B$ satisfies the countable chain condition (von Neumann's condition (5)) when every subset
$S \subseteq B$ whose distinct elements are pairwise disjoint (that is, $a \wedge b = \bot$ for
all distinct $a, b \in S$) is at most countable.

Formalized by `MathlibExt.MeasureTheory.ScottishBook163Wanted.SatisfiesCountableChainCondition`, a definition declared in [WantedExt/MeasureTheory/ScottishBook163Wanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/ScottishBook163Wanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/measures-on-complete-boolean-algebras/index.html#satisfies-countable-chain-condition).

## Von Neumann's generalized distributivity law

A complete Boolean algebra $B$ satisfies
the generalized distributivity law (von Neumann's condition (6)) when, for every double sequence
$(a_{i,j})_{i, j \in \mathbb{N}}$ of elements of $B$ that is increasing in $j$ for each fixed $i$
(that is, $a_{i,0} \le a_{i,1} \le \cdots$ for every $i$),

$$\bigwedge_{i} \bigvee_{j} a_{i,j} = \bigvee_{f} \bigwedge_{i} a_{i,f(i)},$$

where $f$ ranges over all functions $\mathbb{N} \to \mathbb{N}$.

Formalized by `MathlibExt.MeasureTheory.ScottishBook163Wanted.SatisfiesGeneralizedDistributivity`, a definition declared in [WantedExt/MeasureTheory/ScottishBook163Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/ScottishBook163Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/measures-on-complete-boolean-algebras/index.html#satisfies-generalized-distributivity).

## Von Neumann's sufficiency claim

The statement that every complete Boolean algebra
satisfying the countable chain condition and the generalized distributivity law carries a
measure in von Neumann's sense.

Formalized by `MathlibExt.MeasureTheory.ScottishBook163Wanted.VonNeumannSufficiencyClaim`, a definition declared in [WantedExt/MeasureTheory/ScottishBook163Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/ScottishBook163Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/measures-on-complete-boolean-algebras/index.html#von-neumann-sufficiency-claim).

## Von Neumann's conditions do not guarantee a measure

There is a complete Boolean algebra that
satisfies the countable chain condition and the generalized distributivity law but carries no
measure in von Neumann's sense; that is, von Neumann's sufficiency claim is false. This answers
Problem 163 of the Scottish Book in the negative, in its stated form.

The typescript's complement clause prints its two constants swapped relative to its own usage
elsewhere; it is read here as the standard complement laws, with bottom $\bot$ and top $\top$.

## Sources

- J. von Neumann, Problem 163 of the Scottish Book; refuted by M. Talagrand, "Maharam's problem", arXiv:math/0601689 (2006), who constructed an exhaustive submeasure not equivalent to a measure, solving the problems of J. von Neumann (1937) and D. Maharam (1947).

Stated but not proved: `MathlibExt.MeasureTheory.ScottishBook163Wanted.vonNeumannConditionsNotSufficient` is written with `theorem_wanted` in [WantedExt/MeasureTheory/ScottishBook163Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/ScottishBook163Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/measures-on-complete-boolean-algebras/index.html#von-neumann-conditions-not-sufficient).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Measures on complete Boolean algebras](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/measures-on-complete-boolean-algebras/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/measures/measures-on-complete-boolean-algebras)
