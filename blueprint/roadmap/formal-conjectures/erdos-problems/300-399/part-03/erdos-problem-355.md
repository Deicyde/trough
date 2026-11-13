---
declaration: theorem
origin: cited
lean: Erdos355.erdos_355
statement: formalized
---

# Erdős Problem 355

> *References:*
> - [erdosproblems.com/355](https://www.erdosproblems.com/355)
> - [DoKo25] W. van Doorn and V. Kovač, Lacunary sequences whose reciprocal sums represent all
>   rationals in an interval. arXiv:2509.24971 (2025).

*Quoted from [FormalConjectures/ErdosProblems/355.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/355.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/355](https://www.erdosproblems.com/355).

The file states 1 research or textbook statement: 1 solved.

## `Erdos355.erdos_355`

Solved: stated here; a Lean proof is at [https://github.com/Woett/Lean-files/blob/main/ErdosProblem355.lean](https://github.com/Woett/Lean-files/blob/main/ErdosProblem355.lean).

> Is there a lacunary sequence $A\subseteq \mathbb{N}$ (so that $A=\{a_1 < \cdots\}$ and
> there exists some $\lambda > 1$ such that $a_{n+1}/a_n\geq \lambda$ for all $n\geq 1$) such that
>
> $$\left\{ \sum_{a\in A'}\frac{1}{a} : A'\subseteq A\textrm{ finite}\right\}$$
>
> contain all rationals in some open interval?
>
> Bleicher and Erdős conjectured the answer is no.
>
> In fact the answer is yes, with any lacunarity constant $\lambda\in (1,2)$ (though not $\lambda=2$),
> as proved by van Doorn and Kova\v{c} [DoKo25].
>
> This was formalized in Lean by van Doorn using Aristotle.

```lean
theorem erdos_355 :
    ∃ A : ℕ → ℕ, IsLacunary A ∧ ∃ u v : ℝ, u < v ∧ ∀ q : ℚ, ↑q ∈ Set.Ioo u v →
      q ∈ {∑ a ∈ A', (1 / a : ℚ) | (A' : Finset ℕ) (_ : ↑A' ⊆ Set.range A)}
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/355.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/355.lean#L49).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/355.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/355.lean)
- [erdosproblems.com/355](https://www.erdosproblems.com/355)
