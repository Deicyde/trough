---
declaration: section
origin: cited
lean: Stacks.ResolutionOfSurfaces.factorsAsPointBlowups_of_proper_birational, Stacks.ResolutionOfSurfaces.factorsAsPointBlowups_of_isProper_of_isBirational, Stacks.ResolutionOfSurfaces.birationalOver_comp_of_factorsAsPointBlowups, Stacks.ResolutionOfSurfaces.birationalOver_comp_of_factorsAsPointBlowups_unconditional, Stacks.ResolutionOfSurfaces.birationalOver_of_exists_factorsAsPointBlowups, Stacks.ResolutionOfSurfaces.birationalOver_iff_exists_factorsAsPointBlowups_of_isRegular, Stacks.ResolutionOfSurfaces.birationalOver_iff_exists_factorsAsPointBlowups_of_isIntegralRegularSurface
statement: formalized
proof: formalized
---

# 54.17 Factorization birational maps

Section 54.17 of the Stacks Project, [Tag 0C5Q](https://stacks.math.columbia.edu/tag/0C5Q). 2 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C5R, a lemma

[Tag 0C5R](https://stacks.math.columbia.edu/tag/0C5R) in the Stacks Project.

**`Stacks.ResolutionOfSurfaces.factorsAsPointBlowups_of_proper_birational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/FactorizationBirationalSurfaces.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/FactorizationBirationalSurfaces.lean#L278). The attribute's comment: “the conclusion in full; the inputs hsec, blowUpSurface and square remain named arguments and descent is reduced to the drop of the measure, as the module documentation records”.

> **Stacks Project, Tag 0C5R.** Let `f : X ⟶ Y` be a proper birational morphism between
> integral Noetherian schemes regular of dimension two. Then `f` is a sequence of blowups in closed
> points, that is, `f` is up to an isomorphism of its source the composite of a chain of blowups at
> closed points.
>
> Three inputs are arguments rather than theorems: `hsec`, the second arrow of
> [Stacks, Tag 067L]; `blowUpSurface`, the regularity ([Stacks, Tag 0AGR] globally) and the
> dimension of the blowup at a closed point; and `square`, the reduction of [Stacks, Tag 0C5H]
> to a single blowup together with the dichotomy of the source's step 3. The fourth argument
> `descent` is the strict drop of the measure `μ`, the bookkeeping the source omits. None of them
> is inter-derivable with the conclusion; see the module documentation.

```lean
public theorem factorsAsPointBlowups_of_proper_birational
    (hsec : ConormalSequenceSecondArrow.{u}) (μ : ∀ (A B : Scheme.{u}), (B ⟶ A) → ℕ)
    (blowUpSurface : ∀ (A : Scheme.{u}) (a : A) (ha : IsClosed ({a} : Set A)),
      IsIntegralRegularSurface A →
        IsRegular (pointBlowUp ha) ∧ topologicalKrullDim (pointBlowUp ha) = 2)
    (square : ∀ (A B : Scheme.{u}) (g : B ⟶ A), IsIntegralRegularSurface A →
      IsIntegralRegularSurface B → IsProper g → IsBirational g → ¬ IsIso g →
      ∀ (a : A) (ha : IsClosed ({a} : Set A)) (U : A.Opens),
        IsGreatest { V : A.Opens | IsIso (g ∣_ V) } U → a ∉ U →
          HasExceptionalSquareAt g a ha)
    (descent : ∀ (A B : Scheme.{u}) (g : B ⟶ A), IsIntegralRegularSurface A →
      IsIntegralRegularSurface B → IsProper g → IsBirational g → ¬ IsIso g →
      ∀ (a : A) (ha : IsClosed ({a} : Set A)) (U : A.Opens),
        IsGreatest { V : A.Opens | IsIso (g ∣_ V) } U → a ∉ U →
          ∀ ψ : B ⟶ pointBlowUp ha, ψ ≫ pointBlowUpToBase ha = g →
            μ (pointBlowUp ha) B ψ < μ A B g)
    {X Y : Scheme.{u}} (f : X ⟶ Y) (hY : IsIntegralRegularSurface Y)
    (hX : IsIntegralRegularSurface X) (hproper : IsProper f) (hbirational : IsBirational f) :
    FactorsAsPointBlowups Y Set.univ X f
```

**`Stacks.ResolutionOfSurfaces.factorsAsPointBlowups_of_isProper_of_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/PointBlowupFactorizationStep.lean, line 876](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/PointBlowupFactorizationStep.lean#L876).

> **Stacks Project, Tag 0C5R.** Let `f : X ⟶ Y` be a proper birational morphism between
> integral Noetherian schemes regular of dimension two. Then `f` is a sequence of blowups in closed
> points.

```lean
theorem factorsAsPointBlowups_of_isProper_of_isBirational {X Y : Scheme.{u}} (f : X ⟶ Y)
    (hY : IsIntegralRegularSurface Y) (hX : IsIntegralRegularSurface X) (hproper : IsProper f)
    (hbirational : IsBirational f) : FactorsAsPointBlowups Y Set.univ X f
```

## Tag 0C5S, a lemma

[Tag 0C5S](https://stacks.math.columbia.edu/tag/0C5S) in the Stacks Project.

**`Stacks.ResolutionOfSurfaces.birationalOver_comp_of_factorsAsPointBlowups`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/FactorizationBirationalMaps.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/FactorizationBirationalMaps.lean#L244). The attribute's comment: “the converse direction, which the source states without proof: a two-sided chain of blowups in closed points makes `X` and `Y` birational over the base. Unconditional apart from blowUpSurface (the globalization of Tag 0AGR); the route is Tag 02OS, nonvanishing of the point's ideal sheaf, and Tag 0BAD”.

> **The converse direction of [Stacks, Tag 0C5S], whose proof the source omits.** A morphism
> which is a finite sequence of blowups at closed points of an integral Noetherian scheme regular
> of dimension two makes its source birational to the target over any base.

```lean
public theorem birationalOver_comp_of_factorsAsPointBlowups
    (blowUpSurface : ∀ (A : Scheme.{u}) (a : A) (ha : IsClosed ({a} : Set A)),
      IsIntegralRegularSurface A →
        IsIntegralRegularSurface
          (blowUp (Scheme.IdealSheafData.vanishingIdeal (⟨{a}, ha⟩ : Closeds A))))
    {S X Z : Scheme.{u}} (sX : X ⟶ S) (hX : IsIntegralRegularSurface X) {f : Z ⟶ X}
    (hf : FactorsAsPointBlowups X Set.univ Z f) :
    Scheme.BirationalOver (f ≫ sX) sX
```

**`Stacks.ResolutionOfSurfaces.birationalOver_comp_of_factorsAsPointBlowups_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/FactorizationBirationalMapsUnconditional.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/FactorizationBirationalMapsUnconditional.lean#L106). The attribute's comment: “one side of the converse direction, which the source states without proof: a chain of blowups in closed points out of `X` makes its source birational to `X` over the base. The route is Tag 02OS, nonvanishing of the point's ideal sheaf, and Tag 0BAD, and the blowup of such a scheme at a closed point is again such a scheme by the globalization of Tag 0AGR, `AlgebraicGeometry.isRegular_and_topologicalKrullDim_blowUp_vanishingIdeal_singleton`”.

> **One side of the converse direction of [Stacks, Tag 0C5S], whose proof the source omits.** A
> morphism which is a finite sequence of blowups at closed points of an integral Noetherian scheme
> regular of dimension two makes its source birational to the target over any base.

```lean
public theorem birationalOver_comp_of_factorsAsPointBlowups_unconditional
    {S X Z : Scheme.{u}} (sX : X ⟶ S) (hX : IsIntegralRegularSurface X) {f : Z ⟶ X}
    (hf : FactorsAsPointBlowups X Set.univ Z f) :
    Scheme.BirationalOver (f ≫ sX) sX
```

**`Stacks.ResolutionOfSurfaces.birationalOver_of_exists_factorsAsPointBlowups`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/FactorizationBirationalMapsUnconditional.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/FactorizationBirationalMapsUnconditional.lean#L130). The attribute's comment: “the implication from the two-sided chain of blowups in closed points to `S`-birationality of `X` and `Y`, which is the direction the source states without proof. Nothing is assumed: the two sides are composed through `Stacks.ResolutionOfSurfaces.birationalOver_comp_of_factorsAsPointBlowups_unconditional` and the symmetry and transitivity of `AlgebraicGeometry.Scheme.BirationalOver`”.

> **The converse direction of [Stacks, Tag 0C5S], whose proof the source omits.** Let `S` be a
> Noetherian scheme and let `X` and `Y` be proper integral schemes over `S` which are regular of
> dimension two. If there is a scheme `Z` with `S`-morphisms `f : Z ⟶ X` and `g : Z ⟶ Y`, each a
> finite sequence of blowups at closed points, then `X` and `Y` are `S`-birational.
>
> This is the implication of the source's `if and only if` that the source states without proof,
> and it is proved here with nothing assumed: each of the two sides makes `Z` birational to its
> target over `S` by
> `Stacks.ResolutionOfSurfaces.birationalOver_comp_of_factorsAsPointBlowups_unconditional`,
> and `S`-birationality is symmetric and transitive.

```lean
public theorem birationalOver_of_exists_factorsAsPointBlowups
    {S X Y : Scheme.{u}} [X.Over S] [Y.Over S]
    (hX : IsIntegralRegularSurface X) (hY : IsIntegralRegularSurface Y)
    (h : ∃ (Z : Scheme.{u}) (f : Z ⟶ X) (g : Z ⟶ Y),
      f ≫ (X ↘ S) = g ≫ (Y ↘ S) ∧
        FactorsAsPointBlowups X Set.univ Z f ∧ FactorsAsPointBlowups Y Set.univ Z g) :
    Scheme.BirationalOver (X ↘ S) (Y ↘ S)
```

**`Stacks.ResolutionOfSurfaces.birationalOver_iff_exists_factorsAsPointBlowups_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/FactorizationBirationalSurfacesProperOverNoetherian.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/FactorizationBirationalSurfacesProperOverNoetherian.lean#L60). The attribute's comment: “the tag's hypothesis list, with the surface predicate derived rather than assumed: `S` is Noetherian and `X` and `Y` are proper over `S`, integral, regular and of dimension two. The bundled `Stacks.ResolutionOfSurfaces.IsIntegralRegularSurface` of the other registration asks of the two schemes that they be Noetherian as well; here that is obtained from properness over `S` by Tag 01T6”.

> Let `S` be a Noetherian scheme and let `X` and `Y` be proper integral schemes over `S` which
> are regular of dimension two. Then `X` and `Y` are `S`-birational if and only if there is a scheme
> `Z` with `S`-morphisms `f : Z ⟶ X` and `g : Z ⟶ Y`, each a finite sequence of blowups at closed
> points.
>
> Of `X` and `Y` only the tag's own conditions are assumed: integral, regular, of dimension two,
> and proper over the Noetherian base. Their Noetherianness, which
> `Stacks.ResolutionOfSurfaces.IsIntegralRegularSurface` demands in addition, is derived from
> properness over `S`.

```lean
public theorem birationalOver_iff_exists_factorsAsPointBlowups_of_isRegular
    {S X Y : Scheme.{u}} [AlgebraicGeometry.IsNoetherian S] [X.Over S] [Y.Over S]
    [IsProper (X ↘ S)] [IsProper (Y ↘ S)]
    (hXintegral : AlgebraicGeometry.IsIntegral X) (hXregular : AlgebraicGeometry.IsRegular X)
    (hXdim : topologicalKrullDim X = 2) (hYintegral : AlgebraicGeometry.IsIntegral Y)
    (hYregular : AlgebraicGeometry.IsRegular Y) (hYdim : topologicalKrullDim Y = 2) :
    Scheme.BirationalOver (X ↘ S) (Y ↘ S) ↔
      ∃ (Z : Scheme.{u}) (f : Z ⟶ X) (g : Z ⟶ Y),
        f ≫ (X ↘ S) = g ≫ (Y ↘ S) ∧
          FactorsAsPointBlowups X Set.univ Z f ∧ FactorsAsPointBlowups Y Set.univ Z g
```

**`Stacks.ResolutionOfSurfaces.birationalOver_iff_exists_factorsAsPointBlowups_of_isIntegralRegularSurface`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/PointBlowupFactorizationStep.lean, line 907](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/PointBlowupFactorizationStep.lean#L907).

> **Stacks Project, Tag 0C5S.** Let `S` be a Noetherian scheme and let `X` and `Y` be proper
> integral schemes over `S` which are regular of dimension two. Then `X` and `Y` are `S`-birational
> if and only if there is a scheme `Z` with `S`-morphisms `Z ⟶ X` and `Z ⟶ Y`, each a sequence of
> blowups in closed points.

```lean
theorem birationalOver_iff_exists_factorsAsPointBlowups_of_isIntegralRegularSurface
    {S X Y : Scheme.{u}} [AlgebraicGeometry.IsNoetherian S] [X.Over S] [Y.Over S]
    [IsProper (X ↘ S)] [IsProper (Y ↘ S)] (hX : IsIntegralRegularSurface X)
    (hY : IsIntegralRegularSurface Y) :
    Scheme.BirationalOver (X ↘ S) (Y ↘ S) ↔
      ∃ (Z : Scheme.{u}) (f : Z ⟶ X) (g : Z ⟶ Y),
        f ≫ (X ↘ S) = g ≫ (Y ↘ S) ∧
          FactorsAsPointBlowups X Set.univ Z f ∧ FactorsAsPointBlowups Y Set.univ Z g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 54.17, Tag 0C5Q](https://stacks.math.columbia.edu/tag/0C5Q)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
