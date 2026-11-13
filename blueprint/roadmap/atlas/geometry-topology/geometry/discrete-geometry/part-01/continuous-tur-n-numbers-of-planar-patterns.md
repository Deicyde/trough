---
declaration: section
origin: cited
lean: MetaMathlibExt.PointSetContainsPattern, MetaMathlibExt.pointSetContainsPattern_empty, MetaMathlibExt.opx, MetaMathlibExt.opx_nonneg, MetaMathlibExt.opx_empty, MetaMathlibExt.opx_rotate_reflect, MetaMathlibExt.opx_translate, MetaMathlibExt.opx_mono_of_containsPattern
statement: formalized
---

# Continuous Turán numbers of planar patterns

78 results, 27 proved and 51 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html).

## Containment of planar point sets

A set $S \subseteq \mathbb{R}^2$ contains a set
$P \subseteq \mathbb{R}^2$ when there are maps $f_X, f_Y : \mathbb{R} \to \mathbb{R}$ such that
$f_X(x_0) - f_X(x_1) \ge x_0 - x_1$ whenever $x_0 > x_1$ are $x$-coordinates of points of $P$,
$f_Y(y_0) - f_Y(y_1) \ge y_0 - y_1$ whenever $y_0 > y_1$ are $y$-coordinates of points of $P$,
and $(f_X(x), f_Y(y)) \in S$ for every $(x, y) \in P$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 1 (definition of containment).

Formalized by `MetaMathlibExt.PointSetContainsPattern`, a definition declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#point-set-contains-pattern).

## Every planar set contains the empty pattern

Every set $S \subseteq \mathbb{R}^2$ contains
the empty set $\emptyset$ in the sense of containment of planar point sets.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 1 (definition of containment).

Formalized by `MetaMathlibExt.pointSetContainsPattern_empty`, a theorem declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#point-set-contains-pattern-empty).

## Continuous Turán number in the plane

For a real number $n$ and a set
$P \subseteq \mathbb{R}^2$, the continuous Turán number $\operatorname{opx}(n, P)$ is the supremum
of the Lebesgue measures $\mu_2(S)$ over all open sets $S \subseteq [0, n]^2$ that do not contain
$P$ in the sense of point-set pattern containment; it is $0$ when there is no such set.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 1 (definition of `opx(n, P)`).

Formalized by `MetaMathlibExt.opx`, a definition declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx).

## Nonnegativity of the continuous Turán number

For every real number $n$ and every set
$P \subseteq \mathbb{R}^2$, $\operatorname{opx}(n, P) \ge 0$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 1 (definition of `opx(n, P)`).

Formalized by `MetaMathlibExt.opx_nonneg`, a theorem declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-nonneg).

## Continuous Turán number of the empty pattern

For every real number $n$,
$\mathrm{opx}(n, \emptyset) = 0$: every set contains the empty pattern, so no set avoids it.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 1 (definition of `opx(n, P)`).

Formalized by `MetaMathlibExt.opx_empty`, a theorem declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-empty).

## Rotation and reflection invariance of the continuous Turán number

For every real
number $n$ and every set $P \subseteq \mathbb{R}^2$, the value $\operatorname{opx}(n, P)$ does
not change when $P$ is replaced by its image under the rotation by $90^\circ$,
$(x, y) \mapsto (-y, x)$, under the reflection $(x, y) \mapsto (-x, y)$, or under the
reflection $(x, y) \mapsto (x, -y)$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Lemma 2.1.

Stated but not proved: `MetaMathlibExt.opx_rotate_reflect` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-rotate-reflect).

## Translation invariance of the continuous Turán number

Let $n$ be a real number,
$P \subseteq \mathbb{R}^2$ a set and $v \in \mathbb{R}^2$ a vector, and let
$P + v = \{p + v : p \in P\}$ be the translate of $P$ by $v$. Then
$\operatorname{opx}(n, P + v) = \operatorname{opx}(n, P)$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Lemma 2.2.

Stated but not proved: `MetaMathlibExt.opx_translate` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-translate).

## Monotonicity of the continuous Turán number under containment

Let $n$ be a real number
and let $P, Q \subseteq \mathbb{R}^2$. If $Q$ contains $P$ in the sense of containment of planar
point sets, then $\operatorname{opx}(n, P) \le \operatorname{opx}(n, Q)$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Lemma 2.3.

Stated but not proved: `MetaMathlibExt.opx_mono_of_containsPattern` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-mono-of-contains-pattern).

## Monotonicity of the continuous Turán number in the side length

For every set
$P \subseteq \mathbb{R}^2$ and all real numbers $m \le n$, the continuous Turán numbers satisfy
$\operatorname{opx}(m, P) \le \operatorname{opx}(n, P)$.

The paper assumes $0 < m$. This is not needed, since $\operatorname{opx}(m, P) = 0$ for $m \le 0$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Lemma 2.4.

Stated but not proved: `MetaMathlibExt.opx_mono_left` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-mono-left).

## Superadditivity of the continuous Turán number

For every set $P \subseteq \mathbb{R}^2$
and all real numbers $m, n > 0$,
$\operatorname{opx}(m, P) + \operatorname{opx}(n, P) \le \operatorname{opx}(m + n, P)$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Lemma 2.5.

Stated but not proved: `MetaMathlibExt.opx_superadditive` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-superadditive).

## Increment bound for the continuous Turán number

Let $P \subseteq \mathbb{R}^2$ and let
$n, \delta$ be real numbers with $n > 0$ and $0 < \delta < n$. Then the continuous Turán number
$\mathrm{opx}$ satisfies $\mathrm{opx}(n, P) \le \mathrm{opx}(n + \delta, P)$ and
$\mathrm{opx}(n + \delta, P) < \mathrm{opx}(n, P) + 3 n \delta$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Lemma 2.6.

Stated but not proved: `MetaMathlibExt.opx_add_lt` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-add-lt).

## Continuity of the continuous Turán number

For every $P \subseteq \mathbb{R}^2$, the
continuous Turán number $\mathrm{opx}(n, P)$ is a continuous function of $n$ on $(0, \infty)$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Proposition 2.7.

Stated but not proved: `MetaMathlibExt.opx_continuousOn` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-continuous-on).

## Sections of open sets avoiding a horizontal segment

Let $a, b, c, n$ be real numbers with
$c \ge 0$, and let $S \subseteq [0, n]^2$ be an open set that does not contain the closed
horizontal segment $[a, a + c] \times \{b\}$ in the sense of containment of planar point sets.
Then for every $y \in [0, n]$ the horizontal section $\{x \in \mathbb{R} : (x, y) \in S\}$ has
one-dimensional Lebesgue measure at most $c$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Lemma 2.8.

