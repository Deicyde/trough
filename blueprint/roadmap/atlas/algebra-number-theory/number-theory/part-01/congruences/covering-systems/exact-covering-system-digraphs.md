---
declaration: section
origin: cited
lean: MetaMathlibExt.ecsdAdj, MetaMathlibExt.ecsdAdj_two, MetaMathlibExt.IsKDescendant, MetaMathlibExt.isKDescendant_zero, MetaMathlibExt.isKDescendant_one, MetaMathlibExt.IsDigraphCycle, MetaMathlibExt.isDigraphCycle_singleton, MetaMathlibExt.isDigraphCycle_pair
statement: formalized
---

# Exact covering system digraphs

33 results, 8 proved and 25 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html).

## Edge relation of an exact covering system digraph

Let $r \in \mathbb{N}$ and let
$d_1, \dots, d_r$ and $a_1, \dots, a_r$ be integers. The digraph
$G(d_1 n + a_1, \dots, d_r n + a_r)$ has vertex set $\mathbb{Z}$ and an edge $x \to y$ iff
$y = d_i x + a_i$ for some $i \in \{1, \dots, r\}$.

When the pairs $(a_i, d_i)$ form an exact covering system this is the paper's digraph $G_S$;
the definition itself places no condition on the $d_i$ and $a_i$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Section 1 (definition of `G_S`).

Formalized by `MetaMathlibExt.ecsdAdj`, a definition declared in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-adj).

## Out-neighbours in a two-rule digraph

For all integers $d_1, d_2, a_1, a_2, x, y$, the
digraph $G(d_1 n + a_1, d_2 n + a_2)$ has an edge $x \to y$ iff $y = d_1 x + a_1$ or
$y = d_2 x + a_2$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Section 1 (definition of `G_S`).

Formalized by `MetaMathlibExt.ecsdAdj_two`, a theorem declared in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-adj-two).

## $k$-descendants in a digraph on the integers

Let $R$ be a digraph on $\mathbb{Z}$, let
$k \in \mathbb{N}$ and let $m, n \in \mathbb{Z}$. Then $n$ is a $k$-descendant of $m$ in $R$ when
there is a directed walk of exactly $k$ edges from $m$ to $n$, that is, integers
$m = x_0, x_1, \dots, x_k = n$ such that $R$ has an edge $x_{i-1} \to x_i$ for every
$1 \le i \le k$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Section 1 (definition of `k`-descendant).

Formalized by `MetaMathlibExt.IsKDescendant`, a definition declared in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#is-kdescendant).

## The only $0$-descendant of a vertex is itself

Let $R$ be a digraph on $\mathbb{Z}$ and let
$m, n \in \mathbb{Z}$. Then $n$ is a $0$-descendant of $m$ in $R$ if and only if $n = m$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Section 1 (definition of `k`-descendant).

Formalized by `MetaMathlibExt.isKDescendant_zero`, a theorem declared in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#is-kdescendant-zero).

## The $1$-descendants are the out-neighbours

Let $R$ be a digraph on $\mathbb{Z}$ and let
$m, n \in \mathbb{Z}$. Then $n$ is a $1$-descendant of $m$ in $R$ if and only if $R$ has an edge
$m \to n$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Section 1 (definition of successor).

Formalized by `MetaMathlibExt.isKDescendant_one`, a theorem declared in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#is-kdescendant-one).

## Cycles of a digraph on the integers

Let $R$ be a digraph on $\mathbb{Z}$, given by its edge
relation. A list $c = (c_1, \dots, c_t)$ of integers is a cycle of $R$ when it is nonempty, its
entries are pairwise distinct, and $R$ has the edges $c_1 \to c_2, \dots, c_{t-1} \to c_t$ and
$c_t \to c_1$ (for $t = 1$ this means a loop $c_1 \to c_1$).

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Section 2 (cycles `C = (c₁, …, c_t)`).

