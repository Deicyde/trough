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

It is the `(ω, M) = (0, 1)` case of the resolvent-range inequality
`StronglyContinuousSemigroup.norm_le_norm_smul_sub_generator`. Together with
`StronglyContinuousSemigroup.smul_sub_generator_surjective` and the density of the generator
domain, it shows that the hypotheses of the Lumer--Phillips generation theorem are also
necessary.

```lean
TauCeti.Semigroups.ContractionSemigroup.isDissipative_generator.{u_1} {X : Type u_1}
  [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X]
  (S : TauCeti.Semigroups.ContractionSemigroup X) : TauCeti.Semigroups.IsDissipative S.generator
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hille--Yosida characterization](../../part-01/one-parameter-semigroups-completely-monotone-and/hille-yosida-characterization.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Semigroups.ContractionSemigroup.isDissipative_generator`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Dissipative/Basic.html#TauCeti.Semigroups.ContractionSemigroup.isDissipative_generator).

## Other forms

**The converse of the Lumer--Phillips theorem on a Hilbert space.** Formalized in Tau Ceti as [`TauCeti.Semigroups.ContractionSemigroup.real_inner_generator_nonpos`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Dissipative/Hilbert.html#TauCeti.Semigroups.ContractionSemigroup.real_inner_generator_nonpos).

```lean
TauCeti.Semigroups.ContractionSemigroup.real_inner_generator_nonpos.{u_1} {X : Type u_1}
  [NormedAddCommGroup X] [InnerProductSpace ℝ X] [CompleteSpace X]
  (S : TauCeti.Semigroups.ContractionSemigroup X) (x : ↥S.generator.domain) :
  inner ℝ (↑S.generator x) ↑x ≤ 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.Semigroups.ContractionSemigroup.isDissipative_generator`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Dissipative/Basic.html#TauCeti.Semigroups.ContractionSemigroup.isDissipative_generator)
- [Source of `TauCeti.Semigroups.ContractionSemigroup.isDissipative_generator` in TauCeti/Analysis/Semigroups/Dissipative/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Semigroups/Dissipative/Basic.lean#L413)
