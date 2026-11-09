---
declaration: theorem
origin: cited
lean: TauCeti.LFunctions.isBigO_primeSummatory_log_absNorm_div_sub_log, TauCeti.LFunctions.isBigO_primePowerSummatory_div_sub_log
statement: formalized
proof: formalized
---

# Mertens' first theorem for a number field

The sum of `log N𝔭 / N𝔭` over the nonzero prime
ideals `𝔭` of `𝓞 K` of norm at most `x` is `log x + O(1)`.

```lean
TauCeti.LFunctions.isBigO_primeSummatory_log_absNorm_div_sub_log.{u_1} (K : Type u_1) [Field K]
  [NumberField K] :
  (fun x =>
      TauCeti.primeSummatory K
          (fun v => Real.log ↑(Ideal.absNorm v.asIdeal) / ↑(Ideal.absNorm v.asIdeal)) x -
        Real.log x) =O[Filter.atTop]
    fun x => 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A negative-power Abel bound](../arithmetic-dirichlet-series/a-negative-power-abel-bound.md)
- [Chebyshev's identity for a number field](chebyshevs-identity-for-a-number-field.md)
- [The prime ideal theorem](../../part-01/arithmetic-dirichlet-series-and-tauberian-method/the-prime-ideal-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LFunctions.isBigO_primeSummatory_log_absNorm_div_sub_log`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Mertens.html#TauCeti.LFunctions.isBigO_primeSummatory_log_absNorm_div_sub_log).

## Other forms

**Mertens' first theorem for a number field, prime-power form.** Formalized in Tau Ceti as [`TauCeti.LFunctions.isBigO_primePowerSummatory_div_sub_log`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Mertens.html#TauCeti.LFunctions.isBigO_primePowerSummatory_div_sub_log).

```lean
TauCeti.LFunctions.isBigO_primePowerSummatory_div_sub_log.{u_1} (K : Type u_1) [Field K]
  [NumberField K] :
  (fun x =>
      TauCeti.primePowerSummatory K (fun A => TauCeti.primePowerWeight A / ↑(Ideal.absNorm ↑↑A)) x -
        Real.log x) =O[Filter.atTop]
    fun x => 1
```

## Sources

- [Tau Ceti documentation: `TauCeti.LFunctions.isBigO_primeSummatory_log_absNorm_div_sub_log`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Mertens.html#TauCeti.LFunctions.isBigO_primeSummatory_log_absNorm_div_sub_log)
- [Source of `TauCeti.LFunctions.isBigO_primeSummatory_log_absNorm_div_sub_log` in TauCeti/NumberTheory/LFunctions/Mertens.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LFunctions/Mertens.lean#L380)
