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

Formalized in Tau Ceti as [`Real.isEquivalent_Gamma_natCast_add_one_add`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gamma.html#Real.isEquivalent_Gamma_natCast_add_one_add).

## Sources

- [Tau Ceti documentation: `Real.isEquivalent_Gamma_natCast_add_one_add`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gamma.html#Real.isEquivalent_Gamma_natCast_add_one_add)
- [Source of `Real.isEquivalent_Gamma_natCast_add_one_add` in TauCeti/Analysis/SpecialFunctions/Gamma.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/Gamma.lean#L175)
