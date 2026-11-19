---
declaration: theorem
origin: cited
lean: TauCeti.eNorm_setIntegral_fst_lt_snd_le
statement: formalized
proof: formalized
---

# The Christ–Kiselev lemma, in bilinear form

Let `1 / p + 1 / r > 1` with `1 ≤ r`, and let
`β : ℝ × ℝ → G` be integrable on `{(s, t) | s < t}`. Suppose that for intervals `I` and `J` with
`I` to the left of `J`,

`‖∫_{I × J} β‖ ≤ A ‖1_I f‖_p ‖1_J g‖_r`.

Then `‖∫_{s < t} β‖ ≤ (1 - 2^{-δ})⁻¹ A ‖f‖_p ‖g‖_r`, where `δ = 1 / p + 1 / r - 1 > 0`.

For `β (s, t) = ⟪K(t, s) f(s), g(t)⟫`, the hypothesis follows from boundedness of the operator
`f ↦ ∫ K(·, s) f(s) ds` from `Lᵖ` to `L^{r'}`, and the conclusion is the boundedness of its
truncation `f ↦ ∫_{s < ·} K(·, s) f(s) ds` in weak form.

```lean
TauCeti.eNorm_setIntegral_fst_lt_snd_le.{u_1, u_2, u_3} {E : Type u_1} {F : Type u_2} {G : Type u_3}
  [TopologicalSpace E] [ESeminormedAddMonoid E] [TopologicalSpace F] [ESeminormedAddMonoid F]
  [NormedAddCommGroup G] [NormedSpace ℝ G] {p r : ENNReal} (hr : 1 ≤ r) (hpr : 1 < p⁻¹ + r⁻¹)
  {β : ℝ × ℝ → G} (hβ : MeasureTheory.IntegrableOn β {z | z.1 < z.2} MeasureTheory.volume)
  (f : ℝ → E) (g : ℝ → F) {A : ENNReal}
  (hA :
    ∀ (I J : Set ℝ),
      I.OrdConnected →
        J.OrdConnected →
          (∀ s ∈ I, ∀ t ∈ J, s < t) →
            ‖∫ (z : ℝ × ℝ) in I ×ˢ J, β z‖ₑ ≤
              A * MeasureTheory.eLpNorm (I.indicator f) p MeasureTheory.volume *
                MeasureTheory.eLpNorm (J.indicator g) r MeasureTheory.volume) :
  ‖∫ (z : ℝ × ℝ) in {z | z.1 < z.2}, β z‖ₑ ≤
    (1 - 2 ^ (-(p⁻¹ + r⁻¹ - 1).toReal))⁻¹ * A * MeasureTheory.eLpNorm f p MeasureTheory.volume *
      MeasureTheory.eLpNorm g r MeasureTheory.volume
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's inequality for disjoint pieces](../../function/part-01/holders-inequality-for-disjoint-pieces.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.eNorm_setIntegral_fst_lt_snd_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/ChristKiselev.html#TauCeti.eNorm_setIntegral_fst_lt_snd_le).

## Sources

- [Tau Ceti documentation: `TauCeti.eNorm_setIntegral_fst_lt_snd_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/ChristKiselev.html#TauCeti.eNorm_setIntegral_fst_lt_snd_le)
- [Source of `TauCeti.eNorm_setIntegral_fst_lt_snd_le` in TauCeti/MeasureTheory/Integral/ChristKiselev.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Integral/ChristKiselev.lean#L364)
