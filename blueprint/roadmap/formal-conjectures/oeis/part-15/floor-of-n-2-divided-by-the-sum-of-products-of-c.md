---
declaration: theorem
origin: cited
lean: OeisA251758.conjecture
statement: formalized
---

# Floor of $n^2$ divided by the sum of products of consecutive divisors of $n$

> Let $n \ge 2$ be a positive integer with divisors $1 = d_1 < d_2 < \dots < d_k = n$, and let
> $s = d_1 d_2 + d_2 d_3 + \dots + d_{k-1} d_k$. The sequence $a(n)$ lists the values
> $\lfloor n^2 / s \rfloor$.
>
> *References:*
> - [A251758](https://oeis.org/A251758)

*Quoted from [FormalConjectures/OEIS/251758.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/251758.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA251758.conjecture`

Open: stated without proof.

> Let $p\#_i$ denote the $i$-th primorial (`Nat.kthPrimorial i`). For $n = 8$, the primorial ratios
> $x = p\#_{12}/p\#_4, p\#_{13}/p\#_4, p\#_{14}/p\#_4, p\#_{15}/p\#_4, p\#_{16}/p\#_4, \dots$
> satisfy $a(x) = 8$. Is $p\#_{12}/p\#_4 = 35336848261$ the least $x \ge 2$ such that $a(x) = 8$?
>
> "For $n=8$, $x = p\#12/p\#4, p\#13/p\#4, p\#14/p\#4, p\#15/p\#4, p\#16/p\#4$, etc.
> But is $p\#12/p\#4$ the least such $x$?"
> - _Robert G. Wilson v_, Dec 18 2014

```lean
theorem conjecture :
    IsLeast {x : ℕ | 2 ≤ x ∧ a x = 8}
      (Nat.kthPrimorial 12 / Nat.kthPrimorial (Nat.primeCounting' 8))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/251758.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/251758.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/251758.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/251758.lean)
- [A251758](https://oeis.org/A251758)
