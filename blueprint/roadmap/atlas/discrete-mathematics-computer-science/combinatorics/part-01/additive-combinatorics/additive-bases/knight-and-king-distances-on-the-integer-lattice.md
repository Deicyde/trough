---
declaration: section
origin: cited
lean: MetaMathlibExt.knightMoves, MetaMathlibExt.kingMoves, MetaMathlibExt.pieceDistance, MetaMathlibExt.maxNormBall, MetaMathlibExt.pieceDistance_eq_of_mem_of_forall, MetaMathlibExt.pieceDistance_kingMoves, MetaMathlibExt.pieceDistance_knightMoves_one_two, MetaMathlibExt.pieceDistance_knightMoves_one_zero
statement: formalized
---

# Knight and king distances on the integer lattice

14 results, 11 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/knight-and-king-distances-on-the-integer-lattice/index.html).

## Knight moves

For integers $a$ and $b$, the $(a,b)$-knight's move set is

$$N_{a,b} = \{(\pm a, \pm b), (\pm b, \pm a)\} \subset \mathbb{Z}^2,$$

the finite set of the points $(a, b)$, $(-a, b)$, $(a, -b)$, $(-a, -b)$, $(b, a)$, $(-b, a)$,
$(b, -a)$ and $(-b, -a)$.

## Sources

- Christian Táfula, *Knights Are 24/13 Times Faster than the King*, The Fibonacci Quarterly 62(3) (2024), definition of `N_{a,b}`.