Formalized by `MetaMathlibExt.IsDigraphCycle`, a definition declared in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#is-digraph-cycle).

## One-vertex cycles of a digraph on the integers

Let $R$ be a digraph on $\mathbb{Z}$ and let
$x \in \mathbb{Z}$. The one-element list $(x)$ is a cycle of $R$ if and only if $R$ has a loop
$x \to x$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Section 2 (cycles of length 1).

Formalized by `MetaMathlibExt.isDigraphCycle_singleton`, a theorem declared in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#is-digraph-cycle-singleton).

## Two-vertex cycles of a digraph on the integers

Let $R$ be a digraph on $\mathbb{Z}$ and let
$x, y \in \mathbb{Z}$. The list $(x, y)$ is a cycle of $R$ if and only if $x \ne y$ and $R$ has both
edges $x \to y$ and $y \to x$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Section 2 (2-cycles).

Formalized by `MetaMathlibExt.isDigraphCycle_pair`, a theorem declared in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#is-digraph-cycle-pair).

## Translation isomorphism of exact covering system digraphs

Let $r \in \mathbb{N}$, let
$d_1, \dots, d_r$, $a_1, \dots, a_r$ and $k$ be integers, and put $a_i' = a_i - (d_i - 1)k$.
Then the map $x \mapsto x + k$ is a digraph isomorphism from
$G(d_1 n + a_1, \dots, d_r n + a_r)$ onto $G(d_1 n + a_1', \dots, d_r n + a_r')$.

The paper's exact-covering hypothesis on the rules is not needed.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Theorem 1.

Stated but not proved: `MetaMathlibExt.ecsdAdj_shift_relIso` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-adj-shift-rel-iso).

## Reflection isomorphism of exact covering system digraphs

Let $r \in \mathbb{N}$, let
$d_1, \dots, d_r$, $a_1, \dots, a_r$ and $k$ be integers, and put $a_i' = -a_i + (d_i - 1)k$.
Then the map $x \mapsto -(x + k)$ is a digraph isomorphism from
$G(d_1 n + a_1, \dots, d_r n + a_r)$ onto $G(d_1 n + a_1', \dots, d_r n + a_r')$.

The paper's exact-covering hypothesis on the rules is not needed.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Theorem 2.

Stated but not proved: `MetaMathlibExt.ecsdAdj_neg_shift_relIso` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-adj-neg-shift-rel-iso).

## Normal form of the ECSDs $G(2n + a_1, 2n + a_2)$

For all integers $a_1, a_2$ with
$a_1 - a_2$ odd, the exact covering system digraph $G(2n + a_1, 2n + a_2)$, with an edge
$m \to 2m + a_1$ and an edge $m \to 2m + a_2$ for every integer $m$, is isomorphic as a digraph
to $G(2n, 2n - a)$ for some odd natural number $a$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Theorem 3.

Stated but not proved: `MetaMathlibExt.ecsd_type_one_relIso` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-type-one-rel-iso).

## Normal form of Type 2 exact covering system digraphs

Let $a_1, a_2 \in \mathbb{Z}$ with
$a_1 - a_2$ odd, and write $G(2n + a_1, -2n + a_2)$ for the exact covering system digraph on
$\mathbb{Z}$ with an edge $m \to n$ exactly when $n = 2m + a_1$ or $n = -2m + a_2$. Then there is
an odd natural number $a$ such that $G(2n + a_1, -2n + a_2)$ is isomorphic as a digraph to
$G(2n, -2n + a)$, the digraph on $\mathbb{Z}$ with an edge $m \to n$ exactly when $n = 2m$ or
$n = -2m + a$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Theorem 4.

Stated but not proved: `MetaMathlibExt.ecsd_type_two_relIso` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-type-two-rel-iso).

## Normal forms of the ECSDs $G(-2n + a_1, -2n + a_2)$

