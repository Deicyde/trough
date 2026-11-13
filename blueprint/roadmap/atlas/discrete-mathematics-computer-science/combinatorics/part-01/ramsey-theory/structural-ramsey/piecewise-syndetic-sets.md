---
declaration: section
origin: cited
lean: MetaMathlibExt.latticeCube, MetaMathlibExt.mem_latticeCube, MetaMathlibExt.latticeCube_one, MetaMathlibExt.IsDenseInCubes, MetaMathlibExt.isDenseInCubes_one_iff, MetaMathlibExt.IsPiecewiseSyndetic, MetaMathlibExt.isPiecewiseSyndetic_univ, MetaMathlibExt.not_isPiecewiseSyndetic_empty
statement: formalized
---

# Piecewise syndetic sets

16 results, 12 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/piecewise-syndetic-sets/index.html).

## Lattice cube

For $t, m \in \mathbb{N}$ and $a \in \mathbb{N}^t$, the lattice cube
with least corner $a$ and side $m$ is the set of points $x \in \mathbb{N}^t$ such that
$a_i \le x_i < a_i + m$ for every coordinate $i$; it is a subcube of size $m^t$.

## Sources

- Tom C. Brown, *Piecewise Syndetic Sets in `N^t` and `N^X`*, INTEGERS 24 (2024), Article A2, Lemma 1 (subcubes of `N^t` of size `m^t`).

