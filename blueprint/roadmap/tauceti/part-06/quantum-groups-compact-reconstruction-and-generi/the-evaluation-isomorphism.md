---
declaration: def
origin: cited
lean: TauCeti.UqSl2.ladderModuleTensorHomEquiv
statement: formalized
---

# The evaluation isomorphism

At a generic parameter, a locally finite `UqSl2 q`-module `V`
is the direct sum over `(m, ε)` of `L_m^ε ⊗ Hom_U(L_m^ε, V)`, by `v ⊗ φ ↦ φ v`. Here `UqSl2 q`
acts on the left tensor factors, and the multiplicity spaces `Hom_U(L_m^ε, V)` may be
infinite-dimensional.

```lean
TauCeti.UqSl2.ladderModuleTensorHomEquiv.{u} {q : ℂ} {V : Type u} [AddCommGroup V]
  [_root_.Module ℂ V] [_root_.Module (TauCeti.UqSl2 q) V] [IsScalarTower ℂ (TauCeti.UqSl2 q) V]
  [Fact (q ≠ 0)] (hq : TauCeti.IsGenericQuantumParameter q)
  [TauCeti.IsLocallyFiniteModule ℂ (TauCeti.UqSl2 q) V] :
  (Π₀ (p : ℕ × ℤˣ),
      TensorProduct ℂ (TauCeti.UqSl2.LadderModule q p.1 p.2)
        (TauCeti.UqSl2.LadderModule q p.1 p.2 →ₗ[TauCeti.UqSl2 q] V)) ≃ₗ[TauCeti.UqSl2 q]
    V
```

## Depends on

- [The isotypic decomposition of a semisimple module](the-isotypic-decomposition-of-a-semisimple-modul.md)
- [TauCeti.UqSl2.LadderModule](tauceti-uqsl2-laddermodule.md)

## Proof depends on

- [Complete reducibility](complete-reducibility.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UqSl2.ladderModuleTensorHomEquiv`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/LocallyFinite.html#TauCeti.UqSl2.ladderModuleTensorHomEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.UqSl2.ladderModuleTensorHomEquiv`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/LocallyFinite.html#TauCeti.UqSl2.ladderModuleTensorHomEquiv)
- [Source of `TauCeti.UqSl2.ladderModuleTensorHomEquiv` in TauCeti/QuantumGroups/UqSl2/LocallyFinite.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/QuantumGroups/UqSl2/LocallyFinite.lean#L129)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuantumGroups/STATUS.md)
