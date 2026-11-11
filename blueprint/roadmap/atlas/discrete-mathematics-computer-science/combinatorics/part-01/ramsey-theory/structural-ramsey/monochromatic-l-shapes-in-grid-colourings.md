---
declaration: section
origin: cited
lean: MetaMathlibExt.GridLRamseyProperty, MetaMathlibExt.GridLRamseyProperty.mono, MetaMathlibExt.not_gridLRamseyProperty_one_one, MetaMathlibExt.gridLRamseyProperty_one_two, MetaMathlibExt.exists_gridLRamseyProperty, MetaMathlibExt.gridLRamseyProperty_three_2593, MetaMathlibExt.gridLRamseyProperty_three_1804, MetaMathlibExt.gridLRamseyProperty_three_1573
statement: formalized
---

# Monochromatic L-shapes in grid colourings

11 results, 4 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/monochromatic-l-shapes-in-grid-colourings/index.html).

## Grid Ramsey property for Ls

Let $k$ and $n$ be natural numbers and write
$[n] = \{1, \dots, n\}$. An L in the grid $[n] \times [n]$ is a triple of points $(x, y)$,
$(x + d, y)$, $(x + d, y + d)$ with $x$, $y$, $d$ positive integers, $x + d \le n$ and
$y + d \le n$. The pair $(k, n)$ has the grid Ramsey property for Ls when every coloring of
$\mathbb{N} \times \mathbb{N}$ with $k$ colors gives the three points of some L in
$[n] \times [n]$ the same color, that is, contains a monochromatic L. Only the colors on
$[n] \times [n]$ matter.

The grid Ramsey number $R_k(L)$ is the least $n$ with this property. The property is monotone
in $n$, so $R_k(L) \le N$ says exactly that $(k, N)$ has it.

## Sources

- Isaac Mammel, William Smith, and Carl Yerger, *Ramsey Theory on the Integer Grid: The "L" Problem*, INTEGERS 25 (2025), Article A21, Theorem 1 and the definition of `R_k(L)` following it.

