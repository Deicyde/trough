---
declaration: theorem
origin: cited
lean: TauCeti.hasLocalPotentials_iUnion_iff
statement: formalized
proof: formalized
---

# TauCeti.hasLocalPotentials_iUnion_iff

Local potentials can be checked on any open cover.

```lean
TauCeti.hasLocalPotentials_iUnion_iff.{u_1, u_2, u_4} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  {φ : E → E →L[ℝ] F} {ι : Sort u_4} {u : ι → Set E} (hu : ∀ (i : ι), IsOpen (u i)) :
  TauCeti.HasLocalPotentials (⋃ i, u i) φ ↔ ∀ (i : ι), TauCeti.HasLocalPotentials (u i) φ
```

## Depends on

- [TauCeti.HasLocalPotentials](tauceti-haslocalpotentials.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hasLocalPotentials_iUnion_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/LocalPotentials.html#TauCeti.hasLocalPotentials_iUnion_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.hasLocalPotentials_iUnion_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/LocalPotentials.html#TauCeti.hasLocalPotentials_iUnion_iff)
- [Source of `TauCeti.hasLocalPotentials_iUnion_iff` in TauCeti/Analysis/Calculus/LocalPotentials.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/LocalPotentials.lean#L93)
- [Tau Ceti roadmap status: Differential geometry, Part II — relative de Rham theory, fundamental classes and relative transversality](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DeRhamCohomologyAndDuality/STATUS.md)
