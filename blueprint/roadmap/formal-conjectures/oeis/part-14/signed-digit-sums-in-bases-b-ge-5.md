---
declaration: theorem
origin: cited
lean: OeisA243106.digits_sum_restricted
statement: formalized
---

# Signed digit sums in bases $b \ge 5$

> The sequence is defined by
>
> $$a(n) = \sum_{k=1}^n (-1)^{\operatorname{isprime}(k)} 10^k$$
>
> where the sign is $-1$ if $k$ is prime, and $1$ if $k$ is not prime.
>
> Generalizing the digit pattern observed in $a(n)$, it was conjectured on the OEIS entry that
> for any base $b \ge 5$ and any choice of signs $\pm 1$, the absolute value of $\sum_{k=1}^n \pm b^k$
> only contains digits in $\{0, 1, b-2, b-1\}$.
>
> *References:*
> - [A243106](https://oeis.org/A243106)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/243106.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/243106.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA243106.digits_sum_restricted`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/243106.wip.lean#L140](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/243106.wip.lean#L140).

> Conjecture: When expressed in base $b \ge 5$, the absolute value of any partial sum $\sum \pm b^k$ only contains digits belonging to $\{0, 1, b-2, b-1\}$.
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem digits_sum_restricted (b n : ℕ) (hb : b ≥ 5) :
    ∀ (σ : ℕ → Int) (hσ : ∀ k ∈ Icc 1 n, σ k = 1 ∨ σ k = -1),
      let x : Int := (Icc 1 n).sum fun k ↦ σ k * (b : Int) ^ k;
      ∀ d ∈ (b.digits x.natAbs), d = 0 ∨ d = 1 ∨ d = b - 2 ∨ d = b - 1
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/243106.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/243106.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/243106.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/243106.lean)
- [A243106](https://oeis.org/A243106)
