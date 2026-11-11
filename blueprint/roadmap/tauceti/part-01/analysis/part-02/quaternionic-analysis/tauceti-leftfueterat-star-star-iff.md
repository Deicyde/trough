---
declaration: theorem
origin: cited
lean: TauCeti.leftFueterAt_star_star_iff
statement: formalized
proof: formalized
---

# TauCeti.leftFueterAt_star_star_iff

Reflection exchanges pointwise left and right Fueter regularity, in both directions.

```lean
TauCeti.leftFueterAt_star_star_iff {f : Quaternion ℝ → Quaternion ℝ} {q : Quaternion ℝ} :
  TauCeti.LeftFueterAt (fun x => star (f (star x))) (star q) ↔ TauCeti.RightFueterAt f q
```

## Depends on

- [TauCeti.LeftFueterAt](tauceti-leftfueterat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.leftFueterAt_star_star_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/Reflection.html#TauCeti.leftFueterAt_star_star_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.leftFueterAt_star_star_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/Reflection.html#TauCeti.leftFueterAt_star_star_iff)
- [Source of `TauCeti.leftFueterAt_star_star_iff` in TauCeti/Analysis/Quaternion/Reflection.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Quaternion/Reflection.lean#L79)
- [Tau Ceti roadmap status: Quaternionic analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuaternionicAnalysis/STATUS.md)
