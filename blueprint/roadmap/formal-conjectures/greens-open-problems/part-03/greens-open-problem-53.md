---
declaration: theorem
origin: cited
lean: Green53.green_53
statement: formalized
---

# Green's Open Problem 53

> *References:*
> - [Gr24] [Green's Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.53)

*Quoted from [FormalConjectures/GreensOpenProblems/53.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/53.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Green53.green_53`

Open: stated without proof.

> Suppose that $\mathbb{F}_2^n$ is partitioned in to sets $A_1, ..., A_K$.
> Does $2A_i$ contain a coset of codimension $O_K(1)$ for some $i$?

```lean
theorem green_53 :
    ∃ (c : ℕ → ℕ), ∀ (n K : ℕ) (A : Fin K → Set (𝔽₂ n)),
      (⋃ i, A i) = Set.univ →
      Pairwise (Disjoint on A) →
      ∃ (i : Fin K) (S : AffineSubspace (ZMod 2) (𝔽₂ n)),
        (S : Set (𝔽₂ n)) ⊆ A i + A i ∧
        n ≤ Module.finrank (ZMod 2) S.direction + c K
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/53.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/53.lean#L40).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/53.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/53.lean)
- [Green's Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.53)
