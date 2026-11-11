---
declaration: theorem
origin: cited
lean: CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page_of_complete
statement: formalized
proof: formalized
---

# The comparison theorem for complete exhaustive filtrations

Let `α` be a morphism between
the functors of filtrations `F` of `K` and `G` of `L`, and let `n` be a degree. Suppose that, in
degrees `m = n` and `m = n + 1`, the stages below `a` of both filtrations cut out complete
filtrations of the terms of degree `m - 1`, both filtrations are separated in degree `m`, and the
graded pieces at all indices `i < a` have vanishing `H^m`. Suppose also that in degrees `n - 1`
and `n` both filtrations are exhaustive and their graded pieces at all indices `i ≥ b` have
vanishing cohomology. If the morphism of spectral sequences induced by `α` is an isomorphism on
every object of some page `r ≥ 2`, then `α.app ⊤` induces an isomorphism on `H^n`.

```lean
CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page_of_complete.{v, u_1} {R : Type u_1}
  [Ring R] {K : CochainComplex (ModuleCat R) ℤ} (F : ℤ → CategoryTheory.Subobject K)
  (hF : Monotone F) {L : CochainComplex (ModuleCat R) ℤ} (G : ℤ → CategoryTheory.Subobject L)
  (hG : Monotone G)
  (α : CochainComplex.filtrationFunctor F hF ⟶ CochainComplex.filtrationFunctor G hG) (n : ℤ)
  {a b : ℤ}
  (hFc :
    ∀ (m : ℤ),
      n ≤ m →
        m ≤ n + 1 →
          TauCeti.IsCompleteFiltration fun k =>
            (ModuleCat.Hom.hom ((F (a - ↑k)).arrow.f (m - 1))).range)
  (hGc :
    ∀ (m : ℤ),
      n ≤ m →
        m ≤ n + 1 →
          TauCeti.IsCompleteFiltration fun k =>
            (ModuleCat.Hom.hom ((G (a - ↑k)).arrow.f (m - 1))).range)
  (hFs :
    ∀ (m : ℤ),
      n ≤ m →
        m ≤ n + 1 →
          ∀ (x : ↑(K.X m)), (∀ (i : ℤ), x ∈ (ModuleCat.Hom.hom ((F i).arrow.f m)).range) → x = 0)
  (hGs :
    ∀ (m : ℤ),
      n ≤ m →
        m ≤ n + 1 →
          ∀ (x : ↑(L.X m)), (∀ (i : ℤ), x ∈ (ModuleCat.Hom.hom ((G i).arrow.f m)).range) → x = 0)
  (hFa :
    ∀ (m : ℤ),
      n ≤ m →
        m ≤ n + 1 →
          ∀ i < a,
            CategoryTheory.Limits.IsZero
              (HomologicalComplex.homology
                (CategoryTheory.Limits.cokernel ((F i).ofLE (F (i + 1)) ⋯)) m))
  (hGa :
    ∀ (m : ℤ),
      n ≤ m →
        m ≤ n + 1 →
          ∀ i < a,
            CategoryTheory.Limits.IsZero
              (HomologicalComplex.homology
                (CategoryTheory.Limits.cokernel ((G i).ofLE (G (i + 1)) ⋯)) m))
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

- [The comparison theorem for exhaustive filtrations](the-comparison-theorem-for-exhaustive-filtration.md)

## Lean

Formalized in Tau Ceti as [`CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page_of_complete`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/SpectralSequence/Filtered/Complete.html#CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page_of_complete).

## Sources

- [Tau Ceti documentation: `CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page_of_complete`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/SpectralSequence/Filtered/Complete.html#CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page_of_complete)
- [Source of `CochainComplex.isIso_homologyMap_of_isIso_spectralSequence_page_of_complete` in TauCeti/Algebra/Homology/SpectralSequence/Filtered/Complete.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/SpectralSequence/Filtered/Complete.lean#L173)
