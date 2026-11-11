---
declaration: theorem
origin: cited
lean: CategoryTheory.Abelian.SpectralObject.isIso_hom_app_abutment
statement: formalized
proof: formalized
---

# The comparison theorem on `E∞`

Let `φ : X ⟶ Y` be a morphism of spectral objects
indexed by `EInt` and `a ≤ b` such that `H^n(⊥ ≤ a)` and `H^n(b ≤ ⊤)` vanish for `X` and `Y`
(the filtrations of the abutments in degree `n` start at `a` and end at `b`). If `φ` is an
isomorphism on `EInfty q n` for `a ≤ q < b`, then it is an isomorphism on the abutment
`H^n(⊥ ≤ ⊤)`.

```lean
CategoryTheory.Abelian.SpectralObject.isIso_hom_app_abutment.{v_1, u_1} {C : Type u_1}
  [CategoryTheory.Category.{v_1, u_1} C] [CategoryTheory.Abelian C]
  {X Y : CategoryTheory.Abelian.SpectralObject C EInt} (φ : X ⟶ Y) {a b n : ℤ} (hab : a ≤ b)
  (hXa :
    CategoryTheory.Limits.IsZero
      ((X.H n).obj (CategoryTheory.ComposableArrows.mk₁ (CategoryTheory.homOfLE ⋯))))
  (hYa :
    CategoryTheory.Limits.IsZero
      ((Y.H n).obj (CategoryTheory.ComposableArrows.mk₁ (CategoryTheory.homOfLE ⋯))))
  (hXb :
    CategoryTheory.Limits.IsZero
      ((X.H n).obj (CategoryTheory.ComposableArrows.mk₁ (CategoryTheory.homOfLE ⋯))))
  (hYb :
    CategoryTheory.Limits.IsZero
      ((Y.H n).obj (CategoryTheory.ComposableArrows.mk₁ (CategoryTheory.homOfLE ⋯))))
  (hE :
    ∀ (q : ℤ),
      a ≤ q →
        q < b →
          CategoryTheory.IsIso
            (CategoryTheory.Abelian.SpectralObject.EMap φ (CategoryTheory.homOfLE ⋯)
              (CategoryTheory.homOfLE ⋯) (CategoryTheory.homOfLE ⋯) (n - 1) n (n + 1) ⋯ ⋯)) :
  CategoryTheory.IsIso
    ((φ.hom n).app (CategoryTheory.ComposableArrows.mk₁ (CategoryTheory.homOfLE ⋯)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Abelian.SpectralObject.isIso_hom_app_abutment`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/SpectralObject/Comparison.html#CategoryTheory.Abelian.SpectralObject.isIso_hom_app_abutment).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Abelian.SpectralObject.isIso_hom_app_abutment`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/SpectralObject/Comparison.html#CategoryTheory.Abelian.SpectralObject.isIso_hom_app_abutment)
- [Source of `CategoryTheory.Abelian.SpectralObject.isIso_hom_app_abutment` in TauCeti/Algebra/Homology/SpectralObject/Comparison.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/SpectralObject/Comparison.lean#L37)
