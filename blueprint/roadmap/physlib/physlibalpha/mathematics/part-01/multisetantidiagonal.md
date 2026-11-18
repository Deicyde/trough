---
declaration: module
origin: cited
lean: Multiset.sum_antidiagonal_assoc, Multiset.sum_antidiagonal_exchange, Multiset.sum_linearMap_apply, Multiset.tmul_sum, Multiset.sum_antidiagonal_swap, Multiset.sum_map_neg'', Multiset.sum_map_finsetSum, Multiset.fst_le_of_mem_antidiagonal
statement: formalized
proof: formalized
---

# Sums over the antidiagonal of a multiset

The module `PhyslibAlpha.Mathematics.MultisetAntidiagonal`, [PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean): 12 declarations, 12 with a docstring.

## i. Overview

> Combinatorial identities for sums indexed by `Multiset.antidiagonal`: associativity and
> exchange of nested antidiagonal sums, collapsing a sum whose terms vanish off one slot, and
> the interaction with linear maps and tensor products. These are the bookkeeping behind the
> all-orders Leibniz rules of the jet calculus.

## ii. Key results

> - `sum_antidiagonal_assoc` : coassociativity of antidiagonal sums: summing over `s = u + v` and then
>   `u = x + y` is summing over `s = x + t` and then `t = y + v`
> - `sum_antidiagonal_exchange`
> - `sum_linearMap_apply` : a multiset sum of linear maps, applied: the sum of the applications
> - `tmul_sum` : a pure tensor against a multiset sum distributes over the sum

## iv. References

> * None.

## A. Sums over the antidiagonal

**`Multiset.sum_antidiagonal_assoc`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L50).

> Coassociativity of antidiagonal sums: summing over `s = u + v` and then `u = x + y`
> is summing over `s = x + t` and then `t = y + v`.

```lean
lemma sum_antidiagonal_assoc {ι M : Type*} [AddCommMonoid M]
    (s : Multiset ι) (h : Multiset ι → Multiset ι → Multiset ι → M) :
    (s.antidiagonal.map fun p =>
      (p.1.antidiagonal.map fun q => h q.1 q.2 p.2).sum).sum =
    (s.antidiagonal.map fun p =>
      (p.2.antidiagonal.map fun q => h p.1 q.1 q.2).sum).sum
```

**`Multiset.sum_antidiagonal_exchange`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L69).

> The exchange law of doubly-split antidiagonal sums: splitting `s = u + v` and then
> `u = x + y`, `v = z + w` is, with the middle parts exchanged, splitting `s = u' + v'`
> and then `u' = x + z`, `v' = y + w`.

```lean
lemma sum_antidiagonal_exchange {ι M : Type*} [AddCommMonoid M]
    (s : Multiset ι) (h : Multiset ι → Multiset ι → Multiset ι → Multiset ι → M) :
    (s.antidiagonal.map fun p =>
      (p.1.antidiagonal.map fun q =>
        (p.2.antidiagonal.map fun r => h q.1 q.2 r.1 r.2).sum).sum).sum =
    (s.antidiagonal.map fun p =>
      (p.1.antidiagonal.map fun q =>
        (p.2.antidiagonal.map fun r => h q.1 r.1 q.2 r.2).sum).sum).sum
```

**`Multiset.sum_linearMap_apply`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L88).

> A multiset sum of linear maps, applied: the sum of the applications.

```lean
lemma sum_linearMap_apply {R M N : Type*} [Semiring R] [AddCommMonoid M]
    [AddCommMonoid N] [Module R M] [Module R N] (S : Multiset (M →ₗ[R] N)) (x : M) :
    S.sum x = (S.map fun f => f x).sum
```

**`Multiset.tmul_sum`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L96).

> A pure tensor against a multiset sum distributes over the sum.

