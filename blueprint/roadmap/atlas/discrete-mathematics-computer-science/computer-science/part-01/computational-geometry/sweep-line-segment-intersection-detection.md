---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Geometry.lineY, Cslib.Algorithms.Lean.Geometry.mem_segment_iff_lineY, Cslib.Algorithms.Lean.Geometry.direction_eq_lineY, Cslib.Algorithms.Lean.Geometry.exists_mem_inter_of_cross, Cslib.Algorithms.Lean.Geometry.exists_leftmost_mem_inter, Cslib.Algorithms.Lean.Geometry.pairwise_takeWhile_append_cons_dropWhile_lt, Cslib.Algorithms.Lean.Geometry.pairwise_takeWhile_append_cons_dropWhile_le, Cslib.Algorithms.Lean.Geometry.head?_dropWhile_eq_of_unique
statement: formalized
proof: formalized
---

# Sweep-line segment intersection detection

42 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html).

## Non-vertical segments as graphs

## Height of a line at an abscissa

For points $p = (p_1, p_2)$ and $q = (q_1, q_2)$ in $K^2$,
$K$ a field, and $x \in K$, this is $p_2 + (x - p_1)(q_2 - p_2)/(q_1 - p_1)$, with division by
zero read as $0$. When $p_1 \ne q_1$ it is the height at $x$ of the line through $p$ and $q$.

Formalized by `Cslib.Algorithms.Lean.Geometry.lineY`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#line-y).

## A non-vertical segment is the graph of its line

Let $p$ and $q$ be points of the plane
over a linearly ordered field, where a point $z$ has coordinates $(z_1, z_2)$, and suppose
$p_1 < q_1$. A point $z$ lies on the segment from $p$ to $q$ if and only if $p_1 \le z_1 \le q_1$
and $z_2$ is the height at abscissa $z_1$ of the line through $p$ and $q$.

Formalized by `Cslib.Algorithms.Lean.Geometry.mem_segment_iff_lineY`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#mem-segment-iff-line-y).

## DIRECTION as a scaled vertical offset

Let $\Bbbk$ be a field with a linear order, let
$p, q, r \in \Bbbk^2$, writing $p = (p_x, p_y)$ and likewise for $q$ and $r$, with $p_x < q_x$, and
let $y_{pq}(x)$ be the height at $x$ of the line through $p$ and $q$. Then
$\mathrm{DIRECTION}(p, q, r) = (q_x - p_x)\,(y_{pq}(r_x) - r_y)$.

Formalized by `Cslib.Algorithms.Lean.Geometry.direction_eq_lineY`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#direction-eq-line-y).

## Crossing of two non-vertical segments

Let $K$ be a linearly ordered field, write $z_1$ for
the first coordinate of a point $z \in K^2$, and let $[p, q]$ and $[p', q']$ be segments in $K^2$
with $p_1 < q_1$ and $p'_1 < q'_1$. For $t \in K$ let $y(t)$ be the height at $t$ of the line
through $p$ and $q$, and $y'(t)$ that of the line through $p'$ and $q'$. Let $a < b$ with
$p_1 \le a$, $p'_1 \le a$, $b \le q_1$ and $b \le q'_1$. If $y(a) < y'(a)$ and $y'(b) \le y(b)$,
then some $z \in [p, q] \cap [p', q']$ has $a < z_1 \le b$, and $z_1 < b$ if moreover
$y'(b) < y(b)$.

Formalized by `Cslib.Algorithms.Lean.Geometry.exists_mem_inter_of_cross`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#exists-mem-inter-of-cross).

## Leftmost point of the intersection of two segments

Let $K$ be a linearly ordered field,
write $x_1$ for the first coordinate of a point $x \in K^2$, and let $[p, q]$ and $[p', q']$ be
segments in $K^2$ with $p_1 < q_1$ and $p'_1 < q'_1$. If $[p, q] \cap [p', q']$ is nonempty, then
it contains a point $m$ with $m_1 \le w_1$ for every $w \in [p, q] \cap [p', q']$.

