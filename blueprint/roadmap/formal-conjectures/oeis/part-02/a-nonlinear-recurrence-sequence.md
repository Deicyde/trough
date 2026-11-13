---
declaration: theorem
origin: cited
lean: OeisA22030.conjecture
statement: formalized
---

# A nonlinear recurrence sequence

> For even $n$, $a(n+2)$ is the greatest integer such that $a(n+2)/a(n+1) < a(n+1)/a(n)$;
> for odd $n$, the least integer such that $a(n+2)/a(n+1) > a(n+1)/a(n)$;
> $a(0) = 4, a(1) = 16$.
>
> *References:*
> - [A022030](https://oeis.org/A022030)

*Quoted from [FormalConjectures/OEIS/22030.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/22030.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 6 test statements, counted here but not shown.

## `OeisA22030.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a022030-lean/blob/f74afc2/lean/OeisA22030FC.lean#L270-L275](https://github.com/KitaKen1/oeis-a022030-lean/blob/f74afc2/lean/OeisA22030FC.lean#L270-L275).

> Conjecture: $a(n) = 4 a(n-1) - a(n-3) + a(n-4)$.
> - Colin Barker, Feb 16 2012

```lean
theorem conjecture (n : ℕ) (hn : 4 ≤ n) :
    a n = 4 * a (n - 1) - a (n - 3) + a (n - 4)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/22030.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/22030.lean#L76).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/22030.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/22030.lean)
- [A022030](https://oeis.org/A022030)