Stated but not proved: `MetaMathlibExt.volume_section_le_of_segment_free` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#volume-section-le-of-segment-free).

## Extending a pattern by a horizontal segment at its right edge

Let
$P \subseteq \mathbb{R}^2$ and $(x_0, y_0) \in P$ with $x \le x_0$ for every $(x, y) \in P$, and let
$c \ge 0$ and $n > 0$ be real numbers. Then

$$\operatorname{opx}(n, P \cup ([x_0, x_0 + c] \times \{y_0\})) \le \operatorname{opx}(n, P) + cn.$$

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Lemma 2.9.

Stated but not proved: `MetaMathlibExt.opx_union_segment_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-union-segment-le).

## Adding a point to the right of a pattern

Let $P \subseteq \mathbb{R}^2$ and let
$(x_0, y_0) \in P$ be such that every point of $P$ has $x$-coordinate at most $x_0$. Then
$\operatorname{opx}(n, P \cup \{(x_0 + c, y_0)\}) \le \operatorname{opx}(n, P) + cn$ for all real
numbers $c > 0$ and $n > 0$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Corollary 2.10.

Stated but not proved: `MetaMathlibExt.opx_insert_point_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-insert-point-le).

## Continuous Turán number of a dilated finite pattern

Let $P \subseteq \mathbb{R}^2$ be
finite, and let $c > 0$ and $d$ be real numbers such that any two consecutive distinct
$x$-coordinates of points of $P$ differ by at least $c$ and at most $d$, and likewise for
$y$-coordinates. Let $q > 1$ and $qP = \{qp : p \in P\}$. Then for every real $n > 0$,
$\mathrm{opx}(n, qP) \le (\lceil qd/c \rceil + 1)^2 \, \mathrm{opx}(m, P)$, where
$m = \lceil \lceil n/c \rceil / (\lceil qd/c \rceil + 1) \rceil \, c$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Lemma 2.12.

