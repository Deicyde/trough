---
declaration: theorem
origin: cited
lean: TauCeti.isCompl_weightOneEisensteinSubspace_range_cuspToModFormCharSpace
statement: formalized
proof: formalized
---

# The weight-one cusp–Eisenstein decomposition of `M₁(N, χ)` (Diamond–Shurman, Theorem 4.8.1)

the span of the weight-one Eisenstein series of nebentypus `χ` is a complement of
the image of `S₁(N, χ)` in `M₁(N, χ)`.

```lean
TauCeti.isCompl_weightOneEisensteinSubspace_range_cuspToModFormCharSpace {N : ℕ} [NeZero N]
  (χ : (ZMod N)ˣ →* ℂˣ) :
  IsCompl (TauCeti.weightOneEisensteinSubspace χ) (TauCeti.cuspToModFormCharSpace 1 χ).range
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Möbius difference formula](../../../algebra/part-02/other-results/the-mobius-difference-formula.md)
- [The ordered Dirichlet series of a character at `s = 1`](../bounded-laplace-and-ordered-dirichlet-boundary-c/the-ordered-dirichlet-series-of-a-character-at-s.md)
- [Shimizu's inequality at two cusps](../../../analysis/part-03/complex/part-04/shimizus-inequality-at-two-cusps.md)
- [Sturm bound for subgroups of `GL(2, ℝ)` of finite relative index in `SL(2, ℤ)` with discrete strict periods](../../part-02/modular-forms/sturm-bound-for-subgroups-of-gl-2-r-of-finite-re.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isCompl_weightOneEisensteinSubspace_range_cuspToModFormCharSpace`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/EisensteinSeries/WeightOne/Dimension.html#TauCeti.isCompl_weightOneEisensteinSubspace_range_cuspToModFormCharSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.isCompl_weightOneEisensteinSubspace_range_cuspToModFormCharSpace`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/EisensteinSeries/WeightOne/Dimension.html#TauCeti.isCompl_weightOneEisensteinSubspace_range_cuspToModFormCharSpace)
- [Source of `TauCeti.isCompl_weightOneEisensteinSubspace_range_cuspToModFormCharSpace` in TauCeti/NumberTheory/ModularForms/EisensteinSeries/WeightOne/Dimension.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/EisensteinSeries/WeightOne/Dimension.lean#L631)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ModularForms/STATUS.md)
