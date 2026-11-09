---
declaration: theorem
origin: cited
lean: OeisA358684.oeis_358684_conjecture_0
statement: formalized
proof: formalized
---

# Factor bounds for Fermat numbers

> $a(n)$ is the minimum integer $k$ such that the smallest prime factor of the
> $n$-th Fermat number exceeds $2^{2^n - k}$.
>
> *References:*
> - [A358684](https://oeis.org/A358684)
> - [SA22](https://doi.org/10.26493/2590-9770.1473.ec5) Lorenzo Sauras-Altuzarra, *Some properties of the factors of Fermat numbers*, Art Discrete Appl. Math. (2022).

*Quoted from [FormalConjectures/OEIS/358684.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/358684.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 8 test statements and 1 API statement, counted here but not shown.

## `OeisA358684.oeis_358684_conjecture_0`

Proved here.

> Conjecture: the dyadic valuation of A93179(n) - 1 does not exceed 2^n - a(n).
>
> A93179(n) is minFac(fermatNumber n), the smallest prime factor of the n-th Fermat number.
> The conjecture states that if $P_n$ is the smallest prime factor of the $n$-th Fermat number,
> then $\nu_2(P_n - 1) \le 2^n - a(n)$.
> Substituting the definition of $a(n)$, this is equivalent to $\nu_2(P_n - 1) \le \lfloor \log_2(P_n) \rfloor$.
>
> This is Conjecture 3.4 in [SA22].

```lean
theorem oeis_358684_conjecture_0 (n : ℕ) :
    padicValNat 2 (minFac (fermatNumber n) - 1) ≤ 2 ^ n - a n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/358684.lean, line 152](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/358684.lean#L152).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/358684.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/358684.lean)
- [A358684](https://oeis.org/A358684)
