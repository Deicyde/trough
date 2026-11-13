---
declaration: theorem
origin: cited
lean: Erdos196.erdos_196
statement: formalized
---

# Erdős Problem 196

> *References:*
> - [erdosproblems.com/196](https://www.erdosproblems.com/196)
> - [DEGS77] Davis, J. A. and Entringer, R. C. and Graham, R. L. and Simmons, G. J.,
>   *On permutations containing no long arithmetic progressions*. Acta Arith. (1977), 81-90.
> - [Ho26] Ho, Boon Suan, *A 4AP-free permutation of the positive integers*.
>   [arXiv:2609.12780](https://arxiv.org/abs/2609.12780)

*Quoted from [FormalConjectures/ErdosProblems/196.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/196.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/196](https://www.erdosproblems.com/196).

The file states 1 research or textbook statement: 1 solved.

## `Erdos196.erdos_196`

Solved: stated here; a Lean proof is at [https://github.com/lkruer/conjectures/blob/8ede860e8fc90a300207a2c17e8aefe6167b3086/problems/erdos-196/lean/Erdos196.lean](https://github.com/lkruer/conjectures/blob/8ede860e8fc90a300207a2c17e8aefe6167b3086/problems/erdos-196/lean/Erdos196.lean).

> Must every permutation of $\mathbb{N}$ contain a monotone 4-term arithmetic progression?
>
> Here a monotone $k$-term arithmetic progression in a permutation $f$ is a set of indices
> $i_1 < \cdots < i_k$ such that $f(i_1), \ldots, f(i_k)$ is an increasing or decreasing arithmetic
> progression. [DEGS77] showed that every permutation of $\mathbb{N}$ contains a monotone 3-term
> arithmetic progression, and that there are permutations with no monotone 5-term arithmetic
> progression.
>
> The answer is no: [Ho26] constructs an explicit permutation of the positive integers with no
> monotone 4-term arithmetic progression. Independent constructions with Lean formalizations were
> given shortly afterwards by Kruer and Kohlmeyer and, pseudonymously, in the repository
> `coleski/erdos196`; the linked formal proof establishes the negation of this statement.

```lean
theorem erdos_196 : ¬ ∀ (f : ℕ ≃ ℕ), HasMonotoneAP f 4
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/196.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/196.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/196.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/196.lean)
- [erdosproblems.com/196](https://www.erdosproblems.com/196)