Formalized by `Cslib.Algorithms.Lean.Geometry.exists_leftmost_mem_inter`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#exists-leftmost-mem-inter).

## Inserting into a strictly sorted list

Let $f$ map a type $\alpha$ to a linearly ordered
set, let $T$ be a list over $\alpha$ with $f(j) < f(k)$ whenever $j$ occurs before $k$, let
$i \in \alpha$ be such that $f(j) \ne f(i)$ for every $j$ in $T$, and let $P$ be a predicate that
holds for an element $j$ of $T$ exactly when $f(j) < f(i)$. Insert $i$ just before the first
element of $T$ not satisfying $P$: the list made of the longest prefix of $T$ satisfying $P$, then
$i$, then the rest of $T$. In this list, $f(j) < f(k)$ whenever $j$ occurs before $k$.

Formalized by `Cslib.Algorithms.Lean.Geometry.pairwise_takeWhile_append_cons_dropWhile_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#pairwise-take-while-append-cons-drop-whi).

## Inserting into a weakly sorted list

Let $f$ map a type $\alpha$ to a linearly ordered
set, let $T$ be a list over $\alpha$ with $f(j) \le f(k)$ whenever $j$ occurs before $k$, let
$i \in \alpha$, and let $P$ be a predicate that holds for an element $j$ of $T$ exactly when
$f(j) < f(i)$. Insert $i$ just before the first element of $T$ not satisfying $P$: the list made
of the longest prefix of $T$ satisfying $P$, then $i$, then the rest of $T$. In this list,
$f(j) \le f(k)$ whenever $j$ occurs before $k$.

Formalized by `Cslib.Algorithms.Lean.Geometry.pairwise_takeWhile_append_cons_dropWhile_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#pairwise-take-while-append-cons-drop-whi-2).

## First element at or above a uniquely attained height

Let $f$ map a type to a linearly
ordered set, let $y$ be a value, and let $T$ be a list sorted non-strictly by $f$, that is,
$f(j) \le f(k)$ whenever $j$ occurs before $k$ in $T$. Suppose $b$ lies in $T$ with $f(b) = y$,
and every element $c \ne b$ of $T$ has $f(c) \ne y$. Then removing from $T$ its longest prefix of
elements $j$ with $f(j) < y$ leaves a list whose first element is $b$.

Formalized by `Cslib.Algorithms.Lean.Geometry.head?_dropWhile_eq_of_unique`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#head-drop-while-eq-of-unique).

## Splitting a list at two distinct members

If $a$ and $b$ are distinct members of a list
$T$, then there are elements $u$, $w$ with either $u = a$ and $w = b$, or $u = b$ and $w = a$, and
lists $A$, $M$, $B$ such that $T$ is the concatenation of $A$, the element $u$, $M$, the element
$w$ and $B$, in this order.

Formalized by `Cslib.Algorithms.Lean.Geometry.exists_append_of_mem_of_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#exists-append-of-mem-of-mem).

## Left endpoint of a segment

Let $K$ be a linearly ordered set and $S$ a family of segments
in $K^2$, segment $i$ being given by its two endpoints $(a, b)$ in either order. The left endpoint
of segment $i$ is $a$ if $a_1 \le b_1$ and $b$ otherwise, where $a_1$ and $b_1$ are the first
coordinates.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.left`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#left).

## Right endpoint of a segment

Write $z_1$ for the abscissa of a point $z$. If segment $i$
is given by the endpoints $u$ and $v$, in this order, its right endpoint is $v$ when
$u_1 \le v_1$ and $u$ otherwise.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.right`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#right).

## Sweep event

For $n$ segments indexed by $0, \dots, n-1$, an event is a pair $(i, b)$ of a
segment index $i$ and a Boolean $b$; it stands for the left endpoint of segment $i$ when $b$ is
true and for its right endpoint when $b$ is false.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.Event`, an abbreviation declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#event).

