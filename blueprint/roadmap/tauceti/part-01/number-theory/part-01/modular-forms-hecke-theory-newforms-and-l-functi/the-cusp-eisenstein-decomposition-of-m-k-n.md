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

## Proof depends on

- [The Lipschitz formula along residue classes](../../part-02/modular-forms/the-lipschitz-formula-along-residue-classes.md)
- [The Möbius difference formula](../../../algebra/part-02/other-results/the-mobius-difference-formula.md)
- [Shimizu's inequality at two cusps](../../../analysis/part-02/complex/part-03/shimizus-inequality-at-two-cusps.md)
- [Sturm bound for subgroups of `GL(2, ℝ)` of finite relative index in `SL(2, ℤ)` with discrete strict periods](../../part-02/modular-forms/sturm-bound-for-subgroups-of-gl-2-r-of-finite-re.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isCompl_eisensteinSubspace_range_cuspToModFormCharSpace`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/EisensteinSeries/Dimension.html#TauCeti.isCompl_eisensteinSubspace_range_cuspToModFormCharSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.isCompl_eisensteinSubspace_range_cuspToModFormCharSpace`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/EisensteinSeries/Dimension.html#TauCeti.isCompl_eisensteinSubspace_range_cuspToModFormCharSpace)
- [Source of `TauCeti.isCompl_eisensteinSubspace_range_cuspToModFormCharSpace` in TauCeti/NumberTheory/ModularForms/EisensteinSeries/Dimension.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/EisensteinSeries/Dimension.lean#L202)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ModularForms/STATUS.md)
