---
declaration: theorem
origin: cited
lean: TauCeti.IsMorse.nonempty_filteredSpaceSpectralSequence_page_two_X_iso_sigma
statement: formalized
proof: formalized
---

# The first page of the spectral sequence of a critical-band filtration is free on the critical points

Let `f` be a Morse function and `a : ℤ → ℝ` monotone, and let the band
`f⁻¹[a q, a (q + 1)]` be a critical band: compact with at most one critical value, lying strictly
between `a q` and `a (q + 1)`. Then on the first page of the spectral sequence of the filtration
`q ↦ {f ≤ a q}`, the object at `(p, q)`, with `p + q = -n`, is the coproduct of one copy of `R` for
each critical point of index `n` with value in `(a q, a (q + 1)]`.

```lean
TauCeti.IsMorse.nonempty_filteredSpaceSpectralSequence_page_two_X_iso_sigma.{u, v, w, u_1, u_2}
  {E : Type u_1} {H : Type u_2} {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [FiniteDimensional ℝ E] [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] {f : M → ℝ} {a : ℤ → ℝ}
  {A : Type v} [CategoryTheory.Category.{w, v} A] [CategoryTheory.Abelian A]
  [CategoryTheory.Limits.HasCoproducts A] (R : A) (hf : TauCeti.IsMorse I f) (ha : Monotone a)
  {q : ℤ} (hband : TauCeti.IsCriticalBand I f (a q) (a (q + 1))) (pq : ℤ × ℤ) (hq : pq.2 = q)
  (n : ℕ) (hn : pq.1 + pq.2 = -↑n) :
  Nonempty
    (((TauCeti.filteredSpaceSpectralSequence R ⋯).page 2
            TauCeti.isZero_filteredSpaceSpectralSequence_page_two_X_of_forall_notMem._proof_2).X
        pq ≅
      ∐ fun x => R)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The relative homology across a critical level is free on the critical points](the-relative-homology-across-a-critical-level-is.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMorse.nonempty_filteredSpaceSpectralSequence_page_two_X_iso_sigma`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/SpectralSequence.html#TauCeti.IsMorse.nonempty_filteredSpaceSpectralSequence_page_two_X_iso_sigma).

## Sources

- [Tau Ceti documentation: `TauCeti.IsMorse.nonempty_filteredSpaceSpectralSequence_page_two_X_iso_sigma`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/SpectralSequence.html#TauCeti.IsMorse.nonempty_filteredSpaceSpectralSequence_page_two_X_iso_sigma)
- [Source of `TauCeti.IsMorse.nonempty_filteredSpaceSpectralSequence_page_two_X_iso_sigma` in TauCeti/Geometry/Manifold/Morse/SpectralSequence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Morse/SpectralSequence.lean#L171)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MorseTheory/STATUS.md)
