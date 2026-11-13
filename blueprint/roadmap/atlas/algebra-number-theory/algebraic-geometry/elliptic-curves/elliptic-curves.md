---
declaration: section
origin: cited
lean: MetaMathlibExt.good_reduction_torsion_unramified
statement: formalized
proof: formalized
---

# Elliptic curves: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/index.html).

Elliptic curves given by Weierstrass equations, their points over finite fields and number fields, torsion, reduction and Galois representations.

## Néron–Ogg–Shafarevich criterion, easy direction

Let $R$ be a discrete valuation ring
with fraction field $k$, and let $E$ be an elliptic curve over $k$ given by a Weierstrass
equation with good reduction at $R$. Let $n$ be a natural number whose image in the residue
field of $R$ is nonzero, let $k^{\mathrm{sep}}$ be a separable closure of $k$, and let
$\mathcal{O}$ be a valuation subring of $k^{\mathrm{sep}}$ whose intersection with $k$ is $R$.
Then every element $\sigma$ of the inertia subgroup of $\mathcal{O}$ in
$\mathrm{Gal}(k^{\mathrm{sep}}/k)$ fixes every point $P \in E(k^{\mathrm{sep}})$ with $nP = 0$.

Proof: We use Silverman's elementary valuation filtration at the origin in $(z, w)$ coordinates,
together with reduction to the nonsingular residue curve; see *The Arithmetic of Elliptic Curves*,
IV.1, VII.3, and VII.7.

## Sources

- J. H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., GTM 106, Springer, Theorem VII.7.1.

Formalized by `MetaMathlibExt.good_reduction_torsion_unramified`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/NeronOggShafarevich.lean, line 1678](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/NeronOggShafarevich.lean#L1678). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/index.html#good-reduction-torsion-unramified).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Elliptic curves](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/AlgebraicGeometry/elliptic-curves)
