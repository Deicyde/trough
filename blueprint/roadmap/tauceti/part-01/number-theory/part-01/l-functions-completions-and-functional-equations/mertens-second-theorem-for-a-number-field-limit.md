---
declaration: theorem
origin: cited
lean: TauCeti.LFunctions.tendsto_primeSummatory_inv_absNorm_sub_log_log, TauCeti.LFunctions.isBigO_primeSummatory_inv_absNorm_sub_log_log_sub_mertensConstant, TauCeti.LFunctions.abs_sum_primesLE_one_div_sub_log_log_sub_mertensConstant_le
statement: formalized
proof: formalized
---

# Mertens' second theorem for a number field, limit form

As `x → ∞`,
`∑_{N𝔭 ≤ x} 1 / N𝔭 - log log x` tends to Mertens' constant `B_K = mertensConstant K`.

```lean
TauCeti.LFunctions.tendsto_primeSummatory_inv_absNorm_sub_log_log.{u_1} (K : Type u_1) [Field K]
  [NumberField K] :
  Filter.Tendsto
    (fun x =>
      TauCeti.primeSummatory K (fun v => (↑(Ideal.absNorm v.asIdeal))⁻¹) x - Real.log (Real.log x))
    Filter.atTop (nhds (TauCeti.LFunctions.mertensConstant K))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Mertens' first theorem for a number field](mertens-first-theorem-for-a-number-field.md)
- [Mertens' second theorem](../../part-02/chebyshev/mertens-second-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LFunctions.tendsto_primeSummatory_inv_absNorm_sub_log_log`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Mertens.html#TauCeti.LFunctions.tendsto_primeSummatory_inv_absNorm_sub_log_log).

## Other forms

**Mertens' second theorem for a number field.** Formalized in Tau Ceti as [`TauCeti.LFunctions.isBigO_primeSummatory_inv_absNorm_sub_log_log_sub_mertensConstant`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Mertens.html#TauCeti.LFunctions.isBigO_primeSummatory_inv_absNorm_sub_log_log_sub_mertensConstant).

```lean
TauCeti.LFunctions.isBigO_primeSummatory_inv_absNorm_sub_log_log_sub_mertensConstant.{u_1}
  (K : Type u_1) [Field K] [NumberField K] :
  (fun x =>
      TauCeti.primeSummatory K (fun v => (↑(Ideal.absNorm v.asIdeal))⁻¹) x - Real.log (Real.log x) -
        TauCeti.LFunctions.mertensConstant K) =O[Filter.atTop]
    fun x => (Real.log x)⁻¹
```

**Mertens' second theorem for the rational primes, with its constant.** Formalized in Tau Ceti as [`TauCeti.LFunctions.abs_sum_primesLE_one_div_sub_log_log_sub_mertensConstant_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Mertens.html#TauCeti.LFunctions.abs_sum_primesLE_one_div_sub_log_log_sub_mertensConstant_le).

```lean
TauCeti.LFunctions.abs_sum_primesLE_one_div_sub_log_log_sub_mertensConstant_le {x : ℝ}
  (hx : 2 ≤ x) :
  |∑ p ∈ ⌊x⌋₊.primesLE, 1 / ↑p - Real.log (Real.log x) - TauCeti.LFunctions.mertensConstant ℚ| ≤
    2 * (Real.log 4 + 4) / Real.log x
```

## Sources

- [Tau Ceti documentation: `TauCeti.LFunctions.tendsto_primeSummatory_inv_absNorm_sub_log_log`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Mertens.html#TauCeti.LFunctions.tendsto_primeSummatory_inv_absNorm_sub_log_log)
- [Source of `TauCeti.LFunctions.tendsto_primeSummatory_inv_absNorm_sub_log_log` in TauCeti/NumberTheory/LFunctions/Mertens.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LFunctions/Mertens.lean#L543)
- [Tau Ceti roadmap status: L-functions — completions and functional equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LFunctions/STATUS.md)
