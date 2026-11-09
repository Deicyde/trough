---
declaration: theorem
origin: cited
lean: OeisA2454.conjecture
statement: formalized
---

# Central factorial numbers: $((2n)!!)^2$

> Central factorial numbers: $a(n) = 4^n (n!)^2 = ((2n)!!)^2$.
>
> *References:*
> - [A002454](https://oeis.org/A002454)
> - [SSX22] [She, Y.-F., Sun, Z.-W., Xia, W., *A novel permanent identity with applications*,
>   arXiv:2208.12167 (2022)](https://arxiv.org/abs/2208.12167)

*Quoted from [FormalConjectures/OEIS/2454.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/2454.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA2454.conjecture`

Solved: stated here without proof.

> Let $\zeta$ be a primitive $(2n+1)$-th root of unity. Then the permanent of the
> $2n \times 2n$ matrix $[m(j,k)]_{j,k=1..2n}$ is $a(n)/(2n+1) = ((2n)!!)^2/(2n+1)$,
> where $m(j,k)$ is $1$ or $(1+\zeta^{j-k})/(1-\zeta^{j-k})$ according as $j = k$ or not.
> - Zhi-Wei Sun, Jun 26 2022
>
> Proved by [SSX22], Theorem 1.3(ii): for odd $m > 1$ and $\zeta$ a primitive $m$-th root of
> unity, the permanent of $[c_{j,k}]_{1 \le j,k \le m-1}$ is $((m-1)!!)^2/m$. Take $m = 2n+1$;
> translating both matrix indices by one leaves $j - k$ unchanged. For $n = 0$ the matrix is
> empty and both sides are $1$.

```lean
theorem conjecture (n : ℕ) :
    let N : ℕ := 2 * n
    let K : ℕ := N + 1
    ∀ (ζ : ℂ), IsPrimitiveRoot ζ K →
      Matrix.permanent (fun (j k : Fin N) =>
        if j = k then
          (1 : ℂ)
        else
          let pow : ℤ := (j : ℤ) - (k : ℤ)
          (1 + ζ ^ pow) / (1 - ζ ^ pow)
      ) = (a n : ℂ) / (K : ℂ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/OEIS/2454.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/2454.lean#L69).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/2454.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/2454.lean)
- [A002454](https://oeis.org/A002454)
