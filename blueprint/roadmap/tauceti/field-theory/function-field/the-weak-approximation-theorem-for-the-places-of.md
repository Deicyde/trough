---
declaration: theorem
origin: cited
lean: TauCeti.Place.exists_forall_ord_sub_eq
statement: formalized
proof: formalized
---

# The weak approximation theorem for the places of an algebraic function field (Stichtenoth, Theorem 1.3.1), in the equality form

for finitely many pairwise distinct places
`P i`, arbitrary target functions `f i` and arbitrary prescribed integers `r i`, some single
`g : F` satisfies `ord_{P i} (g - f i) = r i` for every `i`.

The prescription is an equality, not an inequality: the error `g - f i` is not merely small at
`P i`, its order there is exactly `r i`. In particular `g - f i ≠ 0` whenever `r i ≠ 0`.

```lean
TauCeti.Place.exists_forall_ord_sub_eq.{u, v, u_1} {k : Type u} {F : Type v} [Field k] [Field F]
  [Algebra k F] {ι : Type u_1} [Finite ι] {P : ι → TauCeti.Place k F} (hP : Function.Injective P)
  (f : ι → F) (r : ι → ℤ) : ∃ g, ∀ (i : ι), (P i).ord (g - f i) = r i
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Place.exists_forall_ord_sub_eq`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Approximation.html#TauCeti.Place.exists_forall_ord_sub_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Place.exists_forall_ord_sub_eq`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Approximation.html#TauCeti.Place.exists_forall_ord_sub_eq)
- [Source of `TauCeti.Place.exists_forall_ord_sub_eq` in TauCeti/FieldTheory/FunctionField/Place/Approximation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Place/Approximation.lean#L82)
