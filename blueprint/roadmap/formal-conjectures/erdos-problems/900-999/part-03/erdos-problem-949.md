---
declaration: theorem
origin: cited
lean: Erdos949.erdos_949, Erdos949.erdos_949.variants.sidon
statement: formalized
---

# Erdős Problem 949

> *Reference:* [erdosproblems.com/949](https://www.erdosproblems.com/949)

*Quoted from [FormalConjectures/ErdosProblems/949.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/949.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/949](https://www.erdosproblems.com/949).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos949.erdos_949`

Open: stated without proof.

> Let $S \subseteq \mathbb{R}$ be a set containing no solutions to $a + b = c$.
> Must there be a set $A \subseteq \mathbb{R} \setminus S$ of cardinality continuum such that
> $A + A \subseteq \mathbb{R}\setminus S$?

```lean
theorem erdos_949 :
    ∀ S : Set ℝ, (∀ a ∈ S, ∀ b ∈ S, a + b ∉ S) → ∃ A ⊆ Sᶜ, #A = 𝔠 ∧ A + A ⊆ Sᶜ
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/949.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/949.lean#L40).

## `Erdos949.erdos_949.variants.sidon`

Proved here.

> Let $S\sub \mathbb{R}$ be a Sidon set. Must there be a set $A\sub \mathbb{R}∖S$ of cardinality
> continuum such that $A + A \sub \mathbb{R}∖S$?

```lean
theorem erdos_949.variants.sidon :
    ∀ S : Set ℝ, IsSidon S → ∃ A ⊆ Sᶜ, #A = 𝔠 ∧ A + A ⊆ Sᶜ
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/949.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/949.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/949.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/949.lean)
- [erdosproblems.com/949](https://www.erdosproblems.com/949)
