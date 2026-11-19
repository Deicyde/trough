---
declaration: theorem
origin: cited
lean: TauCeti.exists_isMinOn_of_weak_closed
statement: formalized
proof: formalized
---

# The direct method

A weakly lower semicontinuous energy with bounded sublevels on
a nonempty weakly closed set in a reflexive space attains its minimum.

```lean
TauCeti.exists_isMinOn_of_weak_closed.{u_1, u_2, u_3} {𝕜 : Type u_1} {V : Type u_2}
  [NontriviallyNormedField 𝕜] [ProperSpace 𝕜] [SeminormedAddCommGroup V] [NormedSpace 𝕜 V]
  {β : Type u_3} [LinearOrder β] {E : V → β} {S : Set V}
  (hV : Function.Surjective ⇑(NormedSpace.inclusionInDoubleDual 𝕜 V)) (hne : S.Nonempty)
  (hS : IsClosed (⇑(toWeakSpace 𝕜 V) '' S))
  (hE : LowerSemicontinuousOn (fun u => E ((toWeakSpace 𝕜 V).symm u)) (⇑(toWeakSpace 𝕜 V) '' S))
  (hb : TauCeti.HasBoundedSublevelsOn E S) : ∃ u ∈ S, IsMinOn E S u
```

## Depends on

- [TauCeti.HasBoundedSublevelsOn](tauceti-hasboundedsublevelson.md)

## Proof depends on

- [TauCeti.exists_isMinOn_of_weak_closed_of_isBounded_sublevel](tauceti-exists-isminon-of-weak-closed-of-isbound.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isMinOn_of_weak_closed`](https://taucetiproject.org/docs/TauCeti/Analysis/Variational/DirectMethod.html#TauCeti.exists_isMinOn_of_weak_closed).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isMinOn_of_weak_closed`](https://taucetiproject.org/docs/TauCeti/Analysis/Variational/DirectMethod.html#TauCeti.exists_isMinOn_of_weak_closed)
- [Source of `TauCeti.exists_isMinOn_of_weak_closed` in TauCeti/Analysis/Variational/DirectMethod.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Variational/DirectMethod.lean#L81)
- [Tau Ceti roadmap status: Variational methods and constrained spectral theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/VariationalMethods/STATUS.md)
