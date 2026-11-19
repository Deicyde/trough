---
declaration: theorem
origin: cited
lean: TauCeti.DynkinType.isLeast_sum_glueMinimum
statement: formalized
proof: formalized
---

# The shortest norm of a glue word is the sum of the shortest norms of its labels

For a
finite family `t` of valid simply-laced components and a glue word `w`,
`μ(w) = ∑ i, μ_(t i)(w_i)` is the least norm of a dual vector of the orthogonal sum of the root
lattices in the coset `glueWordIsometry t ht hv w` named by `w`, and some dual vector of that coset
has this norm.

```lean
TauCeti.DynkinType.isLeast_sum_glueMinimum.{v} {ι : Type v} [Fintype ι] (t : ι → TauCeti.DynkinType)
  (hv : ∀ (i : ι), (t i).Valid) (ht : ∀ (i : ι), (t i).IsSimplyLaced)
  (w : (i : ι) → ((t i).glueAlphabet ⋯).carrier) :
  IsLeast
    {q |
      ∃ x,
        Submodule.Quotient.mk x = (TauCeti.DynkinType.glueWordIsometry t ht hv) w ∧
          ((TauCeti.IntegralLattice.pi fun i => (t i).rootLattice ⋯).form ↑x) ↑x = q}
    (∑ i, (t i).glueMinimum ⋯ (w i))
```

## Depends on

- [TauCeti.FiniteQuadraticModule](../../../number-theory/part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice-discriminantquadraticmod.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DynkinType.isLeast_sum_glueMinimum`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/RootLattice/GlueAlphabet/CosetMinimum.html#TauCeti.DynkinType.isLeast_sum_glueMinimum).

## Sources

- [Tau Ceti documentation: `TauCeti.DynkinType.isLeast_sum_glueMinimum`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/RootLattice/GlueAlphabet/CosetMinimum.html#TauCeti.DynkinType.isLeast_sum_glueMinimum)
- [Source of `TauCeti.DynkinType.isLeast_sum_glueMinimum` in TauCeti/LinearAlgebra/IntegralLattice/RootLattice/GlueAlphabet/CosetMinimum.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/IntegralLattice/RootLattice/GlueAlphabet/CosetMinimum.lean#L502)
- [Tau Ceti roadmap status: Niemeier glue data and explicit Leech constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Rank24LatticeConstructions/STATUS.md)
