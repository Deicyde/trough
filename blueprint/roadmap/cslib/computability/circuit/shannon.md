---
catalog: module
lean: Cslib.Circuits.Shannon.exists_hard_function
statement: formalized
proof: formalized
---

# Shannon's lower bound for finite carriers and binary bases

`Cslib.Computability.Circuit.Shannon`, in [Cslib/Computability/Circuit/Shannon.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Shannon.lean), by Samuel Schlesinger.

> For any fixed finite signature with operation arities at most two, interpreted on a finite
> carrier `U` with `q ≥ 2` elements, some function on `n` inputs requires more than `qⁿ/n` gates
> for all sufficiently large `n`. The threshold may depend on the signature and carrier.
> For the De Morgan basis on `Bool`, this matches Lupanov's upper bound asymptotically.
>
> The logarithm of the counting bound is at most `s log s + O(s)` for `n + 1 ≤ s`.
> At `s = ⌊qⁿ/n⌋`, this is smaller than the logarithm of the `q^(qⁿ)` functions.
> This extends the Boolean counting argument in the references to finite carriers.
>
> ## References
>
> * [Claude E. Shannon, *The Synthesis of Two-Terminal Switching Circuits*][Shannon1949]:
>   Theorem 7, Section 3(e), pp. 77-79, the original counting argument for switching circuits.
> * [Stasys Jukna, *Boolean Function Complexity: Advances and Frontiers*][Jukna2012]:
>   Lemma 1.12 and Theorem 1.14, a modern treatment of Boolean circuit counting.

`Cslib.Circuits.Shannon.exists_hard_function` (theorem, [line 128](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Shannon.lean#L128))

> For all sufficiently large `n`, some function on `n` inputs over `U` requires more than
> `|U|ⁿ/n` gates over the fixed finite signature, whose operations have arity at most two.

```lean
theorem exists_hard_function [Finite σ.Op] [Finite U] [Nontrivial U]
    (I : Interpretation σ U) (arity_le : ∀ op, σ.Arity op ≤ 2) :
    ∃ N : ℕ, ∀ n ≥ N, ∃ f : (Fin n → U) → U,
      ∀ c : Circuit σ n 1,
        c.Computes I (single f) → (Nat.card U : ℝ) ^ n / n < (c.size : ℝ)
```

## Depends on

- [Counting functions computed by finite circuits](counting.md)

## Proof depends on

- [Asymptotic bounds on natural numbers](../../foundations/data/nat/asymptotics.md)
- [A logarithmic lower bound for the factorial](../../foundations/data/nat/factorial.md)

## Sources

- [Cslib/Computability/Circuit/Shannon.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Shannon.lean)
