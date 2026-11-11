---
declaration: theorem
origin: cited
lean: TauCeti.noRetraction_diskBoundary
statement: formalized
proof: formalized
---

# The no-retraction theorem

the boundary sphere `∂Dⁿ` of the disk is not a retract of
the disk `Dⁿ`. That is, there are no maps `i : ∂Dⁿ ⟶ Dⁿ` and `r : Dⁿ ⟶ ∂Dⁿ` with `i ≫ r = 𝟙`;
in particular the boundary inclusion `TopCat.diskBoundaryInclusion n` has no retraction. This
includes `n = 0`, where the boundary is empty.

```lean
TauCeti.noRetraction_diskBoundary.{w} (n : ℕ) :
  IsEmpty (CategoryTheory.Retract (TopCat.diskBoundary n) (TopCat.disk n))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mayer–Vietoris isomorphism of a sphere](the-mayer-vietoris-isomorphism-of-a-sphere.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.noRetraction_diskBoundary`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/BrouwerFixedPoint.html#TauCeti.noRetraction_diskBoundary).

## Sources

- [Tau Ceti documentation: `TauCeti.noRetraction_diskBoundary`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/BrouwerFixedPoint.html#TauCeti.noRetraction_diskBoundary)
- [Source of `TauCeti.noRetraction_diskBoundary` in TauCeti/AlgebraicTopology/Singular/BrouwerFixedPoint.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Singular/BrouwerFixedPoint.lean#L68)
