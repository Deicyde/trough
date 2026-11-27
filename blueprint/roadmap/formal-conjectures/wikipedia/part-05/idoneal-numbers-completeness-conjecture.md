---
declaration: theorem
origin: cited
lean: Idoneal.idoneal_numbers_completeness
statement: formalized
---

# Idoneal numbers completeness conjecture

> An integer $D>0$ is **idoneal** if every
> integer that can be expressed in exactly one way (up to order and signs)
> as $x^2 + D y^2$ with gcd(x, Dy)=1 is a prime power or twice a prime power.
>
> The Idoneal Numbers Completeness Conjecture asserts that the following list of
> 65 numbers is complete:
> 1,2,3,4,5,6,7,8,9,10,12,13,15,16,18,21,22,24,25,28,30,33,37,40,42,45,48,
> 57,58,60,70,72,78,85,88,93,102,105,112,120,130,133,165,168,177,190,210,232,
> 240,253,273,280,312,330,345,357,385,408,462,520,760,840,1320,1365,1848.
> *References:*
> - [Wikipedia: Idoneal number](https://en.wikipedia.org/wiki/Idoneal_number)
> - [OEIS A000926](https://oeis.org/A000926)
> - [We73] Weinberger, P. J., *Exponents of the class groups of complex quadratic fields*.
>   Acta Arith. 22 (1973), 117–124.
> - [Ka11] Kani, E., *Idoneal numbers and some generalizations*. Ann. Sci. Math. Québec 35 (2011),
>   197–227.
> - [MJ15] Mosunov, A. S. and Jacobson, M. J., Jr., *Unconditional class group tabulation of imaginary
>   quadratic fields to $|\Delta| < 2^{40}$*. [arXiv:1502.07953](https://arxiv.org/abs/1502.07953)
>   (2015).
> - [Al26] Alpöge, L., [Note on the Riemann Hypothesis](https://alpo.ge/remark.pdf) (2026).

*Quoted from [FormalConjectures/Wikipedia/IdonealCompleteness.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/IdonealCompleteness.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 1 test statement, counted here but not shown.

## `Idoneal.idoneal_numbers_completeness`

Solved: stated here without proof.

> Idoneal numbers completeness conjecture.
>
> This follows from the Generalized Riemann Hypothesis for Dirichlet $L$-functions, which is proved
> [Al26]. Under this hypothesis, Weinberger [We73, Theorem 1] proved that the class group of
> $\mathbb{Q}(\sqrt{-d})$ does not have exponent $2$ if its discriminant $-d$ satisfies $d > 5460$.
> Completeness of the list is deduced from this in [Ka11, Corollary 23]. Weinberger's proof uses a
> computation of Lehmer, without details, for $d < 200560490130$. The unconditional tabulation for
> $d < 2^{40}$ in [MJ15] covers this range.

```lean
theorem idoneal_numbers_completeness :
    ∀ n : ℕ, IsIdoneal n → n ∈ knownIdonealNumbers
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/IdonealCompleteness.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/IdonealCompleteness.lean#L117).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/IdonealCompleteness.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/IdonealCompleteness.lean)
- [Wikipedia: Idoneal number](https://en.wikipedia.org/wiki/Idoneal_number)
