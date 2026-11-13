---
declaration: section
origin: cited
lean: MetaMathlibExt.compoundSequence, MetaMathlibExt.compoundSequence_zero, MetaMathlibExt.compoundSequence_self, MetaMathlibExt.frobenius_eq_max_apery_sub, MetaMathlibExt.compoundSequence_apery_and_frobenius, MetaMathlibExt.compoundSequence_erase_cofinite_iff, MetaMathlibExt.compoundSequence_erase_frobenius_eq_iff, MetaMathlibExt.compoundSequence_embeddingDimension
statement: formalized
---

# Frobenius numbers of compound sequences

9 results, 3 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/frobenius-numbers-of-compound-sequences/index.html).

## Compound sequence

Let $n$ be a natural number and let $a = (a_i)$ and $b = (b_i)$ be
sequences of natural numbers. For a natural number $j$, the $j$-th term of the compound sequence
of $a$ and $b$ is

$$c_j = \Big(\prod_{i=1}^{j} b_i\Big) \Big(\prod_{i=j+1}^{n} a_i\Big),$$

so that $c_j = b_1 b_2 \cdots b_j \, a_{j+1} \cdots a_n$ for $0 \le j \le n$, the range of
interest; for $j > n$ the second product is empty and $c_j = b_1 \cdots b_j$.

## Sources

