---
declaration: theorem
origin: cited
lean: TauCeti.Ideal.mem_inertia_iff_of_adjoin_eq_top
statement: formalized
proof: formalized
---

# Serre's criterion

When `S` is generated over `R` by a set `s` and `G` acts by `R`-algebra
automorphisms, membership in the inertia subgroup of a two-sided ideal `I` is decided on `s` alone:
the elements moved into `I` form an `R`-subalgebra.

```lean
TauCeti.Ideal.mem_inertia_iff_of_adjoin_eq_top.{u_1, u_2, u_3} {G : Type u_1} [Group G]
  {S : Type u_2} [Ring S] [MulSemiringAction G S] {R : Type u_3} [CommSemiring R] [Algebra R S]
  [SMulCommClass G R S] {I : Ideal S} [I.IsTwoSided] {s : Set S} (hs : Algebra.adjoin R s = ⊤)
  {σ : G} : σ ∈ Ideal.inertia G I ↔ ∀ x ∈ s, σ • x - x ∈ I
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Ideal.mem_inertia_iff_of_adjoin_eq_top`](https://taucetiproject.org/docs/TauCeti/RingTheory/Ideal/Inertia.html#TauCeti.Ideal.mem_inertia_iff_of_adjoin_eq_top).

## Sources

- [Tau Ceti documentation: `TauCeti.Ideal.mem_inertia_iff_of_adjoin_eq_top`](https://taucetiproject.org/docs/TauCeti/RingTheory/Ideal/Inertia.html#TauCeti.Ideal.mem_inertia_iff_of_adjoin_eq_top)
- [Source of `TauCeti.Ideal.mem_inertia_iff_of_adjoin_eq_top` in TauCeti/RingTheory/Ideal/Inertia.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Ideal/Inertia.lean#L44)
