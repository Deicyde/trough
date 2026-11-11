---
declaration: theorem
origin: cited
lean: TauCeti.siegel_identity
statement: formalized
proof: formalized
---

# Siegel's identity

For `θ₁ ≠ θ₀` and `x - θ₂ y ≠ 0` in a field,
`(θ₁ - θ₂) / (θ₁ - θ₀) · (x - θ₀ y) / (x - θ₂ y) + (θ₂ - θ₀) / (θ₁ - θ₀) · (x - θ₁ y) / (x - θ₂ y)`
equals `1`. Applied to the linear factors of a binary form, it turns a Thue equation into unit
equations.

```lean
TauCeti.siegel_identity.{u_1} {F : Type u_1} [Field F] {θ₀ θ₁ θ₂ x y : F} (h : θ₁ ≠ θ₀)
  (hxy : x - θ₂ * y ≠ 0) :
  (θ₁ - θ₂) / (θ₁ - θ₀) * ((x - θ₀ * y) / (x - θ₂ * y)) +
      (θ₂ - θ₀) / (θ₁ - θ₀) * ((x - θ₁ * y) / (x - θ₂ * y)) =
    1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.siegel_identity`](https://taucetiproject.org/docs/TauCeti/Algebra/Field/LinearFractional.html#TauCeti.siegel_identity).

## Sources

- [Tau Ceti documentation: `TauCeti.siegel_identity`](https://taucetiproject.org/docs/TauCeti/Algebra/Field/LinearFractional.html#TauCeti.siegel_identity)
- [Source of `TauCeti.siegel_identity` in TauCeti/Algebra/Field/LinearFractional.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Field/LinearFractional.lean#L85)
