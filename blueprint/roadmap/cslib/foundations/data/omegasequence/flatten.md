---
catalog: module
lean: Cslib.ωSequence.cumLen, Cslib.ωSequence.cumLen_zero, Cslib.ωSequence.cumLen_succ, Cslib.ωSequence.cumLen_one_add_drop, Cslib.ωSequence.cumLen_strictMono, Cslib.ωSequence.cumLen_segment_zero, Cslib.ωSequence.cumLen_segment_one_add, Cslib.ωSequence.flatten, Cslib.ωSequence.flatten_def, Cslib.ωSequence.flatten_get_add, Cslib.ωSequence.flatten_get_cumLen, Cslib.ωSequence.cons_flatten, Cslib.ωSequence.append_flatten, Cslib.ωSequence.map_length_take_sum, Cslib.ωSequence.flatten_take_drop, Cslib.ωSequence.flatten_take, Cslib.ωSequence.flatten_drop, Cslib.ωSequence.extract_flatten, Cslib.ωSequence.forall_flatten_iff, Cslib.ωSequence.toSegs, Cslib.ωSequence.toSegs_def, Cslib.ωSequence.segment_toSegs_cumLen, Cslib.ωSequence.strictMono_flatten
statement: formalized
proof: formalized
---

# Flattening an infinite sequence of lists

`Cslib.Foundations.Data.OmegaSequence.Flatten`, in [Cslib/Foundations/Data/OmegaSequence/Flatten.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean), by Ching-Tsun Chou.

> Given `ls : ωSequence (List α)`, `ls.flatten` is the infinite sequence formed by
> concatenating all members of `ls`.  For this definition to make proper sense,
> we will consistently assume that all lists in `ls` are nonempty.  Furthermore,
> in order to simplify the definition, we will also assume [Inhabited α].

`Cslib.ωSequence.cumLen` (definition, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L34))

> Given an ω-sequence `ls` of lists, `ls.cumLen k` is the cumulative sum
> of `(ls k).length` for `k = 0, ..., k - 1`.

```lean
def cumLen (ls : ωSequence (List α)) : ℕ → ℕ
```

`Cslib.ωSequence.cumLen_zero` (theorem, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L41))

```lean
theorem cumLen_zero {ls : ωSequence (List α)} :
    ls.cumLen 0 = 0
```

`Cslib.ωSequence.cumLen_succ` (theorem, [line 46](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L46))

```lean
theorem cumLen_succ (ls : ωSequence (List α)) (k : ℕ) :
    ls.cumLen (k + 1) = ls.cumLen k + (ls k).length
```

`Cslib.ωSequence.cumLen_one_add_drop` (theorem, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L50))

```lean
theorem cumLen_one_add_drop (ls : ωSequence (List α)) (k : ℕ) :
    ls.cumLen (1 + k) = (ls 0).length + (ls.drop 1).cumLen k
```

`Cslib.ωSequence.cumLen_strictMono` (theorem, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L55))

> If all lists in `ls` are nonempty, then `ls.cumLen` is strictly monotonic.

```lean
theorem cumLen_strictMono {ls : ωSequence (List α)} (h_ls : ∀ k, 0 < (ls k).length) :
    StrictMono ls.cumLen
```

`Cslib.ωSequence.cumLen_segment_zero` (theorem, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L60))

```lean
theorem cumLen_segment_zero {ls : ωSequence (List α)} (h_ls : ∀ k, 0 < (ls k).length)
    (n : ℕ) (h_n : n < (ls 0).length) : segment ls.cumLen n = 0
```

`Cslib.ωSequence.cumLen_segment_one_add` (theorem, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L66))

```lean
theorem cumLen_segment_one_add {ls : ωSequence (List α)} (h_ls : ∀ k, 0 < (ls k).length)
    (n : ℕ) (h_n : (ls 0).length ≤ n) :
    segment ls.cumLen n = 1 + segment (ls.drop 1).cumLen (n - (ls 0).length)
```

`Cslib.ωSequence.flatten` (definition, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L78))

> Given an ω-sequence `ls` of lists, `ls.flatten` is the infinite sequence
> formed by the concatenation of all of them.  For the definition to make proper
> sense, we will consistently assume that all lists in `ls` are nonempty.

```lean
noncomputable def flatten [Inhabited α] (ls : ωSequence (List α)) : ωSequence α
```

`Cslib.ωSequence.flatten_def` (theorem, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L81))

```lean
theorem flatten_def [Inhabited α] (ls : ωSequence (List α)) (n : ℕ) :
    flatten ls n = (ls (segment ls.cumLen n))[n - ls.cumLen (segment ls.cumLen n)]!
```

`Cslib.ωSequence.flatten_get_add` (theorem, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L85))

```lean
theorem flatten_get_add [Inhabited α] (ls : ωSequence (List α)) {n k : ℕ}
    (hk : k < (ls n).length) (hpos : ∀ n, 0 < (ls n).length) :
    ls.flatten (ls.cumLen n + k) = (ls n)[k]
```

`Cslib.ωSequence.flatten_get_cumLen` (theorem, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L92))

```lean
theorem flatten_get_cumLen [Inhabited α] (ls : ωSequence (List α)) {n : ℕ}
    (hpos : ∀ n, 0 < (ls n).length) : ls.flatten (ls.cumLen n) = (ls n)[0]'(hpos n)
```

