---
declaration: theorem
origin: cited
lean: Erdos832.erdos_832
statement: formalized
---

# Erdős Problem 832

> *References:*
> - [erdosproblems.com/832](https://www.erdosproblems.com/832)
> - [AkSh16] Akolzin, Ilia and Shabanov, Dmitry, Colorings of hypergraphs with large number of colors.
>   Discrete Math. (2016), 3020--3031.
> - [Al85] Alon, Noga, Hypergraphs with high chromatic number. Graphs Combin. (1985), 387--389.
> - [ChPe20] Cherkashin, Danila and Petrov, Fedor, Regular behavior of the maximal hypergraph
>   chromatic number. SIAM J. Discrete Math. (2020), 1326--1333.

*Quoted from [FormalConjectures/ErdosProblems/832.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/832.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/832](https://www.erdosproblems.com/832).

The file states 1 research or textbook statement: 1 solved.

## `Erdos832.erdos_832`

Solved: stated here without proof.

> Let $r\geq 3$ and $k$ be sufficiently large in terms of $r$. Is it true that every $r$-uniform
> hypergraph with chromatic number $k$ has at least
>
> $$\binom{(r-1)(k-1)+1}{r}$$
>
> edges, with equality only for the complete graph on $(r-1)(k-1)+1$ vertices?
>
> This was disproved by Alon [Al85]. The validity of this conjecture for $r=3$ remains open.

```lean
theorem erdos_832 :
    ¬ ∀ r : ℕ, 3 ≤ r → ∀ᶠ k : ℕ in atTop,
    ∀ (n : ℕ) (H : Finset (Finset (Fin n))),
      H.IsUniform r → H.HasHypergraphChromaticNumber k →
      ((r - 1) * (k - 1) + 1).choose r ≤ H.card ∧
      (H.card = ((r - 1) * (k - 1) + 1).choose r →
        ∃ S : Finset (Fin n), S.card = (r - 1) * (k - 1) + 1 ∧ H = S.powersetCard r)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/832.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/832.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/832.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/832.lean)
- [erdosproblems.com/832](https://www.erdosproblems.com/832)
