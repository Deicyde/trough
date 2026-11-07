---
declaration: def
origin: cited
lean: TauCeti.AuxTerminalHom
statement: formalized
---

# TauCeti.AuxTerminalHom

The arrow family of `Q` with auxiliary terminals for the vertex sets `A` and `B`, on the
vertex type `V ⊕ Bool`. The arrows between original vertices `Sum.inl v` and `Sum.inl w` are those
of `Q v w`; the fresh source `σ = Sum.inr false` has one arrow to each `Sum.inl a` with `a ∈ A`; the
fresh sink `τ = Sum.inr true` has one arrow from each `Sum.inl b` with `b ∈ B`; and there are no
other arrows.

```lean
TauCeti.AuxTerminalHom.{u, v} {V : Type u} (Q : V → V → Type v) (A B : Finset V) :
  V ⊕ Bool → V ⊕ Bool → Type v
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AuxTerminalHom`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/AuxiliaryTerminals.html#TauCeti.AuxTerminalHom).

## Sources

- [Tau Ceti documentation: `TauCeti.AuxTerminalHom`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/AuxiliaryTerminals.html#TauCeti.AuxTerminalHom)
- [Source of `TauCeti.AuxTerminalHom` in TauCeti/Combinatorics/Network/AuxiliaryTerminals.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Network/AuxiliaryTerminals.lean#L85)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
