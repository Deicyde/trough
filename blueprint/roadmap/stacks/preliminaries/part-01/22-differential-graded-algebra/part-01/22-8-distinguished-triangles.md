---
declaration: section
origin: cited
lean: DifferentialGradedModule.AdmissibleTriangle.DGModule.associatedTriangle_iso_of_compatibleSplittings, DifferentialGradedModule.nonempty_compatibleSplittings, DifferentialGradedModule.associatedTriangle, DifferentialGradedModule.associatedTriangleOfSplittings_eq, DifferentialGradedModule.IsDistinguishedTriangle, DifferentialGradedModule.isDistinguishedTriangle_gradedSplit
statement: formalized
proof: formalized
---

# 22.8 Distinguished triangles

Section 22.8 of the Stacks Project, [Tag 09K5](https://stacks.math.columbia.edu/tag/09K5). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09K6, a lemma

[Tag 09K6](https://stacks.math.columbia.edu/tag/09K6) in the Stacks Project.

**`DifferentialGradedModule.AdmissibleTriangle.DGModule.associatedTriangle_iso_of_compatibleSplittings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/AdmissibleSequenceTriangle.lean, line 778](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/AdmissibleSequenceTriangle.lean#L778).

> The triangle associated to an admissible short exact sequence is, up to canonical
> isomorphism in the homotopy category `K(Mod_{(A,d)})`, independent of the choice of
> compatible splittings: for any two pairs of compatible splittings `(s, π)` and `(s', π')`,
> the identity morphisms on `K`, `L`, `M` form an isomorphism of the associated triangles
> `T : K → L → M → K[1]` and `T' : K → L → M → K[1]` in `K(Mod_{(A,d)})`.

```lean
theorem associatedTriangle_iso_of_compatibleSplittings
    {K L M : DGModule A} (E : AdmissibleSES K L M)
    (P P' : E.CompatibleSplittings) :
    Nonempty (TriangleHtpyIso P.associatedTriangle P'.associatedTriangle)
```

## Tag 09K8, a definition

[Tag 09K8](https://stacks.math.columbia.edu/tag/09K8) in the Stacks Project.

**`DifferentialGradedModule.nonempty_compatibleSplittings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DistinguishedTriangle.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DistinguishedTriangle.lean#L87). The attribute's comment: “part (1), compatible splittings”.

> Admissibility supplies graded splittings compatible with one another.

```lean
theorem nonempty_compatibleSplittings {K L M : DifferentialGradedModule A}
    (f : Hom K L) (g : Hom L M) (hfg : IsAdmissibleShortExact f g) :
    Nonempty (CompatibleSplittings A f g)
```

**`DifferentialGradedModule.associatedTriangle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DistinguishedTriangle.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DistinguishedTriangle.lean#L142). The attribute's comment: “part (1)”.

> The triangle of an admissible short exact sequence in the homotopy category.

```lean
noncomputable def associatedTriangle {K L M : DifferentialGradedModule A}
    (f : Hom K L) (g : Hom L M) (hfg : IsAdmissibleShortExact f g) :
    Pretriangulated.Triangle (HomotopyCategory A)
```

**`DifferentialGradedModule.associatedTriangleOfSplittings_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DistinguishedTriangle.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DistinguishedTriangle.lean#L152). The attribute's comment: “part (1), independence of splittings”. References: SGA 4½ Etat 0 (1.2.4), “splitting independence”.

> The associated triangle is independent of the compatible graded splittings used to compute
> its connecting arrow.

```lean
theorem associatedTriangleOfSplittings_eq {K L M : DifferentialGradedModule A}
    (f : Hom K L) (g : Hom L M) (hfg : IsAdmissibleShortExact f g)
    (c : CompatibleSplittings A f g) :
    associatedTriangleOfSplittings A f g hfg c = associatedTriangle A f g hfg
```

**`DifferentialGradedModule.IsDistinguishedTriangle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DistinguishedTriangle.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DistinguishedTriangle.lean#L162). The attribute's comment: “part (2)”.

> A triangle of the homotopy category is distinguished precisely when it is isomorphic to the
> triangle of an admissible short exact sequence.

```lean
def IsDistinguishedTriangle (T : Pretriangulated.Triangle (HomotopyCategory A)) : Prop
```

**`DifferentialGradedModule.isDistinguishedTriangle_gradedSplit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/GradedSplitAdmissible.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/GradedSplitAdmissible.lean#L165). The attribute's comment: “the triangle of a graded splitting is distinguished”.

> **The triangle of a graded-split short exact sequence is distinguished.** The third arrow may
> be presented by any homomorphism `Z ⟶ X[1]` whose underlying linear map is the connecting
> morphism `π d(s)` of the splitting; a homomorphism of differential graded modules is determined
> by that map.

```lean
theorem isDistinguishedTriangle_gradedSplit (δ : Hom Z (shift X 1))
    (hδ : ∀ z : Z.M, δ.toFun z = (DGCategory.GradedSplitShortExact.connectingHom E).1 z) :
    IsDistinguishedTriangle A (Pretriangulated.Triangle.mk
      ((toHomotopyCategory A).map (homOfCocycle A E.a))
      ((toHomotopyCategory A).map (homOfCocycle A E.b))
      ((toHomotopyCategory A).map δ ≫
        eqToHom (CategoryTheory.Quotient.functor_obj_shift (homotopyRel A) ℤ X 1).symm))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.8, Tag 09K5](https://stacks.math.columbia.edu/tag/09K5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
