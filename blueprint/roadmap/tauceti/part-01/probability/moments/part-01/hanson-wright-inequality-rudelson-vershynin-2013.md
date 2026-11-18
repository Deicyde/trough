---
declaration: theorem
origin: cited
lean: TauCeti.hanson_wright
statement: formalized
proof: formalized
---

# Hanson–Wright inequality (Rudelson–Vershynin 2013, Theorem 1.1)

```lean
TauCeti.hanson_wright.{u_1} :
  ∃ c,
    0 < c ∧
      ∀ {Ω : Type u_1} [inst : MeasurableSpace Ω] (P : MeasureTheory.Measure Ω)
        [MeasureTheory.IsProbabilityMeasure P] {n : ℕ} (X : Fin n → Ω → ℝ) (K : NNReal),
        ProbabilityTheory.iIndepFun X P →
          (∀ (i : Fin n), ProbabilityTheory.HasSubgaussianMGF (X i) K P) →
            ∀ (A : Matrix (Fin n) (Fin n) ℝ) (t : ℝ),
              0 ≤ t →
                P.real
                    {ω |
                      t <
                        |((fun i => X i ω) ⬝ᵥ A.mulVec fun i => X i ω) -
                            ∫ (ω' : Ω), (fun i => X i ω') ⬝ᵥ A.mulVec fun i => X i ω' ∂P|} ≤
                  2 * Real.exp (-c * min (t ^ 2 / (↑K ^ 2 * ∑ i, ∑ j, A i j ^ 2)) (t / (↑K * ‖A‖)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Two-sided Hanson–Wright inequality](two-sided-hanson-wright-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hanson_wright`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/HansonWright.html#TauCeti.hanson_wright).

## Sources

- [Tau Ceti documentation: `TauCeti.hanson_wright`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/HansonWright.html#TauCeti.hanson_wright)
- [Source of `TauCeti.hanson_wright` in TauCeti/Probability/Moments/HansonWright.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Moments/HansonWright.lean#L627)
