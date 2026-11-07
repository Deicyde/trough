---
declaration: theorem
origin: cited
lean: TauCeti.isCompl_eisensteinSubspace_range_cuspToModFormCharSpace
statement: formalized
proof: formalized
---

# The cusp–Eisenstein decomposition of `M_k(N, χ)`

in weight `k ≥ 3`, the span of the
Eisenstein series of nebentypus `χ` is a complement of the image of `S_k(N, χ)` in `M_k(N, χ)`.

```lean
TauCeti.isCompl_eisensteinSubspace_range_cuspToModFormCharSpace {N k : ℕ} [NeZero N]
  (χ : (ZMod N)ˣ →* ℂˣ) (hk : 3 ≤ ↑k) :
  IsCompl (TauCeti.eisensteinSubspace χ hk) (TauCeti.cuspToModFormCharSpace (↑k) χ).range
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isCompl_eisensteinSubspace_range_cuspToModFormCharSpace`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/EisensteinSeries/Dimension.html#TauCeti.isCompl_eisensteinSubspace_range_cuspToModFormCharSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.isCompl_eisensteinSubspace_range_cuspToModFormCharSpace`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/EisensteinSeries/Dimension.html#TauCeti.isCompl_eisensteinSubspace_range_cuspToModFormCharSpace)
- [Source of `TauCeti.isCompl_eisensteinSubspace_range_cuspToModFormCharSpace` in TauCeti/NumberTheory/ModularForms/EisensteinSeries/Dimension.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/EisensteinSeries/Dimension.lean#L202)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularForms/STATUS.md)