## Endpoint of an event

The point of the sweep event $(i, b)$ is the left endpoint of
segment $i$ when $b$ is true (a left-endpoint event) and the right endpoint of segment $i$ when
$b$ is false.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.point`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#point).

## Sweep order on endpoint events

Let $K$ be a linearly ordered set and $S$ a family of
segments in $K^2$, each given by its two endpoints. An endpoint event $e$ of $S$ standing for the
point $(x, y)$ gets the key $(x, \varepsilon, y)$, compared lexicographically, where
$\varepsilon = 0$ if $e$ is a left endpoint and $\varepsilon = 1$ if it is a right endpoint. So
events are ordered by $x$; at equal $x$, left endpoints come first; then by $y$. This is the
endpoint order of CLRS.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.key`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#key).

## Sorted sweep events

For $n$ segments, each given by its two endpoints, the left endpoint
of a segment is its endpoint with the smaller $x$-coordinate, or its first given endpoint when
both $x$-coordinates agree, and the right endpoint is the other one. The event list consists of
the $2n$ events, the left and the right endpoint of each segment, sorted by the $x$-coordinate
of the endpoint, with left endpoints before right endpoints at equal $x$, and then by the
$y$-coordinate of the endpoint; events that tie appear in increasing order of segment index.
This is line 2 of CLRS ANY-SEGMENTS-INTERSECT.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.events`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#events).

## Segment strictly below a point

For a segment $j$, write $l_j$ for its endpoint with the
smaller $x$-coordinate, or for its first given endpoint when both $x$-coordinates agree, and $r_j$
for its other endpoint. For a point $q$, segment $j$ is below $q$ when
$\mathrm{DIRECTION}(l_j, r_j, q) < 0$.

For a non-vertical segment this says that the line through $l_j$ and $r_j$ passes strictly below
$q$ at the abscissa of $q$.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.below`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#below).

## Intersection test for two input segments

Given $n$ segments in the plane over a
linearly ordered field, each given by its two endpoints, and indices $i, j < n$, this runs CLRS
`SEGMENTS-INTERSECT` on the left and right endpoints of segment $i$ and the left and right
endpoints of segment $j$. It returns that procedure's Boolean answer together with its cost in
`DIRECTION` and `ON-SEGMENT` evaluations.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.test`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#test).

## Testing a segment against an optional neighbour

Given a segment $i$ and possibly a
neighbour $j$, return the result of `SEGMENTS-INTERSECT` on segments $i$ and $j$, with its cost,
when $j$ is given, and return false at no cost when there is no neighbour.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.testOpt`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#test-opt).

## Testing the neighbours of a deleted segment

Given $n$ segments in the plane over a
linearly ordered field and two optional segment indices $a$ and $b$ (in the sweep, the segments
just below and just above a deleted segment, when they exist), this runs the intersection test
of segments $a$ and $b$ when both indices are present, and otherwise returns `false` at no
cost.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.testPair`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#test-pair).

## The any-segments-intersect sweep

CLRS `ANY-SEGMENTS-INTERSECT`, lines 3-11: the sweep
processes a list of events with a status list $T$ of segments ordered from bottom to top, returns
true as soon as an intersection test succeeds, and returns false once the events run out. At the
left endpoint $p$ of segment $i$, split $T$ as $A$ followed by $B$, where $A$ is the longest
initial part of $T$ whose segments pass strictly below $p$ by the `DIRECTION` test; this scan
costs $\min(|A| + 1, |T|)$, one `DIRECTION` per segment scanned. Segment $i$ is tested with
`SEGMENTS-INTERSECT` against the first segment of $B$ and then against the last segment of $A$
(when these exist), and the sweep continues with $A$, then $i$, then $B$. At the right endpoint
of segment $i$, with $A$ the part of $T$ before the first occurrence of $i$ and $B$ the part
after it, the last segment of $A$ is tested against the first segment of $B$ when both exist,
and the sweep continues with $A$ followed by $B$.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.sweep`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 394](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L394). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#sweep).

