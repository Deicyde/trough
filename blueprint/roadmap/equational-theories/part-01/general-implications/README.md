# General implications

We will be interested in seeing which laws imply which other laws, in the sense that magmas satisfying the former law automatically satisfy the latter. We will also be interested in *anti-implications* showing that one law does *not* imply another, by producing examples of magmas that satisfy the former law but not the latter. Here is a formal definition.

- [Implication](impl.md)
- [Pre-order](pre-order.md)

Note that we view the stronger law as less than or equal to the weaker law. This is because the class of magmas that satisfy the stronger law is a subset of the class of magmas that satisfy the weaker law. It is also consistent with the conventions of Lean's Mathlib.

Implications between the laws from [Selected laws](../selected-laws/README.md) are depicted in fig:implications.

*(A figure in the source is not reproduced here.)*

- [Maximal element](maximal.md)
- [Minimal element](minimal.md)

Every magma $G$ has a *reversal* $G^{\mathrm{op}}$, formed by by replacing the magma operation $\diamond$ with its opposite $\diamond^{\mathrm{op}}:(x,y) \mapsto y \diamond x$. There is a natural isomorphism between these magmas, which induces an involution $w \mapsto w^{\mathrm{op}}$ on words $w \in M_X$. Every law $w \simeq w'$ then has a *dual* $w^{\mathrm{op}} \simeq (w')^{\mathrm{op}}$.

For instance, the dual of the law $0 \diamond 1 = 0 \diamond 2$ is $1 \diamond 0 = 2 \diamond 0$, which after relabeling is $0 \diamond 1 = 2 \diamond 1$. A list of equations and their duals can be found [here](https://github.com/teorth/equational_theories/blob/main/data/dual_equations.md). Of the 4694 equations under consideration, 84 are self-dual, leaving 2305 pairs of dual equations.

The pre-ordering on laws has a duality symmetry:

- [Duality of laws](duality.md)

Some equational laws can be “diagonalized”:

- [Diagonalization](diag.md)

Thus for instance, [E7](https://teorth.github.io/equational_theories/implications/?7) $({x = y \diamond z})$ is equivalent to [E2](https://teorth.github.io/equational_theories/implications/?2) $({x = y})$.

- [Laws implied by the constant law](constant-impl.md)
- [Criterion for implication](variable-impl.md)
