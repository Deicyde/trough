---
declaration: theorem
origin: cited
lean: TauCeti.Semigroups.IsMDissipative.exists_contractionSemigroup_generator_eq
statement: formalized
proof: formalized
---

# The Lumer--Phillips generation theorem

A densely defined m-dissipative operator on a
real Banach space generates a strongly continuous contraction semigroup.

Dissipativity plus the range condition packaged in `IsMDissipative` is exactly the hypothesis
set of Lumer--Phillips; the semigroup produced is the strong limit of the semigroups generated
by the Yosida approximations of `A`.

```lean
TauCeti.Semigroups.IsMDissipative.exists_contractionSemigroup_generator_eq.{u_1} {X : Type u_1}
  [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X] {A : X →ₗ.[ℝ] X}
  (hA : TauCeti.Semigroups.IsMDissipative A) (hdense : Dense ↑A.domain) : ∃ S, S.generator = A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Converse of the Lumer--Phillips theorem](converse-of-the-lumer-phillips-theorem.md)
- [Duhamel's identity in supremum norm](../pde/part-01/duhamels-identity-in-supremum-norm.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Semigroups.IsMDissipative.exists_contractionSemigroup_generator_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/LumerPhillips.html#TauCeti.Semigroups.IsMDissipative.exists_contractionSemigroup_generator_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Semigroups.IsMDissipative.exists_contractionSemigroup_generator_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/LumerPhillips.html#TauCeti.Semigroups.IsMDissipative.exists_contractionSemigroup_generator_eq)
- [Source of `TauCeti.Semigroups.IsMDissipative.exists_contractionSemigroup_generator_eq` in TauCeti/Analysis/Semigroups/Generation/LumerPhillips.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Semigroups/Generation/LumerPhillips.lean#L83)