## One step of the sweep

A step takes an event and a status list $T$ of segments, ordered
from bottom to top, and returns a new status list, or no result when an intersection is reported.
At the left endpoint $p$ of segment $i$, split $T$ as $A$ followed by $B$, where $A$ is the longest
initial part of $T$ whose segments pass strictly below $p$ by the `DIRECTION` test. If
`SEGMENTS-INTERSECT` reports that $i$ meets the first segment of $B$ or the last segment of $A$
(when these exist), there is no result; otherwise the new status list is $A$, then $i$, then $B$.
At the right endpoint of segment $i$, let $A$ be the part of $T$ before the first occurrence of
$i$ and $B$ the part after it (so $A$ is all of $T$ and $B$ is empty when $i$ does not occur). If
both the last segment of $A$ and the first segment of $B$ exist and `SEGMENTS-INTERSECT` reports
that they meet, there is no result; otherwise the new status list is $A$ followed by $B$.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.step`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 408](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L408). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#step).

## Running the sweep over a list of events

Starting from a status list $T$, the sweep steps
are applied to the events in order, each to the status list left by the previous one. The result
is the final status list, or no result as soon as some step reports an intersection; on the empty
list of events the result is $T$.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.run`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#run).

## Left endpoint events precede right endpoint events

Let $K$ be a linearly ordered set
and $S$ a family of segments in $K^2$, each given by its two endpoints. For every segment $i$ of
$S$, the left endpoint event of $i$ is strictly smaller than its right endpoint event in the sweep
order on events (by $x$-coordinate, then left endpoints before right endpoints, then by
$y$-coordinate).

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.key_left_lt_right`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 485](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L485). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#key-left-lt-right).

## A sweep prefix with a right endpoint has its left endpoint

Let $K$ be a linearly ordered
set and $S$ a family of $n$ segments in $K^2$, each given by its two endpoints. If the sorted sweep
event list of $S$ is a list $P$ followed by a list $Q$, and $P$ contains the right endpoint event
of a segment $j$, then $P$ also contains the left endpoint event of $j$.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.left_mem_of_right_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 520](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L520). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#left-mem-of-right-mem).

## Splitting a list at the first occurrence of a member

If $i$ occurs in a list $T$ of
indices in $\{0, \dots, n-1\}$, then $T$ is the longest initial part of $T$ not containing $i$,
followed by $i$, followed by the part of $T$ after the first occurrence of $i$.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.takeWhile_append_cons_tail_dropWhile`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 552](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L552). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#take-while-append-cons-tail-drop-while).

## The sweep status holds the active segments

Let $P$ be an initial part of the sorted list
of events. If running the sweep over $P$ from the empty status list reports no intersection and
ends with status list $T$, then $T$ has no repeated entries, and a segment $j$ belongs to $T$
exactly when the left endpoint event of $j$ is in $P$ and the right endpoint event of $j$ is not.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.run_mem_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 571](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L571). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#run-mem-iff).

## Meeting segments

Let $K$ be a field with a linear order and $S$ a family of segments in
$K^2$, each given by its two endpoints. Segments $i$ and $j$ of $S$ meet when the closed segment
between the endpoints of $i$ and the closed segment between the endpoints of $j$ have a point in
common.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.Meets`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 629](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L629). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#meets).

## Neighbours on the sweep status are disjoint

Let $P$ be an initial part of the sorted list
of events. If running the sweep over $P$ from the empty status list reports no intersection and
ends with status list $T$, then no two consecutive segments of $T$ meet.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.run_isChain`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 640](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L640). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#run-is-chain).

## Soundness of the any-segments-intersect sweep

