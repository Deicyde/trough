---
declaration: def
origin: cited
lean: GenLoop.sphereHomeomorph
statement: formalized
---

# Finite generalized loops and based sphere-map classes

For every `n : ℕ`,
[`GenLoop.sphereHomeomorph`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/HomotopyGroup/Sphere.lean)
gives a homeomorphism from `GenLoop (Fin n) X x` to
`{F : C(Sⁿ, X) // F (EuclideanSpace.northPoint n) = x}`, where `Sⁿ` is the
unit sphere in `EuclideanSpace ℝ (Fin (n+1))`.
`HomotopyGroup.equivSphereClasses` gives a natural set equivalence from
`HomotopyGroup (Fin n) X x` to the existing `ZerothHomotopy` of this subtype.
Inverse representatives precompose with
[`Cube.collapseToSphere`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Geometry/CubeSphere.lean).
Constants and based postcomposition are preserved, including between targets
in independent universes. Equality of sphere-map components is exactly
homotopy relative to the singleton last-axis north pole. In dimension one,
`HomotopyGroup.pi1MulEquivFundamentalGroup_sphereHomeomorph` sends the component
associated with a based path to that path's fundamental-group class. Targets
require only a topology and a chosen point, with no separation, local compactness
or well-pointedness hypothesis.

For every `n : ℕ` and arbitrary `X : BasedTopCat.{u}`,
[`HomotopyGroup.equivSphereHom`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/HomotopyGroup/SphereHom.lean)
is an ordinary set equivalence from `HomotopyGroup (Fin n) X.right (BasedTopCat.point X)`
to morphisms from the north-based `ULift.{u} Sⁿ` to `X` in the based-homotopy
category. Targets may be any objects of the under category, not only ones
presented by `BasedTopCat.of`, and the construction applies in every universe `u`.
Forward representatives precompose `GenLoop.sphereHomeomorph n` with `ULift.down`;
inverse representatives have values
`t ↦ f.right.hom (ULift.up (Cube.collapseToSphere n t))`.
Here `n = 0` means `S⁰` and `n = 1` means `S¹`. This set comparison alone
specifies no multiplication on the hom-set or group in dimension zero; the
positive-dimensional group comparison below uses a multiplicative opposite.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results) of [FormalFrontier/sphere-topology](https://github.com/FormalFrontier/sphere-topology) at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `GenLoop.sphereHomeomorph` (def), declared in [SphereTopology/Homotopy/HomotopyGroup/Sphere.lean, line 91](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/HomotopyGroup/Sphere.lean#L91).

Read from the source at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), without running Lean.

## Sources

- [sphere-topology at 672d46f9: README, headline results](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results)
- [Source of `GenLoop.sphereHomeomorph` in SphereTopology/Homotopy/HomotopyGroup/Sphere.lean](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/HomotopyGroup/Sphere.lean#L91)
