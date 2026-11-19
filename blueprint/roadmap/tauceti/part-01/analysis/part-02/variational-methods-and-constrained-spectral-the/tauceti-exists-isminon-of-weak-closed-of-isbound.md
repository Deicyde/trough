---
declaration: theorem
origin: cited
lean: TauCeti.exists_isMinOn_of_weak_closed_of_isBounded_sublevel
statement: formalized
proof: formalized
---

# TauCeti.exists_isMinOn_of_weak_closed_of_isBounded_sublevel

A single nonempty bounded sublevel suffices for the direct method on a weakly
closed admissible set.

```lean
TauCeti.exists_isMinOn_of_weak_closed_of_isBounded_sublevel.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {V : Type u_2} [NontriviallyNormedField 𝕜] [ProperSpace 𝕜] [SeminormedAddCommGroup V]
  [NormedSpace 𝕜 V] {β : Type u_3} [LinearOrder β] {E : V → β} {S : Set V}
  (hV : Function.Surjective ⇑(NormedSpace.inclusionInDoubleDual 𝕜 V))
  (hS : IsClosed (⇑(toWeakSpace 𝕜 V) '' S))
  (hE : LowerSemicontinuousOn (fun u => E ((toWeakSpace 𝕜 V).symm u)) (⇑(toWeakSpace 𝕜 V) '' S))
  {b : β} (hne : {u | u ∈ S ∧ E u ≤ b}.Nonempty) (hb : Bornology.IsBounded {u | u ∈ S ∧ E u ≤ b}) :
  ∃ u ∈ S, IsMinOn E S u
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.isMinOn_sublevel_iff](tauceti-isminon-sublevel-iff.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isMinOn_of_weak_closed_of_isBounded_sublevel`](https://taucetiproject.org/docs/TauCeti/Analysis/Variational/DirectMethod.html#TauCeti.exists_isMinOn_of_weak_closed_of_isBounded_sublevel).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isMinOn_of_weak_closed_of_isBounded_sublevel`](https://taucetiproject.org/docs/TauCeti/Analysis/Variational/DirectMethod.html#TauCeti.exists_isMinOn_of_weak_closed_of_isBounded_sublevel)
- [Source of `TauCeti.exists_isMinOn_of_weak_closed_of_isBounded_sublevel` in TauCeti/Analysis/Variational/DirectMethod.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Variational/DirectMethod.lean#L62)
- [Tau Ceti roadmap status: Variational methods and constrained spectral theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/VariationalMethods/STATUS.md)
