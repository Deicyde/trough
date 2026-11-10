---
declaration: def
origin: cited
lean: Projectivization.fundamentalGroupEquivZModTwo
statement: formalized
---

# Real projective fundamental groups and lifted endpoints

For a real
normed space `E` with `2 < Module.rank ℝ E`,
[`Projectivization.fundamentalGroupEquivZModTwo`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/Projectivization.lean)
identifies `π₁(Projectivization ℝ E, b)` with `Multiplicative (ZMod 2)`.
A chosen unit lift over the supplied basepoint fixes the lift description,
but not the resulting coordinate. The identity means returning to that lift;
`Multiplicative.ofAdd (1 : ZMod 2)` means reaching its antipode. The sphere
uses the given norm, with no inner-product, finite-dimensionality or
completeness assumption, including infinite cardinal rank.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results) of [FormalFrontier/sphere-topology](https://github.com/FormalFrontier/sphere-topology) at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Projectivization.fundamentalGroupEquivZModTwo` (def), declared in [SphereTopology/Homotopy/Projectivization.lean, line 96](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/Projectivization.lean#L96).

Read from the source at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), without running Lean.

## Sources

- [sphere-topology at 672d46f9: README, headline results](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results)
- [Source of `Projectivization.fundamentalGroupEquivZModTwo` in SphereTopology/Homotopy/Projectivization.lean](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/Projectivization.lean#L96)
