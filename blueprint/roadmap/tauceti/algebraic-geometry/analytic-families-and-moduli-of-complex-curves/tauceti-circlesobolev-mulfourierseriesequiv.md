---
declaration: def
origin: cited
lean: TauCeti.CircleSobolev.mulFourierSeriesEquiv
statement: formalized
---

# TauCeti.CircleSobolev.mulFourierSeriesEquiv

For a smooth function `f` on the circle that vanishes nowhere, multiplication by `f` as a
continuous linear automorphism of `H^s`, for every real `s`; its inverse is multiplication by
`f⁻¹`.

```lean
TauCeti.CircleSobolev.mulFourierSeriesEquiv.{u_1} {s : ℝ} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] [CompleteSpace E] {T : ℝ} [Fact (0 < T)] (f : AddCircle T → ℂ)
  (hf : ContDiff ℝ ↑⊤ fun x => f ↑x) (hf₀ : ∀ (x : AddCircle T), f x ≠ 0) :
  TauCeti.CircleSobolev s E ≃L[ℂ] TauCeti.CircleSobolev s E
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Peetre's inequality (`TauCeti.CircleSobolev.weight_add_le`)](peetres-inequality-tauceti-circlesobolev-weight.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CircleSobolev.mulFourierSeriesEquiv`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Multiplier.html#TauCeti.CircleSobolev.mulFourierSeriesEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.CircleSobolev.mulFourierSeriesEquiv`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Multiplier.html#TauCeti.CircleSobolev.mulFourierSeriesEquiv)
- [Source of `TauCeti.CircleSobolev.mulFourierSeriesEquiv` in TauCeti/Analysis/Sobolev/Circle/Multiplier.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/Circle/Multiplier.lean#L387)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
