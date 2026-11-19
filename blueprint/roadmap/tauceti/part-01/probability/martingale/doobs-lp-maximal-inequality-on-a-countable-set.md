---
declaration: theorem
origin: cited
lean: MeasureTheory.Submartingale.eLpNorm_biSup_ofReal_le, MeasureTheory.Submartingale.eLpNorm_biSup_ofReal_le_mul_eLpNorm_posPart, MeasureTheory.Martingale.eLpNorm_biSup_eNorm_le
statement: formalized
proof: formalized
---

# Doob's `Lᵖ` maximal inequality on a countable set

Holds for any real submartingale `f` and
`1 < p < ∞` with no sign or `MemLp` hypothesis, since `‖(f⁺) T ω‖ ≤ ‖f T ω‖` pointwise.

```lean
MeasureTheory.Submartingale.eLpNorm_biSup_ofReal_le.{u_1, u_2} {Ω : Type u_1} {ι : Type u_2}
  {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [LinearOrder ι]
  [MeasureTheory.IsFiniteMeasure μ] {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ}
  (hf : MeasureTheory.Submartingale f ℱ μ) {S : Set ι} (hS : S.Countable) {T : ι}
  (hST : ∀ t ∈ S, t ≤ T) {p : ENNReal} (hp : 1 < p) (hp_top : p ≠ ⊤) :
  MeasureTheory.eLpNorm (fun ω => ⨆ t ∈ S, ENNReal.ofReal (f t ω)) p μ ≤
    p / (p - 1) * MeasureTheory.eLpNorm (f T) p μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Event-refined positive-part Doob inequality on a finite set](event-refined-positive-part-doob-inequality-on-a.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Submartingale.eLpNorm_biSup_ofReal_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Submartingale.eLpNorm_biSup_ofReal_le).

## Other forms

**Doob's `Lᵖ` maximal inequality on a countable set (positive-part form).** Formalized in Tau Ceti as [`MeasureTheory.Submartingale.eLpNorm_biSup_ofReal_le_mul_eLpNorm_posPart`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Submartingale.eLpNorm_biSup_ofReal_le_mul_eLpNorm_posPart).

```lean
MeasureTheory.Submartingale.eLpNorm_biSup_ofReal_le_mul_eLpNorm_posPart.{u_1, u_2} {Ω : Type u_1}
  {ι : Type u_2} {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [LinearOrder ι]
  [MeasureTheory.IsFiniteMeasure μ] {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ}
  (hf : MeasureTheory.Submartingale f ℱ μ) {S : Set ι} (hS : S.Countable) {T : ι}
  (hST : ∀ t ∈ S, t ≤ T) {p : ENNReal} (hp : 1 < p) (hp_top : p ≠ ⊤) :
  MeasureTheory.eLpNorm (fun ω => ⨆ t ∈ S, ENNReal.ofReal (f t ω)) p μ ≤
    p / (p - 1) * MeasureTheory.eLpNorm (f⁺ T) p μ
```

**Doob's `Lᵖ` maximal inequality on a countable set for Banach-valued martingales.** Formalized in Tau Ceti as [`MeasureTheory.Martingale.eLpNorm_biSup_eNorm_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Martingale.eLpNorm_biSup_eNorm_le).

```lean
MeasureTheory.Martingale.eLpNorm_biSup_eNorm_le.{u_1, u_2, u_3} {Ω : Type u_1} {E : Type u_2}
  {ι : Type u_3} {mΩ : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [CompleteSpace E] [LinearOrder ι] [MeasureTheory.IsFiniteMeasure μ]
  {ℱ : MeasureTheory.Filtration ι mΩ} {M : ι → Ω → E} (hM : MeasureTheory.Martingale M ℱ μ)
  {S : Set ι} (hS : S.Countable) {T : ι} (hST : ∀ t ∈ S, t ≤ T) {p : ENNReal} (hp : 1 < p)
  (hp_top : p ≠ ⊤) :
  MeasureTheory.eLpNorm (fun ω => ⨆ t ∈ S, ‖M t ω‖ₑ) p μ ≤
    p / (p - 1) * MeasureTheory.eLpNorm (M T) p μ
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.Submartingale.eLpNorm_biSup_ofReal_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Submartingale.eLpNorm_biSup_ofReal_le)
- [Source of `MeasureTheory.Submartingale.eLpNorm_biSup_ofReal_le` in TauCeti/Probability/Martingale/MaximalInequality/Lp.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Martingale/MaximalInequality/Lp.lean#L326)
