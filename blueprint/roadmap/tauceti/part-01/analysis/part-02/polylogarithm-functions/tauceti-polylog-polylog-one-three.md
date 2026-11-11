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
- [Source of `TauCeti.Polylog.polylog_one_three` in TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.lean#L156)
- [Tau Ceti roadmap status: Polylogarithm functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PolylogarithmFunctions/STATUS.md)
