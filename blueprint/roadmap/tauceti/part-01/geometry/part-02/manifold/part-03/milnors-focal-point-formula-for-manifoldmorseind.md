---
declaration: theorem
origin: cited
lean: TauCeti.manifoldMorseIndex_norm_sq_sub_comp_eq_finsum_finrank_ker
statement: formalized
proof: formalized
---

# Milnor's focal-point formula for `manifoldMorseIndex` (Lemma 6.5)

At any critical point
`x` (`i x - a ∈ normalSubspace I i x`) of `y ↦ ‖i y - a‖²` along a `C²` immersion `i : M → V`
(degenerate or not), the manifold Morse index equals the sum over `t ∈ (0, 1)` of the focal
multiplicities of `i x + t • (a - i x)` at `x`, measured by the nullity of `criticalHessian`.

```lean
TauCeti.manifoldMorseIndex_norm_sq_sub_comp_eq_finsum_finrank_ker.{u_1, u_2, u_3, u_4}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} {V : Type u_4} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [I.Boundaryless] [TopologicalSpace M] [ChartedSpace H M] [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] {i : M → V} {x : M} {a : V}
  (hi : ContMDiffAt I (modelWithCornersSelf ℝ V) 2 i x) (h : Function.Injective ⇑(d% i x))
  (ha : i x - a ∈ TauCeti.normalSubspace I i x) :
  TauCeti.manifoldMorseIndex I (fun y => ‖i y - a‖ ^ 2) x =
    ∑ᶠ (t : ℝ) (_ : t ∈ Set.Ioo 0 1),
      Module.finrank ℝ
        ↥(↑(TauCeti.criticalHessian I (fun y => ‖i y - (i x + t • (a - i x))‖ ^ 2) x)).ker
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Milnor's focal-point formula for the Morse index of squared distance (*Morse Theory*, Lemma 6.5)](../../../../analysis/part-03/calculus/part-01/milnors-focal-point-formula-for-the-morse-index.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.manifoldMorseIndex_norm_sq_sub_comp_eq_finsum_finrank_ker`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Immersion/ShapeOperator.html#TauCeti.manifoldMorseIndex_norm_sq_sub_comp_eq_finsum_finrank_ker).

## Sources

- [Tau Ceti documentation: `TauCeti.manifoldMorseIndex_norm_sq_sub_comp_eq_finsum_finrank_ker`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Immersion/ShapeOperator.html#TauCeti.manifoldMorseIndex_norm_sq_sub_comp_eq_finsum_finrank_ker)
- [Source of `TauCeti.manifoldMorseIndex_norm_sq_sub_comp_eq_finsum_finrank_ker` in TauCeti/Geometry/Manifold/Immersion/ShapeOperator.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Immersion/ShapeOperator.lean#L561)
