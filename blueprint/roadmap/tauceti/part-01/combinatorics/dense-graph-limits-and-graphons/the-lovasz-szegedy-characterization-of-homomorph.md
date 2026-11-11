---
declaration: theorem
origin: cited
lean: TauCeti.DenseGraphLimits.lovasz_szegedy_representability
statement: formalized
proof: formalized
---

# The Lovász–Szegedy characterization of homomorphism densities

A graph parameter is the
homomorphism density of a graphon on an atomless standard Borel carrier `(Ω, μ)`, such as the unit
interval, if and only if it is isomorphism invariant, multiplicative, normalized and reflection
positive.

```lean
TauCeti.DenseGraphLimits.lovasz_szegedy_representability.{u_1} {Ω : Type u_1} [MeasurableSpace Ω]
  [StandardBorelSpace Ω] (μ : MeasureTheory.Measure Ω) [MeasureTheory.IsProbabilityMeasure μ]
  [MeasureTheory.NullSingletonClass μ] (f : TauCeti.DenseGraphLimits.GraphParam) :
  (∃ W,
      ∀ (n : ℕ) (F : SimpleGraph (Fin n)) [inst : DecidableRel F.Adj],
        f n F = TauCeti.DenseGraphLimits.homDensity F W) ↔
    TauCeti.DenseGraphLimits.IsIsoInvariant f ∧
      TauCeti.DenseGraphLimits.IsMultiplicative f ∧
        TauCeti.DenseGraphLimits.IsNormalized f ∧ TauCeti.DenseGraphLimits.IsReflectionPositive f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A measurable function on a product factors through Boolean coordinates](a-measurable-function-on-a-product-factors-throu.md)
- [Frieze--Kannan weak regularity](frieze-kannan-weak-regularity.md)
- [Hoeffding's lemma, oscillation form](../../probability/moments/hoeffdings-lemma-oscillation-form.md)
- [TauCeti.DenseGraphLimits.cutDist](tauceti-densegraphlimits-cutdist.md)
- [TauCeti.DenseGraphLimits.cutDist_triangle](tauceti-densegraphlimits-cutdist-triangle.md)
- [TauCeti.DenseGraphLimits.Graphon.unitIntervalRepr](tauceti-densegraphlimits-graphon-unitintervalrep.md)
- [TauCeti.Probability.empiricalFiniteMeasure](../../probability/random-matrices/tauceti-probability-empiricalfinitemeasure.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DenseGraphLimits.lovasz_szegedy_representability`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/Representability/Representation.html#TauCeti.DenseGraphLimits.lovasz_szegedy_representability).

## Sources

- [Tau Ceti documentation: `TauCeti.DenseGraphLimits.lovasz_szegedy_representability`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/Representability/Representation.html#TauCeti.DenseGraphLimits.lovasz_szegedy_representability)
- [Source of `TauCeti.DenseGraphLimits.lovasz_szegedy_representability` in TauCeti/Combinatorics/DenseGraphLimits/Representability/Representation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/DenseGraphLimits/Representability/Representation.lean#L81)
- [Tau Ceti roadmap status: Dense graph limits and graphons](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/DenseGraphLimits/STATUS.md)
