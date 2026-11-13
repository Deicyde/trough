---
declaration: theorem
origin: cited
lean: Erdos1043.erdos_1043, Erdos1043.erdos_1043.variants.weak
statement: formalized
---

# Erdős Problem 1043

> *References:*
> - [erdosproblems.com/1043](https://www.erdosproblems.com/1043)
> - [EHP58] Erdős, P. and Herzog, F. and Piranian, G., Metric properties of polynomials. J.
>   Analyse Math. (1958), 125-148.
> - [Po59] Pommerenke, Ch., On some problems by Erdős, Herzog and Piranian. Michigan Math. J.
>   (1959), 221-225.
> - [Po61] Pommerenke, Ch., On metric properties of complex polynomials. Michigan Math. J. (1961),
>   97-115.

*Quoted from [FormalConjectures/ErdosProblems/1043.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1043.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1043](https://www.erdosproblems.com/1043).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1043.erdos_1043`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos1043.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos1043.lean).

> **Erdős Problem 1043**:
> Let $f\in \mathbb{C}[x]$ be a monic polynomial.
> Must there exist a straight line $\ell$ such that the projection of
>
> $$\{ z: \lvert f(z)\rvert\leq 1\}$$
>
> onto $\ell$ has measure at most $2$?
>
> Pommerenke [Po61] proved that the answer is no.
>
> The projection onto the line $\ell = \mathbb{R} u$ is measured with the Lebesgue measure of that
> line, so `volume` of the projected set is its length.
>
> This was formalized in Lean by Alexeev using Aristotle.

```lean
theorem erdos_1043 :
    ¬ ∀ (f : ℂ[X]), f.Monic → f.degree ≥ 1 →
      ∃ (u : ℂ), ‖u‖ = 1 ∧
      volume ((ℝ ∙ u).orthogonalProjectionOnto '' levelSet f) ≤ 2
```

Category `research solved`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1043.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1043.lean#L60).

## `Erdos1043.erdos_1043.variants.weak`

Solved: stated here without proof.

> On the other hand, Pommerenke also proved there always exists a line such that the projection has
> measure at most 3.3.

```lean
theorem erdos_1043.variants.weak :
    ∀ (f : ℂ[X]), f.Monic → f.degree ≥ 1 →
      ∃ (u : ℂ), ‖u‖ = 1 ∧
      volume ((ℝ ∙ u).orthogonalProjectionOnto '' levelSet f) ≤ 3.3
```

Category `research solved`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1043.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1043.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1043.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1043.lean)
- [erdosproblems.com/1043](https://www.erdosproblems.com/1043)
