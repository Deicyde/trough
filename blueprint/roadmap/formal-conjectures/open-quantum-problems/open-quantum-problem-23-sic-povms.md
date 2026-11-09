---
declaration: theorem
origin: cited
lean: OpenQuantumProblem23.hasSICPOVM_56, OpenQuantumProblem23.hasSICPOVM_58, OpenQuantumProblem23.hasSICPOVM_59, OpenQuantumProblem23.hasSICPOVM_60, OpenQuantumProblem23.hasSICPOVM_64, OpenQuantumProblem23.hasSICPOVM_68, OpenQuantumProblem23.hasSICPOVM_69, OpenQuantumProblem23.hasSICPOVM_70, OpenQuantumProblem23.hasSICPOVM_71, OpenQuantumProblem23.hasSICPOVM_72, OpenQuantumProblem23.hasSICPOVM_75, OpenQuantumProblem23.sicPOVMs
statement: formalized
---

# Open Quantum Problem 23: SIC-POVMs

> ## Mathematical problem
> The OQP page presents three increasingly strong formulations of this problem.
> In this file we formalize the first one, closest to the physics terminology:
> existence of a symmetric informationally complete POVM in every finite dimension.
>
> A SIC-POVM in dimension $d$ can be represented by a family of $d^2$ normalized
> vectors in $\mathbb{C}^d$ whose pairwise squared overlaps are all equal to
> $(d + 1)^{-1}$. We encode such a family as a map `Fin (d ^ 2) → StateVector d`.
>
> ## Background
> SIC-POVMs are a basic structure in finite-dimensional quantum information.
> They are closely related to equiangular lines, tight frames, quantum state
> reconstruction, and finite-dimensional measurement theory.
> The open problem asks whether such families exist in every dimension.
>
> ## What this file formalizes
> This file formalizes the existence problem for symmetric informationally complete
> POVMs through the predicate `HasSICPOVM d`.
>
> More precisely, it contains the following layers.
>
> ### Core API
> The main definitions formalized in this file are:
> - `StateVector d`: a state vector in `ℂ^d`;
> - `mkStateVector`: constructor from coordinates in the computational basis;
> - `IsNormalized ψ`: normalization predicate for a state vector;
> - `overlapSq φ ψ`: squared magnitude of the inner-product overlap;
> - `HasConstantOverlapSq c Φ`: constant pairwise squared-overlap condition;
> - `sicOverlapSq d`: the SIC overlap value `(d + 1)⁻¹`;
> - `IsSICFamily d Φ`: the predicate that a family of `d^2` vectors in `ℂ^d`
>   is a SIC family;
> - `HasSICPOVM d`: existence of a SIC family in dimension `d`.
>
> In addition, the file includes explicit witness families and convenient
> constructors used in the low-dimensional benchmark cases:
> - `vec2`, `vec3`;
> - `qubitSICFamily`;
> - `hesseFamily`;
> - `bb84Family`.
>
> ### Complete open conjecture
> The main open theorem is:
> - `sicPOVMs`, expressing the conjecture that for every `d ≥ 1`, there exists a
>   SIC-POVM in dimension `d`.
>
> ### Special cases
> The file also isolates several special cases:
> - solved low-dimensional benchmark cases:
>   `hasSICPOVM_zero`, `hasSICPOVM_one`, `hasSICPOVM_two`, `hasSICPOVM_three`;
> - a negative benchmark result:
>   `bb84Family_not_isSICFamily`, showing that the BB84 family in dimension `2`
>   does not form a SIC family;
> - selected open benchmark dimensions:
>   `hasSICPOVM_56`, `hasSICPOVM_58`, `hasSICPOVM_59`, `hasSICPOVM_60`,
>   `hasSICPOVM_64`, `hasSICPOVM_68`, `hasSICPOVM_69`, `hasSICPOVM_70`,
>   `hasSICPOVM_71`, `hasSICPOVM_72`, `hasSICPOVM_75`.
>
> ### Test lemmas
> The file includes the following test lemmas and benchmark-support statements:
> - `hasConstantOverlapSq_singleton`;
> - `sicOverlapSq_one`, `sicOverlapSq_two`, `sicOverlapSq_three`,
>   `sicOverlapSq_pos`;
> - `isSICFamily_singleton_iff`, `isSICFamily_one_of_normalized`;
> - `qubitSICFamily_normalized`, `qubitSICFamily_pairwise`;
> - `hesseFamily_normalized`, `hesseFamily_pairwise`;
> - `bb84Family_normalized`.
>
> At present, these `@[category test, AMS 15 47 81]` results are included with
> placeholder proofs `by sorry`; they are intended to be proved in the next PR.
>
> ## References
> *Primary source list entry:*
> - IQOQI Vienna Open Quantum Problems, problem 23:
>   https://oqp.iqoqi.oeaw.ac.at/sic-povms-and-zauners-conjecture
> - Formal Conjectures issue #1823:
>   https://github.com/google-deepmind/formal-conjectures/issues/1823
>
> ### Foundational references
> - J. M. Renes, R. Blume-Kohout, A. J. Scott, and M. C. Caves,
>   *Symmetric informationally complete quantum measurements*,
>   J. Math. Phys. 45, 2171-2180 (2004), arXiv:quant-ph/0310075.
> - G. Zauner,
>   *Quantum Designs: Foundations of a Noncommutative Design Theory*,
>   PhD thesis, University of Vienna (1999).

