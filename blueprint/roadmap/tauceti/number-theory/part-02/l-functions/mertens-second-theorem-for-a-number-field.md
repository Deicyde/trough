---
declaration: theorem
origin: cited
lean: TauCeti.LFunctions.isBigO_primeSummatory_inv_absNorm_sub_log_log_sub_mertensConstant, TauCeti.LFunctions.tendsto_primeSummatory_inv_absNorm_sub_log_log
statement: formalized
proof: formalized
---

# Mertens' second theorem for a number field

The sum of `1 / N𝔭` over the nonzero prime
ideals `𝔭` of `𝓞 K` of norm at most `x` is `log log x + B_K + O(1 / log x)`, where
`B_K = mertensConstant K`.

```lean
TauCeti.LFunctions.isBigO_primeSummatory_inv_absNorm_sub_log_log_sub_mertensConstant.{u_1}
  (K : Type u_1) [Field K] [NumberField K] :
  (fun x =>
      TauCeti.primeSummatory K (fun v => (↑(Ideal.absNorm v.asIdeal))⁻¹) x - Real.log (Real.log x) -
        TauCeti.LFunctions.mertensConstant K) =O[Filter.atTop]
    fun x => (Real.log x)⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Mertens' first theorem for a number field](mertens-first-theorem-for-a-number-field.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LFunctions.isBigO_primeSummatory_inv_absNorm_sub_log_log_sub_mertensConstant`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Mertens.html#TauCeti.LFunctions.isBigO_primeSummatory_inv_absNorm_sub_log_log_sub_mertensConstant).

## Other forms

**Mertens' second theorem for a number field, limit form.** Formalized in Tau Ceti as [`TauCeti.LFunctions.tendsto_primeSummatory_inv_absNorm_sub_log_log`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Mertens.html#TauCeti.LFunctions.tendsto_primeSummatory_inv_absNorm_sub_log_log).

```lean
TauCeti.LFunctions.tendsto_primeSummatory_inv_absNorm_sub_log_log.{u_1} (K : Type u_1) [Field K]
  [NumberField K] :
  Filter.Tendsto
    (fun x =>
      TauCeti.primeSummatory K (fun v => (↑(Ideal.absNorm v.asIdeal))⁻¹) x - Real.log (Real.log x))
    Filter.atTop (nhds (TauCeti.LFunctions.mertensConstant K))
```

## Sources

- [Tau Ceti documentation: `TauCeti.LFunctions.isBigO_primeSummatory_inv_absNorm_sub_log_log_sub_mertensConstant`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Mertens.html#TauCeti.LFunctions.isBigO_primeSummatory_inv_absNorm_sub_log_log_sub_mertensConstant)
- [Source of `TauCeti.LFunctions.isBigO_primeSummatory_inv_absNorm_sub_log_log_sub_mertensConstant` in TauCeti/NumberTheory/LFunctions/Mertens.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LFunctions/Mertens.lean#L556)
