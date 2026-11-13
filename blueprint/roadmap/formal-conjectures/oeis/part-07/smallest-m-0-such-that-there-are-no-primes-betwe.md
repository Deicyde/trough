---
declaration: theorem
origin: cited
lean: OeisA110835.conjecture
statement: formalized
---

# Smallest $m > 0$ such that there are no primes between $nm$ and $n(m+1)$ inclusive.

> Sierpinski's conjecture (1958) is precisely that a(n) >= n for all n.
>
> *References:*
> - [A110835](https://oeis.org/A110835)

*Quoted from [FormalConjectures/OEIS/110835.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/110835.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 3 test statements, counted here but not shown.

## `OeisA110835.conjecture`

Open: stated without proof.

> Sierpinski's conjecture (1958) is precisely that $a(n) >= n$ for all $n$.

```lean
theorem conjecture : ∀ n > 0, a n ≥ n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/110835.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/110835.lean#L111).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/110835.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/110835.lean)
- [A110835](https://oeis.org/A110835)
