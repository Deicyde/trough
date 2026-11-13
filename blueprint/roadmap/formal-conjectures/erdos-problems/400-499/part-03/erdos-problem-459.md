---
declaration: theorem
origin: cited
lean: Erdos459.erdos_459, Erdos459.erdos_459.variants.upper_tight
statement: formalized
---

# Erdős Problem 459

> *References:*
> - [erdosproblems.com/459](https://www.erdosproblems.com/459)
> - [ErGr80] P. Erdős and R. L. Graham, *Old and new problems and results in combinatorial number
>   theory*, Monographies de L'Enseignement Mathématique 28 (1980), p.91.
> - [OEIS A289280](https://oeis.org/A289280)

*Quoted from [FormalConjectures/ErdosProblems/459.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/459.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/459](https://www.erdosproblems.com/459).

The file states 2 research or textbook statements: 2 solved.

## `Erdos459.erdos_459`

Solved: stated here; a Lean proof is at [https://github.com/Woett/Lean-files/blob/main/ErdosProblem459.lean](https://github.com/Woett/Lean-files/blob/main/ErdosProblem459.lean).

> Let $f(u)$ be the largest $v$ such that no $m\in (u,v)$ is composed entirely of primes dividing
> $uv$. Estimate $f(u)$.
>
> The estimate $u + 2 \le f(u) \le u^2$ holds for every $u \ge 2$. The upper bound is attained
> when $u$ is prime, and the lower bound when $u = 2^k - 2$ with $k \ge 2$; Cambie further showed
> that $f(n) = (1 + o(1))n$ for almost all $n$.

```lean
theorem erdos_459 {u : ℕ} (hu : 2 ≤ u) : u + 2 ≤ f u ∧ f u ≤ u ^ 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/459.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/459.lean#L51).

## `Erdos459.erdos_459.variants.upper_tight`

Solved: stated here; a Lean proof is at [https://github.com/Woett/Lean-files/blob/main/ErdosProblem459.lean](https://github.com/Woett/Lean-files/blob/main/ErdosProblem459.lean).

> The upper bound $f u ≤ u ^ 2$ is attained exactly when `u` is prime: $f p = p ^ 2$.

```lean
theorem erdos_459.variants.upper_tight {p : ℕ} (hp : p.Prime) : f p = p ^ 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/459.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/459.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/459.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/459.lean)
- [erdosproblems.com/459](https://www.erdosproblems.com/459)
