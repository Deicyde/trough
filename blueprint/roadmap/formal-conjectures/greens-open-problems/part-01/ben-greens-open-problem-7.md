---
declaration: theorem
origin: cited
lean: Green7.green_7.variants.positive_density
statement: formalized
---

# Ben Green's Open Problem 7

> Does Ulam's sequence have positive density?
> Can one explain the curious Fourier properties of Ulam's sequence?
>
> *References:*
> - [Ben Green's Open Problem 7](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.1)
> - [erdosproblems.com/342](https://www.erdosproblems.com/342)

*Quoted from [FormalConjectures/GreensOpenProblems/7.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/GreensOpenProblems/7.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Green7.green_7.variants.positive_density`

Open: stated without proof.

> Does Ulam's sequence have positive density?

```lean
theorem green_7.variants.positive_density :
    ∀ a : ℕ → ℕ, Erdos342.IsUlamSequence a →
      Set.upperDensity (Set.range a) > 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/GreensOpenProblems/7.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/GreensOpenProblems/7.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/7.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/GreensOpenProblems/7.lean)
- [Ben Green's Open Problem 7](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.1)
