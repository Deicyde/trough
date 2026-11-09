---
declaration: theorem
origin: cited
lean: Erdos726.erdos_726, Erdos726.erdos_726.variants.mertens_estimate
statement: formalized
---

# Erdős Problem 726

> *References:*
> - [erdosproblems.com/726](https://www.erdosproblems.com/726)
> - [EGRS75] Erdős, P., and Graham, R. L. and Ruzsa, I. Z. and Straus, E. G., On the prime factors of
>   $(\sp{2n}\sb{n})$. Math. Comp. (1975), 83-92.

*Quoted from [FormalConjectures/ErdosProblems/726.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/726.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/726](https://www.erdosproblems.com/726).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos726.erdos_726`

Open: stated without proof.

> As $n\to \infty$ ranges over integers
> $\sum_{p\leq n}1_{n\in (p/2,p)\pmod{p}}\frac{1}{p}\sim \frac{\log\log n}{2}$?
>
> A conjecture of Erdős, Graham, Ruzsa, and Straus [EGRS75].
>
> By $n\in (p/2,p)\pmod{p}$ we mean $n\equiv r\pmod{p}$ for some integer $r$ with $p/2\lt r\lt p$.
> The remainder `n % p` is computed in `ℕ` before casting to `ℝ`.

```lean
theorem erdos_726 :
    (fun n : ℕ ↦ ∑ p ∈ (range (n + 1)).filter
        (fun p : ℕ ↦ p.Prime ∧ (p : ℝ) / 2 < ((n % p : ℕ) : ℝ)),
      (1 : ℝ) / (p : ℝ))
    ~[atTop] (fun n : ℕ ↦ Real.log (Real.log (n : ℝ)) / 2)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/726.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/726.lean#L46).

## `Erdos726.erdos_726.variants.mertens_estimate`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/74888affffcf320d798f78a2fb45d13c86704d89/erdos-726/Solution.lean#L36](https://github.com/linrock/math-proofs/blob/74888affffcf320d798f78a2fb45d13c86704d89/erdos-726/Solution.lean#L36).

> The classical estimate of Mertens states that $\sum_{p\leq n}\frac{1}{p}\sim \log\log n$.

```lean
theorem erdos_726.variants.mertens_estimate :
    (fun n : ℕ ↦ ∑ p ∈ (range (n + 1)).filter (fun p ↦ p.Prime), (1 : ℝ) / ((p : ℕ) : ℝ))
    ~[atTop] (fun n : ℕ ↦ Real.log (Real.log (n : ℝ)))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/726.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/726.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/726.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/726.lean)
- [erdosproblems.com/726](https://www.erdosproblems.com/726)
