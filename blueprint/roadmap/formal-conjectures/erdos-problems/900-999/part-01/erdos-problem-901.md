---
declaration: theorem
origin: cited
lean: Erdos901.erdos_901
statement: formalized
---

# Erdős Problem 901

> *References:*
> - [erdosproblems.com/901](https://www.erdosproblems.com/901)
> - [Be77] Beck, J., On a combinatorial problem of {P}. {E}rdős and {L}. {L}ovász. Discrete Math.
>   (1977), 127--131.
> - [Be78] Beck, J., On {$3$}-chromatic hypergraphs. Discrete Math. (1978), 127--137.
> - [Er63b] Erdős, P., On a combinatorial problem. Nordisk Mat. Tidskr. (1963), 5--10, 40.
> - [Er64e] Erdős, P., On a combinatorial problem. {II}. Acta Math. Acad. Sci. Hungar. (1964),
>   445--447.
> - [ErLo75] Erdős, P. and Lovász, L., Problems and results on {$3$}-chromatic hypergraphs and some
>   related questions. (1975), 609--627.
> - [Pl09] Pluhár, András, Greedy colorings of uniform hypergraphs. Random Structures Algorithms
>   (2009), 216--221.
> - [RaSr00] Radhakrishnan, Jaikumar and Srinivasan, Aravind, Improved bounds and algorithms for
>   hypergraph {$2$}-coloring. Random Structures Algorithms (2000), 4--32.

*Quoted from [FormalConjectures/ErdosProblems/901.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/901.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/901](https://www.erdosproblems.com/901).

The file states 1 research or textbook statement: 1 open.

## `Erdos901.erdos_901`

Open: stated without proof.

> Let $m(n)$ be minimal such that there is an $n$-uniform hypergraph with $m(n)$ edges which is
> $3$-chromatic. Estimate $m(n)$.

```lean
theorem erdos_901 :
    (fun n ↦ ((Hypergraph.minChromaticEdges n 3).toNat : ℝ)) =Θ[atTop]
    erdos_901.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/901.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/901.lean#L52).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/901.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/901.lean)
- [erdosproblems.com/901](https://www.erdosproblems.com/901)
