---
declaration: theorem
origin: cited
lean: FusibleNumber.conj_7_1
statement: formalized
---

# Main conjecture on fusible numbers

> *References:*
> - [Fusible numbers and Peano Arithmetic](https://arxiv.org/abs/2003.14342),
>   by Jeff Erickson, Gabriel Nivasch, and Junyan Xu.
> - [Fusible numbers and Peano Arithmetic](https://doi.org/10.46298/lmcs-18%283%3A6%292022),
>   Logical Methods in Computer Science, Volume 18, Issue 3 (July 28, 2022).

*Quoted from [FormalConjectures/Paper/FusibleNumber.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/FusibleNumber.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 2 test statements, counted here but not shown.

## `FusibleNumber.conj_7_1`

Open: stated without proof.

> If `x` is a fusible number and `y` is its successor, then the interval `[x + 1, y + 1)` can be
> divided into intervals `[ℓₙ, ℓₙ₊₁)`, such that the fusible numbers in `[ℓₙ, ℓₙ₊₁)` are obtained by
> fusing the `n + 1`st successor of `x` with a fusible number.
> This formalization differs from Conjecture 7.1 in the paper in four ways:
> (1) it is obtained from Conjecture 7.1 by plugging in `n + 1` into `n`, which simplifies the expressions
>   and removes the need to assume `n ≥ 1`;
> (2) the `n + 1`st successor `s^(n+1)(x)` is replaced by the explicit value `x + (2 - 1 / 2 ^ n) * m`;
> (3) instead of defining `y` to be the successor of `x`, we assert that there is no fusible number
>   strictly between `x` and `y`;
> (4) instead of using `∃ z, IsFusible z ∧ q = s^(n+1)(x) ~ z` we use the value of `z` determined by the equality,
>   namely `z = 2 * q - 1 - s^(n+1)(x)`, and it is easy to see `z ∈ [x + 1 - m / 2 ^ n, x + 1)` as required.

```lean
theorem conj_7_1 (x y q : ℚ) (n : ℕ) (fus_x : IsFusible x) (fus_y : IsFusible y) (lt : x < y)
    (nmem_Ioo : ∀ z, IsFusible z → z ∉ Set.Ioo x y) :
    let m := y - x
    let ℓ (n : ℕ) := y + 1 - m / 2 ^ n
    IsFusible q → q ∈ Set.Ico (ℓ n) (ℓ (n + 1)) → IsFusible (2 * q - 1 - x - (2 - 1 / 2 ^ n) * m)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/FusibleNumber.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/FusibleNumber.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/FusibleNumber.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/FusibleNumber.lean)
- [Fusible numbers and Peano Arithmetic](https://arxiv.org/abs/2003.14342)
