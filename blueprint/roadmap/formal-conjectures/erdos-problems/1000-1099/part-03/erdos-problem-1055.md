---
declaration: theorem
origin: cited
lean: Erdos1055.exists_p, Erdos1055.erdos_1055, Erdos1055.erdos_1055.variants.erdos_limit, Erdos1055.erdos_1055.variants.selfridge_limit
statement: formalized
---

# Erdős Problem 1055

> *Reference:* [erdosproblems.com/1055](https://www.erdosproblems.com/1055)

*Quoted from [FormalConjectures/ErdosProblems/1055.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1055.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1055](https://www.erdosproblems.com/1055).

The file states 4 research or textbook statements: 3 open and 1 textbook result.

## `Erdos1055.exists_p`

Textbook result, stated without proof.

> A prime $p$ is in class $1$ if the only prime divisors of $p+1$ are
> $2$ or $3$. In general, a prime $p$ is in class $r$ if every prime factor
> of $p+1$ is in some class $\leq r-1$, with equality for at least one prime factor.
> Show that for each $r$ there exists a prime $p$ of class $r$.

```lean
theorem exists_p (r : ℕ+) : ∃ p, p.Prime ∧ IsOfClass r p
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1055.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1055.lean#L54).

## `Erdos1055.erdos_1055`

Open: stated without proof.

> A prime $p$ is in class $1$ if the only prime divisors of $p+1$ are
> $2$ or $3$. In general, a prime $p$ is in class $r$ if every prime factor
> of $p+1$ is in some class $\leq r-1$, with equality for at least one prime factor.
> Are there infinitely many primes in each class?

```lean
theorem erdos_1055 (r) : {p | p.Prime ∧ IsOfClass r p}.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1055.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1055.lean#L71).

## `Erdos1055.erdos_1055.variants.erdos_limit`

Open: stated without proof.

> A prime $p$ is in class $1$ if the only prime divisors of $p+1$ are
> $2$ or $3$. In general, a prime $p$ is in class $r$ if every prime factor
> of $p+1$ is in some class $\leq r-1$, with equality for at least one prime factor.
> If $p_r$ is the least prime in class $r$, then how does $p_r^{1/r}$ behave?
> Erdos conjectured that this tends to infinity.

```lean
theorem erdos_1055.variants.erdos_limit :
    Filter.atTop.Tendsto (fun r ↦ (p r : ℝ) ^ (1 / r : ℝ)) Filter.atTop
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1055.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1055.lean#L80).

## `Erdos1055.erdos_1055.variants.selfridge_limit`

Open: stated without proof.

> A prime $p$ is in class $1$ if the only prime divisors of $p+1$ are
> $2$ or $3$. In general, a prime $p$ is in class $r$ if every prime factor
> of $p+1$ is in some class $\leq r-1$, with equality for at least one prime factor.
> If $p_r$ is the least prime in class $r$, then how does $p_r^{1/r}$ behave?
> Selfridge conjectured that this is bounded.

```lean
theorem erdos_1055.variants.selfridge_limit :
    ∃ M, ∀ r, (p r : ℝ) ^ (1 / r : ℝ) ≤ M
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1055.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1055.lean#L90).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1055.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1055.lean)
- [erdosproblems.com/1055](https://www.erdosproblems.com/1055)
