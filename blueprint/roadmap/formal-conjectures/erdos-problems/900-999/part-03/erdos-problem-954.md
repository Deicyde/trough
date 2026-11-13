---
declaration: theorem
origin: cited
lean: Erdos954.erdos_954, Erdos954.erdos_954.variants.upper, Erdos954.erdos_954.variants.lower
statement: formalized
---

# Erdős Problem 954

> *References:*
> - [erdosproblems.com/954](https://www.erdosproblems.com/954)
> - [Er77c] Erdős, P., *Problems and results on combinatorial number theory. III*. Number theory
>   day (Proc. Conf., Rockefeller Univ., New York, 1976), Lecture Notes in Math. 626, Springer
>   (1977), 43-72. [PDF](https://www.renyi.hu/~p_erdos/1977-27.pdf)

*Quoted from [FormalConjectures/ErdosProblems/954.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/954.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/954](https://www.erdosproblems.com/954).

The file states 3 research or textbook statements: 2 open and 1 textbook result. It also has 3 test statements, counted here but not shown.

## `Erdos954.erdos_954`

Open: stated without proof.

> Let $0=a_0\lt a_1\lt a_2\lt \cdots$ be the sequence of integers defined by $a_0=0$ and $a_1=1$, and
> $a_{k+1}$ is the smallest integer $n$ for which the number of solutions to $a_i+a_j \leq n$
> (with $0\leq i\leq j\leq k$ and $j\geq 1$) is $\lt n$.
>
> Is the number of solutions to $a_i+a_j \leq x$ equal to $x+O(x^{1/4+o(1)})$?
>
> The sequence was constructed by Rosen [Er77c, p. 71]. We read $O(x^{1/4+o(1)})$ as
> $O(x^{1/4+\varepsilon})$ for every $\varepsilon>0$, and use the version with $a_0=0$.

```lean
theorem erdos_954 :
    ∀ ε > (0 : ℝ), (fun x : ℕ ↦ (solutionCount x : ℝ) - x) =O[atTop]
      (fun x : ℕ ↦ (x : ℝ) ^ ((1 : ℝ) / 4 + ε))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/954.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/954.lean#L87).

## `Erdos954.erdos_954.variants.upper`

Open: stated without proof.

> Erdős and Rosen could not even prove that the number of solutions to $a_i+a_j\leq x$ is at most
> $(1+o(1))x$ [Er77c, p. 71].

```lean
theorem erdos_954.variants.upper :
    ∀ ε > (0 : ℝ), ∀ᶠ x : ℕ in atTop, (solutionCount x : ℝ) ≤ (1 + ε) * x
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/954.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/954.lean#L97).

## `Erdos954.erdos_954.variants.lower`

Textbook result, stated without proof.

> The number of solutions to $a_i+a_j\leq x$ is always at least $x$ by construction
> [Er77c, p. 71].

```lean
theorem erdos_954.variants.lower : ∀ x : ℕ, x ≤ solutionCount x
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/954.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/954.lean#L106).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/954.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/954.lean)
- [erdosproblems.com/954](https://www.erdosproblems.com/954)
