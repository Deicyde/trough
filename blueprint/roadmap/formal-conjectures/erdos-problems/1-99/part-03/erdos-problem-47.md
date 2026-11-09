---
declaration: theorem
origin: cited
lean: Erdos47.erdos_47
statement: formalized
---

# Erdős Problem 47

> *References:*
> - [erdosproblems.com/47](https://www.erdosproblems.com/47)
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   (1980), 89-115.
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Er92c] Erdős, P., *Some of my forgotten problems in number theory*. Hardy-Ramanujan J. (1992),
>   34-50.
> - [Er95] Erdős, Paul, *Some of my favourite problems in number theory, combinatorics, and geometry*.
>   Resenhas (1995), 165-186.
> - [Er96b] Erdős, Paul, *Some problems I presented or planned to present in my short talk*. Analytic
>   number theory, Vol. 1 (Allerton Park, IL, 1995) (1996), 333-335.
> - [Er97c] Erdős, Paul, *Some of my favorite problems and results*. The mathematics of Paul Erdős, I
>   (1997), 47-67.
> - [Bl21] Bloom, T. F., *On a density conjecture about unit fractions*. arXiv:2112.03726
>   (2021).
> - [LiSa24] Liu, Y. and Sawhney, M., *On further questions regarding unit fractions*.
>   arXiv:2404.07113 (2024).

*Quoted from [FormalConjectures/ErdosProblems/47.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/47.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/47](https://www.erdosproblems.com/47).

The file states 1 research or textbook statement: 1 solved.

## `Erdos47.erdos_47`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos47.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos47.lean).

> If $\delta>0$ and $N$ is sufficiently large in terms of $\delta$, and $A\subseteq\{1,\ldots,N\}$ is such that $\sum_{a\in A}\frac{1}{a}>\delta \log N$ then must there exist $S\subseteq A$ such that $\sum_{n\in S}\frac{1}{n}=1$?
>
> Bloom [Bl21] proved this in the affirmative.

```lean
theorem erdos_47 :
    ∀ δ : ℝ, 0 < δ → ∀ᶠ N : ℕ in atTop, ∀ A : Finset ℕ,
      A ⊆ Finset.Icc 1 N →
      δ * Real.log (N : ℝ) < A.reciprocalSum →
      ∃ S : Finset ℕ, S ⊆ A ∧ S.reciprocalSum = 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/47.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/47.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/47.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/47.lean)
- [erdosproblems.com/47](https://www.erdosproblems.com/47)