Stated but not proved: `MetaMathlibExt.opx_dilate_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-dilate-le).

## Continuous Turán number of a horizontal segment

Let $a, b, c, n$ be real numbers with
$0 \le c \le n$, and let $P = [a, a + c] \times \{b\}$ be the closed horizontal segment of length
$c$ at height $b$. Then $\operatorname{opx}(n, P) = cn$.

The hypothesis $n \ge c$ is missing from the paper, whose lower-bound construction
$(0, c) \times (0, n) \subseteq [0, n]^2$ uses it: for $0 < n < c$ no subset of $[0, n]^2$ contains
$P$, so $\operatorname{opx}(n, P) = n^2 \ne cn$ (for example $c = 2$ and $n = 1$).

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Theorem 4.1.

Stated but not proved: `MetaMathlibExt.opx_horizontal_segment` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-horizontal-segment).

## Continuous Turán number of a diagonal segment

Let $a, b, n$ be real numbers with
$0 < a \le n$ and $0 < b \le n$, and let $P$ be the closed segment from $(0, 0)$ to $(a, b)$.
Then the continuous Turán number satisfies $\operatorname{opx}(n, P) = (a + b)n - ab$.

The hypotheses $a \le n$ and $b \le n$ are missing from the paper, whose lower-bound construction
$(0, a) \times (0, n) \cup (0, n) \times (0, b) \subseteq [0, n]^2$ uses them: for
$0 < n < \max(a, b)$ no subset of $[0, n]^2$ contains $P$, so $\operatorname{opx}(n, P) = n^2$
(for example $a = b = 2$ and $n = 1$, where $(a + b)n - ab = 0 \ne 1$).

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Theorem 4.2.

Stated but not proved: `MetaMathlibExt.opx_diagonal_segment` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-diagonal-segment).

## Open patterns have quadratic continuous Turán number

For every nonempty open set
$P \subseteq \mathbb{R}^2$, $\operatorname{opx}(n, P) = \Theta(n^2)$ as the real number $n$ tends
to infinity.

The paper does not assume that $P$ is nonempty. The assumption is needed, since
$\operatorname{opx}(n, \emptyset) = 0$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Theorem 4.5.

Stated but not proved: `MetaMathlibExt.opx_open_isTheta` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-open-is-theta).

## Rational points of open patterns have quadratic continuous Turán number

Let
$P \subseteq \mathbb{R}^2$ be a nonempty open set and let $Q_P$ be the set of points of $P$ both
of whose coordinates are rational. Then $\operatorname{opx}(n, Q_P) = \Theta(n^2)$ as the real
number $n$ tends to infinity.

The paper does not assume that $P$ is nonempty. The assumption is needed, since
$Q_\emptyset = \emptyset$ and $\operatorname{opx}(n, \emptyset) = 0$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Theorem 4.6.

Stated but not proved: `MetaMathlibExt.opx_rational_points_isTheta` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-rational-points-is-theta).

## Continuous Turán number of the graph of an increasing function

Let $a > 0$ and $b$ be real
numbers and let $f : \mathbb{R} \to \mathbb{R}$ be strictly increasing on $[0, a]$ with
$(f(t) - f(s)) / (t - s) \le b$ for all $s < t$ in $[0, a]$. Then the graph
$P = \{(t, f(t)) : t \in [0, a]\}$ satisfies $\operatorname{opx}(n, P) = \Theta(n)$ as the real
number $n$ tends to infinity.

The hypothesis $a > 0$ is needed: for $a = 0$ the set $P$ is a single point and
$\operatorname{opx}(n, P) = 0$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Theorem 4.3.

Stated but not proved: `MetaMathlibExt.opx_increasing_graph_isTheta` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-increasing-graph-is-theta).

## Large sets of grid cells with no $r \times r$ all-ones submatrix

For all natural numbers
$r \ge 2$ and $n \ge 1$ there is a set $S$ of cells of the $n \times n$ grid
$\{0, \dots, n - 1\}^2$ with $|S| \ge \frac{1}{2} n^{2 - 2/(r+1)}$ that contains no $r \times r$
all-ones submatrix: there are no sets $R, C \subseteq \{0, \dots, n - 1\}$ with $|R| = |C| = r$
and $R \times C \subseteq S$.

In the language of 0-1 matrix extremal functions this says $\operatorname{ex}(n, J_{r,r}) \ge
\frac{1}{2} n^{2-2/(r+1)}$ for the $r \times r$ all-ones matrix $J_{r,r}$; it is the cited
Kővári–Sós–Turán-type lower bound, with the paper's explicit constant.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Lemma 4.4.

Stated but not proved: `MetaMathlibExt.exists_large_Jrr_free_cells` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#exists-large-jrr-free-cells).

## Continuous Turán number of the equal-sign pattern

Let $s > 0$ and $c > 0$ be real numbers
and let $P_{s,2,c} = [0, s] \times \{c, 2c\}$ be the equal-sign pattern, two horizontal segments of
length $s$ at heights $c$ and $2c$. Then, as the real number $n$ tends to infinity with $s$ and
$c$ fixed, $\operatorname{opx}(n, P_{s,2,c}) = \Theta(s^{1/2} n^{3/2})$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Theorem 4.7; `P_{s,t,c}` as defined before it.

Stated but not proved: `MetaMathlibExt.opx_equal_sign_isTheta` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-equal-sign-is-theta).

## Lower bound on the volume of a staircase region

Let $t$ be a natural number and let
$c, n$ be real numbers with $c \ge 0$ and $ct \le n$. Let $X \subseteq \mathbb{R}^t$ be the set of
points $y = (y_0, \dots, y_{t-1})$ such that $y_i < n - ic$ for every $i$, $y_{i+1} + c < y_i$ for
every $i < t - 1$, and $y_{t-1} > 0$ if $t \ge 1$. Then the $t$-dimensional Lebesgue measure of
$X$ is at least $(n/t - c)^t$, where $n/t$ is read as $0$ when $t = 0$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Lemma 4.8, the explicit bound.

Stated but not proved: `MetaMathlibExt.volume_staircase_simplex_ge` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#volume-staircase-simplex-ge).

## Upper bound for stacked horizontal segments

Let $t \ge 2$ be a natural number, let
$s, c > 0$ be real numbers, and let $P_{s,t,c} = [0, s] \times \{c, 2c, \dots, tc\}$ be the union
of the $t$ horizontal segments of length $s$ at heights $c, 2c, \dots, tc$. Then
$\operatorname{opx}(n, P_{s,t,c}) = O(s^{1/t} n^{2 - 1/t})$ as the real number $n$ tends to
infinity, with $s$, $t$ and $c$ fixed.

Since $s$ is fixed, the factor $s^{1/t}$ only changes the implied constant.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Theorem 4.9; `P_{s,t,c}` as defined before Theorem 4.7.

Stated but not proved: `MetaMathlibExt.opx_stacked_segments_isBigO` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-stacked-segments-is-big-o).

## Linear bound for separated horizontal segments

Let $k$ be a natural number and let
$a_i \le b_i$ and $y_i$ be real numbers for $i = 1, \dots, k$, such that the intervals
$[a_i, b_i]$ are pairwise disjoint and the heights $y_i$ are pairwise distinct, and let
$P = \bigcup_{i=1}^k [a_i, b_i] \times \{y_i\}$. Then the continuous Turán number satisfies
$\operatorname{opx}(n, P) = O(n)$ as the real number $n$ tends to infinity.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Theorem 4.10.

Stated but not proved: `MetaMathlibExt.opx_horizontal_segments_isBigO` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-horizontal-segments-is-big-o).

## Containment of a point pattern in a set of grid cells

A set of cells
$A \subseteq \mathbb{N} \times \mathbb{N}$, each cell written (column, row), contains a set
$P \subseteq \mathbb{R}^2$ when there are maps $f_X, f_Y : \mathbb{R} \to \mathbb{N}$ such that
$f_X$ is strictly increasing on the set of $x$-coordinates of points of $P$, $f_Y$ is strictly
increasing on the set of $y$-coordinates of points of $P$, and $(f_X(x), f_Y(y)) \in A$ for every
$(x, y) \in P$.

For finite $P$ this is containment of the 0-1 matrix $M_P$ of $P$ (rows of $P$ listed bottom to
top; flipping the rows of both matrices preserves containment).

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 1 (0-1 matrix containment and the matrix `M_P` of a finite point set).

Formalized by `MetaMathlibExt.CellsContainPattern`, a definition declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#cells-contain-pattern).

## 0-1 matrix extremal function of a point pattern

For a natural number $n$ and a set
$P \subseteq \mathbb{R}^2$, $\mathrm{ex}(n, M_P)$ is the largest number of cells of the
$n \times n$ grid $\{0, \dots, n - 1\}^2$ forming a set that does not contain $P$ (cells contain
$P$ when there are strictly increasing maps from the $x$-coordinates of $P$ to columns and from the
$y$-coordinates of $P$ to rows that send every point of $P$ to a cell of the set), and $0$ if there
is no such set (as for $P = \emptyset$). For finite $P$ this is the 0-1 matrix extremal function
$\mathrm{ex}(n, M_P)$, the maximum number of ones in an $n \times n$ 0-1 matrix that does not
contain the 0-1 matrix $M_P$ of $P$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 1 (definitions of `ex(n, M)` and of `M_P`).

Formalized by `MetaMathlibExt.patternEx`, a definition declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#pattern-ex).

## The extremal function of the empty pattern vanishes

For every natural number $n$,
$\operatorname{ex}(n, M_\emptyset) = 0$, since every set of cells contains the empty pattern.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 1 (definitions of `ex(n, M)` and of `M_P`).

Formalized by `MetaMathlibExt.patternEx_empty`, a theorem declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#pattern-ex-empty).

## The extremal function of a single point vanishes

For every natural number $n$ and every
point $p \in \mathbb{R}^2$, the 0-1 matrix extremal function of the one-point pattern $\{p\}$ on
the $n \times n$ grid is zero: $\mathrm{ex}(n, M_{\{p\}}) = 0$. Indeed, a single point is contained
in every nonempty set of cells.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 1 (definitions of `ex(n, M)` and of `M_P`).

Formalized by `MetaMathlibExt.patternEx_singleton`, a theorem declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#pattern-ex-singleton).

## Trivial upper bound for the 0-1 matrix extremal function

Let $n$ be a natural number and
$P \subseteq \mathbb{R}^2$ a set, and let $\mathrm{ex}(n, M_P)$ be the largest number of cells of
the $n \times n$ grid $\{0, \dots, n - 1\}^2$ forming a set that does not contain $P$ ($0$ if
there is no such set). Then $\mathrm{ex}(n, M_P) \le n^2$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 1 (definitions of `ex(n, M)` and of `M_P`).

Formalized by `MetaMathlibExt.patternEx_le_sq`, a theorem declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#pattern-ex-le-sq).

## Inverse Ackermann function

For a natural number $n$, the inverse Ackermann function
$\alpha(n)$ is the least natural number $k$ with $n \le A(k, k)$, where $A$ is the two-argument
Ackermann function, given for all natural numbers $m$ and $j$ by $A(0, j) = j + 1$,
$A(m + 1, 0) = A(m, 1)$ and $A(m + 1, j + 1) = A(m, A(m + 1, j))$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 3.2 (the inverse Ackermann function `α(n)` in Keszegh's bound quoted before Corollary 3.8).

Formalized by `MetaMathlibExt.inverseAckermann`, a definition declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#inverse-ackermann).

## Defining inequality of the inverse Ackermann function

For every natural number $n$,
$n \le A(\alpha(n), \alpha(n))$, where $\alpha$ is the inverse Ackermann function and $A$ is the
two-argument Ackermann function.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 3.2 (the inverse Ackermann function `α(n)`).

Formalized by `MetaMathlibExt.le_ack_inverseAckermann`, a theorem declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#le-ack-inverse-ackermann).

## Upper bound for the inverse Ackermann function

For all natural numbers $n$ and $k$, if
$n \le A(k, k)$, where $A$ is the two-argument Ackermann function, then $\alpha(n) \le k$, where
$\alpha$ is the inverse Ackermann function.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 3.2 (the inverse Ackermann function `α(n)`).

Formalized by `MetaMathlibExt.inverseAckermann_le`, a theorem declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#inverse-ackermann-le).

## The inverse Ackermann function at 2

The inverse Ackermann function $\alpha$ satisfies
$\alpha(2) = 1$, since $A(0, 0) = 1 < 2 \le 3 = A(1, 1)$, where $A$ is the two-argument
Ackermann function.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 3.2 (the inverse Ackermann function `α(n)`).

Formalized by `MetaMathlibExt.inverseAckermann_two`, a theorem declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#inverse-ackermann-two).

## The inverse Ackermann function at 8

The inverse Ackermann function $\alpha$ satisfies
$\alpha(8) = 3$, since $A(2, 2) = 7 < 8 \le 61 = A(3, 3)$, where $A$ is the two-argument
Ackermann function.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 3.2 (the inverse Ackermann function `α(n)`).

Formalized by `MetaMathlibExt.inverseAckermann_eight`, a theorem declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#inverse-ackermann-eight).

## Continuous Turán numbers versus 0-1 matrix extremal functions

Let $P$ be a finite subset
of $\mathbb{R}^2$. Then the continuous Turán number $\mathrm{opx}(n, P)$ and the 0-1 matrix
extremal function $\mathrm{ex}(n, M_P)$ of $P$ on the $n \times n$ grid satisfy
$\mathrm{opx}(n, P) = \Theta(\mathrm{ex}(n, M_P))$ as $n \to \infty$ through the natural numbers,
with constants depending on $P$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Theorem 3.1.

Stated but not proved: `MetaMathlibExt.opx_isTheta_patternEx` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-is-theta-pattern-ex).

## Lower bound for continuous Turán numbers of finite patterns

Let $P$ be a finite subset of
$\mathbb{R}^2$. For a natural number $n$, write $\mathrm{opx}(n, P)$ for the continuous Turán
number of $P$ (the supremum of the Lebesgue measures of the open subsets of $[0, n]^2$ that do not
contain $P$, or $0$ if there are none) and $\mathrm{ex}(n, M_P)$ for the 0-1 matrix extremal
function of $P$ on the $n \times n$ grid. Then $\mathrm{ex}(n, M_P) = O(\mathrm{opx}(n, P))$ as
$n \to \infty$ through the natural numbers; that is,
$\mathrm{opx}(n, P) = \Omega(\mathrm{ex}(n, M_P))$, with constants depending on $P$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Theorem 3.2.

Stated but not proved: `MetaMathlibExt.patternEx_isBigO_opx` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#pattern-ex-is-big-o-opx).

## Upper bound for continuous Turán numbers of finite patterns

Let $P$ be a finite subset of
$\mathbb{R}^2$. Then the continuous Turán number $\mathrm{opx}(n, P)$ and the 0-1 matrix extremal
function $\mathrm{ex}(n, M_P)$ of $P$ on the $n \times n$ grid satisfy
$\mathrm{opx}(n, P) = O(\mathrm{ex}(n, M_P))$ as $n \to \infty$ through the natural numbers.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Theorem 3.3.

Stated but not proved: `MetaMathlibExt.opx_isBigO_patternEx` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-is-big-o-pattern-ex).

## Linear bound for permutation-like point patterns

There is a real constant $C$ such that
for every real $c > 0$ there is a real constant $K$ with the following property. Let
$P \subseteq \mathbb{R}^2$ be a finite set of $k$ points whose $x$-coordinates are pairwise
distinct and whose $y$-coordinates are pairwise distinct, such that any two consecutive
$x$-coordinates of points of $P$ differ by at most $c$, and so do any two consecutive
$y$-coordinates. Then $\operatorname{opx}(n, P) \le K \cdot 2^{Ck} \cdot n$ for every natural
number $n$.

The paper states the bound as $2^{O(k)} n$, with the implied constant depending on $c$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Corollary 3.4.

Stated but not proved: `MetaMathlibExt.opx_permutation_pattern_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-permutation-pattern-le).

