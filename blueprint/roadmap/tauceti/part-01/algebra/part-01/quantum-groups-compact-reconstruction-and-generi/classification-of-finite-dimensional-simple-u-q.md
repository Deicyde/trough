---
declaration: theorem
origin: cited
lean: TauCeti.UqSl2.existsUnique_linearEquiv_ladderModule
statement: formalized
proof: formalized
---

# Classification of finite-dimensional simple `U_q(sl₂)`-modules

At a generic parameter,
every finite-dimensional simple `UqSl2 q`-module is isomorphic to `L_m^ε` for exactly one
natural number `m` and sign `ε`.

```lean
TauCeti.UqSl2.existsUnique_linearEquiv_ladderModule.{u_1} {q : ℂ} {V : Type u_1} [AddCommGroup V]
  [_root_.Module ℂ V] [_root_.Module (TauCeti.UqSl2 q) V] [IsScalarTower ℂ (TauCeti.UqSl2 q) V]
  [Fact (q ≠ 0)] [FiniteDimensional ℂ V] [IsSimpleModule (TauCeti.UqSl2 q) V]
  (hq : TauCeti.IsGenericQuantumParameter q) :
  ∃! p, Nonempty (TauCeti.UqSl2.LadderModule q p.1 p.2 ≃ₗ[TauCeti.UqSl2 q] V)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.UqSl2.existsUnique_linearEquiv_ladderModule`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/SimpleClassification.html#TauCeti.UqSl2.existsUnique_linearEquiv_ladderModule).

## Sources

- [Tau Ceti documentation: `TauCeti.UqSl2.existsUnique_linearEquiv_ladderModule`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/SimpleClassification.html#TauCeti.UqSl2.existsUnique_linearEquiv_ladderModule)
- [Source of `TauCeti.UqSl2.existsUnique_linearEquiv_ladderModule` in TauCeti/QuantumGroups/UqSl2/SimpleClassification.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/QuantumGroups/UqSl2/SimpleClassification.lean#L59)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuantumGroups/STATUS.md)
