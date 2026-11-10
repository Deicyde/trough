---
declaration: theorem
origin: cited
lean: TauCeti.Place.exists_forall_mem_ord_sub_eq_and_forall_mem_integers, TauCeti.Place.exists_forall_mem_valuation_sub_le_and_forall_mem_integers
statement: formalized
proof: formalized
---

# Strong approximation (Stichtenoth, Theorem 1.6.5)

for a set `S` of places of `F / k`
that is not all of them and a finite subset `s ⊆ S`, some `x : F` satisfies
`ord_P (x - f P) = r P` at every `P ∈ s` and is regular at every place of `S` outside `s`.

The orders on `s` are prescribed exactly, as in weak approximation
(`TauCeti.Place.exists_forall_mem_ord_sub_eq`); what strong approximation adds is the regularity
of `x` at the remaining places of `S`, at the price of requiring `S` to be proper.

```lean
TauCeti.Place.exists_forall_mem_ord_sub_eq_and_forall_mem_integers.{u_1, u_2} {k : Type u_1}
  {F : Type u_2} [Field k] [Field F] [Algebra k F] (hF : TauCeti.IsFunctionField k F)
  (hex : IsIntegrallyClosedIn k F) {S : Set (TauCeti.Place k F)} (hS : S ≠ Set.univ)
  {s : Finset (TauCeti.Place k F)} (hsS : ↑s ⊆ S) (f : TauCeti.Place k F → F)
  (r : TauCeti.Place k F → ℤ) :
  ∃ x, (∀ P ∈ s, P.ord (x - f P) = r P) ∧ ∀ P ∈ S, P ∉ s → x ∈ P.integers
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Riemann's theorem](../../algebraic-curves-function-fields-divisors-and-ri/riemanns-theorem.md)
- [The weak approximation theorem](../part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Place.exists_forall_mem_ord_sub_eq_and_forall_mem_integers`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Consequences/StrongApproximation.html#TauCeti.Place.exists_forall_mem_ord_sub_eq_and_forall_mem_integers).

## Other forms

**Strong approximation, in the inequality form (Stichtenoth, Theorem 1.6.5).** Formalized in Tau Ceti as [`TauCeti.Place.exists_forall_mem_valuation_sub_le_and_forall_mem_integers`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Consequences/StrongApproximation.html#TauCeti.Place.exists_forall_mem_valuation_sub_le_and_forall_mem_integers).

```lean
TauCeti.Place.exists_forall_mem_valuation_sub_le_and_forall_mem_integers.{u_1, u_2} {k : Type u_1}
  {F : Type u_2} [Field k] [Field F] [Algebra k F] (hF : TauCeti.IsFunctionField k F)
  (hex : IsIntegrallyClosedIn k F) {S : Set (TauCeti.Place k F)} (hS : S ≠ Set.univ)
  {s : Finset (TauCeti.Place k F)} (hsS : ↑s ⊆ S) (f : TauCeti.Place k F → F)
  (r : TauCeti.Place k F → ℤ) :
  ∃ x, (∀ P ∈ s, P.valuation (x - f P) ≤ WithZero.exp (-r P)) ∧ ∀ P ∈ S, P ∉ s → x ∈ P.integers
```

## Sources

- [Tau Ceti documentation: `TauCeti.Place.exists_forall_mem_ord_sub_eq_and_forall_mem_integers`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Consequences/StrongApproximation.html#TauCeti.Place.exists_forall_mem_ord_sub_eq_and_forall_mem_integers)
- [Source of `TauCeti.Place.exists_forall_mem_ord_sub_eq_and_forall_mem_integers` in TauCeti/FieldTheory/FunctionField/Consequences/StrongApproximation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Consequences/StrongApproximation.lean#L128)
