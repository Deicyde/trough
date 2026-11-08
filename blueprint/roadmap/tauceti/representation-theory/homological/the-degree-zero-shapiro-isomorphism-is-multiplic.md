---
declaration: theorem
origin: cited
lean: TauCeti.ContCohomology.explicitShapiro0_explicitCup00
statement: formalized
proof: formalized
---

# The degree-zero Shapiro isomorphism is multiplicative for the `(0,0)` cup product

```lean
TauCeti.ContCohomology.explicitShapiro0_explicitCup00.{uG, uA, uB, uC} (G : Type uG) [Group G]
  [TopologicalSpace G] [SeparatelyContinuousMul G] (U : Subgroup G) (A : Type uA) [AddCommGroup A]
  [DistribMulAction (↥U) A] (B : Type uB) [AddCommGroup B] [DistribMulAction (↥U) B] (C : Type uC)
  [AddCommGroup C] [DistribMulAction (↥U) C] (μ : A →+ B →+ C)
  (hμ : ∀ (u : ↥U) (a : A) (b : B), (μ (u • a)) (u • b) = u • (μ a) b)
  (a : ↥(TauCeti.ContCohomology.H0 G (TauCeti.DiscreteCoind G U A)))
  (b : ↥(TauCeti.ContCohomology.H0 G (TauCeti.DiscreteCoind G U B))) :
  (TauCeti.ContCohomology.explicitShapiro0 G U C)
      (((TauCeti.ContCohomology.explicitCup00 G (TauCeti.DiscreteCoind G U A)
            (TauCeti.DiscreteCoind G U B) (TauCeti.DiscreteCoind G U C)
            (TauCeti.DiscreteCoind.pointwisePairing U μ hμ) ⋯)
          a)
        b) =
    ((TauCeti.ContCohomology.explicitCup00 (↥U) A B C μ hμ)
        ((TauCeti.ContCohomology.explicitShapiro0 G U A) a))
      ((TauCeti.ContCohomology.explicitShapiro0 G U B) b)
```

## Depends on

- [Shapiro's lemma in every degree](shapiros-lemma-in-every-degree.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ContCohomology.explicitShapiro0_explicitCup00`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/Shapiro.html#TauCeti.ContCohomology.explicitShapiro0_explicitCup00).

## Sources

- [Tau Ceti documentation: `TauCeti.ContCohomology.explicitShapiro0_explicitCup00`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/Shapiro.html#TauCeti.ContCohomology.explicitShapiro0_explicitCup00)
- [Source of `TauCeti.ContCohomology.explicitShapiro0_explicitCup00` in TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/Shapiro.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/Shapiro.lean#L89)
