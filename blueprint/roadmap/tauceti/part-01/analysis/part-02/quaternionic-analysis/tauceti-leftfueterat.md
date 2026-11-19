---
declaration: def
origin: cited
lean: TauCeti.LeftFueterAt
statement: formalized
---

# TauCeti.LeftFueterAt

`f` is *left Fueter regular* at `q`: it has a real Fréchet derivative `D` at `q` with
`D 1 + i * D i + j * D j + k * D k = 0`.

```lean
TauCeti.LeftFueterAt (f : Quaternion ℝ → Quaternion ℝ) (q : Quaternion ℝ) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LeftFueterAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/Fueter.html#TauCeti.LeftFueterAt).

## Sources

- [Tau Ceti documentation: `TauCeti.LeftFueterAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/Fueter.html#TauCeti.LeftFueterAt)
- [Source of `TauCeti.LeftFueterAt` in TauCeti/Analysis/Quaternion/Fueter.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Quaternion/Fueter.lean#L203)
- [Tau Ceti roadmap status: Quaternionic analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuaternionicAnalysis/STATUS.md)
