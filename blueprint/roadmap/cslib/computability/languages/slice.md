---
catalog: module
lean: Language.slice, Language.slice_eq_true_iff, Language.ofSlices, Language.mem_ofSlices, Language.ofFn_mem_ofSlices, Language.slice_ofSlices
statement: formalized
proof: formalized
---

# Slices of languages

`Cslib.Computability.Languages.Slice`, in [Cslib/Computability/Languages/Slice.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Slice.lean), by Samuel Schlesinger.

> A language is the union of its slices, one for each word length. The slice at length `n` is a
> Boolean-valued function of the `n` letters of a word, so it can be handled by models of
> computation with a fixed number of inputs, such as circuits. Conversely, one such function for
> each length assembles into a language, and slicing that language recovers the functions.
>
> Membership in an arbitrary language is not decidable, so a slice is defined classically. This is
> what lets notions defined for Boolean-valued functions, such as circuit complexity, apply to every
> language rather than only to decidable ones.

`Language.slice` (definition, [line 31](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Slice.lean#L31))

> The words of length `n` in `L`, as a Boolean-valued function of their letters.

```lean
noncomputable def slice (L : Language α) (n : ℕ) : (Fin n → α) → Bool
```

`Language.slice_eq_true_iff` (theorem, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Slice.lean#L34))

```lean
theorem slice_eq_true_iff {L : Language α} {n : ℕ} {x : Fin n → α} :
    L.slice n x = true ↔ List.ofFn x ∈ L
```

`Language.ofSlices` (definition, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Slice.lean#L39))

> The language whose slice at each length `n` is `f n`.

```lean
def ofSlices (f : ∀ n, (Fin n → α) → Bool) : Language α
```

`Language.mem_ofSlices` (theorem, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Slice.lean#L42))

```lean
theorem mem_ofSlices {f : ∀ n, (Fin n → α) → Bool} {w : List α} :
    w ∈ ofSlices f ↔ f w.length (w[·])
```

`Language.ofFn_mem_ofSlices` (theorem, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Slice.lean#L45))

```lean
theorem ofFn_mem_ofSlices {f : ∀ n, (Fin n → α) → Bool} {n : ℕ} {x : Fin n → α} :
    .ofFn x ∈ ofSlices f ↔ f n x
```

`Language.slice_ofSlices` (theorem, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Slice.lean#L50))

```lean
theorem slice_ofSlices (f : ∀ n, (Fin n → α) → Bool) (n : ℕ) :
    (ofSlices f).slice n = f n
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Computability/Languages/Slice.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Slice.lean)
