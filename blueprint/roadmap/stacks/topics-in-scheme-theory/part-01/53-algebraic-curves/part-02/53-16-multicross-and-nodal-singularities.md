---
declaration: section
origin: cited
lean: Stacks.Curves.multicross, Ring.deltaInvariant_ge_numberOfBranches_sub_one, Ring.adicCompletion_algEquiv_multicross_of_deltaInvariant_eq, Ring.deltaInvariant_eq_numberOfBranches_sub_one_of_adicCompletion_algEquiv_multicross, Stacks.Curves.IsMulticrossSingularity, Stacks.Curves.IsOrdinaryDoublePoint, Stacks.Curves.isMulticrossSingularity_tfae, Stacks.Curves.isOrdinaryDoublePoint_of_isGorenstein
statement: formalized
proof: formalized
---

# 53.16 Multicross and nodal singularities

Section 53.16 of the Stacks Project, [Tag 0C1P](https://stacks.math.columbia.edu/tag/0C1P). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C1U, an equation

[Tag 0C1U](https://stacks.math.columbia.edu/tag/0C1U) in the Stacks Project.

**`Stacks.Curves.multicross`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Node/Multicross.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Node/Multicross.lean#L56).

> The ring of `n`-tuples of formal power series having the same constant coefficient.

```lean
def multicross (k : Type*) [CommRing k] (n : ℕ) : Subring (Fin n → PowerSeries k)
```

## Tag 0C1V, a lemma

[Tag 0C1V](https://stacks.math.columbia.edu/tag/0C1V) in the Stacks Project.

**`Ring.deltaInvariant_ge_numberOfBranches_sub_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/MulticrossBranches/BranchBound.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/MulticrossBranches/BranchBound.lean#L77). The attribute's comment: “delta invariant bound”.

> **The delta invariant of a reduced one-dimensional Nagata local algebra over a separably
> closed field is at least the number of branches minus one.**

```lean
theorem deltaInvariant_ge_numberOfBranches_sub_one
    (k : Type u) (A : Type v) [Field k] [IsSepClosed k] [CommRing A] [Algebra k A]
    [IsLocalRing A] [IsReduced A] (hNagata : IsNagataRing A)
    (hdim : ringKrullDim A = 1) (_hres : Nonempty (ResidueField A ≃ₐ[k] k)) :
    numberOfBranchesOfLocalRing A - 1 ≤ Ring.deltaInvariant A
```

**`Ring.adicCompletion_algEquiv_multicross_of_deltaInvariant_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/MulticrossBranches/Completion.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/MulticrossBranches/Completion.lean#L49). The attribute's comment: “equality case”.

> **If equality holds in the branch bound, the completed local algebra is the multicross
> algebra with one power-series factor for each branch.**

```lean
theorem adicCompletion_algEquiv_multicross_of_deltaInvariant_eq
    (k : Type u) (A : Type v) [Field k] [IsSepClosed k] [CommRing A] [Algebra k A]
    [IsLocalRing A] [IsReduced A] (hNagata : IsNagataRing A)
    (hdim : ringKrullDim A = 1) (_hres : Nonempty (ResidueField A ≃ₐ[k] k))
    (heq : Ring.deltaInvariant A = numberOfBranchesOfLocalRing A - 1) :
    ∃ n : ℕ, numberOfBranchesOfLocalRing A = n ∧
      ∃ e : AdicCompletion (maximalIdeal A) A ≃+* multicross k n,
        e.toRingHom.comp (algebraMap k (AdicCompletion (maximalIdeal A) A)) =
          (RingHom.pi fun _ : Fin n ↦ PowerSeries.C).codRestrict
            (multicross k n) (by
              intro a
              rw [mem_multicross]
              simp)
```

**`Ring.deltaInvariant_eq_numberOfBranches_sub_one_of_adicCompletion_algEquiv_multicross`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/MulticrossBranches/Completion.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/MulticrossBranches/Completion.lean#L333). The attribute's comment: “converse equality case”.

> **A coefficient-compatible multicross description of the completion, with one factor for
> each branch, forces equality in the delta-invariant bound.**

```lean
theorem deltaInvariant_eq_numberOfBranches_sub_one_of_adicCompletion_algEquiv_multicross
    (k : Type u) (A : Type v) [Field k] [IsSepClosed k] [CommRing A] [Algebra k A]
    [IsLocalRing A] [IsReduced A] (hNagata : IsNagataRing A)
    (hdim : ringKrullDim A = 1) (_hres : Nonempty (ResidueField A ≃ₐ[k] k))
    (n : ℕ) (hn : numberOfBranchesOfLocalRing A = n)
    (e : AdicCompletion (maximalIdeal A) A ≃+* multicross k n)
    (_he : e.toRingHom.comp (algebraMap k (AdicCompletion (maximalIdeal A) A)) =
      (RingHom.pi fun _ : Fin n ↦ PowerSeries.C).codRestrict
        (multicross k n) (by
          intro a
          rw [mem_multicross]
          simp)) :
    Ring.deltaInvariant A = numberOfBranchesOfLocalRing A - 1
```

## Tag 0C1W, a definition

[Tag 0C1W](https://stacks.math.columbia.edu/tag/0C1W) in the Stacks Project.

**`Stacks.Curves.IsMulticrossSingularity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/IsNode.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/IsNode.lean#L111). The attribute's comment: “multicross singularity”.

> **Stacks 0C1W.** A point is a multicross singularity if it is closed and its completed
> local ring is a multicross ring with at least two branches.

```lean
def IsMulticrossSingularity (k : Type u) [Field k] [IsAlgClosed k] (X : Scheme.{u})
    [X.Over (Spec (.of k))] (x : X) : Prop
```

**`Stacks.Curves.IsOrdinaryDoublePoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/IsNode.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/IsNode.lean#L123). The attribute's comment: “node (ordinary double point)”. References: SGA 7 VI (6.6), “dim 1, k alg. closed”; SGA 7 XV (1.2.1), “dim 1, alg. closed k”; SGA 7 XVII (1.1), “n=2, k alg. closed”; SGA 7 IX (10.5.4); SGA 7 IX (12.1.11).

> **Stacks 0C1W.** A point is an ordinary double point — a node, or a nodal singularity — if
> it is closed and its completed local ring is the two-branch multicross ring.

```lean
def IsOrdinaryDoublePoint (k : Type u) [Field k] [IsAlgClosed k] (X : Scheme.{u})
    [X.Over (Spec (.of k))] (x : X) : Prop
```

## Tag 0C1X, a lemma

[Tag 0C1X](https://stacks.math.columbia.edu/tag/0C1X) in the Stacks Project.

**`Stacks.Curves.isMulticrossSingularity_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/MulticrossGlueingResolution.lean, line 3082](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/MulticrossGlueingResolution.lean#L3082). The attribute's comment: “all three clauses. The hypothesis that the local ring at `x` is not regular is an erratum repair, not a weakening: the source's displayed equivalence is false at a nonsingular closed point, where the delta invariant is 0 and the number of branches is 1, so clauses (2) and (3) hold while (1) fails because Definition 0C1W requires n ≥ 2 -- Lemma 0C1V, which the source cites for the equivalence of (1) and (2), puts no lower bound on n. That counterexample is proved, not asserted, in `Stacks.Curves.exists_counterexample_to_displayed_statement_of_tag_0C1X_at_nonsingular_point`, and at a concrete scheme -- the origin of the affine line -- in `Stacks.Curves.exists_counterexample_to_displayed_statement_of_tag_0C1X_specPolynomial`. The hypothesis excludes exactly the regular configurations, where the equivalence fails, and nothing else”.

> **Stacks 0C1X.** Let `k` be an algebraically closed field, `X` a reduced algebraic
> one-dimensional `k`-scheme and `x ∈ X` a closed point whose local ring is not regular. The
> following are equivalent:
>
> 1. `x` defines a multicross singularity;
> 2. the delta invariant of `X` at `x` is the number of branches of `X` at `x` minus one;
> 3. there is a sequence of morphisms `U_n ⟶ U_{n-1} ⟶ … ⟶ U_0 = U ⊆ X` with `U` an open
>    neighbourhood of `x`, with `U_n` nonsingular, and with every step a glueing of two points as
>    in Example 0C1J.
>
> The equivalence of (1) and (2) is
> `Stacks.Curves.isMulticrossSingularity_iff_deltaInvariant_eq_of_not_isRegularLocalRing`, which
> is Tag 0C1V read at a point of a scheme. For (3) implies (1) the completion at the point glued
> in each step is the pair pullback of the two completions above it, hence a multicross ring or a
> field, and over every other point the step is an isomorphism on stalks. For (1) implies (3) an
> open neighbourhood on which `x` is the only singular point is chosen, Tag 0C1L factors its
> normalization morphism into glueings of two points and squishings of tangent vectors, and no
> step is a squishing because a multicross completion is seminormal while a squishing produces a
> non-seminormal completion.

```lean
theorem isMulticrossSingularity_tfae
    (k : Type u) [Field k] [IsAlgClosed k] (X : Scheme.{u})
    [X.Over (AlgebraicGeometry.Spec (.of k))]
    [LocallyOfFiniteType (X ↘ AlgebraicGeometry.Spec (.of k))]
    [QuasiCompact (X ↘ AlgebraicGeometry.Spec (.of k))] [IsReduced X]
    (hX : topologicalKrullDim X = 1) (x : X) (hx : IsClosed ({x} : Set X))
    (hsing : ¬ IsRegularLocalRing (X.presheaf.stalk x)) :
    List.TFAE
      [Stacks.Curves.IsMulticrossSingularity k X x,
        Ring.deltaInvariant (X.presheaf.stalk x) = numberOfBranches X x - 1,
        HasNonsingularGlueingResolution k X x]
```

## Tag 0CDZ, a lemma

[Tag 0CDZ](https://stacks.math.columbia.edu/tag/0CDZ) in the Stacks Project.

**`Stacks.Curves.isOrdinaryDoublePoint_of_isGorenstein`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/MulticrossGorenstein.lean, line 550](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/MulticrossGorenstein.lean#L550).

> **Stacks 0CDZ.** A multicross singularity of a Gorenstein scheme over an algebraically
> closed field is a node.

```lean
theorem isOrdinaryDoublePoint_of_isGorenstein (k : Type u) [Field k] [IsAlgClosed k]
    (X : Scheme.{u}) [X.Over (Spec (.of k))] [IsGorenstein X] (x : X)
    (hx : IsMulticrossSingularity k X x) :
    IsOrdinaryDoublePoint k X x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.16, Tag 0C1P](https://stacks.math.columbia.edu/tag/0C1P)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
