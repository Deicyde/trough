---
declaration: module
origin: cited
lean: Physlib.Fin.sum_pi_succ_prod_smul, Physlib.Fin.sum_fin_two_arrow
statement: formalized
proof: formalized
---

# Peeling the first slot off a sum over tuples

The module `PhyslibAlpha.Mathematics.ForMathlib.Fin`, [PhyslibAlpha/Mathematics/ForMathlib/Fin.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Fin.lean): 2 declarations, 2 with a docstring.

> Sums over tuples of indices, split into the first slot and the remaining ones.

## i. Overview

> A monomial in several slots contributes one factor per slot, and summing such monomials over
> all tuples of indices is the basic operation of a component expansion.
> `sum_pi_succ_prod_smul` peels the first slot off such a sum, weighted by one scalar per slot,
> turning a sum over `Fin (n + 1) → ι` into a double sum over `ι` and `Fin n → ι` along
> `Fin.consEquiv`. It is the induction step of the component expansions of tensors.
>
> For two slots the splitting is complete, and `sum_fin_two_arrow` writes a sum over pairs of indices
> as a double sum, the form in which two-index invariant tensors are contracted.

## ii. Key results

> - `Physlib.Fin.sum_pi_succ_prod_smul` : a sum over tuples, weighted by one scalar factor per
>   slot, split into the first slot and the rest.
> - `Physlib.Fin.sum_fin_two_arrow` : a sum over pairs of indices, as a double sum.

## iv. References

> The `Fin.consEquiv` along which the splitting is done is Mathlib's.

## A. Splitting off the first slot

**`Physlib.Fin.sum_pi_succ_prod_smul`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Fin.lean#L54).

> A sum over tuples of indices, weighted by one scalar factor per slot, split into the
> first slot and the remaining ones.

```lean
lemma sum_pi_succ_prod_smul {R M ι : Type*} [CommSemiring R] [AddCommMonoid M] [Module R M]
    [Fintype ι] {n : ℕ} (c : Fin (n + 1) → ι → R) (X : (Fin (n + 1) → ι) → M) :
    ∑ q : Fin (n + 1) → ι, (∏ i, c i (q i)) • X q =
      ∑ b : ι, ∑ p : Fin n → ι, (c 0 b * ∏ i, c i.succ (p i)) • X (Fin.cons b p)
```

**`Physlib.Fin.sum_fin_two_arrow`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Fin.lean#L65).

> A sum over functions from `Fin 2` is a double sum.

```lean
lemma sum_fin_two_arrow {α M : Type*} [Fintype α] [AddCommMonoid M] (F : (Fin 2 → α) → M) :
    ∑ ψ : Fin 2 → α, F ψ = ∑ x, ∑ y, F ![x, y]
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/ForMathlib/Fin.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Fin.lean)
