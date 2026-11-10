---
declaration: theorem
origin: cited
lean: Erdos202.erdos_202, Erdos202.erdos_202.variants.erdos_szemeredi
statement: formalized
---

# Erdős Problem 202

> *References:*
> - [erdosproblems.com/202](https://www.erdosproblems.com/202)
> - [BFV13] de la Bretèche, Régis and Ford, Kevin and Vandehey, Joseph, *On non-intersecting
>   arithmetic progressions*. Acta Arith. (2013), 381-392.
> - [Ch05] Chen, Yong-Gao, *On disjoint arithmetic progressions*. Acta Arith. (2005), 143-148.
> - [Cr03b] Croot, III, Ernest S., *On non-intersecting arithmetic progressions*. Acta Arith.
>   (2003), 233-238.
> - [ErSz68] Erdős, P. and Szemerédi, E., *On a problem of P. Erdős and S. Stein*. Acta Arith.
>   (1968), 85-90.
> - [PaPh24] Park, Jinyoung and Pham, Huy Tuan, *A proof of the Kahn-Kalai conjecture*. J. Amer.
>   Math. Soc. (2024), 235-243.

*Quoted from [FormalConjectures/ErdosProblems/202.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/202.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/202](https://www.erdosproblems.com/202).

The file states 2 research or textbook statements: 2 solved.

## `Erdos202.erdos_202`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos202.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos202.lean).

> Let $n_1\lt \cdots < n_r\leq N$ with associated $a_i\pmod{n_i}$ such that the congruence classes are
> disjoint (that is, every integer is $\equiv a_i\pmod{n_i}$ for at most one $1\leq i\leq r$). How
> large can $r$ be in terms of $N$?
>
> Let $f(N)$ be the maximum possible $r$, and let $L(N)=\exp(\sqrt{\log N\log\log N})$.
>
> This was proved by GPT-5.4 Pro (prompted by Ho Boon Suan), using the argument of [BFV13] together
> with the resolution of the Kahn-Kalai conjecture by Park and Pham [PaPh24], so that
>
> $$f(N)= N L(N)^{-1+o(1)}.$$

```lean
theorem erdos_202 : ∃ o : ℕ → ℝ, o =o[atTop] (1 : ℕ → ℝ) ∧
    ∀ᶠ N : ℕ in atTop, (f N : ℝ) = (N : ℝ) * scaleL N ^ (-1 + o N)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/202.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/202.lean#L64).

## `Erdos202.erdos_202.variants.erdos_szemeredi`

Solved: stated here without proof.

> Erdős and Stein conjectured that $f(N)=o(N)$, which was proved by Erdős and Szemerédi [ErSz68].

```lean
theorem erdos_202.variants.erdos_szemeredi :
    (fun N => (f N : ℝ)) =o[atTop] (fun N : ℕ => (N : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/202.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/202.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/202.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/202.lean)
- [erdosproblems.com/202](https://www.erdosproblems.com/202)
