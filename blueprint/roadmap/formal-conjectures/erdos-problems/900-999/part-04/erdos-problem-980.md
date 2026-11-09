---
declaration: theorem
origin: cited
lean: Erdos980.erdos_980, Erdos980.erdos_980.variants.erdos_two
statement: formalized
---

# Erdős Problem 980

> *References:*
> - [erdosproblems.com/980](https://www.erdosproblems.com/980)
> - [El67b] Elliott, P. D. T. A., *A problem of Erdős concerning power residue sums*.
>   Acta Arith. 13 (1967/68), 131-149.
> - [Er61e] Erdős, P., *Remarks on number theory. I*. Mat. Lapok (1961), 10-17.
> - [Er65b] Erdős, P., *Some recent advances and current problems in number theory*. Lectures on
>   Modern Mathematics, Vol. III (1965), 196-244.
> - [MaPo11] Martin, G. and Pollack, P., *The average least character nonresidue and further
>   variations on a theme of Erdős*. [arXiv:1112.1175](https://arxiv.org/abs/1112.1175) (2011).

*Quoted from [FormalConjectures/ErdosProblems/980.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/980.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/980](https://www.erdosproblems.com/980).

The file states 2 research or textbook statements: 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos980.erdos_980`

Solved: stated here without proof.

> Let $k\geq 2$ and $n_k(p)$ denote the least $k$th power nonresidue of $p$. Is it true that
>
> $$\sum_{p\lt x} n_k(p)\sim c_k \frac{x}{\log x}$$
>
> for some constant $c_k>0$?
>
> Erdős [Er65b] asked this; it is true, and was proved by Elliott [El67b]. As in [El67b], the sum
> is over the primes $p \equiv 1 \pmod k$ (for each of which a $k$th power nonresidue exists).

```lean
theorem erdos_980 (k : ℕ) (hk : 2 ≤ k) :
    ∃ c > (0 : ℝ), residueSum k ~[atTop] fun x ↦ c * x / Real.log x
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/980.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/980.lean#L71).

## `Erdos980.erdos_980.variants.erdos_two`

Solved: stated here without proof.

> Erdős [Er61e] proved this when $k=2$, with
>
> $$c_2=\sum_{k=1}^\infty \frac{p_k}{2^k},$$
>
> where $p_k$ is the $k$th prime; the sum is over the odd primes $p < x$ [MaPo11, (1.1)].

```lean
theorem erdos_980.variants.erdos_two :
    residueSum 2 ~[atTop]
      fun x ↦ (∑' i : ℕ, (Nat.nth Nat.Prime i : ℝ) / 2 ^ (i + 1)) * x / Real.log x
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/980.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/980.lean#L81).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/980.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/980.lean)
- [erdosproblems.com/980](https://www.erdosproblems.com/980)
