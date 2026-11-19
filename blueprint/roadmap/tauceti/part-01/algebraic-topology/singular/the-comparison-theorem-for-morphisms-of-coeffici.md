---
declaration: theorem
origin: cited
lean: TauCeti.isIso_filteredSpaceSpectralSequenceCoefficientMap_hom_f
statement: formalized
proof: formalized
---

# The comparison theorem for morphisms of coefficients

If a morphism of coefficients
`φ : R ⟶ R'` induces isomorphisms `Hₙ(X (q + 1), X q; R) ≅ Hₙ(X (q + 1), X q; R')` for every `q`
and `n`, then the induced morphism of spectral sequences is an isomorphism on every object of every
page `r ≥ 2`, that is, from the first page on.

```lean
TauCeti.isIso_filteredSpaceSpectralSequenceCoefficientMap_hom_f.{w, v, u} {A : Type u}
  [CategoryTheory.Category.{v, u} A] [CategoryTheory.Limits.HasCoproducts A]
  [CategoryTheory.Abelian A] {R : A} {Y : TopCat} {X : ℤ → Set ↑Y} (hX : Monotone X) {R' : A}
  (φ : R ⟶ R')
  (h :
    ∀ (q : ℤ) (n : ℕ),
      CategoryTheory.IsIso
        (HomologicalComplex.homologyMap
          (((SSetPair.chainComplexFunctor A).map φ).app
            (TopPair.toSSetPair.obj (TopPair.ofInclusion ⋯)))
          n))
  (r : ℤ) (hr : 2 ≤ r) (pq : ℤ × ℤ) :
  CategoryTheory.IsIso (((TauCeti.filteredSpaceSpectralSequenceCoefficientMap hX φ).hom r hr).f pq)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isIso_filteredSpaceSpectralSequenceCoefficientMap_hom_f`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/FilteredSpace/Basic.html#TauCeti.isIso_filteredSpaceSpectralSequenceCoefficientMap_hom_f).

## Sources

- [Tau Ceti documentation: `TauCeti.isIso_filteredSpaceSpectralSequenceCoefficientMap_hom_f`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/FilteredSpace/Basic.html#TauCeti.isIso_filteredSpaceSpectralSequenceCoefficientMap_hom_f)
- [Source of `TauCeti.isIso_filteredSpaceSpectralSequenceCoefficientMap_hom_f` in TauCeti/AlgebraicTopology/Singular/FilteredSpace/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Singular/FilteredSpace/Basic.lean#L955)
