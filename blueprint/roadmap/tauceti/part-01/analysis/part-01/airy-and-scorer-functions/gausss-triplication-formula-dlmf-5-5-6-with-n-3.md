---
declaration: theorem
origin: cited
lean: Complex.Gamma_mul_Gamma_add_third
statement: formalized
proof: formalized
---

# Gauss's triplication formula (DLMF 5.5.6 with `n = 3`)

for every `z : ℂ`,
`Γ(z) Γ(z + ⅓) Γ(z + ⅔) = 2π 3^{½ − 3z} Γ(3z)`. Both sides vanish at the poles of `Γ`, under
Mathlib's convention `Γ(−n) = 0`.

```lean
Complex.Gamma_mul_Gamma_add_third (z : ℂ) :
  Complex.Gamma z * Complex.Gamma (z + 1 / 3) * Complex.Gamma (z + 2 / 3) =
    2 * ↑Real.pi * 3 ^ (1 / 2 - 3 * z) * Complex.Gamma (3 * z)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gauss's multiplication formula (DLMF 5.5.6) for every `s : ℂ`](gausss-multiplication-formula-dlmf-5-5-6-for-eve.md)

## Lean

Formalized in Tau Ceti as [`Complex.Gamma_mul_Gamma_add_third`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gamma/Multiplication.html#Complex.Gamma_mul_Gamma_add_third).

## Sources

- [Tau Ceti documentation: `Complex.Gamma_mul_Gamma_add_third`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gamma/Multiplication.html#Complex.Gamma_mul_Gamma_add_third)
- [Source of `Complex.Gamma_mul_Gamma_add_third` in TauCeti/Analysis/SpecialFunctions/Gamma/Multiplication.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Gamma/Multiplication.lean#L403)
- [Tau Ceti roadmap status: Airy and Scorer functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsAiry/STATUS.md)
