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
- [Source of `Complex.norm_inv_Gamma_add_natCast_le` in TauCeti/Analysis/SpecialFunctions/Gamma/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/Gamma/Basic.lean#L233)
- [Tau Ceti roadmap status: Exponential, logarithmic, error and incomplete Gamma functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpecialFunctionsEiLiErfIncompleteGamma/STATUS.md)
