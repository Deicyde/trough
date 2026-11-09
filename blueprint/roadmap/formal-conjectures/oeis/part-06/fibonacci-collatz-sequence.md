---
declaration: theorem
origin: cited
lean: OeisA105801.conjecture
statement: formalized
---

# Fibonacci-Collatz sequence

> Fibonacci-Collatz sequence: $a(1)=1, a(2)=2$; for $n > 2$, let $\mathrm{fib} = a(n-1) + a(n-2)$;
> if $\mathrm{fib}$ is odd then $a(n) = 3 \cdot \mathrm{fib} + 1$ else $a(n) = \mathrm{fib}/2$.
>
> *References:*
> - [A105801](https://oeis.org/A105801)

*Quoted from [FormalConjectures/OEIS/105801.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/105801.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA105801.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a105801-lean/blob/68642a80db062bee7061437b60d31c3e7d626595/lean/OeisA105801FC.lean#L323-L351](https://github.com/KitaKen1/oeis-a105801-lean/blob/68642a80db062bee7061437b60d31c3e7d626595/lean/OeisA105801FC.lean#L323-L351).

> Conjecture: for every $k > 0$ there is an index $m$ such that all the $a(n)$ with $n > m$
> have the same residue $\bmod 3^k$.

```lean
theorem conjecture :
    ∀ k : ℕ, 0 < k → ∃ m : ℕ, ∀ n : ℕ, m < n → a n ≡ a (m + 1) [MOD (3^k)]
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/105801.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/105801.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/105801.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/105801.lean)
- [A105801](https://oeis.org/A105801)
