---
declaration: theorem
origin: cited
lean: TauCeti.IsProP.isTopologicallyFinitelyGenerated_iff_isOpen_proPFrattini
statement: formalized
proof: formalized
---

# The open Frattini criterion

A profinite pro-`p` group is topologically finitely
generated exactly when its Frattini subgroup is open.

```lean
TauCeti.IsProP.isTopologicallyFinitelyGenerated_iff_isOpen_proPFrattini.{u_1} {G : Type u_1}
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] {p : ℕ}
  [Fact (Nat.Prime p)] [TotallyDisconnectedSpace G] (hG : TauCeti.IsProP p G) :
  TauCeti.IsTopologicallyFinitelyGenerated G ↔ IsOpen ↑(TauCeti.proPFrattini p G)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Burnside's basis theorem, cardinal form](burnsides-basis-theorem-cardinal-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsProP.isTopologicallyFinitelyGenerated_iff_isOpen_proPFrattini`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/FiniteGeneration.html#TauCeti.IsProP.isTopologicallyFinitelyGenerated_iff_isOpen_proPFrattini).

## Sources

- [Tau Ceti documentation: `TauCeti.IsProP.isTopologicallyFinitelyGenerated_iff_isOpen_proPFrattini`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/FiniteGeneration.html#TauCeti.IsProP.isTopologicallyFinitelyGenerated_iff_isOpen_proPFrattini)
- [Source of `TauCeti.IsProP.isTopologicallyFinitelyGenerated_iff_isOpen_proPFrattini` in TauCeti/Topology/Algebra/Group/Profinite/ProP/FiniteGeneration.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/ProP/FiniteGeneration.lean#L105)