Formalized by `MetaMathlibExt.GridLRamseyProperty`, a definition declared in [WantedExt/Combinatorics/GridLRamseyWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GridLRamseyWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/monochromatic-l-shapes-in-grid-colourings/index.html#grid-lramsey-property).

## Monotonicity of the grid Ramsey property for Ls

Let $k$, $m$, $n$ be natural numbers
with $m \le n$. For a natural number $N$ write $[N] = \{1, \dots, N\}$; given a coloring, a
monochromatic L in $[N] \times [N]$ is a triple of points $(x, y)$, $(x + d, y)$, $(x + d, y + d)$
of the same color with $x$, $y$, $d$ positive integers, $x + d \le N$ and $y + d \le N$. If every
coloring of $\mathbb{N} \times \mathbb{N}$ with $k$ colors has a monochromatic L in
$[m] \times [m]$, then every such coloring has a monochromatic L in $[n] \times [n]$, because a
larger grid contains every L of a smaller one.

## Sources

- Isaac Mammel, William Smith, and Carl Yerger, *Ramsey Theory on the Integer Grid: The "L" Problem*, INTEGERS 25 (2025), Article A21 (definition of `R_k(L)`).

Formalized by `MetaMathlibExt.GridLRamseyProperty.mono`, a theorem declared in [WantedExt/Combinatorics/GridLRamseyWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GridLRamseyWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/monochromatic-l-shapes-in-grid-colourings/index.html#mono).

## One color does not force an L on the $1 \times 1$ grid

The grid L-Ramsey property
fails for $k = 1$ color and grid size $n = 1$: not every coloring of the grid
$\{1\} \times \{1\}$ with one color contains a monochromatic L, that is, three points
$(x, y), (x + d, y), (x + d, y + d)$ of the grid of the same color, with $x, y, d$ positive
integers. In fact this grid contains no L at all, since that needs $x + d \le 1$ with
$x, d \ge 1$.

## Sources

- Isaac Mammel, William Smith, and Carl Yerger, *Ramsey Theory on the Integer Grid: The "L" Problem*, INTEGERS 25 (2025), Article A21 (definition of an L).

Formalized by `MetaMathlibExt.not_gridLRamseyProperty_one_one`, a theorem declared in [WantedExt/Combinatorics/GridLRamseyWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GridLRamseyWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/monochromatic-l-shapes-in-grid-colourings/index.html#not-grid-lramsey-property-one-one).

## With one color the 2 × 2 grid contains an L

Write $[n] = \{1, \dots, n\}$. An L in the
grid $[n] \times [n]$ is a triple of points $(x, y)$, $(x + d, y)$, $(x + d, y + d)$ with $x$, $y$,
$d$ positive integers, $x + d \le n$ and $y + d \le n$. Every coloring of
$\mathbb{N} \times \mathbb{N}$ with a single color gives the three points of some L in
$[2] \times [2]$ the same color, namely the L $(1, 1)$, $(2, 1)$, $(2, 2)$.

Since $[1] \times [1]$ contains no L at all, the grid Ramsey number for one color, the least $n$
such that every coloring with one color has a monochromatic L in $[n] \times [n]$, is
$R_1(L) = 2$.

## Sources

- Isaac Mammel, William Smith, and Carl Yerger, *Ramsey Theory on the Integer Grid: The "L" Problem*, INTEGERS 25 (2025), Article A21 (definition of `R_k(L)`).

Formalized by `MetaMathlibExt.gridLRamseyProperty_one_two`, a theorem declared in [WantedExt/Combinatorics/GridLRamseyWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GridLRamseyWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/monochromatic-l-shapes-in-grid-colourings/index.html#grid-lramsey-property-one-two).

## Grid Ramsey theorem for Ls

Write $[n] = \{1, \dots, n\}$. For every positive integer
$k$ there is a positive integer $n$ such that every coloring of the grid $[n] \times [n]$ with
$k$ colors contains a monochromatic L: positive integers $x$, $y$, $d$ with $x + d \le n$ and
$y + d \le n$ such that the points $(x, y)$, $(x + d, y)$ and $(x + d, y + d)$ all have the
same color.

## Sources

- Isaac Mammel, William Smith, and Carl Yerger, *Ramsey Theory on the Integer Grid: The "L" Problem*, INTEGERS 25 (2025), Article A21, Theorem 1 (quoted there from earlier work).

Stated but not proved: `MetaMathlibExt.exists_gridLRamseyProperty` is written with `theorem_wanted` in [WantedExt/Combinatorics/GridLRamseyWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GridLRamseyWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/monochromatic-l-shapes-in-grid-colourings/index.html#exists-grid-lramsey-property).

## Three-coloring the 2593 × 2593 grid forces a monochromatic L

Write
$[n] = \{1, \dots, n\}$. Every coloring of the grid $[2593] \times [2593]$ with $3$ colors contains
a monochromatic L: positive integers $x$, $y$, $d$ with $x + d \le 2593$ and $y + d \le 2593$ such
that the points $(x, y)$, $(x + d, y)$ and $(x + d, y + d)$ have the same color. Equivalently,
the grid Ramsey number $R_3(L)$, the least $n$ for which every coloring of $[n] \times [n]$ with
$3$ colors contains a monochromatic L, is at most $2593$.

## Sources

- Isaac Mammel, William Smith, and Carl Yerger, *Ramsey Theory on the Integer Grid: The "L" Problem*, INTEGERS 25 (2025), Article A21, Theorem 2 (quoted there from earlier work).

Stated but not proved: `MetaMathlibExt.gridLRamseyProperty_three_2593` is written with `theorem_wanted` in [WantedExt/Combinatorics/GridLRamseyWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GridLRamseyWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/monochromatic-l-shapes-in-grid-colourings/index.html#grid-lramsey-property-three-2593).

## Three-coloring the 1804 × 1804 grid forces a monochromatic L

Write
$[n] = \{1, \dots, n\}$. Every coloring of the grid $[1804] \times [1804]$ with $3$ colors contains
a monochromatic L: positive integers $x$, $y$, $d$ with $x + d \le 1804$ and $y + d \le 1804$ such
that the points $(x, y)$, $(x + d, y)$ and $(x + d, y + d)$ have the same color. Equivalently,
the grid Ramsey number $R_3(L)$, the least $n$ for which every coloring of $[n] \times [n]$ with
$3$ colors contains a monochromatic L, is at most $1804$.

## Sources

- Isaac Mammel, William Smith, and Carl Yerger, *Ramsey Theory on the Integer Grid: The "L" Problem*, INTEGERS 25 (2025), Article A21, Theorem 3.

Stated but not proved: `MetaMathlibExt.gridLRamseyProperty_three_1804` is written with `theorem_wanted` in [WantedExt/Combinatorics/GridLRamseyWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GridLRamseyWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/monochromatic-l-shapes-in-grid-colourings/index.html#grid-lramsey-property-three-1804).

## Three-coloring the 1573 × 1573 grid forces a monochromatic L

Write
$[n] = \{1, \dots, n\}$. Every coloring of the grid $[1573] \times [1573]$ with $3$ colors contains
a monochromatic L: positive integers $x$, $y$, $d$ with $x + d \le 1573$ and $y + d \le 1573$ such
that the points $(x, y)$, $(x + d, y)$ and $(x + d, y + d)$ have the same color. Equivalently,
the grid Ramsey number $R_3(L)$, the least $n$ for which every coloring of $[n] \times [n]$ with
$3$ colors contains a monochromatic L, is at most $1573$.

## Sources

- Isaac Mammel, William Smith, and Carl Yerger, *Ramsey Theory on the Integer Grid: The "L" Problem*, INTEGERS 25 (2025), Article A21, Theorem 4.

Stated but not proved: `MetaMathlibExt.gridLRamseyProperty_three_1573` is written with `theorem_wanted` in [WantedExt/Combinatorics/GridLRamseyWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GridLRamseyWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/monochromatic-l-shapes-in-grid-colourings/index.html#grid-lramsey-property-three-1573).

## Three-coloring the 772 × 772 grid forces a monochromatic L

Write
$[n] = \{1, \dots, n\}$. Every coloring of the grid $[772] \times [772]$ with $3$ colors contains
a monochromatic L: positive integers $x$, $y$, $d$ with $x + d \le 772$ and $y + d \le 772$ such
that the points $(x, y)$, $(x + d, y)$ and $(x + d, y + d)$ have the same color. Equivalently,
the grid Ramsey number $R_3(L)$, the least $n$ for which every coloring of $[n] \times [n]$ with
$3$ colors contains a monochromatic L, is at most $772$.

## Sources

- Isaac Mammel, William Smith, and Carl Yerger, *Ramsey Theory on the Integer Grid: The "L" Problem*, INTEGERS 25 (2025), Article A21, Theorem 5.

Stated but not proved: `MetaMathlibExt.gridLRamseyProperty_three_772` is written with `theorem_wanted` in [WantedExt/Combinatorics/GridLRamseyWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GridLRamseyWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/monochromatic-l-shapes-in-grid-colourings/index.html#grid-lramsey-property-three-772).

## Three-coloring the 493 × 493 grid forces a monochromatic L

Write
$[n] = \{1, \dots, n\}$. Every coloring of the grid $[493] \times [493]$ with $3$ colors contains
a monochromatic L: positive integers $x$, $y$, $d$ with $x + d \le 493$ and $y + d \le 493$ such
that the points $(x, y)$, $(x + d, y)$ and $(x + d, y + d)$ have the same color. Equivalently,
the grid Ramsey number $R_3(L)$, the least $n$ for which every coloring of $[n] \times [n]$ with
$3$ colors contains a monochromatic L, is at most $493$.

This is the paper's main bound. Since a larger grid contains every L of a smaller one, it implies
the bounds $772$, $1573$, $1804$ and $2593$.

## Sources

- Isaac Mammel, William Smith, and Carl Yerger, *Ramsey Theory on the Integer Grid: The "L" Problem*, INTEGERS 25 (2025), Article A21, Theorem 6.

Stated but not proved: `MetaMathlibExt.gridLRamseyProperty_three_493` is written with `theorem_wanted` in [WantedExt/Combinatorics/GridLRamseyWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GridLRamseyWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/monochromatic-l-shapes-in-grid-colourings/index.html#grid-lramsey-property-three-493).

## Forced blue points on a diagonal give a monochromatic L

Let $n \ge 3$, write
$[n] = \{1, \dots, n\}$, let $c$ be a coloring of $\mathbb{N} \times \mathbb{N}$ with $3$ colors
and let red and blue be two distinct colors. Let $s \ge 1$ and let $X$ be a finite set of
natural numbers such that every $x \in X$ satisfies $x \ge 1$ and $x + s \le n$, the point
$(x + s, x)$ is blue, and the points $(x, x)$ and $(x + s, x + s)$ are red (so red at
$(x + s, x)$ would complete the red L $(x, x)$, $(x + s, x)$, $(x + s, x + s)$). If
$\binom{|X|}{2} > n - 2$, then $c$ has a monochromatic L in $[n] \times [n]$: positive integers
$x$, $y$, $d$ with $x + d \le n$ and $y + d \le n$ such that the points $(x, y)$, $(x + d, y)$
and $(x + d, y + d)$ all have the same color.

The paper states the threshold as $|X| \ge \lceil \sqrt{2n - 15/4} + 1/2 \rceil$, meant as the
least $b$ with $\binom{b}{2} > n - 2$. This closed form is one too small when
$\sqrt{2n - 15/4} + 1/2$ is an integer, and the lemma then fails: for $n = 3$, color the
diagonal red, $(2, 1)$, $(3, 2)$, $(2, 3)$ blue, $(3, 1)$ green and $(1, 2)$, $(1, 3)$ red; with
$s = 1$ there are two forced blue points and no monochromatic L.

## Sources

- Isaac Mammel, William Smith, and Carl Yerger, *Ramsey Theory on the Integer Grid: The "L" Problem*, INTEGERS 25 (2025), Article A21, Lemma 1.

Stated but not proved: `MetaMathlibExt.exists_mono_L_of_forced_blue_diagonal` is written with `theorem_wanted` in [WantedExt/Combinatorics/GridLRamseyWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GridLRamseyWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/monochromatic-l-shapes-in-grid-colourings/index.html#exists-mono-l-of-forced-blue-diagonal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monochromatic L-shapes in grid colourings](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/monochromatic-l-shapes-in-grid-colourings/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/ramsey-theory/structural-ramsey/monochromatic-l-shapes-in-grid-colourings)
