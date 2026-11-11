---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Geometry.cross, Cslib.Algorithms.Lean.Geometry.direction, Cslib.Algorithms.Lean.Geometry.onSegment, Cslib.Algorithms.Lean.Geometry.Straddles, Cslib.Algorithms.Lean.Geometry.collinearBranch, Cslib.Algorithms.Lean.Geometry.segmentsIntersect, Cslib.Algorithms.Lean.Geometry.segmentsIntersect_time, Cslib.Algorithms.Lean.Geometry.segmentsIntersect_ret
statement: formalized
proof: formalized
---

# Orientation and segment intersection tests

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html).

## Cross product of plane vectors

For $p = (x_p, y_p)$ and $q = (x_q, y_q)$ in $K^2$, where
$K$ is a linearly ordered field, the cross product is $p \times q = x_p y_q - x_q y_p$ (CLRS
equation (33.1)).

Formalized by `Cslib.Algorithms.Lean.Geometry.cross`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html#cross).

## Direction of three points

For points $p_i, p_j, p_k \in K^2$, where $K$ is a linearly
ordered field, CLRS's DIRECTION$(p_i, p_j, p_k)$ is the cross product
$(p_k - p_i) \times (p_j - p_i)$.

It is positive when $p_k$ is clockwise from $p_j$ about $p_i$, negative when counterclockwise, and
zero when the three points are collinear.

Formalized by `Cslib.Algorithms.Lean.Geometry.direction`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html#direction).

## The ON-SEGMENT test

For points $p_i = (x_i, y_i)$, $p_j = (x_j, y_j)$ and
$p_k = (x_k, y_k)$ in $K^2$, where $K$ is a linearly ordered field, CLRS's
ON-SEGMENT$(p_i, p_j, p_k)$ is the Boolean that is true exactly when $p_k$ lies in the bounding box
of $p_i$ and $p_j$, that is, $\min(x_i, x_j) \le x_k \le \max(x_i, x_j)$ and
$\min(y_i, y_j) \le y_k \le \max(y_i, y_j)$.

Formalized by `Cslib.Algorithms.Lean.Geometry.onSegment`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html#on-segment).

## Values of opposite sign

Two elements $d$ and $e$ of a field with a linear order straddle
zero when $d > 0$ and $e < 0$, or $d < 0$ and $e > 0$; that is, $d$ and $e$ are nonzero with
opposite signs.

Formalized by `Cslib.Algorithms.Lean.Geometry.Straddles`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html#straddles).

## Collinear-endpoint step of SEGMENTS-INTERSECT

Let $K$ be a linearly ordered field,
$d \in K$ and $p_i, p_j, p_k \in K^2$. When $d = 0$, this step costs one unit and returns the value
of ON-SEGMENT$(p_i, p_j, p_k)$; when $d \neq 0$, it costs nothing and returns false.

In SEGMENTS-INTERSECT, $d$ is the direction of $p_k$ relative to $p_i$ and $p_j$.

Formalized by `Cslib.Algorithms.Lean.Geometry.collinearBranch`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html#collinear-branch).

## The SEGMENTS-INTERSECT procedure

Let $K$ be a field with a linear order and let
$p_1, p_2, p_3, p_4 \in K^2$. CLRS's procedure SEGMENTS-INTERSECT$(p_1, p_2, p_3, p_4)$, which
tests whether the segments $p_1p_2$ and $p_3p_4$ meet, first computes, at a cost of $4$, the
directions $d_1 = \mathrm{DIRECTION}(p_3, p_4, p_1)$, $d_2 = \mathrm{DIRECTION}(p_3, p_4, p_2)$,
$d_3 = \mathrm{DIRECTION}(p_1, p_2, p_3)$ and $d_4 = \mathrm{DIRECTION}(p_1, p_2, p_4)$. If $d_1$
and $d_2$ are nonzero with opposite signs and so are $d_3$ and $d_4$, it returns true. Otherwise
it tries in order the cases $d_1 = 0$ with ON-SEGMENT$(p_3, p_4, p_1)$, $d_2 = 0$ with
ON-SEGMENT$(p_3, p_4, p_2)$, $d_3 = 0$ with ON-SEGMENT$(p_1, p_2, p_3)$, and $d_4 = 0$ with
ON-SEGMENT$(p_1, p_2, p_4)$: in each case it runs the ON-SEGMENT test, at a cost of $1$, only when
the direction is $0$, and it returns true as soon as a test succeeds. If none succeeds it returns
false.