Formalized by `MetaMathlibExt.latticeCube`, a definition declared in [WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/piecewise-syndetic-sets/index.html#lattice-cube).

## Membership in a lattice cube

For $t, m \in \mathbb{N}$ and $a, x \in \mathbb{N}^t$,
the point $x$ lies in the lattice cube with least corner $a$ and side $m$ if and only if
$a_i \le x_i < a_i + m$ for every coordinate $i$.

## Sources

- Tom C. Brown, *Piecewise Syndetic Sets in `N^t` and `N^X`*, INTEGERS 24 (2024), Article A2, Lemma 1 (subcubes of `N^t` of size `m^t`).

Formalized by `MetaMathlibExt.mem_latticeCube`, a theorem declared in [WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/piecewise-syndetic-sets/index.html#mem-lattice-cube).

## Lattice cube of side one

For $t \in \mathbb{N}$ and $a \in \mathbb{N}^t$, the lattice
cube with least corner $a$ and side $1$ is the singleton $\{a\}$.

## Sources

- Tom C. Brown, *Piecewise Syndetic Sets in `N^t` and `N^X`*, INTEGERS 24 (2024), Article A2, Lemma 1 (subcubes of `N^t` of size `m^t`).

Formalized by `MetaMathlibExt.latticeCube_one`, a theorem declared in [WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/piecewise-syndetic-sets/index.html#lattice-cube-one).

## Density in subcubes

Let $d \in \mathbb{N}$ and let $C, M \subseteq \mathbb{N}^t$. The set
$C$ is $d$-dense in $M$ when every subcube of $\mathbb{N}^t$ of side $d$ that is contained in $M$
meets $C$.

## Sources

- Tom C. Brown, *Piecewise Syndetic Sets in `N^t` and `N^X`*, INTEGERS 24 (2024), Article A2, Lemma 1 (definition of `m_{i-1}`-dense in `M'`).

Formalized by `MetaMathlibExt.IsDenseInCubes`, a definition declared in [WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/piecewise-syndetic-sets/index.html#is-dense-in-cubes).

## Density one means containment

For sets $C, M \subseteq \mathbb{N}^t$, the set $C$ is
$1$-dense in $M$ if and only if $M \subseteq C$.

## Sources

- Tom C. Brown, *Piecewise Syndetic Sets in `N^t` and `N^X`*, INTEGERS 24 (2024), Article A2, Lemma 1 (definition of `m_{i-1}`-dense in `M'`, with `m_0 = 1`).

Formalized by `MetaMathlibExt.isDenseInCubes_one_iff`, a theorem declared in [WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/piecewise-syndetic-sets/index.html#is-dense-in-cubes-one-iff).

## Piecewise syndetic set

Let $t \in \mathbb{N}$. A set $A \subseteq \mathbb{N}^t$ is
piecewise syndetic if there is $d \in \mathbb{N}$ such that, writing
$[0, d] = \{0, 1, \dots, d\}$, for every $m \in \mathbb{N}$ the set
$A + [0, d]^t = \{y + z : y \in A,\ z \in [0, d]^t\}$ contains a lattice cube of side $m$.

## Sources

- Tom C. Brown, *Piecewise Syndetic Sets in `N^t` and `N^X`*, INTEGERS 24 (2024), Article A2, Proof 1 of Theorem 2 (meaning of piecewise syndetic).

Formalized by `MetaMathlibExt.IsPiecewiseSyndetic`, a definition declared in [WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/piecewise-syndetic-sets/index.html#is-piecewise-syndetic).

## The whole space is piecewise syndetic

For every $t \in \mathbb{N}$, the whole space
$\mathbb{N}^t$ is piecewise syndetic.

## Sources

- Tom C. Brown, *Piecewise Syndetic Sets in `N^t` and `N^X`*, INTEGERS 24 (2024), Article A2, Proof 1 of Theorem 2 (meaning of piecewise syndetic).

Formalized by `MetaMathlibExt.isPiecewiseSyndetic_univ`, a theorem declared in [WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/piecewise-syndetic-sets/index.html#is-piecewise-syndetic-univ).

## The empty set is not piecewise syndetic

For every $t \in \mathbb{N}$, the empty
subset of $\mathbb{N}^t$ is not piecewise syndetic.

## Sources

- Tom C. Brown, *Piecewise Syndetic Sets in `N^t` and `N^X`*, INTEGERS 24 (2024), Article A2, Proof 1 of Theorem 2 (meaning of piecewise syndetic).

Formalized by `MetaMathlibExt.not_isPiecewiseSyndetic_empty`, a theorem declared in [WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/piecewise-syndetic-sets/index.html#not-is-piecewise-syndetic-empty).

## A color class is dense in a subcube (Brown, Lemma 1)

Let $t, r \in \mathbb{N}$ and let
$1 = m_0 < m_1 < m_2 < \cdots$ be a strictly increasing sequence of natural numbers. Let $M$ be a
subcube of $\mathbb{N}^t$ of side $m_r$, and let $c$ be a coloring of $\mathbb{N}^t$ by natural
numbers with $1 \le c(x) \le r$ for every $x \in M$. Then for some color $i$ with $1 \le i \le r$
there is a subcube $M' \subseteq M$ of side $m_i$ in which the class of color $i$ is
$m_{i-1}$-dense.

The paper fixes $t \ge 1$ and $r \ge 1$; both are dropped, since $t = 0$ holds trivially and
$r = 0$ admits no coloring of the nonempty cube $M$.

## Sources

- Tom C. Brown, *Piecewise Syndetic Sets in `N^t` and `N^X`*, INTEGERS 24 (2024), Article A2, Lemma 1.

Stated but not proved: `MetaMathlibExt.exists_subcube_isDenseInCubes_colorClass` is written with `theorem_wanted` in [WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/piecewise-syndetic-sets/index.html#exists-subcube-is-dense-in-cubes-color-c).

## A color class is dense in a large subcube (Brown, Lemma 2)

Let $r, t \in \mathbb{N}$ and
let $f : \mathbb{N} \to \mathbb{N}$. There is $A \in \mathbb{N}$ such that for every coloring of
$\mathbb{N}^t$ with $r$ colors there are natural numbers $d \ge 1$ and $m > f(d)$, a color $j$, and
a subcube $M$ of side $m$ with $M \subseteq [1, A]^t$ in which the class of color $j$ is
$d$-dense. Here $[1, A]^t$ is the set of points $x$ with $1 \le x_i \le A$ for every coordinate $i$.

The paper's "(a smallest)" is omitted: it follows from existence. Only the restriction of the
coloring to $[1, A]^t$ matters.

## Sources

- Tom C. Brown, *Piecewise Syndetic Sets in `N^t` and `N^X`*, INTEGERS 24 (2024), Article A2, Lemma 2.

Stated but not proved: `MetaMathlibExt.exists_cube_bound_isDenseInCubes` is written with `theorem_wanted` in [WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/piecewise-syndetic-sets/index.html#exists-cube-bound-is-dense-in-cubes).

## Piecewise syndeticity is partition regular

Let $A \subseteq \mathbb{N}^t$ be piecewise
syndetic and let $A_1, \dots, A_r \subseteq \mathbb{N}^t$ with $A = A_1 \cup \dots \cup A_r$. Then
some $A_i$ is piecewise syndetic.

## Sources

- Tom C. Brown, *Piecewise Syndetic Sets in `N^t` and `N^X`*, INTEGERS 24 (2024), Article A2, Theorem 1.

Stated but not proved: `MetaMathlibExt.IsPiecewiseSyndetic.exists_of_eq_iUnion` is written with `theorem_wanted` in [WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/piecewise-syndetic-sets/index.html#exists-of-eq-i-union).

## Gap size

For a set $S \subseteq \mathbb{N}^t$, the gap size $\operatorname{gs}(S)$ is the
least $d \ge 1$ such that $S$ is $d$-dense in some subcube of $\mathbb{N}^t$ that contains $S$. If
no such $d$ exists (for instance when $S$ is unbounded, so that no subcube contains it), the value
is $0$.

For $t = 1$, the gap size of a finite set with at least two points is the largest difference
between consecutive elements, and a one-point set has gap size $1$ (Definition 1). The paper
defines $\operatorname{gs}$ only for finite sets; when $t \ge 1$, every finite set has positive gap
size.

## Sources

- Tom C. Brown, *Piecewise Syndetic Sets in `N^t` and `N^X`*, INTEGERS 24 (2024), Article A2, Definition 5.

Formalized by `MetaMathlibExt.cubeGapSize`, a definition declared in [WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/piecewise-syndetic-sets/index.html#cube-gap-size).

## Density bounds the gap size

Let $S \subseteq \mathbb{N}^t$, let $d \ge 1$, and let $M$ be a
subcube of $\mathbb{N}^t$ with $S \subseteq M$. If $S$ is $d$-dense in $M$, then the gap size of $S$
satisfies $\operatorname{gs}(S) \le d$.

## Sources

- Tom C. Brown, *Piecewise Syndetic Sets in `N^t` and `N^X`*, INTEGERS 24 (2024), Article A2, Definition 5 (and Proof 1 of Theorem 2, "hence `gs(S) ≤ d`").

Formalized by `MetaMathlibExt.cubeGapSize_le_of_isDenseInCubes`, a theorem declared in [WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/piecewise-syndetic-sets/index.html#cube-gap-size-le-of-is-dense-in-cubes).

## Finite sets in positive dimension have positive gap size

Let $t \ge 1$. Every finite set
$S \subseteq \mathbb{N}^t$ has gap size $\operatorname{gs}(S) > 0$.

Indeed, $S$ lies in some subcube $[0, m)^t$, and it is vacuously $(m + 1)$-dense there, since no
subcube of side $m + 1$ fits inside.

## Sources

- Tom C. Brown, *Piecewise Syndetic Sets in `N^t` and `N^X`*, INTEGERS 24 (2024), Article A2, Definition 5.

Formalized by `MetaMathlibExt.cubeGapSize_pos`, a theorem declared in [WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/piecewise-syndetic-sets/index.html#cube-gap-size-pos).

## Gap size of a singleton

For every point $x \in \mathbb{N}^t$, the one-point set
$\lbrace x \rbrace$ has gap size $\operatorname{gs}(\lbrace x \rbrace) = 1$.

## Sources

- Tom C. Brown, *Piecewise Syndetic Sets in `N^t` and `N^X`*, INTEGERS 24 (2024), Article A2, Definitions 1 and 5 ("If `|S| = 1`, we set `gs(S) = 1`").

Formalized by `MetaMathlibExt.cubeGapSize_singleton`, a theorem declared in [WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/piecewise-syndetic-sets/index.html#cube-gap-size-singleton).

## Monochromatic sets that are large relative to their gap size

Let $r, t \in \mathbb{N}$ with
$t \ge 1$, and let $f : \mathbb{N} \to \mathbb{N}$ be nondecreasing. There is $B \in \mathbb{N}$
such that for every coloring of $\mathbb{N}^t$ with $r$ colors there is a finite monochromatic set
$S \subseteq [1, B]^t$ with $|S| > f(\operatorname{gs}(S))$, where $\operatorname{gs}(S)$ is the gap
size of $S$ and $[1, B]^t$ is the set of points $x$ with $1 \le x_i \le B$ for every coordinate $i$.

The paper's "(a smallest)" is omitted: it follows from existence. Only the restriction of the
coloring to $[1, B]^t$ matters. The hypothesis $t \ge 1$ is the paper's; for $t = 0$ and $r \ge 1$
the statement fails when $f(1) \ge 1$, since the only point gives $|S| = 1 = \operatorname{gs}(S)$.
The paper's hypothesis $r \ge 1$ is dropped: for $r = 0$ there is no coloring and the statement
holds vacuously.

## Sources

- Tom C. Brown, *Piecewise Syndetic Sets in `N^t` and `N^X`*, INTEGERS 24 (2024), Article A2, Theorem 2.

Stated but not proved: `MetaMathlibExt.exists_cube_bound_monochromatic_card_gt_gapSize` is written with `theorem_wanted` in [WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PiecewiseSyndeticWanted.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/piecewise-syndetic-sets/index.html#exists-cube-bound-monochromatic-card-gt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Piecewise syndetic sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/piecewise-syndetic-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/ramsey-theory/structural-ramsey/piecewise-syndetic-sets)
