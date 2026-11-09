---
declaration: theorem
origin: cited
lean: Erdos77.erdos_77
statement: formalized
---

# Erdős Problem 77

> *References:*
> - [erdosproblems.com/77](https://www.erdosproblems.com/77)
> - [BBCGHMST24] Balister, P. and Bollobás, B. and Campos, M. and Griffiths, S. and Hurley, E. and
>   Morris, R. and Sahasrabudhe, J. and Tiba, M., Upper bounds for multicolour Ramsey numbers.
>   arXiv:2410.17197 (2024).
> - [CGMS23] Campos, Marcelo and Griffiths, Simon and Morris, Robert and Sahasrabudhe, Julian, An
>   exponential improvement for diagonal Ramsey. arXiv:2303.09521 (2023).
> - [Er88] Erdős, P, Problems and results in combinatorial analysis and graph theory. Discrete Math.
>   (1988), 81-92.
> - [Er93] Erdős, Paul, Some of my favorite solved and unsolved problems in graph theory. Quaestiones
>   Math. (1993), 333-350.
> - [GNNW24] Gupta, P. and Ndiaye, N. and Norin, S. and Wei, L., Optimizing the CGMS upper bound on
>   Ramsey numbers. arXiv:2407.19026 (2024).

*Quoted from [FormalConjectures/ErdosProblems/77.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/77.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/77](https://www.erdosproblems.com/77).

The file states 1 research or textbook statement: 1 open.

## `Erdos77.erdos_77`

Open: stated without proof.

> If $R(k)$ is the Ramsey number for $K_k$, the minimal $n$ such that every $2$-colouring of the edges
> of $K_n$ contains a monochromatic copy of $K_k$, then find the value of
> $$\lim_{k\to \infty}R(k)^{1/k}.$$
>
> This problem is #3 in Ramsey Theory in the graphs problem collection.

```lean
theorem erdos_77 :
    Filter.Tendsto (fun k : ℕ ↦ (SimpleGraph.diagonalRamsey k : ℝ) ^ (1 / (k : ℝ)))
      Filter.atTop (𝓝 erdos_77.answer)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/77.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/77.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/77.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/77.lean)
- [erdosproblems.com/77](https://www.erdosproblems.com/77)
