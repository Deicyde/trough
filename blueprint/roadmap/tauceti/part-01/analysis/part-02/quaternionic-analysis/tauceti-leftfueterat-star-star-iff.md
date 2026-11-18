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
- [Source of `TauCeti.leftFueterAt_star_star_iff` in TauCeti/Analysis/Quaternion/Reflection.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Quaternion/Reflection.lean#L79)
- [Tau Ceti roadmap status: Quaternionic analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuaternionicAnalysis/STATUS.md)
