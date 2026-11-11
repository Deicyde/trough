---
declaration: theorem
origin: cited
lean: ChainComplex.sum_range_trace_f_eq_sum_range_trace_homologyMap
statement: formalized
proof: formalized
---

# The Hopf trace formula

If the terms of `K` through degree `n` are finite-dimensional and
the differential `Kₙ₊₁ ⟶ Kₙ` vanishes, then the alternating sums up to degree `n` of the traces
of a chain endomorphism `φ` on the terms and on the homology of `K` agree.

```lean
ChainComplex.sum_range_trace_f_eq_sum_range_trace_homologyMap.{u, v} {k : Type u} [Field k]
  {K : ChainComplex (ModuleCat k) ℕ} (φ : K ⟶ K) {n : ℕ}
  (hfinite : ∀ i ≤ n, Module.Finite k ↑(K.X i)) (hn : K.d (n + 1) n = 0) :
  ∑ i ∈ Finset.range (n + 1), (-1) ^ i * (LinearMap.trace k ↑(K.X i)) (ModuleCat.Hom.hom (φ.f i)) =
    ∑ i ∈ Finset.range (n + 1),
      (-1) ^ i *
        (LinearMap.trace k ↑(HomologicalComplex.homology K i))
          (ModuleCat.Hom.hom (HomologicalComplex.homologyMap φ i))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ChainComplex.sum_range_trace_f_eq_sum_range_trace_homologyMap`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/ModuleCat/HopfTrace.html#ChainComplex.sum_range_trace_f_eq_sum_range_trace_homologyMap).

## Sources

- [Tau Ceti documentation: `ChainComplex.sum_range_trace_f_eq_sum_range_trace_homologyMap`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/ModuleCat/HopfTrace.html#ChainComplex.sum_range_trace_f_eq_sum_range_trace_homologyMap)
- [Source of `ChainComplex.sum_range_trace_f_eq_sum_range_trace_homologyMap` in TauCeti/Algebra/Homology/ModuleCat/HopfTrace.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/ModuleCat/HopfTrace.lean#L145)
- [Tau Ceti roadmap status: Morse–Novikov homology and dynamical Reidemeister torsion](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MorseNovikov/STATUS.md)
