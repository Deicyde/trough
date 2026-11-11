---
declaration: theorem
origin: cited
lean: TauCeti.volume_le_mul_volume_of_forall_dyadicCube, TauCeti.volume_le_mul_volume_of_subset_dyadicCube
statement: formalized
proof: formalized
---

# The Krylov–Safonov covering lemma

Let `0 < δ < 1`, and let `A ⊆ ℝⁿ`, `n ≥ 1`, be
null-measurable with finite measure. If the parent of every dyadic cube `Q` with
`δ |Q| < |A ∩ Q|` (the dyadic cube of the next level containing `Q`) lies in `B`, then
`|A| ≤ δ |B|`.

No measurability of `B` is needed. Both bounds on `δ` are necessary: for `δ ≥ 1` the hypothesis
holds with `B = ∅`, and for `δ = 0` it holds for a cube `A` with `B = ℝⁿ`.

```lean
TauCeti.volume_le_mul_volume_of_forall_dyadicCube.{u_1} {ι : Type u_1} [Fintype ι]
  {A B : Set (ι → ℝ)} {δ : ENNReal} [Nonempty ι]
  (hA : MeasureTheory.NullMeasurableSet A MeasureTheory.volume) (hA' : MeasureTheory.volume A ≠ ⊤)
  (hδ0 : δ ≠ 0) (hδ1 : δ < 1)
  (hB :
    ∀ (k : ℤ) (m m' : ι → ℤ),
      TauCeti.dyadicCube k m ⊆ TauCeti.dyadicCube (k + 1) m' →
        δ * MeasureTheory.volume (TauCeti.dyadicCube k m) <
            MeasureTheory.volume (A ∩ TauCeti.dyadicCube k m) →
          TauCeti.dyadicCube (k + 1) m' ⊆ B) :
  MeasureTheory.volume A ≤ δ * MeasureTheory.volume B
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lebesgue's differentiation theorem along dyadic cubes](../../measure/lebesgues-differentiation-theorem-along-dyadic-c.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.volume_le_mul_volume_of_forall_dyadicCube`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/CalderonZygmund/KrylovSafonov.html#TauCeti.volume_le_mul_volume_of_forall_dyadicCube).

## Other forms

**The Krylov–Safonov covering lemma in a dyadic cube.** Formalized in Tau Ceti as [`TauCeti.volume_le_mul_volume_of_subset_dyadicCube`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/CalderonZygmund/KrylovSafonov.html#TauCeti.volume_le_mul_volume_of_subset_dyadicCube).

```lean
TauCeti.volume_le_mul_volume_of_subset_dyadicCube.{u_1} {ι : Type u_1} [Fintype ι]
  {A B : Set (ι → ℝ)} {δ : ENNReal} {k₀ : ℤ} {m₀ : ι → ℤ}
  (hA : MeasureTheory.NullMeasurableSet A MeasureTheory.volume) (hδ1 : δ < 1)
  (hAQ : A ⊆ TauCeti.dyadicCube k₀ m₀)
  (hAδ : MeasureTheory.volume A ≤ δ * MeasureTheory.volume (TauCeti.dyadicCube k₀ m₀))
  (hB :
    ∀ (k : ℤ) (m m' : ι → ℤ),
      k < k₀ →
        TauCeti.dyadicCube k m ⊆ TauCeti.dyadicCube k₀ m₀ →
          TauCeti.dyadicCube k m ⊆ TauCeti.dyadicCube (k + 1) m' →
            δ * MeasureTheory.volume (TauCeti.dyadicCube k m) <
                MeasureTheory.volume (A ∩ TauCeti.dyadicCube k m) →
              TauCeti.dyadicCube (k + 1) m' ⊆ B) :
  MeasureTheory.volume A ≤ δ * MeasureTheory.volume B
```

## Sources

- [Tau Ceti documentation: `TauCeti.volume_le_mul_volume_of_forall_dyadicCube`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/CalderonZygmund/KrylovSafonov.html#TauCeti.volume_le_mul_volume_of_forall_dyadicCube)
- [Source of `TauCeti.volume_le_mul_volume_of_forall_dyadicCube` in TauCeti/MeasureTheory/Integral/CalderonZygmund/KrylovSafonov.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/CalderonZygmund/KrylovSafonov.lean#L68)
