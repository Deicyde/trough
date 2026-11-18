---
catalog: module
lean: Cslib.Circuits.Boolean.Lupanov.bound, Cslib.Circuits.Boolean.Lupanov.synthesis
statement: formalized
proof: formalized
---

# Lupanov's block construction

`Cslib.Computability.Circuit.Boolean.LupanovConstruction`, in [Cslib/Computability/Circuit/Boolean/LupanovConstruction.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/LupanovConstruction.lean), by Samuel Schlesinger.

> This file is the finite, parametrised core of Lupanov's upper bound. Its purpose is to give a
> gate budget `bound k d s` that is valid for every Boolean function on `k + d` inputs and every
> positive block size `s`, and to prove (`synthesis`) that the budget suffices. The asymptotic file
> `Lupanov.lean` then chooses `k`, `d`, and `s` as functions of `n` and shows that the budget is
> `(1 + ε) 2 ^ n / n`. No asymptotics happen here.
>
> ## Why not the disjunctive normal form?
>
> Writing `f` as the disjunction of its true minterms uses up to `2 ^ n` minterms of `n`
> literals each, so roughly `n 2 ^ n` gates. The waste is that nothing is shared between
> minterms. Lupanov's construction shares almost everything.
>
> ## The picture
>
> Split the `n = k + d` inputs into `k` *address* bits and `d` *data* bits, and view the truth
> table of `f` as a `2 ^ k × 2 ^ d` matrix: row `a` is an address assignment, column `b` is a
> data assignment, and the entry is `f (a ++ b)`. Cut the rows into blocks of `s` consecutive
> rows. Inside one block every column is a bit string of length `s`, its *pattern* in that
> block; there are only `2 ^ s` possible patterns, however many columns there are.
>
> For each block `B` and pattern `v` define two functions:
>
> * `left B v`, of the address bits only: true at `a` when row `a` lies in `B` and `v` has a
>   `1` at the position of `a` within `B`;
> * `right f B v`, of the data bits only: true at `b` when column `b` has pattern `v` in `B`.
>
> Both are functions of the full input that ignore the other half of it. Then
> `left B v a ∧ right f B v b` holds exactly when `a` lies in `B`, `v` is the pattern of
> column `b` inside `B`, and the entry `f (a ++ b)` is `true`. So `f` is the disjunction over
> all pairs `(B, v)` of `left B v ∧ right f B v` (`table_eq`).
>
> ## Counting gates
>
> All `2 ^ k` address minterms and `2 ^ d` data minterms are built once and shared. Each
> `left B v` is a disjunction of at most `s` address minterms, so it costs `O(s)` gates, and
> there are `(2 ^ k / s + 1) · 2 ^ s` of them. Each `right f B v` is a disjunction of data
> minterms, one per column with pattern `v`; the columns of a block are partitioned by their
> patterns (`support_card_sum`), so all the `right f B v` of one block together cost about
> `2 ^ d` gates. Summing over blocks, the dominant contribution is
>
>   `(2 ^ k / s) · 2 ^ d = 2 ^ n / s`.
>
> For the parameters chosen in `Lupanov.lean` the remaining terms are of lower order, and
> `s ≈ n` makes this `2 ^ n / n`. The exact expression is `bound`.
>
> ## References
>
> * [O. B. Lupanov, *On a Method of Circuit Synthesis*][Lupanov1958],
>   Section 1, equation (1.1), pp. 120-122: the original `(k, s)` representation.
> * [Stasys Jukna, *Boolean Function Complexity: Advances and Frontiers*][Jukna2012],
>   Theorem 1.15: a modern exposition.
> * [C. E. Shannon, *The Synthesis of Two-Terminal Switching Circuits*][Shannon1949],
>   Section 3(d), pp. 73-77: the earlier universal-network method for relay contacts.

> ### Minterms

> ### The block decomposition
>
> Rows `block * s, …, block * s + s - 1` form block number `block`. The final block may be
> partial, and when `s ∣ 2 ^ k` there is an empty extra block; rows past `2 ^ k` are read as
> `false` throughout.

> ### Gate counts

> ### Correctness

> ### The bound

`Cslib.Circuits.Boolean.Lupanov.bound` (definition, [line 260](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/LupanovConstruction.lean#L260))

> Gate budget for `k` address bits, `d` data bits, and blocks of `s` rows, as spent by
> `synthesis`. In order: the shared minterms; then for each of the `2 ^ k / s + 1` blocks
> (a partial final block, or an empty extra block when `s ∣ 2 ^ k`), `2 s + 4` gates per
> pattern, namely `2 s + 1` for its `left` part, the constant starting its `right` part, the
> conjunction of the two, and the OR into the running disjunction, plus `2 ^ d` gates in total
> for the ORs inside the `right` parts of the block, one per column; and one constant for the
> empty outer disjunction. The leading term is `(2 ^ k / s) · 2 ^ d ≈ 2 ^ n / s`.

```lean
def bound (k d s : ℕ) : ℕ
```

`Cslib.Circuits.Boolean.Lupanov.synthesis` (theorem, [line 267](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/LupanovConstruction.lean#L267))

> Every Boolean function on `k + d` inputs can be built from the input projections within
> `bound k d s` gates: build all minterms, then the disjunction over block-pattern pairs of
> `left ∧ right`, which equals `f` by `table_eq`.

```lean
theorem synthesis (f : BooleanFunction (k + d)) (hs : 0 < s) :
    Synthesis interpretation (inputs (k + d)) {f} (bound k d s)
```

## Depends on

- [Boolean circuits](basic.md)
- [Simultaneous circuit synthesis](../synthesis.md)
- [Fixed-length bit strings and Boolean functions](../../../foundations/data/bitstring.md)

## Proof depends on

- [Boolean synthesis](synthesis.md)

## Sources

- [Cslib/Computability/Circuit/Boolean/LupanovConstruction.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/LupanovConstruction.lean)
