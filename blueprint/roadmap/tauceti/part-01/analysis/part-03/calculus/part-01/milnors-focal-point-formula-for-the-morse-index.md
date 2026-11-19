---
declaration: theorem
origin: cited
lean: TauCeti.morseIndex_norm_sq_sub_comp_eq_finsum_finrank_ker
statement: formalized
proof: formalized
---

# Milnor's focal-point formula for the Morse index of squared distance (*Morse Theory*, Lemma 6.5)

At any critical point `x` of `y ↦ ‖i y - a‖²` along a `C²` immersion `i`, the Morse
index equals the sum over `t ∈ (0, 1)` of the focal multiplicities of `i x + t • (a - i x)` at `x`
(only finitely many `t` have nonzero focal multiplicity).

```lean
TauCeti.morseIndex_norm_sq_sub_comp_eq_finsum_finrank_ker.{u_1, u_2} {V : Type u_1} {E : Type u_2}
  [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V] [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] {i : V → E} {x : V} {a : E} (hi : ContDiffAt ℝ 2 i x)
  (h : Function.Injective ⇑(fderiv ℝ i x)) (ha : i x - a ∈ (↑(fderiv ℝ i x)).rangeᗮ) :
  TauCeti.morseIndex (fun y => ‖i y - a‖ ^ 2) x =
    ∑ᶠ (t : ℝ) (_ : t ∈ Set.Ioo 0 1),
      Module.finrank ℝ ↥(↑(fderiv ℝ (fderiv ℝ fun y => ‖i y - (i x + t • (a - i x))‖ ^ 2) x)).ker
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.morseIndex_norm_sq_sub_comp_eq_finsum_finrank_ker`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/ShapeOperator.html#TauCeti.morseIndex_norm_sq_sub_comp_eq_finsum_finrank_ker).

## Sources

- [Tau Ceti documentation: `TauCeti.morseIndex_norm_sq_sub_comp_eq_finsum_finrank_ker`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/ShapeOperator.html#TauCeti.morseIndex_norm_sq_sub_comp_eq_finsum_finrank_ker)
- [Source of `TauCeti.morseIndex_norm_sq_sub_comp_eq_finsum_finrank_ker` in TauCeti/Analysis/Calculus/Morse/ShapeOperator.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/Morse/ShapeOperator.lean#L166)
