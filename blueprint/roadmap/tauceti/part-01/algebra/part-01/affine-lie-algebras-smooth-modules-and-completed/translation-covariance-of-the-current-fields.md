---
declaration: theorem
origin: cited
lean: TauCeti.CurrentAlgebra.lie_vacuumTranslation_ncoeff_currentField
statement: formalized
proof: formalized
---

# Translation covariance of the current fields

`[T, J^x[[n]]] = -n J^x[[n - 1]]`, the
coefficient form of `[T, J^x(z)] = ∂_z J^x(z)`.

```lean
TauCeti.CurrentAlgebra.lie_vacuumTranslation_ncoeff_currentField.{u_1, u_2} {R : Type u_1}
  {L : Type u_2} [CommRing R] [LieRing L] [LieAlgebra R L] {Φ : LinearMap.BilinForm R L}
  {hΦ : LinearMap.BilinForm.lieInvariant L Φ} {hΦs : Φ.IsSymm} {a : R} (x : L) (n : ℤ) :
  ⁅TauCeti.CurrentAlgebra.vacuumTranslation Φ hΦ hΦs a,
      VertexOperator.ncoeff
        ((TauCeti.CurrentAlgebra.currentField (TauCeti.CurrentAlgebra.envelopingAction Φ hΦ hΦs a)
            ⋯)
          x)
        n⁆ =
    -(↑n •
        VertexOperator.ncoeff
          ((TauCeti.CurrentAlgebra.currentField (TauCeti.CurrentAlgebra.envelopingAction Φ hΦ hΦs a)
              ⋯)
            x)
          (n - 1))
```

## Depends on

- [TauCeti.CurrentAlgebra.VacuumModule](tauceti-currentalgebra-vacuummodule.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CurrentAlgebra.lie_vacuumTranslation_ncoeff_currentField`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/Vacuum/VectorField.html#TauCeti.CurrentAlgebra.lie_vacuumTranslation_ncoeff_currentField).

## Sources

- [Tau Ceti documentation: `TauCeti.CurrentAlgebra.lie_vacuumTranslation_ncoeff_currentField`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/Vacuum/VectorField.html#TauCeti.CurrentAlgebra.lie_vacuumTranslation_ncoeff_currentField)
- [Source of `TauCeti.CurrentAlgebra.lie_vacuumTranslation_ncoeff_currentField` in TauCeti/Algebra/Lie/Current/Vacuum/VectorField.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Current/Vacuum/VectorField.lean#L225)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