Formalized by `Cslib.Algorithms.Lean.Geometry.segmentsIntersect`, a definition declared in [CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html#segments-intersect).

## Running time of SEGMENTS-INTERSECT

Let $K$ be a field with a linear order and let
$p_1, p_2, p_3, p_4 \in K^2$. In the cost model that charges one unit per DIRECTION computation
and one per ON-SEGMENT test, SEGMENTS-INTERSECT$(p_1, p_2, p_3, p_4)$ costs at least $4$ and at
most $8$.

The four directions are always computed, and at most four ON-SEGMENT tests run.

Formalized by `Cslib.Algorithms.Lean.Geometry.segmentsIntersect_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html#segments-intersect-time).

## SEGMENTS-INTERSECT as a Boolean formula

Let $K$ be a field with a linear order, let
$p_1, p_2, p_3, p_4 \in K^2$, and write $d_1 = \mathrm{DIRECTION}(p_3, p_4, p_1)$,
$d_2 = \mathrm{DIRECTION}(p_3, p_4, p_2)$, $d_3 = \mathrm{DIRECTION}(p_1, p_2, p_3)$ and
$d_4 = \mathrm{DIRECTION}(p_1, p_2, p_4)$. The value returned by
SEGMENTS-INTERSECT$(p_1, p_2, p_3, p_4)$ is true if and only if at least one of the following
holds: $d_1$ and $d_2$ are nonzero with opposite signs and $d_3$ and $d_4$ are nonzero with
opposite signs; $d_1 = 0$ and ON-SEGMENT$(p_3, p_4, p_1)$ is true; $d_2 = 0$ and
ON-SEGMENT$(p_3, p_4, p_2)$ is true; $d_3 = 0$ and ON-SEGMENT$(p_1, p_2, p_3)$ is true; or
$d_4 = 0$ and ON-SEGMENT$(p_1, p_2, p_4)$ is true.

Formalized by `Cslib.Algorithms.Lean.Geometry.segmentsIntersect_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html#segments-intersect-ret).

## Points of a segment lie in its bounding box

Let $K$ be a linearly ordered field and
$p, q, r \in K^2$. If $r$ lies on the closed segment from $p$ to $q$, then ON-SEGMENT$(p, q, r)$ is
true, that is, $r$ lies in the bounding box of $p$ and $q$.

Formalized by `Cslib.Algorithms.Lean.Geometry.onSegment_of_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html#on-segment-of-mem).

## Points of a segment have direction zero

Let $K$ be a linearly ordered field and
$p, q, r \in K^2$. If $r$ lies on the closed segment from $p$ to $q$, then the direction
$(r - p) \times (q - p)$ is zero, that is, $r$ is collinear with $p$ and $q$.

Formalized by `Cslib.Algorithms.Lean.Geometry.direction_eq_zero_of_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html#direction-eq-zero-of-mem).

## A collinear point in the bounding box lies on the segment

Let $K$ be a linearly ordered
field, write $(u_1, u_2) \times (v_1, v_2) = u_1 v_2 - v_1 u_2$ for the cross product on $K^2$, and
let $p, q, r \in K^2$. If $r$ is collinear with $p$ and $q$, that is, the direction
$(r - p) \times (q - p)$ is zero, and ON-SEGMENT$(p, q, r)$ is true, that is, $r$ lies in the
bounding box of $p$ and $q$, then $r$ lies on the closed segment from $p$ to $q$.

This is the fact behind CLRS's use of ON-SEGMENT.

Formalized by `Cslib.Algorithms.Lean.Geometry.mem_segment_of_direction_eq_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html#mem-segment-of-direction-eq-zero).

## Values of opposite sign have nonzero difference

If $d$ and $e$ are elements of a
linearly ordered field that straddle zero, that is, they are nonzero with opposite signs, then
$d - e \ne 0$.

Formalized by `Cslib.Algorithms.Lean.Geometry.Straddles.sub_ne_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html#sub-ne-zero).

## Zero-crossing parameter of values of opposite sign

If $d$ and $e$ are elements of a
linearly ordered field that straddle zero, that is, they are nonzero with opposite signs, then
$0 \le d / (d - e) \le 1$.

Formalized by `Cslib.Algorithms.Lean.Geometry.Straddles.param_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html#param-mem).

## A vanishing convex combination of nonzero values forces opposite signs

Let $d$ and $e$ be
nonzero elements of a linearly ordered field. If $a d + b e = 0$ for some $a, b \ge 0$ in the field
with $a + b = 1$, then $d$ and $e$ have opposite signs.

Formalized by `Cslib.Algorithms.Lean.Geometry.straddles_of_combo`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html#straddles-of-combo).

## Properly crossing segments meet

Let $K$ be a linearly ordered field and
$p_1, p_2, p_3, p_4 \in K^2$. Suppose the directions $(p_1 - p_3) \times (p_4 - p_3)$ and
$(p_2 - p_3) \times (p_4 - p_3)$ are nonzero with opposite signs, and so are
$(p_3 - p_1) \times (p_2 - p_1)$ and $(p_4 - p_1) \times (p_2 - p_1)$. Then the closed segments
$p_1 p_2$ and $p_3 p_4$ have a common point.

Formalized by `Cslib.Algorithms.Lean.Geometry.inter_nonempty_of_straddles`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html#inter-nonempty-of-straddles).

## Points with direction zero lie on the line

Let $K$ be a linearly ordered field and
$p, q, r \in K^2$ with $p \neq q$. If $(r - p) \times (q - p) = 0$, then $r = p + \mu (q - p)$ for
some $\mu \in K$.

One can take $\mu = \frac{(r - p) \cdot (q - p)}{(q - p) \cdot (q - p)}$, a quotient of dot
products.

Formalized by `Cslib.Algorithms.Lean.Geometry.eq_param_of_direction_eq_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html#eq-param-of-direction-eq-zero).

## Collinear case of segment intersection

Let $K$ be a linearly ordered field and
$p_1, p_2, p_3, p_4 \in K^2$. Suppose the directions $(p_1 - p_3) \times (p_4 - p_3)$ and
$(p_2 - p_3) \times (p_4 - p_3)$ are both zero and the closed segments $p_1 p_2$ and $p_3 p_4$
have a common point. Then $p_1$ or $p_2$ lies on the segment $p_3 p_4$, or $p_3$ or $p_4$ lies on
the segment $p_1 p_2$.

Formalized by `Cslib.Algorithms.Lean.Geometry.endpoint_mem_of_collinear`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html#endpoint-mem-of-collinear).

## Meeting segments cross properly or an endpoint lies on the other

Let $K$ be a linearly
ordered field and $p_1, p_2, p_3, p_4 \in K^2$, and suppose the closed segments $[p_1, p_2]$ and
$[p_3, p_4]$ have a common point. Then either $\mathrm{DIRECTION}(p_3, p_4, p_1)$ and
$\mathrm{DIRECTION}(p_3, p_4, p_2)$ are nonzero with opposite signs and
$\mathrm{DIRECTION}(p_1, p_2, p_3)$ and $\mathrm{DIRECTION}(p_1, p_2, p_4)$ are nonzero with
opposite signs, or $p_1 \in [p_3, p_4]$, or $p_2 \in [p_3, p_4]$, or $p_3 \in [p_1, p_2]$, or
$p_4 \in [p_1, p_2]$.

Formalized by `Cslib.Algorithms.Lean.Geometry.straddles_or_endpoint_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html#straddles-or-endpoint-mem).

## Correctness of SEGMENTS-INTERSECT

Let $K$ be a linearly ordered field and let
$p_1, p_2, p_3, p_4 \in K^2$. The procedure SEGMENTS-INTERSECT$(p_1, p_2, p_3, p_4)$ returns true
if and only if the closed segments $[p_1, p_2]$ and $[p_3, p_4]$ have a common point.

## Sources

- CLRS Section 33.1.

Formalized by `Cslib.Algorithms.Lean.Geometry.segmentsIntersect_ret_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Geometry/SegmentIntersection.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html#segments-intersect-ret-eq-true-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Orientation and segment intersection tests](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/computational-geometry/orientation-and-segment-intersection-tests)
