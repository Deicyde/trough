---
declaration: theorem
origin: cited
lean: TauCeti.UqSl2.isSemisimpleModule_of_finiteDimensional
statement: formalized
proof: formalized
---

# Complete reducibility

At a generic parameter, every finite-dimensional
`UqSl2 q`-module is semisimple.

```lean
TauCeti.UqSl2.isSemisimpleModule_of_finiteDimensional.{u_1} {q : ℂ} {V : Type u_1} [AddCommGroup V]
  [_root_.Module ℂ V] [_root_.Module (TauCeti.UqSl2 q) V] [IsScalarTower ℂ (TauCeti.UqSl2 q) V]
  [FiniteDimensional ℂ V] (hq : TauCeti.IsGenericQuantumParameter q) :
  IsSemisimpleModule (TauCeti.UqSl2 q) V
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.UqSl2.isSemisimpleModule_of_finiteDimensional`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/CompleteReducibility.html#TauCeti.UqSl2.isSemisimpleModule_of_finiteDimensional).

## Sources

- [Tau Ceti documentation: `TauCeti.UqSl2.isSemisimpleModule_of_finiteDimensional`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/CompleteReducibility.html#TauCeti.UqSl2.isSemisimpleModule_of_finiteDimensional)
- [Source of `TauCeti.UqSl2.isSemisimpleModule_of_finiteDimensional` in TauCeti/QuantumGroups/UqSl2/CompleteReducibility.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/QuantumGroups/UqSl2/CompleteReducibility.lean#L144)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuantumGroups/STATUS.md)
