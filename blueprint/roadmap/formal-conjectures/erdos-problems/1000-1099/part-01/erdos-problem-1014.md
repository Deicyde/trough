---
declaration: theorem
origin: cited
lean: Erdos1014.erdos_1014, Erdos1014.erdos_1014.variants.upper_bound
statement: formalized
---

# Erdős Problem 1014

> *References:*
> - [erdosproblems.com/1014](https://www.erdosproblems.com/1014)
> - [Er71] Erdős, P., Some unsolved problems in graph theory and combinatorial analysis. Combinatorial
>   Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97-109.
> - [OpenAI26] *On the ratio of $R(k,\ell)$ and $R(k,\ell+1)$*, proof due to an internal model at
>   OpenAI (2026).
>   https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/Ramsey.pdf

*Quoted from [FormalConjectures/ErdosProblems/1014.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1014.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1014](https://www.erdosproblems.com/1014).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1014.erdos_1014`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1014.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1014.lean).

> Let $R(k,l)$ be the Ramsey number, so the minimal $n$ such that every graph on at least $n$
> vertices contains either a $K_k$ or an independent set on $l$ vertices.
>
> Prove, for fixed $k\geq 3$, that
>
> $$\lim_{l\to \infty}\frac{R(k,l+1)}{R(k,l)}=1.$$
>
> This has been
> [solved](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/Ramsey.pdf)
> by an internal model at OpenAI.

```lean
theorem erdos_1014 : ∀ k : ℕ, 3 ≤ k →
    Tendsto (fun l : ℕ ↦ (R(k, l + 1) : ℝ) / (R(k, l) : ℝ)) atTop (𝓝 1)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1014.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1014.lean#L55).

## `Erdos1014.erdos_1014.variants.upper_bound`

Solved: stated here without proof.

> That proof in fact shows that
>
> $$R(k,l+1)\leq (1+O(l^{-c/k^2}))R(k,l)$$
>
> for some constant $c>0$.

```lean
theorem erdos_1014.variants.upper_bound :
    ∃ c : ℝ, 0 < c ∧ ∀ k : ℕ, 3 ≤ k → ∃ C : ℝ, ∀ᶠ l : ℕ in atTop,
      (R(k, l + 1) : ℝ) ≤ (1 + C * (l : ℝ) ^ (-c / (k : ℝ) ^ 2)) * (R(k, l) : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1014.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1014.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1014.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1014.lean)
- [erdosproblems.com/1014](https://www.erdosproblems.com/1014)
