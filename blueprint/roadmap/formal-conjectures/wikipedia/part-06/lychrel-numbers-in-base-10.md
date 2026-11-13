---
declaration: theorem
origin: cited
lean: LychrelNumbers.no_lychrel_numbers_base10, LychrelNumbers.isLychrel10_196
statement: formalized
---

# Lychrel numbers in base 10

> A (base-10) *Lychrel number* is a positive integer which never becomes a palindrome under the
> iteration
>
> $$a_{0} = n, \qquad a_{k+1} = a_k + \operatorname{rev}_{10}(a_k).$$
>
> One commonly stated conjectural direction is that there are no Lychrel numbers in base 10.
> The smallest widely studied open case is `196`.
>
> *References:*
> * [Wikipedia: Lychrel number](https://en.wikipedia.org/wiki/Lychrel_number)
> * [MathWorld: Lychrel Number](https://mathworld.wolfram.com/LychrelNumber.html)
> * [OEIS A023108](https://oeis.org/A023108)
> * [OEIS A023109](https://oeis.org/A023109)

*Quoted from [FormalConjectures/Wikipedia/LychrelNumbers.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LychrelNumbers.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 4 test statements and 1 API statement, counted here but not shown.

## `LychrelNumbers.no_lychrel_numbers_base10`

Open: stated without proof.

> **Lychrel conjecture (base 10):** conjecturally, there are no Lychrel numbers in base 10.
>
> Equivalently, every positive integer eventually becomes a palindrome under the Lychrel iteration.

```lean
theorem no_lychrel_numbers_base10 :
    ∀ n : ℕ, 0 < n → ¬ IsLychrel10 n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/LychrelNumbers.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LychrelNumbers.lean#L74).

## `LychrelNumbers.isLychrel10_196`

Open: stated without proof.

> The first widely studied open case: whether `196` is a base-10 Lychrel number.

```lean
theorem isLychrel10_196 : IsLychrel10 196
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/LychrelNumbers.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LychrelNumbers.lean#L82).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/LychrelNumbers.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LychrelNumbers.lean)
- [Wikipedia: Lychrel number](https://en.wikipedia.org/wiki/Lychrel_number)
