---
catalog: module
lean: Cslib.ωSequence.Step, Cslib.ωSequence.Step.mk, Cslib.ωSequence.LeadsTo, Cslib.ωSequence.LeadsTo.mk, Cslib.ωSequence.step_leadsTo, Cslib.ωSequence.leadsTo_trans, Cslib.ωSequence.leadsTo_cases_or, Cslib.ωSequence.until_frequently_not_leadsTo, Cslib.ωSequence.until_frequently_leadsTo_and, Cslib.ωSequence.frequently_leadsTo_frequently, Cslib.ωSequence.drop_frequently_iff_frequently
statement: formalized
proof: formalized
---

# Temporal reasoning over infinite sequences

`Cslib.Foundations.Data.OmegaSequence.Temporal`, in [Cslib/Foundations/Data/OmegaSequence/Temporal.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Temporal.lean), by Ching-Tsun Chou.

`Cslib.ωSequence.Step` (definition, [line 27](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Temporal.lean#L27))

> `Step p q` means that whenever `p` holds at a position in `xs`, `q` holds at the next position
> in `xs`.

```lean
def Step (xs : ωSequence α) (p q : Set α) : Prop
```

`Cslib.ωSequence.Step.mk` (theorem, [line 30](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Temporal.lean#L30))

```lean
theorem Step.mk {xs : ωSequence α} (h : ∀ k, xs k ∈ p → xs (k + 1) ∈ q) : Step xs p q
```

`Cslib.ωSequence.LeadsTo` (definition, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Temporal.lean#L38))

> "`p` leads to `q`" means that whenever `p` holds at a position in `xs`, `q` holds at the same
> or a later position in `xs`.

```lean
def LeadsTo (xs : ωSequence α) (p q : Set α) : Prop
```

`Cslib.ωSequence.LeadsTo.mk` (theorem, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Temporal.lean#L41))

```lean
theorem LeadsTo.mk {xs : ωSequence α} (h : ∀ k, xs k ∈ p → ∃ k', k ≤ k' ∧ xs k' ∈ q) :
    LeadsTo xs p q
```

`Cslib.ωSequence.step_leadsTo` (theorem, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Temporal.lean#L49))

> `Step` implies `LeadsTo`.

```lean
theorem step_leadsTo {p q : Set α} (h : xs.Step p q) : xs.LeadsTo p q
```

`Cslib.ωSequence.leadsTo_trans` (theorem, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Temporal.lean#L54))

> `LeadsTo` is transitive.

```lean
theorem leadsTo_trans {p q r : Set α}
    (h1 : xs.LeadsTo p q) (h2 : xs.LeadsTo q r) : xs.LeadsTo p r
```

`Cslib.ωSequence.leadsTo_cases_or` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Temporal.lean#L59))

> If `p ∩ q` leads to `r` and `p ∩ qᶜ` leads to `s`, then `p` leads to `r ∪ s`.

```lean
theorem leadsTo_cases_or {p q r s : Set α}
    (h1 : xs.LeadsTo (p ∩ q) r) (h2 : xs.LeadsTo (p ∩ qᶜ) s) : xs.LeadsTo p (r ∪ s)
```

`Cslib.ωSequence.until_frequently_not_leadsTo` (theorem, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Temporal.lean#L64))

> If `p` holds until `q` and `p` fails infinitely often, then `p` leads to `q`.

```lean
theorem until_frequently_not_leadsTo {p q : Set α}
    (h1 : xs.Step (p ∩ qᶜ) p) (h2 : ∃ᶠ k in atTop, xs k ∉ p) : xs.LeadsTo p q
```

`Cslib.ωSequence.until_frequently_leadsTo_and` (theorem, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Temporal.lean#L76))

> If `p` holds until `q` and `q` holds infinite often, then `p` leads to `p ∩ q`.

```lean
theorem until_frequently_leadsTo_and {p q : Set α}
    (h1 : xs.Step (p ∩ qᶜ) p) (h2 : ∃ᶠ k in atTop, xs k ∈ q) : xs.LeadsTo p (p ∩ q)
```

`Cslib.ωSequence.frequently_leadsTo_frequently` (theorem, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Temporal.lean#L88))

> If `p` holds infinitely often and `p` leads to `q`, then `q` holds infinite often as well.

```lean
theorem frequently_leadsTo_frequently {p q : Set α}
    (h1 : ∃ᶠ k in atTop, xs k ∈ p) (h2 : xs.LeadsTo p q) : ∃ᶠ k in atTop, xs k ∈ q
```

`Cslib.ωSequence.drop_frequently_iff_frequently` (theorem, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Temporal.lean#L95))

```lean
theorem drop_frequently_iff_frequently {p : Set α} (n : ℕ) :
    (∃ᶠ k in atTop, (xs.drop n) k ∈ p) ↔ (∃ᶠ k in atTop, xs k ∈ p)
```

## Depends on

- [Definition of `ωSequence` and functions on infinite sequences](defs.md)

## Proof depends on

- [ω-sequences a.k.a. infinite sequences](init.md)

## Sources

- [Cslib/Foundations/Data/OmegaSequence/Temporal.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Temporal.lean)
