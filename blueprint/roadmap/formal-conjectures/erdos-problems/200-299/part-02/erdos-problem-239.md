---
declaration: theorem
origin: cited
lean: Erdos239.erdos_239
statement: formalized
---

# Erdős Problem 239

> *References:*
> - [erdosproblems.com/239](https://www.erdosproblems.com/239)
> - [Ha68] Halász, G., Über die Mittelwerte multiplikativer zahlentheoretischer
>   Funktionen. Acta Math. Acad. Sci. Hungar. (1968), 365-403.
> - [Wi67] Wirsing, E., Das asymptotische Verhalten von Summen über multiplikative Funk­tionen.
>   Acta Math. Acad. Sei. Hung. (1967), 411-467.

*Quoted from [FormalConjectures/ErdosProblems/239.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/239.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/239](https://www.erdosproblems.com/239).

The file states 1 research or textbook statement: 1 solved.

## `Erdos239.erdos_239`

Solved: stated here without proof.

> Let $f:\mathbb{N}\to \{-1,1\}$ be a multiplicative function. Is it true that
> $$ \lim_{N\to \infty}\frac{1}{N}\sum_{n\leq N}f(n)$$ always exists?
>
> The answer is yes, as proved by Wirsing [Wi67], and generalised by Halász [Ha68].

```lean
theorem erdos_239 :
    ∀ f : ℕ → ℝ,
    (∀ n ≥ 1, f n = 1 ∨ f n = -1) ∧
    (∀ m n, m.Coprime n → f (m * n) = f m * f n) ∧
    f 1 = 1 →
    ∃ L, Tendsto (fun N ↦ (∑ n ∈ Finset.Icc 1 N, f n) / N) atTop (𝓝 L)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/239.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/239.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/239.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/239.lean)
- [erdosproblems.com/239](https://www.erdosproblems.com/239)
