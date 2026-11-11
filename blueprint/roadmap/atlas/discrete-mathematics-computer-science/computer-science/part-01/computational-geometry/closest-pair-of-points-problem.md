---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Geometry.dist2, Cslib.Algorithms.Lean.Geometry.IsMinPairDist2, Cslib.Algorithms.Lean.Geometry.minDistFrom, Cslib.Algorithms.Lean.Geometry.bruteMin, Cslib.Algorithms.Lean.Geometry.scanFrom, Cslib.Algorithms.Lean.Geometry.stripScan, Cslib.Algorithms.Lean.Geometry.closestRec, Cslib.Algorithms.Lean.Geometry.closestPair
statement: formalized
proof: formalized
---

# Closest pair of points problem

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html).

## Squared distance in the plane

Let $K$ be a linearly ordered field. The squared distance
between points $p = (p_1, p_2)$ and $q = (q_1, q_2)$ of $K^2$ is $(p_1 - q_1)^2 + (p_2 - q_2)^2$.

Formalized by `Cslib.Algorithms.Lean.Geometry.dist2`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#dist2).

## Least pairwise squared distance

Let $K$ be a linearly ordered field, and write
$d(p, q) = (p_1 - q_1)^2 + (p_2 - q_2)^2$ for the squared distance between points
$p = (p_1, p_2)$ and $q = (q_1, q_2)$ of $K^2$. For a list $c_1, \dots, c_n$ of points of $K^2$,
an element $\delta$ of $K$ is the least pairwise squared distance of the list when
$\delta = d(c_i, c_j)$ for some $i < j$ and $\delta \le d(c_i, c_j)$ for all $i < j$.

Formalized by `Cslib.Algorithms.Lean.Geometry.IsMinPairDist2`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#is-min-pair-dist2).

## Least squared distance from a point to a list

Let $K$ be a linearly ordered field, and
write $d(p, q) = (p_1 - q_1)^2 + (p_2 - q_2)^2$ for the squared distance between points
$p = (p_1, p_2)$ and $q = (q_1, q_2)$ of $K^2$. For a point $p$ and a list $c_1, \dots, c_m$ of
points of $K^2$, the least squared distance from $p$ to the list is no value if $m = 0$ and
$\min_{1 \le k \le m} d(p, c_k)$ otherwise. Computing it is charged one unit of cost per point of
the list, $m$ units in total.

Formalized by `Cslib.Algorithms.Lean.Geometry.minDistFrom`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#min-dist-from).

## Brute-force closest pair

Let $K$ be a field with a linear order, and write
$d(p, q) = (x - x')^2 + (y - y')^2$ for the squared distance between points $p = (x, y)$ and
$q = (x', y')$ of $K^2$. On a list $c_1, \dots, c_n$ of points in $K^2$, the brute-force scan
returns no value if $n < 2$, and otherwise returns $\min_{i < j} d(c_i, c_j)$: for each $i$ it
computes the least squared distance from $c_i$ to the later points $c_{i+1}, \dots, c_n$, and
takes the least of these minima. It is charged one unit of cost per squared distance computed.

Formalized by `Cslib.Algorithms.Lean.Geometry.bruteMin`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#brute-min).

## Strip scan from a point

Let $K$ be a linearly ordered field, and write
$d(p, q) = (p_1 - q_1)^2 + (p_2 - q_2)^2$ for the squared distance between points
$p = (p_1, p_2)$ and $q = (q_1, q_2)$ of $K^2$. Let $\delta \in K$, let $p = (p_1, p_2)$ be a
point of $K^2$ and $c_1, \dots, c_m$ a list of points $c_l = (x_l, y_l)$ of $K^2$, and let
$k \le m$ be largest such that $(y_l - p_2)^2 < \delta$ for all $1 \le l \le k$. The scan from $p$
with threshold $\delta$ returns no value if $k = 0$ and $\min_{1 \le l \le k} d(p, c_l)$
otherwise. It is charged one unit of cost per point $c_1, \dots, c_k$: it stops at the first
point whose squared vertical gap to $p$ is at least $\delta$, without computing its distance.

