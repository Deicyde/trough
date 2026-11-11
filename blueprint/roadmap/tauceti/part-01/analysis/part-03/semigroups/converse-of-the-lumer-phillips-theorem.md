---
declaration: theorem
origin: cited
lean: TauCeti.Semigroups.ContractionSemigroup.isDissipative_generator, TauCeti.Semigroups.ContractionSemigroup.real_inner_generator_nonpos
statement: formalized
proof: formalized
---

# Converse of the Lumer--Phillips theorem

the generator of a contraction semigroup is
dissipative.

This holds on any real normed space `X`: completeness is not needed. Together with
`StronglyContinuousSemigroup.smul_sub_generator_surjective` and the density of the generator
domain, it shows that the hypotheses of the Lumer--Phillips generation theorem are also
necessary.

```lean
TauCeti.Semigroups.ContractionSemigroup.isDissipative_generator.{u_1} {X : Type u_1}
  [NormedAddCommGroup X] [NormedSpace ℝ X] (S : TauCeti.Semigroups.ContractionSemigroup X) :
  TauCeti.Semigroups.IsDissipative S.generator
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Semigroups.ContractionSemigroup.isDissipative_generator`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Dissipative/Basic.html#TauCeti.Semigroups.ContractionSemigroup.isDissipative_generator).

## Other forms

**The converse of the Lumer--Phillips theorem on an inner-product space.** Formalized in Tau Ceti as [`TauCeti.Semigroups.ContractionSemigroup.real_inner_generator_nonpos`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Dissipative/Hilbert.html#TauCeti.Semigroups.ContractionSemigroup.real_inner_generator_nonpos).

```lean
TauCeti.Semigroups.ContractionSemigroup.real_inner_generator_nonpos.{u_1} {X : Type u_1}
  [NormedAddCommGroup X] [InnerProductSpace ℝ X] (S : TauCeti.Semigroups.ContractionSemigroup X)
  (x : ↥S.generator.domain) : inner ℝ (↑S.generator x) ↑x ≤ 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.Semigroups.ContractionSemigroup.isDissipative_generator`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Dissipative/Basic.html#TauCeti.Semigroups.ContractionSemigroup.isDissipative_generator)
- [Source of `TauCeti.Semigroups.ContractionSemigroup.isDissipative_generator` in TauCeti/Analysis/Semigroups/Dissipative/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Semigroups/Dissipative/Basic.lean#L416)
