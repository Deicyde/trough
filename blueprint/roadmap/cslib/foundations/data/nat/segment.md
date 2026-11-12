---
catalog: module
lean: Nat.segment, Nat.strictMono_infinite, Nat.infinite_strictMono, Nat.nth_succ_gap, Nat.nth_of_strictMono, Nat.count_notMem_range_pos, Nat.strictMono_range_gap, Nat.segment_idem, Nat.segment_pre_zero, Nat.segment_zero, Nat.segment_plus_one, Nat.segment_upper_bound, Nat.segment_lower_bound, Nat.segment_range_val, Nat.segment_galois_connection, Nat.segment', Nat.base_zero_strictMono, Nat.segment'_eq_segment, Nat.segment_zero', Nat.segment_upper_bound', Nat.segment_lower_bound'
statement: formalized
proof: formalized
---

# Segments defined by a strictly monotonic function on Nat

`Cslib.Foundations.Data.Nat.Segment`, in [Cslib/Foundations/Data/Nat/Segment.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean), by Ching-Tsun Chou.

> Given a strictly monotonic function `f : ℕ → ℕ` and `k : ℕ` with `k ≥ f 0`,
> `Nat.segment f k` is the unique `m : ℕ` such that `f m ≤ k < f (m + 1)`.
> `Nat.segment f k` is defined to be 0 for `k < f 0`.
> This file defines `Nat.segment` and proves various properties about it.

`Nat.segment` (definition, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L28))

> The `f`-segment of `k`, where `f : ℕ → ℕ` will be assumed to be at least StrictMono.

```lean
noncomputable def Nat.segment (f : ℕ → ℕ) (k : ℕ) : ℕ
```

`Nat.strictMono_infinite` (theorem, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L37))

> Any strictly monotonic function `f : ℕ → ℕ` has an infinite range.

```lean
theorem strictMono_infinite (hm : StrictMono f) :
    (range f).Infinite
```

`Nat.infinite_strictMono` (theorem, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L42))

> Any infinite subset of `ℕ` is the range of a strictly monotonic function.

```lean
theorem infinite_strictMono {ns : Set ℕ} (h : ns.Infinite) :
    ∃ f : ℕ → ℕ, StrictMono f ∧ range f = ns
```

`Nat.nth_succ_gap` (theorem, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L48))

> There is a gap between two successive occurrences of a predicate `p : ℕ → Prop`,
> assuming `p` (as a set) is infinite.

```lean
theorem nth_succ_gap {p : ℕ → Prop} (hf : (ofPred p).Infinite) (n : ℕ) :
    ∀ k < nth p (n + 1) - nth p n, 0 < k → ¬ p (k + nth p n)
```

`Nat.nth_of_strictMono` (theorem, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L55))

> For a strictly monotonic function `f : ℕ → ℕ`, `f n` is exactly the n-th
> element of the range of `f`.

```lean
theorem nth_of_strictMono (hm : StrictMono f) (n : ℕ) :
    f n = nth (· ∈ range f) n
```

`Nat.count_notMem_range_pos` (theorem, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L65))

> If `f 0 = 0`, then `0` is below any `n` not in the range of `f`.

```lean
theorem count_notMem_range_pos (h0 : f 0 = 0) (n : ℕ) (hn : n ∉ range f) :
    0 < count (· ∈ range f) n
```

`Nat.strictMono_range_gap` (theorem, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L72))

> For a strictly monotonic function `f : ℕ → ℕ`, no number (strictly) between
> `f m` and ` f (m + 1)` is in the range of `f`.

```lean
theorem strictMono_range_gap (hm : StrictMono f) {m k : ℕ}
    (hl : f m < k) (hu : k < f (m + 1)) : k ∉ range f
```

`Nat.segment_idem` (theorem, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L78))

> For a strictly monotonic function `f : ℕ → ℕ`, the segment of `f k` is `k`.

```lean
theorem segment_idem (hm : StrictMono f) (k : ℕ) :
    segment f (f k) = k
```

`Nat.segment_pre_zero` (theorem, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L87))

> For a strictly monotonic function `f : ℕ → ℕ`, `segment f k = 0` for all `k < f 0`.

