---
declaration: def
origin: cited
lean: TauCeti.rectifiableSignedArea
statement: formalized
---

# TauCeti.rectifiableSignedArea

The **geometric signed area** of a plane curve `γ` on `[a, b]`: the geometric integral
`TauCeti.rectifiableCurveIntegral` of the area form `(x dy - y dx) / 2` along `γ`, computed along
the natural parameterization of `γ` on its length interval. For a continuous curve of bounded
variation it is invariant under increasing continuous reparametrizations, and it agrees with
`TauCeti.signedArea` for absolutely continuous curves
(`AbsolutelyContinuousOnInterval.rectifiableSignedArea_eq_signedArea`). It is zero for a curve of
infinite length on `[a, b]` and for `b < a`.

```lean
TauCeti.rectifiableSignedArea (γ : ℝ → ℂ) (a b : ℝ) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.rectifiableSignedArea`](https://taucetiproject.org/docs/TauCeti/Analysis/Green/Examples/CurveArea/RectifiableSignedArea.html#TauCeti.rectifiableSignedArea).

## Sources

- [Tau Ceti documentation: `TauCeti.rectifiableSignedArea`](https://taucetiproject.org/docs/TauCeti/Analysis/Green/Examples/CurveArea/RectifiableSignedArea.html#TauCeti.rectifiableSignedArea)
- [Source of `TauCeti.rectifiableSignedArea` in TauCeti/Analysis/Green/Examples/CurveArea/RectifiableSignedArea.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Green/Examples/CurveArea/RectifiableSignedArea.lean#L52)
- [Tau Ceti roadmap status: Euclidean isoperimetry, sharp inequalities, and rigidity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Isoperimetry/STATUS.md)
