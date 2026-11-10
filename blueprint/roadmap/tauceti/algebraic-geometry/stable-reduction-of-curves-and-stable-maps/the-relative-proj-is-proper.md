---
declaration: theorem
origin: cited
lean: CategoryTheory.CommMon.isProper_relativeProjToBase
statement: formalized
proof: formalized
---

# The relative `Proj` is proper

If the graded algebra `A` is of finite type and its
degree-zero part `A₀` is finite over `X`, then `Proj_X(A) ⟶ X` is proper.

```lean
CategoryTheory.CommMon.isProper_relativeProjToBase.{u} {X : AlgebraicGeometry.Scheme}
  {A : CategoryTheory.CommMon (CategoryTheory.GradedObject ℕ X.Modules)}
  [∀ (n : ℕ), SheafOfModules.IsQuasicoherent (A.X n)]
  (h :
    ∀ (U : X.Opens),
      AlgebraicGeometry.IsAffineOpen U →
        Algebra.FiniteType (↑(X.presheaf.obj (Opposite.op U)))
          (DirectSum ℕ fun n => ↑((A.X n).presheaf.obj (Opposite.op U))))
  (h₀ :
    ∀ (U : X.Opens),
      AlgebraicGeometry.IsAffineOpen U →
        Module.Finite ↑(X.presheaf.obj (Opposite.op U)) ↑((A.X 0).presheaf.obj (Opposite.op U))) :
  AlgebraicGeometry.IsProper A.relativeProjToBase
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.CommMon.isProper_relativeProjToBase`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/RelativeProj/Proper.html#CategoryTheory.CommMon.isProper_relativeProjToBase).

## Sources

- [Tau Ceti documentation: `CategoryTheory.CommMon.isProper_relativeProjToBase`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/RelativeProj/Proper.html#CategoryTheory.CommMon.isProper_relativeProjToBase)
- [Source of `CategoryTheory.CommMon.isProper_relativeProjToBase` in TauCeti/AlgebraicGeometry/RelativeProj/Proper.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/RelativeProj/Proper.lean#L116)
- [Tau Ceti roadmap status: Stable reduction of curves and stable maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StableReduction/STATUS.md)
