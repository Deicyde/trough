---
declaration: section
origin: cited
lean: distanceMultiplicity, unitDistNum, distanceSet, distinctDistances, minimalDistinctDistances, distinctDistancesFrom, unitDistNum_le_choose_two, MathlibExt.Combinatorics.FavouriteDistancesFourSpaceErdosProblem754Wanted.favouriteDistanceCountHalfPlusConstant
statement: formalized
---

# Distinct and unit distances

29 results, 22 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html).

## Multiplicity of a distance

Let $P$ be a finite set of points in a metric space and let
$d$ be a real number. The multiplicity of $d$ in $P$ is the number of unordered pairs
$\{p, q\}$ of distinct points of $P$ with $\operatorname{dist}(p, q) = d$.

Formalized by `distanceMultiplicity`, a definition declared in [MathlibExt/Geometry/Metric.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Metric.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#distance-multiplicity).

## Number of unit distances

For a finite set $S$ of points in a metric space, the number of
unit distances of $S$ is the number of unordered pairs $\{p, q\}$ of points of $S$ with
$\operatorname{dist}(p, q) = 1$, that is, the multiplicity of the distance $1$ in $S$.

Formalized by `unitDistNum`, a definition declared in [MathlibExt/Geometry/Metric.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Metric.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#unit-dist-num).

## Distance set of a finite point set

For a finite set $P$ of points in a metric space,
the distance set of $P$ is the finite set of real numbers $\operatorname{dist}(p, q)$ with $p$
and $q$ distinct points of $P$.

Formalized by `distanceSet`, a definition declared in [MathlibExt/Geometry/Metric.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Metric.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#distance-set).

## Number of distinct distances

For a finite set $P$ of points in a metric space, the number
of distinct distances of $P$ is the number of elements of its distance set, that is, the number
of distinct values $\operatorname{dist}(p, q)$ with $p$ and $q$ distinct points of $P$.

Formalized by `distinctDistances`, a definition declared in [MathlibExt/Geometry/Metric.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Metric.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#distinct-distances).

## Minimum number of distinct distances

Let $X$ be a metric space and $n$ a natural number
such that $X$ contains a set of exactly $n$ points. The minimum number of distinct distances for
$n$ points in $X$ is the least number of distinct distances determined by a set of exactly $n$
points of $X$.

The hypothesis that some $n$-point set exists makes the minimum range over a nonempty
collection of sets.

Formalized by `minimalDistinctDistances`, a definition declared in [MathlibExt/Geometry/Metric.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Metric.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#minimal-distinct-distances).

## Number of distinct distances from a point

For a finite set $P$ of points in a metric
space and a point $x$ of the space, this is the number of distinct values
$\operatorname{dist}(y, x)$ with $y$ a point of $P$ other than $x$.

Formalized by `distinctDistancesFrom`, a definition declared in [MathlibExt/Geometry/Metric.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Metric.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#distinct-distances-from).

## Trivial upper bound on unit distances

For a finite set of $n$ points in a metric space,
the number of unit distances is at most $\binom{n}{2}$, the total number of unordered pairs of
distinct points.

Formalized by `unitDistNum_le_choose_two`, a theorem declared in [MathlibExt/Geometry/Metric.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Metric.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#unit-dist-num-le-choose-two).

## Statement of Erdős Problem 754

This is the statement that there is a real constant $C$
such that for every nonempty finite set $A$ of points of the Euclidean space $\mathbb{R}^4$ and
every natural number $f$, if for every $x \in A$ there is a real number $r > 0$ such that at least
$f$ points of $A$ lie at distance $r$ from $x$, then $f \le |A|/2 + C$. Equivalently,
$f(n) \le n/2 + O(1)$, where $f(n)$ is the largest $f$ such that some set $A$ of $n \ge 1$ points of
$\mathbb{R}^4$ has, for every $x \in A$, at least $f$ points of $A$ at one common distance
$r(x) > 0$ from $x$.

Formalized by `MathlibExt.Combinatorics.FavouriteDistancesFourSpaceErdosProblem754Wanted.favouriteDistanceCountHalfPlusConstant`, a definition declared in [WantedExt/Combinatorics/FavouriteDistancesFourSpaceErdosProblem754Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FavouriteDistancesFourSpaceErdosProblem754Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#favourite-distance-count-half-plus-const).

## Erdős Problem 754: favourite distances in $\mathbb{R}^4$

There is a real constant $C$ such
that for every nonempty finite set $A$ of points of the Euclidean space $\mathbb{R}^4$ and every
natural number $f$, if for every $x \in A$ there is a real number $r > 0$ such that at least $f$
points of $A$ lie at distance $r$ from $x$, then $f \le |A|/2 + C$.

Swanepoel proved that for every finite $A \subseteq \mathbb{R}^4$ with $|A| = n$ and every choice
of distances $r(x) > 0$, the number of pairs $(x, y)$ of points of $A$ with $|x - y| = r(x)$ is at
most $n^2/2 + O(n)$, which gives this bound.

## Sources

- T. F. Bloom, Erdős Problems, Problem #754, https://www.erdosproblems.com/754 (status PROVED (LEAN)); resolution: K. J. Swanepoel, Favourite distances in high dimensions, Thirty Essays on Geometric Graph Theory (2013), 499-519, abstract of arXiv:1108.4817: f_d(n) = max ∑_{x ∈ S} e_r(x, S) = (1 - 1/⌊d/2⌋) n² + Θ(n) for even d (n²/2 + O(n) for d = 4); erdosproblems.com/754: proved by Swanepoel (Avis, Erdős and Pach had n/2 + 2 ≤ f(n) ≤ (1 + o(1)) n/2), https://arxiv.org/abs/1108.4817.

Stated but not proved: `MathlibExt.Combinatorics.FavouriteDistancesFourSpaceErdosProblem754Wanted.favouriteDistanceCountHalfPlusConstant_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/FavouriteDistancesFourSpaceErdosProblem754Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FavouriteDistancesFourSpaceErdosProblem754Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#favourite-distance-count-half-plus-const-2).

## Statement of Erdős Problem 659

This is the statement that there is a real constant $C$
such that for every sufficiently large natural number $n$ there is a set $P$ of $n$ points of the
Euclidean plane $\mathbb{R}^2$ such that every $4$-element subset of $P$ determines at least $3$
distinct distances and $P$ determines at most $C n / \sqrt{\log n}$ distinct distances.

Formalized by `MathlibExt.Combinatorics.FewDistancesFourPointErdosProblem659Wanted.fewDistancesWithFourPointCondition`, a definition declared in [WantedExt/Combinatorics/FewDistancesFourPointErdosProblem659Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FewDistancesFourPointErdosProblem659Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#few-distances-with-four-point-condition).

## Erdős Problem 659: few distances with every four points spanning three

There is a real
constant $C$ such that for every sufficiently large natural number $n$ there is a set $P$ of $n$
points of the Euclidean plane $\mathbb{R}^2$ such that every $4$-element subset of $P$ determines
at least $3$ distinct distances and $P$ determines at most $C n / \sqrt{\log n}$ distinct
distances.

A suitable truncation of the lattice $\{(a, b\sqrt{2}) : a, b \in \mathbb{Z}\}$ has
$O(n / \sqrt{\log n})$ distinct distances (Moree and Osburn) and contains none of the six
four-point configurations that determine only two distances: five of them contain a square or an
equilateral triangle (Erdős–Fishburn, Lund–Sheffer), and the pentagon configuration is excluded by
Grayzel.

## Sources

- T. F. Bloom, Erdős Problems, Problem #659, https://www.erdosproblems.com/659 (status PROVED (LEAN)); resolution: B. Grayzel, Solution to a Problem of Erdős Concerning Distances and Points, arXiv:2601.09102 (2026); P. Moree and R. Osburn, Two-dimensional lattices with few distances, Enseign. Math. (2) 52 (2006), 361-380, abstract of arXiv:2601.09102: n-point sets taken from an m × m box of the lattice {(x, √2 y)} determine O(n / √(log n)) distinct distances (Bernays' theorem for u² + 2v²) and every 4 of their points determine at least 3 distances (Perucca's classification of the six two-distance 4-point configurations); erdosproblems.com/659 records the construction (Moree-Osburn, Lund-Sheffer) and the remaining pentagon case ruled out by Grayzel (using Gemini), 'thus giving a complete solution', https://arxiv.org/abs/2601.09102.

Stated but not proved: `MathlibExt.Combinatorics.FewDistancesFourPointErdosProblem659Wanted.fewDistancesWithFourPointCondition_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/FewDistancesFourPointErdosProblem659Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/FewDistancesFourPointErdosProblem659Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#few-distances-with-four-point-condition-2).

## Number of pairs at a given distance

For a finite set $P$ of points in $\mathbb{R}^3$ and a
real number $\delta$, this is the number of unordered pairs $\{p, q\}$ of distinct points
$p, q \in P$ with Euclidean distance $|p - q| = \delta$, computed as half the number of ordered
pairs $(p, q)$ of distinct points of $P$ at distance $\delta$ and taken as a real number.

Formalized by `MathlibExt.Combinatorics.SphereRepeatedDistancesErdosProblem605Wanted.pairsAtDistance`, a definition declared in [WantedExt/Combinatorics/SphereRepeatedDistancesErdosProblem605Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SphereRepeatedDistancesErdosProblem605Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#pairs-at-distance).

## Erdős Problem 605 (repeated distances on the sphere)

The proposition that there is a
function $f : \mathbb{N} \to \mathbb{R}$ with $f(n) \to \infty$ as $n \to \infty$ such that for
every $n \in \mathbb{N}$ there are a set $P$ of $n$ distinct points on the unit sphere
$\{x \in \mathbb{R}^3 : \|x\| = 1\}$ and a real number $\delta$ for which the number of unordered
pairs of distinct points of $P$ at distance $\delta$ is at least $f(n) \cdot n$.

Formalized by `MathlibExt.Combinatorics.SphereRepeatedDistancesErdosProblem605Wanted.sphereRepeatedDistanceSuperlinear`, a definition declared in [WantedExt/Combinatorics/SphereRepeatedDistancesErdosProblem605Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SphereRepeatedDistancesErdosProblem605Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#sphere-repeated-distance-superlinear).

## Erdős Problem 605 is true

There is a function $f : \mathbb{N} \to \mathbb{R}$ with
$f(n) \to \infty$ as $n \to \infty$ such that for every $n \in \mathbb{N}$ there are a set $P$ of
$n$ distinct points on the unit sphere $\{x \in \mathbb{R}^3 : \|x\| = 1\}$ and a real number
$\delta$ for which the number of unordered pairs of distinct points of $P$ at distance $\delta$
is at least $f(n) \cdot n$.

Erdős, Hickerson and Pach (Theorem 2(ii)) found an absolute constant $c > 0$ such that for every
$n$ there are $n$ points on the unit sphere each at distance $\sqrt{2}$ from at least
$c n^{1/3}$ others, hence at least $c n^{4/3} / 2$ pairs at distance $\sqrt{2}$;
erdosproblems.com/605 lists the problem as proved.

## Sources

- T. F. Bloom, Erdős Problems, Problem #605, https://www.erdosproblems.com/605 (status PROVED); resolution: P. Erdős, D. Hickerson and J. Pach, A problem of Leo Moser about repeated distances on the sphere, Amer. Math. Monthly (1989), 569-575, Theorem 2(ii): for every n there are n points on the unit sphere S² each at distance √2 from at least c₂ n^{1/3} others; Theorem 2(i): for every 0 < α < 2, n points each at distance α from at least c₁ log* n others, https://www.erdosproblems.com/605.

Stated but not proved: `MathlibExt.Combinatorics.SphereRepeatedDistancesErdosProblem605Wanted.sphereRepeatedDistanceSuperlinear_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/SphereRepeatedDistancesErdosProblem605Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SphereRepeatedDistancesErdosProblem605Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#sphere-repeated-distance-superlinear-hol).

## Unit distance count of a planar point set

For a finite set $P$ of points in the Euclidean
plane $\mathbb{R}^2$, the unit distance count of $P$ is the number of unordered pairs of points of
$P$ at distance exactly $1$.

The distance is the Euclidean one, $\sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2}$ for $x = (x_1, x_2)$ and
$y = (y_1, y_2)$, not the largest coordinate difference used by the product metric on
$\mathbb{R} \times \mathbb{R}$.

Formalized by `MathlibExt.Combinatorics.UnitDistanceConjectureFalseWanted.Combinatorics.unitDist`, an abbreviation declared in [WantedExt/Combinatorics/UnitDistanceConjectureFalseWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/UnitDistanceConjectureFalseWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#unit-dist).

## Erdős's unit distance conjecture is false

There is a real number $\delta > 0$ such that for
every natural number $N$ there are an integer $n \ge N$ and a set $P$ of exactly $n$ points in the
Euclidean plane $\mathbb{R}^2$ with at least $n^{1+\delta}$ unordered pairs of points of $P$ at
distance exactly $1$.

Because $C / \log \log n \to 0$ for every constant $C$, this contradicts Erdős's conjecture that
$n$ points in the plane determine at most $n^{1 + C / \log \log n}$ unit distances for some
constant $C$ and all large $n$.

## Sources

- OpenAI, *Planar Point Sets with Many Unit Distances*, 2026. https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-proof.pdf . Original conjecture: P. Erdős, *On sets of distances of n points*, Amer. Math. Monthly 53 (1946), 248-250. k-equidistant variant: P. Erdős, K. Falconer, *Some problems in combinatorial geometry*, 1997. Problem `erdos_unit_distance_conjecture_false` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.UnitDistanceConjectureFalseWanted.Combinatorics.erdos_unit_distance_conjecture_false` is written with `theorem_wanted` in [WantedExt/Combinatorics/UnitDistanceConjectureFalseWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/UnitDistanceConjectureFalseWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#erdos-unit-distance-conjecture-false).

## Number of unit-distance pairs in a planar point set

For a finite set $P$ of points in the
Euclidean plane $\mathbb{R}^2$, the number of unit-distance pairs of $P$ is the number of unordered
pairs of points of $P$ at distance exactly $1$.

The distance is the Euclidean one, $\sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2}$ for $x = (x_1, x_2)$ and
$y = (y_1, y_2)$, not the largest coordinate difference used by the product metric on
$\mathbb{R} \times \mathbb{R}$.

Formalized by `MathlibExt.Combinatorics.UnitDistanceUpperBoundWanted.Combinatorics.unitDist`, an abbreviation declared in [WantedExt/Combinatorics/UnitDistanceUpperBoundWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/UnitDistanceUpperBoundWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#unit-dist-2).

## Spencer–Szemerédi–Trotter unit distance bound

There is a constant $C > 0$ such that every
finite set of $n$ points in the Euclidean plane $\mathbb{R}^2$ has at most $C n^{4/3}$ unordered
pairs of points at distance exactly $1$.

## Sources

- J. Spencer, E. Szemerédi, W. T. Trotter Jr., *Unit distances in the Euclidean plane*, in Graph Theory and Combinatorics (Cambridge 1983), Academic Press, 1984. Short crossing-number proof: L. A. Székely, *Crossing numbers and hard Erdős problems in discrete geometry*, Combin. Probab. Comput. 6 (1997). Best constant: P. Ágoston, D. Pálvölgyi, *An improved constant factor for the unit distance problem*, Studia Sci. Math. Hungar. 59 (2022). Problem `unit_distance_upper_bound` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.UnitDistanceUpperBoundWanted.Combinatorics.unit_distance_upper_bound` is written with `theorem_wanted` in [WantedExt/Combinatorics/UnitDistanceUpperBoundWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/UnitDistanceUpperBoundWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#unit-distance-upper-bound).

## Euclidean plane for Erdős Problem 652

The real Euclidean plane is the space
$\mathbb{R}^2$ of pairs of real numbers with the Euclidean inner product and norm.

Formalized by `MathlibExt.Geometry.ErdosProblem652Wanted.Plane`, an abbreviation declared in [WantedExt/Geometry/ErdosProblem652Wanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ErdosProblem652Wanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#plane).

## Points with few distinct distances

For a finite set $X$ of points in the Euclidean plane
and a real number $t$, the number of points $x \in X$ such that the number of distinct distances
from $x$ to the other points of $X$ is less than $t$.

Formalized by `MathlibExt.Geometry.ErdosProblem652Wanted.countSmallPoints`, a definition declared in [WantedExt/Geometry/ErdosProblem652Wanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ErdosProblem652Wanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#count-small-points).

## Many points with few distinct distances

For natural numbers $n$, $k$ and a real number
$c$, the property that some set $X$ of exactly $n$ points in the Euclidean plane contains at
least $k$ points $x$ such that the number of distinct distances from $x$ to the other points of
$X$ is less than $c\sqrt{n}$.

For $1 \le k \le n$ this says that, with the points of $X$ ordered by this number, the $k$-th
smallest value is less than $c\sqrt{n}$.

Formalized by `MathlibExt.Geometry.ErdosProblem652Wanted.HasSmallKth`, a definition declared in [WantedExt/Geometry/ErdosProblem652Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ErdosProblem652Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#has-small-kth).

## Admissible constants in Erdős Problem 652

A real number $c$ is admissible for
$k \in \mathbb{N}$ if there is $N$ such that for every $n \ge N$ some set $X$ of exactly $n$
points in the Euclidean plane contains at least $k$ points $x$ such that the number of distinct
distances from $x$ to the other points of $X$ is less than $c\sqrt{n}$.

Formalized by `MathlibExt.Geometry.ErdosProblem652Wanted.isAdmissibleBound`, a definition declared in [WantedExt/Geometry/ErdosProblem652Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ErdosProblem652Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#is-admissible-bound).

## The Erdős constant $\alpha_k$

For $k \in \mathbb{N}$, $\alpha_k$ is the infimum of the
set of real numbers that are admissible for $k$: the reals $c$ for which there is $N$ such
that for every $n \ge N$ some set $X$ of exactly $n$ points in the Euclidean plane contains
at least $k$ points $x$ such that the number of distinct distances from $x$ to the other points
of $X$ is less than $c\sqrt{n}$. If this set is empty or unbounded below, $\alpha_k = 0$.

Formalized by `MathlibExt.Geometry.ErdosProblem652Wanted.erdosAlpha`, a definition declared in [WantedExt/Geometry/ErdosProblem652Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ErdosProblem652Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#erdos-alpha).

## Erdős Problem 652

For a finite set $X$ of points in the Euclidean plane and $x \in X$,
let $R_X(x)$ be the number of distinct distances from $x$ to the other points of $X$. For
$k \in \mathbb{N}$ let $\alpha_k$ be the infimum of the reals $c$ for which there is $N$ such
that for every $n \ge N$ some set $X$ of exactly $n$ points in the plane has at least $k$
points $x$ with $R_X(x) < c\sqrt{n}$ (an empty set or a set unbounded below is given infimum
$0$). The proposition is that $\alpha_k \to \infty$ as $k \to \infty$.

Formalized by `MathlibExt.Geometry.ErdosProblem652Wanted.conjecture`, a definition declared in [WantedExt/Geometry/ErdosProblem652Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ErdosProblem652Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#conjecture).

## Erdős Problem 652 is true

For a finite set $X$ of points in the Euclidean plane and
$x \in X$, let $R_X(x)$ be the number of distinct distances from $x$ to the other points of
$X$. For $k \in \mathbb{N}$ let $\alpha_k$ be the infimum of the reals $c$ for which there is
$N$ such that for every $n \ge N$ some set $X$ of exactly $n$ points in the plane has at least
$k$ points $x$ with $R_X(x) < c\sqrt{n}$ (an empty set or a set unbounded below is given
infimum $0$). Then $\alpha_k \to \infty$ as $k \to \infty$.

Mathialagan proved that for $2 \le m \le n^{1/3}$, some point of an $m$-point set determines
$\Omega(\sqrt{mn})$ distances to an $n$-point set; with Elekes's circle-grid construction this
gives $\alpha_k = \Theta(\sqrt{k})$.

## Sources

- S. Mathialagan, On bipartite distinct distances in the plane, Electronic Journal of Combinatorics 28(4) (2021) P4.33, arXiv:1912.01883, https://arxiv.org/abs/1912.01883.

Stated but not proved: `MathlibExt.Geometry.ErdosProblem652Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Geometry/ErdosProblem652Wanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ErdosProblem652Wanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#conjecture-holds).

## Rich distances

For a finite set $A$ of points in the Euclidean plane and a natural number
$k$, the rich distances of $A$ at level $k$ are the distances $d$ between two distinct points of
$A$ such that at least $k$ unordered pairs of distinct points of $A$ are at distance $d$.

Formalized by `MathlibExt.Geometry.ErdosProblem756Wanted.richDistances`, a definition declared in [WantedExt/Geometry/ErdosProblem756Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ErdosProblem756Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#rich-distances).

## Maximal number of rich distances

For a natural number $n$, this is the largest, over all
sets $A$ of $n$ points in the Euclidean plane, of the number of rich distances of $A$ at level
$n + 1$, that is, of distances that occur for at least $n + 1$ unordered pairs of distinct points
of $A$.

Formalized by `MathlibExt.Geometry.ErdosProblem756Wanted.maxRichDistances`, a definition declared in [WantedExt/Geometry/ErdosProblem756Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ErdosProblem756Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#max-rich-distances).

## Statement of Erdős Problem 756 on rich distances

For a finite set $A$ of points in the
Euclidean plane, call a distance $k$-rich for $A$ if at least $k$ unordered pairs of distinct points
of $A$ lie at that distance, and let $f(n)$ be the largest number of $(n+1)$-rich distances of a
set of $n$ points. This is the assertion that there is a constant $C$ with $n \le C f(n)$ for all
sufficiently large $n$; that for every $n$ there is a set of $n$ points with at least
$\lfloor n/4 \rfloor$ distances that are $(n+1)$-rich; and that for every $m \ge 1$ there is an
$N$ such that for every $n \ge N$ there is a set of $n$ points with at least
$\lfloor n/(2(m+1)) \rfloor$ distances that are $(n+m)$-rich.

Formalized by `MathlibExt.Geometry.ErdosProblem756Wanted.conjecture`, a definition declared in [WantedExt/Geometry/ErdosProblem756Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ErdosProblem756Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#conjecture-2).

## Bhowmick's theorem on rich distances

For a finite set $A$ of points in the Euclidean plane,
call a distance $k$-rich for $A$ if at least $k$ unordered pairs of distinct points of $A$ lie at
that distance, and let $f(n)$ be the largest number of $(n+1)$-rich distances of a set of $n$
points. Then there is a constant $C$ with $n \le C f(n)$ for all sufficiently large $n$; for every
$n$ there is a set of $n$ points with at least $\lfloor n/4 \rfloor$ distances that are
$(n+1)$-rich; and for every $m \ge 1$ there is an $N$ such that for every $n \ge N$ there is a set
of $n$ points with at least $\lfloor n/(2(m+1)) \rfloor$ distances that are $(n+m)$-rich.

## Sources

- K. Bhowmick, A problem of Erdős about rich distances, arXiv:2407.01174 (2024), https://arxiv.org/abs/2407.01174; External Lean proof of Erdős Problem 756, https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.29.1/ErdosProblems/Erdos756.lean.

Stated but not proved: `MathlibExt.Geometry.ErdosProblem756Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Geometry/ErdosProblem756Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ErdosProblem756Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html#conjecture-holds-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Distinct and unit distances](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/discrete-geometry/part-01/distinct-and-unit-distances)
