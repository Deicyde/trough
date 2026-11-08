---
declaration: def
origin: cited
lean: TauCeti.qTheta
statement: formalized
---

# TauCeti.qTheta

The **theta product** `θ_q(w) = (w; q)_∞ (q w⁻¹; q)_∞`, written as
`(1 - w) ∏_{n ≥ 1} (1 - qⁿ w) (1 - qⁿ w⁻¹)`. The product converges for `‖q‖ < 1`; otherwise the
value is a junk value. With `q = e^{2π i τ}` and `w = e^{2π i (r₁ τ + r₂)}` it is the product in
the Siegel function `g_r(τ)`.

```lean
TauCeti.qTheta.{u_1} {𝕜 : Type u_1} [NormedField 𝕜] (q w : 𝕜) : 𝕜
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.qTheta`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/QPochhammer.html#TauCeti.qTheta).

## Sources

- [Tau Ceti documentation: `TauCeti.qTheta`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/QPochhammer.html#TauCeti.qTheta)
- [Source of `TauCeti.qTheta` in TauCeti/Analysis/SpecialFunctions/QPochhammer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/QPochhammer.lean#L146)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
