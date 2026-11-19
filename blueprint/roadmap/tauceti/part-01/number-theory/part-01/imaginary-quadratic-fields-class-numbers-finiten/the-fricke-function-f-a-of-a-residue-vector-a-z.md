---
declaration: def
origin: cited
lean: TauCeti.frickeFunction
statement: formalized
---

# The Fricke function `f_a` of a residue vector `a ∈ (ℤ/Nℤ)²`

the weight-two division
value `N⁻² ℘((a₀ τ + a₁) / N; ℤ τ + ℤ)` multiplied by the weight `-2` factor `E₄ E₆ / Δ` and
by `(2πi)⁻²`. It is a modular function of weight zero for `Γ(N)`.

```lean
TauCeti.frickeFunction {N : ℕ} [NeZero N] (a : Fin 2 → ZMod N) (τ : UpperHalfPlane) : ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.frickeFunction`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/FunctionField/Fricke.html#TauCeti.frickeFunction).

## Sources

- [Tau Ceti documentation: `TauCeti.frickeFunction`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/FunctionField/Fricke.html#TauCeti.frickeFunction)
- [Source of `TauCeti.frickeFunction` in TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/FunctionField/Fricke.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/FunctionField/Fricke.lean#L93)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
