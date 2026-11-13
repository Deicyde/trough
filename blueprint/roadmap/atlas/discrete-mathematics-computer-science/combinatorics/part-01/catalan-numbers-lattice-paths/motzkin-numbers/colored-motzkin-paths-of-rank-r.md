---
declaration: section
origin: cited
lean: MetaMathlibExt.ULDMotzkin.ULDMotzkinStep, MetaMathlibExt.ULDMotzkin.stepHeight, MetaMathlibExt.ULDMotzkin.pathHeight, MetaMathlibExt.ULDMotzkin.IsMotzkinPath, MetaMathlibExt.ULDMotzkin.ULDMotzkinPath, MetaMathlibExt.ULDMotzkin.uldMotzkinNumber, MetaMathlibExt.ULDMotzkin.uldMotzkinNumber_eq_card
statement: formalized
proof: formalized
---

# Colored Motzkin paths of rank r

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/colored-motzkin-paths-of-rank-r/index.html).

## Colored Motzkin steps of a given rank

Let $r$ and $l$ be natural numbers and let
$u, d \colon \{0, \dots, r - 1\} \to \mathbb{N}$. The admissible steps of rank $r$ are the
up-steps $U_j$ with $0 \le j < r$ in one of $u(j)$ colors, the level steps in one of $l$ colors,
and the down-steps $D_j$ with $0 \le j < r$ in one of $d(j)$ colors: the disjoint union of the
sets $\{j\} \times \{0, \dots, u(j) - 1\}$ for $j < r$, the set $\{0, \dots, l - 1\}$, and the
sets $\{j\} \times \{0, \dots, d(j) - 1\}$ for $j < r$.

A step kind with zero colors contributes no steps. The steps $U_j$ and $D_j$ have jump size
$j + 1$, so no up- or down-step has jump size zero.

Formalized by `MetaMathlibExt.ULDMotzkin.ULDMotzkinStep`, an abbreviation declared in [MathlibExt/Combinatorics/Enumerative/ULDMotzkinNumberOfRankR.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/ULDMotzkinNumberOfRankR.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/colored-motzkin-paths-of-rank-r/index.html#uldmotzkin-step).

## Height change of a colored Motzkin step

The height change of an admissible step of
rank $r$ is the integer $j + 1$ for an up-step $U_j$ with $0 \le j < r$, $0$ for a level step,
and $-(j + 1)$ for a down-step $D_j$ with $0 \le j < r$, whatever its color.

Formalized by `MetaMathlibExt.ULDMotzkin.stepHeight`, a definition declared in [MathlibExt/Combinatorics/Enumerative/ULDMotzkinNumberOfRankR.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/ULDMotzkinNumberOfRankR.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/colored-motzkin-paths-of-rank-r/index.html#step-height).

## Height of a colored step sequence after k steps

For a sequence
$p = (p_0, \dots, p_{n-1})$ of $n$ admissible steps of rank $r$ and a natural number $k$, the
height of $p$ after $k$ steps is the integer $\sum_{i < \min(k, n)} h(p_i)$, where $h$ is the
height change of a step. For $k \ge n$ it is the height of the whole sequence.

Formalized by `MetaMathlibExt.ULDMotzkin.pathHeight`, a definition declared in [MathlibExt/Combinatorics/Enumerative/ULDMotzkinNumberOfRankR.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/ULDMotzkinNumberOfRankR.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/colored-motzkin-paths-of-rank-r/index.html#path-height).

## Colored Motzkin path condition

Let $r \ge 1$. A sequence
$p = (p_0, \dots, p_{n-1})$ of $n$ admissible steps of rank $r$ is a Motzkin path when its
height after $k$ steps is nonnegative for every $k$ with $0 \le k \le n$ and its height after
$n$ steps is $0$.

Formalized by `MetaMathlibExt.ULDMotzkin.IsMotzkinPath`, a definition declared in [MathlibExt/Combinatorics/Enumerative/ULDMotzkinNumberOfRankR.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/ULDMotzkinNumberOfRankR.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/colored-motzkin-paths-of-rank-r/index.html#is-motzkin-path).

## Colored Motzkin paths of rank r and length n

For $r \ge 1$ and a natural number $n$,
the colored Motzkin paths of rank $r$ and length $n$ are the sequences
$(p_0, \dots, p_{n-1})$ of $n$ admissible steps of rank $r$ that satisfy the Motzkin path
condition: the height after $k$ steps is nonnegative for every $k \le n$, and the height after
$n$ steps is $0$.

Formalized by `MetaMathlibExt.ULDMotzkin.ULDMotzkinPath`, a definition declared in [MathlibExt/Combinatorics/Enumerative/ULDMotzkinNumberOfRankR.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/ULDMotzkinNumberOfRankR.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/colored-motzkin-paths-of-rank-r/index.html#uldmotzkin-path).

## (u,l,d)-Motzkin numbers of rank r

Let $r \ge 1$ and $l$ be natural numbers and let
$u, d \colon \{0, \dots, r - 1\} \to \mathbb{N}$. For a natural number $n$, the
$(u,l,d)$-Motzkin number of rank $r$ and length $n$ is the number of colored Motzkin paths of
rank $r$ and length $n$ whose up-steps $U_j$ come in $u(j)$ colors, whose level steps come in
$l$ colors, and whose down-steps $D_j$ come in $d(j)$ colors.

Formalized by `MetaMathlibExt.ULDMotzkin.uldMotzkinNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/ULDMotzkinNumberOfRankR.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/ULDMotzkinNumberOfRankR.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/colored-motzkin-paths-of-rank-r/index.html#uld-motzkin-number).

## The (u,l,d)-Motzkin number counts Motzkin step sequences

Let $r \ge 1$ and $l$ be
natural numbers and let $u, d \colon \{0, \dots, r - 1\} \to \mathbb{N}$. For every natural
number $n$, the $(u,l,d)$-Motzkin number of rank $r$ and length $n$ equals the number of
sequences of $n$ admissible steps of rank $r$ with these color counts that satisfy the Motzkin
path condition.

This holds by definition.

Formalized by `MetaMathlibExt.ULDMotzkin.uldMotzkinNumber_eq_card`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/ULDMotzkinNumberOfRankR.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/ULDMotzkinNumberOfRankR.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/colored-motzkin-paths-of-rank-r/index.html#uld-motzkin-number-eq-card).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Colored Motzkin paths of rank r](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/colored-motzkin-paths-of-rank-r/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/colored-motzkin-paths-of-rank-r)
