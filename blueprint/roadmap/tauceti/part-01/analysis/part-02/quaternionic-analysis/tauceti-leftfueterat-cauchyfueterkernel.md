---
declaration: theorem
origin: cited
lean: TauCeti.leftFueterAt_cauchyFueterKernel
statement: formalized
proof: formalized
---

# TauCeti.leftFueterAt_cauchyFueterKernel

The kernel satisfies the left Fueter equation away from the pole.

```lean
TauCeti.leftFueterAt_cauchyFueterKernel {q q₀ : Quaternion ℝ} (hq : q ≠ q₀) :
  TauCeti.LeftFueterAt (fun x => TauCeti.cauchyFueterKernel x q₀) q
```

## Depends on

- [TauCeti.LeftFueterAt](tauceti-leftfueterat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.leftFueterAt_cauchyFueterKernel`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/Kernel.html#TauCeti.leftFueterAt_cauchyFueterKernel).

## Sources

- [Tau Ceti documentation: `TauCeti.leftFueterAt_cauchyFueterKernel`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/Kernel.html#TauCeti.leftFueterAt_cauchyFueterKernel)
- [Source of `TauCeti.leftFueterAt_cauchyFueterKernel` in TauCeti/Analysis/Quaternion/Kernel.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Quaternion/Kernel.lean#L162)
- [Tau Ceti roadmap status: Quaternionic analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuaternionicAnalysis/STATUS.md)
