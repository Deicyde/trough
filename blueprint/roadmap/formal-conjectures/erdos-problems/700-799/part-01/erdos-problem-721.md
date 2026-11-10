---
declaration: theorem
origin: cited
lean: Erdos721.erdos_721.upper_bound, Erdos721.erdos_721.lower_bound
statement: formalized
---

# Erdős Problem 721

> *References:*
> - [erdosproblems.com/721](https://www.erdosproblems.com/721)
> - [Gr22] Green, B., *New lower bounds for van der Waerden numbers*.
>   [arXiv:2102.01543](https://arxiv.org/abs/2102.01543).
> - [Hu22] Hunter, Z., *Improved lower bounds for van der Waerden numbers*.
>   [arXiv:2111.01099](https://arxiv.org/abs/2111.01099).
> - [Sc21] Schoen, T., *A subexponential upper bound for van der Waerden numbers W(3,k)*.
>   [arXiv:2006.02877](https://arxiv.org/abs/2006.02877).

*Quoted from [FormalConjectures/ErdosProblems/721.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/721.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/721](https://www.erdosproblems.com/721).

The file states 2 research or textbook statements: 2 solved. It also has 2 API statements, counted here but not shown.

## `Erdos721.erdos_721.upper_bound`

Solved: stated here without proof.

> Erdős Problem 721, upper bound: prove that $W(3,k) < \exp(k^c)$ for some
> constant $c<1$.
>
> The first to show that $W(3,k) < \exp(k^c)$ for some $c<1$ was Schoen [Sc21].
> Source: [erdosproblems.com/721](https://www.erdosproblems.com/721).
> The exponent is fixed independently of $k$, and the bound holds for all
> sufficiently large $k$.

```lean
theorem erdos_721.upper_bound : SubexponentialUpperBound
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/721.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/721.lean#L93).

## `Erdos721.erdos_721.lower_bound`

Solved: stated here without proof.

> Erdős Problem 721, lower bound: Hunter [Hu22] improved this to
> $W(3,k) \geq \exp\left(c\frac{(\log k)^2}{\log\log k}\right)$
> for some constant $c>0$.
>
> Source: [erdosproblems.com/721](https://www.erdosproblems.com/721).
> This eventual bound uses a nonforcing interval of length $N$ and the
> successor $N+1$ as a lower bound for the least forcing integer.

```lean
theorem erdos_721.lower_bound : HunterLowerBound
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/721.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/721.lean#L104).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/721.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/721.lean)
- [erdosproblems.com/721](https://www.erdosproblems.com/721)
