---
catalog: module
lean: Cslib.Circuits.Shannon.exists_hard_function_of_card_lt, Cslib.Circuits.Shannon.exists_hard_full_function, Cslib.Circuits.Shannon.tendsto_card_computableFunctions_div, Cslib.Circuits.Shannon.exists_hard_function
statement: formalized
proof: formalized
---

# Shannon's lower bounds for finite carriers

`Cslib.Computability.Circuit.Shannon`, in [Cslib/Computability/Circuit/Shannon.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Circuit/Shannon.lean), by Samuel Schlesinger.

> `exists_hard_full_function` gives a finite criterion for the full basis with every parameter
> explicit, including the arity. The following asymptotic theorem specializes to binary bases.
>
> For any fixed finite signature with operation arities at most two, interpreted on a finite
> carrier `U` with `q ≥ 2` elements, almost all functions on `n` inputs require more than `qⁿ/n`
> gates: the fraction of functions computable within that budget tends to zero. Hence, for all
> sufficiently large `n`, some function requires more than `qⁿ/n` gates. This also holds when the
> signature has infinitely many operations, because the binary full basis simulates every
> signature of arity at most two gate by gate, so its hard functions are hard for all of them.
> For the De Morgan basis on `Bool`, this matches Lupanov's upper bound asymptotically.
>
> The logarithm of the counting bound is at most `s log s + O(s)` for `n + 1 ≤ s`.
> At `s = ⌊qⁿ/n⌋`, this is smaller than the logarithm of the `q^(qⁿ)` functions by at least `s`.
> This extends the Boolean counting argument in the references to finite carriers.
>
> ## References
>
> * [Claude E. Shannon, *The Synthesis of Two-Terminal Switching Circuits*][Shannon1949]:
>   Theorem 7, Section 3(e), pp. 77-79, the original counting argument for switching circuits.
> * [Stasys Jukna, *Boolean Function Complexity: Advances and Frontiers*][Jukna2012]:
>   Lemma 1.12 and Theorem 1.14, a modern treatment of Boolean circuit counting.

`Cslib.Circuits.Shannon.exists_hard_function_of_card_lt` (theorem, [line 57](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Circuit/Shannon.lean#L57))

> A finite counting bound yields a hard function without asymptotic assumptions.

```lean
theorem exists_hard_function_of_card_lt [Finite σ.Op] [Finite U]
    (I : Interpretation σ U) (n s : ℕ)
    (h : (computableFunctions I n s).ncard < card U ^ (card U ^ n)) :
    ∃ f : (Fin n → U) → U, ∀ c : Circuit σ n 1, c.Computes I (single f) → s < c.size
```

`Cslib.Circuits.Shannon.exists_hard_full_function` (theorem, [line 67](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Circuit/Shannon.lean#L67))

> A finite Shannon criterion for the full basis, valid simultaneously for every arity,
> input count, and gate budget. The factorial correction accounts for gate relabelings.

```lean
theorem exists_hard_full_function [Finite U] (k n s : ℕ)
    (h : (s + 1) * fullBasisLineBound (card U) k n s ^ s * (n + s) <
        card U ^ (card U ^ n) * s.factorial) :
    ∃ f : (Fin n → U) → U, ∀ c : Circuit (fullSignature k U) n 1,
      c.Computes fullInterpretation (single f) → s < c.size
```

`Cslib.Circuits.Shannon.tendsto_card_computableFunctions_div` (theorem, [line 157](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Circuit/Shannon.lean#L157))

> Almost all functions on `n` inputs require more than `|U|ⁿ/n` gates over a fixed finite
> signature whose operations have arity at most two: the fraction of functions computable within
> that budget tends to zero.

```lean
theorem tendsto_card_computableFunctions_div [Finite σ.Op] [Finite U] [Nontrivial U]
    (I : Interpretation σ U) (arity_le : ∀ op, σ.Arity op ≤ 2) :
    Tendsto (fun n : ℕ => ((computableFunctions I n (card U ^ n / n)).ncard : ℝ) /
      (card U : ℝ) ^ (card U ^ n)) atTop (𝓝 0)
```

`Cslib.Circuits.Shannon.exists_hard_function` (theorem, [line 174](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Circuit/Shannon.lean#L174))

> For all sufficiently large `n`, some function on `n` inputs over `U` requires more than
> `|U|ⁿ/n` gates over a signature whose operations have arity at most two, which may have
> infinitely many operations. The function is hard for the binary full basis, which simulates
> the signature gate by gate.

```lean
theorem exists_hard_function [Finite U] [Nontrivial U]
    (I : Interpretation σ U) (arity_le : ∀ op, σ.Arity op ≤ 2) :
    ∃ N : ℕ, ∀ n ≥ N, ∃ f : (Fin n → U) → U,
      ∀ c : Circuit σ n 1,
        c.Computes I (single f) → (card U : ℝ) ^ n / n < (c.size : ℝ)
```

## Depends on

- [Counting functions computed by finite circuits](counting.md)

## Proof depends on

- [Circuits over the full basis](full.md)
- [Asymptotic bounds on natural numbers](../../foundations/data/nat/asymptotics.md)
- [A logarithmic lower bound for the factorial](../../foundations/data/nat/factorial.md)

## Sources

- [Cslib/Computability/Circuit/Shannon.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Circuit/Shannon.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Computability.Circuit.Shannon.json)
