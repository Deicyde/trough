---
declaration: theorem
origin: cited
lean: TauCeti.isCompact_toWeakSpace_minimizers
statement: formalized
proof: formalized
---

# TauCeti.isCompact_toWeakSpace_minimizers

For a weakly lower semicontinuous energy with bounded sublevels on a weakly closed set
in a reflexive space, the set of minimizers is weakly compact, including when the admissible
set is empty.

```lean
TauCeti.isCompact_toWeakSpace_minimizers.{u_1, u_2, u_3} {𝕜 : Type u_1} {V : Type u_2}
  [NontriviallyNormedField 𝕜] [ProperSpace 𝕜] [SeminormedAddCommGroup V] [NormedSpace 𝕜 V]
  {β : Type u_3} [LinearOrder β] {E : V → β} {S : Set V}
  (hV : Function.Surjective ⇑(NormedSpace.inclusionInDoubleDual 𝕜 V))
  (hS : IsClosed (⇑(toWeakSpace 𝕜 V) '' S))
  (hE : LowerSemicontinuousOn (fun u => E ((toWeakSpace 𝕜 V).symm u)) (⇑(toWeakSpace 𝕜 V) '' S))
  (hb : TauCeti.HasBoundedSublevelsOn E S) :
  IsCompact (⇑(toWeakSpace 𝕜 V) '' {u | u ∈ S ∧ IsMinOn E S u})
```

## Depends on

- [TauCeti.HasBoundedSublevelsOn](tauceti-hasboundedsublevelson.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isCompact_toWeakSpace_minimizers`](https://taucetiproject.org/docs/TauCeti/Analysis/Variational/DirectMethod.html#TauCeti.isCompact_toWeakSpace_minimizers).

## Sources

- [Tau Ceti documentation: `TauCeti.isCompact_toWeakSpace_minimizers`](https://taucetiproject.org/docs/TauCeti/Analysis/Variational/DirectMethod.html#TauCeti.isCompact_toWeakSpace_minimizers)
- [Source of `TauCeti.isCompact_toWeakSpace_minimizers` in TauCeti/Analysis/Variational/DirectMethod.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Variational/DirectMethod.lean#L107)
- [Tau Ceti roadmap status: Variational methods and constrained spectral theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/VariationalMethods/STATUS.md)
