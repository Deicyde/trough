---
declaration: section
origin: cited
lean: Stacks.RelativeProj.Situation, Stacks.RelativeProj.Situation.sectionRingStructure_exists, Stacks.AlgebraicGeometry.RelativeProjBridge.SheafGradedAlgebra, Stacks.AlgebraicGeometry.RelativeProjBridge.SheafGradedAlgebra.resRingHom, Stacks.AlgebraicGeometry.RelativeProjBridge.SheafGradedAlgebra.resRingHom_of, Stacks.AlgebraicGeometry.RelativeProjBridge.SheafGradedAlgebra.resRingHom_id, Stacks.AlgebraicGeometry.RelativeProjBridge.SheafGradedAlgebra.resRingHom_comp, Stacks.AlgebraicGeometry.RelativeProjBridge.SheafGradedAlgebra.resRingHom_strHom
statement: formalized
proof: formalized
---

# 27.15 Relative Proj via glueing

Section 27.15 of the Stacks Project, [Tag 01NM](https://stacks.math.columbia.edu/tag/01NM). 5 tags here are carried by 34 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01NN, a situation

[Tag 01NN](https://stacks.math.columbia.edu/tag/01NN) in the Stacks Project.

**`Stacks.RelativeProj.Situation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/RelativeProjSectionRings.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/RelativeProjSectionRings.lean#L80). The attribute's comment: “the situation datum, on the SheafOfModules.GradedAlgebra substrate”. References: EGA II (8.3.1), “partial”.

> **Stacks Project, Tag 01NN.** A scheme equipped with a graded algebra over its structure
> sheaf, each of whose homogeneous pieces is quasi-coherent. The algebra is commutative and
> concentrated in nonnegative degrees.

```lean
public structure Situation
```

**`Stacks.RelativeProj.Situation.sectionRingStructure_exists`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/RelativeProjSectionRings.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/RelativeProjSectionRings.lean#L330). The attribute's comment: “graded rings of local sections”.

> **The canonical nonnegatively graded rings of local sections** of a quasi-coherent graded
> algebra, with their structure-sheaf maps and restriction maps.

```lean
public theorem sectionRingStructure_exists (s : Situation.{u}) :
    Nonempty (s.SectionRingStructure)
```

**`Stacks.AlgebraicGeometry.RelativeProjBridge.SheafGradedAlgebra`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjBridge/Algebra.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjBridge/Algebra.lean#L85). The attribute's comment: “the situation datum, on the sheaf-level bilinear-multiplication substrate”.

> A commutative, nonnegatively graded, quasi-coherent graded `𝒪_S`-algebra, given as a family
> of sheaves of modules with an `𝒪_S`-bilinear multiplication and a global unit.
>
> This is the sheaf-level data of Situation 01NN.

```lean
public structure SheafGradedAlgebra (S : Scheme.{u})
```

**`Stacks.AlgebraicGeometry.RelativeProjBridge.SheafGradedAlgebra.resRingHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjBridge/Basic.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjBridge/Basic.lean#L162). The attribute's comment: “graded rings of local sections”.

> Restriction of the graded rings of sections, as a ring homomorphism.

```lean
public noncomputable def resRingHom {U V : S.Opens} (h : U ≤ V) :
    A.sectionRing V →+* A.sectionRing U
```

**`Stacks.AlgebraicGeometry.RelativeProjBridge.SheafGradedAlgebra.resRingHom_of`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjBridge/Basic.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjBridge/Basic.lean#L175). The attribute's comment: “graded rings of local sections”.

> On a homogeneous summand, `resRingHom` is restriction of homogeneous sections.

```lean
public theorem resRingHom_of {U V : S.Opens} (h : U ≤ V) {n : ℕ} (y : A.sectionPieces V n) :
    A.resRingHom h (DirectSum.of (A.sectionPieces V) n y) =
      DirectSum.of (A.sectionPieces U) n (A.resPiece h n y)
```

**`Stacks.AlgebraicGeometry.RelativeProjBridge.SheafGradedAlgebra.resRingHom_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjBridge/Basic.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjBridge/Basic.lean#L194). The attribute's comment: “graded rings of local sections”.

> Restriction along the identity of an open is the identity.

```lean
public theorem resRingHom_id (U : S.Opens) : A.resRingHom (le_refl U) = RingHom.id _
```

**`Stacks.AlgebraicGeometry.RelativeProjBridge.SheafGradedAlgebra.resRingHom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjBridge/Basic.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjBridge/Basic.lean#L202). The attribute's comment: “graded rings of local sections”.

> Restriction along a composite of inclusions is the composite of the restrictions.

```lean
public theorem resRingHom_comp {U V W : S.Opens} (hUV : U ≤ V) (hVW : V ≤ W) :
    A.resRingHom (hUV.trans hVW) = (A.resRingHom hUV).comp (A.resRingHom hVW)
```

**`Stacks.AlgebraicGeometry.RelativeProjBridge.SheafGradedAlgebra.resRingHom_strHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjBridge/Basic.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjBridge/Basic.lean#L212). The attribute's comment: “graded rings of local sections”.

> Restriction is compatible with the structure maps from the functions on the opens.

```lean
public theorem resRingHom_strHom {U V : S.Opens} (h : U ≤ V) (r : Γ(S, V)) :
    A.resRingHom h (A.strHom V r) = A.strHom U (S.presheaf.map (homOfLE h).op r)
```

**`Stacks.AlgebraicGeometry.RelativeProjBridge.SheafGradedAlgebra.instGCommRing`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjBridge/SectionRing.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjBridge/SectionRing.lean#L136). The attribute's comment: “graded rings of local sections”.

> **Stacks 01NN, the graded rings of local sections.** The homogeneous sections of a
> quasi-coherent graded algebra over an open form a graded commutative ring, whose multiplication
> and unit are the algebra's own: see the characterizing equations below.

```lean
public noncomputable instance instGCommRing : DirectSum.GCommRing (A.sectionPieces U)
```

**`Stacks.AlgebraicGeometry.RelativeProjBridge.SheafGradedAlgebra.strHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjBridge/SectionRing.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjBridge/SectionRing.lean#L244). The attribute's comment: “graded rings of local sections”.

> The structure map from the sections of `𝒪_S` over an open to the graded ring of sections
> of `A`: a function is sent to its multiple of the unit.

```lean
public noncomputable def strHom : Γ(S, U) →+* A.sectionRing U
```

**`Stacks.AlgebraicGeometry.RelativeProjBridge.SheafGradedAlgebra.strHom_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjBridge/SectionRing.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjBridge/SectionRing.lean#L256). The attribute's comment: “graded rings of local sections”.

> The structure map sends a function to its multiple of the unit, in degree `0`.

```lean
public theorem strHom_apply (r : Γ(S, U)) :
    A.strHom U r = DirectSum.of (A.sectionPieces U) 0 (r • A.one U)
```

**`AlgebraicGeometry.Space.relativeProjChartAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GradedAlgebraChartRestriction.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GradedAlgebraChartRestriction.lean#L279). The attribute's comment: “the restriction of a graded algebra on an algebraic space to an étale scheme chart, as graded algebra data on the chart; granted quasi-coherence of the module restrictions of the homogeneous pieces, which is the étale-to-Zariski direction of Descent 03DX and is carried here in the same form as in the neighbouring Tag 060Q”.

> **The restriction `𝒜|_V` of a graded algebra on an algebraic space to an étale scheme chart,
> as graded algebra data in the sense of Situation 01NN.**  This is the object the scheme-level
> theory of the relative Proj consumes, so it is what makes a reduction to the case of schemes on
> an étale chart possible.
>
> Commutativity and concentration in nonnegative degrees are transported from `𝒜`.  Quasi-coherence
> of the restricted pieces is the hypothesis `hqc`; see the implementation notes for why it is
> carried and why it is an input rather than a disguised conclusion.

```lean
def relativeProjChartAlgebra
    (hcomm : ∀ (i j : ℤ) (W : (SmallEtale B S hS X.1)ᵒᵖ) (a : (A.piece i).val.obj W)
      (b : (A.piece j).val.obj W), HEq ((A.mul i j).app W a b) ((A.mul j i).app W b a))
    (hneg : ∀ (n : ℤ), n < 0 → ∀ (W : (SmallEtale B S hS X.1)ᵒᵖ)
      (y : (A.piece n).val.obj W), y = 0)
    (hqc : ∀ n : ℤ, (restrictToChartScheme B S hS X.1 X.2 (A.piece n) V).IsQuasicoherent) :
    SheafGradedAlgebra (chartScheme V)
```

**`AlgebraicGeometry.Space.relativeProjChartSituation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjChartSituation.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjChartSituation.lean#L206). The attribute's comment: “the relative Proj situation carried on an étale scheme chart by the restriction of a graded algebra on an algebraic space, granted quasi-coherence of the module restrictions of the homogeneous pieces, which is the étale-to-Zariski direction of Descent 03DX”.

> **The tie: the relative Proj situation of Stacks 01NN carried by the restriction of `𝒜` to an
> étale scheme chart.**
>
> The base is the scheme underlying the chart and the graded algebra is the restriction `𝒜|_V` of
> `AlgebraicGeometry.Space.chartSheafAlgebra`.  Commutativity and concentration in nonnegative
> degrees are the corresponding fields of the space-level situation, transported; quasi-coherence of
> the restricted pieces is the hypothesis `hqc`, for the reason given in the implementation notes.
>
> This is the datum that `AlgebraicGeometry.Space.RelativeProjChart` lacks: that structure takes an
> arbitrary situation `t` on the chart, with no field relating it to the graded algebra on the
> space.

```lean
def relativeProjChartSituation
    (hqc : ∀ n : ℤ, (restrictToChartScheme s.site s.base s.containsBase s.space.1 s.space.2
      (s.algebra.piece n) V).IsQuasicoherent) :
    Stacks.RelativeProj.Situation.{u}
```

## Tag 01NO, a lemma

[Tag 01NO](https://stacks.math.columbia.edu/tag/01NO) in the Stacks Project.

**`Stacks.Blowup.isOpenImmersion_proj_map_reesRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesSheafData.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesSheafData.lean#L127). The attribute's comment: “open immersion, for the Rees algebra of a quasi-coherent ideal sheaf”.

> For affine opens `U ≤ V`, the comparison morphism of charts
> `Proj (Γ(S, U)[ℐ(U)t]) ⟶ Proj (Γ(S, V)[ℐ(V)t])` is an open immersion.

```lean
theorem isOpenImmersion_proj_map_reesRestrict {U V : S.affineOpens} (h : U ≤ V) :
    IsOpenImmersion (Proj.map (reesRestrict ℐ h) (reesIrrelevant_le ℐ h))
```

**`Stacks.Blowup.opensRange_proj_map_reesRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesSheafData.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesSheafData.lean#L176). The attribute's comment: “image is the preimage, for the Rees algebra of a quasi-coherent ideal sheaf”.

> For affine opens `U ≤ V`, the image of the comparison morphism of charts is the preimage of
> `U` in the chart over `V`.

```lean
theorem opensRange_proj_map_reesRestrict {U V : S.affineOpens} (h : U ≤ V) :
    Stacks.RelativeProj.chartToOpen (fun W : S.affineOpens ↦ reesGrading (ℐ.ideal W)) V
        (reesBase ℐ V) ⁻¹ᵁ (S.homOfLE h).opensRange =
      (Proj.map (reesRestrict ℐ h) (reesIrrelevant_le ℐ h)).opensRange
```

**`Stacks.AlgebraicGeometry.ProjInclusionTwist.isIso_projInclusionTwistMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjInclusionTwist/Basic.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjInclusionTwist/Basic.lean#L201). The attribute's comment: “canonical twist isomorphisms”.

> **Tag 01NO's transported comparison map on the `n`-th twist is an isomorphism**, for every
> `n : ℤ` and for an arbitrary inclusion of affine opens of the base, with no hypothesis beyond
> that situation.

```lean
public theorem isIso_projInclusionTwistMap (U V : S.Opens) (h : U ≤ V) (hU : IsAffineOpen U)
    (hV : IsAffineOpen V) (n : ℤ) :
    IsIso (projInclusionTwistMap A U V h hU hV n)
```

**`Stacks.AlgebraicGeometry.RelativeProj.projInclusionDomain_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProj/Assembled.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProj/Assembled.lean#L154). The attribute's comment: “the everywhere-defined morphism”.

> **Tag 01NO, the everywhere-defined morphism.** For an inclusion `U ⊆ V` of affine opens of
> the base, the morphism of projective spectra induced by restriction of homogeneous sections is
> defined on all of `Proj Γ(U, A)`.
>
> This is `Stacks.AlgebraicGeometry.RelativeProjGeneral.mapDomain_res_eq_top_of_le_opens` for the
> graded algebra the bridge produces.

```lean
public theorem projInclusionDomain_eq_top (U V : S.Opens) (h : U ≤ V)
    (hU : IsAffineOpen U) (hV : IsAffineOpen V) :
    mapDomain (A.grading V) (A.grading U) (A.res h) = ⊤
```

**`Stacks.AlgebraicGeometry.RelativeProj.projInclusion_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProj/Assembled.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProj/Assembled.lean#L184). The attribute's comment: “the cartesian square”.

> **Tag 01NO, the cartesian square.** For an inclusion `U ⊆ V` of affine opens of the base,
> the square formed by the induced morphism of projective spectra, the two structure morphisms to
> the affine opens and the inclusion `U ⊆ V` is cartesian.
>
> This is `Stacks.AlgebraicGeometry.RelativeProjGeneral.isPullback_transition_of_le_opens` for the
> graded algebra the bridge produces.

```lean
public theorem projInclusion_isPullback (U V : S.Opens) (h : U ≤ V)
    (hU : IsAffineOpen U) (hV : IsAffineOpen V) :
    IsPullback (projInclusionMap A U V h hU hV) (projInclusionToOpen A U hU)
      (projInclusionToOpen A V hV) (S.homOfLE h)
```

**`Stacks.RelativeProj.Situation.projInclusionDomain_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProj/Charts/Basic.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProj/Charts/Basic.lean#L237). The attribute's comment: “the everywhere-defined morphism”.

> **Stacks Project, Tag 01NO.** The morphism of projective spectra induced by restriction of
> homogeneous sections along an inclusion of affine opens is defined on all of
> `Proj (s.sectionRingGrading U)`.

```lean
public theorem projInclusionDomain_eq_top (hU : IsAffineOpen U) (hV : IsAffineOpen V) :
    mapDomain (s.sectionRingGrading V) (s.sectionRingGrading U)
      (gradedSectionRestriction s U V h) = ⊤
```

**`Stacks.RelativeProj.Situation.projInclusion_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProj/Charts/Descent.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProj/Charts/Descent.lean#L299). The attribute's comment: “the cartesian square”.

> **Stacks Project, Tag 01NO.** The square formed by the comparison morphism of charts, the two
> chart structure morphisms and the inclusion of affine opens of the base is cartesian.

```lean
public theorem projInclusion_isPullback {W W' : s.base.Opens} (h : W ≤ W')
    (hW : IsAffineOpen W) (hW' : IsAffineOpen W') :
    IsPullback (projInclusionMap s W W' h hW hW') (projInclusionToOpen s W hW)
      (projInclusionToOpen s W' hW') (s.base.homOfLE h)
```

**`Stacks.RelativeProj.Situation.isIso_twistMap_gradedSectionRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProj/Twist/Descent.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProj/Twist/Descent.lean#L242). The attribute's comment: “the canonical twist isomorphisms θ, for an arbitrary inclusion of affine opens of the base; their compatibility with the multiplication maps is not covered”.

> **Stacks Project, Tag 01NO.** The canonical comparison
> `θ : r^* 𝒪_{Proj 𝒜(W')}(n) ⟶ 𝒪_{Proj 𝒜(W)}(n)` attached to an inclusion `W ≤ W'` of affine opens
> of the base is an isomorphism, for every `n : ℤ`.

```lean
theorem isIso_twistMap_gradedSectionRestriction {W W' : s.base.Opens} (h : W ≤ W')
    (hW : IsAffineOpen W) (hW' : IsAffineOpen W') (n : ℤ) :
    IsIso (twistMap (gradedSectionRestriction s W W' h)
      (irrelevant_le_map_gradedSectionRestriction s W W' h hW hW') n)
```

**`Stacks.ProjTwistComparison.isIso_twistMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProj/Twist/Iso.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProj/Twist/Iso.lean#L151). The attribute's comment: “the twist comparison is an isomorphism, for a degreewise localization away from a degree-zero element; the descent to a general affine open and the compatibility with the multiplication maps are not covered”.

> **The canonical twist comparison of a degreewise localization is an isomorphism.** If `φ` is,
> in each degree, the localization of `𝒜` away from a degree-zero element `g`, then for every `n`
> the comparison `θ : r^* 𝒪_{Proj 𝒜}(n) ⟶ 𝒪_{Proj ℬ}(n)` is an isomorphism.

```lean
theorem isIso_twistMap {g : A} (h : Stacks.GradedLocalization.IsAwayDegreewise φ g)
    (hg : g ∈ 𝒜 0) : IsIso (twistMap φ hφ n)
```

**`Stacks.ProjTwistComparison.sectionsMap_twistSectionsMul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProj/Twist/Multiplication.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProj/Twist/Multiplication.lean#L158). The attribute's comment: “the compatibility of the twist comparison with the multiplication of twisted sections, i.e. with the pointwise product of fraction families; the compatibility with the sheaf-level multiplication maps 𝒪(p) ⊗ 𝒪(q) ⟶ 𝒪(p + q) is not covered”.

> **The twist comparison is compatible with the multiplication of twisted sections.** The
> comparison of a product of a degree-`p` and a degree-`q` section is the product of the
> comparisons; this is the multiplicativity of the comparison of local rings, applied at each
> point.

```lean
theorem sectionsMap_twistSectionsMul (p q : ℤ) (U : Opens (ProjectiveSpectrum.top 𝒜))
    (a : moduleSections 𝒜 (twistGrading (S := A) 𝒜 p) U)
    (b : moduleSections 𝒜 (twistGrading (S := A) 𝒜 q) U) :
    sectionsMap φ hφ (p + q) U (twistSectionsMul 𝒜 p q U a b) =
      twistSectionsMul ℬ p q (U.comap (ProjectiveSpectrum.comap φ hφ))
        (sectionsMap φ hφ p U a) (sectionsMap φ hφ q U b)
```

**`Stacks.AlgebraicGeometry.TwistMultCompat.projInclusionTwistIso_preserves_products`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TwistMultCompat/Basic.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TwistMultCompat/Basic.lean#L179). The attribute's comment: “multiplication compatibility of twist isomorphisms”.

> **Tag 01NO, multiplication compatibility of twist isomorphisms.** For an inclusion `U ⊆ V` of
> affine opens of the base of a quasi-coherent graded algebra and any two twist indices `n, m : ℤ`,
> the canonical isomorphisms on the twists of the induced morphism of projective spectra are
> compatible with the multiplication maps of Tag 01MU: the pulled-back multiplication followed by
> the comparison on the `(n + m)`-th twist is the tensor product of the comparisons on the `n`-th
> and the `m`-th twists followed by the multiplication map downstairs.
>
> The hypotheses are exactly those of the tagged statement: a quasi-coherent graded algebra on a scheme, two affine
> opens, an inclusion between them, and two unrestricted twist indices.

```lean
public theorem projInclusionTwistIso_preserves_products :
    pullbackTwistMultiplication (A.grading V) (projInclusionMap A U V h hU hV) n m ≫
        (projInclusionTwistIso A U V h hU hV (n + m)).hom =
      ((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u}
          ⟨(((AlgebraicGeometry.Proj (A.grading U)).toRingedSpace)).presheaf,
            (((AlgebraicGeometry.Proj (A.grading U)).toRingedSpace)).IsSheaf⟩)).map
          (X := ((Scheme.Modules.pullback (projInclusionMap A U V h hU hV)).obj
            (twistingSheaf (A.grading V) n),
            (Scheme.Modules.pullback (projInclusionMap A U V h hU hV)).obj
              (twistingSheaf (A.grading V) m)))
          (Y := (twistingSheaf (A.grading U) n, twistingSheaf (A.grading U) m))
          (((projInclusionTwistIso A U V h hU hV n).hom,
            (projInclusionTwistIso A U V h hU hV m).hom) : (_, _) ⟶ (_, _))) ≫
        twistMultiplicationMap (A.grading U) n m
```

## Tag 01NP, a lemma

[Tag 01NP](https://stacks.math.columbia.edu/tag/01NP) in the Stacks Project.

**`Stacks.RelativeProj.Situation.projInclusionMap_and_twistMap_trans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjSituation/Transitive.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjSituation/Transitive.lean#L157). The attribute's comment: “both assertions of the tag as one statement, in the shape of Situation 01NN: the composition law for the tag-01NO morphisms r, and the similar law for the comparison isomorphisms θ”.

> **Stacks Project, Tag 01NP, both of its assertions as one statement.** In Situation 01NN, let
> `U ⊆ U' ⊆ U''` be affine opens of the base and put `A = 𝒜(U)`, `A' = 𝒜(U')`, `A'' = 𝒜(U'')` for
> the graded rings of local sections. Then:
>
> * the composition of the tag-01NO morphisms `r : Proj A ⟶ Proj A'` and `r' : Proj A' ⟶ Proj A''`
>   is the tag-01NO morphism `r'' : Proj A ⟶ Proj A''` of the inclusion `U ⊆ U''`;
> * the similar statement holds for the tag-01NO comparison isomorphisms `θ`: for every degree `n`,
>   every open `V` of `Proj A''`, every section `a` of `𝒪_{Proj A''}(n)` over `V` and every point of
>   `Proj A` lying over `V`, the composite of `θ` and `θ'` and the comparison `θ''` of the outer
>   inclusion read the same degree-`n` fraction.
>
> The two conjuncts are `Stacks.RelativeProj.Situation.projInclusionMap_trans` and
> `Stacks.RelativeProj.Situation.twistMap_gradedSectionRestriction_trans`.

```lean
public theorem projInclusionMap_and_twistMap_trans (U U' U'' : s.base.Opens) (hUU' : U ≤ U')
    (hU'U'' : U' ≤ U'') (hU : IsAffineOpen U) (hU' : IsAffineOpen U')
    (hU'' : IsAffineOpen U'') :
    (projInclusionMap s U U' hUU' hU hU' ≫ projInclusionMap s U' U'' hU'U'' hU' hU'' =
        projInclusionMap s U U'' (hUU'.trans hU'U'') hU hU'') ∧
      ∀ (n : ℤ) (V : Opens (ProjectiveSpectrum.top (s.sectionRingGrading U'')))
          (a : moduleSections (s.sectionRingGrading U'')
            (twistGrading (S := s.sectionRing U'') (s.sectionRingGrading U'') n) V)
          (y : V.comap (ProjectiveSpectrum.comap
            (gradedSectionRestriction s U U'' (hUU'.trans hU'U''))
            (irrelevant_le_map_gradedSectionRestriction s U U'' (hUU'.trans hU'U'') hU hU''))),
        (sectionsMap (gradedSectionRestriction s U U'' (hUU'.trans hU'U''))
            (irrelevant_le_map_gradedSectionRestriction s U U'' (hUU'.trans hU'U'') hU hU'')
            n V a).1 y
          = (sectionsMap (gradedSectionRestriction s U U' hUU')
              (irrelevant_le_map_gradedSectionRestriction s U U' hUU' hU hU') n
              (V.comap (ProjectiveSpectrum.comap (gradedSectionRestriction s U' U'' hU'U'')
                (irrelevant_le_map_gradedSectionRestriction s U' U'' hU'U'' hU' hU'')))
              (sectionsMap (gradedSectionRestriction s U' U'' hU'U'')
                (irrelevant_le_map_gradedSectionRestriction s U' U'' hU'U'' hU' hU'') n V a)).1
              ⟨y.1, mem_comap_comap_of_eq_comp (gradedSectionRestriction s U' U'' hU'U'')
                (irrelevant_le_map_gradedSectionRestriction s U' U'' hU'U'' hU' hU'')
                (gradedSectionRestriction s U U' hUU')
                (irrelevant_le_map_gradedSectionRestriction s U U' hUU' hU hU')
                (irrelevant_le_map_gradedSectionRestriction s U U'' (hUU'.trans hU'U'') hU hU'')
                (gradedSectionRestriction_comp s U U' U'' hUU' hU'U'') y.2⟩
```

## Tag 01NQ, a lemma

[Tag 01NQ](https://stacks.math.columbia.edu/tag/01NQ) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeProj.relativeProj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProj/Assembled.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProj/Assembled.lean#L224). References: EGA II (3.1.2), “existence”; EGA II (8.3.1).

> **Tag 01NQ.** The relative homogeneous spectrum of a quasi-coherent graded algebra on a
> scheme, together with its structure morphism to the base and its canonical affine charts.
>
> The scheme is the colimit of the chart functor on the small affine Zariski site of the base; the
> chart over an affine open is the colimit inclusion, and it is cartesian over that affine open
> because the relative glueing datum's squares are. Compatibility of the charts with the
> transitions holds for the arrows of the site by the defining equation of the colimit, and for an
> arbitrary inclusion of affine opens by
> `Stacks.AlgebraicGeometry.RelativeProjGeneral.transition_comp_chart_of_le_opens`.

```lean
public def relativeProj : RelativeProjData A
```

**`Stacks.RelativeProj.Situation.relativeProj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProj/Charts/Descent.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProj/Charts/Descent.lean#L319). References: EGA II (3.1.2); EGA II (8.3.1), “more general”.

> **Stacks Project, Tag 01NQ.** The relative projective spectrum of a quasi-coherent
> nonnegatively graded algebra on a scheme: the scheme glued from the projective spectra of the
> graded rings of local sections over the affine opens of the base.

```lean
public noncomputable def relativeProj : Scheme.{u}
```

**`Stacks.RelativeProj.Situation.relativeProjToBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProj/Charts/Descent.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProj/Charts/Descent.lean#L323).

> The structure morphism of the relative projective spectrum to its base.

```lean
public noncomputable def relativeProjToBase : relativeProj s ⟶ s.base
```

**`Stacks.RelativeProj.Situation.relativeProjChart`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProj/Charts/Descent.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProj/Charts/Descent.lean#L328).

> The chart over an affine open of the base, as a morphism into the relative projective
> spectrum.

```lean
public noncomputable def relativeProjChart (W : s.base.affineOpens) :
    Proj (s.sectionRingGrading W.1) ⟶ relativeProj s
```

**`Stacks.RelativeProj.Situation.relativeProjChart_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProj/Charts/Descent.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProj/Charts/Descent.lean#L334).

> **The chart over `W` is the part of the relative projective spectrum lying over `W`.** This
> is the defining property of a relative projective spectrum.

```lean
public theorem relativeProjChart_isPullback (W : s.base.affineOpens) :
    IsPullback (relativeProjChart s W) (projInclusionToOpen s W.1 W.2)
      (relativeProjToBase s) W.1.ι
```

**`Stacks.RelativeProj.Situation.relativeProjChart_transition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProj/Charts/Descent.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProj/Charts/Descent.lean#L341).

> The charts are compatible with the comparison morphisms of charts.

```lean
public theorem relativeProjChart_transition {W W' : s.base.affineOpens} (h : W ≤ W') :
    projInclusionMap s W.1 W'.1 h W.2 W'.2 ≫ relativeProjChart s W' = relativeProjChart s W
```

## Tag 01NR, a lemma

[Tag 01NR](https://stacks.math.columbia.edu/tag/01NR) in the Stacks Project.

**`Stacks.AlgebraicGeometry.GluedTwistAlgebra.twistDataOfGradedAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GluedTwistAlgebra/Assemble.lean, line 507](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GluedTwistAlgebra/Assemble.lean#L507). The attribute's comment: “the existence assertion: the graded twists and the homogeneous-section map, for a quasi-coherent graded algebra on any scheme, with no hypothesis beyond the algebra itself. The two uniqueness assertions are carried by `Stacks.AlgebraicGeometry.TwistExistence.isUniqueTwistData` and `Stacks.AlgebraicGeometry.TwistRigidity.determinesChartIso`, which were vacuous until this term existed”.

> **The twists on the relative projective spectrum of a quasi-coherent graded algebra exist**,
> on no hypothesis beyond the graded algebra itself: the nested cocycle of Tag 01MZ that the glued
> twists are indexed by is discharged in every integer degree by
> `Stacks.AlgebraicGeometry.ProjTwistCocycle.isNestedCocycle`.

```lean
public def twistDataOfGradedAlgebra : TwistData A
```

**`Stacks.AlgebraicGeometry.TwistExistence.isUniqueTwistData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TwistExistence/Glue.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TwistExistence/Glue.lean#L230). The attribute's comment: “uniqueness of the complete structure”.

> **Tag 01NR's first uniqueness assertion.** Any two sets of twist data on a relative Proj are
> carried into each other by a *unique* isomorphism of graded algebras commuting with the
> homogeneous-section maps. The existence half is the glued comparison of this file; the
> uniqueness half is
> `Stacks.AlgebraicGeometry.TwistUnique.isUniqueTwistData_of_exists`.

```lean
public theorem isUniqueTwistData (A : SheafGradedAlgebra S) : IsUniqueTwistData A
```

**`Stacks.AlgebraicGeometry.TwistRigidity.determinesChartIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TwistRigidity/Determines.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TwistRigidity/Determines.lean#L135). The attribute's comment: “uniqueness of the affine-chart identifications”.

> An isomorphism of the glued graded algebras of two twist data which commutes with the
> homogeneous-section maps determines every chart identification, in every integer degree.

```lean
public theorem determinesChartIso (A : SheafGradedAlgebra S) : DeterminesChartIso A
```

Declarations registered for the tag:

- [`Stacks.AlgebraicGeometry.RelativeProjTwists.TwistData.chartIso_mul`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjTwists/Statement.lean#L213), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/RelativeProjTwistQcoh/Tags.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjTwistQcoh/Tags.lean#L50) (StacksFrontier): “multiplication on affine charts”.
- [`Stacks.AlgebraicGeometry.RelativeProjTwists.TwistData.chartIso_one`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjTwists/Statement.lean#L226), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/RelativeProjTwistQcoh/Tags.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjTwistQcoh/Tags.lean#L53) (StacksFrontier): “the unit on affine charts”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.15, Tag 01NM](https://stacks.math.columbia.edu/tag/01NM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
