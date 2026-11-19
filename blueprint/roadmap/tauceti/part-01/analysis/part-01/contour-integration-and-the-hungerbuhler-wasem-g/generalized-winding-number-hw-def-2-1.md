---
declaration: def
origin: cited
lean: TauCeti.Contour.windingNumber
statement: formalized
---

# Generalized winding number (HW Def 2.1)

`n_{z₀}(γ) = (2πi)⁻¹ · PV ∮_γ dz/(z − z₀)`, the
principal-value normalization of the index integral for a curve `γ : ℝ → ℂ` on `[a, b]` and any
point `z₀`. See `windingNumber_eq_integral_of_avoidance` for its reduction to the ordinary index
integral; as a `limUnder`-based value it is junk when the principal value does not exist.

```lean
TauCeti.Contour.windingNumber (γ : ℝ → ℂ) (a b : ℝ) (z₀ : ℂ) : ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.windingNumber`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Winding/Number/Basic.html#TauCeti.Contour.windingNumber).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.windingNumber`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Winding/Number/Basic.html#TauCeti.Contour.windingNumber)
- [Source of `TauCeti.Contour.windingNumber` in TauCeti/Analysis/Contour/Winding/Number/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Contour/Winding/Number/Basic.lean#L72)
- [Tau Ceti roadmap status: Contour integration and the Hungerbühler–Wasem generalized residue theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ContourIntegration/STATUS.md)