For all integers $a_1, a_2$ with
$a_1 - a_2$ odd, the exact covering system digraph $G(-2n + a_1, -2n + a_2)$, with an edge
$m \to -2m + a_1$ and an edge $m \to -2m + a_2$ for every integer $m$, is isomorphic as a
digraph to one of the following: $G(-2n, -2n + a)$ for an odd natural number $a$ (Type 3.1);
$G(-2n + 1, -2n + a)$ for an even natural number $a$ with $a \equiv 1 \pmod 3$ (Type 3.2); or
$G(-2n + 1, -2n + a)$ for an even integer $a$ with $a \equiv 2 \pmod 3$ (Type 3.3).

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Theorem 5.

Stated but not proved: `MetaMathlibExt.ecsd_type_three_relIso` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-type-three-rel-iso).

## Cycles of the digraph $G(2n, 2n - a)$

For an integer $b$ write $G_b$ for the digraph
$G(2n, 2n - b)$ on $\mathbb{Z}$, with an edge $m \to 2m$ and an edge $m \to 2m - b$ for every
integer $m$. Let $a$ be an odd natural number, write $x \bmod a$ for the residue of $x$ in
$\{0, \dots, a - 1\}$, and write $\operatorname{ord}(2, q)$ for the multiplicative order of $2$
modulo $q$. Then (i) $G_a$ has a loop at $m$ if and only if $m = 0$ or $m = a$; (ii) $G_a$ has a
directed walk of positive length from $m$ back to $m$ if and only if $0 \le m \le a$; (iii) the
list $(2^k \bmod a)_{0 \le k < \operatorname{ord}(2, a)}$ is a cycle of $G_a$; for every integer
$b$ with $1 \le b < a$ the list $(b 2^k \bmod a)_{0 \le k < \operatorname{ord}(2, a/\gcd(a, b))}$
is a cycle of $G_a$; and every cycle of $G_a$ with more than one vertex is a rotation of one of
these lists for some integer $b$ with $1 \le b < a$; (iv) for all natural numbers $t$ and $a'$
with $a = t a'$, a list $(c_1, \dots, c_s)$ of integers is a cycle of $G_{a'}$ if and only if
$(t c_1, \dots, t c_s)$ is a cycle of $G_a$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Theorem 6.

Stated but not proved: `MetaMathlibExt.ecsd_two_two_sub_cycles` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-two-two-sub-cycles).

## Descendants in the digraph $G(2n, -2n + a)$

Let $a$ and $m$ be integers and let
$k \ge 1$. In the digraph $G(2n, -2n + a)$ on $\mathbb{Z}$, with an edge $x \to 2x$ and an edge
$x \to -2x + a$ for every integer $x$, the $k$-descendants of $m$ (the ends of directed walks of
exactly $k$ edges from $m$) are exactly the integers $2^k m$, the integers $2^k m - ba$ and
$-(2^k m - ba)$ for natural numbers $b$ with $1 \le b < 2^{k-1}$, and $-(2^k m - 2^{k-1} a)$.

This holds for every integer $a$, not only for odd $a$, for which $G(2n, -2n + a)$ is an exact
covering system digraph.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Proposition 1.

Stated but not proved: `MetaMathlibExt.ecsd_two_neg_two_descendants` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-two-neg-two-descendants).

## Cycles of the digraph $G(2n, -2n + a)$

For an integer $b$ write $G_b$ for the digraph
$G(2n, -2n + b)$ on $\mathbb{Z}$, with an edge $m \to 2m$ and an edge $m \to -2m + b$ for every
integer $m$. Let $a$ be an odd natural number. Then (i) $G_a$ has a loop at $m$ if and only if
$m = 0$ or $3m = a$; (ii) $G_a$ has a directed walk of positive length from $m$ back to $m$ if
and only if $0 \le m < a/2$; (iii) for all natural numbers $t$ and $a'$ with $a = t a'$, a list
$(c_1, \dots, c_s)$ of integers is a cycle of $G_{a'}$ if and only if $(t c_1, \dots, t c_s)$ is
a cycle of $G_a$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Theorem 7.

Stated but not proved: `MetaMathlibExt.ecsd_two_neg_two_cycles` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-two-neg-two-cycles).

