---
declaration: theorem
origin: cited
lean: TauCeti.IsFreelyIndependentElements.freeCumulantSeries_mul
statement: formalized
proof: formalized
---

# TauCeti.IsFreelyIndependentElements.freeCumulantSeries_mul

*Free cumulants of a product of free elements*: if `c i` and `c j`, for `i ≠ j`, belong to a
freely independent family for a normalised `φ`, then the free cumulant series of `c i * c j` is
the boxed convolution of the free cumulant series of `c i` and of `c j`.

```lean
TauCeti.IsFreelyIndependentElements.freeCumulantSeries_mul.{u_1, u_2, u_3} {R : Type u_1}
  {A : Type u_2} [CommRing R] [Semiring A] [Algebra R A] {φ : A →ₗ[R] R} {ι : Type u_3} {c : ι → A}
  (h : TauCeti.IsFreelyIndependentElements φ c) (hφ : φ 1 = 1) {i j : ι} (hij : i ≠ j) :
  TauCeti.freeCumulantSeries (⇑φ) (c i * c j) =
    (TauCeti.freeCumulantSeries (⇑φ) (c i)).boxedConvolution (TauCeti.freeCumulantSeries (⇑φ) (c j))
```

## Depends on

- [PowerSeries.boxedConvolution](powerseries-boxedconvolution.md)
- [TauCeti.freeCumulant](tauceti-freecumulant.md)

## Proof depends on

- [TauCeti.IsFreelyIndependent.freeCumulant_mul_eq_sum_partitionCumulant_mul_partitionCumulant](tauceti-isfreelyindependent-freecumulant-mul-eq.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsFreelyIndependentElements.freeCumulantSeries_mul`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Cumulant/BoxedConvolution/Basic.html#TauCeti.IsFreelyIndependentElements.freeCumulantSeries_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.IsFreelyIndependentElements.freeCumulantSeries_mul`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Cumulant/BoxedConvolution/Basic.html#TauCeti.IsFreelyIndependentElements.freeCumulantSeries_mul)
- [Source of `TauCeti.IsFreelyIndependentElements.freeCumulantSeries_mul` in TauCeti/Probability/FreeProbability/Cumulant/BoxedConvolution/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/FreeProbability/Cumulant/BoxedConvolution/Basic.lean#L125)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FreeProbability/STATUS.md)
