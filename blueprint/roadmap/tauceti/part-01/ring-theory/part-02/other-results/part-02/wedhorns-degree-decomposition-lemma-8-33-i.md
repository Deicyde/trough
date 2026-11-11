---
declaration: theorem
origin: cited
lean: TauCeti.Huber.twoSidedRestrictedSubmodule_eq_sup
statement: formalized
proof: formalized
---

# Wedhorn's degree decomposition, Lemma 8.33(i)

A two-sided restricted family is the sum of
its non-negative part and its negative part: `A⟨z, z⁻¹⟩ = A⟨z⟩ + z⁻¹A⟨z⁻¹⟩` at the level of
coefficients. This is `twoSidedRestrictedSubmodule_eq_sup_compl` at the sign partition, which is
where the restrictedness of each summand is established.

```lean
TauCeti.Huber.twoSidedRestrictedSubmodule_eq_sup.{u_1, u_2} (A : Type u_1) (M : Type u_2)
  [Semiring A] [AddCommMonoid M] [TopologicalSpace M] [_root_.Module A M] [ContinuousAdd M]
  [ContinuousConstSMul A M] :
  TauCeti.Huber.twoSidedRestrictedSubmodule A M =
    (TauCeti.Huber.twoSidedRestrictedSubmodule A M ⊓ Submodule.pi {n | 0 ≤ n}ᶜ fun x => ⊥) ⊔
      TauCeti.Huber.twoSidedRestrictedSubmodule A M ⊓ Submodule.pi {n | n < 0}ᶜ fun x => ⊥
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.twoSidedRestrictedSubmodule_eq_sup`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/Restricted/TwoSidedSeries/Basic.html#TauCeti.Huber.twoSidedRestrictedSubmodule_eq_sup).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.twoSidedRestrictedSubmodule_eq_sup`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/Restricted/TwoSidedSeries/Basic.html#TauCeti.Huber.twoSidedRestrictedSubmodule_eq_sup)
- [Source of `TauCeti.Huber.twoSidedRestrictedSubmodule_eq_sup` in TauCeti/RingTheory/Huber/Restricted/TwoSidedSeries/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Huber/Restricted/TwoSidedSeries/Basic.lean#L193)
