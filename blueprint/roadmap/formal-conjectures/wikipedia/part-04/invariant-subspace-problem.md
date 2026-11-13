---
declaration: theorem
origin: cited
lean: InvariantSubspaceProblem.Invariant_subspace_problem, InvariantSubspaceProblem.Invariant_subspace_problem_finite_dimensional, InvariantSubspaceProblem.Invariant_subspace_problem_non_separable, InvariantSubspaceProblem.Invariant_subspace_problem_normal_operator, InvariantSubspaceProblem.Invariant_subspace_problem_l1
statement: formalized
---

# Invariant Subspace Problem

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Invariant_subspace_problem),
> [Chalendar-Partington](https://arxiv.org/abs/2507.21834)

*Quoted from [FormalConjectures/Wikipedia/InvariantSubspaceProblem.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InvariantSubspaceProblem.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 1 open and 4 solved. It also has 1 API statement, counted here but not shown.

## `InvariantSubspaceProblem.Invariant_subspace_problem`

Open: stated without proof.

> Show that every bounded linear operator `T : H → H` on a separable Hilbert space `H` of dimension
> at least 2 has a non-trivial closed `T`-invariant subspace: a closed linear subspace `W` of `H`,
> which is different from `H` and from `{0}`, such that `T ( W ) ⊂ W`. One needs the assumption that
> the dimension of `H` is at least 2 because otherwise any subspace would be either `H` or `{0}`.

```lean
theorem Invariant_subspace_problem [InnerProductSpace ℂ H] [TopologicalSpace.SeparableSpace H]
    [CompleteSpace H] (hdim : 2 ≤ Module.rank ℂ H) (T : H →L[ℂ] H) :
    Nonempty (ClosedInvariantSubspace T)
```

Category `research open`; AMS [47 Operator theory](../../by-subject/part-02/47-operator-theory/README.md). Declared in [FormalConjectures/Wikipedia/InvariantSubspaceProblem.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InvariantSubspaceProblem.lean#L48).

## `InvariantSubspaceProblem.Invariant_subspace_problem_finite_dimensional`

Proved here.

> Every (bounded) linear operator `T : H → H` on a finite-dimensional normed space `H` of dimension
> at least 2 has a non-trivial (closed) `T`-invariant subspace. Since `ℂ` is algebraically closed,
> `T` has an eigenvector `v ≠ 0`, and the line `ℂ ∙ v` is such a subspace.
>
> `H` is a complex normed space: with a bare `Module ℂ H` unrelated to the norm, finite-dimensional
> subspaces need not be closed, and the statement fails already in complex dimension `2`.

```lean
theorem Invariant_subspace_problem_finite_dimensional [NormedSpace ℂ H] (h : FiniteDimensional ℂ H)
    (hdim : 2 ≤ Module.rank ℂ H) (T : H →L[ℂ] H) : Nonempty (ClosedInvariantSubspace T)
```

Category `research solved`; AMS [47 Operator theory](../../by-subject/part-02/47-operator-theory/README.md). Declared in [FormalConjectures/Wikipedia/InvariantSubspaceProblem.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InvariantSubspaceProblem.lean#L61).

## `InvariantSubspaceProblem.Invariant_subspace_problem_non_separable`

Proved here.

> Every bounded linear operator `T : H → H` on a non-separable Hilbert space `H` has a
> non-trivial closed `T`-invariant subspace. Such an invariant space is given by considering the
> closure of the linear span of the orbit of any single non-zero vector.

```lean
theorem Invariant_subspace_problem_non_separable [InnerProductSpace ℂ H] [CompleteSpace H]
    (h : ¬TopologicalSpace.SeparableSpace H) (T : H →L[ℂ] H) :
    Nonempty (ClosedInvariantSubspace T)
```

Category `research solved`; AMS [47 Operator theory](../../by-subject/part-02/47-operator-theory/README.md). Declared in [FormalConjectures/Wikipedia/InvariantSubspaceProblem.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InvariantSubspaceProblem.lean#L100).

## `InvariantSubspaceProblem.Invariant_subspace_problem_normal_operator`

Solved: stated here; a Lean proof is at [https://github.com/baobingzhang/jsp-000024-lomonosov-lean/blob/8b43adc9781d70deb3d23bcdf38ec6195683669b/InvariantSubspaceLomonosov.lean#L422-L424](https://github.com/baobingzhang/jsp-000024-lomonosov-lean/blob/8b43adc9781d70deb3d23bcdf38ec6195683669b/InvariantSubspaceLomonosov.lean#L422-L424); a Lean proof is at [https://github.com/zblore/fc-isp-normal/blob/399f8bd8b68d4e24f33a6077e01a4adf3ae51df6/ISPNormal/Normal.lean#L143-L144](https://github.com/zblore/fc-isp-normal/blob/399f8bd8b68d4e24f33a6077e01a4adf3ae51df6/ISPNormal/Normal.lean#L143-L144).

> Every normal linear operator `T : H → H` on a Hilbert space `H` of dimension at least 2 has a
> non-trivial closed `T`-invariant subspace. If `T` is a multiple of the identity, one can take any
> non-trivial subspace. If not, one can take any nontrivial spectral subspace of `T`.

```lean
theorem Invariant_subspace_problem_normal_operator [InnerProductSpace ℂ H] [CompleteSpace H]
    (hdim : 2 ≤ Module.rank ℂ H) (T : H →L[ℂ] H) [IsStarNormal T]:
    Nonempty (ClosedInvariantSubspace T)
```

Category `research solved`; AMS [47 Operator theory](../../by-subject/part-02/47-operator-theory/README.md). Declared in [FormalConjectures/Wikipedia/InvariantSubspaceProblem.lean, line 138](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InvariantSubspaceProblem.lean#L138).

## `InvariantSubspaceProblem.Invariant_subspace_problem_l1`

Solved: stated here; a Lean proof is at [https://github.com/zblore/fc-read-l1/blob/57ceaa0ecdea86e90d82c1fd241c17e3bdb93e2d/ReadL1/Main.lean#L24-L27](https://github.com/zblore/fc-read-l1/blob/57ceaa0ecdea86e90d82c1fd241c17e3bdb93e2d/ReadL1/Main.lean#L24-L27).

> There exists a bounded linear operator `T` on the l1 space `(lp (fun (_ : ℕ) => ℂ) 1))` without
> non-trivial closed `T`-invariant subspace [Read 1985](https://doi.org/10.1112/blms/17.4.305), see
> also the first counterexample by Enflo [Enflo 1987](https://doi.org/10.1007%2FBF02392260), submitted
> in 1981.

```lean
theorem Invariant_subspace_problem_l1 :
    ∃ (T : (lp (fun (_ : ℕ) => ℂ) 1) →L[ℂ] (lp (fun (_ : ℕ) => ℂ) 1)),
    IsEmpty (ClosedInvariantSubspace T)
```

Category `research solved`; AMS [47 Operator theory](../../by-subject/part-02/47-operator-theory/README.md). Declared in [FormalConjectures/Wikipedia/InvariantSubspaceProblem.lean, line 151](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InvariantSubspaceProblem.lean#L151).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/InvariantSubspaceProblem.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InvariantSubspaceProblem.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Invariant_subspace_problem)