- Edgar Federico Elizeche and Amitabha Tripathi, *A Note on Deletions from Compound Sequences That Leave the Frobenius Number Invariant*, INTEGERS 25 (2025), Article A6, Section 2, eq. (1) (after Kiers, O'Neill, and Ponomarenko).

Formalized by `MetaMathlibExt.compoundSequence`, a definition declared in [WantedExt/NumberTheory/CompoundSequenceFrobeniusWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompoundSequenceFrobeniusWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/frobenius-numbers-of-compound-sequences/index.html#compound-sequence).

## First term of a compound sequence

For every natural number $n$ and all sequences $a$, $b$
of natural numbers, the compound sequence $c$ of $a$ and $b$ satisfies $c_0 = a_1 a_2 \cdots a_n$.

## Sources

- Edgar Federico Elizeche and Amitabha Tripathi, *A Note on Deletions from Compound Sequences That Leave the Frobenius Number Invariant*, INTEGERS 25 (2025), Article A6, Section 2, eq. (1).

Formalized by `MetaMathlibExt.compoundSequence_zero`, a theorem declared in [WantedExt/NumberTheory/CompoundSequenceFrobeniusWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompoundSequenceFrobeniusWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/frobenius-numbers-of-compound-sequences/index.html#compound-sequence-zero).

## Last term of a compound sequence

For every natural number $n$ and all sequences $a$, $b$
of natural numbers, the compound sequence $c$ of $a$ and $b$ satisfies $c_n = b_1 b_2 \cdots b_n$.

## Sources

- Edgar Federico Elizeche and Amitabha Tripathi, *A Note on Deletions from Compound Sequences That Leave the Frobenius Number Invariant*, INTEGERS 25 (2025), Article A6, Section 2, eq. (1).

Formalized by `MetaMathlibExt.compoundSequence_self`, a theorem declared in [WantedExt/NumberTheory/CompoundSequenceFrobeniusWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompoundSequenceFrobeniusWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/frobenius-numbers-of-compound-sequences/index.html#compound-sequence-self).

## Brauer–Shockley formula for the Frobenius number

Let $A_1, \dots, A_k$ be positive
integers with $\gcd(A_1, \dots, A_k) = 1$, let $S$ be the additive submonoid of $\mathbb{N}$ they
generate, and let $a = A_i$ be one of them with $a \ge 2$. For $1 \le x \le a - 1$ let $m_x$ be
the least element of $S$ congruent to $x$ modulo $a$. If $M$ is the largest of the numbers $m_x$,
then $M - a$ is the largest integer not in $S$, that is, the Frobenius number of $S$.

The case $a = 1$, where the maximum would be over an empty set, is excluded.

## Sources

- Edgar Federico Elizeche and Amitabha Tripathi, *A Note on Deletions from Compound Sequences That Leave the Frobenius Number Invariant*, INTEGERS 25 (2025), Article A6, Lemma 1, quoting Brauer and Shockley.

Stated but not proved: `MetaMathlibExt.frobenius_eq_max_apery_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompoundSequenceFrobeniusWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompoundSequenceFrobeniusWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/frobenius-numbers-of-compound-sequences/index.html#frobenius-eq-max-apery-sub).

## Apéry set and Frobenius number of a compound sequence

Let $n$ be a natural number and
let $a_1, \dots, a_n$ and $b_1, \dots, b_n$ be natural numbers with $0 < a_i < b_i$ for
$1 \le i \le n$ and $\gcd(a_i, b_j) = 1$ whenever $1 \le j \le i \le n$. Let $c_0, \dots, c_n$
be their compound sequence and $S$ the additive submonoid of $\mathbb{N}$ generated by
$c_0, \dots, c_n$. Then (Kiers, O'Neill and Ponomarenko) the Apéry set of $S$ with respect to
$c_0$, the set of least elements of $S$ in the residue classes modulo $c_0$, is

$$\Big\{\sum_{i=1}^{n} c_i x_i : x_1, \dots, x_n \in \mathbb{N},\ x_i < a_i\Big\},$$

and the largest integer not in $S$, the Frobenius number of $S$, is

$$F(S) = \sum_{i=1}^{n} (a_i - 1) c_i - c_0.$$

## Sources

- Edgar Federico Elizeche and Amitabha Tripathi, *A Note on Deletions from Compound Sequences That Leave the Frobenius Number Invariant*, INTEGERS 25 (2025), Article A6, Theorem 2, eq. (2), quoting Kiers, O'Neill, and Ponomarenko.

Stated but not proved: `MetaMathlibExt.compoundSequence_apery_and_frobenius` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompoundSequenceFrobeniusWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompoundSequenceFrobeniusWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/frobenius-numbers-of-compound-sequences/index.html#compound-sequence-apery-and-frobenius).

## When deleting a term of a compound sequence leaves a numerical semigroup

Let $n \ge 1$
and let $a_1, \dots, a_n$ and $b_1, \dots, b_n$ be natural numbers with $0 < a_i < b_i$ for
$1 \le i \le n$ and $\gcd(a_i, b_j) = 1$ whenever $1 \le j \le i \le n$; let $c_0, \dots, c_n$
be their compound sequence. For $0 \le j \le n$, the additive submonoid of $\mathbb{N}$
generated by the terms $c_i$ with $0 \le i \le n$ and $i \ne j$ has finite complement in
$\mathbb{N}$ (so it is a numerical semigroup) if and only if either $0 < j < n$ and
$\gcd(a_j, b_{j+1}) = 1$, or $j = n$ and $a_n = 1$.

## Sources

- Edgar Federico Elizeche and Amitabha Tripathi, *A Note on Deletions from Compound Sequences That Leave the Frobenius Number Invariant*, INTEGERS 25 (2025), Article A6, Proposition 3.

Stated but not proved: `MetaMathlibExt.compoundSequence_erase_cofinite_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompoundSequenceFrobeniusWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompoundSequenceFrobeniusWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/frobenius-numbers-of-compound-sequences/index.html#compound-sequence-erase-cofinite-iff).

## Deletions from a compound sequence that keep the Frobenius number

Let $n$ be a natural
number and let $(a_i)_{i \ge 0}$ and $(b_i)_{i \ge 0}$ be sequences of natural numbers with
$0 < a_i < b_i$ for $1 \le i \le n$ and $\gcd(a_i, b_j) = 1$ whenever $1 \le j \le i \le n$; let
$c_0, \dots, c_n$ be their compound sequence. Let $0 \le j \le n$ and suppose that the terms
$c_i$ with $0 \le i \le n$ and $i \ne j$ have greatest common divisor $1$. Let $S$ be the
additive submonoid of $\mathbb{N}$ generated by $c_0, \dots, c_n$ and $S^\star$ the one
generated by the $c_i$ with $0 \le i \le n$ and $i \ne j$. Then some integer is both the largest
integer not in $S^\star$ and the largest integer not in $S$, that is, $S^\star$ and $S$ have the
same Frobenius number, if and only if $a_j = 1$.

## Sources

- Edgar Federico Elizeche and Amitabha Tripathi, *A Note on Deletions from Compound Sequences That Leave the Frobenius Number Invariant*, INTEGERS 25 (2025), Article A6, Theorem 4.

Stated but not proved: `MetaMathlibExt.compoundSequence_erase_frobenius_eq_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompoundSequenceFrobeniusWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompoundSequenceFrobeniusWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/frobenius-numbers-of-compound-sequences/index.html#compound-sequence-erase-frobenius-eq-iff).

## Embedding dimension of the semigroup of a compound sequence

Let $n$ be a natural number
and let $a_1, \dots, a_n$ and $b_1, \dots, b_n$ be natural numbers with $0 < a_i < b_i$ for
$1 \le i \le n$ and $\gcd(a_i, b_j) = 1$ whenever $1 \le j \le i \le n$; let $c_0, \dots, c_n$
be their compound sequence and $S$ the additive submonoid of $\mathbb{N}$ generated by
$c_0, \dots, c_n$. Let $k$ be the number of indices $1 \le i \le n$ with $a_i = 1$. Then the
minimal generating set of $S$, the set of nonzero elements of $S$ that are not a sum of two
nonzero elements of $S$, has exactly $n - k + 1$ elements; that is, the embedding dimension of
$S$ is $n - k + 1$.

## Sources

- Edgar Federico Elizeche and Amitabha Tripathi, *A Note on Deletions from Compound Sequences That Leave the Frobenius Number Invariant*, INTEGERS 25 (2025), Article A6, Theorem 5.

Stated but not proved: `MetaMathlibExt.compoundSequence_embeddingDimension` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompoundSequenceFrobeniusWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompoundSequenceFrobeniusWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/frobenius-numbers-of-compound-sequences/index.html#compound-sequence-embedding-dimension).

## The minimal generating set as the least Frobenius-preserving subset

Let $n$ be a natural
number and let $a_1, \dots, a_n$ and $b_1, \dots, b_n$ be natural numbers with $0 < a_i < b_i$
for $1 \le i \le n$ and $\gcd(a_i, b_j) = 1$ whenever $1 \le j \le i \le n$; let
$C = \{c_0, \dots, c_n\}$ be the set of terms of their compound sequence and $S$ the additive
submonoid of $\mathbb{N}$ generated by $C$. Say that a set $G$ of natural numbers has the same
Frobenius number as $S$ if some integer is both the largest integer not in the submonoid
generated by $G$ and the largest integer not in $S$. Let $M$ be the minimal generating set of
$S$, the set of nonzero elements of $S$ that are not a sum of two nonzero elements of $S$. Then
$M \subseteq C$ and $M$ has the same Frobenius number as $S$, and every subset $C' \subseteq C$
with the same Frobenius number as $S$ has at least as many elements as $M$, with the same number
of elements only if $C' = M$.

## Sources

- Edgar Federico Elizeche and Amitabha Tripathi, *A Note on Deletions from Compound Sequences That Leave the Frobenius Number Invariant*, INTEGERS 25 (2025), Article A6, Theorem 6.

Stated but not proved: `MetaMathlibExt.compoundSequence_minimal_generating_set_least` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompoundSequenceFrobeniusWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompoundSequenceFrobeniusWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/frobenius-numbers-of-compound-sequences/index.html#compound-sequence-minimal-generating-set).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Frobenius numbers of compound sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/frobenius-numbers-of-compound-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/numerical-semigroups/frobenius-numbers-of-compound-sequences)
