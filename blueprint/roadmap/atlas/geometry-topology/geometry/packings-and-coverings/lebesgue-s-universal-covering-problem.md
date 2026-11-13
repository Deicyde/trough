---
declaration: section
origin: cited
lean: MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.Plane, MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.IsUnitDiameterConvexSet, MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.CoversCongruentCopy, MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.IsUniversalConvexCover, MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.planarArea, MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.admissibleCoverAreas, MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.lebesgueUniversalCoveringConstant, MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.directionalWidth
statement: formalized
---

# Lebesgue's universal covering problem

35 results, 22 proved and 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html).

## The Euclidean plane of Lebesgue's covering problem

The ambient space is the Euclidean
plane $\mathbb{R}^2$, with the Euclidean distance.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.Plane`, an abbreviation declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#plane).

## Convex sets of diameter one

A set $K$ in the Euclidean plane $\mathbb{R}^2$ is a
unit-diameter convex set when it is nonempty and convex and its diameter
$\sup_{x, y \in K} \lVert x - y \rVert$ is exactly $1$.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.IsUnitDiameterConvexSet`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#is-unit-diameter-convex-set).

## Covering a congruent copy

A planar set $\Omega$ covers a congruent copy of a planar set
$K$ when some isometry $e$ of the plane onto itself satisfies $e(K) \subseteq \Omega$.

Isometries include reflections.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.CoversCongruentCopy`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#covers-congruent-copy).

## Universal convex covers

A set $\Omega$ in the Euclidean plane $\mathbb{R}^2$ is a universal
convex cover when it is nonempty and convex and, for every nonempty convex set
$K \subseteq \mathbb{R}^2$ of diameter $1$, some isometry $e$ of the plane onto itself satisfies
$e(K) \subseteq \Omega$.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.IsUniversalConvexCover`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#is-universal-convex-cover).

## Planar area

The area of a set $S$ in the Euclidean plane $\mathbb{R}^2$
is its Lebesgue measure (outer measure if $S$ is not measurable), a value in $[0, \infty]$,
so infinite area is allowed.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.planarArea`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#planar-area).

## Areas of universal convex covers

The set of admissible cover areas is the set of all
$a \in [0, \infty]$ for which there is a universal convex cover $\Omega$ in the plane (a nonempty
convex set containing a congruent copy of every nonempty convex planar set of diameter $1$) whose
Lebesgue area is $a$.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.admissibleCoverAreas`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#admissible-cover-areas).

## Lebesgue universal covering constant

Call a set $\Omega$ in the Euclidean plane
$\mathbb{R}^2$ a universal convex cover if it is nonempty and convex and, for every nonempty
convex set $K \subseteq \mathbb{R}^2$ of diameter exactly $1$, some isometry of the plane onto
itself maps $K$ into $\Omega$. The Lebesgue universal covering constant is the infimum, taken in
$[0, \infty]$, of the Lebesgue areas of all universal convex covers; the infimum of an empty
family would be $\infty$.

The definition does not assume that a universal convex cover of minimal area exists.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.lebesgueUniversalCoveringConstant`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#lebesgue-universal-covering-constant).

## Directional width

For a planar set $K$ and a vector $u$ in the plane, the width of $K$
in direction $u$ is $\sup_{x \in K} \langle u, x \rangle - \inf_{x \in K} \langle u, x \rangle$,
where the supremum and infimum are taken in $\mathbb{R}$, with the convention that each is $0$
when the set of values $\langle u, x \rangle$ is empty or unbounded on that side.

It is only applied to nonempty compact $K$, where both extrema are attained.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.directionalWidth`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#directional-width).

## Sets of constant width one

A set $K$ in the Euclidean plane $\mathbb{R}^2$ has constant
width $1$ when it is nonempty, compact and convex and, for every unit vector $u$, its width in
direction $u$, namely $\sup_{x \in K} \langle u, x \rangle - \inf_{x \in K} \langle u, x \rangle$,
equals $1$.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.IsConstantWidthOne`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#is-constant-width-one).

## Statement of the existence of a minimal universal convex cover

This proposition states
that some nonempty convex set $\Omega$ in the Euclidean plane $\mathbb{R}^2$ is a universal convex
cover, that is, for every nonempty convex set $K \subseteq \mathbb{R}^2$ of diameter $1$ some
isometry $e$ of the plane onto itself satisfies $e(K) \subseteq \Omega$, and that the area (planar
Lebesgue measure) of $\Omega$ equals the Lebesgue universal covering constant, the infimum of the
areas of all universal convex covers.

The existence of such a cover follows from the Blaschke selection theorem.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.elekes1994MinimalCoverExists`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#elekes1994-minimal-cover-exists).

## Covering sets of constant width one suffices (statement)

The proposition that every
nonempty convex subset $\Omega$ of the Euclidean plane that contains a congruent copy of every
nonempty compact convex planar set of constant width $1$ is a universal convex cover, that is,
contains a congruent copy of every nonempty convex planar set of diameter $1$.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.vrecica1981ConstantWidthOneSuffices`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#vrecica1981-constant-width-one-suffices).

## Jung's upper bound for Lebesgue's universal covering constant (statement)

The proposition
that Lebesgue's universal covering constant is at most $\pi/3$.

This is the bound given by Jung's theorem: a closed disk of radius $1/\sqrt{3}$, of area $\pi/3$,
contains a translate of every planar set of diameter $1$.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.trivialJungElekes1994UpperBound`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#trivial-jung-elekes1994-upper-bound).

