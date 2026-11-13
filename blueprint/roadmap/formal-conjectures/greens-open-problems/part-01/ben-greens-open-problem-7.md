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

*Quoted from [FormalConjectures/GreensOpenProblems/7.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/7.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Green7.green_7.variants.positive_density`

Open: stated without proof.

> Does Ulam's sequence have positive density?

```lean
theorem green_7.variants.positive_density :
    ∀ a : ℕ → ℕ, Erdos342.IsUlamSequence a →
      Set.upperDensity (Set.range a) > 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/GreensOpenProblems/7.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/7.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/7.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/7.lean)
- [Ben Green's Open Problem 7](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.1)