## Descendants modulo the difference of offsets

Let $a_1, a_2, x, y$ be integers and
$k \in \mathbb{N}$. If $y$ is a $k$-descendant of $x$ in $G(-2n + a_1, -2n + a_2)$, that is,
the end of a directed walk of exactly $k$ edges from $x$, then

$$y \equiv (-2)^k x + a_1 \cdot \frac{1 - (-2)^k}{3} \pmod{|a_1 - a_2|}.$$

The quotient is an integer because $3$ divides $1 - (-2)^k$.

The exact-covering condition on $a_1, a_2$ is not needed.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Theorem 8.

Stated but not proved: `MetaMathlibExt.ecsd_neg_two_descendant_modEq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-neg-two-descendant-mod-eq).

## Cyclic vertices in every residue class

Let $a_1, a_2$ be integers with $a_1 - a_2$
odd. Then every residue class modulo $|a_1 - a_2|$ contains a vertex that lies on a directed
cycle of $G(-2n + a_1, -2n + a_2)$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Theorem 9.

Stated but not proved: `MetaMathlibExt.ecsd_neg_two_cyclic_residues` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-neg-two-cyclic-residues).

## Cycles of $G(-2n, -2n + a)$

Let $a$ be an odd natural number and $G = G(-2n, -2n + a)$.
A cycle of $G$ is a list $(c_1, \dots, c_t)$, $t \ge 1$, of distinct integers with edges
$c_1 \to c_2, \dots, c_{t-1} \to c_t$ and $c_t \to c_1$; a vertex is cyclic if it lies on a
cycle. For an integer $x$ let $\hat{x}$ be the representative of $x$ modulo $a$ in the interval
$(-a/3, 2a/3]$, and let $\operatorname{ord}_q(-2)$ be the multiplicative order of $-2$ modulo
$q$. Then:
(i) for every integer $m$, $G$ has a loop at $m$ iff $m = 0$ or $3m = a$;
(ii) an integer $m$ is cyclic iff $-a \le 3m \le 2a$;
(iii) if $3 \nmid a$, then $G$ has exactly $a$ cyclic vertices and each residue class modulo
$a$ contains exactly one of them; if $3 \mid a$, then $G$ has exactly $a + 1$ cyclic vertices,
each residue class modulo $a$ other than the class of $2a/3$ contains exactly one of them, and
the two-vertex list $(-a/3, 2a/3)$ is a cycle of $G$;
(iv) the list $(\widehat{(-2)^k})_{0 \le k < \operatorname{ord}_a(-2)}$ is a cycle of $G$, and
for every integer $b$ with $-a < 3b < 2a$, $b \ne 0$ and $3b \ne a$, so is the list
$(\widehat{b(-2)^k})_{0 \le k < \operatorname{ord}_{a/\gcd(a, b)}(-2)}$;
(v) if $a = t a'$ with $t, a' \in \mathbb{N}$, then a list $C$ of integers is a cycle of
$G(-2n, -2n + a')$ iff the list $tC$ obtained by multiplying every entry by $t$ is a cycle of
$G$.

The paper also assumes $a'$ odd in (v); this follows from $a$ odd.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Theorem 10.

Stated but not proved: `MetaMathlibExt.ecsd_neg_two_neg_two_cycles` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-neg-two-neg-two-cycles).

## Cyclic vertices of $G(-2n + 1, -2n + a)$ when $a \equiv 1 \pmod 3$

Let $a$ be an even
natural number with $a \equiv 1 \pmod 3$ and let $m$ be an integer. The digraph
$G(-2n + 1, -2n + a)$ on $\mathbb{Z}$, with an edge $x \to -2x + 1$ and an edge $x \to -2x + a$
for every integer $x$, has a directed walk of positive length from $m$ back to $m$ if and only
if $-(a - 1)/3 < m < 2a/3$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Theorem 11.

Stated but not proved: `MetaMathlibExt.ecsd_type_three_two_cyclic_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-type-three-two-cyclic-iff).

