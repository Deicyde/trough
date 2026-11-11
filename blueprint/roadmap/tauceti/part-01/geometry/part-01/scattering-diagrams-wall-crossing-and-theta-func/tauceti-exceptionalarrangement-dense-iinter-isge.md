---
declaration: theorem
origin: cited
lean: TauCeti.ExceptionalArrangement.dense_iInter_isGeneric
statement: formalized
proof: formalized
---

# TauCeti.ExceptionalArrangement.dense_iInter_isGeneric

A countable family of finite arrangements has dense common generic locus.

```lean
TauCeti.ExceptionalArrangement.dense_iInter_isGeneric.{u_1, u_2, u_3} {V : Type u_1} {P : Type u_2}
  [NormedAddCommGroup V] [NormedSpace ℝ V] [MetricSpace P] [NormedAddTorsor V P]
  [FiniteDimensional ℝ V] {ι : Type u_3} [Countable ι]
  (E : ι → TauCeti.ExceptionalArrangement ℝ P) : Dense {x | ∀ (i : ι), (E i).IsGeneric x}
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ExceptionalArrangement.dense_iInter_isGeneric`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Affine/Generic.html#TauCeti.ExceptionalArrangement.dense_iInter_isGeneric).

## Sources

- [Tau Ceti documentation: `TauCeti.ExceptionalArrangement.dense_iInter_isGeneric`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Affine/Generic.html#TauCeti.ExceptionalArrangement.dense_iInter_isGeneric)
- [Source of `TauCeti.ExceptionalArrangement.dense_iInter_isGeneric` in TauCeti/Analysis/Normed/Affine/Generic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Affine/Generic.lean#L305)
- [Tau Ceti roadmap status: Scattering diagrams, wall crossing and theta functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ScatteringDiagrams/STATUS.md)
