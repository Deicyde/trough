---
declaration: theorem
origin: cited
lean: TauCeti.Semigroups.hilleYosida_generation
statement: formalized
proof: formalized
---

# Hille--Yosida generation theorem

Let `A` be a densely defined operator on a real Banach
space, let `1 ≤ M`, and suppose that every real `lambda > omega` belongs to the resolvent set of
`A`, with the power estimates

`‖R(lambda, A) ^ n‖ ≤ M / (lambda - omega) ^ n` for every `n ≥ 1`.

Then `A` generates a strongly continuous semigroup with growth bound `(omega, M)`. The produced
semigroup is the exponential unshift of the exponent-zero Yosida limit for `A - omega I`.

```lean
TauCeti.Semigroups.hilleYosida_generation.{u_1} {X : Type u_1} [NormedAddCommGroup X]
  [NormedSpace ℝ X] [CompleteSpace X] {A : X →ₗ.[ℝ] X} {M omega : ℝ} (hM : 1 ≤ M)
  (hres : ∀ (lambda : ℝ), omega < lambda → lambda ∈ A.resolventSet)
  (hpow :
    ∀ (n : ℕ),
      1 ≤ n → ∀ (lambda : ℝ), omega < lambda → ‖A.resolvent lambda ^ n‖ ≤ M / (lambda - omega) ^ n)
  (hdense : Dense ↑A.domain) : ∃ S, S.generator = A ∧ S.HasGrowthBound omega M
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Duhamel's identity in supremum norm](../../../part-02/pde/part-01/duhamels-identity-in-supremum-norm.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Semigroups.hilleYosida_generation`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/HilleYosida/Generation.html#TauCeti.Semigroups.hilleYosida_generation).

## Sources

- [Tau Ceti documentation: `TauCeti.Semigroups.hilleYosida_generation`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/HilleYosida/Generation.html#TauCeti.Semigroups.hilleYosida_generation)
- [Source of `TauCeti.Semigroups.hilleYosida_generation` in TauCeti/Analysis/Semigroups/Generation/HilleYosida/Generation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Semigroups/Generation/HilleYosida/Generation.lean#L199)
