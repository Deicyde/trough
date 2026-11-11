---
declaration: theorem
origin: cited
lean: DiffContOnCl.circleAverage_herglotzRieszKernel_smul_re_add
statement: formalized
proof: formalized
---

# The Herglotz formula on a disc

a function holomorphic on a disc and continuous up to its
boundary is the Herglotz–Riesz integral of its boundary real part, plus the imaginary constant
`(f c).im * I`. Unlike the Poisson formula, which recovers `f` from all of its boundary values,
this recovers `f` from the boundary values of its real part alone.

```lean
DiffContOnCl.circleAverage_herglotzRieszKernel_smul_re_add {f : ℂ → ℂ} {c w : ℂ} {R : ℝ}
  (hf : DiffContOnCl ℂ f (Metric.ball c R)) (hw : w ∈ Metric.ball c R) :
  Real.circleAverage (fun ζ => herglotzRieszKernel c w ζ • ↑(f ζ).re) c R + ↑(f c).im * Complex.I =
    f w
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`DiffContOnCl.circleAverage_herglotzRieszKernel_smul_re_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Herglotz.html#DiffContOnCl.circleAverage_herglotzRieszKernel_smul_re_add).

## Sources

- [Tau Ceti documentation: `DiffContOnCl.circleAverage_herglotzRieszKernel_smul_re_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Herglotz.html#DiffContOnCl.circleAverage_herglotzRieszKernel_smul_re_add)
- [Source of `DiffContOnCl.circleAverage_herglotzRieszKernel_smul_re_add` in TauCeti/Analysis/Complex/Herglotz.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Herglotz.lean#L119)