## Bounds on the cyclic vertices of $G(-2n + 1, -2n + a)$ when $a \equiv 2 \pmod 3$

Let $a$
be an even integer with $a \equiv 2 \pmod 3$, and let $m$ be an integer such that the digraph
$G(-2n + 1, -2n + a)$ on $\mathbb{Z}$, with an edge $x \to -2x + 1$ and an edge $x \to -2x + a$
for every integer $x$, has a directed walk of positive length from $m$ back to $m$. If $a \ge 2$,
then $-(a - 1)/3 < m < 2a/3$; if $a \le -2$, then $-2(|a| + 1)/3 < m < (|a| + 3)/3$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Theorem 12.

Stated but not proved: `MetaMathlibExt.ecsd_type_three_three_cyclic_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-type-three-three-cyclic-bounds).

## Cyclic vertices of $G(-2n + 1, -2n + a)$ and their residues when $a \equiv 2 \pmod 3$

Let
$a$ be an even integer with $a \equiv 2 \pmod 3$, and call an integer $m$ cyclic if the digraph
$G(-2n + 1, -2n + a)$ on $\mathbb{Z}$, with an edge $x \to -2x + 1$ and an edge $x \to -2x + a$
for every integer $x$, has a directed walk of positive length from $m$ back to $m$. Then: if
$a \ge 2$, every integer $m$ with $-(a - 1)/3 < m < 2a/3$ is cyclic; if $a \le -2$, every integer
$m$ with $-2(|a| + 1)/3 < m < (|a| + 3)/3$ is cyclic; every residue class modulo $|a - 1|$
contains a cyclic integer; and there are a least cyclic integer $\ell$ and a greatest cyclic
integer $h$ such that $\ell \equiv h \pmod{|a - 1|}$, the list $(\ell, h)$ is a cycle, and any
two distinct cyclic integers that are congruent modulo $|a - 1|$ are $\ell$ and $h$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Theorem 13.

Stated but not proved: `MetaMathlibExt.ecsd_type_three_three_cyclic` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-type-three-three-cyclic).

## Digit representations and connected digraphs

Let $d \ge 2$ be a natural number, let
$D$ be an integer with $|D| = d$, and let $a_1, \dots, a_d$ be integers such that for every
integer $n$ there is exactly one $i$ with $D \mid n - a_i$. Let
$G = G(Dn + a_1, \dots, Dn + a_d)$. Then every integer $z$ can be written as
$z = \sum_{j=0}^{k} b_j D^j$ with $k \in \mathbb{N}$ and digits
$b_0, \dots, b_k \in \{a_1, \dots, a_d\}$ if and only if the underlying undirected graph of $G$
is connected and $0$ lies on a directed cycle of $G$.

The paper also states that the representation is unique; that clause is omitted here.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Theorem 14.

Stated but not proved: `MetaMathlibExt.ecsd_digit_representation_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-digit-representation-iff).

## Connectivity of $G(-2n + 1, -2n + a)$

For an even integer $a$, the underlying undirected
graph of $G(-2n + 1, -2n + a)$ is connected iff $a = 1 + 3^m$ or $a = 1 - 3^m$ for some
integer $m \ge 0$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Theorem 15.

