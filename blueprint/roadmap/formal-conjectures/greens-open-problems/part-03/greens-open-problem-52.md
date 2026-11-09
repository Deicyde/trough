---
declaration: theorem
origin: cited
lean: Green52.green_52, Green52.green_52_log
statement: formalized
---

# Green's Open Problem 52

> *Reference:* [Green's Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.52)

*Quoted from [FormalConjectures/GreensOpenProblems/52.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/52.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Green52.green_52`

Open: stated without proof.

> Suppose that $A \subset \mathbb{F}_2^n$ is a set with an additive complement of size $K$.
> Does $2A$ contain a coset of codimension $O_K(1)$?

```lean
theorem green_52 :
    ∃ (c : ℕ → ℕ), ∀ (n K : ℕ) (A : Set (𝔽₂ n)) (S : Finset (𝔽₂ n)),
      S.card = K → A + (S : Set (𝔽₂ n)) = Set.univ →
      ∃ (V : AffineSubspace (ZMod 2) (𝔽₂ n)), (V : Set (𝔽₂ n)) ⊆ A + A ∧
        n ≤ Module.finrank (ZMod 2) V.direction + c K
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/52.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/52.lean#L39).

## `Green52.green_52_log`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/green-52-log-counterexample/blob/16cb5d0/lean/Green52LogCounterexampleFC.lean#L661-L668](https://github.com/KitaKen1/green-52-log-counterexample/blob/16cb5d0/lean/Green52LogCounterexampleFC.lean#L661-L668).

> Could $2A$ even contain a coset of codimension $O(\log K)$?
>
> From [Green's 2025 update](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.52):
>
> > Update 2025. Kaave Hosseini and Ryan Alweiss have independently pointed out
> > that the second question is far too optimistic. To see this, let $A$ be a Hamming ball
> > of radius $n/2 - \sqrt{n}$. There is a set $S$ of size $O(n)$ such that
> > $A + S = \mathbb{F}_2^n$; a random choice of $S$ will work. However, every subspace
> > contained in $A - A$ has codimension $\gg \sqrt{n}$.

```lean
theorem green_52_log :
    ¬ ∃ (C D : ℝ), ∀ (n K : ℕ) (A : Set (𝔽₂ n)) (S : Finset (𝔽₂ n)),
      0 < K → S.card = K → A + (S : Set (𝔽₂ n)) = Set.univ →
      ∃ (V : AffineSubspace (ZMod 2) (𝔽₂ n)), (V : Set (𝔽₂ n)) ⊆ A + A ∧
        (n : ℝ) ≤ (Module.finrank (ZMod 2) V.direction : ℝ) + C * log (K : ℝ) + D
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/52.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/52.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/52.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/52.lean)
- [Green's Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.52)
