---
declaration: theorem
origin: cited
lean: OeisA67599.conjecture
statement: formalized
---

# Decimal encoding of the prime factorization of $n$

> If $n$ has prime factorization $p_1^{e_1} \dots p_r^{e_r}$ with $p_1 < \dots < p_r$,
> then its decimal encoding is $p_1 e_1 \dots p_r e_r$.
>
> *References:*
> - [A067599](https://oeis.org/A067599)

*Quoted from [FormalConjectures/OEIS/67599.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/67599.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA67599.conjecture`

Open: stated without proof.

> "$a(31) = a(177147) = 311$. Is there any solution to $a(n) = n$?
> - _Franklin T. Adams-Watters_, Dec 18 2006"

```lean
theorem conjecture :
    ∃ n : ℕ, 2 ≤ n ∧ a n = n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/67599.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/67599.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/67599.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/67599.lean)
- [A067599](https://oeis.org/A067599)
