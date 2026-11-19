# Local sphere eversion

The local theory of [Local theory of convex integration](../local-theory-of-convex-integration/README.md) is already enough to deduce Smale's sphere eversion theorem, although it is less natural than going through the general results of [Global theory of open and ample relations](../global-theory-of-open-and-ample-relations/README.md). The goal of this appendix is to explain how to do so. In this section $E$ denote a finite dimensional real vector space equipped with an inner product. Later we will assume it is 3-dimensional. We denote by $𝕊$ the unit sphere in $E$.

Although we want to study immersions of $𝕊$ into $E$, we want to work only with functions defined on the whole $E$. So we introduce a slightly artificial relation. We denote by $B$ the open ball with radius $9/10$ around the origin in $E$ and set:

$$
\mathcal{R} := \{(x, y, φ) ∈ J^1(E, E) \;|\; x ∉ B ⇒ φ|_{x^⊥} \text{ is injective}\}.
$$

Of course solutions of this relation restrict to immersions of $𝕊$.

- [loc_immersion_rel_open](lem-loc-immersion-rel-open.md)
- [loc_immersion_rel_ample](lem-loc-immersion-rel-ample.md)
- [Smale 1958](sphere-eversion-of-loc.md)
