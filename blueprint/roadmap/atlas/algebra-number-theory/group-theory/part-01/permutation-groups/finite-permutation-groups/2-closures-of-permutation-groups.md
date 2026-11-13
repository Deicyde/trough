---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.TotallyTwoClosedInsolubleKourovka20Problem1Wanted.IsTwoClosedAction, MathlibExt.GroupTheory.TotallyTwoClosedInsolubleKourovka20Problem1Wanted.IsTotallyTwoClosed, MathlibExt.GroupTheory.TotallyTwoClosedInsolubleKourovka20Problem1Wanted.insolubleTotallyTwoClosedWithNontrivialFitting, MathlibExt.GroupTheory.TotallyTwoClosedInsolubleKourovka20Problem1Wanted.insolubleTotallyTwoClosedWithNontrivialFitting_holds, MathlibExt.GroupTheory.TwoClosureSolvableCompositionFactorsKourovka19Problem67Wanted.twoClosure, MathlibExt.GroupTheory.TwoClosureSolvableCompositionFactorsKourovka19Problem67Wanted.solvableTwoClosureFactorsCyclicOrAlternating, MathlibExt.GroupTheory.TwoClosureSolvableCompositionFactorsKourovka19Problem67Wanted.solvableTwoClosureFactorsCyclicOrAlternating_refuted
statement: formalized
---

# 2-closures of permutation groups

7 results, 5 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/2-closures-of-permutation-groups/index.html).

## 2-closed actions

An action of a group $G$ on a set $\Omega$ is $2$-closed when every
permutation $\sigma$ of $\Omega$ that preserves each $G$-orbit on ordered pairs (that is, for all
$\alpha, \beta \in \Omega$ some $g \in G$ satisfies $\sigma(\alpha) = g \alpha$ and
$\sigma(\beta) = g \beta$) is induced by an element of $G$: there is $g \in G$ with
$\sigma(\omega) = g \omega$ for all $\omega \in \Omega$.

