---
declaration: section
origin: cited
lean: Stacks.Duality.isNormalizedDualizingComplex_derivedStalkOfComplex, Stacks.Duality.isNormalizedDualizingComplex_derivedStalkOfComplex_normalizedDualizingComplex, Stacks.Duality.associatedShiftFunction_sub_eq_trdeg, Stacks.Duality.associatedShiftFunction_sub_eq_trdeg_of_upperShriek, Stacks.Duality.associatedShiftFunction_sub_eq_trdeg_normalizedDualizingComplex, Stacks.Duality.exists_fibreDim_eq_and_neg_le_of_nontrivial_stalk_homology_upperShriek, Stacks.Duality.fibreDim_bounds_of_nontrivial_stalk_homology_upperShriek_of_flat_unconditional, Stacks.Duality.hasTorAmplitude_derivedScalarRestriction_upperShriek
statement: formalized
proof: formalized
---

# 48.21 Dimension functions

Section 48.21 of the Stacks Project, [Tag 0BV4](https://stacks.math.columbia.edu/tag/0BV4). 8 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AWL, a lemma

[Tag 0AWL](https://stacks.math.columbia.edu/tag/0AWL) in the Stacks Project.

**`Stacks.Duality.isNormalizedDualizingComplex_derivedStalkOfComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/NormalizedAtClosedPointCharts.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/NormalizedAtClosedPointCharts.lean#L79).

> **Stacks Project, Tag 0AWL (Lemma 48.21.1).** Let `S` be a Noetherian scheme with a
> dualizing complex `ω_S^•`, let `p : X ⟶ S` be of finite type, and let `ω_X^•` be normalized
> relative to `ω_S^•`: every point has an affine open neighbourhood `U` with
> `ω_X^•|_U ≅ (U ⟶ S)^! ω_S^•` for a compactification of `U` over `S`. Let `x ∈ X` be a closed
> point and `s = p x`. If `ω_{S,s}^•` is a normalized dualizing complex over `𝒪_{S,s}`, then
> `ω_{X,x}^•` is a normalized dualizing complex over `𝒪_{X,x}`. The source also asks that `s` be
> closed; this is not needed.

```lean
theorem isNormalizedDualizingComplex_derivedStalkOfComplex
    {S X : Scheme.{u}} [AlgebraicGeometry.IsNoetherian S] (p : X ⟶ S) [LocallyOfFiniteType p]
    (ωS : quasiCoherentDerivedCategory S) (hωS : IsDualizingComplex ωS.obj)
    (ωX : DerivedCategory X.Modules)
    (hωX : ∀ x : X, ∃ (U : X.Opens) (_ : IsAffine U.toScheme) (_ : x ∈ U)
      (j : CompactificationOf (Over.mk (ftsHomToBase (U.ι ≫ p)).left)),
      Nonempty ((Scheme.Modules.restrictFunctor U.ι).mapDerivedCategory.obj ωX ≅
        ((upperShriek (ftsHomToBase (U.ι ≫ p)) j).obj ωS).obj))
    (x : X) (hx : IsClosed ({x} : Set X))
    (hωSs : ∃ E : CochainComplex S.Modules ℤ, Nonempty (DerivedCategory.Q.obj E ≅ ωS.obj) ∧
      Dualizing.IsNormalizedDualizingComplex.{u, u} (derivedStalkOfComplex (p x) E)) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian p
    ∀ E : CochainComplex X.Modules ℤ, Nonempty (DerivedCategory.Q.obj E ≅ ωX) →
      Dualizing.IsNormalizedDualizingComplex.{u, u} (derivedStalkOfComplex x E)
```

**`Stacks.Duality.isNormalizedDualizingComplex_derivedStalkOfComplex_normalizedDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/NormalizedDualizingComplexNagataCharts.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/NormalizedDualizingComplexNagataCharts.lean#L98).

> **[Stacks, Tag 0AWL].** Let `S` be a Noetherian scheme with a dualizing complex `ω_S^•`, let
> `X` be of finite type over `S` and `ω_X^•` the dualizing complex normalized relative to `ω_S^•`.
> If `x ∈ X` is a closed point lying over a closed point `s` of `S`, then `ω_{X,x}^•` is a
> normalized dualizing complex over `𝒪_{X,x}` provided that `ω_{S,s}^•` is a normalized dualizing
> complex over `𝒪_{S,s}`. Stalks are the derived stalks of representatives; the closedness of `s`
> is not used.

```lean
theorem isNormalizedDualizingComplex_derivedStalkOfComplex_normalizedDualizingComplex
    (x : X) (hx : IsClosed ({x} : Set X))
    (hωSs : haveI := hp.base_noetherian
      ∃ E : CochainComplex S.Modules ℤ, Nonempty (DerivedCategory.Q.obj E ≅ ωS.obj.obj) ∧
      Dualizing.IsNormalizedDualizingComplex.{u, u}
        (@derivedStalkOfComplex S (p x) (HasDerivedCategory.standard _) E)) :
    haveI := hp.source_noetherian
    ∀ E : CochainComplex X.Modules ℤ,
      Nonempty (DerivedCategory.Q.obj E ≅ (normalizedDualizingComplex hp ωS hωS).complex.obj.obj) →
        Dualizing.IsNormalizedDualizingComplex.{u, u}
          (@derivedStalkOfComplex X x (HasDerivedCategory.standard _) E)
```

## Tag 0AWM, a lemma

[Tag 0AWM](https://stacks.math.columbia.edu/tag/0AWM) in the Stacks Project.

**`Stacks.Duality.associatedShiftFunction_sub_eq_trdeg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/NormalizedDualizingDimensionFunction.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/NormalizedDualizingDimensionFunction.lean#L208). The attribute's comment: “RESTRICTED: three inputs are explicit hypotheses. That the shift functions of the two dualizing complexes are dimension functions is the unproved half of Tag 0AWF, carried as dimension functions delta\_S and delta\_X together with hdS and hdX. That f carries closed points to closed points -- the source's reduction to a proper f, through Nagata compactification and Tag 0AUC -- is hClosedImage. The identity at a closed point over a closed point, Tag 0AWL, is hClosedPoint; 0AWL itself is proved, but the bridge from normalized stalks to a value of associatedShiftFunction is not. What is proved is the body of the lemma: universal catenarity of S from Tag 0AWF, then that the difference of the two functions is determined by its values at closed points, by Tag 02JW and Tag 02IB and Tag 02IL, and that the transcendence degree vanishes at a closed point, by Tag 01TF”.

> **Stacks Project, Tag 0AWM.** Let `S` be a Noetherian scheme and let `ω_S^•` be a dualizing
> complex. Let `f : X ⟶ S` be of finite type and let `ω_X^•` be the dualizing complex normalized
> relative to `ω_S^•`. For all `x ∈ X`
>
> `δ_X(x) - δ_S(f x) = trdeg_{κ(f x)} κ(x)`
>
> where `δ_S`, resp. `δ_X`, is the dimension function of `ω_S^•`, resp. `ω_X^•`, of
> [Stacks, Tag 0AWF] — here `Stacks.Duality.associatedShiftFunction`.
>
> Universal catenarity of `S`, which [Stacks, Tag 02JW] needs, is *derived* from `hωS` by
> [Stacks, Tag 0AWF] (`Stacks.Duality.isUniversallyCatenary_of_isDualizingComplex`). What is
> carried are the three things this repository does not have:
>
> * `δS`, `δX` with `hδS`, `hδX` — that the shift functions *are* dimension functions. This is
>   the companion half of [Stacks, Tag 0AWF], which
>   `StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/AssociatedShiftFunction.lean` states
>   explicitly that it does not prove; only the universally-catenary half is proved.
> * `hClosedImage` — that `f` carries closed points to closed points, the source's reduction to a
>   proper `f`.
> * `hClosedPoint` — the identity at a closed point over a closed point, [Stacks, Tag 0AWL],
>   proved as
>   `Stacks.Duality.isNormalizedDualizingComplex_derivedStalkOfComplex_normalizedDualizingComplex`;
>   what is missing is the bridge from that statement about normalized stalks to a value of
>   `Stacks.Duality.associatedShiftFunction`.
>
> The relation between `ω_X^•` and `ω_S^•` enters only through `hClosedPoint`, which is exactly
> where the source uses it; the complex `ω_X^•` is otherwise a parameter.

```lean
theorem associatedShiftFunction_sub_eq_trdeg {X S : Scheme.{u}}
    [IsLocallyNoetherian S] [IsLocallyNoetherian X]
    [HasDerivedCategory S.Modules] [HasDerivedCategory X.Modules]
    (f : X ⟶ S) [LocallyOfFiniteType f]
    {ωS : DerivedCategory S.Modules} (hωS : IsDualizingComplex ωS)
    (ωX : DerivedCategory X.Modules)
    (δS : DimensionFunction S) (hδS : ∀ s : S, δS s = associatedShiftFunction ωS s)
    (δX : DimensionFunction X) (hδX : ∀ y : X, δX y = associatedShiftFunction ωX y)
    (hClosedImage : ∀ y : X, IsClosed ({y} : Set X) → IsClosed ({f y} : Set S))
    (hClosedPoint : ∀ y : X, IsClosed ({y} : Set X) → IsClosed ({f y} : Set S) →
      associatedShiftFunction ωX y = associatedShiftFunction ωS (f y))
    (x : X) :
    letI := (f.residueFieldMap x).hom.toAlgebra
    associatedShiftFunction ωX x - associatedShiftFunction ωS (f x) =
      (Cardinal.toNat (Algebra.trdeg (S.residueField (f x)) (X.residueField x)) : ℤ)
```

**`Stacks.Duality.associatedShiftFunction_sub_eq_trdeg_of_upperShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DimensionFunctionTrdegCharts.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/DimensionFunctionTrdegCharts.lean#L117).

> **Stacks Project, Tag 0AWM (Lemma 48.21.2).** Let `S` be a Noetherian scheme with a
> dualizing complex `ω_S^•`, let `p : X ⟶ S` be of finite type, and let `ω_X^•` be normalized
> relative to `ω_S^•`: every point has an affine open neighbourhood `U` with
> `ω_X^•|_U ≅ (U ⟶ S)^! ω_S^•` for a compactification of `U` over `S`. Then for every `x ∈ X`,
> `δ_X(x) - δ_S(p x) = trdeg_{κ(p x)} κ(x)`, where `δ_X`, `δ_S` are the dimension functions of
> `ω_X^•`, `ω_S^•` ([Stacks, Tag 0AWF]).

```lean
theorem associatedShiftFunction_sub_eq_trdeg_of_upperShriek
    {S X : Scheme.{u}} [AlgebraicGeometry.IsNoetherian S] (p : X ⟶ S) [LocallyOfFiniteType p]
    (ωS : quasiCoherentDerivedCategory S) (hωS : IsDualizingComplex ωS.obj)
    (ωX : DerivedCategory X.Modules)
    (hωX : ∀ x : X, ∃ (U : X.Opens) (_ : IsAffine U.toScheme) (_ : x ∈ U)
      (j : CompactificationOf (Over.mk (ftsHomToBase (U.ι ≫ p)).left)),
      Nonempty ((Scheme.Modules.restrictFunctor U.ι).mapDerivedCategory.obj ωX ≅
        ((upperShriek (ftsHomToBase (U.ι ≫ p)) j).obj ωS).obj))
    (x : X) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian p
    letI := (p.residueFieldMap x).hom.toAlgebra
    associatedShiftFunction ωX x - associatedShiftFunction ωS.obj (p x) =
      (Cardinal.toNat (Algebra.trdeg (S.residueField (p x)) (X.residueField x)) : ℤ)
```

**`Stacks.Duality.associatedShiftFunction_sub_eq_trdeg_normalizedDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/NormalizedDualizingComplexNagataCharts.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/NormalizedDualizingComplexNagataCharts.lean#L120).

> **[Stacks, Tag 0AWM].** Let `S` be a Noetherian scheme with a dualizing complex `ω_S^•`, let
> `p : X ⟶ S` be of finite type and `ω_X^•` the dualizing complex normalized relative to `ω_S^•`.
> For all `x ∈ X`, `δ_X(x) - δ_S(p x) = trdeg_{κ(p x)} κ(x)`, where `δ_S`, `δ_X` are the
> dimension functions of `ω_S^•`, `ω_X^•` ([Stacks, Tag 0AWF]).

```lean
theorem associatedShiftFunction_sub_eq_trdeg_normalizedDualizingComplex (x : X) :
    haveI := hp.base_noetherian
    haveI := hp.source_noetherian
    letI := (p.residueFieldMap x).hom.toAlgebra
    associatedShiftFunction (normalizedDualizingComplex hp ωS hωS).complex.obj.obj x -
        associatedShiftFunction ωS.obj.obj (p x) =
      (Cardinal.toNat (Algebra.trdeg (S.residueField (p x)) (X.residueField x)) : ℤ)
```

## Tag 0BV5, a lemma

[Tag 0BV5](https://stacks.math.columbia.edu/tag/0BV5) in the Stacks Project.

**`Stacks.Duality.exists_fibreDim_eq_and_neg_le_of_nontrivial_stalk_homology_upperShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekFibreDimensionFinite.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekFibreDimensionFinite.lean#L64). The attribute's comment: “f^! is Stacks.Duality.upperShriek of any compactification j; O\_Y is DerivedPushforward.derivedStructureSheaf; H^i(-)\_x ≠ 0 is Nontrivial on the stalk at x of the i-th cohomology sheaf; dim\_x(X\_y) is topologicalKrullDimAt of the scheme-theoretic fibre at x, shown to be a natural number d, and the conclusion is -d ≤ i”.

> **Stacks Project, Tag 0BV5 (Lemma 48.21.3).** In Situation 48.16.1 let `f : X ⟶ Y` be a
> morphism of `FTS S` and let `x ∈ X` with image `y ∈ Y`. Then
>
>   `H^i(f^!𝒪_Y)_x ≠ 0  ⟹  -dim_x(X_y) ≤ i`,
>
> for every compactification `j` defining `f^!`. The local dimension `dim_x(X_y)` of the fibre
> (`topologicalKrullDimAt` of the scheme-theoretic fibre at `x`) is a natural number `d`, since the
> fibre is of finite type over the residue field of `y`, and the conclusion is `-d ≤ i`.

```lean
theorem exists_fibreDim_eq_and_neg_le_of_nontrivial_stalk_homology_upperShriek
    (x : X.left) (i : ℤ)
    (hi : Nontrivial (((DerivedCategory.homologyFunctor X.left.Modules i).obj
      (((upperShriek f j).obj
        (derivedStructureSheaf Y.left)).obj)).presheaf.stalk x)) :
    ∃ d : ℕ, topologicalKrullDimAt (f.left.fiber (f.left x)) (f.left.asFiber x) =
      (d : WithBot ℕ∞) ∧ -(d : ℤ) ≤ i
```

## Tag 0BV6, a lemma

[Tag 0BV6](https://stacks.math.columbia.edu/tag/0BV6) in the Stacks Project.

**`Stacks.Duality.fibreDim_bounds_of_nontrivial_stalk_homology_upperShriek_of_flat_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekFibreDimensionFlatCharts.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekFibreDimensionFlatCharts.lean#L77). The attribute's comment: “first assertion: the bounds -dim\_x(X\_y) <= i <= 0 on nonzero stalks”.

> **Stacks Project, Tag 0BV6 (Lemma 48.21.4), the first assertion.** In Situation 48.16.1 let
> `f : X ⟶ Y` be a flat morphism of `FTS S` and let `x ∈ X` with image `y ∈ Y`. Then
>
>   `H^i(f^!𝒪_Y)_x ≠ 0  ⟹  -dim_x(X_y) ≤ i ≤ 0`,
>
> for every compactification `j` defining `f^!`, the local dimension `dim_x(X_y)` being named by
> `hd`. On a chart of `Stacks.Duality.upperShriekStructureSheafCharts` this is the ring-level
> [Stacks, Tag 0E9Q].

```lean
theorem fibreDim_bounds_of_nontrivial_stalk_homology_upperShriek_of_flat_unconditional
    [Flat f.left] (x : X.left) (d : ℕ)
    (hd : topologicalKrullDimAt (f.left.fiber (f.left x)) (f.left.asFiber x) =
      (d : WithBot ℕ∞))
    (i : ℤ)
    (hi : Nontrivial (((DerivedCategory.homologyFunctor X.left.Modules i).obj
      (((upperShriek f j).obj
        (derivedStructureSheaf Y.left)).obj)).presheaf.stalk x)) :
    -(d : ℤ) ≤ i ∧ i ≤ 0
```

**`Stacks.Duality.hasTorAmplitude_derivedScalarRestriction_upperShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekFibreDimensionFlatCharts.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekFibreDimensionFlatCharts.lean#L118). The attribute's comment: “second assertion: Tor amplitude in [-d, 0] over f^\{-1}O\_Y when all fibres have dimension at most d”.

> **Stacks Project, Tag 0BV6 (Lemma 48.21.4), the second assertion.** In Situation 48.16.1 let
> `f : X ⟶ Y` be a flat morphism of `FTS S` all of whose fibres have dimension at most `d`. Then
> `f^!𝒪_Y` has Tor amplitude in `[-d, 0]` as an object of `D(X, f^{-1}𝒪_Y)`, for every
> compactification `j` defining `f^!`.
>
> By [Stacks, Tag 09U9] this is a statement about the derived stalks read over the local rings of
> `Y`; on a chart of `Stacks.Duality.upperShriekStructureSheafCharts` it is the Tor amplitude clause
> of the ring-level [Stacks, Tag 0E9Q].

```lean
theorem hasTorAmplitude_derivedScalarRestriction_upperShriek [Flat f.left] (d : ℕ)
    (hd : ∀ y : Y.left, topologicalKrullDim (f.left.fiber y) ≤ (d : WithBot ℕ∞)) :
    Stacks.Cohomology.TorAmplitude.HasTorAmplitude
      (RingedSpace.inverseImage Y.left.toRingedSpace f.left.base)
      ((Scheme.Hom.derivedScalarRestriction f.left).obj (relativeDualizingComplexObj f j))
      (-(d : ℤ)) 0
```

## Tag 0E9V, a lemma

[Tag 0E9V](https://stacks.math.columbia.edu/tag/0E9V) in the Stacks Project.

**`Stacks.Duality.neg_le_and_propertySkModule_stalk_homology_upperShriek_of_residueTrdeg_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekTranscendenceDegreeSerre.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekTranscendenceDegreeSerre.lean#L53). The attribute's comment: “both conclusions: the vanishing H^i(f^! O\_Y)\_x nonzero implies -r <= i, and the (S\_2) property of the stalk H^\{-r}(f^! O\_Y)\_x as an O\_\{X,x}-module”.

> **Stacks Project, Tag 0E9V (Lemma 48.21.5).** In Situation [Stacks, Tag 0F42], let
> `f : X ⟶ Y` be a morphism of `FTS S` and let `x ∈ X` with image `y = f x`.  Assume `𝒪_{Y, y}` is
> Cohen–Macaulay and `trdeg_{κ(f ξ)} κ(ξ) ≤ r` for every generic point `ξ` of an irreducible
> component of `X` containing `x`.  Then `H^i(f^!𝒪_Y)_x ≠ 0` implies `-r ≤ i`, and the stalk
> `H^{-r}(f^!𝒪_Y)_x` is `(S₂)` as an `𝒪_{X,x}`-module (it is a finite `𝒪_{X,x}`-module by
> `module_finite_modulesStalk_homology_upperShriek`).  Here `f^!` is `upperShriek f j` for any
> compactification `j`.

```lean
theorem neg_le_and_propertySkModule_stalk_homology_upperShriek_of_residueTrdeg_le
    (x : X.left) (r : ℕ)
    (hCM : IsCohenMacaulayLocalRing (Y.left.presheaf.stalk (f.left.base x)))
    (htrdeg : ∀ ξ : X.left, closure {ξ} ∈ irreducibleComponents X.left → x ∈ closure {ξ} →
      Stacks.Chow.residueTrdeg f.left ξ ≤ (r : Cardinal)) :
    (∀ i : ℤ, Nontrivial (((DerivedCategory.homologyFunctor X.left.Modules i).obj
        (((upperShriek f j).obj (derivedStructureSheaf Y.left)).obj)).presheaf.stalk x) →
        -(r : ℤ) ≤ i) ∧
    letI := module_finite_modulesStalk_homology_upperShriek f j x (-(r : ℤ))
    PropertySkModule (X.left.presheaf.stalk x) ((modulesStalkFunctor x).obj
      ((DerivedCategory.homologyFunctor X.left.Modules (-(r : ℤ))).obj
        (((upperShriek f j).obj (derivedStructureSheaf Y.left)).obj))) 2
```

## Tag 0BV7, a lemma

[Tag 0BV7](https://stacks.math.columbia.edu/tag/0BV7) in the Stacks Project.

**`Stacks.Duality.exists_isCoherent_isFlatOver_iso_single`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekQuasiFinite.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekQuasiFinite.lean#L141).

> **Stacks Project, Tag 0BV7 (Lemma 48.21.6).** In Situation 48.16.1 let `f : X ⟶ Y` be a
> morphism of `FTS S`. If `f` is flat and quasi-finite, then `f^!𝒪_Y = ω_{X/Y}[0]` for some
> coherent `𝒪_X`-module `ω_{X/Y}` flat over `Y`, for every compactification `j` defining `f^!`.
>
> The fibres are discrete, so by [Stacks, Tag 0BV6] `f^!𝒪_Y` is concentrated in degree `0` and
> has Tor amplitude `[0, 0]` over `Y`; its cohomology sheaves are coherent by the chart models.

```lean
theorem exists_isCoherent_isFlatOver_iso_single [Flat f.left] [LocallyQuasiFinite f.left] :
    ∃ ω : X.left.Modules, _root_.SheafOfModules.IsCoherent ω ∧
      IsFlatOver f.left.toLRSHom.toShHom ω ∧
      Nonempty (relativeDualizingComplexObj f j ≅
        (DerivedCategory.singleFunctor X.left.Modules 0).obj ω)
```

## Tag 0BV8, a lemma

[Tag 0BV8](https://stacks.math.columbia.edu/tag/0BV8) in the Stacks Project.

**`Stacks.Duality.exists_isCoherent_isFlatOver_iso_shift_upperShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekChartConsequences.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekChartConsequences.lean#L70).

> Let `S` be Noetherian and `f : X ⟶ Y` a Cohen–Macaulay morphism of `FTS S`. Then
> `f^!𝒪_Y = ω_{X/Y}[d]` for a coherent `𝒪_X`-module `ω_{X/Y}` flat over `Y`, where `d` is the
> locally constant relative dimension of `X` over `Y`: on the open where the relative dimension is
> `d`, `f^!𝒪_Y` is `ω_{X/Y}` placed in degree `-d`.

```lean
theorem exists_isCoherent_isFlatOver_iso_shift_upperShriek
    (hCM : f.left.IsCohenMacaulay (isLocallyNoetherian_fiber_left f)) :
    letI h := (isCohenMacaulay_iff_flat_and_fibers f.left (isLocallyNoetherian_fiber_left f)).mp hCM
    letI : Flat f.left := h.1
    letI := locallyOfFinitePresentation_left f
    ∃ ω : X.left.Modules, ω.IsCoherent ∧ IsFlatOver f.left.toLRSHom.toShHom ω ∧
      ∀ d : ℕ, Nonempty ((Scheme.Modules.restrictFunctor (relativeDimensionOpen f.left h.2 d).ι
          ).mapDerivedCategory.obj (relativeDualizingComplexObj f j) ≅
        ((DerivedCategory.singleFunctor _ 0).obj
          ((Scheme.Modules.restrictFunctor (relativeDimensionOpen f.left h.2 d).ι).obj ω))⟦
            (d : ℤ)⟧)
```

## Tag 0BV9, a remark

[Tag 0BV9](https://stacks.math.columbia.edu/tag/0BV9) in the Stacks Project.

**`Stacks.Duality.NormalizedOnOpens.newShriekStructureSheaf_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekRelativeDualizingComplex.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekRelativeDualizingComplex.lean#L98). The attribute's comment: “Lemmas 0BV5, 0BV6 (both assertions), 0BV7 and 0BV8 with f^! replaced by f\_new^! = D\_X o Lf^* o D\_Y, for every morphism of schemes of finite type over a Noetherian base with a dualizing complex, separated or not”.

> **Stacks Project, Tag 0BV9 (Remark 48.21.7).** Let `S` be a Noetherian scheme endowed with a
> dualizing complex `ω_S^•`, and let `f : X ⟶ Y` be a morphism of schemes of finite type over `S`,
> not necessarily separated. With `ω_X^•`, `ω_Y^•` normalized relative to `ω_S^•` and
> `f_new^! 𝒪_Y = D_X(Lf^* D_Y(𝒪_Y))`, Lemmas 0BV5, 0BV6, 0BV7 and 0BV8 hold with `f^!` replaced
> by `f_new^!`:
>
> 1. (0BV5) for `x ∈ X` with image `y`, `H^i(f_new^! 𝒪_Y)_x ≠ 0 ⟹ -dim_x(X_y) ≤ i`;
> 2. (0BV6) if `f` is flat, then `H^i(f_new^! 𝒪_Y)_x ≠ 0 ⟹ -dim_x(X_y) ≤ i ≤ 0`, and if all
>    fibres of `f` have dimension `≤ d`, then `f_new^! 𝒪_Y` has Tor amplitude in `[-d, 0]` as an
>    object of `D(X, f^{-1}𝒪_Y)`;
> 3. (0BV7) if `f` is flat and quasi-finite, then `f_new^! 𝒪_Y = ω_{X/Y}[0]` for some coherent
>    `𝒪_X`-module `ω_{X/Y}` flat over `Y`;
> 4. (0BV8) if `f` is Cohen–Macaulay, then `f_new^! 𝒪_Y = ω_{X/Y}[d]` for some coherent
>    `𝒪_X`-module `ω_{X/Y}` flat over `Y`, where `d` is the locally constant relative dimension of
>    `X` over `Y`: on the open and closed locus where the relative dimension is `d`, `f_new^! 𝒪_Y`
>    is `ω_{X/Y}` placed in degree `-d`.
>
> The local dimension `dim_x(X_y)` is named by a natural number `d`.

```lean
theorem newShriekStructureSheaf_spec :
    -- Lemma 0BV5
    (∀ (x : X) (d : ℕ), topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) = (d : WithBot ℕ∞) →
      ∀ i : ℤ, Nontrivial (((@DerivedCategory.homologyFunctor X.Modules _ _
        (PerfectApproximation.standardModel X) i).obj
          (newShriekStructureSheaf c f 𝒦X 𝒦Y)).presheaf.stalk x) → -(d : ℤ) ≤ i) ∧
    -- Lemma 0BV6
    (Flat f →
      (∀ (x : X) (d : ℕ),
        topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) = (d : WithBot ℕ∞) →
        ∀ i : ℤ, Nontrivial (((@DerivedCategory.homologyFunctor X.Modules _ _
          (PerfectApproximation.standardModel X) i).obj
            (newShriekStructureSheaf c f 𝒦X 𝒦Y)).presheaf.stalk x) → -(d : ℤ) ≤ i ∧ i ≤ 0) ∧
      ∀ d : ℕ, (∀ y : Y, topologicalKrullDim (f.fiber y) ≤ (d : WithBot ℕ∞)) →
        letI := HasDerivedCategory.standard (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace)
        letI := HasDerivedCategory.standard
          (StrictlyPerfect.OXMod.{u, u} (RingedSpace.inverseImage Y.toRingedSpace f.base))
        Stacks.Cohomology.TorAmplitude.HasTorAmplitude
          (RingedSpace.inverseImage Y.toRingedSpace f.base)
          ((Scheme.Hom.derivedScalarRestriction f).obj (newShriekStructureSheaf c f 𝒦X 𝒦Y))
          (-(d : ℤ)) 0) ∧
    -- Lemma 0BV7
    (Flat f → LocallyQuasiFinite f →
      letI := PerfectApproximation.standardModel X
      ∃ ω : X.Modules, ω.IsCoherent ∧ IsFlatOver f.toLRSHom.toShHom ω ∧
        Nonempty ((newShriekStructureSheaf c f 𝒦X 𝒦Y : DerivedCategory X.Modules) ≅
          (DerivedCategory.singleFunctor X.Modules 0).obj ω)) ∧
    -- Lemma 0BV8
    (∀ hCM : f.IsCohenMacaulay
        (isLocallyNoetherian_fiber_of_isFiniteTypeOverNoetherian (hp := hp) hpe),
      letI h := (isCohenMacaulay_iff_flat_and_fibers f
        (isLocallyNoetherian_fiber_of_isFiniteTypeOverNoetherian (hp := hp) hpe)).mp hCM
      letI : Flat f := h.1
      letI := locallyOfFinitePresentation_of_isFiniteTypeOverNoetherian (hp := hp) (hq := hq) hpe
      letI := PerfectApproximation.standardModel X
      ∃ ω : X.Modules, ω.IsCoherent ∧ IsFlatOver f.toLRSHom.toShHom ω ∧
        ∀ d : ℕ,
          letI := PerfectApproximation.standardModel (relativeDimensionOpen f h.2 d).toScheme
          Nonempty ((Scheme.Modules.restrictFunctor (relativeDimensionOpen f h.2 d).ι
              ).mapDerivedCategory.obj
                (newShriekStructureSheaf c f 𝒦X 𝒦Y : DerivedCategory X.Modules) ≅
            ((DerivedCategory.singleFunctor _ 0).obj
              ((Scheme.Modules.restrictFunctor (relativeDimensionOpen f h.2 d).ι).obj ω))⟦
                (d : ℤ)⟧))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.21, Tag 0BV4](https://stacks.math.columbia.edu/tag/0BV4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
