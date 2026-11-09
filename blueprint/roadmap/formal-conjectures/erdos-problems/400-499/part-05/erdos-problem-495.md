---
declaration: theorem
origin: cited
lean: Erdos495.erdos_495
statement: formalized
---

# Erdős Problem 495

> *Reference:* [erdosproblems.com/495](https://www.erdosproblems.com/495)

*Quoted from [FormalConjectures/ErdosProblems/495.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/495.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/495](https://www.erdosproblems.com/495).

The file states 1 research or textbook statement: 1 open.

## `Erdos495.erdos_495`

Open: stated without proof.

> Let $\alpha,\beta \in \mathbb{R}$. Is it true that$$\liminf_{n\to \infty} n \| n\alpha \|
>   \| n\beta\| =0$$? This is also known as the Littlewood conjecture.

```lean
theorem erdos_495 : ∀ α β : ℝ, liminf (fun n : ℕ ↦ (n : ℝ) * distToNearestInt (n * α)
  * distToNearestInt (n * β)) atTop = 0
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/495.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/495.lean#L37).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/495.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/495.lean)
- [erdosproblems.com/495](https://www.erdosproblems.com/495)
