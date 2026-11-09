---
declaration: theorem
origin: cited
lean: Erdos86.erdos_86
statement: formalized
---

# Erdős Problem 86

> *References:*
> - [erdosproblems.com/86](https://www.erdosproblems.com/86)
> - [BHLL14] Balogh, József and Hu, Ping and Lidický, Bernard and Liu, Hong, *Upper bounds on the size
>   of 4- and 6-cycle-free subgraphs of the hypercube*. European J. Combin. (2014), 75-85.
> - [BHN95] Brass, Peter and Harborth, Heiko and Nienborg, Hauke, *On the maximum number of edges in a
>   {$C_4$}-free subgraph of {$Q_n$}*. J. Graph Theory (1995), 17--23.
> - [Ba12b] R. Baber, *Turán densities of hypercubes*. arXiv:1201.3587 (2012).
> - [Er91] Erdős, P., *Problems and results in combinatorial analysis and combinatorial number
>   theory*. Graph theory, combinatorics, and applications, Vol. 1 (Kalamazoo, MI, 1988) (1991),
>   397-406.

*Quoted from [FormalConjectures/ErdosProblems/86.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/86.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/86](https://www.erdosproblems.com/86).

The file states 1 research or textbook statement: 1 open.

## `Erdos86.erdos_86`

Open: stated without proof.

> Let $Q_n$ be the $n$-dimensional hypercube graph (so that $Q_n$ has $2^n$ vertices and $n2^{n-1}$ edges). Is it true that every subgraph of $Q_n$ with $$\geq \left(\frac{1}{2}+o(1)\right)n2^{n-1}$$ many edges contains a $C_4$?

```lean
theorem erdos_86 :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ n : ℕ in atTop, ∀ H : SimpleGraph (Fin n → Bool),
      H ≤ hypercube n →
        (1 / 2 + ε) * n * 2 ^ (n - 1 : ℕ) ≤ (H.edgeSet.ncard : ℝ) →
          cycleGraph 4 ⊑ H
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/86.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/86.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/86.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/86.lean)
- [erdosproblems.com/86](https://www.erdosproblems.com/86)
