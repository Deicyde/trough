---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.ConvexProjection.exists_unique_nearest_point_of_complete_convex, MathlibExt.Analysis.InnerProductSpace.ConvexProjection.exists_convexProjection_spec, MathlibExt.Analysis.InnerProductSpace.ConvexProjection.convexProjection, MathlibExt.Analysis.InnerProductSpace.ConvexProjection.convexProjection_spec, MathlibExt.Analysis.InnerProductSpace.ConvexProjection.convexProjection_mem, MathlibExt.Analysis.InnerProductSpace.ConvexProjection.convexProjection_norm_eq_iInf, MathlibExt.Analysis.InnerProductSpace.ConvexProjection.convexProjection_variational, MathlibExt.Analysis.InnerProductSpace.ConvexProjection.convexProjection_eq_of_isNearestPoint
statement: formalized
proof: formalized
---

# Hilbert projection theorem

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/hilbert-projection-theorem/index.html).

## Existence and uniqueness of the nearest point

Let $K$ be a nonempty complete convex
subset of a real inner product space $F$. For every $x \in F$ there is exactly one $p \in K$
with $\|x - p\| = \inf_{w \in K} \|x - w\|$, that is, exactly one point of $K$ nearest to $x$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ConvexProjection.exists_unique_nearest_point_of_complete_convex`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/hilbert-projection-theorem/index.html#exists-unique-nearest-point-of-complete).

## Totalized existence of the convex projection

For every subset $K$ of a real inner product
space $F$ and every $x \in F$, there is a point $p \in F$ such that, if $K$ is nonempty, complete
and convex, then $p \in K$ and $\|x - p\| = \inf_{w \in K} \|x - w\|$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ConvexProjection.exists_convexProjection_spec`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/hilbert-projection-theorem/index.html#exists-convex-projection-spec).

## Nearest-point projection onto a convex set

For a subset $K$ of a real inner product space
$F$ and a point $x \in F$, the nearest-point projection $P_K(x)$ is a chosen point of $F$ such
that, whenever $K$ is nonempty, complete and convex, $P_K(x) \in K$ and
$\|x - P_K(x)\| = \inf_{w \in K} \|x - w\|$; it is then the unique point of $K$ nearest to $x$.
When $K$ fails one of these hypotheses, the value of $P_K(x)$ is unspecified.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ConvexProjection.convexProjection`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/hilbert-projection-theorem/index.html#convex-projection).

## Defining property of the convex projection

Let $K$ be a nonempty complete convex subset
of a real inner product space $F$, and let $P_K$ be the nearest-point projection onto $K$. For
every $x \in F$, $P_K(x) \in K$ and $\|x - P_K(x)\| = \inf_{w \in K} \|x - w\|$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ConvexProjection.convexProjection_spec`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/hilbert-projection-theorem/index.html#convex-projection-spec).

## The convex projection lies in the set

Let $K$ be a nonempty complete convex subset of a
real inner product space $F$, and let $P_K$ be the nearest-point projection onto $K$. Then
$P_K(x) \in K$ for every $x \in F$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ConvexProjection.convexProjection_mem`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/hilbert-projection-theorem/index.html#convex-projection-mem).

## The convex projection minimizes the distance to the set

Let $K$ be a nonempty complete
convex subset of a real inner product space $F$, and let $P_K$ be the nearest-point projection
onto $K$. Then $\|x - P_K(x)\| = \inf_{w \in K} \|x - w\|$ for every $x \in F$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ConvexProjection.convexProjection_norm_eq_iInf`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/hilbert-projection-theorem/index.html#convex-projection-norm-eq-i-inf).

## Variational inequality for the convex projection

