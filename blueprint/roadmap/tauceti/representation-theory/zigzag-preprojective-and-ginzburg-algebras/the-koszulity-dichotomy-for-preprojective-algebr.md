---
declaration: theorem
origin: cited
lean: TauCeti.forall_preprojectiveKoszulLeft_injective_iff
statement: formalized
proof: formalized
---

# The Koszulity dichotomy for preprojective algebras of oriented graphs

for a connected
finite simple graph `G` and any orientation `o` of `G`, the left Koszul differential of
`Π_k(OrientedQuiver G o)` is injective at every vertex if and only if `G` is not isomorphic to the
diagram of any valid Dynkin type.

```lean
TauCeti.forall_preprojectiveKoszulLeft_injective_iff.{u, w} (k : Type w) [Field k] {V : Type u}
  {G : SimpleGraph V} [Finite V] (hG : G.Connected) (o : TauCeti.DoubledQuiver.Orientation G) :
  (∀ (v : TauCeti.DoubledQuiver.OrientedQuiver G o),
      Function.Injective ⇑(TauCeti.preprojectiveKoszulLeft k v)) ↔
    ¬∃ t, t.Valid ∧ Nonempty (G ≃g TauCeti.diagramGraph t.cartanMatrix)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul defect formula](../quiver/the-koszul-defect-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.forall_preprojectiveKoszulLeft_injective_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Preprojective/Koszul/NonDynkin.html#TauCeti.forall_preprojectiveKoszulLeft_injective_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.forall_preprojectiveKoszulLeft_injective_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Preprojective/Koszul/NonDynkin.html#TauCeti.forall_preprojectiveKoszulLeft_injective_iff)
- [Source of `TauCeti.forall_preprojectiveKoszulLeft_injective_iff` in TauCeti/RepresentationTheory/Quiver/Preprojective/Koszul/NonDynkin.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Quiver/Preprojective/Koszul/NonDynkin.lean#L183)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
