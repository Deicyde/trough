---
catalog: module
lean: Cslib.Circuits.Boolean.Lupanov.exists_circuit, Cslib.Circuits.Boolean.Lupanov.complexity_le
statement: formalized
proof: formalized
---

# Lupanov's asymptotically optimal upper bound

`Cslib.Computability.Circuit.Boolean.Lupanov`, in [Cslib/Computability/Circuit/Boolean/Lupanov.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Lupanov.lean), by Samuel Schlesinger.

> Every Boolean function on `n` inputs has a De Morgan circuit with at most
> `(1 + ε) * 2 ^ n / n` gates for all sufficiently large `n`, given any `ε > 0`.
> The threshold is uniform in the function; size counts constants and negations.
> This matches Shannon's counting lower bound up to the factor `1 + ε`, which is why the
> bound is called asymptotically optimal.
>
> This file only does the asymptotics. The circuit comes from the block construction in
> `LupanovConstruction.lean`, which gives, for any split of the inputs into `k` address bits
> and `d` data bits and any positive block size `s`, a circuit with at most `bound k d s` gates.
>
> ## Choosing the parameters
>
> Write `l = log₂ n`. We take `k = 3 l` address bits, `d = n - 3 l` data bits, and blocks of
> `s = n - 5 l` rows. Then:
>
> * the leading term of `bound` is `(2 ^ k / s + 1) · 2 ^ d ≈ 2 ^ n / s`, and since
>   `s = n - 5 l` is `n (1 - o(1))`, this is `(1 + o(1)) 2 ^ n / n` (`mainTerm_le`);
> * the minterms cost about `(2 ^ k + 2 ^ d) · 2 n = O(n ^ 4) + O(2 ^ n / n ^ 2)`, using
>   `2 ^ k ≤ n ^ 3`;
> * the `left` parts cost about `(2 ^ k / s) · 2 ^ s · 2 s ≈ 2 ^ (k + s) = 2 ^ (n - 2 l)`,
>   which is `O(2 ^ n / n ^ 2)`.
>
> `bound_le` packages the two error terms as `3 n ^ 4 + 16 n · 2 ^ d`;
> `Nat.eventually_mul_pow_le_pow` and `error_le` show that the polynomial and the exponential
> term are each `o(2 ^ n / n)`. Then `eventually_bound_le` combines everything into
> `P · n · bound ≤ (P + 1) · 2 ^ n` for all large `n`, for any natural number `P`.
> Taking `P > 1 / ε` in `exists_circuit` gives the theorem; `complexity_le` states it as a
> bound on circuit complexity.
>
> ## References
>
> * [O. B. Lupanov, *On a Method of Circuit Synthesis*][Lupanov1958],
>   Theorem 4 and Section 6, pp. 131-135: the upper bound for general weighted bases,
>   specialized here to the De Morgan basis.
> * [Stasys Jukna, *Boolean Function Complexity: Advances and Frontiers*][Jukna2012],
>   Theorem 1.15: a modern exposition.

`Cslib.Circuits.Boolean.Lupanov.exists_circuit` (theorem, [line 208](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Lupanov.lean#L208))

> Lupanov's upper bound: every Boolean function on `n` inputs has a De Morgan circuit
> with at most `(1 + ε) 2ⁿ/n` gates, uniformly for sufficiently large `n`.
>
> Pick a natural number `P > 1 / ε`, so that `(P + 1) / P < 1 + ε`; then the threshold `m`
> comes from `eventually_bound_le P`.

```lean
theorem exists_circuit (ε : ℝ) (hε : 0 < ε) :
    ∃ m : ℕ, ∀ n ≥ m, ∀ f : BooleanFunction n,
      ∃ c : Circuit signature n 1,
        c.Computes interpretation (single f) ∧ (c.size : ℝ) ≤ (1 + ε) * 2 ^ n / n
```

`Cslib.Circuits.Boolean.Lupanov.complexity_le` (theorem, [line 238](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Lupanov.lean#L238))

> Lupanov's upper bound for circuit complexity: every Boolean function on `n` inputs has
> complexity at most `(1 + ε) 2ⁿ/n`, uniformly for sufficiently large `n`.

```lean
theorem complexity_le (ε : ℝ) (hε : 0 < ε) :
    ∃ m : ℕ, ∀ n ≥ m, ∀ f : BooleanFunction n,
      (complexity interpretation (single f) : ℝ) ≤ (1 + ε) * 2 ^ n / n
```

## Depends on

- [Completeness of the De Morgan basis](complexity.md)
- [Fixed-length bit strings and Boolean functions](../../../foundations/data/bitstring.md)

## Proof depends on

- [Asymptotic bounds on natural numbers](../../../foundations/data/nat/asymptotics.md)

## Sources

- [Cslib/Computability/Circuit/Boolean/Lupanov.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Lupanov.lean)
