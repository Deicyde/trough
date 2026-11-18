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

- [A negative-power Abel bound](../../part-02/arithmetic-dirichlet-series/a-negative-power-abel-bound.md)
- [Chebyshev's identity for a number field](chebyshevs-identity-for-a-number-field.md)
- [The prime ideal theorem](../arithmetic-dirichlet-series-and-tauberian-method/the-prime-ideal-theorem.md)

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
- [Source of `TauCeti.LFunctions.isBigO_primeSummatory_log_absNorm_div_sub_log` in TauCeti/NumberTheory/LFunctions/Mertens.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LFunctions/Mertens.lean#L422)
- [Tau Ceti roadmap status: L-functions — completions and functional equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LFunctions/STATUS.md)