`Cslib.ωSequence.cons_flatten` (theorem, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L98))

> `ls.flatten` equals the concatenation of `ls.head` and `ls.tail.flatten`.

```lean
theorem cons_flatten [Inhabited α] {ls : ωSequence (List α)} (h_ls : ∀ k, 0 < (ls k).length) :
    ls.head ++ω ls.tail.flatten = ls.flatten
```

`Cslib.ωSequence.append_flatten` (theorem, [line 110](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L110))

> `ls.flatten` equals the concatenation of `(ls.take n).flatten` and `(ls.drop n).flatten`.

```lean
theorem append_flatten [Inhabited α] {ls : ωSequence (List α)} (h_ls : ∀ k, 0 < (ls k).length)
    (n : ℕ) : (ls.take n).flatten ++ω (ls.drop n).flatten = ls.flatten
```

`Cslib.ωSequence.map_length_take_sum` (theorem, [line 116](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L116))

> The sum of `List.map List.length (take n ls)` is `ls.cumLen n`.

```lean
theorem map_length_take_sum {ls : ωSequence (List α)} (n : ℕ) :
    (List.map List.length (take n ls)).sum = ls.cumLen n
```

`Cslib.ωSequence.flatten_take_drop` (theorem, [line 122](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L122))

> In fact, `(ls.take n).flatten` is `ls.flatten.take (ls.cumLen n)`
> and `(ls.drop n).flatten` is `ls.flatten.drop (ls.cumLen n)`.

```lean
theorem flatten_take_drop [Inhabited α]
    {ls : ωSequence (List α)} (h_ls : ∀ k, 0 < (ls k).length) (n : ℕ) :
    (ls.take n).flatten = ls.flatten.take (ls.cumLen n) ∧
    (ls.drop n).flatten = ls.flatten.drop (ls.cumLen n)
```

`Cslib.ωSequence.flatten_take` (theorem, [line 130](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L130))

```lean
theorem flatten_take [Inhabited α]
    {ls : ωSequence (List α)} (h_ls : ∀ k, 0 < (ls k).length) (n : ℕ) :
    (ls.take n).flatten = ls.flatten.take (ls.cumLen n)
```

`Cslib.ωSequence.flatten_drop` (theorem, [line 135](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L135))

```lean
theorem flatten_drop [Inhabited α]
    {ls : ωSequence (List α)} (h_ls : ∀ k, 0 < (ls k).length) (n : ℕ) :
    (ls.drop n).flatten = ls.flatten.drop (ls.cumLen n)
```

`Cslib.ωSequence.extract_flatten` (theorem, [line 143](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L143))

> `ls n` is the segment from position `ls.cumLen n` to position `ls.cumLen (n + 1) - 1`
> of `ls.flatten`

```lean
theorem extract_flatten [Inhabited α] {ls : ωSequence (List α)} (h_ls : ∀ k, 0 < (ls k).length)
    (n : ℕ) : ls.flatten.extract (ls.cumLen n) (ls.cumLen (n + 1)) = ls n
```

`Cslib.ωSequence.forall_flatten_iff` (theorem, [line 151](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L151))

> Distributivity of "forall" over `flatten`.

```lean
theorem forall_flatten_iff [Inhabited α] {ls : ωSequence (List α)} (h_ls : ∀ k, 0 < (ls k).length)
    (p : α → Prop) : (∀ n, p (ls.flatten n)) ↔ ∀ k, (ls k).Forall p
```

`Cslib.ωSequence.toSegs` (definition, [line 162](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L162))

> Given an ω-sequence `s` and a function `f : ℕ → ℕ`, `s.toSegs f` is the ω-sequence
> whose `n`-th element is the list `s.extract (f n) (f (n + 1))`.  In all its uses, the
> function `f` will always be assumed to be strictly monotonic with `f 0 = 0`.

```lean
def toSegs (s : ωSequence α) (f : ℕ → ℕ) : ωSequence (List α)
```

`Cslib.ωSequence.toSegs_def` (theorem, [line 165](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L165))

```lean
theorem toSegs_def (s : ωSequence α) (f : ℕ → ℕ) (n : ℕ) :
    s.toSegs f n = s.extract (f n) (f (n + 1))
```

`Cslib.ωSequence.segment_toSegs_cumLen` (theorem, [line 171](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L171))

> `(s.toSegs f).cumLen` is `f` itself.

```lean
theorem segment_toSegs_cumLen {f : ℕ → ℕ}
    (hm : StrictMono f) (h0 : f 0 = 0) (s : ωSequence α) :
    (s.toSegs f).cumLen = f
```

`Cslib.ωSequence.strictMono_flatten` (theorem, [line 180](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean#L180))

> `(s.toSegs f).flatten` is `s` itself.

```lean
theorem strictMono_flatten [Inhabited α] {f : ℕ → ℕ}
    (hm : StrictMono f) (h0 : f 0 = 0) (s : ωSequence α) :
    (s.toSegs f).flatten = s
```

## Depends on

- [Segments defined by a strictly monotonic function on Nat](../nat/segment.md)
- [Definition of `ωSequence` and functions on infinite sequences](defs.md)

## Proof depends on

- [ω-sequences a.k.a. infinite sequences](init.md)

## Sources

- [Cslib/Foundations/Data/OmegaSequence/Flatten.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Flatten.lean)
