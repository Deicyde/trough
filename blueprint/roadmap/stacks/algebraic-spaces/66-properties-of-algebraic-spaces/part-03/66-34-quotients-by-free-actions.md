---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isAlgebraicSpace_orbitQuotientSheaf_points_of_free, AlgebraicGeometry.Space.isAlgebraicSpace_actionQuotient_of_actsFreelyOnNonemptyPoints, AlgebraicGeometry.Space.isAlgebraicSpace_orbitQuotientSheaf_of_isFreeOnNonemptyPoints
statement: formalized
proof: formalized
---

# 66.34 Quotients by free actions

Section 66.34 of the Stacks Project, [Tag 071R](https://stacks.math.columbia.edu/tag/071R). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 071S, a lemma

[Tag 071S](https://stacks.math.columbia.edu/tag/071S) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_orbitQuotientSheaf_points_of_free`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FreeActionOrbitQuotient.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FreeActionOrbitQuotient.lean#L279). The attribute's comment: “for an action of the abstract group on an object of the big fppf site in place of an arbitrary algebraic space, and with freeness read on the points over the test schemes with nonempty underlying space”.

> **Stacks 071S** for an action on an object of a big fppf site over `S`: the quotient of `V`
> by a free action of an abstract group `G`, formed as in the source as the fppf sheafification
> of the presheaf `T ↦ V(T)/G` of pointwise orbits, is an algebraic space over `S`.
>
> That quotient is the quotient sheaf of the graph relation of the action, by
> `AlgebraicGeometry.Space.isoOrbitQuotientActionQuotient`, so this is
> `AlgebraicGeometry.Space.isAlgebraicSpace_actionQuotient_of_actsFreelyOnNonemptyPoints`.

```lean
theorem isAlgebraicSpace_orbitQuotientSheaf_points_of_free
    (ha : ActsFreelyOnNonemptyPoints ((Over.post B.inclusion).obj V) G a) :
    IsAlgebraicSpace B S hS (orbitQuotientSheaf B S hS G
      (Stacks.Groupoids.points (Over.post B.inclusion)
        ((Over.post B.inclusion).obj V)) hnat).obj
```

**`AlgebraicGeometry.Space.isAlgebraicSpace_actionQuotient_of_actsFreelyOnNonemptyPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FreeActionQuotient.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FreeActionQuotient.lean#L148). The attribute's comment: “for an action of the abstract group on an object of the big fppf site in place of an arbitrary algebraic space, the quotient being the sheaf quotient of the graph relation of the action, and freeness being read on the points over the test schemes with nonempty underlying space”.

> **Stacks 071S** for an action on an object of a big fppf site over `S`: the quotient of `V`
> by a free action of an abstract group `G` is an algebraic space over `S`.
>
> The graph relation of a free action is an étale equivalence relation, by
> `AlgebraicGeometry.Space.actsFreelyOnNonemptyPoints_iff` and Tag 02Z2, so this is
> `AlgebraicGeometry.Space.isAlgebraicSpace_actionQuotient` with its descent hypothesis
> discharged.

```lean
theorem isAlgebraicSpace_actionQuotient_of_actsFreelyOnNonemptyPoints
    (a : G →* Aut (underlyingOver B hS V))
    (ha : ActsFreelyOnNonemptyPoints (underlyingOver B hS V) G a) :
    IsAlgebraicSpace B S hS (actionQuotient G B hS V a)
```

**`AlgebraicGeometry.Space.isAlgebraicSpace_orbitQuotientSheaf_of_isFreeOnNonemptyPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FreeActionSpaceQuotient.lean, line 1002](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FreeActionSpaceQuotient.lean#L1002). The attribute's comment: “with freeness read on the points over the test objects with nonempty underlying scheme”.

> **Stacks 071S.** Let `S` be a scheme, `X` an algebraic space over `S` and `G` an abstract
> group acting on `X` by a natural pointwise action. If the action is free then the quotient
> `X/G`, the fppf sheafification of the presheaf `T ↦ X(T)/G` of pointwise orbits, is an
> algebraic space over `S`.
>
> Freeness is read on the points over the test objects with nonempty underlying scheme
> (`AlgebraicGeometry.Space.IsFreeOnNonemptyPoints`); over a test object with empty underlying
> scheme a sheaf is terminal, so asking it there would force `G` to be trivial, by
> `AlgebraicGeometry.Space.forall_isCancelSMul_iff_subsingleton`.
>
> The proof is the source's. At a surjective étale chart `φ : U ⟶ X` the relation
> `R = ∐_{g ∈ G} U ×_{φ, X, g • φ} U` is an object of the site — freeness bounds the index set
> by the points of `U ×_S U` — and it is the kernel pair of `U ⟶ X/G`, so it is an étale
> equivalence relation, `U/R` is an algebraic space by Tag 02WW, and `X/G ≅ U/R` because both
> are the coequalizer of `h_R ⇉ h_U` in fppf sheaves.

```lean
theorem isAlgebraicSpace_orbitQuotientSheaf_of_isFreeOnNonemptyPoints
    (hnat : IsNaturalAction B S hS G X) (hX : IsAlgebraicSpace B S hS X)
    (hfree : IsFreeOnNonemptyPoints B S hS G X) :
    IsAlgebraicSpace B S hS (orbitQuotientSheaf B S hS G X hnat).obj
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.34, Tag 071R](https://stacks.math.columbia.edu/tag/071R)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
