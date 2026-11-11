---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SumsetPartitionErdosProblem741Wanted.upperDensitySumsetSplits, MathlibExt.Combinatorics.SumsetPartitionErdosProblem741Wanted.HasBoundedGaps, MathlibExt.Combinatorics.SumsetPartitionErdosProblem741Wanted.basisWithoutBoundedGapSplit, MathlibExt.Combinatorics.SumsetPartitionErdosProblem741Wanted.upperDensitySumsetSplits_holds, MathlibExt.Combinatorics.SumsetPartitionErdosProblem741Wanted.basisWithoutBoundedGapSplit_holds, MathlibExt.NumberTheory.ErdosProblem871Wanted.conjecture, MathlibExt.NumberTheory.ErdosProblem871Wanted.disprovedForm, MathlibExt.NumberTheory.ErdosProblem871Wanted.conjecture_refuted
statement: formalized
---

# Splitting sets with dense sumsets

8 results, 5 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/splitting-sets-with-dense-sumsets/index.html).

## Erdős Problem 741, upper-density question

This proposition asserts that for every set
$A \subseteq \mathbb{N}$ whose sumset $A + A = \{a + b : a, b \in A\}$ has positive upper density
there are disjoint sets $A_1, A_2 \subseteq \mathbb{N}$ with $A_1 \cup A_2 = A$ such that both
$A_1 + A_1$ and $A_2 + A_2$ have positive upper density.