```lean
theorem segment_pre_zero (hm : StrictMono f) {k : ℕ} (h : k < f 0) :
    segment f k = 0
```

`Nat.segment_zero` (theorem, [line 99](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L99))

> For a strictly monotonic function `f : ℕ → ℕ` with `f 0 = 0`, `segment f 0 = 0`.

```lean
theorem segment_zero (hm : StrictMono f) (h0 : f 0 = 0) :
    segment f 0 = 0
```

`Nat.segment_plus_one` (theorem, [line 106](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L106))

> A slight restatement of the definition of `segment` which has proven useful.

```lean
theorem segment_plus_one (h0 : f 0 = 0) (k : ℕ) :
    segment f k + 1 = count (· ∈ range f) (k + 1)
```

`Nat.segment_upper_bound` (theorem, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L113))

> For a strictly monotonic function `f : ℕ → ℕ` with `f 0 = 0`,
> `k < f (segment f k + 1)` for all `k : ℕ`.

```lean
theorem segment_upper_bound (hm : StrictMono f) (h0 : f 0 = 0) (k : ℕ) :
    k < f (segment f k + 1)
```

`Nat.segment_lower_bound` (theorem, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L123))

> For a strictly monotonic function `f : ℕ → ℕ` with `f 0 = 0`,
> `f (segment f k) ≤ k` for all `k : ℕ`.

```lean
theorem segment_lower_bound (hm : StrictMono f) (h0 : f 0 = 0) (k : ℕ) :
    f (segment f k) ≤ k
```

`Nat.segment_range_val` (theorem, [line 133](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L133))

> For a strictly monotonic function `f : ℕ → ℕ`, all `k` satisfying `f m ≤ k < f (m + 1)`
> has `segment f k = m`.

```lean
theorem segment_range_val (hm : StrictMono f) {m k : ℕ}
    (hl : f m ≤ k) (hu : k < f (m + 1)) : segment f k = m
```

`Nat.segment_galois_connection` (theorem, [line 148](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L148))

> For a strictly monotonic function `f : ℕ → ℕ` with `f 0 = 0`,
> `f` and `segment f` form a Galois connection.

```lean
theorem segment_galois_connection (hm : StrictMono f) (h0 : f 0 = 0) :
    GaloisConnection f (segment f)
```

`Nat.segment'` (definition, [line 159](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L159))

> `segment'` is a helper function that will be proved to be equal to `segment`.
> It facilitates the proofs of some theorems below.

```lean
noncomputable def segment' (f : ℕ → ℕ) (k : ℕ) : ℕ
```

`Nat.base_zero_strictMono` (theorem, [line 166](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L166))

```lean
theorem base_zero_strictMono (hm : StrictMono f) :
    StrictMono (f · - f 0)
```

`Nat.segment'_eq_segment` (theorem, [line 173](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L173))

> For a strictly monotonic function `f : ℕ → ℕ`,
> `segment' f` and `segment f` are actually equal.

```lean
theorem segment'_eq_segment (hm : StrictMono f) :
    segment' f = segment f
```

`Nat.segment_zero'` (theorem, [line 186](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L186))

> For a strictly monotonic function `f : ℕ → ℕ`, `segment f k = 0` for all `k ≤ f 0`.

```lean
theorem segment_zero' (hm : StrictMono f) {k : ℕ} (h : k ≤ f 0) :
    segment f k = 0
```

`Nat.segment_upper_bound'` (theorem, [line 192](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L192))

> For a strictly monotonic function `f : ℕ → ℕ`, `k < f (segment f k + 1)` for all `k ≥ f 0`.

```lean
theorem segment_upper_bound' (hm : StrictMono f) {k : ℕ} (h : f 0 ≤ k) :
    k < f (segment f k + 1)
```

`Nat.segment_lower_bound'` (theorem, [line 199](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean#L199))

> For a strictly monotonic function `f : ℕ → ℕ`, `f (segment f k) ≤ k` for all `k ≥ f 0`.

```lean
theorem segment_lower_bound' (hm : StrictMono f) {k : ℕ} (h : f 0 ≤ k) :
    f (segment f k) ≤ k
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Data/Nat/Segment.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Segment.lean)
