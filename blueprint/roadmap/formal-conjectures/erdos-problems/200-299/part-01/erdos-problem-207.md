---
declaration: theorem
origin: cited
lean: Erdos207.erdos_207
statement: formalized
---

# Erdős Problem 207

> *References:*
> - [erdosproblems.com/207](https://www.erdosproblems.com/207)
> - [KSSS22b] Kwan, M. and Sah, A. and Sawhney, M. and Simkin, M., High-girth Steiner triple systems.
>   arXiv:2201.04554 (2022).

*Quoted from [FormalConjectures/ErdosProblems/207.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/207.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/207](https://www.erdosproblems.com/207).

The file states 1 research or textbook statement: 1 solved.

## `Erdos207.erdos_207`

Solved: stated here without proof.

> For any $g\geq 2$, if $n$ is sufficiently large and $\equiv 1,3\pmod{6}$ then there exists a
> 3-uniform hypergraph on $n$ vertices such that
>
> - every pair of vertices is contained in exactly one edge (i.e. the graph is a Steiner triple
> system) and
>
> - for any $2\leq j\leq g$ any collection of $j$ edges contains at least $j+3$ vertices.
>
> Proved by Kwan, Sah, Sawhney, and Simkin [KSSS22b].

```lean
theorem erdos_207 :
    ∀ g : ℕ, 2 ≤ g → ∀ᶠ n : ℕ in atTop,
    n % 6 = 1 ∨ n % 6 = 3 → ∃ H : Finset (Finset (Fin n)),
      H.IsBlockDesign 2 3 ∧ ∀ E ⊆ H,
        2 ≤ E.card → E.card ≤ g → E.card + 3 ≤ (E.biUnion id).card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/207.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/207.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/207.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/207.lean)
- [erdosproblems.com/207](https://www.erdosproblems.com/207)
