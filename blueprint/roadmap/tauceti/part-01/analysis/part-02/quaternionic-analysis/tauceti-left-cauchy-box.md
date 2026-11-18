---
declaration: theorem
origin: cited
lean: TauCeti.left_cauchy_box
statement: formalized
proof: formalized
---

# TauCeti.left_cauchy_box

The box Cauchy theorem for a left Fueter regular function. The coefficients are ordered
`eᵢ * f`, where `eᵢ` runs through `1, i, j, k`. Only pointwise regularity in the open box and
continuity on the closed box are required, including when the box is degenerate.

```lean
TauCeti.left_cauchy_box {a b : Fin 4 → ℝ} (hab : a ≤ b) {f : Quaternion ℝ → Quaternion ℝ}
  (hc : ContinuousOn f (⇑TauCeti.Quaternion.dq '' Set.Icc a b))
  (hf :
    TauCeti.LeftFueterOn f (⇑TauCeti.Quaternion.dq '' Set.univ.pi fun i => Set.Ioo (a i) (b i))) :
  (TauCeti.boxBoundarySum a b fun i x =>
      TauCeti.Quaternion.dq (Pi.single i 1) * f (TauCeti.Quaternion.dq x)) =
    0
```

## Depends on

- [TauCeti.LeftFueterAt](tauceti-leftfueterat.md)

## Proof depends on

- [TauCeti.cauchy_box](tauceti-cauchy-box.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.left_cauchy_box`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/Cauchy.html#TauCeti.left_cauchy_box).

## Sources

- [Tau Ceti documentation: `TauCeti.left_cauchy_box`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/Cauchy.html#TauCeti.left_cauchy_box)
- [Source of `TauCeti.left_cauchy_box` in TauCeti/Analysis/Quaternion/Cauchy.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Quaternion/Cauchy.lean#L78)
- [Tau Ceti roadmap status: Quaternionic analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuaternionicAnalysis/STATUS.md)
