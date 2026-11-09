---
declaration: theorem
origin: cited
lean: Erdos79.erdos_79
statement: formalized
---

# Erdős Problem 79

> *References:*
> - [erdosproblems.com/79](https://www.erdosproblems.com/79)
> - [EFRS93] Erdős, P., Faudree, R. J., Rousseau, C. C. and Schelp, R. H., Ramsey size linear graphs.
>   Combin. Probab. Comput. (1993), 389-399.
> - [Wi24] Wigderson, Y., Infinitely many minimally non-Ramsey size linear graphs.
>   arXiv:2409.05931 (2024).

*Quoted from [FormalConjectures/ErdosProblems/79.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/79.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/79](https://www.erdosproblems.com/79).

The file states 1 research or textbook statement: 1 solved.

## `Erdos79.erdos_79`

Solved: stated here without proof.

> We say $G$ is Ramsey size linear if $R(G,H)\ll m$ for all graphs $H$ with $m$ edges and
> no isolated vertices.
>
> Are there infinitely many graphs $G$ which are not Ramsey size linear but such that all of
> its proper subgraphs are?
>
> Asked by Erdős, Faudree, Rousseau, and Schelp [EFRS93]. $K_4$ was long the only known example.
> Wigderson [Wi24] proved that there are infinitely many such graphs.

```lean
theorem erdos_79 :
    ∀ (N : ℕ), ∃ (n : ℕ) (_ : N ≤ n) (G : SimpleGraph (Fin n)),
      ¬ G.IsRamseySizeLinear ∧
      ∀ H : G.Subgraph, H < ⊤ → H.coe.IsRamseySizeLinear
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/79.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/79.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/79.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/79.lean)
- [erdosproblems.com/79](https://www.erdosproblems.com/79)
