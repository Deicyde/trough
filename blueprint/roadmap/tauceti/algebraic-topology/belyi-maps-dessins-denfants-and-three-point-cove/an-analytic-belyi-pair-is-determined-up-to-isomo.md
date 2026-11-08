---
declaration: theorem
origin: cited
lean: TauCeti.AnalyticBelyiPair.toIsoClass_injective
statement: formalized
proof: formalized
---

# An analytic Belyi pair is determined up to isomorphism by its permutation triple

```lean
TauCeti.AnalyticBelyiPair.toIsoClass_injective (n : ℕ) :
  Function.Injective (TauCeti.AnalyticBelyiPair.toIsoClass n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Analytic Belyi pairs are classified by finite covers of the thrice-punctured sphere](analytic-belyi-pairs-are-classified-by-finite-co.md)
- [The analytic inverse function theorem](../../analysis/part-01/analytic/the-analytic-inverse-function-theorem.md)
- [Connected covers of `ℂ ∖ {0, 1}` of degree `n` up to isomorphism are classified by the isomorphism classes of connected triples of degree `n`](connected-covers-of-c-0-1-of-degree-n-up-to-isom.md)
- [The isomorphism `π₁(S¹) ≃* ℤ` is the degree](../universal-covers/the-isomorphism-1-s1-z-is-the-degree.md)
- [The open mapping theorem](../../analysis/part-02/complex/part-02/the-open-mapping-theorem.md)
- [Rouché's theorem for a disc, classical form](../../analysis/part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-02/rouches-theorem-for-a-disc-classical-form.md)
- [TauCeti.CoveringSpace](../universal-covers/tauceti-coveringspace.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AnalyticBelyiPair.toIsoClass_injective`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/AnalyticBelyiPair.html#TauCeti.AnalyticBelyiPair.toIsoClass_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.AnalyticBelyiPair.toIsoClass_injective`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/AnalyticBelyiPair.html#TauCeti.AnalyticBelyiPair.toIsoClass_injective)
- [Source of `TauCeti.AnalyticBelyiPair.toIsoClass_injective` in TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/AnalyticBelyiPair.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/AnalyticBelyiPair.lean#L366)