## Upper bound for the continuous Turán number of a grid

Let $X$ and $Y$ be finite sets of
real numbers, let $P = X \times Y$ be the grid they span and let $t = |X|$ be its number of
columns. Then $\operatorname{opx}(n, P) = O(n^{2 - 1/t})$ as the natural number $n$ tends to
infinity, where for $t = 0$ (so that $P$ is empty) the exponent $2 - 1/t$ is read as $2$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Corollary 3.5.

Stated but not proved: `MetaMathlibExt.opx_grid_isBigO` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-grid-is-big-o).

## Power saving for continuous Turán numbers of finite planar patterns

Let
$P \subseteq \mathbb{R}^2$ be finite. Then there is a real number $\varepsilon > 0$ such that the
continuous Turán number satisfies $\operatorname{opx}(n, P) = O(n^{2 - \varepsilon})$ as the
natural number $n$ tends to infinity.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Corollary 3.6.

Stated but not proved: `MetaMathlibExt.exists_opx_isBigO_rpow` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 431](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L431). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#exists-opx-is-big-o-rpow).

## Continuous Turán number of a grid with two columns

Let $X$ and $Y$ be finite sets of real
numbers with $|X| = 2$ and $|Y| \ge 2$, and let $P = X \times Y$ be the grid with $2$ columns and
$|Y|$ rows. Then $\operatorname{opx}(n, P) = \Theta(n^{3/2})$ as the natural number $n$ tends to
infinity.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Corollary 3.7, first sentence.

