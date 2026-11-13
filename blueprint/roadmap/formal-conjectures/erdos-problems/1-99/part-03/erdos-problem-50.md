---
declaration: theorem
origin: cited
lean: Erdos50.erdos_50_schoenberg, Erdos50.erdos_50_singular, Erdos50.erdos_50
statement: formalized
---

# Erdős Problem 50

> *References:*
> * [erdosproblems.com/50](https://www.erdosproblems.com/50)
> * [Er95] Erdős, Paul, Some of my favourite problems in number theory, combinatorics, and geometry.
> Resenhas (1995), 165-186.
> * [Sch38] Schoenberg, I. J. "On asymptotic distributions of arithmetical functions."
> Transactions of the American Mathematical Society 39.2 (1936): 315-330.

*Quoted from [FormalConjectures/ErdosProblems/50.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/50.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/50](https://www.erdosproblems.com/50).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos50.erdos_50_schoenberg`

Solved: stated here without proof.

> Schoenberg [Sch38] proved that the asymptotic distribution function of $\varphi(n)/n$ exists.
> That is, for any $c \in [0, 1]$, the proportion of integers $n \le N$ satisfying $\varphi(n)/n < c$
> approaches a limit as $N \to \infty$. This limit function is the cumulative distribution function
> of the values of $\varphi(n)/n$.

```lean
theorem erdos_50_schoenberg : ∃ f : ℝ → ℝ, IsDistributionOfPhiRatio f
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/50.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/50.lean#L61).

## `Erdos50.erdos_50_singular`

Solved: stated here without proof.

> Erdős [Er95] proved that the distribution function of $\varphi(n)/n$ is purely singular on
> $[0, 1]$: it is continuous there, but its derivative is zero almost everywhere on $[0, 1]$.

```lean
theorem erdos_50_singular (f : ℝ → ℝ) (hf : IsDistributionOfPhiRatio f) :
    IsPurelySingularOn f (Icc 0 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/50.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/50.lean#L69).

## `Erdos50.erdos_50`

Open: stated without proof.

> Let $f$ be the asymptotic distribution function of $\varphi(n)/n$, so that for each $c \in [0,1]$,
> $f(c)$ is the natural density of $\{n : \varphi(n) < cn\}$. Is it true that there is no $x$ such
> that the derivative $f'(x)$ exists and is positive?

```lean
theorem erdos_50 : ∀ᵉ (f : ℝ → ℝ) (hf : IsDistributionOfPhiRatio f),
    ¬∃ x ∈ Icc (0 : ℝ) 1, ∃ y > 0, HasDerivWithinAt f y (Icc 0 1) x
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/50.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/50.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/50.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/50.lean)
- [erdosproblems.com/50](https://www.erdosproblems.com/50)