*Quoted from [FormalConjectures/OpenQuantumProblems/23.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/23.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 12 research or textbook statements: 12 open. It also has 17 test statements, counted here but not shown.

## `OpenQuantumProblem23.hasSICPOVM_56`

Open: stated without proof.

> Benchmark open subproblem: existence of a SIC-POVM in dimension $56$.

```lean
theorem hasSICPOVM_56 : HasSICPOVM 56
```

Category `research open`; AMS [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [47 Operator theory](../by-subject/part-02/47-operator-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/OpenQuantumProblems/23.lean, line 320](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/23.lean#L320).

## `OpenQuantumProblem23.hasSICPOVM_58`

Open: stated without proof.

> Benchmark open subproblem: existence of a SIC-POVM in dimension $58$.

```lean
theorem hasSICPOVM_58 : HasSICPOVM 58
```

Category `research open`; AMS [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [47 Operator theory](../by-subject/part-02/47-operator-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/OpenQuantumProblems/23.lean, line 324](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/23.lean#L324).

## `OpenQuantumProblem23.hasSICPOVM_59`

Open: stated without proof.

> Benchmark open subproblem: existence of a SIC-POVM in dimension $59$.

```lean
theorem hasSICPOVM_59 : HasSICPOVM 59
```

Category `research open`; AMS [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [47 Operator theory](../by-subject/part-02/47-operator-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/OpenQuantumProblems/23.lean, line 328](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/23.lean#L328).

## `OpenQuantumProblem23.hasSICPOVM_60`

Open: stated without proof.

> Benchmark open subproblem: existence of a SIC-POVM in dimension $60$.

```lean
theorem hasSICPOVM_60 : HasSICPOVM 60
```

Category `research open`; AMS [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [47 Operator theory](../by-subject/part-02/47-operator-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/OpenQuantumProblems/23.lean, line 332](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/23.lean#L332).

## `OpenQuantumProblem23.hasSICPOVM_64`

Open: stated without proof.

> Benchmark open subproblem: existence of a SIC-POVM in dimension $64$.

```lean
theorem hasSICPOVM_64 : HasSICPOVM 64
```

Category `research open`; AMS [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [47 Operator theory](../by-subject/part-02/47-operator-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/OpenQuantumProblems/23.lean, line 336](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/23.lean#L336).

## `OpenQuantumProblem23.hasSICPOVM_68`

Open: stated without proof.

> Benchmark open subproblem: existence of a SIC-POVM in dimension $68$.

```lean
theorem hasSICPOVM_68 : HasSICPOVM 68
```

Category `research open`; AMS [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [47 Operator theory](../by-subject/part-02/47-operator-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/OpenQuantumProblems/23.lean, line 340](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/23.lean#L340).

## `OpenQuantumProblem23.hasSICPOVM_69`

Open: stated without proof.

> Benchmark open subproblem: existence of a SIC-POVM in dimension $69$.

```lean
theorem hasSICPOVM_69 : HasSICPOVM 69
```

Category `research open`; AMS [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [47 Operator theory](../by-subject/part-02/47-operator-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/OpenQuantumProblems/23.lean, line 344](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/23.lean#L344).

## `OpenQuantumProblem23.hasSICPOVM_70`

Open: stated without proof.

> Benchmark open subproblem: existence of a SIC-POVM in dimension $70$.

```lean
theorem hasSICPOVM_70 : HasSICPOVM 70
```

Category `research open`; AMS [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [47 Operator theory](../by-subject/part-02/47-operator-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/OpenQuantumProblems/23.lean, line 348](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/23.lean#L348).

## `OpenQuantumProblem23.hasSICPOVM_71`

Open: stated without proof.

> Benchmark open subproblem: existence of a SIC-POVM in dimension $71$.

```lean
theorem hasSICPOVM_71 : HasSICPOVM 71
```

Category `research open`; AMS [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [47 Operator theory](../by-subject/part-02/47-operator-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/OpenQuantumProblems/23.lean, line 352](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/23.lean#L352).

## `OpenQuantumProblem23.hasSICPOVM_72`

Open: stated without proof.

> Benchmark open subproblem: existence of a SIC-POVM in dimension $72$.

```lean
theorem hasSICPOVM_72 : HasSICPOVM 72
```

Category `research open`; AMS [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [47 Operator theory](../by-subject/part-02/47-operator-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/OpenQuantumProblems/23.lean, line 356](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/23.lean#L356).

## `OpenQuantumProblem23.hasSICPOVM_75`

Open: stated without proof.

> Benchmark open subproblem: existence of a SIC-POVM in dimension $75$.

```lean
theorem hasSICPOVM_75 : HasSICPOVM 75
```

Category `research open`; AMS [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [47 Operator theory](../by-subject/part-02/47-operator-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/OpenQuantumProblems/23.lean, line 360](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/23.lean#L360).

## `OpenQuantumProblem23.sicPOVMs`

Open: stated without proof.

> Do SIC-POVMs exist in every finite dimension?

```lean
theorem sicPOVMs :
    ∀ d : ℕ, 1 ≤ d → HasSICPOVM d
```

Category `research open`; AMS [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [47 Operator theory](../by-subject/part-02/47-operator-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md). Declared in [FormalConjectures/OpenQuantumProblems/23.lean, line 366](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/23.lean#L366).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OpenQuantumProblems/23.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/23.lean)
- [https://oqp.iqoqi.oeaw.ac.at/sic-povms-and-zauners-conjecture](https://oqp.iqoqi.oeaw.ac.at/sic-povms-and-zauners-conjecture)