Stated but not proved: `MetaMathlibExt.opx_grid_two_columns_isTheta` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-grid-two-columns-is-theta).

## Continuous Turán number of a grid with three columns

Let $X$ and $Y$ be finite sets of
real numbers with $|X| = 3$ and $|Y| \ge 3$, and let $P = X \times Y$ be the grid with $3$ columns
and $|Y|$ rows. Then $\operatorname{opx}(n, P) = \Theta(n^{5/3})$ as the natural number $n$ tends
to infinity.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Corollary 3.7, second sentence.

Stated but not proved: `MetaMathlibExt.opx_grid_three_columns_isTheta` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 450](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L450). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-grid-three-columns-is-theta).

## Almost linear bound for patterns with at most one point in each row

Let
$P \subseteq \mathbb{R}^2$ be a finite set whose points have pairwise distinct $y$-coordinates.
Then there is a natural number $t$ such that $\operatorname{opx}(n, P) = O(n \cdot 2^{\alpha(n)^t})$
as the natural number $n$ tends to infinity, where $\operatorname{opx}$ is the continuous Turán
number and $\alpha$ is the inverse Ackermann function.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Corollary 3.8.

Stated but not proved: `MetaMathlibExt.exists_opx_isBigO_inverseAckermann` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 461](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L461). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#exists-opx-is-big-o-inverse-ackermann).

## Two-row patterns of growing width

For each real $n$ let $Q_n \subseteq \mathbb{R}^2$
be a set all of whose points have $y$-coordinate $0$ or $1$, whose least $x$-coordinate is $0$
and whose greatest $x$-coordinate is $s(n)$. Then the following are equivalent: for every
$\varepsilon > 0$, $\operatorname{opx}(n, Q_n) \ge n^{2 - \varepsilon}$ for all sufficiently large
real $n$; and for every $\varepsilon > 0$, $s(n) \ge n^{1 - \varepsilon}$ for all sufficiently
large real $n$.

In asymptotic notation: $\operatorname{opx}(n, Q_n) = \Omega(n^{2 - o(1)})$ if and only if
$s(n) = \Omega(n^{1 - o(1)})$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Proposition 6.4.

