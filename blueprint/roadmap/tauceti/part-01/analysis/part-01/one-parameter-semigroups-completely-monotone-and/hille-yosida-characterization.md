---
declaration: theorem
origin: cited
lean: TauCeti.Semigroups.hilleYosida_generation_iff
statement: formalized
proof: formalized
---

# Hille--Yosida characterization

An unbounded operator is the generator of a strongly
continuous semigroup with growth bound `(omega, M)` if and only if `1 ≤ M`, its domain is dense,
the half-line `(omega, ∞)` lies in its resolvent set, and its resolvent powers satisfy the sharp
Hille--Yosida estimates.

```lean
TauCeti.Semigroups.hilleYosida_generation_iff.{u_1} {X : Type u_1} [NormedAddCommGroup X]
  [NormedSpace ℝ X] [CompleteSpace X] (A : X →ₗ.[ℝ] X) (M omega : ℝ) :
  (∃ S, S.generator = A ∧ S.HasGrowthBound omega M) ↔
    1 ≤ M ∧
      Dense ↑A.domain ∧
        (∀ (lambda : ℝ), omega < lambda → lambda ∈ A.resolventSet) ∧
          ∀ (n : ℕ),
            1 ≤ n →
              ∀ (lambda : ℝ), omega < lambda → ‖A.resolvent lambda ^ n‖ ≤ M / (lambda - omega) ^ n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Sharp Hille--Yosida power bound for the generator resolvent](../../part-03/semigroups/sharp-hille-yosida-power-bound-for-the-generator.md)

## Informally uses

- [Hille--Yosida for contraction semigroups](hille-yosida-for-contraction-semigroups.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Semigroups.hilleYosida_generation_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/HilleYosida/Generation.html#TauCeti.Semigroups.hilleYosida_generation_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Semigroups.hilleYosida_generation_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/HilleYosida/Generation.html#TauCeti.Semigroups.hilleYosida_generation_iff)
- [Source of `TauCeti.Semigroups.hilleYosida_generation_iff` in TauCeti/Analysis/Semigroups/Generation/HilleYosida/Generation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Semigroups/Generation/HilleYosida/Generation.lean#L215)
- [Tau Ceti roadmap status: One-parameter semigroups, completely monotone and positive-definite functions, and Bochner-type representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/OneParameterSemigroups/STATUS.md)
