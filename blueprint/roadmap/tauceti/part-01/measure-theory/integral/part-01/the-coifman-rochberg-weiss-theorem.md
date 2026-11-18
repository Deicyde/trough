---
declaration: theorem
origin: cited
lean: TauCeti.exists_eLpNorm_smul_sub_le_of_norm_sub_le_mul_rpow
statement: formalized
proof: formalized
---

# The Coifman–Rochberg–Weiss theorem

Let `1 ≤ s < p`, `δ > 0`, and let `A`, `Aₚ`, `C₀` be
constants. There is a constant `C`, depending only on these and the dimension `n`, with the
following property on `ℝⁿ = ι → ℝ` with the sup distance.

Let `T` be a bounded linear operator on `L²` such that `T h x = ∫ K x z (h z) dz` for almost every
`x` in any ball on which `h` vanishes, where the kernel satisfies the standard smoothness estimate
in its first variable,

`‖K x y - K x' y‖ ≤ C₀ dist x x' ^ δ dist y x' ^ (-(n + δ))` whenever `dist y x' > 2 dist x x'`,

and such that `‖T h‖_s ≤ A ‖h‖_s` and `‖T h‖_p ≤ Aₚ ‖h‖_p` for `h ∈ L²`. Let `b` be almost
everywhere strongly measurable with `‖b‖_{BMO} ≤ M`, and let `f, g ∈ L²` with `g = b f`. Then the
commutator
`[b, T] f = b T f - T (b f)` satisfies

`‖[b, T] f‖_p ≤ C M ‖f‖_p`.

Calderón–Zygmund operators with a standard kernel whose adjoint also has one satisfy the hypotheses
for every `1 < s < p < ∞`, with the `Lˢ` and `Lᵖ` bounds supplied by the Calderón–Zygmund theorem.
Since `T` is only given on `L²`, the commutator is stated for `f ∈ L²` with `b f ∈ L²`; neither
`f ∈ Lᵖ` nor any integrability of the commutator is assumed.

```lean
TauCeti.exists_eLpNorm_smul_sub_le_of_norm_sub_le_mul_rpow.{u_1, u_2, u_4} {ι : Type u_1}
  [Fintype ι] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] {F : Type u_4}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] {s p : ℝ} (hs : 1 ≤ s) (hsp : s < p)
  (A Aₚ C₀ : NNReal) {δ : ℝ} (hδ : 0 < δ) :
  ∃ C,
    ∀
      (T :
        ↥(MeasureTheory.Lp E 2 MeasureTheory.volume) →L[ℝ]
          ↥(MeasureTheory.Lp F 2 MeasureTheory.volume))
      {K : (ι → ℝ) → (ι → ℝ) → E →L[ℝ] F},
      (∀ (x : ι → ℝ), MeasureTheory.AEStronglyMeasurable (K x) MeasureTheory.volume) →
        (∀ (x x' y : ι → ℝ),
            2 * dist x x' < dist y x' →
              ‖K x y - K x' y‖ ≤ ↑C₀ * (dist x x' ^ δ * dist y x' ^ (-(↑(Fintype.card ι) + δ)))) →
          (∀ (h : ↥(MeasureTheory.Lp E 2 MeasureTheory.volume)) (y : ι → ℝ) (ρ : ℝ),
              (∀ᵐ (z : ι → ℝ), z ∈ Metric.ball y ρ → ↑↑h z = 0) →
                ∀ᵐ (x : ι → ℝ), x ∈ Metric.ball y ρ → ↑↑(T h) x = ∫ (z : ι → ℝ), (K x z) (↑↑h z)) →
            (∀ (h : ↥(MeasureTheory.Lp E 2 MeasureTheory.volume)),
                MeasureTheory.eLpNorm (↑↑(T h)) (ENNReal.ofReal s) MeasureTheory.volume ≤
                  ↑A * MeasureTheory.eLpNorm (↑↑h) (ENNReal.ofReal s) MeasureTheory.volume) →
              (∀ (h : ↥(MeasureTheory.Lp E 2 MeasureTheory.volume)),
                  MeasureTheory.eLpNorm (↑↑(T h)) (ENNReal.ofReal p) MeasureTheory.volume ≤
                    ↑Aₚ * MeasureTheory.eLpNorm (↑↑h) (ENNReal.ofReal p) MeasureTheory.volume) →
                ∀ {b : (ι → ℝ) → ℝ} {M : NNReal},
                  MeasureTheory.AEStronglyMeasurable b MeasureTheory.volume →
                    TauCeti.bmoSeminorm b MeasureTheory.volume ≤ ↑M →
                      ∀ (f g : ↥(MeasureTheory.Lp E 2 MeasureTheory.volume)),
                        (↑↑g =ᵐ[MeasureTheory.volume] fun y => b y • ↑↑f y) →
                          MeasureTheory.eLpNorm (fun y => b y • ↑↑(T f) y - ↑↑(T g) y)
                              (ENNReal.ofReal p) MeasureTheory.volume ≤
                            ↑C * ↑M *
                              MeasureTheory.eLpNorm (↑↑f) (ENNReal.ofReal p) MeasureTheory.volume
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Fefferman–Stein inequality](the-fefferman-stein-inequality.md)
- [The Hardy–Littlewood maximal inequality](the-hardy-littlewood-maximal-inequality.md)
- [Jensen's inequality for the square of a mean](../part-02/jensens-inequality-for-the-square-of-a-mean.md)
- [Lebesgue's differentiation theorem along dyadic cubes](../../measure/lebesgues-differentiation-theorem-along-dyadic-c.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_eLpNorm_smul_sub_le_of_norm_sub_le_mul_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/CalderonZygmund/Commutator.html#TauCeti.exists_eLpNorm_smul_sub_le_of_norm_sub_le_mul_rpow).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_eLpNorm_smul_sub_le_of_norm_sub_le_mul_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/CalderonZygmund/Commutator.html#TauCeti.exists_eLpNorm_smul_sub_le_of_norm_sub_le_mul_rpow)
- [Source of `TauCeti.exists_eLpNorm_smul_sub_le_of_norm_sub_le_mul_rpow` in TauCeti/MeasureTheory/Integral/CalderonZygmund/Commutator.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Integral/CalderonZygmund/Commutator.lean#L779)
