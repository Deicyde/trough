---
declaration: theorem
origin: cited
lean: Gourevitch.gourevitch_series_identity
statement: formalized
---

# Gourevitch's series identity

> *References:*
>  - [About a New Kind of Ramanujan-Type Series](https://doi.org/10.1080/10586458.2003.10504518) by *Jesús Guillera*
>  - [G2003] Guillera, Jesús. "About a new kind of Ramanujan-type series." Experimental Mathematics 12.4 (2003): 507-510.
>  - [A2025] Au, Kam Cheong. "Wilf-Zeilberger seeds and non-trivial hypergeometric identities." Journal of Symbolic Computation 130 (2025): 102421. [arXiv:2312.14051](https://arxiv.org/abs/2312.14051)

*Quoted from [FormalConjectures/Paper/Gourevitch.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Gourevitch.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `Gourevitch.gourevitch_series_identity`

Solved: stated here without proof.

> The Gourevitch series identity:
> The following identity holds:
> $\sum_{n=0}^{\infty} \frac{1 + 14 n + 76 n^2 + 168 n^3}{2^{20 n}} \binom{2n}{n}^7 = \frac{32}{\pi^3}.$
> This was originally conjectured in [G2003] by Guillera and proven in [A2025] by Au.

```lean
theorem gourevitch_series_identity :
    ∑' n : ℕ, ((1 + 14 * n + 76 * n ^ 2 + 168 * n ^ 3) / (2 ^ (20 * n)) : ℝ)
      * Nat.centralBinom n ^ 7 = 32 / (Real.pi ^ 3)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Paper/Gourevitch.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Gourevitch.lean#L40).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/Gourevitch.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Gourevitch.lean)
- [About a New Kind of Ramanujan-Type Series](https://doi.org/10.1080/10586458.2003.10504518)
