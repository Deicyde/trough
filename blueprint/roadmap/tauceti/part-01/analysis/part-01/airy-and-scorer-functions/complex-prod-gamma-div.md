---
declaration: theorem
origin: cited
lean: Complex.prod_Gamma_div
statement: formalized
proof: formalized
---

# Complex.prod_Gamma_div

`∏_{k=1}^{m-1} Γ(k/m) = (2π)^{(m-1)/2} m^{-1/2}` (DLMF 5.5.7), for complex `Γ`.

```lean
Complex.prod_Gamma_div {m : ℕ} (hm : 0 < m) :
  ∏ k ∈ Finset.Ico 1 m, Complex.Gamma (↑k / ↑m) = (2 * ↑Real.pi) ^ ((↑m - 1) / 2) * ↑m ^ (-(1 / 2))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gauss's multiplication formula (DLMF 5.5.6) for every `s : ℂ`](gausss-multiplication-formula-dlmf-5-5-6-for-eve.md)

## Lean

Formalized in Tau Ceti as [`Complex.prod_Gamma_div`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gamma/Multiplication.html#Complex.prod_Gamma_div).

## Sources

- [Tau Ceti documentation: `Complex.prod_Gamma_div`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gamma/Multiplication.html#Complex.prod_Gamma_div)
- [Source of `Complex.prod_Gamma_div` in TauCeti/Analysis/SpecialFunctions/Gamma/Multiplication.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Gamma/Multiplication.lean#L367)
- [Tau Ceti roadmap status: Airy and Scorer functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsAiry/STATUS.md)
