---
declaration: theorem
origin: cited
lean: Erdos994.erdos_994, Erdos994.erdos_994.variants.simultaneous
statement: formalized
---

# Erdős Problem 994

> *References:*
> - [erdosproblems.com/994](https://www.erdosproblems.com/994)
> - [Er64b] Erdős, P., _Problems and results on diophantine approximations_. Compositio Math.
>   (1964), 52-65.
> - [Kh23] Khintchine, A., _Ein Satz über Kettenbrüche, mit arithmetischen Anwendungen_. Math. Z.
>   (1923), 289--306.
> - [Ma70] Marstrand, J. M., _On Khinchin's conjecture about strong uniform distribution_. Proc.
>   London Math. Soc. (3) (1970), 540--556.

*Quoted from [FormalConjectures/ErdosProblems/994.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/994.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/994](https://www.erdosproblems.com/994).

The file states 2 research or textbook statements: 1 solved and 1 textbook result.

## `Erdos994.erdos_994`

Solved: stated here without proof.

> Let $E\subseteq (0,1)$ be a meaurable subset with Lebesgue measure $\lambda(E)$. Is it true that,
> for almost all $\alpha$,
> $$\lim_{n\to \infty}\frac{1}{n}\sum_{1\leq k\leq n}1_{\{k\alpha \}\in E}=\lambda(E)$$
> for all $E$?
>
> This is a conjecture of Khintchine [Kh23] (with the exceptional null set of $\alpha$ allowed to
> depend on $E$). It is false, and was disproved by Marstrand [Ma70].

```lean
theorem erdos_994 :
    ¬ ∀ E ⊆ Ioo (0 : ℝ) 1, MeasurableSet E →
      ∀ᵐ α : ℝ, Tendsto (visitAverage E α) atTop (nhds (volume E).toReal)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/994.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/994.lean#L55).

## `Erdos994.erdos_994.variants.simultaneous`

Textbook result, proved here.

> Read literally, with "for almost all $\alpha$" placed before "for all $E$", the statement is
> trivially false: for any $\alpha$, removing the countable orbit $\{\{k\alpha\} : k\geq 1\}$ from
> $(0,1)$ gives a measurable set of measure $1$ which is never visited.

```lean
theorem erdos_994.variants.simultaneous :
    ¬ ∀ᵐ α : ℝ, ∀ E ⊆ Ioo (0 : ℝ) 1, MeasurableSet E →
      Tendsto (visitAverage E α) atTop (nhds (volume E).toReal)
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/994.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/994.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/994.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/994.lean)
- [erdosproblems.com/994](https://www.erdosproblems.com/994)
