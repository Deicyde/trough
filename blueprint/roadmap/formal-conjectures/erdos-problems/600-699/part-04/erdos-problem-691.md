---
declaration: theorem
origin: cited
lean: Erdos691.erdos_691
statement: formalized
---

# Erdős Problem 691

> *Reference:* [erdosproblems.com/691](https://www.erdosproblems.com/691)

*Quoted from [FormalConjectures/ErdosProblems/691.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/691.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/691](https://www.erdosproblems.com/691).

The file states 1 research or textbook statement: 1 open.

## `Erdos691.erdos_691`

Open: stated without proof.

> Given $A \subseteq \mathbb{N}$, let
> $M_A = \{n \geq 1 : a \mid n \text{ for some } a \in A\}$. Find a necessary and sufficient
> condition on $A$ for $M_A$ to have density $1$.

```lean
theorem erdos_691 :
    erdos_691.answer = fun A ↦ (multiples A).HasDensity 1
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/691.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/691.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/691.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/691.lean)
- [erdosproblems.com/691](https://www.erdosproblems.com/691)