Formalized by `Cslib.Algorithms.Lean.Geometry.scanFrom`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#scan-from).

## Closest-pair strip scan

Let $K$ be a linearly ordered field, $\delta \in K$ and
$c_1, \dots, c_n$ a list of points of $K^2$. For each $i$, the strip scan runs the strip scan from
$c_i$ with threshold $\delta$ on the later points $c_{i+1}, \dots, c_n$. It returns the least of
the values these scans return, or no value if none of them returns a value, and its cost is the
sum of their costs.

Formalized by `Cslib.Algorithms.Lean.Geometry.stripScan`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#strip-scan).

## Closest-pair recursion

Let $K$ be a linearly ordered field and $c_1, \dots, c_n$ a list
of points $c_i = (x_i, y_i)$ of $K^2$. If $n \le 3$, the recursion returns the brute-force scan of
the list. Otherwise let $m = \lfloor n/2 \rfloor$, and run the recursion on $c_1, \dots, c_m$ and
on $c_{m+1}, \dots, c_n$. If neither call returns a value, it returns no value. Otherwise let
$\delta$ be the least of the returned values, let $T$ be the list of the points $c_i$ with
$(x_i - x_m)^2 < \delta$ in their original order, sorted by second coordinate with a stable merge
sort, and run the strip scan with threshold $\delta$ on $T$. The recursion returns
$\min(\delta, s)$ if the strip scan returns a value $s$, and $\delta$ otherwise. In the base case
its cost is that of the brute-force scan; otherwise it is the sum of the costs of the two
recursive calls and of the strip scan when it is run, and splitting, filtering and sorting are
free.

Formalized by `Cslib.Algorithms.Lean.Geometry.closestRec`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#closest-rec).

## Divide-and-conquer closest pair

Let $K$ be a field with a linear order. Given a list of
points in $K^2$, the closest-pair algorithm sorts the points by first coordinate (merge sort, at
no cost) and runs the closest-pair recursion on the sorted list. It returns a squared distance or
no value, and is charged one unit of cost per squared distance computed.

This is CLRS `CLOSEST-PAIR` (Section 33.4), with distances compared squared.

Formalized by `Cslib.Algorithms.Lean.Geometry.closestPair`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#closest-pair).

## Closest-pair answer

Let $K$ be a linearly ordered field, and write
$d(p, q) = (p_1 - q_1)^2 + (p_2 - q_2)^2$ for the squared distance between points
$p = (p_1, p_2)$ and $q = (q_1, q_2)$ of $K^2$. For a list $c_1, \dots, c_n$ of points of $K^2$,
an optional value $r$ (an element of $K$ or no value) is an answer for the list when every value
$\delta$ that $r$ holds equals $d(c_i, c_j)$ for some $i < j$, and when for all $i < j$, $r$ holds
a value $\delta$ with $\delta \le d(c_i, c_j)$.

Formalized by `Cslib.Algorithms.Lean.Geometry.IsAnswer`, a structure declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#is-answer).

## The nearest-point scan returns the least squared distance

Let $K$ be a linearly ordered
field, write $d(u, v) = (x - x')^2 + (y - y')^2$ for the squared distance between points
$u = (x, y)$ and $v = (x', y')$ of $K^2$, let $p \in K^2$, and let $qs$ be a list of points in
$K^2$. If the scan for the least squared distance from $p$ to the entries of $qs$ returns a value
$\delta$, then $\delta = d(p, q)$ for some entry $q$ of $qs$. For every entry $q$ of $qs$, the
scan returns a value $\delta$ with $\delta \le d(p, q)$.