Let $S$ be a family of $n$ segments in
$K^2$, $K$ a linearly ordered field, and split the sorted list of their $2n$ endpoint events as
$P$ followed by $Q$. If running the sweep over $P$ from the empty status list succeeds with status
list $T$, and running it over $Q$ from $T$ reports an intersection, then there are two distinct
indices $i \ne j$ such that segments $i$ and $j$ meet.

In particular, when the sweep over all the events reports an intersection, two distinct segments
meet.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.exists_meets_of_run_eq_none`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 692](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L692). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#exists-meets-of-run-eq-none).

## The sweep order persists before the leftmost intersection

Let finitely many segments in
the plane over a linearly ordered field be given, where a point $z$ has coordinates $(z_1, z_2)$
and segment $j$ has left endpoint $l_j$ and right endpoint $r_j$ with $(l_j)_1 < (r_j)_1$. Write
$y_j(t)$ for the height at abscissa $t$ of the line through $l_j$ and $r_j$. Let $p_x$ be such
that every point shared by two distinct segments has abscissa at least $p_x$, let
$x \le x' < p_x$, and let $T$ be a list of segments such that $(l_j)_1 \le x$ and
$x' \le (r_j)_1$ for every $j$ in $T$. If $y_j(x) < y_k(x)$ whenever $j$ occurs before $k$ in
$T$, then $y_j(x') < y_k(x')$ whenever $j$ occurs before $k$ in $T$.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.pairwise_lt_of_pairwise_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 760](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L760). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#pairwise-lt-of-pairwise-lt).

## The sweep order holds weakly at the leftmost intersection

Let finitely many segments in
the plane over a linearly ordered field be given, where a point $z$ has coordinates $(z_1, z_2)$
and segment $j$ has left endpoint $l_j$ and right endpoint $r_j$ with $(l_j)_1 < (r_j)_1$. Write
$y_j(t)$ for the height at abscissa $t$ of the line through $l_j$ and $r_j$. Let $p_x$ be such
that every point shared by two distinct segments has abscissa at least $p_x$, let $x < p_x$, and
let $T$ be a list of segments such that $(l_j)_1 \le x$ and $p_x \le (r_j)_1$ for every $j$ in
$T$. If $y_j(x) < y_k(x)$ whenever $j$ occurs before $k$ in $T$, then $y_j(p_x) \le y_k(p_x)$
whenever $j$ occurs before $k$ in $T$.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.pairwise_le_of_pairwise_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 775](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L775). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#pairwise-le-of-pairwise-lt).

## Phase one: the status list is strictly sorted between the processed and remaining events

Fix a number $p_x$ in the field of coordinates. Suppose no segment is vertical (each segment's
left endpoint has smaller $x$-coordinate than its right endpoint) and every point common to two
distinct segments has $x$-coordinate at least $p_x$. Split the sorted list of events as $P$
followed by $Q$, where the endpoint of every event of $P$ has $x$-coordinate less than $p_x$, and
suppose running the sweep over $P$ from the empty status list reports no intersection and ends
with status list $T$. Let $x < p_x$ be at least the $x$-coordinate of the endpoint of every event
of $P$ and at most that of every event of $Q$. Then whenever segment $j$ comes before segment $k$
in $T$, the height at $x$ of the line through the endpoints of $j$ is less than that of the line
through the endpoints of $k$.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.run_pairwise_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 795](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L795). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#run-pairwise-lt).

## The status list is weakly sorted after the events left of a vertical line

Fix a number
$p_x$ in the field of coordinates. Suppose no segment is vertical (each segment's left endpoint
has smaller $x$-coordinate than its right endpoint) and every point common to two distinct
segments has $x$-coordinate at least $p_x$. Split the sorted list of events as $P$ followed by
$Q$, where the endpoint of every event of $P$ has $x$-coordinate less than $p_x$ and that of every
event of $Q$ has $x$-coordinate at least $p_x$. If running the sweep over $P$ from the empty
status list reports no intersection and ends with status list $T$, then whenever segment $j$
comes before segment $k$ in $T$, the height at $p_x$ of the line through the endpoints of $j$ is
at most that of the line through the endpoints of $k$.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.run_pairwise_le_of_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 892](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L892). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#run-pairwise-le-of-lt).

## Phase two: inserting left endpoints on a vertical line keeps the status weakly sorted

Fix a number $p_x$ in the field of coordinates. Suppose no segment is vertical (each segment's
left endpoint has smaller $x$-coordinate than its right endpoint) and every point common to two
distinct segments has $x$-coordinate at least $p_x$. Split the sorted list of events as $P_1$,
then $P_2$, then $Q$, where the endpoint of every event of $P_1$ has $x$-coordinate less than
$p_x$, every event of $P_2$ is a left endpoint with $x$-coordinate equal to $p_x$, and the
endpoint of every event of $Q$ has $x$-coordinate at least $p_x$. If running the sweep over $P_1$
followed by $P_2$ from the empty status list reports no intersection and ends with status list
$T$, then whenever segment $j$ comes before segment $k$ in $T$, the height at $p_x$ of the line
through the endpoints of $j$ is at most that of the line through the endpoints of $k$.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.run_pairwise_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 922](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L922). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#run-pairwise-le).

## Sweep completeness when the leftmost intersection is inside both segments

Let $n$
segments in the plane over a linearly ordered field be given, where $z_1$ is the abscissa of a
point $z$ and segment $i$ has left endpoint $l_i$ and right endpoint $r_i$ with
$(l_i)_1 < (r_i)_1$, and suppose no point lies on three distinct segments. Let $a \ne b$ be
segments that share a point $p$ such that every point shared by two distinct segments has
abscissa at least $p_1$, and suppose $(l_a)_1 < p_1$ and $(l_b)_1 < p_1$. Then the sweep, run on
the sorted list of endpoint events from the empty status list, reports an intersection.

Just before the sweep line reaches $p$, the segments $a$ and $b$ are neighbours on the status
list, so they were tested.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.run_eq_none_of_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 965](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L965). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#run-eq-none-of-lt).

## Sweep completeness when the leftmost intersection is a left endpoint

Let $n$ segments in
the plane over a linearly ordered field be given, where $z_1$ is the abscissa of a point $z$ and
segment $i$ has left endpoint $l_i$ and right endpoint $r_i$ with $(l_i)_1 < (r_i)_1$, and
suppose no point lies on three distinct segments. Let $a \ne b$ be segments such that $l_a$ lies
on segment $b$ and every point shared by two distinct segments has abscissa at least $(l_a)_1$.
If the left endpoint of $b$ comes before the left endpoint of $a$ in the sorted list of endpoint
events, then the sweep, run on that list from the empty status list, reports an intersection.

Inserting $a$ places it right next to $b$, so the two are tested.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.run_eq_none_of_left`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 1061](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L1061). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#run-eq-none-of-left).

