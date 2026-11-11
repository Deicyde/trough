---
declaration: theorem
origin: cited
lean: Finset.sum_piAntidiag_prod_choose, Finset.sum_filter_piAntidiag_prod_choose_fiberwise
statement: formalized
proof: formalized
---

# Vandermonde's identity for finitely many groups

the ways of choosing `n` objects from
groups of sizes `K i`, `i ∈ s`, sorted by how many come from each group.

```lean
Finset.sum_piAntidiag_prod_choose.{u_1} {ι : Type u_1} [DecidableEq ι] (s : Finset ι) (K : ι → ℕ)
  (n : ℕ) : ∑ k ∈ s.piAntidiag n, ∏ i ∈ s, (K i).choose (k i) = (∑ i ∈ s, K i).choose n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Finset.sum_piAntidiag_prod_choose`](https://taucetiproject.org/docs/TauCeti/Data/Nat/Choose/Vandermonde.html#Finset.sum_piAntidiag_prod_choose).

## Other forms

**Vandermonde's identity grouped along a map `f : ι → κ`.** Formalized in Tau Ceti as [`Finset.sum_filter_piAntidiag_prod_choose_fiberwise`](https://taucetiproject.org/docs/TauCeti/Data/Nat/Choose/Vandermonde.html#Finset.sum_filter_piAntidiag_prod_choose_fiberwise).

```lean
Finset.sum_filter_piAntidiag_prod_choose_fiberwise.{u_1, u_2} {ι : Type u_1} [DecidableEq ι]
  {κ : Type u_2} [Fintype ι] [Fintype κ] [DecidableEq κ] (f : ι → κ) (K : ι → ℕ) (m : κ → ℕ) :
  ∑ k ∈ Finset.univ.piAntidiag (∑ j, m j) with ∀ (j : κ), ∑ i with f i = j, k i = m j,
      ∏ i, (K i).choose (k i) =
    ∏ j, (∑ i with f i = j, K i).choose (m j)
```

## Sources

- [Tau Ceti documentation: `Finset.sum_piAntidiag_prod_choose`](https://taucetiproject.org/docs/TauCeti/Data/Nat/Choose/Vandermonde.html#Finset.sum_piAntidiag_prod_choose)
- [Source of `Finset.sum_piAntidiag_prod_choose` in TauCeti/Data/Nat/Choose/Vandermonde.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Data/Nat/Choose/Vandermonde.lean#L45)
