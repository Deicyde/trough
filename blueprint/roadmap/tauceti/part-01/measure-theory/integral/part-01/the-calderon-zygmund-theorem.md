---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.eLpNorm_le_of_hormander, ContinuousLinearMap.eLpNorm_le_of_hormander_adjoint, ContinuousLinearMap.eLpNorm_le_of_setLIntegral_compl_closedBall_adjoint_le, ContinuousLinearMap.eLpNorm_le_of_setLIntegral_compl_closedBall_le, ContinuousLinearMap.mul_volume_lt_enorm_le_of_hormander, ContinuousLinearMap.mul_volume_lt_enorm_le_of_norm_sub_le_mul_rpow, ContinuousLinearMap.mul_volume_lt_enorm_le_of_setLIntegral_compl_closedBall_le, TauCeti.exists_eLpNorm_le_of_setLIntegral_compl_closedBall_le, ContinuousLinearMap.exists_eLpNorm_le_of_norm_sub_le_mul_rpow, ContinuousLinearMap.exists_mul_volume_lt_enorm_le_of_norm_sub_le_mul_rpow, TauCeti.exists_eLpNorm_le_of_hormander, TauCeti.exists_mul_volume_lt_enorm_le_of_hormander
statement: formalized
proof: formalized
---

# The Calderón–Zygmund theorem

**The Calderón–Zygmund theorem** for an operator given by a kernel, strong type `(p, p)` for
`1 < p < 2`. Let `T` be a bounded linear operator on `L²(ℝⁿ)` such that `T b x = ∫ K x y (b y) dy`
for almost every `x` off any closed ball outside which `b` vanishes, where the kernel `K` satisfies
Hörmander's condition `∫_{dist x y' > 2 dist y y'} ‖K x y - K x y'‖ dx ≤ B` for all `y`, `y'`.
Then for every `1 < p < 2` and every `f ∈ L²`,

`‖T f‖_p ≤ (p / (p - 1) · 2 (2ⁿ (4 ‖T‖² + 1) + 4 B) + p / (2 - p) · 4 ‖T‖²) ^ (1 / p) ‖f‖_p`.

```lean
ContinuousLinearMap.eLpNorm_le_of_hormander.{u_1, u_2, u_3} {ι : Type u_1} [Fintype ι] [Nonempty ι]
  {E : Type u_2} {F : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E]
  [NormedAddCommGroup F] [NormedSpace ℝ F] {p : ENNReal} [CompleteSpace F]
  (T :
    ↥(MeasureTheory.Lp E 2 MeasureTheory.volume) →L[ℝ] ↥(MeasureTheory.Lp F 2 MeasureTheory.volume))
  {K : (ι → ℝ) → (ι → ℝ) → E →L[ℝ] F} (hK : MeasureTheory.StronglyMeasurable (Function.uncurry K))
  {B : ENNReal}
  (hB : ∀ (y y' : ι → ℝ), ∫⁻ (x : ι → ℝ) in {x | 2 * dist y y' < dist x y'}, ‖K x y - K x y'‖ₑ ≤ B)
  (hrep :
    ∀ (b : ↥(MeasureTheory.Lp E 2 MeasureTheory.volume)) (y : ι → ℝ) (r : ℝ),
      (∀ᵐ (x : ι → ℝ), x ∉ Metric.closedBall y r → ↑↑b x = 0) →
        ∀ᵐ (x : ι → ℝ), x ∉ Metric.closedBall y r → ↑↑(T b) x = ∫ (z : ι → ℝ), (K x z) (↑↑b z))
  (hp : 1 < p) (hp₂ : p < 2) (f : ↥(MeasureTheory.Lp E 2 MeasureTheory.volume)) :
  MeasureTheory.eLpNorm (↑↑(T f)) p MeasureTheory.volume ≤
    (ENNReal.ofReal (p.toReal / (p.toReal - 1)) *
            (2 * (2 ^ Fintype.card ι * (4 * ‖T‖ₑ ^ 2 + 1) + 4 * B)) +
          ENNReal.ofReal (p.toReal / (2 - p.toReal)) * (4 * ‖T‖ₑ ^ 2)) ^
        (1 / p.toReal) *
      MeasureTheory.eLpNorm (↑↑f) p MeasureTheory.volume
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's inequality for the integral of a product](../../function/part-01/holders-inequality-for-the-integral-of-a-product.md)
- [Lebesgue's differentiation theorem along dyadic cubes](../../measure/lebesgues-differentiation-theorem-along-dyadic-c.md)
- [Minkowski's integral inequality](../part-02/minkowskis-integral-inequality.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.eLpNorm_le_of_hormander`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/CalderonZygmund/StrongType.html#ContinuousLinearMap.eLpNorm_le_of_hormander).