## Statement of Pál's hexagon bound

The proposition that the Lebesgue universal covering
constant is at most $\sqrt{3}/2$, the bound given by Pál's regular hexagon.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.pal1920HexagonUpperBound`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#pal1920-hexagon-upper-bound).

## Statement of Pál's truncated hexagon bound

The proposition that the Lebesgue universal
covering constant is at most $2 - 2/\sqrt{3}$, the bound given by Pál's truncated hexagon.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.pal1920TruncatedHexagonUpperBound`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#pal1920-truncated-hexagon-upper-bound).

## Statement of Sprague's bound

The proposition that the Lebesgue universal covering
constant is at most $0.844137708436$.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.sprague1936UpperBound`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#sprague1936-upper-bound).

## Statement of Hansen's corrected upper bound

This proposition states that the Lebesgue
universal covering constant, the infimum of the areas of the nonempty convex sets in the Euclidean
plane that contain a congruent copy of every nonempty convex planar set of diameter $1$, is at most
$0.844137708398$.

This is Hansen's finite-decimal upper bound, as corrected by Baez, Bagdasaryan and Gibbs.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.hansen1992CorrectedBBG2015UpperBound`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#hansen1992-corrected-bbg2015-upper-bound).

## Statement of the Baez–Bagdasaryan–Gibbs upper bound

This is the proposition that there
is a real number $b$ with $0.844115297128419059 \le b < 0.844115297128419060$ such that the
Lebesgue universal covering constant (the infimum of the areas of universal convex covers) is at
most $b$.

The 18 printed digits are a truncation of the bound, not its exact value.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.bbg2015ApproximateUpperBound`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#bbg2015-approximate-upper-bound).

## Statement of Gibbs's upper bound

This proposition states that the Lebesgue universal
covering constant, the infimum of the areas of the nonempty convex sets in the Euclidean plane that
contain a congruent copy of every nonempty convex planar set of diameter $1$, is at most
$0.8440935944$.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.gibbs2018UpperBound`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#gibbs2018-upper-bound).

## Disk lower bound for Lebesgue's universal covering constant (statement)

The proposition
that Lebesgue's universal covering constant is at least $\pi/4$.

This is the bound given by a disk of radius $1/2$, which has diameter $1$ and area $\pi/4$.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.trivialUnitDiskLowerBound`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#trivial-unit-disk-lower-bound).

## Statement of Elekes's disk-and-triangle lower bound

This is the proposition that the
Lebesgue universal covering constant (the infimum of the areas of universal convex covers) is at
least $0.8257$.

The bound comes from simultaneously covering a disk and an equilateral triangle of diameter $1$.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.elekes1994DiskTriangleLowerBound`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#elekes1994-disk-triangle-lower-bound).

## Statement of Elekes's regular-polygon lower bound

This proposition states that the Lebesgue
universal covering constant, the infimum of the areas of the nonempty convex sets in the Euclidean
plane that contain a congruent copy of every nonempty convex planar set of diameter $1$, is at
least $0.8271$.

This is Elekes's finite-decimal lower bound, obtained using regular $3^j$-gons as well.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.elekes1994RegularPolygonLowerBound`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#elekes1994-regular-polygon-lower-bound).

## Statement of the Brass–Sharifi lower bound

This is the proposition that the Lebesgue
universal covering constant (the infimum of the areas of universal convex covers) is at least
$0.832$.

Brass and Sharifi obtained this bound by a rigorous computer-aided argument.

Formalized by `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.brassSharifi2005LowerBound`, a definition declared in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#brass-sharifi2005-lower-bound).

## Existence of a minimal universal cover

There is a universal convex cover $\Omega$ (a
nonempty convex planar set containing a congruent copy of every nonempty convex planar set of
diameter $1$) whose Lebesgue area equals the Lebesgue universal covering constant, the infimum of
the areas of all universal convex covers.

## Sources

- Elekes, Generalized breadths, circular Cantor sets, and the least area UCC (1994).

Stated but not proved: `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.elekes1994MinimalCoverExists_holds` is written with `theorem_wanted` in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#elekes1994-minimal-cover-exists-holds).

## Covering sets of constant width one suffices

Let $\Omega$ be a nonempty convex subset of
the Euclidean plane that contains a congruent copy (an image under an isometry of the plane,
reflections allowed) of every nonempty compact convex planar set of constant width $1$. Then
$\Omega$ contains a congruent copy of every nonempty convex planar set of diameter $1$, that is,
$\Omega$ is a universal convex cover.

## Sources

- Vrećica, A note on sets of constant width (1981).

Stated but not proved: `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.vrecica1981ConstantWidthOneSuffices_holds` is written with `theorem_wanted` in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#vrecica1981-constant-width-one-suffices-2).

