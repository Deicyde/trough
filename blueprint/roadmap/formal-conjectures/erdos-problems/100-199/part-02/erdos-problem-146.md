---
declaration: theorem
origin: cited
lean: Erdos146.erdos_146, Erdos146.erdos_146.variants.two_degenerate_counterexample
statement: formalized
---

# Erdős Problem 146

> *References:*
> - [erdosproblems.com/146](https://www.erdosproblems.com/146)
> - [ErSi84] Erdős, P. and Simonovits, M., *Cube-supersaturated graphs and related problems*.
>   Progress in graph theory (1984), 203-218.
> - [OpenAI26] OpenAI, *Ten advances in mathematics and theoretical computer science*. (2026).

*Quoted from [FormalConjectures/ErdosProblems/146.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/146.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/146](https://www.erdosproblems.com/146).

The file states 2 research or textbook statements: 2 solved.

## `Erdos146.erdos_146`

Solved: stated here without proof.

> If $H$ is bipartite and is $r$-degenerate, that is, every induced subgraph of $H$ has minimum
> degree $\leq r$, then
>
> $$\mathrm{ex}(n;H) \ll n^{2-1/r}.$$
>
> The answer is no. OpenAI [OpenAI26] give a connected bipartite `2`-degenerate `H` and constants
> `c, ε > 0` with $\mathrm{ex}(n;H)\geq cn^{3/2+\epsilon}$ for all large `n`, which exceeds the
> conjectured $n^{2-1/2}=n^{3/2}$. See `erdos_146.variants.two_degenerate_counterexample`.

```lean
theorem erdos_146 :
    ¬ ∀ (r q : ℕ) (H : SimpleGraph (Fin q)),
      0 < r → H.IsBipartite → H.IsDegenerate r →
        Asymptotics.IsBigO atTop
          (fun n : ℕ => (extremalNumber n H : ℝ))
          (fun n : ℕ => (n : ℝ) ^ ((2 : ℝ) - 1 / (r : ℝ)))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/146.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/146.lean#L46).

## `Erdos146.erdos_146.variants.two_degenerate_counterexample`

Solved: stated here; a Lean proof is at [https://github.com/openai/ten-proofs/blob/94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6/CompactnessAndDegeneracy.lean](https://github.com/openai/ten-proofs/blob/94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6/CompactnessAndDegeneracy.lean).

> The counterexample: a connected bipartite `2`-degenerate `H` whose extremal number exceeds
> $n^{3/2+\epsilon}$ infinitely often, so the `r = 2` case of `erdos_146` fails.

```lean
theorem erdos_146.variants.two_degenerate_counterexample :
    ∃ (q : ℕ) (H : SimpleGraph (Fin q)),
      H.Connected ∧ H.IsBipartite ∧ H.IsDegenerate 2 ∧
      ∃ c ε : ℝ, 0 < c ∧ 0 < ε ∧
        ∀ᶠ n : ℕ in atTop,
          c * (n : ℝ) ^ ((3 : ℝ) / 2 + ε) ≤ (extremalNumber n H : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/146.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/146.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/146.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/146.lean)
- [erdosproblems.com/146](https://www.erdosproblems.com/146)