## A leftmost intersection point

Let $\Bbbk$ be a linearly ordered field, let
$s_0, \dots, s_{n-1}$ be closed segments in $\Bbbk^2$, none of them vertical, and write $z_x$ for
the $x$-coordinate of a point $z$. If some $s_i$ and $s_j$ with $i \ne j$ meet, then there are
indices $a \ne b$ and a point $p \in s_a \cap s_b$ such that $p_x \le z_x$ for all indices
$k \ne l$ and every point $z \in s_k \cap s_l$.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.exists_leftmost_meet`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 1165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L1165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#exists-leftmost-meet).

## Completeness of the segment-intersection sweep

Let $n$ segments in the plane over a
linearly ordered field be given, none of them vertical (the left endpoint of each has strictly
smaller abscissa than its right endpoint), and assume, as CLRS does, that no point lies on three
distinct segments. If two distinct segments meet, then the sweep, run on the sorted list of
endpoint events from the empty status list, reports an intersection.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.run_eq_none_of_meets`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 1194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L1194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#run-eq-none-of-meets).

## Cost charged to a sweep event

For $n$ segments, the charge of an event is $n + 16$ if it
is the left endpoint of a segment and $8$ if it is the right endpoint of a segment.

These charges bound the actual costs: a left endpoint scans at most $n$ segments of the status
list and runs two SEGMENTS-INTERSECT tests, and a right endpoint runs one test.

