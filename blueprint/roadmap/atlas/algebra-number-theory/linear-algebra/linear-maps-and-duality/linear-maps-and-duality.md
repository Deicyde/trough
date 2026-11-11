---
declaration: section
origin: cited
lean: LinearEquiv.affineEvaluation, LinearMap.exact_and_surjective_iff_forall_lcomp
statement: formalized
proof: formalized
---

# Linear maps and duality: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/index.html).

Vector spaces and modules, linear maps and their invariants such as trace, dual spaces, dual bases and perfect pairings, and exactness of sequences of linear maps.

## Evaluation of an affine function at two points

Evaluation of the affine function `x ↦ slope * x + intercept` at two distinct points.

Formalized by `LinearEquiv.affineEvaluation`, a definition declared in [MathlibExt/LinearAlgebra/AffineEvaluation.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/AffineEvaluation.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/index.html#affine-evaluation).

## Hom detects exact sequences ending in a surjection

Let $R$ be a commutative ring, let
$M$, $N$, $P$ be $R$-modules, and let $\varphi : M \to N$ and $\psi : N \to P$ be $R$-linear
maps. Then the image of $\varphi$ equals the kernel of $\psi$ and $\psi$ is surjective if and
only if, for every $R$-module $D$ in the same universe as $N$ and $P$, precomposition with $\psi$,
$g \mapsto g \circ \psi$, is an injective map $\operatorname{Hom}_R(P, D) \to
\operatorname{Hom}_R(N, D)$ whose image is the kernel of precomposition with $\varphi$,
$h \mapsto h \circ \varphi$, as a map $\operatorname{Hom}_R(N, D) \to \operatorname{Hom}_R(M, D)$.

Formalized by `LinearMap.exact_and_surjective_iff_forall_lcomp`, a theorem declared in [MathlibExt/LinearAlgebra/LeftExact.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/LeftExact.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/index.html#exact-and-surjective-iff-forall-lcomp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linear maps and duality](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/linear-maps-and-duality)
