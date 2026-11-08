---
declaration: theorem
origin: cited
lean: TauCeti.LFunctions.idealSummatory_log_absNorm_eq
statement: formalized
proof: formalized
---

# Chebyshev's identity for a number field

Summing `log N𝔞 = ∑_{𝔟 ∣ 𝔞} Λ_K(𝔟)` over the
nonzero integral ideals of norm at most `x` and exchanging the order of summation,
`∑_{N𝔞 ≤ x} log N𝔞 = ∑_{N(𝔭 ^ k) ≤ x} log N𝔭 · #{𝔞 : N𝔞 ≤ x / N(𝔭 ^ k)}`.

```lean
TauCeti.LFunctions.idealSummatory_log_absNorm_eq.{u_1} (K : Type u_1) [Field K] [NumberField K]
  (x : ℝ) :
  TauCeti.idealSummatory K (fun I => Real.log ↑(Ideal.absNorm ↑I)) x =
    TauCeti.primePowerSummatory K
      (fun A => TauCeti.primePowerWeight A * ↑(TauCeti.idealsLE K (x / ↑(Ideal.absNorm ↑↑A))).card)
      x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The analytic Euler product](the-analytic-euler-product.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LFunctions.idealSummatory_log_absNorm_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Mertens.html#TauCeti.LFunctions.idealSummatory_log_absNorm_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.LFunctions.idealSummatory_log_absNorm_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Mertens.html#TauCeti.LFunctions.idealSummatory_log_absNorm_eq)
- [Source of `TauCeti.LFunctions.idealSummatory_log_absNorm_eq` in TauCeti/NumberTheory/LFunctions/Mertens.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LFunctions/Mertens.lean#L86)
