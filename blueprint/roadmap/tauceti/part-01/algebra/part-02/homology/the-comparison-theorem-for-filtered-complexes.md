---
declaration: theorem
origin: cited
lean: CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page
statement: formalized
proof: formalized
---

# The comparison theorem for filtered complexes

Let `α` be a morphism between the
functors of finite increasing filtrations `F` of `K` and `G` of `L` (`F_a = G_a = ⊥` and
`F_b = G_b = ⊤`). If the induced morphism of spectral sequences is an isomorphism on every object
of some page `r ≥ 2`, then `α.app ⊤` induces isomorphisms in cohomology.

```lean
CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page.{v_1, u_1} {C : Type u_1}
  [CategoryTheory.Category.{v_1, u_1} C] [CategoryTheory.Abelian C] {K L : CochainComplex C ℤ}
  (F : ℤ → CategoryTheory.Subobject K) (hF : Monotone F) (G : ℤ → CategoryTheory.Subobject L)
  (hG : Monotone G)
  (α : CochainComplex.filtrationFunctor F hF ⟶ CochainComplex.filtrationFunctor G hG) {a b : ℤ}
  (hFa : F a = ⊥) (hGa : G a = ⊥) (hFb : F b = ⊤) (hGb : G b = ⊤) (r : ℤ) (hr : 2 ≤ r)
  (h :
    ∀ (pq : ℤ × ℤ),
      CategoryTheory.IsIso
        (((CategoryTheory.Abelian.SpectralObject.spectralSequenceMap
                  CategoryTheory.Abelian.SpectralObject.coreE₂Cohomological
                  (CochainComplex.spectralObjectMap α)).hom
              r hr).f
          pq))
  (n : ℤ) : CategoryTheory.IsIso (HomologicalComplex.homologyMap (α.app ⊤) n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The comparison theorem (`CategoryTheory.Abelian.SpectralObject.isIso_hom_app_abutment_of_isIso_page`)](the-comparison-theorem-categorytheory-abelian-sp.md)

## Lean

Formalized in Tau Ceti as [`CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/SpectralSequence/Filtered/Comparison.html#CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page).

## Sources

- [Tau Ceti documentation: `CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/SpectralSequence/Filtered/Comparison.html#CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page)
- [Source of `CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page` in TauCeti/Algebra/Homology/SpectralSequence/Filtered/Comparison.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/SpectralSequence/Filtered/Comparison.lean#L66)
