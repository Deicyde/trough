---
declaration: theorem
origin: cited
lean: TauCeti.hasLocalPotentials_of_extDeriv_eq_zero
statement: formalized
proof: formalized
---

# TauCeti.hasLocalPotentials_of_extDeriv_eq_zero

A closed `C¹` covector field on an open set has local potentials. Closedness is expressed
by the exterior derivative of the corresponding alternating one-form.

```lean
TauCeti.hasLocalPotentials_of_extDeriv_eq_zero.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  [CompleteSpace F] {s : Set E} {φ : E → E →L[ℝ] F} (hs : IsOpen s) (hφ : ContDiffOn ℝ 1 φ s)
  (hd : ∀ x ∈ s, extDeriv (fun y => (ContinuousAlternatingMap.ofSubsingletonLIE 0) (φ y)) x = 0) :
  TauCeti.HasLocalPotentials s φ
```

## Depends on

- [TauCeti.HasLocalPotentials](tauceti-haslocalpotentials.md)

## Proof depends on

- [The Poincaré lemma](../../part-03/calculus/part-02/the-poincare-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hasLocalPotentials_of_extDeriv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/LocalPotentials.html#TauCeti.hasLocalPotentials_of_extDeriv_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.hasLocalPotentials_of_extDeriv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/LocalPotentials.html#TauCeti.hasLocalPotentials_of_extDeriv_eq_zero)
- [Source of `TauCeti.hasLocalPotentials_of_extDeriv_eq_zero` in TauCeti/Analysis/Calculus/DifferentialForm/LocalPotentials.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/DifferentialForm/LocalPotentials.lean#L34)
- [Tau Ceti roadmap status: Differential geometry, Part II — relative de Rham theory, fundamental classes and relative transversality](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DeRhamCohomologyAndDuality/STATUS.md)
