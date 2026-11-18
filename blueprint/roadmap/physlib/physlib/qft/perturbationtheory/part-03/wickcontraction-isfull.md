---
declaration: module
origin: cited
lean: WickContraction.card_of_isfull_even, WickContraction.card_of_isfull_odd, WickContraction.IsFull, WickContraction.isFull_iff_equivInvolution_no_fixed_point, WickContraction.isFullInvolutionEquiv
statement: formalized
proof: formalized
---

# Full contraction

The module `Physlib.QFT.PerturbationTheory.WickContraction.IsFull`, [Physlib/QFT/PerturbationTheory/WickContraction/IsFull.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/IsFull.lean): 6 declarations (1 instance with no name), 5 with a docstring, 2 listed as significant.

> We say that a contraction is full if it has no uncontracted fields.

**`WickContraction.IsFull`**, a def, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/IsFull.lean#L31).

> A contraction is full if there are no uncontracted fields, i.e. the finite set
> of uncontracted fields is empty.

```lean
def IsFull : Prop
```

**An instance with no name**, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/IsFull.lean#L34).

> The condition on whether or not a contraction is full is decidable.

```lean
instance : Decidable (IsFull c)
```

**`WickContraction.isFull_iff_equivInvolution_no_fixed_point`**, a lemma, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/IsFull.lean#L36).

```lean
lemma isFull_iff_equivInvolution_no_fixed_point :
    IsFull c ↔ ∀ (i : Fin n), (equivInvolution c).1 i ≠ i
```

**`WickContraction.isFullInvolutionEquiv`**, a def, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/IsFull.lean#L43).

> The equivalence between full contractions and fixed-point free involutions.

```lean
def isFullInvolutionEquiv : {c : WickContraction n // IsFull c} ≃
    {f : Fin n → Fin n // Function.Involutive f ∧ (∀ i, f i ≠ i)}
```

**`WickContraction.card_of_isfull_even`**, a theorem, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/IsFull.lean#L56). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If `n` is even then the number of full contractions is `(n-1)!!`.

```lean
theorem card_of_isfull_even (he : Even n) :
    Fintype.card {c : WickContraction n // IsFull c} = (n - 1)‼
```

**`WickContraction.card_of_isfull_odd`**, a theorem, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/IsFull.lean#L63). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If `n` is odd then there are no full contractions. This is because
> there will always be at least one element unpaired.

```lean
theorem card_of_isfull_odd (ho : Odd n) :
    Fintype.card {c : WickContraction n // IsFull c} = 0
```

## Depends on

- [Equivalence extracting element from contraction](../part-02/wickcontraction-extractequiv.md)
- [Involution associated with a contraction](wickcontraction-involutions.md)

## Proof depends on

- [Fin involutions](../../../mathematics/formathlib/fin-involutions.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/IsFull.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/IsFull.lean)
