---
declaration: theorem
origin: cited
lean: TauCeti.SU2.sub_inv_mul_character_symPower_torusHom, TauCeti.SU2.sin_mul_character_symPower_torusExp
statement: formalized
proof: formalized
---

# The Weyl numerator identity

Multiplying the weight string of `Symᵈ(ℂ²)` by the Weyl
denominator `z - z⁻¹` telescopes to `z^{d+1} - z^{-(d+1)}`.

No hypothesis is needed on `z`: at the two points `z = ±1` where the denominator vanishes both
sides are `0`.

```lean
TauCeti.SU2.sub_inv_mul_character_symPower_torusHom (d : ℕ) (z : Circle) :
  (↑z - (↑z)⁻¹) * (TauCeti.SU2.symPower d).character (TauCeti.SU2.torusHom z) =
    ↑z ^ (d + 1) - (↑z)⁻¹ ^ (d + 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SU2.sub_inv_mul_character_symPower_torusHom`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SU2/Weyl/Character.html#TauCeti.SU2.sub_inv_mul_character_symPower_torusHom).

## Other forms

**The Weyl numerator identity in the angle parametrisation.** Formalized in Tau Ceti as [`TauCeti.SU2.sin_mul_character_symPower_torusExp`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SU2/Weyl/Character.html#TauCeti.SU2.sin_mul_character_symPower_torusExp).

```lean
TauCeti.SU2.sin_mul_character_symPower_torusExp (d : ℕ) (θ : ℝ) :
  ↑(Real.sin θ) * (TauCeti.SU2.symPower d).character (TauCeti.SU2.torusExp θ) =
    ↑(Real.sin ((↑d + 1) * θ))
```

## Sources

- [Tau Ceti documentation: `TauCeti.SU2.sub_inv_mul_character_symPower_torusHom`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SU2/Weyl/Character.html#TauCeti.SU2.sub_inv_mul_character_symPower_torusHom)
- [Source of `TauCeti.SU2.sub_inv_mul_character_symPower_torusHom` in TauCeti/RepresentationTheory/SU2/Weyl/Character.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/SU2/Weyl/Character.lean#L90)
