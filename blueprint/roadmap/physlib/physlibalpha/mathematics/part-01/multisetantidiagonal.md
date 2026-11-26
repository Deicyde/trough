---
declaration: module
origin: cited
lean: Multiset.sum_antidiagonal_assoc, Multiset.sum_antidiagonal_exchange, Multiset.sum_linearMap_apply, Multiset.tmul_sum, Multiset.sum_antidiagonal_swap, Multiset.sum_map_neg'', Multiset.sum_map_finsetSum, Multiset.fst_le_of_mem_antidiagonal
statement: formalized
proof: formalized
---

# Sums over the antidiagonal of a multiset

The module `PhyslibAlpha.Mathematics.MultisetAntidiagonal`, [PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean): 13 declarations, 13 with a docstring.

## i. Overview

> Combinatorial identities for sums indexed by `Multiset.antidiagonal`: associativity and
> exchange of nested antidiagonal sums, collapsing a sum whose terms vanish off one slot, and
> the interaction with linear maps and tensor products. These are the bookkeeping behind the
> all-orders Leibniz rules of the jet calculus.

## ii. Key results

> - `sum_antidiagonal_assoc` : coassociativity of antidiagonal sums: summing over `s = u + v` and then
>   `u = x + y` is summing over `s = x + t` and then `t = y + v`
> - `sum_antidiagonal_exchange` : the exchange law of doubly-split antidiagonal sums
> - `sum_antidiagonal_assoc_cycle` : a sum over triple splittings is invariant under the cyclic
>   shift of the three parts
> - `sum_linearMap_apply` : a multiset sum of linear maps, applied: the sum of the applications
> - `tmul_sum` : a pure tensor against a multiset sum distributes over the sum

## iv. References

> * None.

## A. Sums over the antidiagonal

**`Multiset.sum_antidiagonal_assoc`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L52).

> Coassociativity of antidiagonal sums. Summing over `s = u + v` and then `u = x + y`
> is summing over `s = x + t` and then `t = y + v`.

```lean
lemma sum_antidiagonal_assoc {ι M : Type*} [AddCommMonoid M]
    (s : Multiset ι) (h : Multiset ι → Multiset ι → Multiset ι → M) :
    (s.antidiagonal.map fun p =>
      (p.1.antidiagonal.map fun q => h q.1 q.2 p.2).sum).sum =
    (s.antidiagonal.map fun p =>
      (p.2.antidiagonal.map fun q => h p.1 q.1 q.2).sum).sum
```

**`Multiset.sum_antidiagonal_exchange`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L71).

> The exchange law of doubly-split antidiagonal sums. Splitting `s = u + v` and then
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

**`Multiset.sum_linearMap_apply`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L90).

> A multiset sum of linear maps, applied, is the sum of the applications.

```lean
lemma sum_linearMap_apply {R M N : Type*} [Semiring R] [AddCommMonoid M]
    [AddCommMonoid N] [Module R M] [Module R N] (S : Multiset (M →ₗ[R] N)) (x : M) :
    S.sum x = (S.map fun f => f x).sum
```

**`Multiset.tmul_sum`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L98).

> A pure tensor against a multiset sum distributes over the sum.

```lean
lemma tmul_sum {R M N : Type*} [CommSemiring R] [AddCommMonoid M]
    [AddCommMonoid N] [Module R M] [Module R N] (m : M) (S : Multiset N) :
    m ⊗ₜ[R] S.sum = (S.map fun n => m ⊗ₜ[R] n).sum
```

**`Multiset.sum_antidiagonal_swap`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L106).

> Antidiagonal sums are symmetric under swapping the two parts.

```lean
lemma sum_antidiagonal_swap {ι M : Type*} [AddCommMonoid M]
    (s : Multiset ι) (h : Multiset ι → Multiset ι → M) :
    (s.antidiagonal.map fun p => h p.1 p.2).sum =
    (s.antidiagonal.map fun p => h p.2 p.1).sum
```

**`Multiset.sum_map_neg''`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L119).