## Jung's bound for the Lebesgue covering problem

The Lebesgue universal covering constant
is at most $\pi/3$.

## Sources

- Jung's theorem, quoted in Elekes (1994), catalogue constant 13b.

Stated but not proved: `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.trivialJungElekes1994UpperBound_holds` is written with `theorem_wanted` in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#trivial-jung-elekes1994-upper-bound-hold).

## Pál's hexagon bound

The Lebesgue universal covering constant is at most $\sqrt{3}/2$.

## Sources

- Pál, Über ein elementares Variationsproblem (1920), hexagon bound.

Stated but not proved: `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.pal1920HexagonUpperBound_holds` is written with `theorem_wanted` in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#pal1920-hexagon-upper-bound-holds).

## Pál's truncated hexagon bound

The Lebesgue universal covering constant is at most
$2 - 2/\sqrt{3}$.

## Sources

- Pál, Über ein elementares Variationsproblem (1920), truncated hexagon bound.

Stated but not proved: `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.pal1920TruncatedHexagonUpperBound_holds` is written with `theorem_wanted` in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#pal1920-truncated-hexagon-upper-bound-ho).

## Sprague's bound

The Lebesgue universal covering constant is at most $0.844137708436$.

## Sources

- Sprague, Über ein elementares Variationsproblem (1936).

Stated but not proved: `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.sprague1936UpperBound_holds` is written with `theorem_wanted` in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#sprague1936-upper-bound-holds).

## Hansen's upper bound for Lebesgue's covering problem, as corrected

The Lebesgue universal
covering constant, the infimum of the areas of the nonempty convex sets in the Euclidean plane that
contain a congruent copy of every nonempty convex planar set of diameter $1$, is at most
$0.844137708398$.

## Sources

- Hansen (1992), corrected in Baez, Bagdasaryan and Gibbs (2015).

Stated but not proved: `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.hansen1992CorrectedBBG2015UpperBound_holds` is written with `theorem_wanted` in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#hansen1992-corrected-bbg2015-upper-bound-2).

## Baez–Bagdasaryan–Gibbs upper bound

There is a real number $b$ with
$0.844115297128419059 \le b < 0.844115297128419060$ such that the Lebesgue universal covering
constant (the infimum of the areas of universal convex covers) is at most $b$.

## Sources

- Baez, Bagdasaryan and Gibbs, The Lebesgue universal covering problem (2015).

Stated but not proved: `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.bbg2015ApproximateUpperBound_holds` is written with `theorem_wanted` in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#bbg2015-approximate-upper-bound-holds).

## Gibbs's upper bound for Lebesgue's covering problem

The Lebesgue universal covering
constant, the infimum of the areas of the nonempty convex sets in the Euclidean plane that contain a
congruent copy of every nonempty convex planar set of diameter $1$, is at most $0.8440935944$.

## Sources

- Gibbs, An Upper Bound for Lebesgue's Covering Problem (2018).

Stated but not proved: `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.gibbs2018UpperBound_holds` is written with `theorem_wanted` in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#gibbs2018-upper-bound-holds).

## Disk lower bound for Lebesgue's universal covering constant

Lebesgue's universal covering
constant, the infimum of the areas of the nonempty convex planar sets that contain a congruent
copy of every nonempty convex planar set of diameter $1$, is at least $\pi/4$, the area of a disk
of radius $1/2$.

## Sources

- Radius-half disk lower-bound row, optimization catalogue constant 13b.

Stated but not proved: `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.trivialUnitDiskLowerBound_holds` is written with `theorem_wanted` in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#trivial-unit-disk-lower-bound-holds).

## Elekes's disk-and-triangle lower bound

The Lebesgue universal covering constant (the
infimum of the areas of universal convex covers) is at least $0.8257$.

## Sources

- Elekes (1994), disk and equilateral triangle lower bound.

Stated but not proved: `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.elekes1994DiskTriangleLowerBound_holds` is written with `theorem_wanted` in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#elekes1994-disk-triangle-lower-bound-hol).

## Elekes's regular-polygon lower bound for Lebesgue's covering problem

The Lebesgue universal
covering constant, the infimum of the areas of the nonempty convex sets in the Euclidean plane that
contain a congruent copy of every nonempty convex planar set of diameter $1$, is at least $0.8271$.

## Sources

- Elekes (1994), additional regular polygon lower bound.

Stated but not proved: `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.elekes1994RegularPolygonLowerBound_holds` is written with `theorem_wanted` in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#elekes1994-regular-polygon-lower-bound-h).

## Brass–Sharifi lower bound

The Lebesgue universal covering constant (the infimum of the
areas of universal convex covers) is at least $0.832$.

## Sources

- Brass and Sharifi, A lower bound for Lebesgue's universal cover problem (2005).

Stated but not proved: `MathlibExt.Geometry.LebesgueUniversalCoveringConstantWanted.brassSharifi2005LowerBound_holds` is written with `theorem_wanted` in [WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LebesgueUniversalCoveringConstantWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html#brass-sharifi2005-lower-bound-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lebesgue's universal covering problem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/packings-and-coverings/lebesgue-s-universal-covering-problem)
