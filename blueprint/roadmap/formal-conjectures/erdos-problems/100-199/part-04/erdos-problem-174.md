---
declaration: theorem
origin: cited
lean: Erdos174.erdos_174, Erdos174.erdos_174.variants.spherical, Erdos174.erdos_174.variants.graham, Erdos174.erdos_174.variants.leader_russell_walters, Erdos174.erdos_174.variants.brick, Erdos174.erdos_174.variants.simplex, Erdos174.erdos_174.variants.trapezoid
statement: formalized
---

# Erdős Problem 174

> *References:*
> - [erdosproblems.com/174](https://www.erdosproblems.com/174)
> - [EGMRSS73] Erdős, P. and Graham, R. L. and Montgomery, P. and Rothschild, B. L. and Spencer,
>   J. and Straus, E. G., *Euclidean Ramsey Theorems I*. J. Comb. Th. A (1973), 341-363.
>   [PDF](https://www.renyi.hu/~p_erdos/1973-08.pdf)
> - [Er75f] Erdős, Paul, *On some problems of elementary and combinatorial geometry*. Ann. Mat. Pura
>   Appl. (4) (1975), 99-108. [PDF](https://www.renyi.hu/~p_erdos/1975-25.pdf)
> - [FrRo90] Frankl, P. and Rödl, V., *A partition property of simplices in Euclidean space*.
>   J. Amer. Math. Soc. (1990), 1-7.
> - [Kr92] Kříž, Igor, *All trapezoids are Ramsey*. Discrete Math. (1992), 59-62.
> - [LRW12] Leader, Imre and Russell, Paul A. and Walters, Mark, *Transitive sets in Euclidean
>   Ramsey theory*. J. Combin. Theory Ser. A (2012), 382-396.
>   [arXiv:1012.1350](https://arxiv.org/abs/1012.1350)

*Quoted from [FormalConjectures/ErdosProblems/174.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/174.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/174](https://www.erdosproblems.com/174).

The file states 7 research or textbook statements: 3 open and 4 solved. It also has 1 test statement, counted here but not shown.

## `Erdos174.erdos_174`

Open: stated without proof.

> A finite set $A\subset \mathbb{R}^n$ is called Ramsey if, for any $k\geq 1$, there exists some
> $d=d(A,k)$ such that in any $k$-colouring of $\mathbb{R}^d$ there exists a monochromatic copy
> of $A$. Characterise the Ramsey sets in $\mathbb{R}^n$.
>
> A copy of $A$ is a set congruent to $A$, as in [EGMRSS73, p. 344].

```lean
theorem erdos_174 (n : ℕ) :
    {A : Set (EuclideanSpace ℝ (Fin n)) | IsRamsey A} = erdos_174.answer n
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/174.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/174.lean#L80).

## `Erdos174.erdos_174.variants.spherical`

Solved: stated here without proof.

> Erdős, Graham, Montgomery, Rothschild, Spencer, and Straus [EGMRSS73] proved that every Ramsey
> set is 'spherical': it lies on the surface of some sphere.

```lean
theorem erdos_174.variants.spherical {n : ℕ} (A : Set (EuclideanSpace ℝ (Fin n)))
    (hA : IsRamsey A) : EuclideanGeometry.Cospherical A
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/174.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/174.lean#L89).

## `Erdos174.erdos_174.variants.graham`

Open: stated without proof.

> Graham has conjectured that every spherical set is Ramsey.

```lean
theorem erdos_174.variants.graham {n : ℕ} (A : Set (EuclideanSpace ℝ (Fin n)))
    (hA : A.Finite) (hs : EuclideanGeometry.Cospherical A) : IsRamsey A
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/174.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/174.lean#L97).

## `Erdos174.erdos_174.variants.leader_russell_walters`

Open: stated without proof.

> Leader, Russell, and Walters [LRW12] have alternatively conjectured that a set is Ramsey if and
> only if it is 'subtransitive': it can be embedded in some higher-dimensional set on which
> rotations act transitively.
>
> We use the definition of [LRW12]: a subset of a finite set whose symmetry group acts
> transitively.

```lean
theorem erdos_174.variants.leader_russell_walters {n : ℕ}
    (A : Set (EuclideanSpace ℝ (Fin n))) (hA : A.Finite) :
    IsRamsey A ↔ IsSubtransitive A
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/174.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/174.lean#L110).

## `Erdos174.erdos_174.variants.brick`

Solved: stated here without proof.

> Sets known to be Ramsey include vertices of $k$-dimensional rectangles [EGMRSS73].
>
> This is the case of the vertices `{x | ∀ i, x i = 0 ∨ x i = a i}` of a rectangular
> parallelepiped [EGMRSS73, Cor. 21]; some $a_i$ may be $0$ [EGMRSS73, Cor. 22].

```lean
theorem erdos_174.variants.brick {n : ℕ} (a : Fin n → ℝ) :
    IsRamsey {x : EuclideanSpace ℝ (Fin n) | ∀ i, x i = 0 ∨ x i = a i}
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/174.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/174.lean#L122).

## `Erdos174.erdos_174.variants.simplex`

Solved: stated here without proof.

> Sets known to be Ramsey include non-degenerate simplices [FrRo90].
>
> A non-degenerate simplex is a set of affinely independent points.

```lean
theorem erdos_174.variants.simplex {n : ℕ} (A : Set (EuclideanSpace ℝ (Fin n)))
    (hA : AffineIndependent ℝ (Subtype.val : A → EuclideanSpace ℝ (Fin n))) :
    IsRamsey A
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/174.lean, line 132](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/174.lean#L132).

## `Erdos174.erdos_174.variants.trapezoid`

Solved: stated here without proof.

> Sets known to be Ramsey include trapezoids [Kr92].
>
> We state it for isosceles trapezoids with vertices $(\pm s, 0)$ and $(\pm t, h)$, $h\neq 0$.
> A trapezoid that is not isosceles is not spherical, so it is not Ramsey by [EGMRSS73].

```lean
theorem erdos_174.variants.trapezoid (s t h : ℝ) (hh : h ≠ 0) :
    IsRamsey ({!₂[-s, 0], !₂[s, 0], !₂[-t, h], !₂[t, h]} :
      Set (EuclideanSpace ℝ (Fin 2)))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/174.lean, line 144](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/174.lean#L144).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/174.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/174.lean)
- [erdosproblems.com/174](https://www.erdosproblems.com/174)
