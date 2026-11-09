---
declaration: theorem
origin: cited
lean: TauCeti.finrank_linearMap_eq_natCard_of_linearEquiv_pi
statement: formalized
proof: formalized
---

# The multiplicity theorem

If `M` decomposes as a finite direct sum of simple modules
`N i`, then the dimension of the space of `A`-linear maps from a simple module `S` into `M` is
the number of factors isomorphic to `S`.

Only the right-hand side mentions the decomposition, so this is the statement that the
multiplicity of `S` in `M` is an invariant of `M`; see
`TauCeti.natCard_eq_natCard_of_linearEquiv_pi`.

```lean
TauCeti.finrank_linearMap_eq_natCard_of_linearEquiv_pi.{u_1, u_2, u_3, u_4, u_5, u_6} {k : Type u_1}
  {A : Type u_2} {S : Type u_3} [Field k] [IsAlgClosed k] [Ring A] [Algebra k A] [AddCommGroup S]
  [_root_.Module k S] [_root_.Module A S] [IsScalarTower k A S] [IsSimpleModule A S]
  [FiniteDimensional k S] {ι : Type u_4} [Finite ι] {N : ι → Type u_5}
  [(i : ι) → AddCommGroup (N i)] [(i : ι) → _root_.Module k (N i)] [(i : ι) → _root_.Module A (N i)]
  [∀ (i : ι), IsScalarTower k A (N i)] [∀ (i : ι), IsSimpleModule A (N i)] {M : Type u_6}
  [AddCommGroup M] [_root_.Module k M] [_root_.Module A M] [IsScalarTower k A M]
  (e : M ≃ₗ[A] (i : ι) → N i) :
  Module.finrank k (S →ₗ[A] M) = Nat.card { i // Nonempty (S ≃ₗ[A] N i) }
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Schur's lemma, vanishing form](schurs-lemma-vanishing-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.finrank_linearMap_eq_natCard_of_linearEquiv_pi`](https://taucetiproject.org/docs/TauCeti/RingTheory/Semisimple/Multiplicity.html#TauCeti.finrank_linearMap_eq_natCard_of_linearEquiv_pi).

## Sources

- [Tau Ceti documentation: `TauCeti.finrank_linearMap_eq_natCard_of_linearEquiv_pi`](https://taucetiproject.org/docs/TauCeti/RingTheory/Semisimple/Multiplicity.html#TauCeti.finrank_linearMap_eq_natCard_of_linearEquiv_pi)
- [Source of `TauCeti.finrank_linearMap_eq_natCard_of_linearEquiv_pi` in TauCeti/RingTheory/Semisimple/Multiplicity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Semisimple/Multiplicity.lean#L220)
