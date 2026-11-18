---
declaration: theorem
origin: cited
lean: Complex.norm_inv_Gamma_add_natCast_le
statement: formalized
proof: formalized
---

# Complex.norm_inv_Gamma_add_natCast_le

On the half-plane `1 ≤ Re s`, the reciprocal Gamma function decays factorially along
`s + k`: `‖1 / Γ(s + k)‖ ≤ ‖1 / Γ(s)‖ / k!`. Together with the boundedness of `1 / Γ` on compact
sets, this gives locally uniform bounds for series with coefficients `1 / Γ(b + k)` as functions
of a complex parameter `b`.

```lean
Complex.norm_inv_Gamma_add_natCast_le {s : ℂ} (hs : 1 ≤ s.re) (k : ℕ) :
  ‖(Complex.Gamma (s + ↑k))⁻¹‖ ≤ ‖(Complex.Gamma s)⁻¹‖ / ↑k.factorial
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Complex.norm_inv_Gamma_add_natCast_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gamma/Basic.html#Complex.norm_inv_Gamma_add_natCast_le).

## Sources

- [Tau Ceti documentation: `Complex.norm_inv_Gamma_add_natCast_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gamma/Basic.html#Complex.norm_inv_Gamma_add_natCast_le)
- [Source of `Complex.norm_inv_Gamma_add_natCast_le` in TauCeti/Analysis/SpecialFunctions/Gamma/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Gamma/Basic.lean#L241)
- [Tau Ceti roadmap status: Exponential, logarithmic, error and incomplete Gamma functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsEiLiErfIncompleteGamma/STATUS.md)
