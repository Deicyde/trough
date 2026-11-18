---
declaration: theorem
origin: cited
lean: TauCeti.HasLocalPotentials.pullback
statement: formalized
proof: formalized
---

# TauCeti.HasLocalPotentials.pullback

Pullback of a locally potential covector field along a `C¹` map of open domains has
local potentials, obtained by composing each potential with the map.

```lean
TauCeti.HasLocalPotentials.pullback.{u_1, u_2, u_3} {E : Type u_1} {F : Type u_2} {G : Type u_3}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  [NormedAddCommGroup G] [NormedSpace ℝ G] {s : Set E} {φ : E → E →L[ℝ] F} {u : Set G} {f : G → E}
  (hφ : TauCeti.HasLocalPotentials s φ) (hu : IsOpen u) (hf : ContDiffOn ℝ 1 f u)
  (hfs : Set.MapsTo f u s) : TauCeti.HasLocalPotentials u fun x => φ (f x) ∘SL fderiv ℝ f x
```

## Depends on

- [TauCeti.HasLocalPotentials](tauceti-haslocalpotentials.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HasLocalPotentials.pullback`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/LocalPotentials.html#TauCeti.HasLocalPotentials.pullback).

## Sources

- [Tau Ceti documentation: `TauCeti.HasLocalPotentials.pullback`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/LocalPotentials.html#TauCeti.HasLocalPotentials.pullback)
- [Source of `TauCeti.HasLocalPotentials.pullback` in TauCeti/Analysis/Calculus/LocalPotentials.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/LocalPotentials.lean#L147)
- [Tau Ceti roadmap status: Differential geometry, Part II — relative de Rham theory, fundamental classes and relative transversality](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DeRhamCohomologyAndDuality/STATUS.md)
