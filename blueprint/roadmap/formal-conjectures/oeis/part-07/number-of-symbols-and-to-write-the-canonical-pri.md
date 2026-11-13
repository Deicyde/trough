---
declaration: theorem
origin: cited
lean: OeisA110475.conjecture
statement: formalized
---

# Number of symbols '\*' and '^' to write the canonical prime factorization of n

> The canonical prime factorization is $n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}$.
> The written form is $p_1^{\wedge} e_1 * p_2^{\wedge} e_2 * \cdots * p_k^{\wedge} e_k$,
> where the $\wedge$ appears only if $e_i > 1$.
> $a(n) = (\text{number of distinct prime factors}) - 1 +$
> $(\text{number of distinct prime factors with exponent } > 1)$.
>
> *References:*
> - [A110475](https://oeis.org/A110475)

*Quoted from [FormalConjectures/OEIS/110475.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/110475.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA110475.conjecture`

Open: stated without proof.

> It is conjectured that $1,2,3,4,5,6,7,9,11$ are the only positive integers
> which cannot be represented as the sum of two elements of indices $n$ such that $a(n) = 1$.

```lean
theorem conjecture :
  ∀ m > 0, m ∉ exceptionalSet ↔ ∃ x y : ℕ, a x = 1 ∧ a y = 1 ∧ m = x + y
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/110475.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/110475.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/110475.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/110475.lean)
- [A110475](https://oeis.org/A110475)