Stated but not proved: `MetaMathlibExt.opx_two_row_growing_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-two-row-growing-iff).

## Saturating sets for a point pattern

Let $n$ be a real number and let $P$ and $S$ be
subsets of $\mathbb{R}^2$. Then $S$ is saturating for $P$ in $[0, n]^2$ when $S$ is an open
subset of $[0, n]^2$ that does not contain $P$, while every open set $S'$ with
$S \subsetneq S' \subseteq [0, n]^2$ contains $P$. Here a set $T$ contains $P$ when there are
maps $f_X, f_Y : \mathbb{R} \to \mathbb{R}$ such that $f_X(x) - f_X(x') \ge x - x'$ whenever
$x > x'$ are $x$-coordinates of points of $P$, likewise $f_Y(y) - f_Y(y') \ge y - y'$ whenever
$y > y'$ are $y$-coordinates of points of $P$, and $(f_X(x), f_Y(y)) \in T$ for every
$(x, y) \in P$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 6 (definition of saturating sets).

Formalized by `MetaMathlibExt.IsOpxSaturating`, a definition declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 484](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L484). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#is-opx-saturating).

## Saturation function for continuous patterns

For a real number $n$ and a set
$P \subseteq \mathbb{R}^2$, call an open set $S \subseteq [0, n]^2$ saturating for $P$ if $S$
does not contain $P$ but every open set $S' \subseteq [0, n]^2$ properly containing $S$ contains
$P$ (containment in the sense of point-set pattern containment). The saturation function
$\operatorname{osat}(n, P)$ is the infimum of the Lebesgue measures $\mu_2(S)$ over all sets $S$
saturating for $P$, and is $0$ when no saturating set exists.

The paper leaves $\operatorname{osat}(n, P)$ undefined when no saturating set exists.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 6 (definition of `osat(n, P)`).

Formalized by `MetaMathlibExt.osat`, a definition declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 495](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L495). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#osat).

## The saturation function is nonnegative

For every real number $n$ and every set
$P \subseteq \mathbb{R}^2$, $\operatorname{osat}(n, P) \ge 0$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 6 (definition of `osat(n, P)`).

Formalized by `MetaMathlibExt.osat_nonneg`, a theorem declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#osat-nonneg).

## Saturation function and continuous Turán number of a single point

For every real number
$n$ and every point $p \in \mathbb{R}^2$, $\operatorname{osat}(n, \{p\}) = 0$ and
$\operatorname{opx}(n, \{p\}) = 0$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Lemma 6.5.

Stated but not proved: `MetaMathlibExt.osat_singleton_and_opx_singleton` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 512](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L512). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#osat-singleton-and-opx-singleton).

## Containment of point sets in $\mathbb{R}^d$

Let $d$ be a natural number and let
$S, P \subseteq \mathbb{R}^d$. Then $S$ contains $P$ when there are maps
$f_1, \dots, f_d : \mathbb{R} \to \mathbb{R}$ that expand distances between coordinates of points
of $P$, that is, $f_i(p_i) - f_i(q_i) \ge p_i - q_i$ for every $i$ and all $p, q \in P$ with
$p_i > q_i$, and such that $(f_1(p_1), \dots, f_d(p_d)) \in S$ for every $p \in P$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 5 (definition of containment in `ℝ^d`).

Formalized by `MetaMathlibExt.ContainsPatternD`, a definition declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#contains-pattern-d).

## Every set in $\mathbb{R}^d$ contains the empty pattern

For every natural number $d$ and
every set $S \subseteq \mathbb{R}^d$, $S$ contains the empty set $\emptyset \subseteq \mathbb{R}^d$
in the sense of containment of point sets in $\mathbb{R}^d$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 5 (definition of containment in `ℝ^d`).

Formalized by `MetaMathlibExt.containsPatternD_empty`, a theorem declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 531](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#contains-pattern-d-empty).

## Continuous Turán number in $\mathbb{R}^d$

For a natural number $d$, a real number $n$
and a set $P \subseteq \mathbb{R}^d$, the continuous Turán number $\mathrm{opx}(n, P, d)$ is the
supremum of the $d$-dimensional Lebesgue measures $\mu_d(S)$ over all open sets
$S \subseteq [0, n]^d$ that do not contain $P$ in the sense of containment of point sets in
$\mathbb{R}^d$; it is $0$ when there is no such set.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 5 (definition of `opx(n, P, d)`).

Formalized by `MetaMathlibExt.opxD`, a definition declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 539](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L539). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-d).

## Higher-dimensional continuous Turán numbers are nonnegative

For every dimension $d$,
real number $n$ and set $P \subseteq \mathbb{R}^d$, $\mathrm{opx}(n, P, d) \ge 0$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 5 (definition of `opx(n, P, d)`).

Formalized by `MetaMathlibExt.opxD_nonneg`, a theorem declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 547](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L547). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-d-nonneg).

## The higher-dimensional continuous Turán number of the empty pattern

For every dimension
$d$ and every real number $n$, $\mathrm{opx}(n, \emptyset, d) = 0$: every set contains the empty
pattern, so no set is free of it.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 5 (definition of `opx(n, P, d)`).

Formalized by `MetaMathlibExt.opxD_empty`, a theorem declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 556](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L556). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-d-empty).

## Containment of a point pattern in d-dimensional grid cells

Let $d$ be a natural number,
let $A \subseteq \mathbb{N}^d$ be a set of cells and let $P \subseteq \mathbb{R}^d$. Then $A$
contains $P$ when there are maps $f_1, \dots, f_d : \mathbb{R} \to \mathbb{N}$ such that each $f_i$
is strictly increasing on the set $\{p_i : p \in P\}$ of $i$-th coordinates of points of $P$, and
$(f_1(p_1), \dots, f_d(p_d)) \in A$ for every $p \in P$.

For finite $P$ this is containment of the $d$-dimensional 0-1 matrix $M_P$ of $P$ in the 0-1
matrix whose ones are the cells of $A$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 5 (containment of `d`-dimensional 0-1 matrices and the matrix `M_P`).

Formalized by `MetaMathlibExt.CellsContainPatternD`, a definition declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 565](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L565). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#cells-contain-pattern-d).

## Extremal function of a $d$-dimensional pattern

For natural numbers $d$ and $n$ and a set
$P \subseteq \mathbb{R}^d$, say that a set $A$ of cells of $\mathbb{N}^d$ contains $P$ when there
are maps $f_1, \dots, f_d$ to $\mathbb{N}$, each $f_i$ strictly increasing on the $i$-th
coordinates of the points of $P$, with $(f_1(p_1), \dots, f_d(p_d)) \in A$ for every $p \in P$.
Then $\operatorname{ex}(n, M_P, d)$ is the largest number of cells of a set of cells of the grid
$\{0, \dots, n - 1\}^d$ that does not contain $P$, and is $0$ when every such set contains $P$.
For finite $P$ this is the $d$-dimensional 0-1 matrix extremal function of the matrix $M_P$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 5 (definitions of `ex(n, M, d)` and of `M_P`).

Formalized by `MetaMathlibExt.patternExD`, a definition declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 575](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L575). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#pattern-ex-d).

## The $d$-dimensional extremal function of the empty pattern vanishes

For all natural
numbers $d$ and $n$, $\operatorname{ex}(n, M_\emptyset, d) = 0$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 5 (definitions of `ex(n, M, d)` and of `M_P`).

Formalized by `MetaMathlibExt.patternExD_empty`, a theorem declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 583](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L583). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#pattern-ex-d-empty).

## The $d$-dimensional extremal function of a single point vanishes

For all natural numbers
$d$ and $n$ and every point $p \in \mathbb{R}^d$, $\operatorname{ex}(n, M_{\{p\}}, d) = 0$, since a
single point is contained in every nonempty set of cells.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Section 5 (definitions of `ex(n, M, d)` and of `M_P`).

Formalized by `MetaMathlibExt.patternExD_singleton`, a theorem declared in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 592](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L592). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#pattern-ex-d-singleton).

## Higher-dimensional continuous Turán numbers are monotone under containment

Let
$P, Q \subseteq \mathbb{R}^d$. If $Q$ contains $P$, then
$\mathrm{opx}(n, P, d) \le \mathrm{opx}(n, Q, d)$ for every real number $n$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Lemma 5.1.

Stated but not proved: `MetaMathlibExt.opxD_mono_of_containsPatternD` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 605](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L605). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-d-mono-of-contains-pattern-d).

## Higher-dimensional continuous Turán numbers are monotone in the side length

For every
set $P \subseteq \mathbb{R}^d$ and all real numbers $m \le n$,
$\mathrm{opx}(m, P, d) \le \mathrm{opx}(n, P, d)$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Lemma 5.2.

Stated but not proved: `MetaMathlibExt.opxD_mono_left` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 612](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L612). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-d-mono-left).

## Increment bound for the d-dimensional continuous Turán number

Let $d \ge 2$ be a
natural number, let $P \subseteq \mathbb{R}^d$, and let $n, \varepsilon$ be real numbers with
$n > 0$ and $0 < \varepsilon < n$. Then the $d$-dimensional continuous Turán number
$\mathrm{opx}$ satisfies $\mathrm{opx}(n, P, d) \le \mathrm{opx}(n + \varepsilon, P, d)$ and
$\mathrm{opx}(n + \varepsilon, P, d) < \mathrm{opx}(n, P, d) + d (2n)^{d-1} \varepsilon$.

The hypothesis $d \ge 2$ is needed: for $d = 1$ and $P = \{0, L\}$ with $L > n + \varepsilon$,
every open subset of $[0, n + \varepsilon]$ avoids $P$, so
$\mathrm{opx}(n + \varepsilon, P, 1) = n + \varepsilon = \mathrm{opx}(n, P, 1) + \varepsilon$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Lemma 5.3.

Stated but not proved: `MetaMathlibExt.opxD_add_lt` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 622](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L622). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-d-add-lt).

## Continuity of the d-dimensional continuous Turán number

For every natural number $d$
and every $P \subseteq \mathbb{R}^d$, the $d$-dimensional continuous Turán number
$\mathrm{opx}(n, P, d)$ is a continuous function of $n$ on $(0, \infty)$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Proposition 5.4.

Stated but not proved: `MetaMathlibExt.opxD_continuousOn` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 630](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L630). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-d-continuous-on).

## Projection bound for the d-dimensional continuous Turán number

Let $d$ be a natural
number, $n$ a real number and $P \subseteq \mathbb{R}^{d+1}$, and let $\Pr(P)$ be the subset of
$\mathbb{R}^d$ obtained by dropping the last coordinate of every point of $P$. Writing
$\mathrm{opx}(n, Q, k)$ for the $k$-dimensional continuous Turán number, we have
$n \cdot \mathrm{opx}(n, \Pr(P), d) \le \mathrm{opx}(n, P, d + 1)$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Lemma 5.5; `Pr(P)` as defined before it.

Stated but not proved: `MetaMathlibExt.mul_opxD_init_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 638](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L638). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#mul-opx-d-init-le).