Stated but not proved: `MetaMathlibExt.ecsd_one_component_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-one-component-iff).

## Shortest walks to $\pm(a - 1)$ in $G(-2n + 1, -2n + a)$

Let $m \ge 1$ be an integer and
$a = 1 + 3^m$ or $a = 1 - 3^m$. Then in $G(-2n + 1, -2n + a)$ the least $k \in \mathbb{N}$ such
that $a - 1$ is a $k$-descendant of $0$ (the end of a directed walk of exactly $k$ edges from
$0$) is $3^m$, and the least $k$ such that $-(a - 1)$ is a $k$-descendant of $0$ is also $3^m$.

The paper states this for every $a \notin \{0, 2\}$, which is false: for $a = 6$ the shortest
walk from $0$ to $5$ has $4$ edges. Its proof uses that the cycle through $0$ has $|a - 1|$
edges, which holds when the digraph has a single component.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Theorem 16.

Stated but not proved: `MetaMathlibExt.ecsd_path_length_to_a_sub_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-path-length-to-a-sub-one).

## Degree-2 ECSDs with one component and $0$ on a cycle

Let $d_1, d_2 \in \{2, -2\}$ and let
$a_1, a_2$ be integers with $a_1 - a_2$ odd, excluding the case $d_1 = d_2 = -2$ with
$|a_1 - a_2| = 1$. Consider the exact covering system digraph $G(d_1 n + a_1, d_2 n + a_2)$, with
an edge $m \to d_i m + a_i$ for every integer $m$ and $i = 1, 2$. It has a single component (any
two integers are joined by a path in its underlying undirected graph) and a directed walk of
positive length from $0$ back to $0$ if and only if one of the following holds: $d_1 = 2$,
$d_2 = -2$, $a_1 = 0$ and $a_2 = \pm 1$; or $d_1 = -2$, $d_2 = 2$, $a_2 = 0$ and $a_1 = \pm 1$;
or $d_1 = d_2 = -2$, $|a_1 - a_2| = 3^m$ for some integer $m \ge 0$, neither $a_1$ nor $a_2$ is
divisible by $3$, and $\max(|a_1|, |a_2|) \le 2|a_1 - a_2| - 1$.

The excluded case behaves differently: $G(-2n + 1, -2n + 2)$ has a single component and the
cycle $(0, 1)$, although $\max(1, 2) = 2 > 2 \cdot 1 - 1$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Theorem 17.

Stated but not proved: `MetaMathlibExt.ecsd_single_component_zero_cyclic_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-single-component-zero-cyclic-iff).

## Negabinary representations with digits $1$ and $a$

Let $a \in \mathbb{Z}$. Every integer
$z$ can be written as $z = \sum_{j=0}^{k} b_j (-2)^j$ for some $k \in \mathbb{N}$ and digits
$b_0, \dots, b_k \in \{1, a\}$ if and only if $a = 1 + 3^m$ or $a = 1 - 3^m$ for some integer
$m \ge 0$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Corollary 1.

Stated but not proved: `MetaMathlibExt.negabinary_digits_one_a_complete_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#negabinary-digits-one-a-complete-iff).

## Negabinary representations with two digits

Let $a_1, a_2 \in \mathbb{Z}$ with
$|a_1 - a_2| \ne 1$. Every integer $z$ can be written as $z = \sum_{j=0}^{k} b_j (-2)^j$ for some
$k \in \mathbb{N}$ and digits $b_0, \dots, b_k \in \{a_1, a_2\}$ if and only if
$|a_1 - a_2| = 3^m$ for some integer $m \ge 0$, neither $a_1$ nor $a_2$ is divisible by $3$, and
$\max\{|a_1|, |a_2|\} \le 2|a_1 - a_2| - 1$.

The hypothesis $|a_1 - a_2| \ne 1$ restricts the printed statement, which fails when
$|a_1 - a_2| = 1$: the digits $\{1, 2\}$ represent every integer, yet $\max\{1, 2\} = 2 > 1$.
The paper's alternative $\{a_1, a_2\} = \{0, \pm 1\}$ lies in the excluded case and is dropped.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Corollary 2.

