---
declaration: section
origin: cited
lean: Set.IsAsymptoticAddBasisOfOrder, Set.IsAddBasisOfOrder, Set.IsAsymptoticAddBasis, Set.IsWeakAddBasisOfOrder, Set.IsWeakAddBasis, MathlibExt.NumberTheory.ErdosProblem869Wanted.addSumset, MathlibExt.NumberTheory.ErdosProblem869Wanted.IsAdditiveBasisOrder2, MathlibExt.NumberTheory.ErdosProblem869Wanted.IsMinimalAdditiveBasisOrder2
statement: formalized
---

# Asymptotic additive bases

10 results, 9 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/asymptotic-additive-bases/index.html).

## Asymptotic additive basis of order $n$

Let $M$ be an additive commutative monoid,
$A \subseteq M$ and $n$ a natural number. $A$ is an asymptotic additive basis of order $n$ if all
but finitely many elements of $M$ are sums of exactly $n$ (not necessarily distinct) elements of
$A$, that is, $M \setminus nA$ is finite, where $nA = \{a_1 + \dots + a_n : a_1, \dots, a_n \in A\}$
and $0A = \{0\}$.

For $M = \mathbb{N}$ this means that every sufficiently large natural number is such a sum.

Formalized by `Set.IsAsymptoticAddBasisOfOrder`, a definition declared in [MathlibExt/Combinatorics/Additive/Basis.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/Basis.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/asymptotic-additive-bases/index.html#is-asymptotic-add-basis-of-order).

## Exact additive basis of order $n$

Let $M$ be an additive commutative monoid,
$A \subseteq M$ and $n$ a natural number. $A$ is an exact additive basis of order $n$ if every
element of $M$ is a sum of exactly $n$ (not necessarily distinct) elements of $A$, that is,
$M = nA$, where $nA = \{a_1 + \dots + a_n : a_1, \dots, a_n \in A\}$ and $0A = \{0\}$.

Formalized by `Set.IsAddBasisOfOrder`, a definition declared in [MathlibExt/Combinatorics/Additive/Basis.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/Basis.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/asymptotic-additive-bases/index.html#is-add-basis-of-order).

## Asymptotic additive basis

A subset $A$ of an additive commutative monoid $M$ is an
asymptotic additive basis if there is a natural number $n$ such that $A$ is an asymptotic additive
basis of order $n$, that is, all but finitely many elements of $M$ are sums of exactly $n$ (not
necessarily distinct) elements of $A$.

Formalized by `Set.IsAsymptoticAddBasis`, a definition declared in [MathlibExt/Combinatorics/Additive/Basis.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/Basis.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/asymptotic-additive-bases/index.html#is-asymptotic-add-basis).

## Weak additive basis of order $n$

Let $M$ be an additive commutative monoid,
$A \subseteq M$ and $n$ a natural number. $A$ is a weak additive basis of order $n$ if every
element of $M$ is a sum of at most $n$ (not necessarily distinct) elements of $A$, that is, lies
in $mA$ for some $m \le n$, where $mA = \{a_1 + \dots + a_m : a_1, \dots, a_m \in A\}$ and
$0A = \{0\}$.

Formalized by `Set.IsWeakAddBasisOfOrder`, a definition declared in [MathlibExt/Combinatorics/Additive/Basis.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/Basis.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/asymptotic-additive-bases/index.html#is-weak-add-basis-of-order).

## Weak additive basis

A subset $A$ of an additive commutative monoid $M$ is a weak additive
basis if there is a natural number $n$ such that $A$ is a weak additive basis of order $n$, that
is, every element of $M$ is a sum of at most $n$ (not necessarily distinct) elements of $A$.

Formalized by `Set.IsWeakAddBasis`, a definition declared in [MathlibExt/Combinatorics/Additive/Basis.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/Basis.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/asymptotic-additive-bases/index.html#is-weak-add-basis).

## Sumset of a set of naturals

For a set $A$ of natural numbers, $A + A$ is the set of
natural numbers $n$ such that $n = a + b$ for some $a, b \in A$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem869Wanted.addSumset`, a definition declared in [WantedExt/NumberTheory/ErdosProblem869Wanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem869Wanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/asymptotic-additive-bases/index.html#add-sumset).

## Additive basis of order 2

A set $A$ of natural numbers is an additive basis of order $2$
if there is a natural number $N$ such that every natural number $n \ge N$ can be written as
$n = a + b$ with $a, b \in A$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem869Wanted.IsAdditiveBasisOrder2`, a definition declared in [WantedExt/NumberTheory/ErdosProblem869Wanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem869Wanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/asymptotic-additive-bases/index.html#is-additive-basis-order2).

## Minimal additive basis of order 2

A set $A$ of natural numbers is a minimal additive
basis of order $2$ if it is an additive basis of order $2$ and, for every $a \in A$, infinitely
many natural numbers do not lie in the sumset $(A \setminus \{a\}) + (A \setminus \{a\})$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem869Wanted.IsMinimalAdditiveBasisOrder2`, a definition declared in [WantedExt/NumberTheory/ErdosProblem869Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem869Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/asymptotic-additive-bases/index.html#is-minimal-additive-basis-order2).

## Erdős Problem 869 (disjoint bases and minimal bases)

The statement that for all disjoint
sets $A_1$ and $A_2$ of natural numbers that are both additive bases of order $2$, there is a set
$B \subseteq A_1 \cup A_2$ that is a minimal additive basis of order $2$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem869Wanted.Statement`, a definition declared in [WantedExt/NumberTheory/ErdosProblem869Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem869Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/asymptotic-additive-bases/index.html#statement).

## Erdős Problem 869 is false (Larsen)

There are disjoint sets $A_1$ and $A_2$ of natural
numbers, both additive bases of order $2$, such that no subset of $A_1 \cup A_2$ is a minimal
additive basis of order $2$.

## Sources

- Daniel Larsen, Three questions of Erdős–Nathanson on asymptotic bases of order 2, arXiv:2603.03472 (2026), https://arxiv.org/abs/2603.03472; Lean proof of the negative answer to Erdős Problem 869, https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos869.lean#L3490.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem869Wanted.Statement_refuted` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem869Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem869Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/asymptotic-additive-bases/index.html#statement-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Asymptotic additive bases](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/asymptotic-additive-bases/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/additive-bases/asymptotic-additive-bases)
