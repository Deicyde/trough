---
declaration: theorem
origin: cited
lean: TauCeti.finrank_linearMap_pi_eq_natCard
statement: formalized
proof: formalized
---

# The multiplicity theorem for a product of simple modules

The dimension of the space of
`A`-linear maps from a simple module `S` into a finite product of simple modules counts the
factors isomorphic to `S`.

```lean
TauCeti.finrank_linearMap_pi_eq_natCard.{u_1, u_2, u_3, u_4, u_5} {k : Type u_1} {A : Type u_2}
  {S : Type u_3} [Field k] [IsAlgClosed k] [Ring A] [Algebra k A] [AddCommGroup S]
  [_root_.Module k S] [_root_.Module A S] [IsScalarTower k A S] [IsSimpleModule A S]
  [FiniteDimensional k S] {ι : Type u_4} [Finite ι] {N : ι → Type u_5}
  [(i : ι) → AddCommGroup (N i)] [(i : ι) → _root_.Module k (N i)] [(i : ι) → _root_.Module A (N i)]
  [∀ (i : ι), IsScalarTower k A (N i)] [∀ (i : ι), IsSimpleModule A (N i)] :
  Module.finrank k (S →ₗ[A] (i : ι) → N i) = Nat.card { i // Nonempty (S ≃ₗ[A] N i) }
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Schur's lemma, vanishing form](schurs-lemma-vanishing-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.finrank_linearMap_pi_eq_natCard`](https://taucetiproject.org/docs/TauCeti/RingTheory/Semisimple/Multiplicity.html#TauCeti.finrank_linearMap_pi_eq_natCard).

## Sources

- [Tau Ceti documentation: `TauCeti.finrank_linearMap_pi_eq_natCard`](https://taucetiproject.org/docs/TauCeti/RingTheory/Semisimple/Multiplicity.html#TauCeti.finrank_linearMap_pi_eq_natCard)
- [Source of `TauCeti.finrank_linearMap_pi_eq_natCard` in TauCeti/RingTheory/Semisimple/Multiplicity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Semisimple/Multiplicity.lean#L212)
