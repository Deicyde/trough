---
declaration: module
origin: cited
lean: Physlib.Fin.sum_pi_succ_prod_smul, Physlib.Fin.sum_filter_weight_succ
statement: formalized
proof: formalized
---

# Peeling the first slot off a sum over tuples

The module `PhyslibAlpha.Mathematics.ForMathlib.Fin`, [PhyslibAlpha/Mathematics/ForMathlib/Fin.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ForMathlib/Fin.lean): 2 declarations, 2 with a docstring.

> Sums over tuples of indices, split into the first slot and the remaining ones.

## i. Overview

> A monomial in several slots contributes one factor per slot, and summing such monomials over
> all tuples of indices is the basic operation of a component expansion. Both lemmas here peel
> the first slot off such a sum, turning a sum over `Fin (n + 1) → ι` into a double sum over `ι`
> and `Fin n → ι` along `Fin.consEquiv`. `sum_pi_succ_prod_smul` does this for a sum weighted by
> one scalar per slot, and `sum_filter_weight_succ` for a sum restricted to the tuples of a
> prescribed total weight, where the first slot takes its own weight and the rest make up the
> remainder. They are the induction steps of the component expansions which the weight
> decompositions run on.

## ii. Key results

> - `Physlib.Fin.sum_pi_succ_prod_smul` : a sum over tuples, weighted by one scalar factor per
>   slot, split into the first slot and the rest.
> - `Physlib.Fin.sum_filter_weight_succ` : the same split for a sum over the tuples of a
>   prescribed total weight.

## iv. References

> The `Fin.consEquiv` along which the splitting is done is Mathlib's.

## A. Splitting off the first slot

**`Physlib.Fin.sum_pi_succ_prod_smul`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ForMathlib/Fin.lean#L57).

> A sum over tuples of indices, weighted by one scalar factor per slot, split into the
> first slot and the remaining ones.

```lean
lemma sum_pi_succ_prod_smul {R M ι : Type*} [CommSemiring R] [AddCommMonoid M] [Module R M]
    [Fintype ι] {n : ℕ} (c : Fin (n + 1) → ι → R) (X : (Fin (n + 1) → ι) → M) :
    ∑ q : Fin (n + 1) → ι, (∏ i, c i (q i)) • X q =
      ∑ b : ι, ∑ p : Fin n → ι, (c 0 b * ∏ i, c i.succ (p i)) • X (Fin.cons b p)
```

**`Physlib.Fin.sum_filter_weight_succ`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ForMathlib/Fin.lean#L71).

> Peeling the first slot off a sum over the tuples of a prescribed total weight: the first
> slot takes its own weight `w b` and the remaining slots make up the rest. Each slot draws its
> letter from the same alphabet `ι`, `w` gives a letter its weight and the weights of the slots
> add; `f s` is the factor contributed by slot `s`.

```lean
lemma sum_filter_weight_succ {R ι : Type*} [CommSemiring R] [Fintype ι] {n : ℕ} (w : ι → ℤ)
    (f : Fin (n + 1) → ι → R) (m : ℤ) :
    ∑ q ∈ Finset.univ.filter (fun q : Fin (n + 1) → ι => (∑ s, w (q s)) = m), ∏ s, f s (q s)
      = ∑ b : ι, f 0 b
          * ∑ q ∈ Finset.univ.filter (fun q : Fin n → ι => (∑ s, w (q s)) = m - w b),
              ∏ s, f s.succ (q s)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/ForMathlib/Fin.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ForMathlib/Fin.lean)
