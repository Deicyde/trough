---
declaration: theorem
origin: cited
lean: Erdos461.erdos_461
statement: formalized
---

# Erdős Problem 461

> *References:*
> - [erdosproblems.com/461](https://www.erdosproblems.com/461)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).

*Quoted from [FormalConjectures/ErdosProblems/461.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/461.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/461](https://www.erdosproblems.com/461).

The file states 1 research or textbook statement: 1 open. It also has 3 test statements and 1 API statement, counted here but not shown.

## `Erdos461.erdos_461`

Open: stated without proof.

> Let $s_t(n)$ be the $t$-smooth component of $n$ - that is, the product of all primes $p$ (with
> multiplicity) dividing $n$ such that $p\lt t$. Let $f(n,t)$ count the number of distinct possible
> values for $s_t(m)$ for $m\in [n+1,n+t]$. Is it true that
> $$f(n,t)\gg t$$
> (uniformly, for all $t$ and $n$)?
>
> Erdős and Graham report they can show
> $$f(n,t) \gg \frac{t}{\log t}.$$

```lean
theorem erdos_461 :
    ∃ c : ℝ, 0 < c ∧ ∀ n t : ℕ, c * (t : ℝ) ≤ (f n t : ℝ)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/461.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/461.lean#L53).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/461.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/461.lean)
- [erdosproblems.com/461](https://www.erdosproblems.com/461)
