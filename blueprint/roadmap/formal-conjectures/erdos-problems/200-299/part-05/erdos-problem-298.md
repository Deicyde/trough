---
declaration: theorem
origin: cited
lean: Erdos298.erdos_298, Erdos298.erdos_298.variants.natural_density
statement: formalized
---

# Erdős Problem 298

> *References:*
> - [erdosproblems.com/298](https://www.erdosproblems.com/298)
> - [Bl21] Bloom, T. F., On a density conjecture about unit fractions. arXiv:2112.03726 (2021).

*Quoted from [FormalConjectures/ErdosProblems/298.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/298.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/298](https://www.erdosproblems.com/298).

The file states 2 research or textbook statements: 2 solved.

## `Erdos298.erdos_298`

Solved: stated here; a proof in another system is at [https://github.com/b-mehta/unit-fractions/blob/master/src/final_results.lean](https://github.com/b-mehta/unit-fractions/blob/master/src/final_results.lean).

> Does every set $A \subseteq \mathbb{N}$ of positive density contain some finite $S \subset A$ such that
> $\sum_{n \in S} \frac{1}{n} = 1$?
>
> The answer is yes, proved by Bloom [Bl21] (even if 'positive density' is interpreted as 'positive
> upper density', which is likely what Erdős intended).
>
> The theorem below uses the positive-upper-density interpretation; the literal natural-density
> interpretation is recorded separately.
>
> This was formalized in Lean 3 by Bloom and Mehta.

```lean
theorem erdos_298 : (∀ (A : Set ℕ), 0 ∉ A → 0 < A.upperDensity →
    ∃ (S : Finset ℕ), ↑S ⊆ A ∧ ∑ n ∈ S, (1 / n : ℚ) = 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/298.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/298.lean#L46).

## `Erdos298.erdos_298.variants.natural_density`

Solved: stated here without proof.

> The literal natural-density interpretation of Erdős Problem 298 follows from [Bl21].

```lean
theorem erdos_298.variants.natural_density : (∀ (A : Set ℕ), 0 ∉ A →
    A.HasPosDensity →
    ∃ (S : Finset ℕ), ↑S ⊆ A ∧ ∑ n ∈ S, (1 / n : ℚ) = 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/298.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/298.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/298.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/298.lean)
- [erdosproblems.com/298](https://www.erdosproblems.com/298)
