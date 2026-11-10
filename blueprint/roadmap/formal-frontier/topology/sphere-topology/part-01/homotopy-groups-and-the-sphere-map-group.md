---
declaration: def
origin: cited
lean: HomotopyGroup.mulOppositeEquivSphereHom
statement: formalized
---

# Homotopy groups and the sphere-map group

For `n : ℕ` and any
`X : BasedTopCat.{u}`,
[`HomotopyGroup.mulOppositeEquivSphereHom`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/HomotopyGroup/SphereCogroup.lean)
gives a multiplicative equivalence from
`(HomotopyGroup (Fin (n + 1)) X.right (BasedTopCat.point X))ᵐᵒᵖ`
to the canonical `CategoryTheory.yonedaGrp` evaluation of `Metric.Sphere.cogroup n`
at `op (op (Q.obj X))`, where `Q := BasedTopCat.homotopyQuotient`.
Its elements are incoming morphisms to the cogroup carrier in the ordinary
opposite based-homotopy category; their unops are outgoing classes from the
lifted, north-based `Sⁿ⁺¹` to `X`. These categorical opposites differ from the source's
multiplicative opposite. Writing `E := HomotopyGroup.equivSphereHom (n + 1) X`,
`mulOppositeEquivSphereHom_apply_op` sends `MulOpposite.op a` to `(E a).op`;
`mulOppositeEquivSphereHom_symm_apply` sends `f` to
`MulOpposite.op (E.symm f.unop)`, without inversion or a change of representative.
`mulOppositeEquivSphereHom_naturality` identifies based postcomposition by
`h : X ⟶ Y` with the Yoneda action on `(Q.map h).op.op`.
Since folding `F, G` represents `J(G) * J(F)`, the source opposite matters
even for `n = 0`, which is `S¹`. No direct group comparison by the same class
map without that opposite, S¹ commutativity or group on S⁰ is asserted.
Targets require only their topology and chosen point.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results) of [FormalFrontier/sphere-topology](https://github.com/FormalFrontier/sphere-topology) at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `HomotopyGroup.mulOppositeEquivSphereHom` (def), declared in [SphereTopology/Homotopy/HomotopyGroup/SphereCogroup.lean, line 217](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/HomotopyGroup/SphereCogroup.lean#L217).

Read from the source at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), without running Lean.

## Sources

- [sphere-topology at 672d46f9: README, headline results](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results)
- [Source of `HomotopyGroup.mulOppositeEquivSphereHom` in SphereTopology/Homotopy/HomotopyGroup/SphereCogroup.lean](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/HomotopyGroup/SphereCogroup.lean#L217)
