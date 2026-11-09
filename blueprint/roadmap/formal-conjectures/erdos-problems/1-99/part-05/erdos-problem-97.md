---
declaration: theorem
origin: cited
lean: Erdos97.erdos_97, Erdos97.erdos_97.variants.three_equidistant, Erdos97.erdos_97.variants.k_equidistant, Erdos97.erdos_97.variants.three_unit_distance, Erdos97.erdos_97.variants.three_unit_distance_cut_min
statement: formalized
---

# Erdős Problem 97

> *Reference:* [erdosproblems.com/97](https://www.erdosproblems.com/97)

*Quoted from [FormalConjectures/ErdosProblems/97.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/97.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/97](https://www.erdosproblems.com/97).

The file states 5 research or textbook statements: 2 open and 3 solved.

## `Erdos97.erdos_97`

Open: stated without proof.

> Does every convex polygon have a vertex with no other 4 vertices equidistant from it?

```lean
theorem erdos_97 :
    ∀ A : Finset ℝ², A.Nonempty → ConvexIndep A → ¬HasNEquidistantProperty 4 A
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/97.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/97.lean#L79).

## `Erdos97.erdos_97.variants.three_equidistant`

Solved: stated here without proof.

> Erdős originally conjectured this (in [Er46b]) with no 3 vertices equidistant,
> but Danzer found a convex polygon on 9 points such that every vertex has three
> vertices equidistant from it (but this distance depends on the vertex).
> Danzer's construction is explained in [Er87b].
>
> [Er46b] Erdős, P., _On sets of distances of $n$ points_. Amer. Math. Monthly (1946), 248-250.
> [Er87b] Erdős, P., _Some combinatorial and metric problems in geometry_. Intuitive geometry (Siófok, 1985), 167-177.

```lean
theorem erdos_97.variants.three_equidistant :
    ∃ A : Finset ℝ², A.Nonempty ∧ ConvexIndep A ∧ HasNEquidistantProperty 3 A
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/97.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/97.lean#L93).

## `Erdos97.erdos_97.variants.k_equidistant`

Open: stated without proof.

> Erdős also conjectured that there is a $k$ for which every convex polygon has a vertex
> with no other $k$ vertices equidistant from it.

```lean
theorem erdos_97.variants.k_equidistant :
    ∃ k : ℕ, ∀ A : Finset ℝ², A.Nonempty → ConvexIndep A → ¬HasNEquidistantProperty k A
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/97.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/97.lean#L112).

## `Erdos97.erdos_97.variants.three_unit_distance`

Solved: stated here without proof.

> Fishburn and Reeds [FiRe92] have found a convex polygon on 20 points such that
> every vertex has three vertices equidistant from it (and this distance is the same for all vertices).
>
> [FiRe92] Fishburn, P. C. and Reeds, J. A., _Unit distances between vertices of a convex polygon_. Comput. Geom. (1992), 81-91.

```lean
theorem erdos_97.variants.three_unit_distance :
    ∃ A : Finset ℝ², A.Nonempty ∧ ConvexIndep A ∧ HasNUnitDistanceProperty 3 A
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/97.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/97.lean#L123).

## `Erdos97.erdos_97.variants.three_unit_distance_cut_min`

Solved: stated here without proof.

> Fishburn and Reeds [FiRe92] also proved that the smallest $n$ for which there exists
> a convex $n$-gon and a cut $\{A, B\}$ of its vertices such that $|\{b \in B : d(a, b) = 1\}| ≥ 3$
> for all $a \in A$, and $|\{a \in A : d(a, b) = 1\}| ≥ 3$ for all $b \in B$, is $n = 20$.

```lean
theorem erdos_97.variants.three_unit_distance_cut_min :
    sInf {n : ℕ | ∃ (V : Finset ℝ²) (A B : Finset ℝ²),
      n = V.card ∧ ConvexIndep V ∧ A.Nonempty ∧ B.Nonempty ∧ IsCut V A B ∧
      HasNUnitDistancePointsOn 3 B A ∧ HasNUnitDistancePointsOn 3 A B} = 20
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/97.lean, line 140](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/97.lean#L140).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/97.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/97.lean)
- [erdosproblems.com/97](https://www.erdosproblems.com/97)