```lean
lemma tmul_sum {R M N : Type*} [CommSemiring R] [AddCommMonoid M]
    [AddCommMonoid N] [Module R M] [Module R N] (m : M) (S : Multiset N) :
    m ⊗ₜ[R] S.sum = (S.map fun n => m ⊗ₜ[R] n).sum
```

**`Multiset.sum_antidiagonal_swap`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L104).

> Antidiagonal sums are symmetric under swapping the two parts.

```lean
lemma sum_antidiagonal_swap {ι M : Type*} [AddCommMonoid M]
    (s : Multiset ι) (h : Multiset ι → Multiset ι → M) :
    (s.antidiagonal.map fun p => h p.1 p.2).sum =
    (s.antidiagonal.map fun p => h p.2 p.1).sum
```

**`Multiset.sum_map_neg''`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L117).

> A multiset sum of negations is the negation of the sum.

```lean
lemma sum_map_neg'' {ι M : Type*} [AddCommGroup M]
    (s : Multiset ι) (f : ι → M) :
    (s.map fun i => -f i).sum = -(s.map f).sum
```

**`Multiset.sum_map_finsetSum`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L127).

> The exchange of a finite sum with a multiset sum.

```lean
lemma sum_map_finsetSum {α β M : Type*} [AddCommMonoid M]
    (m : Multiset α) (t : Finset β) (f : β → α → M) :
    (m.map fun a => ∑ b ∈ t, f b a).sum = ∑ b ∈ t, (m.map (f b)).sum
```

**`Multiset.fst_le_of_mem_antidiagonal`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L137).

> The first part of a splitting of `s` is a sub-multiset of `s`.

```lean
lemma fst_le_of_mem_antidiagonal {ι : Type*} {s : Multiset ι} {p : Multiset ι × Multiset ι}
    (hp : p ∈ s.antidiagonal) : p.1 ≤ s
```

**`Multiset.snd_le_of_mem_antidiagonal`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L142).

> The second part of a splitting of `s` is a sub-multiset of `s`.

```lean
lemma snd_le_of_mem_antidiagonal {ι : Type*} {s : Multiset ι} {p : Multiset ι × Multiset ι}
    (hp : p ∈ s.antidiagonal) : p.2 ≤ s
```

**`Multiset.sum_antidiagonal_eq_of_fst_ne_zero`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L149).

> A sum over the antidiagonal of a family vanishing off `p.1 = 0` collapses to the
> single term at `(0, s)`.

```lean
lemma sum_antidiagonal_eq_of_fst_ne_zero {ι M : Type*} [AddCommMonoid M]
    (s : Multiset ι) (F : Multiset ι × Multiset ι → M)
    (hF : ∀ p ∈ s.antidiagonal, p.1 ≠ 0 → F p = 0) :
    (s.antidiagonal.map F).sum = F (0, s)
```

**`Multiset.sum_antidiagonal_eq_of_snd_ne_zero`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L171).

> A sum over the antidiagonal of a family vanishing off `p.2 = 0` collapses to the
> single term at `(s, 0)`.

```lean
lemma sum_antidiagonal_eq_of_snd_ne_zero {ι M : Type*} [AddCommMonoid M]
    (s : Multiset ι) (F : Multiset ι × Multiset ι → M)
    (hF : ∀ p ∈ s.antidiagonal, p.2 ≠ 0 → F p = 0) :
    (s.antidiagonal.map F).sum = F (s, 0)
```

**`Multiset.sum_antidiagonal_middle_exchange`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L185).

> The exchange of the second and third slot in a nested antidiagonal sum.

```lean
lemma sum_antidiagonal_middle_exchange {ι M : Type*} [AddCommMonoid M]
    (s : Multiset ι) (h : Multiset ι → Multiset ι → Multiset ι → M) :
    (s.antidiagonal.map fun p =>
        (p.1.antidiagonal.map fun q => h q.1 q.2 p.2).sum).sum
      = (s.antidiagonal.map fun p =>
        (p.1.antidiagonal.map fun q => h q.1 p.2 q.2).sum).sum
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean)
