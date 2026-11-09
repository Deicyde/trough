---
declaration: theorem
origin: cited
lean: Erdos933.erdos_933, Erdos933.erdos_933.variants.mahler, Erdos933.erdos_933.variants.lower_bound
statement: formalized
---

# Erdős Problem 933

> *References:*
> - [erdosproblems.com/933](https://www.erdosproblems.com/933)
> - [Er76d] Erdős, P, Problems and results on number theoretic properties of consecutive integers and
>   related questions. Proceedings of the Fifth Manitoba Conference on Numerical Mathematics (Univ.
>   Manitoba, Winnipeg, Man., 1975) (1976), 25-44.

*Quoted from [FormalConjectures/ErdosProblems/933.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/933.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/933](https://www.erdosproblems.com/933).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos933.erdos_933`

Open: stated without proof.

> If $n(n+1)=2^k3^lm$, where $(m,6)=1$, then is it true that
> $\limsup_{n\to \infty} \frac{2^k3^l}{n\log n}=\infty$?

```lean
theorem erdos_933 :
    atTop.limsup (fun n : ℕ ↦
      ((((2 ^ k n * 3 ^ l n : ℕ) : ℝ) / ((n : ℝ) * Real.log (n : ℝ))) : EReal)) = ⊤
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/933.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/933.lean#L47).

## `Erdos933.erdos_933.variants.mahler`

Solved: stated here without proof.

> Mahler proved (a more general result that implies in particular) that $2^k3^l\lt n^{1+o(1)}$.

```lean
theorem erdos_933.variants.mahler :
    ∃ c : ℕ → ℝ, (c =o[atTop] (1 : ℕ → ℝ)) ∧
      ∀ᶠ n in atTop, ((2 ^ k n * 3 ^ l n : ℕ) : ℝ) < (n : ℝ) ^ (1 + c n)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/933.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/933.lean#L56).

## `Erdos933.erdos_933.variants.lower_bound`

Proved here.

> Erdős [Er76d] wrote 'it is easy to see' that for infinitely many $n$, $2^k 3^l > n\log n$.
>
> Steinerberger has noted a simple proof of this fact follows from taking $n=2^{3^r}$ for any
> integer $r\geq 1$, when $k=3^r$ and $l=r+1$.

```lean
theorem erdos_933.variants.lower_bound :
    Set.Infinite { n : ℕ | ((2 ^ k n * 3 ^ l n : ℕ) : ℝ) > (n : ℝ) * Real.log (n : ℝ) }
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/933.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/933.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/933.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/933.lean)
- [erdosproblems.com/933](https://www.erdosproblems.com/933)
