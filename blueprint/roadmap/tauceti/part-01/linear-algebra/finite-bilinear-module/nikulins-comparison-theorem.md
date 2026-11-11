---
declaration: theorem
origin: cited
lean: TauCeti.FiniteQuadraticModule.nonempty_isometry_iff_bilinear_isometry_and_gaussSign_eq
statement: formalized
proof: formalized
---

# Nikulin's comparison theorem

Two nondegenerate finite quadratic modules are isometric
exactly when their polar bilinear modules are isometric and their Gauss-sum invariants agree.

```lean
TauCeti.FiniteQuadraticModule.nonempty_isometry_iff_bilinear_isometry_and_gaussSign_eq.{u, v}
  {A : TauCeti.FiniteQuadraticModule} {B : TauCeti.FiniteQuadraticModule} (hA : A.IsNondegenerate) :
  Nonempty (A.Isometry B) ↔
    Nonempty (A.Isometry B.toFiniteBilinearModule) ∧ A.gaussSign = B.gaussSign
```

## Depends on

- [TauCeti.FiniteQuadraticModule](../../number-theory/part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)

## Proof depends on

- [Euler's four-square identity for a quadratic map](../quadratic-form/eulers-four-square-identity-for-a-quadratic-map.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteQuadraticModule.nonempty_isometry_iff_bilinear_isometry_and_gaussSign_eq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/FiniteBilinearModule/Comparison.html#TauCeti.FiniteQuadraticModule.nonempty_isometry_iff_bilinear_isometry_and_gaussSign_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteQuadraticModule.nonempty_isometry_iff_bilinear_isometry_and_gaussSign_eq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/FiniteBilinearModule/Comparison.html#TauCeti.FiniteQuadraticModule.nonempty_isometry_iff_bilinear_isometry_and_gaussSign_eq)
- [Source of `TauCeti.FiniteQuadraticModule.nonempty_isometry_iff_bilinear_isometry_and_gaussSign_eq` in TauCeti/LinearAlgebra/FiniteBilinearModule/Comparison.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/FiniteBilinearModule/Comparison.lean#L173)
