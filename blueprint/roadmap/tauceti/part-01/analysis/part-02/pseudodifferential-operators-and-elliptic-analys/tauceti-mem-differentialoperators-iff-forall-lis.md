---
declaration: theorem
origin: cited
lean: TauCeti.mem_differentialOperators_iff_forall_list_prod
statement: formalized
proof: formalized
---

# TauCeti.mem_differentialOperators_iff_forall_list_prod

A differential operator has order at most `m` exactly when all its `(m + 1)`-fold iterated
commutators with multiplication by elements of `A` vanish.

```lean
TauCeti.mem_differentialOperators_iff_forall_list_prod.{u_1, u_2, u_3, u_4} {R : Type u_1}
  {A : Type u_2} {M : Type u_3} {N : Type u_4} [CommSemiring R] [CommSemiring A] [Algebra R A]
  [AddCommMonoid M] [_root_.Module A M] [_root_.Module R M] [IsScalarTower R A M] [AddCommGroup N]
  [_root_.Module A N] [_root_.Module R N] [IsScalarTower R A N] {D : M →ₗ[R] N} {m : ℕ} :
  D ∈ TauCeti.differentialOperators R A M N m ↔
    ∀ (a : Fin (m + 1) → A), (List.ofFn fun i => TauCeti.smulCommutator R (a i)).prod D = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.mem_differentialOperators_iff_forall_list_prod`](https://taucetiproject.org/docs/TauCeti/RingTheory/Derivation/DifferentialOperator.html#TauCeti.mem_differentialOperators_iff_forall_list_prod).

## Sources

- [Tau Ceti documentation: `TauCeti.mem_differentialOperators_iff_forall_list_prod`](https://taucetiproject.org/docs/TauCeti/RingTheory/Derivation/DifferentialOperator.html#TauCeti.mem_differentialOperators_iff_forall_list_prod)
- [Source of `TauCeti.mem_differentialOperators_iff_forall_list_prod` in TauCeti/RingTheory/Derivation/DifferentialOperator.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Derivation/DifferentialOperator.lean#L270)
- [Tau Ceti roadmap status: Pseudodifferential operators and elliptic analysis on bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PseudodifferentialOperators/STATUS.md)
