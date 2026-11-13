---
declaration: theorem
origin: cited
lean: Erdos760.erdos_760, Erdos760.erdos_760.variants.erdos_gimbel
statement: formalized
---

# Erdős Problem 760

> *References:*
> - [erdosproblems.com/760](https://www.erdosproblems.com/760)
> - [AKS97] Alon, Noga and Krivelevich, Michael and Sudakov, Benny, *Subgraphs with a large
>   cochromatic number*. J. Graph Theory (1997), 295-297.

*Quoted from [FormalConjectures/ErdosProblems/760.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/760.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/760](https://www.erdosproblems.com/760).

The file states 2 research or textbook statements: 2 solved.

## `Erdos760.erdos_760`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos760.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos760.lean).

> The cochromatic number of $G$, denoted by $\zeta(G)$, is the minimum number of colours needed to
> colour the vertices of $G$ such that each colour class induces either a complete graph or
> independent set.
>
> If $G$ is a graph with chromatic number $\chi(G)=m$ then must $G$ contain a subgraph $H$ with
>
> $$
> \zeta(H) \gg \frac{m}{\log m}?
> $$
>
> A problem of Erdős and Gimbel, who proved that there must exist a subgraph $H$ with
>
> $$
> \zeta(H) \gg \left(\frac{m}{\log m}\right)^{1/2}.
> $$
>
> The proposed bound would be best possible, as shown by taking $G$ to be a complete graph.
>
> The answer is yes, proved by Alon, Krivelevich, and Sudakov.

```lean
theorem erdos_760 :
    ∃ c > (0 : ℝ), ∀ (V : Type*) [Finite V] (G : SimpleGraph V) (m : ℕ),
      G.chromaticNumber = (m : ℕ∞) →
        ∃ H : G.Subgraph, ∃ k : ℕ, ((k : ℕ∞) ≤ H.coe.cochromaticNumber) ∧
          (c * (m : ℝ) / Real.log (m : ℝ) ≤ (k : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/760.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/760.lean#L53).

## `Erdos760.erdos_760.variants.erdos_gimbel`

Solved: stated here without proof.

> A problem of Erdős and Gimbel, who proved that there must exist a subgraph $H$ with
>
> $$
> \zeta(H) \gg \left(\frac{m}{\log m}\right)^{1/2}.
> $$

```lean
theorem erdos_760.variants.erdos_gimbel :
    ∃ c > (0 : ℝ), ∀ (V : Type*) [Finite V] (G : SimpleGraph V) (m : ℕ),
      G.chromaticNumber = (m : ℕ∞) →
        ∃ H : G.Subgraph, ∃ k : ℕ, ((k : ℕ∞) ≤ H.coe.cochromaticNumber) ∧
          (c * Real.sqrt ((m : ℝ) / Real.log (m : ℝ)) ≤ (k : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/760.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/760.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/760.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/760.lean)
- [erdosproblems.com/760](https://www.erdosproblems.com/760)
