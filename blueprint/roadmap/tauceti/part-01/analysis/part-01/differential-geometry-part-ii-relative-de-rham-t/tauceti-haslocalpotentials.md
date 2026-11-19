---
declaration: def
origin: cited
lean: TauCeti.HasLocalPotentials
statement: formalized
---

# TauCeti.HasLocalPotentials

A covector field has local potentials on `s` if each point has a ball contained in `s`
on which the field is the derivative of an ambient `C¹` function.

```lean
TauCeti.HasLocalPotentials.{u_1, u_2} {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] (s : Set E) (φ : E → E →L[ℝ] F) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HasLocalPotentials`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/LocalPotentials.html#TauCeti.HasLocalPotentials).

## Sources

- [Tau Ceti documentation: `TauCeti.HasLocalPotentials`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/LocalPotentials.html#TauCeti.HasLocalPotentials)
- [Source of `TauCeti.HasLocalPotentials` in TauCeti/Analysis/Calculus/LocalPotentials.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/LocalPotentials.lean#L35)
- [Tau Ceti roadmap status: Differential geometry, Part II — relative de Rham theory, fundamental classes and relative transversality](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DeRhamCohomologyAndDuality/STATUS.md)
