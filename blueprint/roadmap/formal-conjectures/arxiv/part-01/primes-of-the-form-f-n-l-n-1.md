---
declaration: theorem
origin: cited
lean: Arxiv.«2211.10788».infinitely_many_lucas_fibonacci_sum_primes
statement: formalized
---

# Primes of the form $F_n+L_{n+1}$

> The third diagonal of the determinant Hosoya triangle contains the numbers $F_n+L_{n+1}$,
> where $F_n$ and $L_n$ are the Fibonacci and Lucas numbers. Since
> $L_{n+1}=F_n+F_{n+2}$, these numbers are $2F_n+F_{n+2}$. Their prime values begin
> $5,23,37,97,157,1741,\ldots$. These are the terms of OEIS A091157 after its initial $3$,
> which comes from extending the Fibonacci and Lucas indices to $n=-1$.
>
> *References:*
> - H.-Y. Ching, R. Flórez, F. Luca, A. Mukherjee, and J. C. Saunders,
>   [Primes and composites in the determinant Hosoya triangle](https://arxiv.org/abs/2211.10788),
>   introduction and Question 1 of Section 5.
> - [OEIS A091157](https://oeis.org/A091157)

*Quoted from [FormalConjectures/Arxiv/2211.10788/LucasFibonacciSumPrimes.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Arxiv/2211.10788/LucasFibonacciSumPrimes.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 7 test statements and 1 API statement, counted here but not shown.

## `Arxiv.«2211.10788».infinitely_many_lucas_fibonacci_sum_primes`

Open: stated without proof.

> "Are there infinitely many primes of this form?"
> The form in the introduction is $F_n+L_{n+1}$.

```lean
theorem infinitely_many_lucas_fibonacci_sum_primes :
    {p : ℕ | p.Prime ∧ ∃ n, p = lucasFibonacciSum n}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Arxiv/2211.10788/LucasFibonacciSumPrimes.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Arxiv/2211.10788/LucasFibonacciSumPrimes.lean#L89).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2211.10788/LucasFibonacciSumPrimes.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Arxiv/2211.10788/LucasFibonacciSumPrimes.lean)
- [Primes and composites in the determinant Hosoya triangle](https://arxiv.org/abs/2211.10788)
