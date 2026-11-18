---
catalog: module
lean: Finset.card_filter_not_le_card_filter_of_involution, Finset.card_div_two_le_card_filter_of_involution
statement: formalized
proof: formalized
---

# Counting via involutions

`Cslib.Foundations.Data.Finset.Involution`, in [Cslib/Foundations/Data/Finset/Involution.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Finset/Involution.lean), by Samuel Schlesinger.

> If `σ` is an involution on a finset `s` and every orbit `{x, σ x}` meets a
> predicate `p`, then at least half of `s` satisfies `p`. This is the
> combinatorial core of pairing arguments such as the Ehrenfeucht–Haussler–
> Kearns–Valiant lower bound on PAC sample complexity.
>
> ## Main statements
>
> - `Finset.card_filter_not_le_card_filter_of_involution`: the elements of `s`
>   failing `p` inject via `σ` into those satisfying `p`.
> - `Finset.card_div_two_le_card_filter_of_involution`: at least half of `s`
>   satisfies `p`.

`Finset.card_filter_not_le_card_filter_of_involution` (theorem, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Finset/Involution.lean#L35))

> If `σ` is an involution on `s` and every orbit `{x, σ x}` meets `p`, then
> `σ` injects the elements of `s` failing `p` into those satisfying `p`.

```lean
theorem card_filter_not_le_card_filter_of_involution
    (hσ : ∀ x ∈ s, σ (σ x) = x) (hσs : ∀ x ∈ s, σ x ∈ s)
    (hp : ∀ x ∈ s, p x ∨ p (σ x)) :
    #(s.filter fun x => ¬ p x) ≤ #(s.filter p)
```

`Finset.card_div_two_le_card_filter_of_involution` (theorem, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Finset/Involution.lean#L45))

> If `σ` is an involution on `s` and every orbit `{x, σ x}` meets `p`, then
> at least half of `s` satisfies `p`.

```lean
theorem card_div_two_le_card_filter_of_involution
    (hσ : ∀ x ∈ s, σ (σ x) = x) (hσs : ∀ x ∈ s, σ x ∈ s)
    (hp : ∀ x ∈ s, p x ∨ p (σ x)) :
    #s / 2 ≤ #(s.filter p)
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Data/Finset/Involution.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Finset/Involution.lean)
