---
declaration: theorem
origin: cited
lean: TauCeti.Contour.residue_div_sub_pow_of_analyticAt
statement: formalized
proof: formalized
---

# The residue of the Cauchy kernel

If `g` is analytic at `z₀`, then the function
`g z / (z - z₀) ^ (k + 1)` has residue the Taylor coefficient `iteratedDeriv k g z₀ / k !` at `z₀`:
the whole Laurent principal part comes from the first `k + 1` Taylor terms of `g`, and only the one
of index `k` sits at order `−1`. This is the residue behind Cauchy's integral formula for the
`k`-th derivative; the constant case is `TauCeti.Contour.residue_const_div_sub_pow`.

```lean
TauCeti.Contour.residue_div_sub_pow_of_analyticAt {g : ℂ → ℂ} {z₀ : ℂ} (hg : AnalyticAt ℂ g z₀)
  (k : ℕ) :
  TauCeti.Contour.residue (fun z => g z / (z - z₀) ^ (k + 1)) z₀ =
    iteratedDeriv k g z₀ / ↑k.factorial
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.residue_div_sub_pow_of_analyticAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Residue/Basic.html#TauCeti.Contour.residue_div_sub_pow_of_analyticAt).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.residue_div_sub_pow_of_analyticAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Residue/Basic.html#TauCeti.Contour.residue_div_sub_pow_of_analyticAt)
- [Source of `TauCeti.Contour.residue_div_sub_pow_of_analyticAt` in TauCeti/Analysis/Contour/Residue/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Contour/Residue/Basic.lean#L370)
- [Tau Ceti roadmap status: Contour integration and the Hungerbühler–Wasem generalized residue theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ContourIntegration/STATUS.md)
