---
declaration: theorem
origin: cited
lean: Erdos668.erdos_668.parts.i, Erdos668.erdos_668.parts.ii, Erdos668.erdos_668.variants.four_points
statement: formalized
---

# Erdős Problem 668

> *References:*
> - [erdosproblems.com/668](https://www.erdosproblems.com/668)
> - [A385657](https://oeis.org/A385657)
> - [AMP25] B. Alexeev, D. Mixon, and H. Parshall, *The Erdős unit distance problem for small point
>   sets*. arXiv:2412.11914 (2025).
> - [EHSVZ25] P. Engel, O. Hammond-Lee, Y. Su, D. Varga, and P. Zsámboki, *Diverse beam search to
>   find densest-known planar unit distance graphs*. arXiv:2406.15317 (2025).
> - [Er97f] Erdős, Paul, *Some unsolved problems*. Combinatorics, geometry and probability
>   (Cambridge, 1993) (1997), 1-10.

*Quoted from [FormalConjectures/ErdosProblems/668.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/668.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/668](https://www.erdosproblems.com/668).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos668.erdos_668.parts.i`

Open: stated without proof.

> Is it true that the number of incongruent sets of $n$ points in $\mathbb{R}^2$ which maximise the
> number of unit distances tends to infinity as $n\to\infty$?
>
> The actual maximal number of unit distances is the subject of
> [Erdős Problem 90](https://www.erdosproblems.com/90).
>
> Two sets of points are congruent if an isometry of the plane maps one onto the other.

```lean
theorem erdos_668.parts.i :
    ∀ m : ℕ, ∀ᶠ n in atTop, ∃ A : Fin m → Finset ℝ²,
      (∀ i, (A i).card = n ∧ unitDistNum (A i) = maxUnitDistances n) ∧
      ∀ i j, i ≠ j → ¬ ∃ f : ℝ² ≃ᵢ ℝ², f '' A i = A j
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/668.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/668.lean#L54).

## `Erdos668.erdos_668.parts.ii`

Solved: stated here without proof.

> Is it always $>1$ for $n>3$?
>
> In fact this is $=1$ also for $n=4$, the unique example given by two equilateral triangles joined
> by an edge.
>
> Computational evidence of Engel, Hammond-Lee, Su, Varga, and Zsámboki [EHSVZ25] and Alexeev,
> Mixon, and Parshall [AMP25] suggests that this count is $=1$ for various other $5\leq n\leq 21$
> (although these calculations were checking only up to graph isomorphism, rather than
> congruency).

```lean
theorem erdos_668.parts.ii :
    ¬ ∀ n : ℕ, 3 < n → ∃ A B : Finset ℝ², A.card = n ∧ B.card = n ∧
      unitDistNum A = maxUnitDistances n ∧ unitDistNum B = maxUnitDistances n ∧
      ¬ ∃ f : ℝ² ≃ᵢ ℝ², f '' A = B
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/668.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/668.lean#L72).

## `Erdos668.erdos_668.variants.four_points`

Solved: stated here without proof.

> For $n=4$ there is, up to congruence, exactly one set of points in $\mathbb{R}^2$ which maximises
> the number of unit distances: two unit equilateral triangles $abc$ and $bcd$ joined by the edge
> $bc$, with $a\neq d$.

```lean
theorem erdos_668.variants.four_points :
    ∃ a b c d : ℝ², dist a b = 1 ∧ dist a c = 1 ∧ dist b c = 1 ∧ dist b d = 1 ∧ dist c d = 1 ∧
      ({a, b, c, d} : Finset ℝ²).card = 4 ∧
      ∀ B : Finset ℝ², B.card = 4 →
        (unitDistNum B = maxUnitDistances 4 ↔ ∃ f : ℝ² ≃ᵢ ℝ², f '' {a, b, c, d} = B)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/668.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/668.lean#L84).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/668.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/668.lean)
- [erdosproblems.com/668](https://www.erdosproblems.com/668)
