---
declaration: theorem
origin: cited
lean: Complex.prod_Gamma_add_div
statement: formalized
proof: formalized
---

# Gauss's multiplication formula (DLMF 5.5.6) for every `s : ℂ`

`∏_{k<m} Γ(s + k/m) = (2π)^{(m-1)/2} m^{1/2 - ms} Γ(ms)`.

```lean
Complex.prod_Gamma_add_div {m : ℕ} (hm : 0 < m) (s : ℂ) :
  ∏ k ∈ Finset.range m, Complex.Gamma (s + ↑k / ↑m) =
    (2 * ↑Real.pi) ^ ((↑m - 1) / 2) * ↑m ^ (1 / 2 - ↑m * s) * Complex.Gamma (↑m * s)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Real.prod_sin_pi_mul_div](real-prod-sin-pi-mul-div.md)

## Lean

Formalized in Tau Ceti as [`Complex.prod_Gamma_add_div`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gamma/Multiplication.html#Complex.prod_Gamma_add_div).

## Sources

- [Tau Ceti documentation: `Complex.prod_Gamma_add_div`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gamma/Multiplication.html#Complex.prod_Gamma_add_div)
- [Source of `Complex.prod_Gamma_add_div` in TauCeti/Analysis/SpecialFunctions/Gamma/Multiplication.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Gamma/Multiplication.lean#L335)
- [Tau Ceti roadmap status: Airy and Scorer functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsAiry/STATUS.md)
