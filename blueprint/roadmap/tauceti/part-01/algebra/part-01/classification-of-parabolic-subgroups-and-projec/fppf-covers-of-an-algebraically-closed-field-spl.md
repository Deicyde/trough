---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.eq_top_of_mem_fppfTopology_of_isAlgClosed
statement: formalized
proof: formalized
---

# Fppf covers of an algebraically closed field split

The only fppf covering sieve of
`Spec K` is the maximal sieve.

```lean
AlgebraicGeometry.Scheme.eq_top_of_mem_fppfTopology_of_isAlgClosed.{u} (K : Type u) [Field K]
  [IsAlgClosed K] (S : CategoryTheory.Sieve (AlgebraicGeometry.Spec ↧K))
  (hS : S ∈ AlgebraicGeometry.Scheme.fppfTopology (AlgebraicGeometry.Spec ↧K)) : S = ⊤
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.eq_top_of_mem_fppfTopology_of_isAlgClosed`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Sites/FppfAlgClosed.html#AlgebraicGeometry.Scheme.eq_top_of_mem_fppfTopology_of_isAlgClosed).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.eq_top_of_mem_fppfTopology_of_isAlgClosed`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Sites/FppfAlgClosed.html#AlgebraicGeometry.Scheme.eq_top_of_mem_fppfTopology_of_isAlgClosed)
- [Source of `AlgebraicGeometry.Scheme.eq_top_of_mem_fppfTopology_of_isAlgClosed` in TauCeti/AlgebraicGeometry/Sites/FppfAlgClosed.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Sites/FppfAlgClosed.lean#L48)
- [Tau Ceti roadmap status: Classification of parabolic subgroups and projective homogeneous spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FlagVarieties/STATUS.md)
