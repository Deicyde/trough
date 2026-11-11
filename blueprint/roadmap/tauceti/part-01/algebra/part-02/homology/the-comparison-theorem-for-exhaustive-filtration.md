---
declaration: theorem
origin: cited
lean: CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page_of_exhaustive
statement: formalized
proof: formalized
---

# The comparison theorem for exhaustive filtrations

Let `α` be a morphism between the
functors of filtrations `F` of `K` and `G` of `L`, and let `n` be a degree. Suppose that the
stages `F_i` and `G_i` at all indices `i ≤ a` have vanishing cohomology in degrees `n` and `n + 1`
(for instance `F_a = G_a = ⊥`), that in degrees `n - 1` and `n` every element of `K` and of `L`
lies in some stage of the filtration, and that the graded pieces of both filtrations at all
indices `i ≥ b` have vanishing cohomology (no inequality between `a` and `b` is needed). If the
morphism of spectral sequences induced by `α` is an isomorphism on every object of some page
`r ≥ 2`, then `α.app ⊤` induces an isomorphism on `H^n`.

```lean
CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page_of_exhaustive.{v, u_1}
  {R : Type u_1} [Ring R] {K : CochainComplex (ModuleCat R) ℤ} (F : ℤ → CategoryTheory.Subobject K)
  (hF : Monotone F) {L : CochainComplex (ModuleCat R) ℤ} (G : ℤ → CategoryTheory.Subobject L)
  (hG : Monotone G)
  (α : CochainComplex.filtrationFunctor F hF ⟶ CochainComplex.filtrationFunctor G hG) (n : ℤ)
  {a b : ℤ}
  (hFa :
    ∀ (m : ℤ),
      n ≤ m →
        m ≤ n + 1 →
          ∀ i ≤ a,
            CategoryTheory.Limits.IsZero
              (HomologicalComplex.homology (CategoryTheory.Subobject.underlying.obj (F i)) m))
  (hGa :
    ∀ (m : ℤ),
      n ≤ m →
        m ≤ n + 1 →
          ∀ i ≤ a,
            CategoryTheory.Limits.IsZero
              (HomologicalComplex.homology (CategoryTheory.Subobject.underlying.obj (G i)) m))
  (hFex :
    ∀ (m : ℤ),
      n - 1 ≤ m → m ≤ n → ∀ (x : ↑(K.X m)), ∃ q, x ∈ (ModuleCat.Hom.hom ((F q).arrow.f m)).range)
  (hGex :
    ∀ (m : ℤ),
      n - 1 ≤ m → m ≤ n → ∀ (x : ↑(L.X m)), ∃ q, x ∈ (ModuleCat.Hom.hom ((G q).arrow.f m)).range)
  (hFb :
    ∀ (m : ℤ),
      n - 1 ≤ m →
        m ≤ n →
          ∀ (i : ℤ),
            b ≤ i →
              CategoryTheory.Limits.IsZero
                (HomologicalComplex.homology
                  (CategoryTheory.Limits.cokernel ((F i).ofLE (F (i + 1)) ⋯)) m))
  (hGb :
    ∀ (m : ℤ),
      n - 1 ≤ m →
        m ≤ n →
          ∀ (i : ℤ),
            b ≤ i →
              CategoryTheory.Limits.IsZero
                (HomologicalComplex.homology
                  (CategoryTheory.Limits.cokernel ((G i).ofLE (G (i + 1)) ⋯)) m))
  (r : ℤ) (hr : 2 ≤ r)
  (h :
    ∀ (pq : ℤ × ℤ),
      CategoryTheory.IsIso
        (((CategoryTheory.Abelian.SpectralObject.spectralSequenceMap
                  CategoryTheory.Abelian.SpectralObject.coreE₂Cohomological
                  (CochainComplex.spectralObjectMap α)).hom
              r hr).f
          pq)) :
  CategoryTheory.IsIso (HomologicalComplex.homologyMap (α.app ⊤) n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The comparison theorem (`CategoryTheory.Abelian.SpectralObject.isIso_hom_app_abutment_of_isIso_page`)](the-comparison-theorem-categorytheory-abelian-sp.md)

## Lean

Formalized in Tau Ceti as [`CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page_of_exhaustive`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/SpectralSequence/Filtered/Exhaustive.html#CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page_of_exhaustive).

## Sources

- [Tau Ceti documentation: `CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page_of_exhaustive`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/SpectralSequence/Filtered/Exhaustive.html#CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page_of_exhaustive)
- [Source of `CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page_of_exhaustive` in TauCeti/Algebra/Homology/SpectralSequence/Filtered/Exhaustive.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/SpectralSequence/Filtered/Exhaustive.lean#L194)
