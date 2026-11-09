---
declaration: theorem
origin: cited
lean: Erdos354.erdos_354.parts.i, Erdos354.erdos_354.parts.ii
statement: formalized
---

# Erdős Problem 354

> *References:*
> - [erdosproblems.com/354](https://www.erdosproblems.com/354)
> - [YC26] Yingzhe Yu and Kani Chen, *Erdős Problem 354(i): Strong Completeness of Two
>   Dyadic Floor Sequences* (2026).
>   [Manuscript](https://github.com/Andrewyzzz/erdos354/blob/c735d9389a79a2aa20fc04103d8890dd330b531e/proof/FORMALIZED_PROOF.pdf)

*Quoted from [FormalConjectures/ErdosProblems/354.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/354.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/354](https://www.erdosproblems.com/354).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos354.erdos_354.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/Andrewyzzz/erdos354/blob/c735d9389a79a2aa20fc04103d8890dd330b531e/formalization/Dyadic354/UpstreamBridge.lean#L34](https://github.com/Andrewyzzz/erdos354/blob/c735d9389a79a2aa20fc04103d8890dd330b531e/formalization/Dyadic354/UpstreamBridge.lean#L34).

> Let $\alpha,\beta\in \mathbb{R}_{>0}$ such that $\alpha/\beta$ is irrational. Is the multiset
>
> $$\{ \lfloor \alpha\rfloor,\lfloor 2\alpha\rfloor,\lfloor 4\alpha\rfloor,\ldots\}\cup
> \{ \lfloor \beta\rfloor,\lfloor 2\beta\rfloor,\lfloor 4\beta\rfloor,\ldots\}$$
>
> complete?
>
> Yu and Chen [YC26] prove an affirmative answer. They also prove that the set of nonzero
> values remains complete after deletion of any finite set of values.

```lean
theorem erdos_354.parts.i : ∀ᵉ (α > 0) (β > 0), Irrational (α / β) →
    IsAddCompleteNatSeq' (FloorMultiples.interleave α β 2)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/354.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/354.lean#L53).

## `Erdos354.erdos_354.parts.ii`

Open: stated without proof.

> Let $\alpha,\beta\in \mathbb{R}_{>0}$ such that $\alpha/\beta$ is irrational. Is
>
> $$\{ \lfloor \alpha\rfloor,\lfloor \gamma\alpha\rfloor,\lfloor \gamma^2\alpha\rfloor,\ldots\}\cup
> \{ \lfloor \beta\rfloor,\lfloor \gamma\beta\rfloor,\lfloor \gamma^2\beta\rfloor,\ldots\}$$
>
> complete?

```lean
theorem erdos_354.parts.ii : ∃ γ ∈ Set.Ioo (1 : ℝ) 2, ∀ᵉ (α > 0) (β > 0), Irrational (α / β) →
    IsAddCompleteNatSeq' (FloorMultiples.interleave α β γ)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/354.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/354.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/354.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/354.lean)
- [erdosproblems.com/354](https://www.erdosproblems.com/354)