Formalized by `MathlibExt.GroupTheory.TotallyTwoClosedInsolubleKourovka20Problem1Wanted.IsTwoClosedAction`, a definition declared in [WantedExt/GroupTheory/TotallyTwoClosedInsolubleKourovka20Problem1Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/TotallyTwoClosedInsolubleKourovka20Problem1Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/2-closures-of-permutation-groups/index.html#is-two-closed-action).

## Totally 2-closed groups

A group $G$ is totally $2$-closed when every faithful action of
$G$ on a set $\Omega$ is $2$-closed; equivalently, in each faithful permutation representation of
$G$ on a set $\Omega$, $G$ is the largest subgroup of $\mathrm{Sym}(\Omega)$ preserving each of
its orbits on $\Omega^2$.

Formalized by `MathlibExt.GroupTheory.TotallyTwoClosedInsolubleKourovka20Problem1Wanted.IsTotallyTwoClosed`, a definition declared in [WantedExt/GroupTheory/TotallyTwoClosedInsolubleKourovka20Problem1Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/TotallyTwoClosedInsolubleKourovka20Problem1Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/2-closures-of-permutation-groups/index.html#is-totally-two-closed).

## Kourovka Problem 20.1 (insoluble totally 2-closed groups)

The statement, asked by
M. Arezoomand, M. A. Iranmanesh, C. E. Praeger and G. Tracey, that there exists a finite group $G$
that is not soluble, is totally $2$-closed, and has a nontrivial nilpotent normal subgroup
(equivalently, a nontrivial Fitting subgroup).

Formalized by `MathlibExt.GroupTheory.TotallyTwoClosedInsolubleKourovka20Problem1Wanted.insolubleTotallyTwoClosedWithNontrivialFitting`, a definition declared in [WantedExt/GroupTheory/TotallyTwoClosedInsolubleKourovka20Problem1Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/TotallyTwoClosedInsolubleKourovka20Problem1Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/2-closures-of-permutation-groups/index.html#insoluble-totally-two-closed-with-nontri).

## A finite insoluble totally 2-closed group with nontrivial Fitting subgroup

There exists a
finite group $G$ that is not soluble, is totally $2$-closed, and has a nontrivial nilpotent normal
subgroup (equivalently, a nontrivial Fitting subgroup).

The Kourovka Notebook (21st issue) answers Problem 20.1 "Yes, there are". Kinyon and Urban (an
AI-generated solution confirmed by G. Tracey) prove that $J_1 \times C_{13}$ is totally $2$-closed
(Section 3.34, Lemma 3.11), insoluble and has Fitting subgroup $C_{13}$; the Notebook also obtains
$J_1 \times C_p$ for primes $p \in \lbrace 13, 17 \rbrace$ or $p > 19$ from Theorem 1.1 of
Arezoomand-Iranmanesh-Praeger-Tracey and Theorem 2 and Proposition 2 of Abdollahi-Arezoomand.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 20.1 (M. Arezoomand, M. A. Iranmanesh, C. E. Praeger, G. Tracey); resolution: M. Kinyon and J. Urban, Results on problems from the Kourovka Notebook, preprint, version 4, 19 September 2026; M. Arezoomand, M. A. Iranmanesh, C. E. Praeger and G. Tracey, Bull. Math. Sci. 14 (2024), no. 1, 2350004; A. Abdollahi and M. Arezoomand, J. Algebra Appl. 17 (2018), no. 4, 1850065, Kinyon-Urban, Section 3.34 (Problem 20.1): J1 × C13 is totally 2-closed, insoluble, with Fitting subgroup C13 (Lemma 3.11: direct products of totally 2-closed groups of coprime orders are totally 2-closed), an AI solution confirmed by G. Tracey; the Kourovka Notebook (21st issue) also derives J1 × C_p (p ∈ {13, 17} or p > 19) from Theorem 1.1 of Arezoomand-Iranmanesh-Praeger-Tracey and Theorem 2 and Proposition 2 of Abdollahi-Arezoomand, https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/kourovka-mathematics.pdf.

Stated but not proved: `MathlibExt.GroupTheory.TotallyTwoClosedInsolubleKourovka20Problem1Wanted.insolubleTotallyTwoClosedWithNontrivialFitting_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/TotallyTwoClosedInsolubleKourovka20Problem1Wanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/TotallyTwoClosedInsolubleKourovka20Problem1Wanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/2-closures-of-permutation-groups/index.html#insoluble-totally-two-closed-with-nontri-2).

## The $2$-closure of a permutation group

For a subgroup $G$ of the symmetric group
$\mathrm{Sym}(\Omega)$, the $2$-closure $G^{(2)}$ of $G$ is the subgroup of $\mathrm{Sym}(\Omega)$
generated by the permutations $\sigma$ that map every pair of points into its $G$-orbit, that is,
such that for all $\alpha, \beta \in \Omega$ there is $g \in G$ with $g(\alpha) = \sigma(\alpha)$
and $g(\beta) = \sigma(\beta)$.

These permutations already form a subgroup: the largest subgroup of $\mathrm{Sym}(\Omega)$
containing $G$ with the same orbits as $G$ on $\Omega \times \Omega$.

Formalized by `MathlibExt.GroupTheory.TwoClosureSolvableCompositionFactorsKourovka19Problem67Wanted.twoClosure`, a definition declared in [WantedExt/GroupTheory/TwoClosureSolvableCompositionFactorsKourovka19Problem67Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/TwoClosureSolvableCompositionFactorsKourovka19Problem67Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/2-closures-of-permutation-groups/index.html#two-closure).

## Kourovka Problem 19.67

The statement that for every finite set $\Omega$ and every
solvable subgroup $G$ of the symmetric group $\mathrm{Sym}(\Omega)$, every composition factor of
the $2$-closure $G^{(2)}$ of $G$ is cyclic or isomorphic to the alternating group $A_n$ for some
natural number $n$.

Formalized by `MathlibExt.GroupTheory.TwoClosureSolvableCompositionFactorsKourovka19Problem67Wanted.solvableTwoClosureFactorsCyclicOrAlternating`, a definition declared in [WantedExt/GroupTheory/TwoClosureSolvableCompositionFactorsKourovka19Problem67Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/TwoClosureSolvableCompositionFactorsKourovka19Problem67Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/2-closures-of-permutation-groups/index.html#solvable-two-closure-factors-cyclic-or-a).

## Skresanov's counterexample to Kourovka Problem 19.67

There exist a finite set $\Omega$, a
solvable subgroup $G$ of the symmetric group $\mathrm{Sym}(\Omega)$, and a composition factor $S$
of the $2$-closure $G^{(2)}$ of $G$ such that $S$ is not cyclic and $S$ is not isomorphic to the
alternating group $A_n$ for any $n$. Here $G^{(2)}$ is the subgroup of $\mathrm{Sym}(\Omega)$
generated by the permutations $\sigma$ such that for all $\alpha, \beta \in \Omega$ some $g \in G$
has $g(\alpha) = \sigma(\alpha)$ and $g(\beta) = \sigma(\beta)$, and a composition factor of
$G^{(2)}$ is a simple group onto which some subnormal subgroup of $G^{(2)}$ maps.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 19.67 (I. Ponomarenko); resolution: S. V. Skresanov, Counterexamples to two conjectures in the Kourovka notebook, Algebra Logic 58 (2019), no. 3, 249-253, abstract: counterexamples to Questions 12.78 and 19.67 of the Kourovka Notebook; Kourovka Archive, Problem 19.67: No, it is not true, https://doi.org/10.1007/s10469-019-09543-1.

Stated but not proved: `MathlibExt.GroupTheory.TwoClosureSolvableCompositionFactorsKourovka19Problem67Wanted.solvableTwoClosureFactorsCyclicOrAlternating_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/TwoClosureSolvableCompositionFactorsKourovka19Problem67Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/TwoClosureSolvableCompositionFactorsKourovka19Problem67Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/2-closures-of-permutation-groups/index.html#solvable-two-closure-factors-cyclic-or-a-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: 2-closures of permutation groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/2-closures-of-permutation-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/2-closures-of-permutation-groups)
