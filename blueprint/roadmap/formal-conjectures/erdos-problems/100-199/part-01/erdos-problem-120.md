---
declaration: theorem
origin: cited
lean: Erdos120.erdos_120, Erdos120.erdos_120.variants.finite_set
statement: formalized
---

# Erdős Problem 120

> *Reference:*
> - [erdosproblems.com/120](https://www.erdosproblems.com/120)
> - [St20](http://matwbn.icm.edu.pl/ksiazki/fm/fm1/fm1111.pdf) Steinhaus, Hugo, Sur les distances des points dans les ensembles de measure positive. Fund. Math. (1920), 93-104.

*Quoted from [FormalConjectures/ErdosProblems/120.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/120.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/120](https://www.erdosproblems.com/120).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos120.erdos_120`

Open: stated without proof.

> Let $A \subseteq \mathbb{R}$ be an infinite set. Must there be a set $E \subseteq \mathbb{R}$
> of positive measure which does not contain any set of the shape $a * A + b$
> for some $a,b \in \mathbb{R}$ and $a \neq 0$?

```lean
theorem erdos_120 : ∀ A : Set ℝ, A.Infinite → Erdos120For A
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/120.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/120.lean#L48).

## `Erdos120.erdos_120.variants.finite_set`

Solved: stated here without proof.

> Steinhaus [St20] has proved Erdős 120 to be false whenever $A$ is a finite set.

```lean
theorem erdos_120.variants.finite_set {A : Set ℝ} (h : A.Finite) : ¬ Erdos120For A
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/120.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/120.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/120.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/120.lean)
- [erdosproblems.com/120](https://www.erdosproblems.com/120)
