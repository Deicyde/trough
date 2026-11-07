---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.summingENorm_le_ofReal_iff_exists_eq_comp_codRestrict_topologicalClosure
statement: formalized
proof: formalized
---

# Pietsch factorization

through the closure of the canonical image: for a Banach space `F`,
`1 ≤ p < ∞` and `C ≥ 0`, `πₚ(T) ≤ C` iff there are a regular Borel probability measure `ν` on the
weak-star compact dual unit ball and an operator `S` of norm at most `C` on the closure of
`range jₚ` in `Lᵖ(ν)` such that `T = S ∘ jₚ`.

```lean
ContinuousLinearMap.summingENorm_le_ofReal_iff_exists_eq_comp_codRestrict_topologicalClosure.{u_1,
    u_2, u_3}
  {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [SeminormedAddCommGroup E]
  [NormedSpace 𝕜 E] [MeasurableSpace (WeakDual 𝕜 E)] [BorelSpace (WeakDual 𝕜 E)] {p : ENNReal}
  [Fact (1 ≤ p)] [NormedAddCommGroup F] [NormedSpace 𝕜 F] [CompleteSpace F] (hp : p ≠ ⊤)
  {T : E →L[𝕜] F} {C : ℝ} (hC : 0 ≤ C) :
  ContinuousLinearMap.summingENorm p T ≤ ENNReal.ofReal C ↔
    ∃ ν,
      ∃ (x : MeasureTheory.IsProbabilityMeasure ν),
        ν.Regular ∧
          ∃ S,
            ‖S‖ ≤ C ∧
              T =
                S ∘SL
                  (WeakDual.evalLp p ν).codRestrict
                    (↑(WeakDual.evalLp p ν)).range.topologicalClosure ⋯
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Pietsch domination theorem](pietsch-domination-theorem.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.summingENorm_le_ofReal_iff_exists_eq_comp_codRestrict_topologicalClosure`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Factorization.html#ContinuousLinearMap.summingENorm_le_ofReal_iff_exists_eq_comp_codRestrict_topologicalClosure).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.summingENorm_le_ofReal_iff_exists_eq_comp_codRestrict_topologicalClosure`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Factorization.html#ContinuousLinearMap.summingENorm_le_ofReal_iff_exists_eq_comp_codRestrict_topologicalClosure)
- [Source of `ContinuousLinearMap.summingENorm_le_ofReal_iff_exists_eq_comp_codRestrict_topologicalClosure` in TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Factorization.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Factorization.lean#L141)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
