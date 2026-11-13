---
declaration: section
origin: cited
lean: AlgebraicGeometry.DeterminantTwoTerm.specDet, AlgebraicGeometry.DeterminantTwoTerm.specDelta, AlgebraicGeometry.DeterminantTwoTerm.specDet_map_specDelta, AlgebraicGeometry.DeterminantTwoTerm.specDetPresentationIso, AlgebraicGeometry.DeterminantTwoTerm.specDetPresentationIso_specDelta, AlgebraicGeometry.DeterminantTwoTerm.determinantFunctor, AlgebraicGeometry.DeterminantTwoTerm.determinantSection, AlgebraicGeometry.DeterminantTwoTerm.determinantChartPresentationIso
statement: formalized
proof: formalized
---

# 36.39 Determinants of complexes

Section 36.39 of the Stacks Project, [Tag 0FJW](https://stacks.math.columbia.edu/tag/0FJW). 2 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FJX, a lemma

[Tag 0FJX](https://stacks.math.columbia.edu/tag/0FJX) in the Stacks Project.

**`AlgebraicGeometry.DeterminantTwoTerm.specDet`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeterminantTwoTermAffine.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeterminantTwoTermAffine.lean#L285). The attribute's comment: “the determinant functor, for an affine scheme”.

> The determinant functor on `Spec R`, from the groupoid of perfect objects of `D(𝒪_{Spec R})` of
> Tor amplitude in `[-1, 0]` and their isomorphisms to the groupoid of invertible
> `𝒪_{Spec R}`-modules and their isomorphisms.
>
> It is the determinant of More on Algebra, Section 0FJI, transported along the identification of
> the source groupoid with the ring-level one and along the associated-sheaf functor.

```lean
def specDet (R : CommRingCat.{u}) :
    Core (PerfectTwoTermAmplitude (Spec R)) ⥤ Core (InvertibleModuleCat (Spec R))
```

**`AlgebraicGeometry.DeterminantTwoTerm.specDelta`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeterminantTwoTermAffine.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeterminantTwoTermAffine.lean#L315). The attribute's comment: “the canonical global section δ(L) of the determinant of a rank-zero object, for an affine scheme”.

> The canonical global section `δ(L)` of the determinant of a rank-zero object of the source
> groupoid on `Spec R`: the canonical element of More on Algebra, Section 0FJI, read as a global
> section.

```lean
def specDelta (R : CommRingCat.{u}) (L : PerfectTwoTermAmplitude (Spec R))
    (hL : IsRankZeroSpec R L) : Γ(((specDet R).obj ⟨L⟩).of.obj, ⊤)
```

**`AlgebraicGeometry.DeterminantTwoTerm.specDet_map_specDelta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeterminantTwoTermAffine.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeterminantTwoTermAffine.lean#L323). The attribute's comment: “the compatibility det(a)(δ(L)) = δ(K) of the canonical global section with isomorphisms, for an affine scheme”.

> For every isomorphism `a : L ⟶ K` of rank-zero objects of the source groupoid on `Spec R`,
> `det(a)(δ(L)) = δ(K)`.

```lean
theorem specDet_map_specDelta (R : CommRingCat.{u}) {L K : PerfectTwoTermAmplitude (Spec R)}
    (a : (⟨L⟩ : Core (PerfectTwoTermAmplitude (Spec R))) ⟶ ⟨K⟩)
    (hL : IsRankZeroSpec R L) (hK : IsRankZeroSpec R K) :
    Scheme.Modules.Hom.app
        ((IsInvertibleProperty (Spec R)).ι.map ((specDet R).map a).iso.hom) ⊤
        (specDelta R L hL) = specDelta R K hK
```

**`AlgebraicGeometry.DeterminantTwoTerm.specDetPresentationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeterminantTwoTermAffine.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeterminantTwoTermAffine.lean#L337). The attribute's comment: “the construction is locally the one of More on Algebra, Section 0FJI: on an affine scheme the determinant is the determinant line of a two-term finite-projective presentation”.

> The determinant on `Spec R` of an object of the source groupoid is the sheaf associated with
> the determinant line of More on Algebra, Section 0FJI of any two-term finite-projective
> presentation of the corresponding complex of `R`-modules. Such a presentation always exists,
> `TwoTermDeterminant.presentation` being one.

```lean
def specDetPresentationIso (R : CommRingCat.{u}) (L : PerfectTwoTermAmplitude (Spec R))
    (P : TwoTermPresentation (sourceComplex R L).obj) :
    letI := P.finite (-1)
    letI := P.projective (-1)
    letI := P.finite 0
    letI := P.projective 0
    ((specDet R).obj ⟨L⟩).of.obj ≅
      tilde (ModuleCat.of R
        (TwoTermComplex.determinantLine (P.complex.d (-1) 0).hom))
```

**`AlgebraicGeometry.DeterminantTwoTerm.specDetPresentationIso_specDelta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeterminantTwoTermAffine.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeterminantTwoTermAffine.lean#L354). The attribute's comment: “the canonical global section is locally the canonical element of More on Algebra, Section 0FJI: on an affine scheme it is the determinant of the differential of a two-term finite-projective presentation”.

> Under the identification of the determinant with the determinant line of a rank-zero two-term
> finite-projective presentation, the canonical global section is the canonical element of More on
> Algebra, Section 0FJI of that presentation.

```lean
theorem specDetPresentationIso_specDelta (R : CommRingCat.{u})
    (L : PerfectTwoTermAmplitude (Spec R)) (P : TwoTermPresentation (sourceComplex R L).obj)
    (hP : P.IsRankZero) (hL : IsRankZeroSpec R L) :
    letI := P.finite (-1)
    letI := P.projective (-1)
    letI := P.finite 0
    letI := P.projective 0
    Scheme.Modules.Hom.app (specDetPresentationIso R L P).hom ⊤ (specDelta R L hL) =
      (tilde.toOpen (ModuleCat.of R
        (TwoTermComplex.determinantLine (P.complex.d (-1) 0).hom)) ⊤).hom
          (TwoTermComplex.delta (P.complex.d (-1) 0).hom hP)
```

**`AlgebraicGeometry.DeterminantTwoTerm.determinantFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeterminantTwoTermGlobal.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeterminantTwoTermGlobal.lean#L158). The attribute's comment: “part (1): the determinant functor, from the groupoid of perfect objects of Tor amplitude in [-1, 0] and their isomorphisms to the groupoid of invertible modules and their isomorphisms, on an arbitrary scheme”.

> The determinant functor on an arbitrary scheme, from the groupoid of perfect objects of
> `D(𝒪_X)` of Tor-amplitude in `[-1, 0]` and their isomorphisms to the groupoid of invertible
> `𝒪_X`-modules and their isomorphisms.
>
> The value at `L` is the invertible module glued from the determinants of `L` on the affine opens
> of `X`, and the value at an isomorphism is glued from the determinants of its restrictions to the
> affine charts.

```lean
def determinantFunctor (X : Scheme.{u}) :
    Core (PerfectTwoTermAmplitude X) ⥤ Core (InvertibleModuleCat X)
```

**`AlgebraicGeometry.DeterminantTwoTerm.determinantSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeterminantTwoTermGlobal.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeterminantTwoTermGlobal.lean#L200). The attribute's comment: “part (2): the canonical global section δ(L) of the determinant of a rank-zero object, on an arbitrary scheme”.

> The canonical global section `δ(L)` of the determinant of a rank-zero perfect object of
> `D(𝒪_X)` of Tor-amplitude in `[-1, 0]` on an arbitrary scheme: the global section glued from the
> canonical elements of More on Algebra, Section 0FJI on the affine charts, which are matched by the
> chart comparisons.

```lean
def determinantSection {L : PerfectTwoTermAmplitude X} (hL : IsRankZeroOn L) :
    Γ(((determinantFunctor X).obj ⟨L⟩).of.obj, ⊤)
```

**`AlgebraicGeometry.DeterminantTwoTerm.determinantChartPresentationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeterminantTwoTermGlobal.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeterminantTwoTermGlobal.lean#L229). The attribute's comment: “part (3): the construction is affine locally the one of More on Algebra, Section 0FJI — on an affine open of an arbitrary scheme the determinant is the determinant line of a two-term finite-projective presentation of the complex the object restricts to there”.

> On an affine open `V` of an arbitrary scheme `X` the determinant of `L` is the sheaf
> associated with the determinant line of More on Algebra, Section 0FJI of *any* two-term
> finite-projective presentation `P` of the complex of `Γ(X, V)`-modules that `L` restricts to on the
> chart of `V`: the restriction of the determinant to `V` is the pullback along
> `AlgebraicGeometry.IsAffineOpen.isoSpec` of that associated sheaf.
>
> The isomorphism is the glueing comparison
> `AlgebraicGeometry.AffineOpensGlue.ChartComparison.chartIso` of the datum, followed by
> `AlgebraicGeometry.DeterminantTwoTerm.chartDetPresentationIso`.

```lean
def determinantChartPresentationIso (L : PerfectTwoTermAmplitude X) (V : X.affineOpens)
    (P : TwoTermPresentation (chartComplex L V).obj) :
    letI := P.finite (-1)
    letI := P.projective (-1)
    letI := P.finite 0
    letI := P.projective 0
    Scheme.Modules.restrict ((determinantFunctor X).obj ⟨L⟩).of.obj
        (AffineOpensGlue.chart X V) ≅
      (Scheme.Modules.pullback V.2.isoSpec.hom).obj
        (tilde (ModuleCat.of Γ(X, (V.1 : X.Opens))
          (TwoTermComplex.determinantLine (P.complex.d (-1) 0).hom)))
```

**`AlgebraicGeometry.DeterminantTwoTerm.determinantFunctor_map_determinantSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeterminantTwoTermGlobalDelta.lean, line 325](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeterminantTwoTermGlobalDelta.lean#L325). The attribute's comment: “part (2): the compatibility det(a)(δ(L)) = δ(K) of the canonical global section with isomorphisms, on an arbitrary scheme”.

> For every isomorphism `a : L ⟶ K` of rank-zero perfect objects of `D(𝒪_X)` of Tor-amplitude in
> `[-1, 0]` on an arbitrary scheme `X`, the determinant of `a` carries the canonical global section
> of the determinant of `L` to that of `K`: `det(a)(δ(L)) = δ(K)`.

```lean
theorem determinantFunctor_map_determinantSection {L K : PerfectTwoTermAmplitude X}
    (a : (⟨L⟩ : Core (PerfectTwoTermAmplitude X)) ⟶ ⟨K⟩)
    (hL : IsRankZeroOn L) (hK : IsRankZeroOn K) :
    Scheme.Modules.Hom.app
        ((IsInvertibleProperty X).ι.map ((determinantFunctor X).map a).iso.hom) ⊤
        (determinantSection hL) = determinantSection hK
```

**`AlgebraicGeometry.DeterminantTwoTerm.determinantChartPresentationIso_determinantSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeterminantTwoTermGlobalDelta.lean, line 462](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeterminantTwoTermGlobalDelta.lean#L462). The attribute's comment: “part (3): the canonical global section is affine locally the canonical element of More on Algebra, Section 0FJI — on an affine open of an arbitrary scheme it is the determinant of the differential of a two-term finite-projective presentation”.

> Let `X` be a scheme, `L` a rank-zero perfect object of `D(𝒪_X)` of Tor-amplitude in `[-1, 0]`,
> `V` an affine open of `X` and `P` a rank-zero two-term finite-projective presentation of the
> complex of `Γ(X, V)`-modules that `L` restricts to on the chart of `V`. Then the canonical global
> section `δ(L)` of the determinant of `L`, restricted to `V` and read on the chart of `V` through
> `AlgebraicGeometry.DeterminantTwoTerm.chartDetRestrictPresentationIso`, is the canonical element of
> More on Algebra, Section 0FJI of `P` — the determinant of the differential of `P` — read as a
> global section of the associated sheaf of the determinant line and restricted to the image open.
>
> So the construction is affine locally the one of More on Algebra, Section 0FJI, canonical element
> included: `δ(L)` reads on an affine open as `TwoTermComplex.delta` of the differential of any
> two-term finite-projective presentation there.

```lean
theorem determinantChartPresentationIso_determinantSection {L : PerfectTwoTermAmplitude X}
    (hL : IsRankZeroOn L) (V : X.affineOpens)
    (P : TwoTermPresentation (chartComplex L V).obj) (hP : P.IsRankZero) :
    letI := P.finite (-1)
    letI := P.projective (-1)
    letI := P.finite 0
    letI := P.projective 0
    Scheme.Modules.Hom.app (chartDetRestrictPresentationIso L V P).hom
        ((V.1 : X.Opens).ι ⁻¹ᵁ (V.1 : X.Opens))
        ((chartComparison L).chartSec V (V.1 : X.Opens)
          ((chartComparison L).glued.val.map (homOfLE le_top).op (determinantSection hL))) =
      (tilde (ModuleCat.of Γ(X, (V.1 : X.Opens))
          (TwoTermComplex.determinantLine (P.complex.d (-1) 0).hom))).val.map
        (homOfLE (le_top :
          V.2.isoSpec.hom ''ᵁ ((V.1 : X.Opens).ι ⁻¹ᵁ (V.1 : X.Opens)) ≤ ⊤)).op
        ((tilde.toOpen (ModuleCat.of Γ(X, (V.1 : X.Opens))
          (TwoTermComplex.determinantLine (P.complex.d (-1) 0).hom)) ⊤).hom
          (TwoTermComplex.delta (P.complex.d (-1) 0).hom hP))
```

## Tag 0FJY, a remark

[Tag 0FJY](https://stacks.math.columbia.edu/tag/0FJY) in the Stacks Project.

**`AlgebraicGeometry.DeterminantTwoTerm.pullbackDeterminantIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeterminantTwoTermGlobal/PullbackDeterminant.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeterminantTwoTermGlobal/PullbackDeterminant.lean#L61). The attribute's comment: “(b) the canonical identification f^*det(K) → det(Lf^*K), for the determinant functor of Lemma 0FJX (determinantFunctor)”.

> **The determinant functor commutes with pullback.** For a morphism of schemes `f : X ⟶ Y` and
> a perfect object `K` of `D(𝒪_Y)` of Tor amplitude in `[-1, 0]`, the canonical identification
> `f^* det(K) ≅ det(Lf^*K)` of the values of the determinant functor of Stacks 0FJX.

```lean
def pullbackDeterminantIso :
    (Scheme.Modules.pullback f).obj ((determinantFunctor Y).obj ⟨K⟩).of.obj ≅
      ((determinantFunctor X).obj ⟨pullbackObj f K⟩).of.obj
```

**`AlgebraicGeometry.DeterminantTwoTerm.pullbackDeterminantIso_hom_pullbackSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeterminantTwoTermGlobal/PullbackDeterminant.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeterminantTwoTermGlobal/PullbackDeterminant.lean#L87). The attribute's comment: “(b) the identification f^*det(K) → det(Lf^*K) is canonical: over affine opens W ⊆ f⁻¹V it is the base change of the determinant of More on Algebra 0FJI of the complex representing K over V”.

> **The identification `f^* det(K) ≅ det(Lf^*K)` is canonical: on affine opens it is the base
> change of local determinants.** For affine opens `V ⊆ Y` and `W ⊆ f⁻¹V`, it sends the pullback of
> a section `a` of `det(K)` over `V` to the section of `det(Lf^*K)` over `W` which is the image of
> `a ∈ det(M_V)` under the base change `det(M_V) → Γ(X, W) ⊗_{Γ(Y, V)} det(M_V) = det(M'_W)` of the
> determinants of More on Algebra, Section 0FJI; the sections over affine opens are read as
> determinant modules through `globalDetSectionsEquiv`.

```lean
theorem pullbackDeterminantIso_hom_pullbackSection (V : Y.affineOpens) (W : X.affineOpens)
    (h : (W : X.Opens) ≤ f ⁻¹ᵁ V) (a : Γ(((determinantFunctor Y).obj ⟨K⟩).of.obj, V)) :
    (globalDetSectionsEquiv (pullbackObj f K) W).symm
        ((pullbackDeterminantIso f K).hom.val.app (op (W : X.Opens))
          (Scheme.Modules.pullbackSection f _ V W h a)) =
      pullbackDetMap f K V W h ((globalDetSectionsEquiv K V).symm a)
```

**`AlgebraicGeometry.DeterminantTwoTerm.pullbackDeterminantIso_hom_determinantSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeterminantTwoTermGlobal/PullbackDeterminant.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeterminantTwoTermGlobal/PullbackDeterminant.lean#L109). The attribute's comment: “(c) if K has rank 0, δ(K) pulls back to δ(Lf^*K) via f^*det(K) → det(Lf^*K), for the determinant functor of Lemma 0FJX and its canonical section (determinantSection)”.

> **The canonical global section pulls back to the canonical global section.** If `K` has rank
> zero, the identification `f^* det(K) ≅ det(Lf^*K)` carries the pullback of the canonical global
> section `δ(K)` of Stacks 0FJX to `δ(Lf^*K)`.

```lean
theorem pullbackDeterminantIso_hom_determinantSection {K : PerfectTwoTermAmplitude Y}
    (hK : IsRankZeroOn K) :
    (pullbackDeterminantIso f K).hom.val.app (op ⊤)
        (Scheme.Modules.pullbackSection f _ ⊤ ⊤ le_top (determinantSection hK)) =
      determinantSection (isRankZeroOn_pullbackObj f hK)
```

**`AlgebraicGeometry.DeterminantTwoTerm.isPerfectTwoTermAmplitude_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeterminantTwoTermPerfect.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeterminantTwoTermPerfect.lean#L174). The attribute's comment: “the derived pullback lands in the source category”. References: SGA 6 I (4.19.2), “special case”.

> **The source category is preserved by derived pullback.** For a morphism of schemes
> `f : X ⟶ Y`, the derived pullback `Lf^*K` of a perfect object `K` of `D(𝒪_Y)` of Tor amplitude in
> `[-1, 0]` is again perfect of Tor amplitude in `[-1, 0]`.

```lean
theorem isPerfectTwoTermAmplitude_derivedPullback {X Y : Scheme.{u}} (f : X ⟶ Y)
    (K : DerivedCategory Y.Modules) (hK : IsPerfectTwoTermAmplitude Y K) :
    IsPerfectTwoTermAmplitude X
      ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        f.toLRSHom.toShHom).obj K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.39, Tag 0FJW](https://stacks.math.columbia.edu/tag/0FJW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
