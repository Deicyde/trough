---
declaration: theorem
origin: cited
lean: Erdos51.erdos_51
statement: formalized
---

# Erdős Problem 51

> *Reference:* [erdosproblems.com/51](https://www.erdosproblems.com/51)

*Quoted from [FormalConjectures/ErdosProblems/51.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/51.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/51](https://www.erdosproblems.com/51).

The file states 1 research or textbook statement: 1 open.

## `Erdos51.erdos_51`

Open: stated without proof.

> Is there an infinite set $A \subset \mathbb{N}$ such that for every $a \in A$,
> there is an integer n such that $\phi(n)=a$, and
> yet if $n_a$ is the smallest such integer, then $\frac{n_a}{a} → \infty$ as $a → ∞$?

```lean
theorem erdos_51 : ∃ A : Set ℕ, ∃ n : A → ℕ,
      A.Infinite ∧
      (∀ a : A, IsLeast (φ ⁻¹' {(a : ℕ)}) (n a)) ∧
      Tendsto (fun a : A => (n a : ℝ) / (a : ℝ)) atTop atTop
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/51.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/51.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/51.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/51.lean)
- [erdosproblems.com/51](https://www.erdosproblems.com/51)