## Other forms

**The Calderón–Zygmund theorem.** Formalized in Tau Ceti as [`ContinuousLinearMap.eLpNorm_le_of_hormander_adjoint`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/CalderonZygmund/StrongType.html#ContinuousLinearMap.eLpNorm_le_of_hormander_adjoint).

```lean
ContinuousLinearMap.eLpNorm_le_of_hormander_adjoint.{u_1, u_4, u_5} {ι : Type u_1} [Fintype ι]
  [Nonempty ι] {p : ENNReal} {H : Type u_4} {K : Type u_5} [NormedAddCommGroup H]
  [InnerProductSpace ℝ H] [CompleteSpace H] [NormedAddCommGroup K] [InnerProductSpace ℝ K]
  [CompleteSpace K]
  (T :
    ↥(MeasureTheory.Lp H 2 MeasureTheory.volume) →L[ℝ] ↥(MeasureTheory.Lp K 2 MeasureTheory.volume))
  {k : (ι → ℝ) → (ι → ℝ) → K →L[ℝ] H} (hk : MeasureTheory.StronglyMeasurable (Function.uncurry k))
  {B : ENNReal}
  (hB : ∀ (y y' : ι → ℝ), ∫⁻ (x : ι → ℝ) in {x | 2 * dist y y' < dist x y'}, ‖k x y - k x y'‖ₑ ≤ B)
  (hrep :
    ∀ (b : ↥(MeasureTheory.Lp K 2 MeasureTheory.volume)) (y : ι → ℝ) (r : ℝ),
      (∀ᵐ (x : ι → ℝ), x ∉ Metric.closedBall y r → ↑↑b x = 0) →
        ∀ᵐ (x : ι → ℝ),
          x ∉ Metric.closedBall y r →
            ↑↑((ContinuousLinearMap.adjoint T) b) x = ∫ (z : ι → ℝ), (k x z) (↑↑b z))
  (hp : 2 < p) (hp_top : p ≠ ⊤) (f : ↥(MeasureTheory.Lp H 2 MeasureTheory.volume)) :
  MeasureTheory.eLpNorm (↑↑(T f)) p MeasureTheory.volume ≤
    (ENNReal.ofReal p.toReal * (2 * (2 ^ Fintype.card ι * (4 * ‖T‖ₑ ^ 2 + 1) + 4 * B)) +
          ENNReal.ofReal (p.toReal / (p.toReal - 2)) * (4 * ‖T‖ₑ ^ 2)) ^
        (1 - 1 / p.toReal) *
      MeasureTheory.eLpNorm (↑↑f) p MeasureTheory.volume
```

**The Calderón–Zygmund theorem, strong type `(p, p)` for `2 < p < ∞`.** Formalized in Tau Ceti as [`ContinuousLinearMap.eLpNorm_le_of_setLIntegral_compl_closedBall_adjoint_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/CalderonZygmund/StrongType.html#ContinuousLinearMap.eLpNorm_le_of_setLIntegral_compl_closedBall_adjoint_le).

```lean
ContinuousLinearMap.eLpNorm_le_of_setLIntegral_compl_closedBall_adjoint_le.{u_1, u_4, u_5}
  {ι : Type u_1} [Fintype ι] [Nonempty ι] {p : ENNReal} {H : Type u_4} {K : Type u_5}
  [NormedAddCommGroup H] [InnerProductSpace ℝ H] [CompleteSpace H] [NormedAddCommGroup K]
  [InnerProductSpace ℝ K] [CompleteSpace K]
  (T :
    ↥(MeasureTheory.Lp H 2 MeasureTheory.volume) →L[ℝ] ↥(MeasureTheory.Lp K 2 MeasureTheory.volume))
  {B : ENNReal} {c : ℝ}
  (hT :
    ∀ (b : ↥(MeasureTheory.Lp K 2 MeasureTheory.volume)) (y : ι → ℝ) (r : ℝ),
      (∀ᵐ (x : ι → ℝ), x ∉ Metric.closedBall y r → ↑↑b x = 0) →
        ∫ (x : ι → ℝ), ↑↑b x = 0 →
          ∫⁻ (x : ι → ℝ) in (Metric.closedBall y (c * r))ᶜ,
              ‖↑↑((ContinuousLinearMap.adjoint T) b) x‖ₑ ≤
            B * ∫⁻ (x : ι → ℝ), ‖↑↑b x‖ₑ)
  (hp : 2 < p) (hp_top : p ≠ ⊤) (f : ↥(MeasureTheory.Lp H 2 MeasureTheory.volume)) :
  MeasureTheory.eLpNorm (↑↑(T f)) p MeasureTheory.volume ≤
    (ENNReal.ofReal p.toReal *
            (2 *
              (2 ^ Fintype.card ι * (4 * ‖T‖ₑ ^ 2) + ENNReal.ofReal c ^ Fintype.card ι + 4 * B)) +
          ENNReal.ofReal (p.toReal / (p.toReal - 2)) * (4 * ‖T‖ₑ ^ 2)) ^
        (1 - 1 / p.toReal) *
      MeasureTheory.eLpNorm (↑↑f) p MeasureTheory.volume
```

**The Calderón–Zygmund theorem, strong type `(p, p)` for `1 < p < 2`.** Formalized in Tau Ceti as [`ContinuousLinearMap.eLpNorm_le_of_setLIntegral_compl_closedBall_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/CalderonZygmund/StrongType.html#ContinuousLinearMap.eLpNorm_le_of_setLIntegral_compl_closedBall_le).

```lean
ContinuousLinearMap.eLpNorm_le_of_setLIntegral_compl_closedBall_le.{u_1, u_2, u_3} {ι : Type u_1}
  [Fintype ι] [Nonempty ι] {E : Type u_2} {F : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [CompleteSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] {p : ENNReal}
  (T :
    ↥(MeasureTheory.Lp E 2 MeasureTheory.volume) →L[ℝ] ↥(MeasureTheory.Lp F 2 MeasureTheory.volume))
  {B : ENNReal} {c : ℝ}
  (hT :
    ∀ (b : ↥(MeasureTheory.Lp E 2 MeasureTheory.volume)) (y : ι → ℝ) (r : ℝ),
      (∀ᵐ (x : ι → ℝ), x ∉ Metric.closedBall y r → ↑↑b x = 0) →
        ∫ (x : ι → ℝ), ↑↑b x = 0 →
          ∫⁻ (x : ι → ℝ) in (Metric.closedBall y (c * r))ᶜ, ‖↑↑(T b) x‖ₑ ≤
            B * ∫⁻ (x : ι → ℝ), ‖↑↑b x‖ₑ)
  (hp : 1 < p) (hp₂ : p < 2) (f : ↥(MeasureTheory.Lp E 2 MeasureTheory.volume)) :
  MeasureTheory.eLpNorm (↑↑(T f)) p MeasureTheory.volume ≤
    (ENNReal.ofReal (p.toReal / (p.toReal - 1)) *
            (2 *
              (2 ^ Fintype.card ι * (4 * ‖T‖ₑ ^ 2) + ENNReal.ofReal c ^ Fintype.card ι + 4 * B)) +
          ENNReal.ofReal (p.toReal / (2 - p.toReal)) * (4 * ‖T‖ₑ ^ 2)) ^
        (1 / p.toReal) *
      MeasureTheory.eLpNorm (↑↑f) p MeasureTheory.volume
```

**The Calderón–Zygmund theorem for an operator given by a kernel.** Formalized in Tau Ceti as [`ContinuousLinearMap.mul_volume_lt_enorm_le_of_hormander`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/CalderonZygmund/WeakType.html#ContinuousLinearMap.mul_volume_lt_enorm_le_of_hormander).

```lean
ContinuousLinearMap.mul_volume_lt_enorm_le_of_hormander.{u_1, u_2, u_3} {ι : Type u_1} [Fintype ι]
  {E : Type u_2} {F : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E]
  [NormedAddCommGroup F] [NormedSpace ℝ F] [Nonempty ι] [CompleteSpace F]
  (T :
    ↥(MeasureTheory.Lp E 2 MeasureTheory.volume) →L[ℝ] ↥(MeasureTheory.Lp F 2 MeasureTheory.volume))
  {K : (ι → ℝ) → (ι → ℝ) → E →L[ℝ] F} (hK : MeasureTheory.StronglyMeasurable (Function.uncurry K))
  {B : ENNReal}
  (hB : ∀ (y y' : ι → ℝ), ∫⁻ (x : ι → ℝ) in {x | 2 * dist y y' < dist x y'}, ‖K x y - K x y'‖ₑ ≤ B)
  (hrep :
    ∀ (b : ↥(MeasureTheory.Lp E 2 MeasureTheory.volume)) (y : ι → ℝ) (r : ℝ),
      (∀ᵐ (x : ι → ℝ), x ∉ Metric.closedBall y r → ↑↑b x = 0) →
        ∀ᵐ (x : ι → ℝ), x ∉ Metric.closedBall y r → ↑↑(T b) x = ∫ (z : ι → ℝ), (K x z) (↑↑b z))
  (f : ↥(MeasureTheory.Lp E 2 MeasureTheory.volume)) (t : ENNReal) :
  t * MeasureTheory.volume {x | t < ‖↑↑(T f) x‖ₑ} ≤
    (2 ^ Fintype.card ι * (4 * ‖T‖ₑ ^ 2 + 1) + 4 * B) * ∫⁻ (x : ι → ℝ), ‖↑↑f x‖ₑ
```

**The Calderón–Zygmund theorem for an operator with a standard kernel.** Formalized in Tau Ceti as [`ContinuousLinearMap.mul_volume_lt_enorm_le_of_norm_sub_le_mul_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/CalderonZygmund/StandardKernel.html#ContinuousLinearMap.mul_volume_lt_enorm_le_of_norm_sub_le_mul_rpow).

```lean
ContinuousLinearMap.mul_volume_lt_enorm_le_of_norm_sub_le_mul_rpow.{u_1, u_2, u_3} {ι : Type u_1}
  [Fintype ι] {E : Type u_2} {F : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [CompleteSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F]
  (T :
    ↥(MeasureTheory.Lp E 2 MeasureTheory.volume) →L[ℝ] ↥(MeasureTheory.Lp F 2 MeasureTheory.volume))
  {K : (ι → ℝ) → (ι → ℝ) → E →L[ℝ] F} (hKm : MeasureTheory.StronglyMeasurable (Function.uncurry K))
  {C : NNReal} {δ : ℝ} (hδ : 0 < δ)
  (hK :
    ∀ (x y y' : ι → ℝ),
      2 * dist y y' < dist x y' →
        ‖K x y - K x y'‖ ≤ ↑C * (dist y y' ^ δ * dist x y' ^ (-(↑(Fintype.card ι) + δ))))
  (hrep :
    ∀ (b : ↥(MeasureTheory.Lp E 2 MeasureTheory.volume)) (y : ι → ℝ) (r : ℝ),
      (∀ᵐ (x : ι → ℝ), x ∉ Metric.closedBall y r → ↑↑b x = 0) →
        ∀ᵐ (x : ι → ℝ), x ∉ Metric.closedBall y r → ↑↑(T b) x = ∫ (z : ι → ℝ), (K x z) (↑↑b z))
  (f : ↥(MeasureTheory.Lp E 2 MeasureTheory.volume)) (t : ENNReal) :
  t * MeasureTheory.volume {x | t < ‖↑↑(T f) x‖ₑ} ≤
    (2 ^ Fintype.card ι * (4 * ‖T‖ₑ ^ 2 + 1) +
        4 * (↑C * ENNReal.ofReal (4 ^ Fintype.card ι / (2 ^ δ - 1)))) *
      ∫⁻ (x : ι → ℝ), ‖↑↑f x‖ₑ
```

**The Calderón–Zygmund theorem, weak type `(1, 1)`.** Formalized in Tau Ceti as [`ContinuousLinearMap.mul_volume_lt_enorm_le_of_setLIntegral_compl_closedBall_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/CalderonZygmund/WeakType.html#ContinuousLinearMap.mul_volume_lt_enorm_le_of_setLIntegral_compl_closedBall_le).

```lean
ContinuousLinearMap.mul_volume_lt_enorm_le_of_setLIntegral_compl_closedBall_le.{u_1, u_2, u_3}
  {ι : Type u_1} [Fintype ι] {E : Type u_2} {F : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [CompleteSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] [Nonempty ι]
  (T :
    ↥(MeasureTheory.Lp E 2 MeasureTheory.volume) →L[ℝ] ↥(MeasureTheory.Lp F 2 MeasureTheory.volume))
  {B : ENNReal} {c : ℝ}
  (hT :
    ∀ (b : ↥(MeasureTheory.Lp E 2 MeasureTheory.volume)) (y : ι → ℝ) (r : ℝ),
      (∀ᵐ (x : ι → ℝ), x ∉ Metric.closedBall y r → ↑↑b x = 0) →
        ∫ (x : ι → ℝ), ↑↑b x = 0 →
          ∫⁻ (x : ι → ℝ) in (Metric.closedBall y (c * r))ᶜ, ‖↑↑(T b) x‖ₑ ≤
            B * ∫⁻ (x : ι → ℝ), ‖↑↑b x‖ₑ)
  (f : ↥(MeasureTheory.Lp E 2 MeasureTheory.volume)) (t : ENNReal) :
  t * MeasureTheory.volume {x | t < ‖↑↑(T f) x‖ₑ} ≤
    (2 ^ Fintype.card ι * (4 * ‖T‖ₑ ^ 2) + ENNReal.ofReal c ^ Fintype.card ι + 4 * B) *
      ∫⁻ (x : ι → ℝ), ‖↑↑f x‖ₑ
```

**The Calderón–Zygmund theorem.** Formalized in Tau Ceti as [`TauCeti.exists_eLpNorm_le_of_setLIntegral_compl_closedBall_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/CalderonZygmund/StrongType.html#TauCeti.exists_eLpNorm_le_of_setLIntegral_compl_closedBall_le).

```lean
TauCeti.exists_eLpNorm_le_of_setLIntegral_compl_closedBall_le.{u_1, u_2, u_3} {ι : Type u_1}
  [Fintype ι] [Nonempty ι] {H : Type u_2} {K : Type u_3} [NormedAddCommGroup H]
  [InnerProductSpace ℝ H] [CompleteSpace H] [NormedAddCommGroup K] [InnerProductSpace ℝ K]
  [CompleteSpace K] {p : ENNReal} (c : ℝ) {M B B' : ENNReal} (hM : M ≠ ⊤) (hB : B ≠ ⊤)
  (hB' : B' ≠ ⊤) (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀
      (T :
        ↥(MeasureTheory.Lp H 2 MeasureTheory.volume) →L[ℝ]
          ↥(MeasureTheory.Lp K 2 MeasureTheory.volume)),
      ‖T‖ₑ ≤ M →
        (∀ (b : ↥(MeasureTheory.Lp H 2 MeasureTheory.volume)) (y : ι → ℝ) (r : ℝ),
            (∀ᵐ (x : ι → ℝ), x ∉ Metric.closedBall y r → ↑↑b x = 0) →
              ∫ (x : ι → ℝ), ↑↑b x = 0 →
                ∫⁻ (x : ι → ℝ) in (Metric.closedBall y (c * r))ᶜ, ‖↑↑(T b) x‖ₑ ≤
                  B * ∫⁻ (x : ι → ℝ), ‖↑↑b x‖ₑ) →
          (∀ (b : ↥(MeasureTheory.Lp K 2 MeasureTheory.volume)) (y : ι → ℝ) (r : ℝ),
              (∀ᵐ (x : ι → ℝ), x ∉ Metric.closedBall y r → ↑↑b x = 0) →
                ∫ (x : ι → ℝ), ↑↑b x = 0 →
                  ∫⁻ (x : ι → ℝ) in (Metric.closedBall y (c * r))ᶜ,
                      ‖↑↑((ContinuousLinearMap.adjoint T) b) x‖ₑ ≤
                    B' * ∫⁻ (x : ι → ℝ), ‖↑↑b x‖ₑ) →
            ∀ (f : ↥(MeasureTheory.Lp H 2 MeasureTheory.volume)),
              MeasureTheory.eLpNorm (↑↑(T f)) p MeasureTheory.volume ≤
                ↑C * MeasureTheory.eLpNorm (↑↑f) p MeasureTheory.volume
```

**The Calderón–Zygmund theorem on an inner product space, strong type `(p, p)` for `1 < p < ∞`.** Formalized in Tau Ceti as [`ContinuousLinearMap.exists_eLpNorm_le_of_norm_sub_le_mul_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/CalderonZygmund/InnerProductSpace.html#ContinuousLinearMap.exists_eLpNorm_le_of_norm_sub_le_mul_rpow).

```lean
ContinuousLinearMap.exists_eLpNorm_le_of_norm_sub_le_mul_rpow.{u_1, u_4, u_5} {V : Type u_1}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [MeasurableSpace V] [BorelSpace V]
  [FiniteDimensional ℝ V] {H : Type u_4} {K : Type u_5} [NormedAddCommGroup H]
  [InnerProductSpace ℝ H] [CompleteSpace H] [NormedAddCommGroup K] [InnerProductSpace ℝ K]
  [CompleteSpace K] {p : ENNReal} [Nontrivial V]
  (T :
    ↥(MeasureTheory.Lp H 2 MeasureTheory.volume) →L[ℝ] ↥(MeasureTheory.Lp K 2 MeasureTheory.volume))
  {k : V → V → H →L[ℝ] K} (hkm : MeasureTheory.StronglyMeasurable (Function.uncurry k))
  {k' : V → V → K →L[ℝ] H} (hk'm : MeasureTheory.StronglyMeasurable (Function.uncurry k'))
  {C₀ C C₀' C' : NNReal} {δ δ' : ℝ} (hδ : 0 < δ) (hδ' : 0 < δ')
  (hsize : ∀ (x y : V), x ≠ y → ‖k x y‖ ≤ ↑C₀ * dist x y ^ (-↑(Module.finrank ℝ V)))
  (hsize' : ∀ (x y : V), x ≠ y → ‖k' x y‖ ≤ ↑C₀' * dist x y ^ (-↑(Module.finrank ℝ V)))
  (hk :
    ∀ (x y y' : V),
      2 * dist y y' < dist x y' →
        ‖k x y - k x y'‖ ≤ ↑C * (dist y y' ^ δ * dist x y' ^ (-(↑(Module.finrank ℝ V) + δ))))
  (hk' :
    ∀ (x y y' : V),
      2 * dist y y' < dist x y' →
        ‖k' x y - k' x y'‖ ≤ ↑C' * (dist y y' ^ δ' * dist x y' ^ (-(↑(Module.finrank ℝ V) + δ'))))
  (hrep :
    ∀ (f : ↥(MeasureTheory.Lp H 2 MeasureTheory.volume)) (s : Set V),
      IsCompact s →
        (∀ᵐ (x : V), x ∉ s → ↑↑f x = 0) →
          ∀ᵐ (x : V), x ∉ s → ↑↑(T f) x = ∫ (z : V), (k x z) (↑↑f z))
  (hrep' :
    ∀ (f : ↥(MeasureTheory.Lp K 2 MeasureTheory.volume)) (s : Set V),
      IsCompact s →
        (∀ᵐ (x : V), x ∉ s → ↑↑f x = 0) →
          ∀ᵐ (x : V), x ∉ s → ↑↑((ContinuousLinearMap.adjoint T) f) x = ∫ (z : V), (k' x z) (↑↑f z))
  (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ (f : ↥(MeasureTheory.Lp H 2 MeasureTheory.volume)),
      MeasureTheory.eLpNorm (↑↑(T f)) p MeasureTheory.volume ≤
        ↑C * MeasureTheory.eLpNorm (↑↑f) p MeasureTheory.volume
```

**The Calderón–Zygmund theorem on an inner product space, weak type `(1, 1)`.** Formalized in Tau Ceti as [`ContinuousLinearMap.exists_mul_volume_lt_enorm_le_of_norm_sub_le_mul_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/CalderonZygmund/InnerProductSpace.html#ContinuousLinearMap.exists_mul_volume_lt_enorm_le_of_norm_sub_le_mul_rpow).

```lean
ContinuousLinearMap.exists_mul_volume_lt_enorm_le_of_norm_sub_le_mul_rpow.{u_1, u_2, u_3}
  {V : Type u_1} [NormedAddCommGroup V] [InnerProductSpace ℝ V] [MeasurableSpace V] [BorelSpace V]
  [FiniteDimensional ℝ V] {E : Type u_2} {F : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [CompleteSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] [Nontrivial V]
  (T :
    ↥(MeasureTheory.Lp E 2 MeasureTheory.volume) →L[ℝ] ↥(MeasureTheory.Lp F 2 MeasureTheory.volume))
  {k : V → V → E →L[ℝ] F} (hkm : MeasureTheory.StronglyMeasurable (Function.uncurry k))
  {C₀ C : NNReal} {δ : ℝ} (hδ : 0 < δ)
  (hsize : ∀ (x y : V), x ≠ y → ‖k x y‖ ≤ ↑C₀ * dist x y ^ (-↑(Module.finrank ℝ V)))
  (hk :
    ∀ (x y y' : V),
      2 * dist y y' < dist x y' →
        ‖k x y - k x y'‖ ≤ ↑C * (dist y y' ^ δ * dist x y' ^ (-(↑(Module.finrank ℝ V) + δ))))
  (hrep :
    ∀ (f : ↥(MeasureTheory.Lp E 2 MeasureTheory.volume)) (s : Set V),
      IsCompact s →
        (∀ᵐ (x : V), x ∉ s → ↑↑f x = 0) →
          ∀ᵐ (x : V), x ∉ s → ↑↑(T f) x = ∫ (z : V), (k x z) (↑↑f z)) :
  ∃ A,
    ∀ (f : ↥(MeasureTheory.Lp E 2 MeasureTheory.volume)) (t : ENNReal),
      t * MeasureTheory.volume {x | t < ‖↑↑(T f) x‖ₑ} ≤ ↑A * ∫⁻ (x : V), ‖↑↑f x‖ₑ
```

**The Calderón–Zygmund theorem on an inner product space under Hörmander's condition.** Formalized in Tau Ceti as [`TauCeti.exists_eLpNorm_le_of_hormander`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/CalderonZygmund/InnerProductSpace.html#TauCeti.exists_eLpNorm_le_of_hormander).

```lean
TauCeti.exists_eLpNorm_le_of_hormander.{u_1, u_4, u_5} {V : Type u_1} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [MeasurableSpace V] [BorelSpace V] [FiniteDimensional ℝ V] {H : Type u_4}
  {K : Type u_5} [NormedAddCommGroup H] [InnerProductSpace ℝ H] [CompleteSpace H]
  [NormedAddCommGroup K] [InnerProductSpace ℝ K] [CompleteSpace K] {p : ENNReal} [Nontrivial V]
  {M B B' : ENNReal} (hM : M ≠ ⊤) (hB : B ≠ ⊤) (hB' : B' ≠ ⊤) (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀
      (T :
        ↥(MeasureTheory.Lp H 2 MeasureTheory.volume) →L[ℝ]
          ↥(MeasureTheory.Lp K 2 MeasureTheory.volume))
      (k : V → V → H →L[ℝ] K) (k' : V → V → K →L[ℝ] H),
      ‖T‖ₑ ≤ M →
        MeasureTheory.StronglyMeasurable (Function.uncurry k) →
          MeasureTheory.StronglyMeasurable (Function.uncurry k') →
            (∀ (y y' : V), ∫⁻ (x : V) in {x | 2 * dist y y' < dist x y'}, ‖k x y - k x y'‖ₑ ≤ B) →
              (∀ (y y' : V),
                  ∫⁻ (x : V) in {x | 2 * dist y y' < dist x y'}, ‖k' x y - k' x y'‖ₑ ≤ B') →
                (∀ (f : ↥(MeasureTheory.Lp H 2 MeasureTheory.volume)) (s : Set V),
                    IsCompact s →
                      (∀ᵐ (x : V), x ∉ s → ↑↑f x = 0) →
                        ∀ᵐ (x : V), x ∉ s → ↑↑(T f) x = ∫ (z : V), (k x z) (↑↑f z)) →
                  (∀ (f : ↥(MeasureTheory.Lp K 2 MeasureTheory.volume)) (s : Set V),
                      IsCompact s →
                        (∀ᵐ (x : V), x ∉ s → ↑↑f x = 0) →
                          ∀ᵐ (x : V),
                            x ∉ s →
                              ↑↑((ContinuousLinearMap.adjoint T) f) x =
                                ∫ (z : V), (k' x z) (↑↑f z)) →
                    ∀ (f : ↥(MeasureTheory.Lp H 2 MeasureTheory.volume)),
                      MeasureTheory.eLpNorm (↑↑(T f)) p MeasureTheory.volume ≤
                        ↑C * MeasureTheory.eLpNorm (↑↑f) p MeasureTheory.volume
```

**The Calderón–Zygmund theorem on an inner product space under Hörmander's condition.** Formalized in Tau Ceti as [`TauCeti.exists_mul_volume_lt_enorm_le_of_hormander`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/CalderonZygmund/InnerProductSpace.html#TauCeti.exists_mul_volume_lt_enorm_le_of_hormander).

```lean
TauCeti.exists_mul_volume_lt_enorm_le_of_hormander.{u_1, u_2, u_3} {V : Type u_1}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [MeasurableSpace V] [BorelSpace V]
  [FiniteDimensional ℝ V] {E : Type u_2} {F : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [CompleteSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] [Nontrivial V]
  {M B : ENNReal} (hM : M ≠ ⊤) (hB : B ≠ ⊤) :
  ∃ A,
    ∀
      (T :
        ↥(MeasureTheory.Lp E 2 MeasureTheory.volume) →L[ℝ]
          ↥(MeasureTheory.Lp F 2 MeasureTheory.volume))
      (k : V → V → E →L[ℝ] F),
      ‖T‖ₑ ≤ M →
        MeasureTheory.StronglyMeasurable (Function.uncurry k) →
          (∀ (y y' : V), ∫⁻ (x : V) in {x | 2 * dist y y' < dist x y'}, ‖k x y - k x y'‖ₑ ≤ B) →
            (∀ (f : ↥(MeasureTheory.Lp E 2 MeasureTheory.volume)) (s : Set V),
                IsCompact s →
                  (∀ᵐ (x : V), x ∉ s → ↑↑f x = 0) →
                    ∀ᵐ (x : V), x ∉ s → ↑↑(T f) x = ∫ (z : V), (k x z) (↑↑f z)) →
              ∀ (f : ↥(MeasureTheory.Lp E 2 MeasureTheory.volume)) (t : ENNReal),
                t * MeasureTheory.volume {x | t < ‖↑↑(T f) x‖ₑ} ≤ ↑A * ∫⁻ (x : V), ‖↑↑f x‖ₑ
```

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.eLpNorm_le_of_hormander`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/CalderonZygmund/StrongType.html#ContinuousLinearMap.eLpNorm_le_of_hormander)
- [Source of `ContinuousLinearMap.eLpNorm_le_of_hormander` in TauCeti/MeasureTheory/Integral/CalderonZygmund/StrongType.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/CalderonZygmund/StrongType.lean#L110)