Formalized by `Cslib.Algorithms.Lean.Geometry.minDistFrom_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#min-dist-from-spec).

## The strip scan bounds every pair with a small vertical gap

Let $K$ be a linearly ordered
field, write $d(p, q) = (x - x')^2 + (y - y')^2$ for the squared distance between points
$p = (x, y)$ and $q = (x', y')$ of $K^2$, and let $\delta \in K$. Let $ys$ be a list of points in
$K^2$ sorted by second coordinate: whenever an entry precedes another, its second coordinate is at
most the other's. If $a = (a_1, a_2)$ and $b = (b_1, b_2)$ are entries of $ys$ at positions $i < j$
respectively and $(b_2 - a_2)^2 < \delta$, then the strip scan with threshold $\delta$ on $ys$
returns a value $e$ with $e \le d(a, b)$.

Formalized by `Cslib.Algorithms.Lean.Geometry.stripScan_lower`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#strip-scan-lower).

## The closest-pair recursion is correct on lists sorted by first coordinate

Let $K$ be a
linearly ordered field, write $d(u, v) = (x - x')^2 + (y - y')^2$ for the squared distance between
points $u = (x, y)$ and $v = (x', y')$ of $K^2$, and let $xs$ be a list of points in $K^2$ sorted
by first coordinate: whenever an entry precedes another, its first coordinate is at most the
other's. If the closest-pair recursion returns a value $\delta$ on $xs$, then $\delta = d(p, q)$
for some entries $p$, $q$ of $xs$ at different positions. For any two entries $p$, $q$ of $xs$ at
different positions, the recursion returns a value $\delta$ with $\delta \le d(p, q)$.

Formalized by `Cslib.Algorithms.Lean.Geometry.closestRec_isAnswer`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#closest-rec-is-answer).

## The closest-pair algorithm returns the answer

Let $K$ be a linearly ordered field, write
$d(p, q) = (x - x')^2 + (y - y')^2$ for the squared distance between points $p = (x, y)$ and
$q = (x', y')$ of $K^2$, and let $ps$ be a list of points in $K^2$. If the divide-and-conquer
closest-pair algorithm returns a value $\delta$ on $ps$, then $\delta = d(p, q)$ for some entries
$p$, $q$ of $ps$ at different positions. For any two entries $p$, $q$ of $ps$ at different
positions, the algorithm returns a value $\delta$ with $\delta \le d(p, q)$.

Formalized by `Cslib.Algorithms.Lean.Geometry.closestPair_isAnswer`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean, line 462](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean#L462). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#closest-pair-is-answer).

## Correctness of divide-and-conquer closest pair

Let $K$ be a linearly ordered field and let
$ps$ be a list of at least two points in $K^2$. Then the divide-and-conquer closest-pair algorithm
returns a value $\delta$, and $\delta$ is the least squared distance between two entries of $ps$
at different positions: some two entries at different positions have squared distance $\delta$,
and any two entries at different positions have squared distance at least $\delta$.

This is the correctness of CLRS Section 33.4, with distances compared squared.

Formalized by `Cslib.Algorithms.Lean.Geometry.closestPair_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean, line 471](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean#L471). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#closest-pair-spec).

## The closest-pair algorithm returns no value exactly on fewer than two points

Let $K$ be a
linearly ordered field. For every list of points in $K^2$, the divide-and-conquer closest-pair
algorithm returns no value if and only if the list has fewer than two entries.

Formalized by `Cslib.Algorithms.Lean.Geometry.closestPair_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean, line 480](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean#L480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#closest-pair-eq-none-iff).

## Divide and conquer agrees with brute force

Let $K$ be a linearly ordered field. For every
list of points in $K^2$, the divide-and-conquer closest-pair algorithm returns the same value as
the brute-force scan (their costs may differ).

Formalized by `Cslib.Algorithms.Lean.Geometry.closestPair_eq_bruteMin`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean, line 498](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean#L498). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#closest-pair-eq-brute-min).

## Cost of the brute-force closest-pair scan

Let $K$ be a field with a linear order and let
$ps$ be a list of $n$ points in $K^2$. Counting one unit of cost per squared distance computed,
twice the cost of the brute-force scan on $ps$ equals $n(n-1)$; that is, the scan computes exactly
$n(n-1)/2$ squared distances.

Formalized by `Cslib.Algorithms.Lean.Geometry.bruteMin_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean, line 515](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPair.lean#L515). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#brute-min-time).

## Side-tagged points

A tagged point is a pair $(p, s)$ of a point $p \in \mathbb{R}^2$ and a
Boolean $s$, read as the side of the dividing line on which $p$ lies: false for left, true for
right.

Formalized by `Cslib.Algorithms.Lean.Geometry.Tagged`, an abbreviation declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPairTime.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPairTime.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#tagged).

## Same-side points far apart

For a real $\delta$, two tagged points $a$ and $b$ are
same-side far apart when, if $a$ and $b$ carry the same side, the squared distance between their
points is at least $\delta$.

Formalized by `Cslib.Algorithms.Lean.Geometry.SameSideFar`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPairTime.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPairTime.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#same-side-far).

## Strip points

Given reals $\delta$ and $x_{\mathrm{mid}}$, a tagged point $((x, y), s)$ lies
in the strip when $(x - x_{\mathrm{mid}})^2 < \delta$, and moreover $x \le x_{\mathrm{mid}}$ if its
side $s$ is left ($s$ false) and $x_{\mathrm{mid}} \le x$ if its side $s$ is right ($s$ true).

Formalized by `Cslib.Algorithms.Lean.Geometry.InStrip`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPairTime.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPairTime.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#in-strip).

## Packing bound for the strip

Let $\delta$ and $x_{\mathrm{mid}}$ be reals, $p$ a tagged
point, $Z$ a list of tagged points, and $L$ the list $p$ followed by $Z$; write $y_a$ for the
$y$-coordinate of a tagged point $a$. Suppose every point of $L$ lies in the strip for $\delta$ and
$x_{\mathrm{mid}}$, any two points of $L$ at different positions with the same side are at squared
distance at least $\delta$, and every point $a$ of $Z$ satisfies $y_p \le y_a$ and
$(y_a - y_p)^2 < \delta$. Then $Z$ has at most $7$ entries.

## Sources

- CLRS, third edition, Section 33.4, the packing argument.

Formalized by `Cslib.Algorithms.Lean.Geometry.length_le_seven`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPairTime.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPairTime.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#length-le-seven).

## Cost of the scan from one strip point

Let $\delta$ be a real, $q = (q_1, q_2)$ a point of
$\mathbb{R}^2$ and $L$ a list of points of $\mathbb{R}^2$. The cost of the scan from $q$ over $L$
with threshold $\delta$, one unit per squared distance computed, equals the length of the longest
initial segment of $L$ all of whose points $r = (r_1, r_2)$ satisfy $(r_2 - q_2)^2 < \delta$.

Formalized by `Cslib.Algorithms.Lean.Geometry.scanFrom_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPairTime.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPairTime.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#scan-from-time).

## Cost of the strip scan

Let $\delta$ and $x_{\mathrm{mid}}$ be reals and $Y$ a list of
tagged points that is sorted by nondecreasing $y$-coordinate, whose points all lie in the strip for
$\delta$ and $x_{\mathrm{mid}}$, and in which any two points at different positions with the same
side are at squared distance at least $\delta$. Then the strip scan with parameter $\delta$ over the
underlying points of $Y$ (tags forgotten) computes at most $7m$ squared distances, where $m$ is the
length of $Y$.

Formalized by `Cslib.Algorithms.Lean.Geometry.stripScan_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPairTime.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPairTime.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#strip-scan-time-le).

## Running time of the closest-pair recursion

For every list of $n$ points in $\mathbb{R}^2$
sorted by nondecreasing $x$-coordinate, the divide-and-conquer recursion of the closest-pair
algorithm computes at most $7 n \lceil \log_2 n \rceil + n$ squared distances, where
$\lceil \log_2 0 \rceil$ is read as $0$.

Formalized by `Cslib.Algorithms.Lean.Geometry.closestRec_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPairTime.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPairTime.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#closest-rec-time-le).

## Running time of the closest-pair algorithm

For every list of $n$ points in $\mathbb{R}^2$,
the closest-pair algorithm computes at most $7 n \lceil \log_2 n \rceil + n$ squared distances,
where $\lceil \log_2 0 \rceil$ is read as $0$. In particular it computes $O(n \log n)$ distances.

## Sources

- CLRS, third edition, Section 33.4.

Formalized by `Cslib.Algorithms.Lean.Geometry.closestPair_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/ClosestPairTime.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/ClosestPairTime.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html#closest-pair-time-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Closest pair of points problem](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/computational-geometry/closest-pair-of-points-problem)
