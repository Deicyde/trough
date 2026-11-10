---
declaration: theorem
origin: cited
lean: Green50.green_50
statement: formalized
---

# Ben Green's Open Problem 50

> Suppose that $A \subset \mathbb{F}_2^n$ is a set of density $\alpha$. Does $10A$ contain a coset
> of some subspace of dimension at least $n - O(\log(1/\alpha))$?
>
> Here $kA$ denotes the $k$-fold iterated sumset, i.e., the set of all sums of $k$ elements from $A$
> (with repetition allowed). In `Mathlib`, this is denoted `k • A` using pointwise scalar
> multiplication on sets.
>
> *Reference:* [Ben Green's Open Problem 50](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.6 Problem 50)

*Quoted from [FormalConjectures/GreensOpenProblems/50.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/50.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Green50.green_50`

Open: stated without proof.

> Let $A \subset \mathbb{F}_2^n$ be a set of density $\alpha > 0$. Does $10A$ contain a coset
> of some subspace of dimension at least $n - O(\log(1/\alpha))$?
>
> More precisely: does there exist an absolute constant $C > 0$ such that for all $n \geq 1$ and all
> nonempty $A \subseteq \mathbb{F}_2^n$ with density $\alpha > 0$, the sumset $10A$ contains a coset
> of some subspace of dimension at least $n - C \log_2(1/\alpha)$?
>
> The sumset $10A$ is defined as $\{a_1 + a_2 + \cdots + a_{10} : a_i \in A\}$, using the pointwise
> scalar multiplication notation `10 • A` where `•` denotes the iterated addition of a set.
>
> Note: We model $\mathbb{F}_2^n$ as `Fin n → ZMod 2`, which is an $n$-dimensional vector space
> over $\mathbb{F}_2$.

```lean
theorem green_50 :
    ∃ C > (0 : ℝ), ∀ n : ℕ, ∀ A : Finset (𝔽₂ n),
    A.Nonempty →
    let α : ℝ := A.dens
    ∃ (W : Submodule (ZMod 2) (𝔽₂ n)) (v : 𝔽₂ n),
      v +ᵥ (W : Set (𝔽₂ n)) ⊆ ↑(10 • A) ∧
      (n : ℝ) - C * Real.logb 2 (1 / α) ≤ Module.finrank (ZMod 2) W
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/50.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/50.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/50.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/50.lean)
- [https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.6](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.6)