Let $K$ be a nonempty complete convex
subset of a real inner product space $F$, and let $P_K$ be the nearest-point projection onto $K$.
For every $x \in F$ and every $w \in K$, $\langle x - P_K(x), w - P_K(x) \rangle \le 0$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ConvexProjection.convexProjection_variational`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/hilbert-projection-theorem/index.html#convex-projection-variational).

## Nearest points coincide with the convex projection

Let $K$ be a nonempty complete convex
subset of a real inner product space $F$, let $P_K$ be the nearest-point projection onto $K$, and
let $x \in F$. If $p \in K$ satisfies $\|x - p\| = \inf_{w \in K} \|x - w\|$, then $P_K(x) = p$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ConvexProjection.convexProjection_eq_of_isNearestPoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/hilbert-projection-theorem/index.html#convex-projection-eq-of-is-nearest-point).

## The convex projection fixes the points of the set

Let $K$ be a nonempty complete convex
subset of a real inner product space $F$, and let $P_K$ be the nearest-point projection onto $K$.
Then $P_K(x) = x$ for every $x \in K$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ConvexProjection.convexProjection_eq_self_of_mem`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/hilbert-projection-theorem/index.html#convex-projection-eq-self-of-mem).

## Idempotence of the convex projection

Let $K$ be a nonempty complete convex subset of a
real inner product space $F$, and let $P_K$ be the nearest-point projection onto $K$. Then
$P_K(P_K(x)) = P_K(x)$ for every $x \in F$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ConvexProjection.convexProjection_idem`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/hilbert-projection-theorem/index.html#convex-projection-idem).

## Nonexpansiveness of nearest-point selection

Let $K$ be a convex subset of a real inner
product space $F$, let $x, y \in F$, and let $p, q \in K$ satisfy
$\|x - p\| = \inf_{w \in K} \|x - w\|$ and $\|y - q\| = \inf_{w \in K} \|y - w\|$, so that $p$
is a point of $K$ nearest to $x$ and $q$ is a point of $K$ nearest to $y$. Then
$\|p - q\| \le \|x - y\|$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ConvexProjection.norm_sub_le_of_isNearestPoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/hilbert-projection-theorem/index.html#norm-sub-le-of-is-nearest-point).

## Firm nonexpansiveness of nearest-point selection

Let $K$ be a convex subset of a real
inner product space $F$, let $x, y \in F$, and let $p, q \in K$ satisfy
$\|x - p\| = \inf_{w \in K} \|x - w\|$ and $\|y - q\| = \inf_{w \in K} \|y - w\|$, so that $p$
is a point of $K$ nearest to $x$ and $q$ is a point of $K$ nearest to $y$. Then
$\|p - q\|^2 + \|(x - p) - (y - q)\|^2 \le \|x - y\|^2$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ConvexProjection.norm_sub_sq_add_norm_sub_sq_le_of_isNearestPoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/hilbert-projection-theorem/index.html#norm-sub-sq-add-norm-sub-sq-le-of-is-nea).

## The convex projection is $1$-Lipschitz

Let $K$ be a nonempty complete convex subset of a
real inner product space $F$, and let $P_K$ be the nearest-point projection onto $K$. Then
$\|P_K x - P_K y\| \le \|x - y\|$ for all $x, y \in F$, that is, $P_K$ is $1$-Lipschitz.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ConvexProjection.lipschitzWith_convexProjection`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/hilbert-projection-theorem/index.html#lipschitz-with-convex-projection).

## Firm nonexpansiveness of the convex projection

Let $K$ be a nonempty complete convex
subset of a real inner product space $F$, and let $P_K$ be the nearest-point projection onto $K$.
For all $x, y \in F$,
$\|P_K(x) - P_K(y)\|^2 + \|(x - P_K(x)) - (y - P_K(y))\|^2 \le \|x - y\|^2$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ConvexProjection.convexProjection_firmly_nonexpansive`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ConvexProjection.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/hilbert-projection-theorem/index.html#convex-projection-firmly-nonexpansive).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hilbert projection theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/hilbert-projection-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/hilbert-spaces/hilbert-projection-theorem)
