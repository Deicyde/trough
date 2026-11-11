---
declaration: theorem
origin: cited
lean: TauCeti.LFunctions.tendsto_primeSummatory_inv_absNorm_sub_log_log, TauCeti.LFunctions.isBigO_primeSummatory_inv_absNorm_sub_log_log_sub_mertensConstant
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

## Sources

- [Tau Ceti documentation: `TauCeti.LFunctions.tendsto_primeSummatory_inv_absNorm_sub_log_log`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Mertens.html#TauCeti.LFunctions.tendsto_primeSummatory_inv_absNorm_sub_log_log)
- [Source of `TauCeti.LFunctions.tendsto_primeSummatory_inv_absNorm_sub_log_log` in TauCeti/NumberTheory/LFunctions/Mertens.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LFunctions/Mertens.lean#L605)
- [Tau Ceti roadmap status: L-functions — completions and functional equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LFunctions/STATUS.md)
