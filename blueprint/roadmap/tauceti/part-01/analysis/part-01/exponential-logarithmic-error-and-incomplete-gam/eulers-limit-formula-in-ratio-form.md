---
declaration: theorem
origin: cited
lean: Real.isEquivalent_Gamma_natCast_add_one_add
statement: formalized
proof: formalized
---

# Euler's limit formula in ratio form

For every real `s`, `Γ(n + 1 + s)` is asymptotic to
`n ^ s * n!` as the natural number `n` tends to infinity.

```lean
Real.isEquivalent_Gamma_natCast_add_one_add (s : ℝ) :
  Asymptotics.IsEquivalent Filter.atTop (fun n => Real.Gamma (↑n + 1 + s)) fun n =>
    ↑n ^ s * ↑n.factorial
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Real.isEquivalent_Gamma_natCast_add_one_add`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gamma/Basic.html#Real.isEquivalent_Gamma_natCast_add_one_add).

## Sources

- [Tau Ceti documentation: `Real.isEquivalent_Gamma_natCast_add_one_add`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gamma/Basic.html#Real.isEquivalent_Gamma_natCast_add_one_add)
- [Source of `Real.isEquivalent_Gamma_natCast_add_one_add` in TauCeti/Analysis/SpecialFunctions/Gamma/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/Gamma/Basic.lean#L181)