Stated but not proved: `MetaMathlibExt.negabinary_two_digits_complete_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#negabinary-two-digits-complete-iff).

## Divisibility of $2^{3n} + 1$ from $2^n + 1$

For every natural number $n$, if $3n$
divides $2^n + 1$, then $9n$ divides $2^{3n} + 1$.

Equivalently, if $3$ divides $2^n + 1$ and $n$ divides $(2^n + 1)/3$, then $3n$ divides
$(2^{3n} + 1)/3$. For $n = 0$ the hypothesis fails, so positivity is not assumed.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Lemma 1.

Stated but not proved: `MetaMathlibExt.three_mul_dvd_two_pow_add_one_cube` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 430](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L430). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#three-mul-dvd-two-pow-add-one-cube).

## Divisibility of $1 - (-2)^{3k}$ from $1 - (-2)^k$

For every integer $n$ and every
natural number $k$, if $3n$ divides $1 - (-2)^k$, then $9n$ divides $1 - (-2)^{3k}$.

Since $3$ always divides $1 - (-2)^k$, this is equivalent to: if $n$ divides
$(1 - (-2)^k)/3$, then $3n$ divides $(1 - (-2)^{3k})/3$. The paper states it for positive $n$
and $k$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Lemma 2.

Stated but not proved: `MetaMathlibExt.three_mul_dvd_one_sub_neg_two_pow_cube` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#three-mul-dvd-one-sub-neg-two-pow-cube).

## Bounding the power of $3$ dividing $2^{3k} + 1$

For all natural numbers $m$ and $k$, if
$3^{m+1}$ does not divide $2^k + 1$, then $3^{m+2}$ does not divide $2^{3k} + 1$.

For odd $k$, where $3$ divides $2^k + 1$, this says: if $3^m$ does not divide $(2^k + 1)/3$,
then $3^{m+1}$ does not divide $(2^{3k} + 1)/3$. For even $k$ the conclusion holds since $3$
does not divide $2^{3k} + 1$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Lemma 3.

Stated but not proved: `MetaMathlibExt.three_pow_not_dvd_two_pow_add_one_cube` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 450](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L450). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#three-pow-not-dvd-two-pow-add-one-cube).

## Nine divides $n$ when $n > 3$ and $3n$ divides $2^n + 1$

Let $n > 3$ be a natural
number. If $3n$ divides $2^n + 1$, then $9$ divides $n$.

For odd $n$ the hypothesis says that $n$ divides the integer $(2^n + 1)/3$, which is the form
in the paper; for even $n$ it never holds, since $3$ does not divide $2^n + 1$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Lemma 4, quoting [3].

Stated but not proved: `MetaMathlibExt.nine_dvd_of_three_mul_dvd_two_pow_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#nine-dvd-of-three-mul-dvd-two-pow-add-on).

## Single-component degree-2 ECSDs up to isomorphism

Let $d_1, d_2 \in \{2, -2\}$ and let
$a_1, a_2$ be integers with $a_1 - a_2$ odd. If the exact covering system digraph
$G(d_1 n + a_1, d_2 n + a_2)$, with an edge $m \to d_i m + a_i$ for every integer $m$ and
$i = 1, 2$, has a single component, that is, any two integers are joined by a path in its
underlying undirected graph, then it is isomorphic as a digraph to $G(2n, -2n + 1)$ or to
$G(-2n + 1, -2n + a)$ for some integer $a$ with $a = 0$, $a = 2$ or $a \equiv 1 \pmod 3$.

## Sources

- Dana Neidmann, *Exact Covering System Digraphs of Degree 2 and Non-Standard Binary Representations of Integers*, INTEGERS 26 (2026), Article A107, Proposition 2.

Stated but not proved: `MetaMathlibExt.ecsd_single_component_relIso` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean, line 468](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/ExactCoveringSystemDigraphWanted.lean#L468). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html#ecsd-single-component-rel-iso).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Exact covering system digraphs](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/congruences/covering-systems/exact-covering-system-digraphs)
