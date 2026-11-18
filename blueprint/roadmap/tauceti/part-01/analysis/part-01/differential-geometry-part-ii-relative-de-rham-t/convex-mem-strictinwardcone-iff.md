---
declaration: theorem
origin: cited
lean: Convex.mem_strictInwardCone_iff
statement: formalized
proof: formalized
---

# Convex.mem_strictInwardCone_iff

In a convex set, a direction is strictly inward if and only if its positive ray meets the
interior. No closedness or finite-dimensionality is required.

```lean
Convex.mem_strictInwardCone_iff.{u_1} {E : Type u_1} [SeminormedAddCommGroup E] [NormedSpace ℝ E]
  {s : Set E} {x v : E} (hs : Convex ℝ s) (hx : x ∈ s) :
  v ∈ TauCeti.strictInwardCone s x ↔ ∃ t, 0 < t ∧ x + t • v ∈ interior s
```

## Depends on

- [TauCeti.strictInwardCone](tauceti-strictinwardcone.md)

## Lean

Formalized in Tau Ceti as [`Convex.mem_strictInwardCone_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Cone/StrictInward.html#Convex.mem_strictInwardCone_iff).

## Sources

- [Tau Ceti documentation: `Convex.mem_strictInwardCone_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Cone/StrictInward.html#Convex.mem_strictInwardCone_iff)
- [Source of `Convex.mem_strictInwardCone_iff` in TauCeti/Analysis/Convex/Cone/StrictInward.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Convex/Cone/StrictInward.lean#L174)
- [Tau Ceti roadmap status: Differential geometry, Part II — relative de Rham theory, fundamental classes and relative transversality](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DeRhamCohomologyAndDuality/STATUS.md)
