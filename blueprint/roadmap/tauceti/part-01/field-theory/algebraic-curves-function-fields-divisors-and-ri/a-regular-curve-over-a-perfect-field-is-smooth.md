---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.IsCurveOver.smoothOfRelativeDimension_one_of_perfectField
statement: formalized
proof: formalized
---

# A regular curve over a perfect field is smooth

if the local rings of a curve `X` over a
perfect field `k` at its codimension-one points are discrete valuation rings, then `X` is smooth
of relative dimension one over `k`.

```lean
AlgebraicGeometry.Scheme.IsCurveOver.smoothOfRelativeDimension_one_of_perfectField.{u} (k : Type u)
  [Field k] (X : AlgebraicGeometry.Scheme) [X.Over (AlgebraicGeometry.Spec ↧k)] [PerfectField k]
  [AlgebraicGeometry.Scheme.IsCurveOver k]
  [∀ (y : TauCeti.AlgebraicGeometry.CodimensionOnePoint X),
      IsDiscreteValuationRing ↑(X.presheaf.stalk ↑y)] :
  AlgebraicGeometry.SmoothOfRelativeDimension 1 (X ↘ AlgebraicGeometry.Spec ↧k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The global dimension of a regular local ring is its Krull dimension](../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [TauCeti.globalDimension](../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.IsCurveOver.smoothOfRelativeDimension_one_of_perfectField`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/Smooth.html#AlgebraicGeometry.Scheme.IsCurveOver.smoothOfRelativeDimension_one_of_perfectField).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.IsCurveOver.smoothOfRelativeDimension_one_of_perfectField`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/Smooth.html#AlgebraicGeometry.Scheme.IsCurveOver.smoothOfRelativeDimension_one_of_perfectField)
- [Source of `AlgebraicGeometry.Scheme.IsCurveOver.smoothOfRelativeDimension_one_of_perfectField` in TauCeti/AlgebraicGeometry/Curves/Smooth.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Curves/Smooth.lean#L53)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AlgebraicCurves/STATUS.md)
