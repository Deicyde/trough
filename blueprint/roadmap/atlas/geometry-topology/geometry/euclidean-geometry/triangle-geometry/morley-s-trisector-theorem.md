---
declaration: section
origin: cited
lean: MathlibExt.Geometry.MorleyWanted.Geometry.Morley.Plane, MathlibExt.Geometry.MorleyWanted.Geometry.Morley.IsEquilateralTriple, MathlibExt.Geometry.MorleyWanted.Geometry.Morley.LiesInTriangle, MathlibExt.Geometry.MorleyWanted.Geometry.Morley.IsMorleyConfiguration, MathlibExt.Geometry.MorleyWanted.Geometry.Morley.morley_theorem
statement: formalized
---

# Morley's trisector theorem

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/morley-s-trisector-theorem/index.html).

## Euclidean plane for Morley's theorem

The Euclidean plane $\mathbb{R}^2$ with its
standard Euclidean distance.

Formalized by `MathlibExt.Geometry.MorleyWanted.Geometry.Morley.Plane`, an abbreviation declared in [WantedExt/Geometry/MorleyWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/MorleyWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/morley-s-trisector-theorem/index.html#plane).

## Equilateral triple of points

Three points $P$, $Q$, $R$ of the Euclidean plane form an
equilateral triple when, writing $d$ for the Euclidean distance, $d(P, Q) = d(Q, R)$ and
$d(Q, R) = d(R, P)$. Coincident points are allowed, so $P = Q = R$ qualifies.

Formalized by `MathlibExt.Geometry.MorleyWanted.Geometry.Morley.IsEquilateralTriple`, a definition declared in [WantedExt/Geometry/MorleyWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/MorleyWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/morley-s-trisector-theorem/index.html#is-equilateral-triple).

## Point in a closed triangle

A point $X$ of the Euclidean plane lies in the triangle with
vertices $A$, $B$, $C$ when $X$ belongs to the convex hull of $\{A, B, C\}$, the closed triangle
$ABC$ (a segment or a point when $A$, $B$, $C$ are collinear).

Formalized by `MathlibExt.Geometry.MorleyWanted.Geometry.Morley.LiesInTriangle`, a definition declared in [WantedExt/Geometry/MorleyWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/MorleyWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/morley-s-trisector-theorem/index.html#lies-in-triangle).

## Morley configuration

Points $A$, $B$, $C$, $P$, $Q$, $R$ of the Euclidean plane form a
Morley configuration when $A$, $B$, $C$ are not collinear, each of $P$, $Q$, $R$ lies in the
closed triangle $ABC$, and, writing $\angle XYZ \in [0, \pi]$ for the unoriented angle at $Y$,
$0 < \angle CAR = \angle RAP = \angle PAB$ and $3 \angle PAB = \angle CAB$;
$0 < \angle ABP = \angle PBQ = \angle QBC$ and $3 \angle QBC = \angle ABC$;
$0 < \angle BCQ = \angle QCR = \angle RCA$ and $3 \angle RCA = \angle BCA$.
Thus $P$, $Q$, $R$ are the intersections of adjacent angle trisectors of the triangle $ABC$.

Formalized by `MathlibExt.Geometry.MorleyWanted.Geometry.Morley.IsMorleyConfiguration`, a definition declared in [WantedExt/Geometry/MorleyWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/MorleyWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/morley-s-trisector-theorem/index.html#is-morley-configuration).

## Morley's trisector theorem

If points $A$, $B$, $C$, $P$, $Q$, $R$ of the Euclidean plane
form a Morley configuration, so that $ABC$ is a nondegenerate triangle and $P$, $Q$, $R$ are the
intersections of its adjacent angle trisectors, then $P$, $Q$, $R$ form an equilateral triple:
writing $d$ for the Euclidean distance, $d(P, Q) = d(Q, R)$ and $d(Q, R) = d(R, P)$.

## Sources

- F. Morley (c. 1899). Knill, §162. Problem `morley_theorem` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.MorleyWanted.Geometry.Morley.morley_theorem` is written with `theorem_wanted` in [WantedExt/Geometry/MorleyWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/MorleyWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/morley-s-trisector-theorem/index.html#morley-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Morley's trisector theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/morley-s-trisector-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/euclidean-geometry/triangle-geometry/morley-s-trisector-theorem)
