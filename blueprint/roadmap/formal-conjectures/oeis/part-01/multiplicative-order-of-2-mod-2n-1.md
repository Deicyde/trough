---
declaration: theorem
origin: cited
lean: OeisA2326.conjecture1, OeisA2326.conjecture2
statement: formalized
---

# Multiplicative order of 2 mod $2n+1$

> The multiplicative order of 2 modulo $2n+1$.
> In other words, the least $m > 0$ such that $2n+1$ divides $2^m - 1$.
>
> *References:*
> - [A002326](https://oeis.org/A002326)

*Quoted from [FormalConjectures/OEIS/2326.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/2326.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA2326.conjecture1`

Open: stated without proof.

> If $p$ is an odd prime then $a((p^3-1)/2) = p \cdot a((p^2-1)/2)$.
> Because otherwise $a((p^3-1)/2) < p \cdot a((p^2-1)/2)$ iff $a((p^3-1)/2) = a((p-1)/2)$
> for a prime $p$. Equivalently $p^3$ divides $2^{p-1}-1$, but no such prime $p$ is known.
> - Thomas Ordowski, Feb 10 2014

```lean
theorem conjecture1 (p : ℕ) (hp : p.Prime) (hp_odd : p ≠ 2) :
    a ((p ^ 3 - 1) / 2) = p * a ((p ^ 2 - 1) / 2)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/2326.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/2326.lean#L78).

## `OeisA2326.conjecture2`

Open: stated without proof.

> A generalization of the previous conjecture: For each $k \ge 2$, if $p$ is an odd prime
> then $a((p^{k+1}-1)/2) = p \cdot a((p^k-1)/2)$.
> Computer testing of this generalized conjecture shows that there is no counterexample for $k$
> and $p$ both up to 1000.
> - [Ahmad J. Masad](https://oeis.org/wiki/User:Ahmad_J._Masad), Oct 17 2020
>
> The two are in fact equivalent. Its $k = 2$ instance is `conjecture1`. Conversely, write
> $d = \operatorname{ord}_{p^2}(2)$. `conjecture1` for $p$ says
> $v_p(2^d - 1) = 2$, and lifting the exponent for the odd prime $p$ then gives
> $v_p(2^{d p^t} - 1) = 2 + t$, hence $\operatorname{ord}_{p^{2+t}}(2) = d p^t$ for every
> $t \ge 0$, which is every instance for that $p$.

```lean
theorem conjecture2 (k : ℕ) (hk : 2 ≤ k) (p : ℕ) (hp : p.Prime) (hp_odd : p ≠ 2) :
    a ((p ^ (k + 1) - 1) / 2) = p * a ((p ^ k - 1) / 2)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/2326.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/2326.lean#L96).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/2326.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/2326.lean)
- [A002326](https://oeis.org/A002326)
