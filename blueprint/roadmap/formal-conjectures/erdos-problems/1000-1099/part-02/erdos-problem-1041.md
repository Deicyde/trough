---
declaration: theorem
origin: cited
lean: Erdos1041.exists_connected_component_contains_two_roots, Erdos1041.erdos_1041
statement: formalized
---

# Erdős Problem 1041

> *Reference:* [erdosproblems.com/1041](https://www.erdosproblems.com/1041)

*Quoted from [FormalConjectures/ErdosProblems/1041.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1041.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1041](https://www.erdosproblems.com/1041).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1041.exists_connected_component_contains_two_roots`

Solved: stated here without proof.

> **Erdős–Herzog–Piranian Component Lemma** (Metric Properties of Polynomials, 1958):
> If $f$ is a monic degree $n$ polynomial with all roots in the unit disk,
> then some connected component
> of $\{z \mid |f(z)| < 1\}$ contains at least two roots with multiplicity.
>
> See p. 139, above Problem 5:
> [EHP58] Erdős, P. and Herzog, F. and Piranian, G., _Metric properties of polynomials_.
>   J. Analyse Math. (1958), 125-148.

```lean
theorem exists_connected_component_contains_two_roots :
    ∃ C, C ⊆ {z | ‖f.eval z‖ < 1} ∧ IsConnected C ∧
      2 ≤ (f.roots.filter (· ∈ C)).card
```

Category `research solved`; AMS [32 Several complex variables and analytic spaces](../../../by-subject/part-01/32-several-complex-variables-and-analytic-spaces/README.md). Declared in [FormalConjectures/ErdosProblems/1041.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1041.lean#L57).

## `Erdos1041.erdos_1041`

Solved: stated here; a Lean proof is at [https://github.com/wcook04/plectis-erdos-lean/blob/587c48f213106c20ba2cdf3d585700c1394fc44f/verification/FC1041HausdorffCounterexample/lean/ErdosProblems/Erdos1041/Counterexample/HausdorffLength.lean#L449-L454](https://github.com/wcook04/plectis-erdos-lean/blob/587c48f213106c20ba2cdf3d585700c1394fc44f/verification/FC1041HausdorffCounterexample/lean/ErdosProblems/Erdos1041/Counterexample/HausdorffLength.lean#L449-L454).

> Let
>
> $$ f(z) = \prod_{i=1}^{n} (z - z_i) \in \mathbb{C}[x] $$
>
> with $|z_i| < 1$ for all $i$.
>
> Conjecture: Must there always exist a path of length less than 2 in
>
> $$ \{ z \in \mathbb{C} \mid |f(z)| < 1 \} $$
>
> which connects two of the roots of $f$?
>
> The answer is negative. ani gave a counterexample of degree seven on the
> [Erdős problems forum](https://www.erdosproblems.com/forum/thread/1041) on 7 September 2026.
> The linked formalisation proves, for the member $s = 10^{-6}$ of ani's family, that every
> connected subset of $\{ z \mid |f(z)| < 1 \}$ containing two distinct roots has
> one-dimensional Hausdorff measure greater than $2$.

```lean
theorem erdos_1041 :
    ¬ ∀ (n : ℕ) (f : ℂ[X]), n ≥ 2 → f.natDegree = n → f.Monic →
      f.rootSet ℂ ⊆ Metric.ball 0 1 →
      ∃ (z₁ z₂ : ℂ) (h : ({z₁, z₂} : Multiset ℂ) ≤ f.roots) (γ : Path z₁ z₂),
        Set.range γ ⊆ { z : ℂ | ‖f.eval z‖ < 1 } ∧ length (Set.range γ) < 2
```

Category `research solved`; AMS [32 Several complex variables and analytic spaces](../../../by-subject/part-01/32-several-complex-variables-and-analytic-spaces/README.md). Declared in [FormalConjectures/ErdosProblems/1041.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1041.lean#L82).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1041.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1041.lean)
- [erdosproblems.com/1041](https://www.erdosproblems.com/1041)
