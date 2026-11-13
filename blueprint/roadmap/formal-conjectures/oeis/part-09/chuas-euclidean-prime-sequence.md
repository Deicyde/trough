---
declaration: theorem
origin: cited
lean: OeisA167604.conjecture
statement: formalized
---

# Chua's Euclidean prime sequence

> For a product $n$ of the preceding terms, Chua's sequence chooses the least
> prime dividing $d + n / d$ for some divisor $d$ of $n$. The open question is
> whether every prime occurs.
>
> *References:*
> - [OEIS A167604](https://oeis.org/A167604)
> - Andrew R. Booker,
>   [A variant of the Euclid--Mullin sequence containing every prime](https://arxiv.org/abs/1605.08929)

*Quoted from [FormalConjectures/OEIS/167604.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/167604.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements, counted here but not shown.

## `OeisA167604.conjecture`

Open: stated without proof.

> Does Chua's sequence contain every prime?

```lean
theorem conjecture :
    ∀ p : ℕ, p.Prime → ∃ n ≥ 1, a n = p
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/167604.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/167604.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/167604.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/167604.lean)
- [OEIS A167604](https://oeis.org/A167604)