Formalized by `MetaMathlibExt.knightMoves`, a definition declared in [WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/knight-and-king-distances-on-the-integer-lattice/index.html#knight-moves).

## King moves

The king's move set $K \subset \mathbb{Z}^2$ consists of the eight unit
horizontal, vertical and diagonal steps:

$$K = \{(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)\}.$$

## Sources

- Christian Táfula, *Knights Are 24/13 Times Faster than the King*, The Fibonacci Quarterly 62(3) (2024), definition of `K`.

Formalized by `MetaMathlibExt.kingMoves`, a definition declared in [WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/knight-and-king-distances-on-the-integer-lattice/index.html#king-moves).

## Piece distance on the integer lattice

Let $A \subseteq \mathbb{Z}^2$ be a finite set of
moves and, for $h \ge 1$, let $hA = \{a_1 + \dots + a_h : a_1, \dots, a_h \in A\}$ be its
$h$-fold sumset. The piece distance of a point $p \in \mathbb{Z}^2$ for $A$ is the natural
number that is $0$ if $p = (0,0)$ and otherwise the infimum of the set of integers $h \ge 1$
with $p \in hA$, where the infimum of the empty set is taken to be $0$.

Points other than the origin that are not a sum of moves from $A$ therefore have distance $0$.

## Sources

- Christian Táfula, *Knights Are 24/13 Times Faster than the King*, The Fibonacci Quarterly 62(3) (2024), definition of `A(x,y)`.

Formalized by `MetaMathlibExt.pieceDistance`, a definition declared in [WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/knight-and-king-distances-on-the-integer-lattice/index.html#piece-distance).

## Max-norm ball

For a natural number $h$, the max-norm ball $B_h \subset \mathbb{Z}^2$ is the
product of two copies of the integer interval $\{-h, \dots, h\}$, that is, the set of lattice
points $(x, y)$ with $\max(|x|, |y|) \le h$.

## Sources

- Christian Táfula, *Knights Are 24/13 Times Faster than the King*, The Fibonacci Quarterly 62(3) (2024), definition of `B_h`.

Formalized by `MetaMathlibExt.maxNormBall`, a definition declared in [WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/knight-and-king-distances-on-the-integer-lattice/index.html#max-norm-ball).

## Piece distance from a minimal fold

Let $A \subset \mathbb{Z}^2$ be a finite set, let
$p \in \mathbb{Z}^2$ be nonzero and let $n \ge 1$ be a natural number. If $p$ lies in the
$n$-fold sumset $nA = \{a_1 + \dots + a_n : a_1, \dots, a_n \in A\}$, and every natural number
$h \ge 1$ with $p \in hA$ satisfies $n \le h$, then the piece distance of $p$ for $A$ is $n$.

## Sources

- Christian Táfula, *Knights Are 24/13 Times Faster than the King*, The Fibonacci Quarterly 62(3) (2024), definition of `A(x,y)`.

Formalized by `MetaMathlibExt.pieceDistance_eq_of_mem_of_forall`, a theorem declared in [WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/knight-and-king-distances-on-the-integer-lattice/index.html#piece-distance-eq-of-mem-of-forall).

## King distance is the max norm

For every lattice point $p = (x, y) \in \mathbb{Z}^2$, the
piece distance of $p$ for the king's move set $K$ is $\max(|x|, |y|)$.

## Sources

- Christian Táfula, *Knights Are 24/13 Times Faster than the King*, The Fibonacci Quarterly 62(3) (2024), definitions of `A(x,y)` and `K`.

Formalized by `MetaMathlibExt.pieceDistance_kingMoves`, a theorem declared in [WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/knight-and-king-distances-on-the-integer-lattice/index.html#piece-distance-king-moves).

## The knight reaches $(1,2)$ in one move

Let $N \subseteq \mathbb{Z}^2$ be the move set of the
usual knight, consisting of the eight vectors $(\pm 1, \pm 2)$ and $(\pm 2, \pm 1)$. The piece
distance of the point $(1,2)$ for $N$ is $1$.

## Sources

- Christian Táfula, *Knights Are 24/13 Times Faster than the King*, The Fibonacci Quarterly 62(3) (2024), definition of the usual knight following the definition of `N_{a,b}`.

Formalized by `MetaMathlibExt.pieceDistance_knightMoves_one_two`, a theorem declared in [WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/knight-and-king-distances-on-the-integer-lattice/index.html#piece-distance-knight-moves-one-two).

## The knight needs three moves to reach $(1,0)$

Let $N \subseteq \mathbb{Z}^2$ be the move set
of the usual knight, consisting of the eight vectors $(\pm 1, \pm 2)$ and $(\pm 2, \pm 1)$. The
piece distance of the point $(1,0)$ for $N$ is $3$.

## Sources

- Christian Táfula, *Knights Are 24/13 Times Faster than the King*, The Fibonacci Quarterly 62(3) (2024), characteristic value for the usual knight.

Formalized by `MetaMathlibExt.pieceDistance_knightMoves_one_zero`, a theorem declared in [WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/knight-and-king-distances-on-the-integer-lattice/index.html#piece-distance-knight-moves-one-zero).

## The usual knight reaches (1, 1) in two moves

For the usual knight's move set
$N_{1,2} = \{(\pm 1, \pm 2), (\pm 2, \pm 1)\}$, the piece distance of the point $(1, 1)$ is $2$.

## Sources

- Christian Táfula, *Knights Are 24/13 Times Faster than the King*, The Fibonacci Quarterly 62(3) (2024), characteristic value for the usual knight.

Formalized by `MetaMathlibExt.pieceDistance_knightMoves_one_one`, a theorem declared in [WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/knight-and-king-distances-on-the-integer-lattice/index.html#piece-distance-knight-moves-one-one).

## The knight's distance to the origin is zero

Let $N \subseteq \mathbb{Z}^2$ be the move set of
the usual knight, consisting of the eight vectors $(\pm 1, \pm 2)$ and $(\pm 2, \pm 1)$. The
piece distance of the origin $(0,0)$ for $N$ is $0$.

This holds by the definition of piece distance, which sets the distance at the origin to $0$.

## Sources

- Christian Táfula, *Knights Are 24/13 Times Faster than the King*, The Fibonacci Quarterly 62(3) (2024), definition of `A(0,0)`.

Formalized by `MetaMathlibExt.pieceDistance_knightMoves_zero_zero`, a theorem declared in [WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/knight-and-king-distances-on-the-integer-lattice/index.html#piece-distance-knight-moves-zero-zero).

## Number of points in the max-norm ball

For every natural number $h$, the max-norm ball
$B_h = \{(x, y) \in \mathbb{Z}^2 : \max(|x|, |y|) \le h\}$ has exactly $(2h+1)^2$ points.

## Sources

- Christian Táfula, *Knights Are 24/13 Times Faster than the King*, The Fibonacci Quarterly 62(3) (2024), definition of `B_h`.

Formalized by `MetaMathlibExt.card_maxNormBall`, a theorem declared in [WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/knight-and-king-distances-on-the-integer-lattice/index.html#card-max-norm-ball).

## Uniform bound for knight distance on a box

There is an absolute constant $M \in \mathbb{R}$
such that for all natural numbers $a$ and $b$ with $1 \le a < b$, $\gcd(a, b) = 1$ and $a + b$
odd, every lattice point $(x, y) \in \mathbb{Z}^2$ with $\max(|x|, |y|) \le a + b$ has piece
distance at most $Mb$ for the $(a,b)$-knight's move set
$N_{a,b} = \{(\pm a, \pm b), (\pm b, \pm a)\}$.

## Sources

- Christian Táfula, *Knights Are 24/13 Times Faster than the King*, The Fibonacci Quarterly 62(3) (2024), Lemma 2.1.

Stated but not proved: `MetaMathlibExt.knight_distance_uniform_on_box` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/knight-and-king-distances-on-the-integer-lattice/index.html#knight-distance-uniform-on-box).

## Knight distance asymptotics

There is an absolute constant $M \in \mathbb{R}$ with the
following property. Let $a$ and $b$ be natural numbers with $1 \le a < b$, $\gcd(a, b) = 1$ and
$a + b$ odd, let $N_{a,b} = \{(\pm a, \pm b), (\pm b, \pm a)\}$ be the $(a,b)$-knight's move set,
and for $p \in \mathbb{Z}^2$ let $d_{a,b}(p)$ be the piece distance of $p$ for $N_{a,b}$. Then
for all integers $x$ and $y$ with $0 \le y \le x$: if $by \le ax$, then
$|d_{a,b}(x, y) - x/b| \le Mb$; and if $ax < by$, then
$|d_{a,b}(x, y) - (x + y)/(a + b)| \le Mb$.

## Sources

- Christian Táfula, *Knights Are 24/13 Times Faster than the King*, The Fibonacci Quarterly 62(3) (2024), Theorem 1.1.

Stated but not proved: `MetaMathlibExt.knight_distance_asymptotics` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/knight-and-king-distances-on-the-integer-lattice/index.html#knight-distance-asymptotics).

## Velocity formula for the (a, b)-knight

Let $a$ and $b$ be natural numbers with
$1 \le a < b$, $\gcd(a, b) = 1$ and $a + b$ odd, let
$N_{a,b} = \{(\pm a, \pm b), (\pm b, \pm a)\}$ be the $(a,b)$-knight's move set, and for
$p \in \mathbb{Z}^2$ let $d_{a,b}(p)$ be the piece distance of $p$ for $N_{a,b}$. For a natural
number $h$, let $B_h = \{(x, y) \in \mathbb{Z}^2 : \max(|x|, |y|) \le h\}$ be the max-norm
ball and let $\bar{d}(h) = |B_h|^{-1} \sum_{p \in B_h} d_{a,b}(p)$ be the average of $d_{a,b}$
over $B_h$. Then

$$\lim_{h \to \infty} \frac{2h}{3} \, \bar{d}(h)^{-1} = \frac{2(a+b)b^2}{a^2 + 3b^2}.$$

## Sources

- Christian Táfula, *Knights Are 24/13 Times Faster than the King*, The Fibonacci Quarterly 62(3) (2024), Theorem 1.3.

Stated but not proved: `MetaMathlibExt.knight_velocity_formula` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/KnightKingVelocityWanted.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/knight-and-king-distances-on-the-integer-lattice/index.html#knight-velocity-formula).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Knight and king distances on the integer lattice](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/knight-and-king-distances-on-the-integer-lattice/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/additive-bases/knight-and-king-distances-on-the-integer-lattice)
