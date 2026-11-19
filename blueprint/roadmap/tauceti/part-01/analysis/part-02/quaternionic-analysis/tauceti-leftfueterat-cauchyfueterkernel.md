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
- [Source of `TauCeti.leftFueterAt_cauchyFueterKernel` in TauCeti/Analysis/Quaternion/Kernel.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Quaternion/Kernel.lean#L214)
- [Tau Ceti roadmap status: Quaternionic analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuaternionicAnalysis/STATUS.md)
