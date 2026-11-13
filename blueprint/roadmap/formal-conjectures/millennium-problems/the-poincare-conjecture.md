---
declaration: theorem
origin: cited
lean: PoincareConjecture.poincare_conjecture, PoincareConjecture.poincare_conjecture.variants.dimension_two, PoincareConjecture.poincare_conjecture.variants.dimension_ge_five, PoincareConjecture.poincare_conjecture.variants.dimension_four, PoincareConjecture.poincare_conjecture.variants.smooth_for_three, PoincareConjecture.poincare_conjecture.variants.smooth_implication, PoincareConjecture.poincare_conjecture.variants.smooth_known_cases, PoincareConjecture.poincare_conjecture.variants.smooth_dimension_four, PoincareConjecture.poincare_conjecture.variants.smooth_other_cases
statement: formalized
---

# The Poincaré Conjecture

> References:
> - [Miln2022](https://www.claymath.org/wp-content/uploads/2022/06/poincare.pdf)
> - [Wang2017](https://annals.math.princeton.edu/2017/186-2/p03).
> - [mo296171](https://mathoverflow.net/questions/296171/unique-smooth-structure-on-3-manifolds)
> - [mathlib4](https://github.com/leanprover-community/mathlib4)
>
> The formalisations in this file are based on the ones written by Junyan Xu in Mathlib4.

*Quoted from [FormalConjectures/Millennium/Poincare.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/Poincare.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 9 research or textbook statements: 2 open, 2 solved and 5 textbook results.

## `PoincareConjecture.poincare_conjecture`

Solved: stated here without proof.

> The Millennium Problem, solved by Grigori Perelman in 2003: the Poincaré Conjecture holds.

```lean
theorem poincare_conjecture : ConjectureFor 3
```

Category `research solved`; AMS [54 General topology](../by-subject/part-02/54-general-topology/README.md), [57 Manifolds and cell complexes](../by-subject/part-02/57-manifolds-and-cell-complexes/README.md). Declared in [FormalConjectures/Millennium/Poincare.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/Poincare.lean#L52).

## `PoincareConjecture.poincare_conjecture.variants.dimension_two`

Textbook result, stated without proof.

> The Generalized Poincaré Conjecture holds for surfaces.

```lean
theorem poincare_conjecture.variants.dimension_two : ConjectureFor 2
```

Category `textbook`; AMS [54 General topology](../by-subject/part-02/54-general-topology/README.md), [57 Manifolds and cell complexes](../by-subject/part-02/57-manifolds-and-cell-complexes/README.md). Declared in [FormalConjectures/Millennium/Poincare.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/Poincare.lean#L59).

## `PoincareConjecture.poincare_conjecture.variants.dimension_ge_five`

Textbook result, stated without proof.

> The Generalized Poincaré Conjecture holds for dimensions at least 5.

```lean
theorem poincare_conjecture.variants.dimension_ge_five (n : ℕ) (hn : 5 ≤ n) : ConjectureFor n
```

Category `textbook`; AMS [54 General topology](../by-subject/part-02/54-general-topology/README.md), [57 Manifolds and cell complexes](../by-subject/part-02/57-manifolds-and-cell-complexes/README.md). Declared in [FormalConjectures/Millennium/Poincare.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/Poincare.lean#L66).

## `PoincareConjecture.poincare_conjecture.variants.dimension_four`

Textbook result, stated without proof.

> The Generalized Poincaré Conjecture holds in dimension 4.

```lean
theorem poincare_conjecture.variants.dimension_four : ConjectureFor 4
```

Category `textbook`; AMS [54 General topology](../by-subject/part-02/54-general-topology/README.md), [57 Manifolds and cell complexes](../by-subject/part-02/57-manifolds-and-cell-complexes/README.md). Declared in [FormalConjectures/Millennium/Poincare.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/Poincare.lean#L73).

## `PoincareConjecture.poincare_conjecture.variants.smooth_for_three`

Textbook result, stated without proof.

> A reformulation of the Millennium Problem in terms of smooth 3-folds.

```lean
theorem poincare_conjecture.variants.smooth_for_three : SmoothConjectureFor 3
```

Category `textbook`; AMS [54 General topology](../by-subject/part-02/54-general-topology/README.md), [57 Manifolds and cell complexes](../by-subject/part-02/57-manifolds-and-cell-complexes/README.md). Declared in [FormalConjectures/Millennium/Poincare.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/Poincare.lean#L87).

## `PoincareConjecture.poincare_conjecture.variants.smooth_implication`

Textbook result, stated without proof.

> The smooth formulation of the Millennium Problem implies the general case. This follows from
> the fact that every topological 3-fold admits a smooth structure [mo296171].

```lean
theorem poincare_conjecture.variants.smooth_implication (H : SmoothConjectureFor 3) :
    ConjectureFor 3
```

Category `textbook`; AMS [54 General topology](../by-subject/part-02/54-general-topology/README.md), [57 Manifolds and cell complexes](../by-subject/part-02/57-manifolds-and-cell-complexes/README.md). Declared in [FormalConjectures/Millennium/Poincare.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/Poincare.lean#L93).

## `PoincareConjecture.poincare_conjecture.variants.smooth_known_cases`

Solved: stated here without proof.

> The smooth version of the Poincaré conjecture is known to hold in dimensions
> $1, 2, 3, 5, 6, 12, 56, 61$. See [Wang2017].

```lean
theorem poincare_conjecture.variants.smooth_known_cases (n : ℕ) (hn : n ∈ SmoothTrueValues) :
    SmoothConjectureFor n
```

Category `research solved`; AMS [54 General topology](../by-subject/part-02/54-general-topology/README.md), [57 Manifolds and cell complexes](../by-subject/part-02/57-manifolds-and-cell-complexes/README.md). Declared in [FormalConjectures/Millennium/Poincare.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/Poincare.lean#L103).

## `PoincareConjecture.poincare_conjecture.variants.smooth_dimension_four`

Open: stated without proof.

> The four dimensional case of the smooth version of the conjecture is still open.
> See [Wang2017].

```lean
theorem poincare_conjecture.variants.smooth_dimension_four : SmoothConjectureFor 4
```

Category `research open`; AMS [54 General topology](../by-subject/part-02/54-general-topology/README.md), [57 Manifolds and cell complexes](../by-subject/part-02/57-manifolds-and-cell-complexes/README.md). Declared in [FormalConjectures/Millennium/Poincare.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/Poincare.lean#L110).

## `PoincareConjecture.poincare_conjecture.variants.smooth_other_cases`

Open: stated without proof.

> It is conjectured that the only values of $n > 4$ for which the smooth version of the
> conjecture holds are $n = 5, 6, 12, 56, 61$. See Conjecture 1.17 in [Wang2017].

```lean
theorem poincare_conjecture.variants.smooth_other_cases (n : ℕ) (hn : n > 4)
    (hn' : n ∉ SmoothTrueValues) : ¬ SmoothConjectureFor n
```

Category `research open`; AMS [54 General topology](../by-subject/part-02/54-general-topology/README.md), [57 Manifolds and cell complexes](../by-subject/part-02/57-manifolds-and-cell-complexes/README.md). Declared in [FormalConjectures/Millennium/Poincare.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/Poincare.lean#L116).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Millennium/Poincare.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/Poincare.lean)
- [Miln2022](https://www.claymath.org/wp-content/uploads/2022/06/poincare.pdf)
