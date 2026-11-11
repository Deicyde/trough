---
declaration: theorem
origin: cited
lean: CategoryTheory.Abelian.SpectralObject.isIso_hom_app_abutment_of_isIso_page
statement: formalized
proof: formalized
---

# The comparison theorem (`CategoryTheory.Abelian.SpectralObject.isIso_hom_app_abutment_of_isIso_page`)

Let `φ : X ⟶ Y` be a morphism of spectral objects indexed by
`EInt` and integers `a`, `b` (no inequality between them is needed) such that `H^m(⊥ ≤ i)`
vanishes for `i ≤ a` and `m ∈ {n, n + 1}`, and `H^m(i ≤ ⊤)` vanishes for `i ≥ b` and
`m ∈ {n - 1, n}`, for `X` and `Y`. If the induced morphism of spectral sequences is an
isomorphism on every object of some page `r ≥ 2`, then `φ` is an isomorphism on the abutments
`H^n(⊥ ≤ ⊤)`.

```lean
CategoryTheory.Abelian.SpectralObject.isIso_hom_app_abutment_of_isIso_page.{v_1, u_1} {C : Type u_1}
  [CategoryTheory.Category.{v_1, u_1} C] [CategoryTheory.Abelian C]
  {X Y : CategoryTheory.Abelian.SpectralObject C EInt} (φ : X ⟶ Y) {a b : ℤ} (n : ℤ)
  (hXa :
    ∀ (m i : ℤ),
      n ≤ m →
        m ≤ n + 1 →
          i ≤ a →
            CategoryTheory.Limits.IsZero
              ((X.H m).obj (CategoryTheory.ComposableArrows.mk₁ (CategoryTheory.homOfLE ⋯))))
  (hYa :
    ∀ (m i : ℤ),
      n ≤ m →
        m ≤ n + 1 →
          i ≤ a →
            CategoryTheory.Limits.IsZero
              ((Y.H m).obj (CategoryTheory.ComposableArrows.mk₁ (CategoryTheory.homOfLE ⋯))))
  (hXb :
    ∀ (m i : ℤ),
      n - 1 ≤ m →
        m ≤ n →
          b ≤ i →
            CategoryTheory.Limits.IsZero
              ((X.H m).obj (CategoryTheory.ComposableArrows.mk₁ (CategoryTheory.homOfLE ⋯))))
  (hYb :
    ∀ (m i : ℤ),
      n - 1 ≤ m →
        m ≤ n →
          b ≤ i →
            CategoryTheory.Limits.IsZero
              ((Y.H m).obj (CategoryTheory.ComposableArrows.mk₁ (CategoryTheory.homOfLE ⋯))))
  (r : ℤ) (hr : 2 ≤ r)
  (h :
    ∀ (pq : ℤ × ℤ),
      CategoryTheory.IsIso
        (((CategoryTheory.Abelian.SpectralObject.spectralSequenceMap
                  CategoryTheory.Abelian.SpectralObject.coreE₂Cohomological φ).hom
              r hr).f
          pq)) :
  CategoryTheory.IsIso
    ((φ.hom n).app (CategoryTheory.ComposableArrows.mk₁ (CategoryTheory.homOfLE ⋯)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The comparison theorem on `E∞`](the-comparison-theorem-on-e.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Abelian.SpectralObject.isIso_hom_app_abutment_of_isIso_page`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/SpectralObject/Comparison.html#CategoryTheory.Abelian.SpectralObject.isIso_hom_app_abutment_of_isIso_page).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Abelian.SpectralObject.isIso_hom_app_abutment_of_isIso_page`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/SpectralObject/Comparison.html#CategoryTheory.Abelian.SpectralObject.isIso_hom_app_abutment_of_isIso_page)
- [Source of `CategoryTheory.Abelian.SpectralObject.isIso_hom_app_abutment_of_isIso_page` in TauCeti/Algebra/Homology/SpectralObject/Comparison.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/SpectralObject/Comparison.lean#L114)
