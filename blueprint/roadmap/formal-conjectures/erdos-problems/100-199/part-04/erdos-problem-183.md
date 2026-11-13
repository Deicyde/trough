---
declaration: theorem
origin: cited
lean: Erdos183.erdos_183, Erdos183.erdos_183.variants.explicit_lower_bound
statement: formalized
---

# Erdős Problem 183

> *References:*
> - [erdosproblems.com/183](https://www.erdosproblems.com/183)
> - [Er61] Erdős, P., *Graph theory and probability. II*. Canad. J. Math. (1961), 346-352.
> - [OpenAI26] OpenAI, *Ten advances in mathematics and theoretical computer science*. (2026).

*Quoted from [FormalConjectures/ErdosProblems/183.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/183.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/183](https://www.erdosproblems.com/183).

The file states 2 research or textbook statements: 2 solved.

## `Erdos183.erdos_183`

Solved: stated here; a Lean proof is at [https://github.com/openai/ten-proofs/blob/94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6/MulticolorTriangleRamsey.lean](https://github.com/openai/ten-proofs/blob/94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6/MulticolorTriangleRamsey.lean).

> Let $R(3;k)$ be the minimal $n$ such that if the edges of $K_n$ are coloured with $k$ colours
> then there must exist a monochromatic triangle. Determine
>
> $$\lim_{k\to \infty}R(3;k)^{1/k}.$$
>
> There is no finite limit: $R(3;k)^{1/k}\to\infty$. This was established by OpenAI [OpenAI26]
> along with the explicit superexponential lower bound in
> `erdos_183.variants.explicit_lower_bound`.

```lean
theorem erdos_183 :
    Tendsto (fun k : ℕ => (multicolourTriangleRamsey k : ℝ) ^ ((1 : ℝ) / (k : ℝ)))
      atTop atTop
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/183.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/183.lean#L59).

## `Erdos183.erdos_183.variants.explicit_lower_bound`

Solved: stated here; a Lean proof is at [https://github.com/openai/ten-proofs/blob/94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6/MulticolorTriangleRamsey.lean](https://github.com/openai/ten-proofs/blob/94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6/MulticolorTriangleRamsey.lean).

> The explicit bound behind `erdos_183`: for every $k\geq 2$,
>
> $$R(3;k)\geq \left(\frac{k^{1/3}}{6e^{38}\log k}\right)^k.$$

```lean
theorem erdos_183.variants.explicit_lower_bound :
    ∀ k : ℕ, 2 ≤ k →
      (((1 : ℝ) / (6 * Real.exp 38)) * (k : ℝ) ^ ((1 : ℝ) / 3) / Real.log (k : ℝ)) ^ k ≤
        (multicolourTriangleRamsey k : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/183.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/183.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/183.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/183.lean)
- [erdosproblems.com/183](https://www.erdosproblems.com/183)