## Patterns with a constant last coordinate

Let $P \subseteq \mathbb{R}^{d+1}$ be a set
whose points all have the same last coordinate, and let $\mathrm{Pr}(P) \subseteq \mathbb{R}^d$ be
the set obtained by deleting the last coordinate of each point of $P$. Then for every real number
$n$, $\mathrm{opx}(n, P, d + 1) = n \cdot \mathrm{opx}(n, \mathrm{Pr}(P), d)$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Proposition 5.6.

Stated but not proved: `MetaMathlibExt.opxD_eq_mul_opxD_init` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 646](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L646). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-d-eq-mul-opx-d-init).

## Rational points of an embedded open planar set

Let $m$ be a natural number and let
$P \subseteq \mathbb{R}^2$ be a nonempty open set. Let
$P' = P \times \{0\}^{m+1} \subseteq \mathbb{R}^{m+3}$, and let $Q_{P'}$ be the set of points of
$P'$ all of whose coordinates are rational. Then $\mathrm{opx}(n, Q_{P'}, m + 3) = \Theta(n^{m+3})$
as the real number $n$ tends to infinity.

Nonemptiness is added: for $P = \emptyset$ the set $Q_{P'}$ is empty.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Corollary 5.7.

Stated but not proved: `MetaMathlibExt.opxD_rational_points_embed_isTheta` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 656](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L656). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-d-rational-points-embed-is-theta).

## Nonempty open patterns in dimension at least two

Let $d \ge 2$, let
$P \subseteq \mathbb{R}^d$ be a nonempty open set, and let $Q_P$ be the set of points of $P$ all
of whose coordinates are rational. Then, as the real number $n \to \infty$,
$\mathrm{opx}(n, P, d) = \Theta(n^d)$ and $\mathrm{opx}(n, Q_P, d) = \Theta(n^d)$.

The paper states this without the hypotheses $P \neq \emptyset$ and $d \ge 2$; both are needed:
$\mathrm{opx}(n, \emptyset, d) = 0$, and for $d = 1$ the interval $P = (0, 1)$ has
$\mathrm{opx}(n, P, 1) \le 1$, since a $P$-free open set $S$ has Lebesgue measure at most $1$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Corollary 5.8.

Stated but not proved: `MetaMathlibExt.opxD_open_isTheta` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 669](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L669). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-d-open-is-theta).

## Dilation bound for the d-dimensional continuous Turán number

Let $d$ be a natural
number, let $P \subseteq \mathbb{R}^d$ be finite and let $c_1, c_2, q, n$ be real numbers with
$c_1 > 0$, $q > 1$ and $n > 0$. Suppose that for every coordinate $i$ and all $p, p' \in P$ with
$p_i < p'_i$ such that no $r \in P$ has $p_i < r_i < p'_i$, we have
$c_1 \le p'_i - p_i \le c_2$. Let $qP = \{q p : p \in P\}$ and
$m = \lceil q c_2 / c_1 \rceil + 1$. Then the $d$-dimensional continuous Turán number
$\mathrm{opx}$ satisfies

$$
\mathrm{opx}(n, qP, d) \le
m^d \, \mathrm{opx}(\lceil \lceil n / c_1 \rceil / m \rceil \, c_1, P, d).
$$

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Lemma 5.10.

Stated but not proved: `MetaMathlibExt.opxD_dilate_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 682](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L682). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-d-dilate-le).

## Higher-dimensional continuous Turán numbers versus extremal functions

Let $d$ be a
natural number and let $P \subseteq \mathbb{R}^d$ be finite. Then the $d$-dimensional continuous
Turán number $\mathrm{opx}(n, P, d)$ and the $d$-dimensional 0-1 matrix extremal function
$\mathrm{ex}(n, M_P, d)$ of $P$ satisfy $\mathrm{opx}(n, P, d) = \Theta(\mathrm{ex}(n, M_P, d))$
as the natural number $n$ tends to infinity, with constants depending on $P$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Theorem 5.11.

Stated but not proved: `MetaMathlibExt.opxD_isTheta_patternExD` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 695](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L695). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-d-is-theta-pattern-ex-d).

## Upper bound for higher-dimensional permutation-type patterns

For every $d$ there is a
real number $C$ such that for every real $c > 0$ there is a real number $K$ with the following
property. Let $P \subseteq \mathbb{R}^d$ be a finite set of $k$ points such that, for each
coordinate $i$, distinct points of $P$ have distinct $i$-th coordinates and consecutive values of
the $i$-th coordinate on $P$ differ by at most $c$. Then
$\mathrm{opx}(n, P, d) \le K \cdot 2^{Ck} \cdot n^{d-1}$ for every natural number $n$, where
$n^{d-1}$ means $1$ when $d = 0$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Corollary 5.12.

Stated but not proved: `MetaMathlibExt.opxD_permutation_pattern_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 704](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L704). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-d-permutation-pattern-le).

## Upper bound for higher-dimensional grid patterns

Let $X_1, \dots, X_d$ be finite sets of
real numbers, $k_i = |X_i|$, and $P = X_1 \times \dots \times X_d \subseteq \mathbb{R}^d$. Put
$\alpha = \max_i k_i / \prod_i k_i$ if $d \ge 1$ and every $k_i$ is positive, and $\alpha = 0$
otherwise. Then $\mathrm{opx}(n, P, d) = O(n^{d - \alpha})$ as the natural number $n \to \infty$.

When some $k_i = 0$ the grid $P$ is empty and the bound reads $O(n^d)$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Corollary 5.13.

Stated but not proved: `MetaMathlibExt.opxD_grid_isBigO` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 717](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L717). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-d-grid-is-big-o).

## Power saving for continuous Turán numbers of finite patterns in $\mathbb{R}^d$

Let $d$
be a natural number and let $P \subseteq \mathbb{R}^d$ be finite. Then there is a real number
$\varepsilon > 0$ such that the $d$-dimensional continuous Turán number satisfies
$\mathrm{opx}(n, P, d) = O(n^{d - \varepsilon})$ as the natural number $n$ tends to infinity.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Corollary 5.14.

