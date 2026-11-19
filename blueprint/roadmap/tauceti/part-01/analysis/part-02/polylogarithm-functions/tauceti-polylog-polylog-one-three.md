---
declaration: theorem
origin: cited
lean: TauCeti.Polylog.polylog_one_three
statement: formalized
proof: formalized
---

# TauCeti.Polylog.polylog_one_three

On the cut, weight one uses the lower boundary value: its imaginary part
at 3 is `-π`, not `π`.

```lean
TauCeti.Polylog.polylog_one_three :
  TauCeti.Polylog.polylog 1 3 = -↑(Real.log 2) - ↑Real.pi * Complex.I
```

## Depends on

- [TauCeti.Polylog.polylog](tauceti-polylog-polylog.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Polylog.polylog_one_three`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.html#TauCeti.Polylog.polylog_one_three).

## Sources

- [Tau Ceti documentation: `TauCeti.Polylog.polylog_one_three`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.html#TauCeti.Polylog.polylog_one_three)
- [Source of `TauCeti.Polylog.polylog_one_three` in TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.lean#L156)
- [Tau Ceti roadmap status: Polylogarithm functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PolylogarithmFunctions/STATUS.md)
