---
declaration: theorem
origin: cited
lean: Erdos1197.erdos_1197
statement: formalized
---

# Erdős Problem 1197

> *References:*
> - [erdosproblems.com/1197](https://www.erdosproblems.com/1197)
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   (1980), 89-115.
> - [BuMa99] Buczolich, Zoltán and Mauldin, R. Daniel, *On the convergence of
>   $\sum^\infty_{n=1}f(nx)$ for measurable functions*. Mathematika (1999), 337--341.

*Quoted from [FormalConjectures/ErdosProblems/1197.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1197.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1197](https://www.erdosproblems.com/1197).

The file states 1 research or textbook statement: 1 solved.

## `Erdos1197.erdos_1197`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1197.lean#L705](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1197.lean#L705).

> Let $E\subset (0,\infty)$ be a set of positive measure. Is it true that, for almost all $x>0$,
> for all sufficiently large (depending on $x$) integers $n$ there exists an integer $r\geq 1$ such
> that $nx\in r\cdot E$?
>
> A problem of Haight, who constructed a set $E\subset (0,\infty)$ of infinite measure such that,
> for all $x\in E$, $x\not\in r\cdot E$ if $r\geq 2$, and also for all $x>0$, if $n$ is large enough
> then $nx\not\in E$ (see [1195](https://www.erdosproblems.com/1195)).
>
> This is trivially true if $E$ contains an interval $(a,b)$ with $a\lt b$, since for any $x>0$, for
> all large $n$, the interval $(\frac{nx}{b},\frac{nx}{a})$ has length $>1$ so contains at least
> one integer $r\geq 1$.
>
> Buczolich and Mauldin [BuMa99] proved that there exists an open set $E\subset (0,\infty)$ and two
> intervals $I,J\subset [1/2,1)$ such that, for all $x\in I$, $x\in \frac{1}{n}\cdot E$ for
> infinitely many $n\geq 1$, and for almost all $x\in J$, $x\not\in \frac{1}{n}\cdot E$ for all
> sufficiently large (depending on $x$) $n$.
>
> This was solved in the negative by ebarschkis in the comments, who constructed a counterexample
> using a variant of the Buczolich-Mauldin construction.

```lean
theorem erdos_1197 : ¬ ∀ E : Set ℝ, MeasurableSet E → E ⊆ Set.Ioi 0 → 0 < volume E →
    ∀ᵐ x ∂(volume.restrict (Set.Ioi (0 : ℝ))), ∀ᶠ n : ℕ in atTop,
      ∃ r : ℕ, 1 ≤ r ∧ (n : ℝ) * x ∈ (r : ℝ) • E
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/1197.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1197.lean#L62).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1197.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1197.lean)
- [erdosproblems.com/1197](https://www.erdosproblems.com/1197)
