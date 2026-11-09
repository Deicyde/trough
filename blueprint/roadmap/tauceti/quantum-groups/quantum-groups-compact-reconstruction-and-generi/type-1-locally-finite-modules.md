---
declaration: theorem
origin: cited
lean: TauCeti.UqSl2.isTypeOne_and_isLocallyFiniteModule_iff_exists_linearEquiv_dfinsupp_ladderModule
statement: formalized
proof: formalized
---

# Type-1 locally finite modules

At a generic parameter, a module is of type 1 and locally
finite exactly when it is isomorphic to a direct sum of positive signed ladder modules `L_m^+`.

```lean
TauCeti.UqSl2.isTypeOne_and_isLocallyFiniteModule_iff_exists_linearEquiv_dfinsupp_ladderModule.{u}
  {q : ℂ} [Fact (q ≠ 0)] {V : Type u} [AddCommGroup V] [_root_.Module ℂ V]
  [_root_.Module (TauCeti.UqSl2 q) V] [IsScalarTower ℂ (TauCeti.UqSl2 q) V]
  (hq : TauCeti.IsGenericQuantumParameter q) :
  TauCeti.UqSl2.IsTypeOne q V ∧ TauCeti.IsLocallyFiniteModule ℂ (TauCeti.UqSl2 q) V ↔
    ∃ ι m, Nonempty (V ≃ₗ[TauCeti.UqSl2 q] Π₀ (i : ι), TauCeti.UqSl2.LadderModule q (m i) 1)
```

## Depends on

- [TauCeti.UqSl2.LadderModule](tauceti-uqsl2-laddermodule.md)

## Proof depends on

- [Complete reducibility](complete-reducibility.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UqSl2.isTypeOne_and_isLocallyFiniteModule_iff_exists_linearEquiv_dfinsupp_ladderModule`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/TypeOne.html#TauCeti.UqSl2.isTypeOne_and_isLocallyFiniteModule_iff_exists_linearEquiv_dfinsupp_ladderModule).

## Sources

- [Tau Ceti documentation: `TauCeti.UqSl2.isTypeOne_and_isLocallyFiniteModule_iff_exists_linearEquiv_dfinsupp_ladderModule`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/TypeOne.html#TauCeti.UqSl2.isTypeOne_and_isLocallyFiniteModule_iff_exists_linearEquiv_dfinsupp_ladderModule)
- [Source of `TauCeti.UqSl2.isTypeOne_and_isLocallyFiniteModule_iff_exists_linearEquiv_dfinsupp_ladderModule` in TauCeti/QuantumGroups/UqSl2/TypeOne.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/QuantumGroups/UqSl2/TypeOne.lean#L347)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuantumGroups/STATUS.md)
