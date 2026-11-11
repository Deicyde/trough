---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.KourovkaNotebookShared.IsChiefFactor, MathlibExt.GroupTheory.KourovkaNotebookShared.FittingHeightLE, MathlibExt.GroupTheory.KourovkaNotebookShared.IsCompositionFactor, MathlibExt.GroupTheory.KourovkaNotebookShared.IsConjugacySeparable, MathlibExt.GroupTheory.KourovkaNotebookShared.IsResiduallyFiniteP, MathlibExt.GroupTheory.KourovkaNotebookShared.restrictedWreath, MathlibExt.GroupTheory.KourovkaNotebookShared.IsPrimePartition, MathlibExt.GroupTheory.KourovkaNotebookShared.IsSigmaPrimary
statement: formalized
---

# σ-solubility, σ-nilpotency and σ-subnormality

13 results, 12 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/solubility-nilpotency-and-subnormality/index.html).

## Chief factors

For subgroups $A$ and $B$ of a group $G$, $A / B$ is a chief factor of $G$
if $A$ and $B$ are normal in $G$, $B < A$, and every normal subgroup $N$ of $G$ with
$B \le N \le A$ equals $B$ or $A$.

Formalized by `MathlibExt.GroupTheory.KourovkaNotebookShared.IsChiefFactor`, a definition declared in [WantedExt/GroupTheory/KourovkaNotebookShared.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/KourovkaNotebookShared.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/solubility-nilpotency-and-subnormality/index.html#is-chief-factor).

## Groups of Fitting height at most $h$

For a natural number $h$, a group $G$ has Fitting
height (nilpotent length) at most $h$ if there are normal subgroups
$1 = G_0 \le G_1 \le \cdots \le G_h = G$ of $G$ such that for every $i < h$ some term of the lower
central series of $G_{i+1}$ lies in $G_i$, that is, $G_{i+1} / G_i$ is nilpotent.

Formalized by `MathlibExt.GroupTheory.KourovkaNotebookShared.FittingHeightLE`, a definition declared in [WantedExt/GroupTheory/KourovkaNotebookShared.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/KourovkaNotebookShared.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/solubility-nilpotency-and-subnormality/index.html#fitting-height-le).

## Composition factors via subnormal subgroups

A group $S$ is a composition factor of a group
$K$ if $S$ is simple and some subnormal subgroup $H$ of $K$ has a surjective homomorphism onto $S$.

For finite $K$ this is the same as $S$ occurring as a factor of a composition series of $K$
(refine the subnormal chain through the kernel).

Formalized by `MathlibExt.GroupTheory.KourovkaNotebookShared.IsCompositionFactor`, a definition declared in [WantedExt/GroupTheory/KourovkaNotebookShared.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/KourovkaNotebookShared.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/solubility-nilpotency-and-subnormality/index.html#is-composition-factor).

## Conjugacy separable groups

A group $G$ is conjugacy separable if any two elements
$x, y \in G$ whose images are conjugate in every quotient $G / N$ by a normal subgroup $N$ of
finite index (that is, $g x g^{-1} y^{-1} \in N$ for some $g \in G$) are conjugate in $G$.

Formalized by `MathlibExt.GroupTheory.KourovkaNotebookShared.IsConjugacySeparable`, a definition declared in [WantedExt/GroupTheory/KourovkaNotebookShared.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/KourovkaNotebookShared.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/solubility-nilpotency-and-subnormality/index.html#is-conjugacy-separable).

## Residually finite $p$-groups

For a natural number $p$, a group $G$ is residually a finite
$p$-group if every element $g \ne 1$ of $G$ lies outside some normal subgroup of $G$ whose index
is $p^k$ for some $k \ge 0$, where an infinite index counts as $0$.

This notion appears in Kourovka Notebook problems 1.84, 4.52 and 10.30.

Formalized by `MathlibExt.GroupTheory.KourovkaNotebookShared.IsResiduallyFiniteP`, a definition declared in [WantedExt/GroupTheory/KourovkaNotebookShared.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/KourovkaNotebookShared.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/solubility-nilpotency-and-subnormality/index.html#is-residually-finite-p).

## Restricted wreath product

For groups $A$ and $B$, let $A \wr_r B = A^B \rtimes B$ be the
regular (unrestricted) wreath product, where $A^B$ is the group of all functions $f : B \to A$ and
$b \in B$ acts on it by $(b \cdot f)(x) = f(b^{-1} x)$. The restricted wreath product $A \wr B$ is
the subgroup of $A \wr_r B$ generated by the elements $(f, b)$ whose function part $f$ has finite
support, that is, $f(x) \ne 1$ for only finitely many $x \in B$.

These elements already form a subgroup, and for finite $B$ it is all of $A \wr_r B$.

Formalized by `MathlibExt.GroupTheory.KourovkaNotebookShared.restrictedWreath`, a definition declared in [WantedExt/GroupTheory/KourovkaNotebookShared.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/KourovkaNotebookShared.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/solubility-nilpotency-and-subnormality/index.html#restricted-wreath).

## Partitions of the primes

A family $\sigma = (\sigma_i)_{i \in I}$ of sets of natural
numbers is a partition of the primes if every $\sigma_i$ is a nonempty set of primes, $\sigma_i$
and $\sigma_j$ are disjoint whenever $i \ne j$, and every prime lies in some $\sigma_i$.

Formalized by `MathlibExt.GroupTheory.KourovkaNotebookShared.IsPrimePartition`, a definition declared in [WantedExt/GroupTheory/KourovkaNotebookShared.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/KourovkaNotebookShared.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/solubility-nilpotency-and-subnormality/index.html#is-prime-partition).

## $\sigma$-primary numbers

For a family $\sigma = (\sigma_i)_{i \in I}$ of sets of natural
numbers, a natural number $n$ is $\sigma$-primary if there is an index $i$ such that every prime
divisor of $n$ lies in $\sigma_i$. For $n = 0$ this means that some $\sigma_i$ contains every
prime.

A finite group is called $\sigma$-primary when its order is.

Formalized by `MathlibExt.GroupTheory.KourovkaNotebookShared.IsSigmaPrimary`, a definition declared in [WantedExt/GroupTheory/KourovkaNotebookShared.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/KourovkaNotebookShared.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/solubility-nilpotency-and-subnormality/index.html#is-sigma-primary).

## $\sigma$-subnormal subgroups

For a family $\sigma = (\sigma_i)_{i \in I}$ of sets of
natural numbers, a subgroup $A$ of a group $G$ is $\sigma$-subnormal in $G$ if there is a chain of
subgroups $A = A_0 \le A_1 \le \cdots \le A_n = G$ such that for every $i < n$ either $A_i$ is
normal in $A_{i+1}$, or the index in $A_{i+1}$ of the normal core of $A_i$ in $A_{i+1}$ is
$\sigma$-primary (an infinite index counts as $0$).

Formalized by `MathlibExt.GroupTheory.KourovkaNotebookShared.IsSigmaSubnormal`, a definition declared in [WantedExt/GroupTheory/KourovkaNotebookShared.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/KourovkaNotebookShared.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/solubility-nilpotency-and-subnormality/index.html#is-sigma-subnormal).

## $\sigma$-nilpotent groups

For a family $\sigma = (\sigma_i)_{i \in I}$ of sets of natural
numbers, a group $G$ is $\sigma$-nilpotent if it is the internal direct product of finitely many
normal subgroups $H_1, \dots, H_t$ whose orders are $\sigma$-primary (the order of an infinite
subgroup counts as $0$): the $H_k$ generate $G$, and each $H_k$ meets the subgroup generated by
the others trivially.

Formalized by `MathlibExt.GroupTheory.KourovkaNotebookShared.IsSigmaNilpotent`, a definition declared in [WantedExt/GroupTheory/KourovkaNotebookShared.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/KourovkaNotebookShared.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/solubility-nilpotency-and-subnormality/index.html#is-sigma-nilpotent).

## $\sigma$-soluble groups

For a family $\sigma = (\sigma_i)_{i \in I}$ of sets of natural
numbers, a group $G$ is $\sigma$-soluble if for every chief factor $A / B$ of $G$ the index
$|A : B|$ is $\sigma$-primary (an infinite index counts as $0$).

Formalized by `MathlibExt.GroupTheory.KourovkaNotebookShared.IsSigmaSoluble`, a definition declared in [WantedExt/GroupTheory/KourovkaNotebookShared.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/KourovkaNotebookShared.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/solubility-nilpotency-and-subnormality/index.html#is-sigma-soluble).

## Skiba's $\sigma$-subnormality question (Kourovka 19.84)

The statement that for every
partition $\sigma$ of the set of primes, every finite group $G$ and every subgroup $A$ of $G$, if
$A$ is $\sigma$-subnormal in the subgroup $\langle A, A^x \rangle$ generated by $A$ and
$A^x = xAx^{-1}$ for every $x \in G$, then $A$ is $\sigma$-subnormal in $G$.

Formalized by `MathlibExt.GroupTheory.SigmaSubnormalJoinConjugateKourovka19Problem84Wanted.sigmaSubnormalFromJoinsWithConjugates`, a definition declared in [WantedExt/GroupTheory/SigmaSubnormalJoinConjugateKourovka19Problem84Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SigmaSubnormalJoinConjugateKourovka19Problem84Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/solubility-nilpotency-and-subnormality/index.html#sigma-subnormal-from-joins-with-conjugat).

## A counterexample to Skiba's $\sigma$-subnormality question

The statement of Kourovka
Problem 19.84 is false: there are a partition $\sigma$ of the set of primes, a finite group $G$
and a subgroup $A$ of $G$ such that $A$ is $\sigma$-subnormal in the subgroup
$\langle A, A^x \rangle$ generated by $A$ and $A^x = xAx^{-1}$ for every $x \in G$, but $A$ is
not $\sigma$-subnormal in $G$.

Tyutyanov's example is $G = S_5$, a partition with blocks $\{2, 3\}$ and $\{5\}$, and
$A = \langle (1\,2) \rangle$. Wielandt's theorem gives the affirmative answer for the partition
into single primes.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 19.84 (A. N. Skiba); resolution: V. N. Tyutyanov, letter of 28 August 2019, Kourovka Archive, Problem 19.84: No, not always; in G = S₅ with σ = {2, 3} ∪ {5} the subgroup A = ⟨(12)⟩ is σ-subnormal in ⟨A, A^x⟩ for every x but not σ-subnormal in G, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.SigmaSubnormalJoinConjugateKourovka19Problem84Wanted.sigmaSubnormalFromJoinsWithConjugates_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/SigmaSubnormalJoinConjugateKourovka19Problem84Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SigmaSubnormalJoinConjugateKourovka19Problem84Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/solubility-nilpotency-and-subnormality/index.html#sigma-subnormal-from-joins-with-conjugat-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: σ-solubility, σ-nilpotency and σ-subnormality](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/solubility-nilpotency-and-subnormality/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/soluble-finite-groups/solubility-nilpotency-and-subnormality)
