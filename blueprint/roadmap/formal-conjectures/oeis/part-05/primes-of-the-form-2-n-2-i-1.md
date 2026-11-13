---
declaration: theorem
origin: cited
lean: OeisA81091.conjectureA81091
statement: formalized
---

# Primes of the form 2^n + 2^i + 1

> There are infinite primes of the form $2^n + 2^i + 1$, with $0 < i < n$.
> See Wagstaff (2001) where this conjecture is posed.
>
> *References:*
> - [A81091](https://oeis.org/A81091)
> - Samuel S. Wagstaff, Jr., [Prime Numbers with a fixed number of one bits or zero bits in their binary representation](http://projecteuclid.org/euclid.em/999188636), Exp. Math. vol. 10, issue 2 (2001) 267.

*Quoted from [FormalConjectures/OEIS/81091.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/81091.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA81091.conjectureA81091`

Open: stated without proof.

> **Conjecture (A81091)**: There are infinite primes of the form $2^n + 2^i + 1$,
> with $0 < i < n$.

```lean
theorem conjectureA81091 :
    Set.Infinite {p : ℕ | A p}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/81091.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/81091.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/81091.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/81091.lean)
- [A81091](https://oeis.org/A81091)
