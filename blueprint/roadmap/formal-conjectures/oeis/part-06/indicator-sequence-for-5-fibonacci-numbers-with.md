---
declaration: theorem
origin: cited
lean: OeisA105565.conjecture
statement: formalized
---

# Indicator sequence for 5 Fibonacci numbers with n digits

> $a(n) = 1$ if exactly 5 Fibonacci numbers exist with exactly $n$ digits, otherwise $0$.
> For the partial sums $S(n) = \sum_{k=1}^n a(k)$, it is conjectured that
> $\beta-2 < S(n)-\alpha n < \beta-1$, where $\alpha = \log(10)/\log(\phi) - 4$
> and $\beta = \log(5)/(2\log(\phi)) - 1$.
>
> *References:*
> - [A105565](https://oeis.org/A105565)

*Quoted from [FormalConjectures/OEIS/105565.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/105565.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA105565.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/HaigAd/formal-conjectures/blob/327b99914ce787ab41c67ba645626982e15b0124/FormalConjectures/OEIS/105565.lean#L595](https://github.com/HaigAd/formal-conjectures/blob/327b99914ce787ab41c67ba645626982e15b0124/FormalConjectures/OEIS/105565.lean#L595).

> Conjecture: $\beta-2 < S(n)-\alpha n < \beta-1$.
> The constants $\alpha$ and $\beta$ are as defined in the formula section.
>
> Solved by OpenAI Codex, prompted by Adam Haig. A complete Lean 4 proof is
> linked by the `formal_proof` attribute below.

```lean
theorem conjecture (n : ℕ) (hn : 1 ≤ n) :
    betaConst - 2 < s n - alphaConst * (n : Real) ∧
      s n - alphaConst * (n : Real) < betaConst - 1
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/105565.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/105565.lean#L101).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/105565.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/105565.lean)
- [A105565](https://oeis.org/A105565)