Formalized by `Cslib.Algorithms.Lean.Geometry.AnySegments.eventCost`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 1262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L1262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#event-cost).

## ANY-SEGMENTS-INTERSECT

Let $\Bbbk$ be a linearly ordered field. Given $n$ segments
$s_0, \dots, s_{n-1}$ in $\Bbbk^2$, each given by its two endpoints, write $l_t$, the left endpoint
of $s_t$, for its endpoint with the smaller $x$-coordinate, or for its first given endpoint when
both $x$-coordinates agree, and $r_t$, the right endpoint, for the other one. The procedure sorts
the $2n$ endpoints by $x$-coordinate, left endpoints before right endpoints at equal $x$, then by
$y$-coordinate, with remaining ties in increasing order of segment index. It then sweeps a
vertical line across them, starting with an empty status list of segments, kept from bottom to
top. At the left endpoint $l_i$ of $s_i$, let $P$ be the longest initial part of the status list
consisting of segments $s_t$ with $\mathrm{DIRECTION}(l_t, r_t, l_i) < 0$. Then $s_i$ is tested
with SEGMENTS-INTERSECT first against the segment just after $P$ and then against the last
segment of $P$, when these exist, and is inserted directly after $P$. At the right endpoint of
$s_i$, the segments just before and just after $s_i$ in the status list, when both exist, are
tested against each other and $s_i$ is deleted. The procedure returns true as soon as a test
succeeds and false after the last event. Cost counts one unit per evaluation of DIRECTION or
ON-SEGMENT (CLRS, third edition, Section 33.2).

The status is kept in a list rather than CLRS's red-black tree.

Formalized by `Cslib.Algorithms.Lean.Geometry.anySegmentsIntersect`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 1321](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L1321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#any-segments-intersect).

## Correctness of ANY-SEGMENTS-INTERSECT

Let $\Bbbk$ be a linearly ordered field and let
$s_0, \dots, s_{n-1}$ be closed segments in $\Bbbk^2$, each given by its two endpoints in either
order. Suppose no segment is vertical (its two endpoints have different $x$-coordinates) and no
point lies on three segments $s_i$, $s_j$, $s_k$ with $i$, $j$, $k$ pairwise distinct. Then
ANY-SEGMENTS-INTERSECT returns true on these segments if and only if there are indices $i \ne j$
such that $s_i$ and $s_j$ intersect (CLRS, third edition, Theorem 33.1).

Formalized by `Cslib.Algorithms.Lean.Geometry.anySegmentsIntersect_ret_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 1328](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L1328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#any-segments-intersect-ret-eq-true-iff).

## Running time of ANY-SEGMENTS-INTERSECT

Let $\Bbbk$ be a field with a linear order. For
every $n$ segments in $\Bbbk^2$, each given by its two endpoints, ANY-SEGMENTS-INTERSECT costs at
most $n^2 + 24n$, so it runs in time $O(n^2)$. Cost counts one unit per evaluation of DIRECTION
or ON-SEGMENT.

The bound comes from at most $n$ DIRECTION evaluations to place each segment in the list-based
status and at most three SEGMENTS-INTERSECT tests per segment.

Formalized by `Cslib.Algorithms.Lean.Geometry.anySegmentsIntersect_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean, line 1353](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Geometry/AnySegmentsIntersect.lean#L1353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html#any-segments-intersect-time-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sweep-line segment intersection detection](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/computational-geometry/sweep-line-segment-intersection-detection)
