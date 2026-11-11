---
declaration: section
origin: cited
lean: MetaMathlibExt.motzkinDiscriminant, MetaMathlibExt.IsMotzkinSquareRoot, MetaMathlibExt.motzkinSquareRoot, MetaMathlibExt.motzkinH, MetaMathlibExt.motzkinG, MetaMathlibExt.IsMotzkinRiordanPair, MetaMathlibExt.MotzkinRiordanPair, MetaMathlibExt.MotzkinRiordanPair.entry
statement: formalized
proof: formalized
---

# Motzkin triangle

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-triangle/index.html).

## Motzkin discriminant and Riordan pairs

## Motzkin discriminant

The Motzkin discriminant is the formal power series
$1 - 2X - 3X^2 \in \mathbb{Q}[[X]]$, the discriminant in the generating functions for the Motzkin
triangle.

Formalized by `MetaMathlibExt.motzkinDiscriminant`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-triangle/index.html#motzkin-discriminant).

## Square roots of the Motzkin discriminant

A formal power series $s \in \mathbb{Q}[[X]]$ is
a Motzkin square root when $s^2 = 1 - 2X - 3X^2$ and the constant coefficient of $s$ is $1$.

Formalized by `MetaMathlibExt.IsMotzkinSquareRoot`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-triangle/index.html#is-motzkin-square-root).

## Canonical square root of the Motzkin discriminant

The canonical square root is the power
series $s = \sum_{n \ge 0} \binom{1/2}{n} (-2X - 3X^2)^n \in \mathbb{Q}[[X]]$, obtained by
substituting $-2X - 3X^2$ for $Y$ in the binomial series
$(1 + Y)^{1/2} = \sum_{n \ge 0} \binom{1/2}{n} Y^n$.

It is the branch of $\sqrt{1 - 2X - 3X^2}$ with constant coefficient $1$ used by the Motzkin
generating functions.

Formalized by `MetaMathlibExt.motzkinSquareRoot`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-triangle/index.html#motzkin-square-root).

## Second component of the Motzkin Riordan pair

Let
$s = \sum_{n \ge 0} \binom{1/2}{n} (-2X - 3X^2)^n \in \mathbb{Q}[[X]]$ be the canonical square root
of $1 - 2X - 3X^2$. The power series $h \in \mathbb{Q}[[X]]$ has $n$-th coefficient
$\frac{1}{2} [X^{n+1}] (1 - X - s)$ for every $n \ge 0$. Since $1 - X - s$ has constant coefficient
$0$, this is the quotient $h = (1 - X - s)/(2X)$.

The definition uses a coefficient shift so that no division by $X$ is required.

Formalized by `MetaMathlibExt.motzkinH`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-triangle/index.html#motzkin-h).

## First component of the Motzkin Riordan pair

Let
$s = \sum_{n \ge 0} \binom{1/2}{n} (-2X - 3X^2)^n \in \mathbb{Q}[[X]]$ be the canonical square root
of $1 - 2X - 3X^2$, which has constant coefficient $1$. The power series $g \in \mathbb{Q}[[X]]$ is
the multiplicative inverse $g = s^{-1}$ of $s$, that is, $g = 1/\sqrt{1 - 2X - 3X^2}$.

Formalized by `MetaMathlibExt.motzkinG`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-triangle/index.html#motzkin-g).

## Motzkin Riordan pairs

Formal power series $g, h \in \mathbb{Q}[[X]]$ form a Motzkin Riordan
pair when there is a power series $s \in \mathbb{Q}[[X]]$ with $s^2 = 1 - 2X - 3X^2$ and constant
coefficient $1$ such that $g s = 1$ and $2 X h = 1 - X - s$.

Writing the second identity without division by $X$ keeps the characterization internal to formal
power series. The constant-coefficient condition selects the intended square-root branch.

Formalized by `MetaMathlibExt.IsMotzkinRiordanPair`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-triangle/index.html#is-motzkin-riordan-pair).

## Bundled Motzkin Riordan pairs

A bundled Motzkin Riordan pair consists of formal power
series $g, h \in \mathbb{Q}[[X]]$ together with a proof that they form a Motzkin Riordan pair: there
is $s \in \mathbb{Q}[[X]]$ with $s^2 = 1 - 2X - 3X^2$ and constant coefficient $1$ such that
$g s = 1$ and $2 X h = 1 - X - s$.

Formalized by `MetaMathlibExt.MotzkinRiordanPair`, a structure declared in [MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-triangle/index.html#motzkin-riordan-pair).

## Entries of a Motzkin Riordan array

For a Motzkin Riordan pair $(g, h)$ and natural numbers
$n$ and $k$, the $(n, k)$ entry is the rational number $[X^n]\, g h^k$, the coefficient of $X^n$ in
the power series $g h^k \in \mathbb{Q}[[X]]$.

Formalized by `MetaMathlibExt.MotzkinRiordanPair.entry`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-triangle/index.html#entry).

## The canonical Motzkin Riordan pair

Let $s \in \mathbb{Q}[[X]]$ be the canonical square
root of $1 - 2X - 3X^2$, given by the binomial series, which has constant coefficient $1$. The
canonical Motzkin Riordan pair is $(g, h)$ with $g = s^{-1}$ and $h = (1 - X - s)/(2X)$, the
Motzkin Riordan pair conditions being witnessed by $s$.

Formalized by `MetaMathlibExt.motzkinRiordanPair`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-triangle/index.html#motzkin-riordan-pair-2).

## Motzkin triangle

Let $s$ be the square root of $1 - 2X - 3X^2$ in the ring of formal
power series over $\mathbb{Q}$ with constant coefficient $1$, and let $g = 1/s$ and
$h = (1 - X - s)/(2X)$. For natural numbers $n$ and $k$, the $(n, k)$ entry of the Motzkin
triangle (OEIS A094531) is the rational number given by the coefficient of $X^n$ in $g h^k$.

Formalized by `MetaMathlibExt.motzkinTriangle`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-triangle/index.html#motzkin-triangle).

## Initial rows of the Motzkin triangle

Writing $T(n, k)$ for the $(n, k)$ entry of the
canonical Motzkin triangle, the rows $n = 0, 1, 2, 3$ (with $0 \le k \le n$) are
$T(0, 0) = 1$; $T(1, 0) = T(1, 1) = 1$; $T(2, 0) = 3$, $T(2, 1) = 2$, $T(2, 2) = 1$; and
$T(3, 0) = 7$, $T(3, 1) = 6$, $T(3, 2) = 3$, $T(3, 3) = 1$, matching OEIS A094531.

Formalized by `MetaMathlibExt.motzkinTriangle_initial_rows`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinTriangle.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-triangle/index.html#motzkin-triangle-initial-rows).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Motzkin triangle](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-triangle/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-triangle)
