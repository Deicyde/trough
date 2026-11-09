---
declaration: theorem
origin: cited
lean: OeisA382590.kthPrimeFactor_periodic
statement: formalized
---

# Periodicity of $k$-th prime factors in coupled nonlinear recurrence $a(n)$

> The sequence $a(n)$ is defined by $a(n) = a(n-1)b(n-2) + a(n-2)b(n-1)$
> where $b(n) = a(n-1)b(n-2) - a(n-2)b(n-1)$, with $a(0) = b(0) = b(1) = 1$ and $a(1) = 2$.
>
> *References:*
> - [A382590](https://oeis.org/A382590)
> - [mathoverflow/490330](https://mathoverflow.net/questions/490330): B. Morga, "Peculiar family of
>   recurrence formula where for $n>1$ if you take the $n$-th prime factor of each term, you get an
>   eventually periodic sequence", Mar. 31, 2025.

*Quoted from [FormalConjectures/OEIS/382590.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/382590.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 7 test statements, counted here but not shown.

## `OeisA382590.kthPrimeFactor_periodic`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/LeanOeisProofs/NewFormalization/A382590.lean#L201](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/0a23974e54b90afd1453ef02c27cf8f617bad940/LeanOeisProofs/NewFormalization/A382590.lean#L201).

> Conjecture: For any $k > 1$, if you take the $k$-th prime factor of each term, you get an
> eventually periodic sequence. - _Bryle Morga_, Mar 31 2025
>
> Here the $k$-th prime factor of $a(n)$ is the $k$-th smallest distinct prime divisor of
> $|a(n)|$; for example the second prime factors of $a(5) = 18$, $a(6) = 20$ and $a(7) = 896$
> are $3$, $5$ and $7$.
>
> This was proved by Terence Tao in a [MathOverflow answer](https://mathoverflow.net/a/490348),
> using that $a(n)$ divides $a(n+3)$ for all $n$.
> Lean formalization by Wentao Li, with AI assistance.

```lean
theorem kthPrimeFactor_periodic : ∀ k : ℕ, k ≥ 2 → ∃ N₀ p : ℕ, p > 0 ∧
    ∀ n : ℕ, n ≥ N₀ → kthPrimeFactor k (a (n + p)) = kthPrimeFactor k (a n)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/382590.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/382590.lean#L114).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/382590.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/382590.lean)
- [A382590](https://oeis.org/A382590)
