---
declaration: theorem
origin: cited
lean: TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_iff_forall_prime
statement: formalized
proof: formalized
---

# An induction theorem, one prime at a time and with coefficients in a subring

Let `A` be a
subring of `k` admitting an additive map `t : A → ℤ` with `t 1 = 1`; for example `ℤ[ζ]` for a root
of unity `ζ` in characteristic zero (`PowerBasis.exists_linearMap_apply_one`). The virtual
characters induced from a family of subgroups exhaust `R(G)` exactly when, for every prime `p`,
some multiple `m • 1` with `p ∤ m` is an `A`-linear combination of them.

This reduces an induction theorem to a separate statement for each prime `p`. In Serre's proof of
Brauer's induction theorem, that statement is supplied, for the elementary subgroups, by the
`p`-elementary subgroups with coefficients in `ℤ[ζ]`, `ζ` a primitive `|G|`-th root of unity; this
declaration does not prove it.

```lean
TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_iff_forall_prime.{u, v} {k : Type u}
  {G : Type v} [Field k] [Group G] [Finite G] {P : Subgroup G → Prop} [IsAlgClosed k]
  (A : Subring k) (t : ↥A →+ ℤ) (ht : t 1 = 1) :
  TauCeti.ClassFunction.indVirtualCharacters k G P = TauCeti.virtualCharacters k G ↔
    ∀ (p : ℕ),
      Nat.Prime p →
        ∃ m, ¬p ∣ m ∧ m • 1 ∈ Submodule.span ↥A ↑(TauCeti.ClassFunction.indVirtualCharacters k G P)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [An induction theorem is a single membership](an-induction-theorem-is-a-single-membership.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_iff_forall_prime`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Ideal.html#TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_iff_forall_prime).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_iff_forall_prime`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Ideal.html#TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_iff_forall_prime)
- [Source of `TauCeti.ClassFunction.indVirtualCharacters_eq_virtualCharacters_iff_forall_prime` in TauCeti/RepresentationTheory/Induction/Ideal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Induction/Ideal.lean#L432)
