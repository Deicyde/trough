---
declaration: theorem
origin: cited
lean: Convex.exists_uniform_ball_subset_of_mem_strictInwardCone
statement: formalized
proof: formalized
---

# Convex.exists_uniform_ball_subset_of_mem_strictInwardCone

The inward ball estimates can be chosen uniformly near any strictly inward point-vector
pair, as long as the perturbed starting point stays in the convex set.

```lean
Convex.exists_uniform_ball_subset_of_mem_strictInwardCone.{u_1} {E : Type u_1}
  [SeminormedAddCommGroup E] [NormedSpace ℝ E] {s : Set E} {x v : E} (hs : Convex ℝ s)
  (hv : v ∈ TauCeti.strictInwardCone s x) :
  ∃ ε > 0,
    ∃ δ > 0,
      ∀ᶠ (p : E × E) in nhds (x, v),
        p.1 ∈ s → ∀ t ∈ Set.Ioo 0 δ, Metric.ball (p.1 + t • p.2) (ε * t) ⊆ s
```

## Depends on

- [TauCeti.strictInwardCone](tauceti-strictinwardcone.md)

## Lean

Formalized in Tau Ceti as [`Convex.exists_uniform_ball_subset_of_mem_strictInwardCone`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Cone/StrictInward.html#Convex.exists_uniform_ball_subset_of_mem_strictInwardCone).

## Sources

- [Tau Ceti documentation: `Convex.exists_uniform_ball_subset_of_mem_strictInwardCone`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Cone/StrictInward.html#Convex.exists_uniform_ball_subset_of_mem_strictInwardCone)
- [Source of `Convex.exists_uniform_ball_subset_of_mem_strictInwardCone` in TauCeti/Analysis/Convex/Cone/StrictInward.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Convex/Cone/StrictInward.lean#L186)
- [Tau Ceti roadmap status: Differential geometry, Part II — relative de Rham theory, fundamental classes and relative transversality](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DeRhamCohomologyAndDuality/STATUS.md)
