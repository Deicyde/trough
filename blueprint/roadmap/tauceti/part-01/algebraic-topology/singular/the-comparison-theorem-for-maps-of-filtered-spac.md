---
declaration: theorem
origin: cited
lean: TauCeti.isIso_filteredSpaceSpectralSequenceMap_hom_f
statement: formalized
proof: formalized
---

# The comparison theorem for maps of filtered spaces

If a map `g : Y ⟶ Y'` carrying each
`X q` into `X' q` induces isomorphisms `Hₙ(X (q + 1), X q) ≅ Hₙ(X' (q + 1), X' q)` for every `q`
and `n`, then the induced morphism of spectral sequences is an isomorphism on every object of every
page `r ≥ 2`, that is, from the first page on.

```lean
TauCeti.isIso_filteredSpaceSpectralSequenceMap_hom_f.{w, v, u} {A : Type u}
  [CategoryTheory.Category.{v, u} A] [CategoryTheory.Limits.HasCoproducts A]
  [CategoryTheory.Abelian A] (R : A) {Y : TopCat} {X : ℤ → Set ↑Y} (hX : Monotone X) {Y' : TopCat}
  {X' : ℤ → Set ↑Y'} (hX' : Monotone X') (g : Y ⟶ Y')
  (hg : ∀ (q : ℤ), Set.MapsTo (⇑(CategoryTheory.ConcreteCategory.hom g)) (X q) (X' q))
  (h :
    ∀ (q : ℤ) (n : ℕ),
      CategoryTheory.IsIso
        (TopPair.singularHomologyMap (TauCeti.filteredSpaceStepMap hX hX' g hg ⋯) R n))
  (r : ℤ) (hr : 2 ≤ r) (pq : ℤ × ℤ) :
  CategoryTheory.IsIso (((TauCeti.filteredSpaceSpectralSequenceMap R hX hX' g hg).hom r hr).f pq)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isIso_filteredSpaceSpectralSequenceMap_hom_f`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/FilteredSpace/Basic.html#TauCeti.isIso_filteredSpaceSpectralSequenceMap_hom_f).

## Sources

- [Tau Ceti documentation: `TauCeti.isIso_filteredSpaceSpectralSequenceMap_hom_f`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/FilteredSpace/Basic.html#TauCeti.isIso_filteredSpaceSpectralSequenceMap_hom_f)
- [Source of `TauCeti.isIso_filteredSpaceSpectralSequenceMap_hom_f` in TauCeti/AlgebraicTopology/Singular/FilteredSpace/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Singular/FilteredSpace/Basic.lean#L738)
