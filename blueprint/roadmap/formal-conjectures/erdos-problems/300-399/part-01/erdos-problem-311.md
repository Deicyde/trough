---
declaration: theorem
origin: cited
lean: Erdos311.erdos_311, Erdos311.delta_ge_inv_lcm, Erdos311.delta_ge_exp
statement: formalized
---

# Erdős Problem 311

> *References:*
> - [erdosproblems.com/311](https://www.erdosproblems.com/311)
> - [ErGr80] P. Erdős and R. L. Graham, *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathématique (1980), p. 40.

*Quoted from [FormalConjectures/ErdosProblems/311.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/311.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/311](https://www.erdosproblems.com/311).

The file states 3 research or textbook statements: 1 open and 2 textbook results. It also has 1 test statement, counted here but not shown.

## `Erdos311.erdos_311`

Open: stated without proof.

> Let $\delta(N)$ be the minimal non-zero value of $\lvert 1-\sum_{n\in A}\frac{1}{n}\rvert$ as $A$
> ranges over all subsets of $\{1,\ldots,N\}$. Is it true that
> $$\delta(N)=e^{-(c+o(1))N}$$
> for some constant $c\in (0,1)$?
>
> The formulation in [ErGr80] has the additional condition that $A$ contains no $S$ with
> $\sum_{n\in S}\frac{1}{n}=1$; Kovac (in the comments on the problem page) showed that the
> formulation above is equivalent. We state $\delta(N)=e^{-(c+o(1))N}$ as
> $-\log \delta(N) / N \to c$.

```lean
theorem erdos_311 :
    ∃ c ∈ Set.Ioo (0 : ℝ) 1,
      Tendsto (fun N : ℕ => -Real.log (delta N) / N) atTop (𝓝 c)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/311.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/311.lean#L55).

## `Erdos311.delta_ge_inv_lcm`

Textbook result, stated without proof.

> The trivial lower bound: every non-zero value of $1 - \sum_{n \in A} 1/n$ is a non-zero rational
> with denominator dividing $[1, \ldots, N]$, so $\delta(N) \geq 1/[1,\ldots,N]$.

```lean
theorem delta_ge_inv_lcm (N : ℕ) : 1 / (((Icc 1 N).lcm id : ℕ) : ℝ) ≤ delta N
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/311.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/311.lean#L65).

## `Erdos311.delta_ge_exp`

Textbook result, stated without proof.

> Since $[1, \ldots, N] = e^{(1+o(1))N}$, the trivial bound gives $\delta(N) \ge e^{-(1+o(1))N}$.

```lean
theorem delta_ge_exp : ∀ ε > 0, ∀ᶠ N : ℕ in atTop, Real.exp (-(1 + ε) * N) ≤ delta N
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/311.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/311.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/311.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/311.lean)
- [erdosproblems.com/311](https://www.erdosproblems.com/311)
