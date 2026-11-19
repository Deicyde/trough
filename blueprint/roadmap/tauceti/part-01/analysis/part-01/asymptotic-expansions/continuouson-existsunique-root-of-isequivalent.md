---
declaration: theorem
origin: cited
lean: ContinuousOn.existsUnique_root_of_isEquivalent
statement: formalized
proof: formalized
---

# ContinuousOn.existsUnique_root_of_isEquivalent

DLMF 2.2.1: if `f` is continuous and strictly increasing on `[a, ∞)` and `f(x) ∼ x` as
`x → +∞`, then for every `y > f(a)` the equation `f(x) = y` has a unique root in `(a, ∞)`.

```lean
ContinuousOn.existsUnique_root_of_isEquivalent {f : ℝ → ℝ} {a : ℝ} (hf : ContinuousOn f (Set.Ici a))
  (hmono : StrictMonoOn f (Set.Ici a)) (hfx : Asymptotics.IsEquivalent Filter.atTop f id) {y : ℝ}
  (hy : f a < y) : ∃! x, a < x ∧ f x = y
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousOn.existsUnique_root_of_isEquivalent`](https://taucetiproject.org/docs/TauCeti/Analysis/Asymptotics/TranscendentalEquation.html#ContinuousOn.existsUnique_root_of_isEquivalent).

## Sources

- [Tau Ceti documentation: `ContinuousOn.existsUnique_root_of_isEquivalent`](https://taucetiproject.org/docs/TauCeti/Analysis/Asymptotics/TranscendentalEquation.html#ContinuousOn.existsUnique_root_of_isEquivalent)
- [Source of `ContinuousOn.existsUnique_root_of_isEquivalent` in TauCeti/Analysis/Asymptotics/TranscendentalEquation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Asymptotics/TranscendentalEquation.lean#L38)
- [Tau Ceti roadmap status: Asymptotic expansions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AsymptoticExpansions/STATUS.md)
