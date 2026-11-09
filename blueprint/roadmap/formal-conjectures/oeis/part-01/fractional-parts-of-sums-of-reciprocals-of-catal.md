---
declaration: theorem
origin: cited
lean: OeisA108.catalanReciprocalSum_fracPart_inj
statement: formalized
---

# Fractional parts of sums of reciprocals of Catalan numbers $C(n)$

> Catalan numbers $C(n) = \frac{1}{n+1}\binom{2n}{n}$.
>
> The sum $\sum_{i=j}^k \frac{1}{a(i)}$ of reciprocals of Catalan numbers.
>
> *References:*
> - [A000108](https://oeis.org/A000108)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/108.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/108.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA108.catalanReciprocalSum_fracPart_inj`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/108.wip.lean#L255](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/108.wip.lean#L255).

> Conjecture: All the rational numbers $\sum_{i=j}^k \frac{1}{a(i)}$ with
> $0 < \min\{2,k\} \le j \le k$ have pairwise distinct fractional parts.
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem catalanReciprocalSum_fracPart_inj : ∀ ⦃j₁ k₁ j₂ k₂ : ℕ⦄,
    IndexCond j₁ k₁ → IndexCond j₂ k₂ →
    (j₁, k₁) ≠ (j₂, k₂) →
    fracPart (catalanReciprocalSum j₁ k₁) ≠ fracPart (catalanReciprocalSum j₂ k₂)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/108.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/108.lean#L87).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/108.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/108.lean)
- [A000108](https://oeis.org/A000108)
