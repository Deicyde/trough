---
declaration: theorem
origin: cited
lean: TauCeti.SU2.character_symPower_torusHom_eq_div, TauCeti.SU2.character_symPower_torusExp_eq_sin_div_sin
statement: formalized
proof: formalized
---

# The Weyl character formula for `SU(2)`

Away from the two points `z = ±1` of the maximal
torus, where the Weyl denominator vanishes, the character of `Symᵈ(ℂ²)` at `diag (z, z⁻¹)` is the
quotient of the Weyl numerator by the Weyl denominator.

```lean
TauCeti.SU2.character_symPower_torusHom_eq_div (d : ℕ) {z : Circle} (hz : ↑z ^ 2 ≠ 1) :
  (TauCeti.SU2.symPower d).character (TauCeti.SU2.torusHom z) =
    (↑z ^ (d + 1) - (↑z)⁻¹ ^ (d + 1)) / (↑z - (↑z)⁻¹)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Weyl numerator identity](the-weyl-numerator-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SU2.character_symPower_torusHom_eq_div`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SU2/Weyl/Character.html#TauCeti.SU2.character_symPower_torusHom_eq_div).

## Other forms

**The Weyl character formula in the angle parametrisation.** Formalized in Tau Ceti as [`TauCeti.SU2.character_symPower_torusExp_eq_sin_div_sin`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SU2/Weyl/Character.html#TauCeti.SU2.character_symPower_torusExp_eq_sin_div_sin).

```lean
TauCeti.SU2.character_symPower_torusExp_eq_sin_div_sin (d : ℕ) {θ : ℝ} (hθ : Real.sin θ ≠ 0) :
  (TauCeti.SU2.symPower d).character (TauCeti.SU2.torusExp θ) =
    ↑(Real.sin ((↑d + 1) * θ) / Real.sin θ)
```

## Sources

- [Tau Ceti documentation: `TauCeti.SU2.character_symPower_torusHom_eq_div`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SU2/Weyl/Character.html#TauCeti.SU2.character_symPower_torusHom_eq_div)
- [Source of `TauCeti.SU2.character_symPower_torusHom_eq_div` in TauCeti/RepresentationTheory/SU2/Weyl/Character.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/SU2/Weyl/Character.lean#L115)
