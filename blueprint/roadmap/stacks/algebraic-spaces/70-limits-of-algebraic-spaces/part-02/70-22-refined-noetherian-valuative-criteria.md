---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isProper_of_denseRange_of_exists_discreteLift, AlgebraicGeometry.Space.isSeparated_of_denseRange_of_subsingleton_discreteLift, AlgebraicGeometry.Space.isProper_of_denseRange_of_unique_discreteLift
statement: formalized
proof: formalized
---

# 70.22 Refined Noetherian valuative criteria

Section 70.22 of the Stacks Project, [Tag 0H1Z](https://stacks.math.columbia.edu/tag/0H1Z). 3 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CMD, a lemma

[Tag 0CMD](https://stacks.math.columbia.edu/tag/0CMD) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isProper_of_denseRange_of_exists_discreteLift`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RefinedValuativeProperness.lean#L511), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/NoetherianRefinedValuativeCriterion.lean, line 499](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/NoetherianRefinedValuativeCriterion.lean#L499) (StacksFrontier): “Let `f : X ⟶ Y` and `h : U ⟶ X` be morphisms of algebraic spaces over `S`, with `Y` locally Noetherian, `f` and `h` of finite type, `f` separated and the image of `|h| : |U| → |X|` dense in `|X|`. If every commutative valuative diagram for `f` over a discrete valuation ring whose generic arrow factors through `h` has a dotted arrow, then `f` is proper.”.

## Tag 0CME, a lemma

[Tag 0CME](https://stacks.math.columbia.edu/tag/0CME) in the Stacks Project.

**`AlgebraicGeometry.Space.isSeparated_of_denseRange_of_subsingleton_discreteLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RefinedValuativeSeparatedness.lean, line 417](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RefinedValuativeSeparatedness.lean#L417).

> **Stacks 0CME.** Let `f : X ⟶ Y` and `h : U ⟶ X` be morphisms of algebraic spaces over `S`
> with `Y` locally Noetherian, `f` locally of finite type and quasi-separated, `h` of finite type
> and the image of `|h| : |U| → |X|` dense in `|X|`. If every commutative valuative diagram for `f`
> over a discrete valuation ring `A` with fraction field `K` whose generic arrow `Spec K ⟶ X`
> factors through `h` has at most one dotted arrow `Spec A ⟶ X`, then `f` is separated.
>
> The relative diagonal of `f` is representable, a monomorphism, separated, locally of finite type,
> and quasi-compact because `f` is quasi-separated. Its base change `V ⟶ C` along an étale chart
> `C` of the locally Noetherian algebraic space `X ×_Y X` (Stacks 04ZK) is therefore a
> quasi-compact monomorphism of schemes locally of finite type over a locally Noetherian scheme,
> and it satisfies condition (4) of Stacks 0208: at a generic point of `V` a dotted arrow exists by
> `nonempty_liftStruct_of_denseRange`, and it is unique since `V ⟶ C` is a monomorphism. So
> `V ⟶ C` is proper (Stacks 0208), hence a closed immersion (Stacks 04XV), and being a closed
> immersion descends from the chart to the diagonal (Stacks 02L6, 02WZ).

```lean
theorem isSeparated_of_denseRange_of_subsingleton_discreteLift
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hU : IsAlgebraicSpace B S hS U) (f : X ⟶ Y) (h : U ⟶ X)
    (hnoeth : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hlft : IsLocallyOfFiniteType B S hS f) (hqs : IsQuasiSeparated B S hS f)
    (hh : IsFiniteType B S hS h)
    (hdense : @DenseRange _ (pointTopology B S hS X) _ (pointsMap B S hS U h))
    (hvaluative : ∀ q : ValuativeSquare f, IsDiscreteValuationRing q.R →
      ∀ g : yoneda.obj (siteObject B S hS q.field_mem
          (Spec.map (CommRingCat.ofHom (algebraMap q.R q.K)) ≫ q.base)) ⟶ U,
        g ≫ h = q.generic → Subsingleton q.Lift) :
    IsSeparated B S hS f
```

## Tag 0CMF, a lemma

[Tag 0CMF](https://stacks.math.columbia.edu/tag/0CMF) in the Stacks Project.

**`AlgebraicGeometry.Space.isProper_of_denseRange_of_unique_discreteLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RefinedValuativeProperness.lean, line 540](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RefinedValuativeProperness.lean#L540).

> **Stacks 0CMF.** Let `f : X ⟶ Y` and `h : U ⟶ X` be morphisms of algebraic spaces over `S`
> with `Y` locally Noetherian, `f` and `h` of finite type, `f` quasi-separated and the image of
> `|h| : |U| → |X|` dense in `|X|`. If every commutative valuative diagram for `f` over a discrete
> valuation ring `A` with fraction field `K` whose generic arrow `Spec K ⟶ X` factors through `h`
> has exactly one dotted arrow `Spec A ⟶ X`, then `f` is proper.
>
> As in the source this combines Stacks 0CME, which gives separatedness of `f` from the uniqueness
> of the dotted arrows, with Stacks 0CMD, which gives properness from their existence.

```lean
theorem isProper_of_denseRange_of_unique_discreteLift
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hU : IsAlgebraicSpace B S hS U) (f : X ⟶ Y) (h : U ⟶ X)
    (hnoeth : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hft : IsFiniteType B S hS f) (hh : IsFiniteType B S hS h) (hqs : IsQuasiSeparated B S hS f)
    (hdense : @DenseRange _ (pointTopology B S hS X) _ (pointsMap B S hS U h))
    (hvaluative : ∀ q : ValuativeSquare f, IsDiscreteValuationRing q.R →
      ∀ g : yoneda.obj (siteObject B S hS q.field_mem
          (Spec.map (CommRingCat.ofHom (algebraMap q.R q.K)) ≫ q.base)) ⟶ U,
        g ≫ h = q.generic → Nonempty q.Lift ∧ Subsingleton q.Lift) :
    IsProper B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.22, Tag 0H1Z](https://stacks.math.columbia.edu/tag/0H1Z)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
