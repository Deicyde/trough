---
declaration: theorem
origin: cited
lean: TauCeti.hom_eq_zero_of_isEmpty_linearEquiv, TauCeti.endAlgEquivSelfOfIsSimpleModule, LinearEquiv.finrank_linearMap_eq_one, TauCeti.finrank_linearMap_eq_zero_of_isEmpty_linearEquiv
statement: formalized
proof: formalized
---

# Schur's lemma, vanishing form

A linear map between simple modules is zero if the two
modules are not linearly equivalent.

The `IsEmpty` hypothesis is the constructive form of saying that no equivalence exists.

```lean
TauCeti.hom_eq_zero_of_isEmpty_linearEquiv.{u, v, w} {R : Type u} [Ring R] {M : Type v} {N : Type w}
  [AddCommGroup M] [_root_.Module R M] [AddCommGroup N] [_root_.Module R N] [IsSimpleModule R M]
  [IsSimpleModule R N] (h : IsEmpty (M ≃ₗ[R] N)) (f : M →ₗ[R] N) : f = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.hom_eq_zero_of_isEmpty_linearEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Semisimple/Schur.html#TauCeti.hom_eq_zero_of_isEmpty_linearEquiv).

## Other forms

**Schur's lemma over an algebraically closed field.** Formalized in Tau Ceti as [`TauCeti.endAlgEquivSelfOfIsSimpleModule`](https://taucetiproject.org/docs/TauCeti/RingTheory/Semisimple/Schur.html#TauCeti.endAlgEquivSelfOfIsSimpleModule).

```lean
TauCeti.endAlgEquivSelfOfIsSimpleModule.{u, v, w} {k : Type u} {A : Type v} {S : Type w} [Field k]
  [IsAlgClosed k] [Ring A] [Algebra k A] [AddCommGroup S] [_root_.Module k S] [_root_.Module A S]
  [IsScalarTower k A S] [IsSimpleModule A S] [FiniteDimensional k S] : Module.End A S ≃ₐ[k] k
```

**Schur's lemma over an algebraically closed field, in dimensions.** Formalized in Tau Ceti as [`LinearEquiv.finrank_linearMap_eq_one`](https://taucetiproject.org/docs/TauCeti/RingTheory/Semisimple/Schur.html#LinearEquiv.finrank_linearMap_eq_one).

```lean
LinearEquiv.finrank_linearMap_eq_one.{u_1, u_2, u_3, u_4} {k : Type u_1} {A : Type u_2}
  {S : Type u_3} [Field k] [IsAlgClosed k] [Ring A] [Algebra k A] [AddCommGroup S]
  [_root_.Module k S] [_root_.Module A S] [IsScalarTower k A S] [IsSimpleModule A S]
  [FiniteDimensional k S] {N : Type u_4} [AddCommGroup N] [_root_.Module k N] [_root_.Module A N]
  [IsScalarTower k A N] (e : S ≃ₗ[A] N) : Module.finrank k (S →ₗ[A] N) = 1
```

**Schur's lemma, vanishing form, in dimensions.** Formalized in Tau Ceti as [`TauCeti.finrank_linearMap_eq_zero_of_isEmpty_linearEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Semisimple/Schur.html#TauCeti.finrank_linearMap_eq_zero_of_isEmpty_linearEquiv).

```lean
TauCeti.finrank_linearMap_eq_zero_of_isEmpty_linearEquiv.{u_1, u_2, u_3, u_4} {k : Type u_1}
  {A : Type u_2} {S : Type u_3} {N : Type u_4} [CommSemiring k] [Ring A] [Algebra k A]
  [AddCommGroup S] [_root_.Module A S] [IsSimpleModule A S] [AddCommGroup N] [_root_.Module k N]
  [_root_.Module A N] [IsScalarTower k A N] [IsSimpleModule A N] (h : IsEmpty (S ≃ₗ[A] N)) :
  Module.finrank k (S →ₗ[A] N) = 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.hom_eq_zero_of_isEmpty_linearEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Semisimple/Schur.html#TauCeti.hom_eq_zero_of_isEmpty_linearEquiv)
- [Source of `TauCeti.hom_eq_zero_of_isEmpty_linearEquiv` in TauCeti/RingTheory/Semisimple/Schur.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Semisimple/Schur.lean#L79)