> A multiset sum of negations is the negation of the sum.

```lean
lemma sum_map_neg'' {ι M : Type*} [AddCommGroup M]
    (s : Multiset ι) (f : ι → M) :
    (s.map fun i => -f i).sum = -(s.map f).sum
```

**`Multiset.sum_map_finsetSum`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L129).

> The exchange of a finite sum with a multiset sum.

```lean
lemma sum_map_finsetSum {α β M : Type*} [AddCommMonoid M]
    (m : Multiset α) (t : Finset β) (f : β → α → M) :
    (m.map fun a => ∑ b ∈ t, f b a).sum = ∑ b ∈ t, (m.map (f b)).sum
```

**`Multiset.fst_le_of_mem_antidiagonal`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L139).

> The first part of a splitting of `s` is a sub-multiset of `s`.

```lean
lemma fst_le_of_mem_antidiagonal {ι : Type*} {s : Multiset ι} {p : Multiset ι × Multiset ι}
    (hp : p ∈ s.antidiagonal) : p.1 ≤ s
```

**`Multiset.snd_le_of_mem_antidiagonal`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L144).

> The second part of a splitting of `s` is a sub-multiset of `s`.

```lean
lemma snd_le_of_mem_antidiagonal {ι : Type*} {s : Multiset ι} {p : Multiset ι × Multiset ι}
    (hp : p ∈ s.antidiagonal) : p.2 ≤ s
```

**`Multiset.sum_antidiagonal_eq_of_fst_ne_zero`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L151).

> A sum over the antidiagonal of a family vanishing off `p.1 = 0` collapses to the
> single term at `(0, s)`.

```lean
lemma sum_antidiagonal_eq_of_fst_ne_zero {ι M : Type*} [AddCommMonoid M]
    (s : Multiset ι) (F : Multiset ι × Multiset ι → M)
    (hF : ∀ p ∈ s.antidiagonal, p.1 ≠ 0 → F p = 0) :
    (s.antidiagonal.map F).sum = F (0, s)
```

**`Multiset.sum_antidiagonal_eq_of_snd_ne_zero`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L173).

> A sum over the antidiagonal of a family vanishing off `p.2 = 0` collapses to the
> single term at `(s, 0)`.

```lean
lemma sum_antidiagonal_eq_of_snd_ne_zero {ι M : Type*} [AddCommMonoid M]
    (s : Multiset ι) (F : Multiset ι × Multiset ι → M)
    (hF : ∀ p ∈ s.antidiagonal, p.2 ≠ 0 → F p = 0) :
    (s.antidiagonal.map F).sum = F (s, 0)
```

**`Multiset.sum_antidiagonal_middle_exchange`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L187).

> The exchange of the second and third slot in a nested antidiagonal sum.

```lean
lemma sum_antidiagonal_middle_exchange {ι M : Type*} [AddCommMonoid M]
    (s : Multiset ι) (h : Multiset ι → Multiset ι → Multiset ι → M) :
    (s.antidiagonal.map fun p =>
        (p.1.antidiagonal.map fun q => h q.1 q.2 p.2).sum).sum
      = (s.antidiagonal.map fun p =>
        (p.1.antidiagonal.map fun q => h q.1 p.2 q.2).sum).sum
```

**`Multiset.sum_antidiagonal_assoc_cycle`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean#L200).

> A nested antidiagonal sum over the splittings `s = x + y + z` is invariant under the cyclic
> shift `(x, y, z) ↦ (z, x, y)` of the summand.

```lean
lemma sum_antidiagonal_assoc_cycle {ι M : Type*} [AddCommMonoid M]
    (s : Multiset ι) (h : Multiset ι → Multiset ι → Multiset ι → M) :
    (s.antidiagonal.map fun p =>
        (p.1.antidiagonal.map fun q => h q.1 q.2 p.2).sum).sum
      = (s.antidiagonal.map fun p =>
        (p.1.antidiagonal.map fun q => h p.2 q.1 q.2).sum).sum
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/MultisetAntidiagonal.lean)
