---
declaration: theorem
origin: cited
lean: Erdos28.erdos_28
statement: formalized
---

# Erdős Problem 28

> *Reference:* [erdosproblems.com/28](https://www.erdosproblems.com/28)

*Quoted from [FormalConjectures/ErdosProblems/28.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/28.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/28](https://www.erdosproblems.com/28).

The file states 1 research or textbook statement: 1 open.

## `Erdos28.erdos_28`

Open: stated without proof.

> If $A ⊆ \mathbb{N}$ is such that $A + A$ contains all but finitely many integers then
>  $\limsup 1_A ∗ 1_A(n) = \infty$.

```lean
theorem erdos_28 (A : Set ℕ) (h : (A + A)ᶜ.Finite) :
    limsup (fun (n : ℕ) => (sumRep A n : ℕ∞)) atTop = (⊤ : ℕ∞)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/28.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/28.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/28.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/28.lean)
- [erdosproblems.com/28](https://www.erdosproblems.com/28)