Stated but not proved: `MetaMathlibExt.exists_opxD_isBigO_rpow` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 727](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L727). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#exists-opx-d-is-big-o-rpow).

## Stacked permutation patterns in three dimensions

Let $P \subseteq \mathbb{R}^2$ be a
finite set of at least two points with pairwise distinct $x$-coordinates and pairwise distinct
$y$-coordinates, and for $i \in \{2, 3\}$ let
$P_i = \{(x, y, j) : (x, y) \in P,\ j \in \{1, \dots, i\}\} \subseteq \mathbb{R}^3$. Then, as $n$
tends to infinity through the natural numbers, $\mathrm{opx}(n, P_2, 3) = \Theta(n^{5/2})$ and
$\mathrm{opx}(n, P_3, 3) = \Theta(n^{8/3})$.

The requirement of at least two points is the paper's standing assumption on the permutation
matrix: for a single point, $P_2$ is two points on a vertical line and
$\mathrm{opx}(n, P_2, 3) \le n^2$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Corollary 5.15.

Stated but not proved: `MetaMathlibExt.opxD_permutation_stack_isTheta` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 739](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L739). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-d-permutation-stack-is-theta).

## Upper bound for continuous Turán numbers of stacked patterns

Let $d \ge 2$ and $t \ge 2$
be natural numbers and let $c > 0$. For $P \subseteq \mathbb{R}^d$ let
$Q_{P,t,c} = \{(x, ic) : x \in P,\ i \in \{1, \dots, t\}\} \subseteq \mathbb{R}^{d+1}$. Then there
is a real constant $K$, depending only on $d$, $t$ and $c$, such that for every
$P \subseteq \mathbb{R}^d$ and every real $n > 0$,
$\mathrm{opx}(n, Q_{P,t,c}, d + 1) \le
K \left(\mathrm{opx}(n, P, d)^{1/t} \, n^{d + 1 - d/t} + n^d\right)$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Theorem 5.16; `Q_{P,t,c}` as defined before it.

Stated but not proved: `MetaMathlibExt.opxD_stack_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 753](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L753). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-d-stack-le).

## Two-layer stacks of patterns with linear continuous Turán number

Let
$P \subseteq \mathbb{R}^2$ have at least two points, and suppose that
$\mathrm{opx}(n, P) = O(n)$ as the real number $n$ tends to infinity. Let $c > 0$ and
$Q_{P,2,c} = \{(x, y, z) : (x, y) \in P,\ z \in \{c, 2c\}\} \subseteq \mathbb{R}^3$. Then
$\mathrm{opx}(n, Q_{P,2,c}, 3) = \Theta(n^{5/2})$ as the real number $n$ tends to infinity.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Corollary 5.17, first sentence.

Stated but not proved: `MetaMathlibExt.opxD_stack_two_isTheta` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 764](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L764). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-d-stack-two-is-theta).

## Three-layer stacks of patterns with linear continuous Turán number

Let
$P \subseteq \mathbb{R}^2$ contain three points with pairwise distinct $x$-coordinates, and
suppose that $\mathrm{opx}(n, P) = O(n)$ as the real number $n$ tends to infinity. Let $c > 0$
and $Q_{P,3,c} = \{(x, y, z) : (x, y) \in P,\ z \in \{c, 2c, 3c\}\} \subseteq \mathbb{R}^3$. Then
$\mathrm{opx}(n, Q_{P,3,c}, 3) = \Theta(n^{8/3})$ as the real number $n$ tends to infinity.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Corollary 5.17, second sentence.

Stated but not proved: `MetaMathlibExt.opxD_stack_three_isTheta` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 775](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L775). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-d-stack-three-is-theta).

## Stacked graphs of increasing functions in three dimensions

Let $a > 0$, $b$ and $c > 0$
be real numbers and let $f : \mathbb{R} \to \mathbb{R}$ be strictly increasing on $[0, a]$ with
$(f(t) - f(s)) / (t - s) \le b$ whenever $0 \le s < t \le a$. Let
$P = \{(t, f(t)) : t \in [0, a]\}$ be the graph of $f$ over $[0, a]$ and, for $k \ge 1$, let
$Q_{P,k,c} = \{(x, y, ic) : (x, y) \in P,\ i \in \{1, \dots, k\}\} \subseteq \mathbb{R}^3$. Then,
as the real number $n \to \infty$, $\mathrm{opx}(n, Q_{P,2,c}, 3) = \Theta(n^{5/2})$ and
$\mathrm{opx}(n, Q_{P,3,c}, 3) = \Theta(n^{8/3})$.

The hypothesis $a > 0$ excludes the degenerate cases where the graph $P$ is a single point
($a = 0$) or empty ($a < 0$).

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Corollary 5.18.

Stated but not proved: `MetaMathlibExt.opxD_graph_stack_isTheta` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 787](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L787). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-d-graph-stack-is-theta).

## Stacked plus signs in three dimensions

Let $r > 0$ and $c > 0$, let
$P = \{(x, y) \in \mathbb{R}^2 : |x| \le r,\ |y| \le r,\ x = 0 \text{ or } y = 0\}$ be the plus
sign of size $r$, and for $t \in \{2, 3\}$ let
$Q_{P,t,c} = \{(x, y, ic) : (x, y) \in P,\ i \in \{1, \dots, t\}\} \subseteq \mathbb{R}^3$. Then,
as the real number $n$ tends to infinity, $\mathrm{opx}(n, Q_{P,2,c}, 3) = \Theta(n^{5/2})$ and
$\mathrm{opx}(n, Q_{P,3,c}, 3) = \Theta(n^{8/3})$.

The paper's size parameter $d$ is renamed $r$, and $r > 0$ is added: for $r = 0$, $Q_{P,2,c}$ is
two points on a vertical line and $\mathrm{opx}(n, Q_{P,2,c}, 3) \le c n^2$.

## Sources

- Jesse Geneson, *Continuous Turán Numbers*, INTEGERS 24 (2024), Article A1, Corollary 5.19.

Stated but not proved: `MetaMathlibExt.opxD_plus_stack_isTheta` is written with `theorem_wanted` in [WantedExt/Combinatorics/ContinuousTuranWanted.lean, line 802](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ContinuousTuranWanted.lean#L802). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html#opx-d-plus-stack-is-theta).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Continuous Turán numbers of planar patterns](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/discrete-geometry/part-01/continuous-tur-n-numbers-of-planar-patterns)
