---
declaration: theorem
origin: cited
lean: Green60.green_60
statement: formalized
---

# Ben Green's Open Problem 60

> *Reference:* [Ben Green's Open Problem 60](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.8 Problem 60)

*Quoted from [FormalConjectures/GreensOpenProblems/60.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/60.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Green60.green_60`

Open: stated without proof.

> Is there an absolute constant $c > 0$ such that, whenever $A ⊆ \mathbb{N}$ is a set of squares
> with $|A| ≥ 2$, the sumset $A + A$ satisfies $|A + A| ≥ |A|^{1 + c}$?

```lean
theorem green_60 :
    ∃ c > (0 : ℝ),
      ∀ (A : Finset ℕ),
        (∀ a ∈ A, IsSquare a) →
        2 ≤ A.card →
          ((A + A).card : ℝ) ≥ (A.card : ℝ) ^ (1 + c)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/60.lean, line 36](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/60.lean#L36).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/60.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/60.lean)
- [https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.8](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.8)
