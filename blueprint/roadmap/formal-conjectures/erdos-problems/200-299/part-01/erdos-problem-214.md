---
declaration: theorem
origin: cited
lean: Erdos214.erdos_214, Erdos214.erdos_214.variants.juhasz, Erdos214.erdos_214.variants.egmrss, Erdos214.erdos_214.variants.juhasz_twelve_points, Erdos214.erdos_214.variants.csizmadia_toth, Erdos214.erdos_214.variants.bounds
statement: formalized
---

# Erdős Problem 214

> *References:*
> - [erdosproblems.com/214](https://www.erdosproblems.com/214)
> - [CsTo94] Csizmadia, György and Tóth, Géza, *Note on a Ramsey-type problem in geometry*.
>   J. Combin. Theory Ser. A (1994), 302-306.
> - [EGMRSS75] Erdős, P. and Graham, R. L. and Montgomery, P. and Rothschild, B. L. and Spencer, J.
>   and Straus, E. G., *Euclidean Ramsey theorems. II*. (1975), 529-557.
> - [Ju79] Juhász, Rozália, *Ramsey type theorems in the plane*. J. Combin. Theory Ser. A (1979),
>   152-160.

*Quoted from [FormalConjectures/ErdosProblems/214.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/214.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/214](https://www.erdosproblems.com/214).

The file states 6 research or textbook statements: 6 solved.

## `Erdos214.erdos_214`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos214.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos214.lean).

> Let $S\subset \mathbb{R}^2$ be such that no two points in $S$ are distance $1$ apart. Must the
> complement of $S$ contain four points which form a unit square?
>
> The answer is yes, proved by Juhász [Ju79], who proved more generally that the complement of $S$
> must contain a congruent copy of any set of four points.

```lean
theorem erdos_214 :
    ∀ S : Set ℝ², UnitDistanceAvoiding S →
      ∃ p : Fin 4 → ℝ², (∀ i, p i ∈ Sᶜ) ∧ (p ≅ unitSquare)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/214.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/214.lean#L65).

## `Erdos214.erdos_214.variants.juhasz`

Solved: stated here without proof.

> The answer is yes, proved by Juhász [Ju79], who proved more generally that the complement of $S$
> must contain a congruent copy of any set of four points.

```lean
theorem erdos_214.variants.juhasz : HasRedCopies 4
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/214.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/214.lean#L75).

## `Erdos214.erdos_214.variants.egmrss`

Solved: stated here without proof.

> Erdős, Graham, Montgomery, Rothschild, Spencer, and Straus [EGMRSS75] had earlier showed that
> $3\leq k\leq 10^{12}$.

```lean
theorem erdos_214.variants.egmrss : 3 ≤ k ∧ k ≤ 10 ^ 12
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/214.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/214.lean#L83).

## `Erdos214.erdos_214.variants.juhasz_twelve_points`

Solved: stated here without proof.

> Juhász [Ju79] also improved the upper bound to $k\leq 11$.

```lean
theorem erdos_214.variants.juhasz_twelve_points : ¬ HasRedCopies 12
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/214.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/214.lean#L90).

## `Erdos214.erdos_214.variants.csizmadia_toth`

Solved: stated here without proof.

> The upper bound was improved further by Csizmadia and Tóth [CsTo94] to $k\leq 7$.

```lean
theorem erdos_214.variants.csizmadia_toth : ¬ HasRedCopies 8
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/214.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/214.lean#L97).

## `Erdos214.erdos_214.variants.bounds`

Solved: stated here without proof.

> The best known bounds currently are
>
> $$4\leq k\leq 7.$$

```lean
theorem erdos_214.variants.bounds : 4 ≤ k ∧ k ≤ 7
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/214.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/214.lean#L105).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/214.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/214.lean)
- [erdosproblems.com/214](https://www.erdosproblems.com/214)
