---
declaration: def
origin: cited
lean: TauCeti.ModularForm.siegelFunction
statement: formalized
---

# The Siegel function

`g_r(τ)` attached to `r = (r₁, r₂) ∈ ℝ²`:
`g_r(τ) = -e^{π i B₂(r₁) τ} e^{π i r₂ (r₁ - 1)} (1 - w) ∏_{n ≥ 1} (1 - qⁿ w) (1 - qⁿ w⁻¹)`
with `q = e^{2π i τ}`, `w = e^{2π i (r₁ τ + r₂)}` and `B₂ = bernoulliFun 2` the second Bernoulli
polynomial `x² - x + 1/6`. The product converges for `τ` in the upper half-plane, where `g_r` is
holomorphic; elsewhere the value is a junk value.

```lean
TauCeti.ModularForm.siegelFunction (r : Fin 2 → ℝ) (τ : ℂ) : ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularForm.siegelFunction`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/SiegelFunction/Basic.html#TauCeti.ModularForm.siegelFunction).

## Sources

- [Tau Ceti documentation: `TauCeti.ModularForm.siegelFunction`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/SiegelFunction/Basic.html#TauCeti.ModularForm.siegelFunction)
- [Source of `TauCeti.ModularForm.siegelFunction` in TauCeti/NumberTheory/ModularForms/SiegelFunction/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/SiegelFunction/Basic.lean#L90)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