Formalized by `MathlibExt.Combinatorics.SumsetPartitionErdosProblem741Wanted.upperDensitySumsetSplits`, a definition declared in [WantedExt/Combinatorics/SumsetPartitionErdosProblem741Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SumsetPartitionErdosProblem741Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/splitting-sets-with-dense-sumsets/index.html#upper-density-sumset-splits).

## Sets with bounded gaps

A set $S \subseteq \mathbb{N}$ has bounded gaps (is syndetic) if
there is a natural number $g$ such that for every natural number $n$ some $s \in S$ satisfies
$n \le s < n + g$.

Formalized by `MathlibExt.Combinatorics.SumsetPartitionErdosProblem741Wanted.HasBoundedGaps`, a definition declared in [WantedExt/Combinatorics/SumsetPartitionErdosProblem741Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SumsetPartitionErdosProblem741Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/splitting-sets-with-dense-sumsets/index.html#has-bounded-gaps).

## Erdős Problem 741, bounded-gaps question

This proposition asserts that there is a set
$A \subseteq \mathbb{N}$ that is an asymptotic additive basis of order $2$ (all but finitely many
natural numbers are sums of two elements of $A$) such that for all disjoint sets
$A_1, A_2 \subseteq \mathbb{N}$ with $A_1 \cup A_2 = A$, the sumsets
$A_1 + A_1 = \{a + b : a, b \in A_1\}$ and $A_2 + A_2$ do not both have bounded gaps.

Formalized by `MathlibExt.Combinatorics.SumsetPartitionErdosProblem741Wanted.basisWithoutBoundedGapSplit`, a definition declared in [WantedExt/Combinatorics/SumsetPartitionErdosProblem741Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SumsetPartitionErdosProblem741Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/splitting-sets-with-dense-sumsets/index.html#basis-without-bounded-gap-split).

## Splitting a set whose sumset has positive upper density

For every set
$A \subseteq \mathbb{N}$ whose sumset $A + A = \{a + b : a, b \in A\}$ has positive upper density,
there are disjoint sets $A_1, A_2 \subseteq \mathbb{N}$ with $A_1 \cup A_2 = A$ such that both
$A_1 + A_1$ and $A_2 + A_2$ have positive upper density.

## Sources

- T. F. Bloom, Erdős Problems, Problem #741, https://www.erdosproblems.com/741 (status SOLVED (LEAN)); resolution: B. Alexeev, M. Putterman, M. Sawhney, M. Sellke and G. Valiant, Short proofs in combinatorics and number theory, arXiv:2603.29961 (2026); erdosproblems.com/741 (DeepMind), Theorem 3.1 of arXiv:2603.29961 (proof due to an internal OpenAI model): there is A ⊂ ℕ, a basis of order 2 with [4, ∞) ⊆ A + A, such that for every partition A = A₁ ⊔ A₂ one of A₁ + A₁, A₂ + A₂ does not have bounded gaps; erdosproblems.com/741: DeepMind gave a positive answer to the upper-density question (proof sketched in the comments), https://arxiv.org/abs/2603.29961.

Stated but not proved: `MathlibExt.Combinatorics.SumsetPartitionErdosProblem741Wanted.upperDensitySumsetSplits_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/SumsetPartitionErdosProblem741Wanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SumsetPartitionErdosProblem741Wanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/splitting-sets-with-dense-sumsets/index.html#upper-density-sumset-splits-holds).

## An asymptotic basis of order 2 admitting no bounded-gap splitting

There is a set
$A \subseteq \mathbb{N}$ that is an asymptotic additive basis of order $2$ (all but finitely many
natural numbers are sums of two elements of $A$) such that for all disjoint sets
$A_1, A_2 \subseteq \mathbb{N}$ with $A_1 \cup A_2 = A$, the sumsets
$A_1 + A_1 = \{a + b : a, b \in A_1\}$ and $A_2 + A_2$ do not both have bounded gaps, where a set
$S \subseteq \mathbb{N}$ has bounded gaps if for some $g \in \mathbb{N}$ every interval
$[n, n + g)$ with $n \in \mathbb{N}$ meets $S$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #741, https://www.erdosproblems.com/741 (status SOLVED (LEAN)); resolution: B. Alexeev, M. Putterman, M. Sawhney, M. Sellke and G. Valiant, Short proofs in combinatorics and number theory, arXiv:2603.29961 (2026); erdosproblems.com/741 (DeepMind), Theorem 3.1 of arXiv:2603.29961 (proof due to an internal OpenAI model): there is A ⊂ ℕ, a basis of order 2 with [4, ∞) ⊆ A + A, such that for every partition A = A₁ ⊔ A₂ one of A₁ + A₁, A₂ + A₂ does not have bounded gaps; erdosproblems.com/741: DeepMind gave a positive answer to the upper-density question (proof sketched in the comments), https://arxiv.org/abs/2603.29961.

Stated but not proved: `MathlibExt.Combinatorics.SumsetPartitionErdosProblem741Wanted.basisWithoutBoundedGapSplit_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/SumsetPartitionErdosProblem741Wanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SumsetPartitionErdosProblem741Wanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/splitting-sets-with-dense-sumsets/index.html#basis-without-bounded-gap-split-holds).

## Erdős Problem 871 (splitting rich bases of order 2)

The statement that for every set $A$
of natural numbers such that every sufficiently large $n$ is $a + b$ with $a, b \in A$ and, for
every natural number $t$, every sufficiently large $n$ has at least $t$ representations
$n = a + b$ with $a, b \in A$ and $a \le b$, the set $A$ is the disjoint union of two sets $B$ and
$C$ such that every sufficiently large $n$ is $a + b$ with $a, b \in B$ and every sufficiently
large $n$ is $a + b$ with $a, b \in C$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem871Wanted.conjecture`, a definition declared in [WantedExt/NumberTheory/ErdosProblem871Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem871Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/splitting-sets-with-dense-sumsets/index.html#conjecture).

## Negation of the Erdős Problem 871 statement

This is the proposition that there is a set
$A$ of natural numbers such that every sufficiently large $n$ is $a + b$ with $a, b \in A$ and,
for every natural number $t$, every sufficiently large $n$ has at least $t$ representations
$n = a + b$ with $a, b \in A$ and $a \le b$, but $A$ is not the disjoint union of two sets $B$
and $C$ such that every sufficiently large $n$ is $a + b$ with $a, b \in B$ and every
sufficiently large $n$ is $a + b$ with $a, b \in C$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem871Wanted.disprovedForm`, a definition declared in [WantedExt/NumberTheory/ErdosProblem871Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem871Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/splitting-sets-with-dense-sumsets/index.html#disproved-form).

## Erdős Problem 871 is false (Larsen)

There is a set $A$ of natural numbers such that every
sufficiently large $n$ is $a + b$ with $a, b \in A$ and, for every natural number $t$, every
sufficiently large $n$ has at least $t$ representations $n = a + b$ with $a, b \in A$ and
$a \le b$, but $A$ is not the disjoint union of two sets $B$ and $C$ such that every sufficiently
large $n$ is $a + b$ with $a, b \in B$ and every sufficiently large $n$ is $a + b$ with
$a, b \in C$.

## Sources

- Larsen (formalized in Lean), per erdosproblems.com/871, https://www.erdosproblems.com/871; Lean disproof of Erdos Problem 871 (Larsen with Claude Opus 4.5), plby/lean-proofs, https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos871.lean#L2388.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem871Wanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem871Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem871Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/splitting-sets-with-dense-sumsets/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Splitting sets with dense sumsets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/splitting-sets-with-dense-sumsets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/additive-bases/splitting-sets-with-dense-sumsets)
