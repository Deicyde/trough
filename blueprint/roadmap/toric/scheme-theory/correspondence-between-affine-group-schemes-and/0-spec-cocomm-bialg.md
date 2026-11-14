---
declaration: proposition
origin: cited
lean: AlgebraicGeometry.isCommMonObj_spec_asOver_spec, AlgebraicGeometry.instCommGrpObjSpecAsOverSpec
statement: formalized
proof: formalized
---

# Spec sends cocommutative bialgebras to commutative monoid schemes

If $A$ is a cocommutative bialgebra over $R$, then $\operatorname{Spec} A$ is a commutative monoid scheme.

## Depends on

- [Spec as a functor on Hopf algebras](0-spec-hopf.md)

## Proof

Diagrams are the same up to identifying $\operatorname{Spec} (A \otimes A)$ with $\operatorname{Spec} A \otimes \operatorname{Spec} A$.

## Lean

Formalized as [`AlgebraicGeometry.isCommMonObj_spec_asOver_spec`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.isCommMonObj_spec_asOver_spec), [`AlgebraicGeometry.instCommGrpObjSpecAsOverSpec`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.instCommGrpObjSpecAsOverSpec).

## Sources

- [Toric varieties blueprint: chapters/4-1-affine-group-schemes.tex, line 84](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/4-1-affine-group-schemes.tex#L84)
