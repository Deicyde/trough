---
declaration: section
origin: cited
lean: Stacks.Curves.isProper_complementaryCurve, Stacks.Curves.topologicalKrullDim_complementaryCurve, Stacks.Curves.isIso_globalSections_complementaryCurve, Stacks.Curves.existsUnique_contractionOfRationalTail, Stacks.Curves.isIso_structureSheaf_to_pushforward_canonicalContraction, Stacks.Curves.smoothAt_or_isNode_complementaryCurve_of_notMem_support, Stacks.Curves.nodal_complementaryCurve, Stacks.Curves.tail_inf_complementaryCurveIdeal_eq_bot
statement: formalized
proof: formalized
---

# 53.23 Contracting rational tails

Section 53.23 of the Stacks Project, [Tag 0E3G](https://stacks.math.columbia.edu/tag/0E3G). 6 tags here are carried by 25 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E3H, an example

[Tag 0E3H](https://stacks.math.columbia.edu/tag/0E3H) in the Stacks Project.

**`Stacks.Curves.isProper_complementaryCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/CanonicalContraction/ContractedCurve.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/CanonicalContraction/ContractedCurve.lean#L86). The attribute's comment: “complementary_curve_is_proper”.

> **Stacks 0E3H.** The scheme-theoretic closure of the complement of a closed subscheme of a
> proper scheme over a field is again proper over that field. For a rational tail this is the
> assertion that `X'` is proper over `k`; no rational-tail hypothesis is needed for it.

```lean
theorem isProper_complementaryCurve
    (k : Type u) [Field k] (X : Scheme.{u}) [X.Over (Spec (.of k))]
    [IsProper (X ↘ Spec (.of k))] (C : X.IdealSheafData) :
    IsProper (complementaryCurveι C ≫ (X ↘ Spec (.of k)))
```

**`Stacks.Curves.topologicalKrullDim_complementaryCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/CanonicalContraction/ContractedCurve.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/CanonicalContraction/ContractedCurve.lean#L104). The attribute's comment: “complementary_curve_has_dimension_one”.

> **Stacks 0E3H.** The scheme-theoretic closure `X'` of the complement of a rational tail of
> a proper one-dimensional curve over a field with only constant global functions is again of
> dimension one.

```lean
theorem topologicalKrullDim_complementaryCurve
    (k : Type u) [Field k] (X : Scheme.{u}) [X.Over (Spec (.of k))]
    [IsProper (X ↘ Spec (.of k))]
    (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (C : X.IdealSheafData) (hC : IsRationalTail k X C) :
    topologicalKrullDim (complementaryCurve C) = 1
```

**`Stacks.Curves.isIso_globalSections_complementaryCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/CanonicalContraction/ContractedCurve.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/CanonicalContraction/ContractedCurve.lean#L179). The attribute's comment: “complementary_curve_has_constant_global_functions”.

> **Stacks 0E3H.** The scheme-theoretic closure `X'` of the complement of a rational tail of
> a proper one-dimensional nodal curve over a field with only constant global functions again has
> only constant global functions: `H⁰(X', 𝒪_{X'}) = k`.

```lean
theorem isIso_globalSections_complementaryCurve
    (k : Type u) [Field k] (X : Scheme.{u}) [X.Over (Spec (.of k))]
    [IsProper (X ↘ Spec (.of k))]
    (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X)
    (C : X.IdealSheafData) (hC : IsRationalTail k X C) :
    IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫
      (complementaryCurveι C ≫ (X ↘ Spec (.of k))).appTop)
```

**`Stacks.Curves.existsUnique_contractionOfRationalTail`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/CanonicalContraction/Existence.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/CanonicalContraction/Existence.lean#L195). The attribute's comment: “canonical_contraction”.

> **Stacks 0E3H.** A rational tail of a proper one-dimensional nodal curve over a field with
> only constant global functions admits exactly one contraction onto the scheme-theoretic closure
> of its complement.

```lean
theorem existsUnique_contractionOfRationalTail
    (k : Type u) [Field k] (X : Scheme.{u}) [X.Over (Spec (.of k))]
    [IsProper (X ↘ Spec (.of k))]
    (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫
      (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X)
    (C : X.IdealSheafData)
    (hC : IsRationalTail k X C) :
    ∃! c : X ⟶ complementaryCurve C, IsContractionOfRationalTail hC c
```

**`Stacks.Curves.isIso_structureSheaf_to_pushforward_canonicalContraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/CanonicalContraction/Existence.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/CanonicalContraction/Existence.lean#L246). The attribute's comment: “pushforward_structure_sheaf”.

> **Stacks 0E3H.** The canonical contraction `c : X ⟶ X'` of a rational tail induces an
> isomorphism `𝒪_{X'} ⟶ c_*𝒪_X` of sheaves of rings.

```lean
theorem isIso_structureSheaf_to_pushforward_canonicalContraction
    (k : Type u) [Field k] (X : Scheme.{u}) [X.Over (Spec (.of k))]
    [IsProper (X ↘ Spec (.of k))]
    (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫
      (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X)
    (C : X.IdealSheafData)
    (hC : IsRationalTail k X C) :
    IsIso (canonicalContraction k X hdim hnodal C hC).toRingCatSheafHom
```

**`Stacks.Curves.smoothAt_or_isNode_complementaryCurve_of_notMem_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/CanonicalContraction/NodalAwayFromAttaching.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/CanonicalContraction/NodalAwayFromAttaching.lean#L119). The attribute's comment: “at_worst_nodal_away_from_the_attaching_point”.

> **Stacks 0E3H, the at-worst-nodal singularities of `X'` away from the attaching point.** Let
> `X` be a proper one-dimensional scheme over a field `k` with at-worst-nodal singularities and
> only constant global functions, let `C ⊆ X` be a rational tail and let `X'` be the
> scheme-theoretic closure of the complement of `C`. Every closed point of `X'` whose image in `X`
> lies outside `C` is smooth over `k` or is a node of `X'`.

```lean
theorem smoothAt_or_isNode_complementaryCurve_of_notMem_support
    (k : Type u) [Field k] (X : Scheme.{u}) [X.Over (Spec (.of k))]
    [IsProper (X ↘ Spec (.of k))]
    (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X)
    (C : X.IdealSheafData) (hC : IsRationalTail k X C)
    (y : complementaryCurve C) (hyc : IsClosed ({y} : Set (complementaryCurve C)))
    (hy : (complementaryCurveι C).base y ∈ (C.support.compl : X.Opens)) :
    letI : (complementaryCurve C).Over (Spec (.of k)) :=
      ⟨complementaryCurveι C ≫ (X ↘ Spec (.of k))⟩
    InfinitesimalLifting.SmoothAt (complementaryCurveι C ≫ (X ↘ Spec (.of k))) y ∨
      IsNode k (complementaryCurve C) y
```

**`Stacks.Curves.nodal_complementaryCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/CanonicalContraction/SmoothAtAttaching.lean, line 499](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/CanonicalContraction/SmoothAtAttaching.lean#L499). The attribute's comment: “complementary_curve_has_at_worst_nodal_singularities”.

> **Stacks 0E3H: the scheme-theoretic closure of the complement of a rational tail of a proper
> one-dimensional nodal curve with only constant global functions again has at-worst-nodal
> singularities.** Away from the attaching point this is the étale transport of
> `Stacks.Curves.smoothAt_or_isNode_complementaryCurve_of_notMem_support`; at the attaching point
> the closure is in fact *smooth* over `k`, by
> `Stacks.Curves.smoothAt_complementaryCurve_attachingPoint`.

```lean
theorem nodal_complementaryCurve
    (k : Type u) [Field k] (X : Scheme.{u}) [X.Over (Spec (.of k))]
    [IsProper (X ↘ Spec (.of k))]
    (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X)
    (C : X.IdealSheafData) (hC : IsRationalTail k X C) :
    letI : (complementaryCurve C).Over (Spec (.of k)) :=
      ⟨complementaryCurveι C ≫ (X ↘ Spec (.of k))⟩
    HasAtWorstNodalSingularities k (complementaryCurve C)
```

**`Stacks.Curves.tail_inf_complementaryCurveIdeal_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ComplementaryCurve/SchemeTheoreticUnion.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ComplementaryCurve/SchemeTheoreticUnion.lean#L158). The attribute's comment: “scheme_theoretic_union”.

> A rational tail `C` on a proper one-dimensional scheme over a field with at-worst-nodal
> singularities and with only constant global functions, together with the scheme-theoretic closure
> of its complement, has scheme-theoretic union the entire curve. Reducedness of the curve comes
> from the nodality hypothesis.

```lean
theorem tail_inf_complementaryCurveIdeal_eq_bot (k : Type u) [Field k] (X : Scheme.{u})
    [X.Over (Spec (.of k))] [IsProper (X ↘ Spec (.of k))]
    (_hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X) (C : X.IdealSheafData)
    (_hC : IsRationalTail k X C) :
    C ⊓ complementaryCurveIdeal C = ⊥
```

**`Stacks.Curves.isNode_attachingPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/AttachingPointNode.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/AttachingPointNode.lean#L46). The attribute's comment: “attaching_point_is_node”.

> **Stacks 0E3H.** The attaching point of a rational tail — where it meets the closure of
> its complement — is a node of the ambient curve.

```lean
theorem isNode_attachingPoint
    (k : Type u) [Field k] (X : Scheme.{u}) [X.Over (Spec (.of k))]
    [IsProper (X ↘ Spec (.of k))]
    (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X)
    (C : X.IdealSheafData) (hC : IsRationalTail k X C) :
    IsNode k X (C.subschemeι hC.attachingPoint)
```

**`Stacks.Curves.isFiniteSeparable_residueField_attachingPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/AttachingPointNode.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/AttachingPointNode.lean#L94). The attribute's comment: “finite_separable_residue_field”.

> **Stacks 0E3H.** At the attaching point of a rational tail, the extension of the residue
> field by the residue field of the node (in the sense of `Stacks.Curves.IsNode`) is finite and
> separable.

```lean
theorem isFiniteSeparable_residueField_attachingPoint
    (k : Type u) [Field k] (X : Scheme.{u}) [X.Over (Spec (.of k))]
    [IsProper (X ↘ Spec (.of k))]
    (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X)
    (C : X.IdealSheafData) (hC : IsRationalTail k X C) :
    let x := C.subschemeι hC.attachingPoint
    let kToStalk : k →+* X.presheaf.stalk x :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop ≫
        X.presheaf.germ ⊤ x (by simp)).hom
    letI : Algebra k (X.presheaf.stalk x) := kToStalk.toAlgebra
    letI : Algebra k (X.residueField x) := ((X.residue x).hom.comp kToStalk).toAlgebra
    Module.Finite k (X.residueField x) ∧ Algebra.IsSeparableExtension k (X.residueField x)
```

**`AlgebraicGeometry.IsContractionOfRationalTail`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/Contraction.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/Contraction.lean#L63). The attribute's comment: “contraction_of_a_rational_tail”.

> A morphism contracting a rational tail onto its complementary curve.

```lean
def IsContractionOfRationalTail {k : Type u} [Field k] {X : Scheme.{u}}
    [X.Over (Spec (.of k))] {C : X.IdealSheafData} (hC : IsRationalTail k X C)
    (c : X ⟶ complementaryCurve C) : Prop
```

**`AlgebraicGeometry.IsRationalTail`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/RationalTail.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/RationalTail.lean#L72). The attribute's comment: “rational_tail”.

> An integral irreducible component `C` of a scheme over `k` is a rational tail when the
> closure of its complement is nonempty, its intersection with `C` is one reduced point, the
> global functions on `C` map isomorphically to the residue field of that point, and `C` has
> genus zero.

```lean
def IsRationalTail (k : Type u) [Field k] (X : Scheme.{u}) [X.Over (Spec (.of k))]
    (C : X.IdealSheafData) : Prop
```

**`Stacks.Curves.genus_complementaryCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/DirectImage/RationalTailCohomologyIso.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/DirectImage/RationalTailCohomologyIso.lean#L254). The attribute's comment: “complementary_curve”.

> **Contracting a rational tail does not change the genus**: for `X` proper over `k` of
> dimension one with at worst nodal singularities and only constant global functions, and `C ⊆ X`
> a rational tail, the scheme-theoretic closure `X'` of the complement of `C` has the genus of `X`.
>
> This is the genus clause of [Stacks, Tag 0E3H], with no hypothesis beyond that tag's own. It is
> `Stacks.Curves.contractionCohomologyObjIso` at the canonical contraction, restricted further
> along the structure map of `X'` — which identifies the two `k`-module structures by
> `Stacks.Curves.structureMap_appTop_comp_appTop` — and then read as an equality of dimensions.
>
> The attribute registers Tag 0E3H with the sub-label `"complementary_curve"`, and not the bare
> tag: [Stacks, Tag 0E3H] makes several separate assertions about `X'` and this declaration
> proves only the one about the genus, so no single declaration states the whole example.

```lean
theorem genus_complementaryCurve
    (k : Type u) [Field k] (X : Scheme.{u}) [X.Over (Spec (.of k))]
    [IsProper (X ↘ Spec (.of k))]
    (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X)
    (C : X.IdealSheafData) (hC : IsRationalTail k X C) :
    genus (complementaryCurveι C ≫ (X ↘ Spec (.of k))) = genus (X ↘ Spec (.of k))
```

**`Stacks.Curves.isZero_rightDerived_one_pushforward_ambientStructureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/DirectImage/RationalTailHigherDirectImage.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/DirectImage/RationalTailHigherDirectImage.lean#L284). The attribute's comment: “higher_direct_image_vanishing”.

> **`R ¹ c_* 𝒪_X = 0` for a contraction `c` of a rational tail on a nodal curve.**
>
> This is the direct-image vanishing clause of [Stacks, Tag 0E3H], at that tag's standing
> hypotheses: `X` is proper and one-dimensional over `k` with only constant global functions and
> at worst nodal singularities. Those hypotheses enter only through
> `Stacks.Curves.tail_inf_complementaryCurveIdeal_eq_bot`, which says that the tail and the
> closure of its complement cover `X` scheme-theoretically, so that the union term of
> `Stacks.Curves.isZero_rightDerived_one_pushforward_schemeTheoreticUnion` is the structure sheaf
> of `X` itself.
>
> The genus equality that [Stacks, Tag 0E3H] ultimately asserts is downstream of this and is not
> claimed here; the scoped sub-label registers the direct-image clause alone.

```lean
public theorem isZero_rightDerived_one_pushforward_ambientStructureSheaf
    (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X)
    {hC : IsRationalTail k X C} {c : X ⟶ complementaryCurve C}
    (hc : IsContractionOfRationalTail hC c) :
    Limits.IsZero (((Scheme.Modules.pushforward c).rightDerived 1).obj
      (Scheme.IdealSheafData.ambientStructureSheaf X))
```

## Tag 0E63, a lemma

[Tag 0E63](https://stacks.math.columbia.edu/tag/0E63) in the Stacks Project.

**`AlgebraicGeometry.invertibleCurveDegree_pullback_dualizingSheafOverField_neg_of_isRationalTail`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/DualizingSheafDegree.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/DualizingSheafDegree.lean#L317).

> **Stacks Project, Tag 0E63.** Let `X` be a proper scheme of dimension one over a field `k`
> with `H⁰(X, 𝒪_X) = k` and at-worst-nodal singularities, and let `C ⊆ X` be a rational tail. Then
> `deg(ω_X|_C) < 0`.
>
> Here `ω_X` is invertible
> (`AlgebraicGeometry.isInvertible_dualizingSheafOverField_of_hasAtWorstNodalSingularities`). The
> sequence `0 ⟶ ω_C ⟶ ω_X|_C ⟶ 𝒪_{C ∩ X'} ⟶ 0` of [Stacks, Tag 0E34] gives
> `deg(ω_X|_C) = -[k' : k]` with `k' = Γ(C, 𝒪_C)`
> (`AlgebraicGeometry.invertibleCurveDegree_eq_neg_of_isRationalTail`).

```lean
theorem invertibleCurveDegree_pullback_dualizingSheafOverField_neg_of_isRationalTail
    [IsProper (X ↘ Spec (.of k))] (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : Stacks.Curves.HasAtWorstNodalSingularities k X)
    (C : X.IdealSheafData) (hC : IsRationalTail k X C) :
    haveI := connectedSpace_of_isIso_globalSections k (X ↘ Spec (.of k))
    letI hω := isInvertible_dualizingSheafOverField_of_hasAtWorstNodalSingularities k X hdim
      hnodal
    letI := Stacks.AlgebraicGeometry.Tag09NY.isInvertible_modulePullback C.subschemeι
      (Stacks.Duality.dualizingSheafOverField (X ↘ Spec (.of k))) hω
    invertibleCurveDegree k (C.subschemeι ≫ (X ↘ Spec (.of k)))
        (Stacks.Curves.topologicalKrullDim_subscheme_eq_one_of_isRationalTail k X hdim C hC).le
        ((Scheme.Modules.pullback C.subschemeι).obj
          (Stacks.Duality.dualizingSheafOverField (X ↘ Spec (.of k)))) < 0
```

## Tag 0E3I, a lemma

[Tag 0E3I](https://stacks.math.columbia.edu/tag/0E3I) in the Stacks Project.

**`AlgebraicGeometry.exists_iso_sigma_isRationalTail_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/BaseChange.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/BaseChange.lean#L184).

> **[Stacks, Tag 0E3I].** Let `X` be a proper scheme over a field `k` of dimension one with
> `H⁰(X, 𝒪_X) = k` and at-worst-nodal singularities, and let `C ⊆ X` be a rational tail. For every
> field extension `K/k` the base change `C_K ⊆ X_K` is a finite disjoint union of rational tails
> of `X_K`: there are finitely many rational tails `Dᵢ` of `X_K` and an isomorphism
> `∐ᵢ Dᵢ ≅ C_K` compatible with the closed immersions into `X_K`.

```lean
theorem exists_iso_sigma_isRationalTail_baseChange
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    (X : Scheme.{u}) [X.Over (Spec (.of k))]
    [IsProper (X ↘ Spec (.of k))]
    (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X)
    (C : X.IdealSheafData) (hC : IsRationalTail k X C) :
    let g : Spec (.of K) ⟶ Spec (.of k) :=
      Spec.map (CommRingCat.ofHom (algebraMap k K))
    let Y := (pullback (X ↘ Spec (.of k)) g : Scheme.{u})
    let p : Y ⟶ X := pullback.fst (X ↘ Spec (.of k)) g
    letI : Y.Over (Spec (.of K)) := ⟨pullback.snd (X ↘ Spec (.of k)) g⟩
    ∃ (ι : Type u) (_ : Finite ι) (D : ι → Y.IdealSheafData)
        (_ : ∀ i, IsRationalTail K Y (D i))
        (e : (∐ fun i ↦ (D i).subscheme) ≅ (C.comap p).subscheme),
      e.hom ≫ (C.comap p).subschemeι =
        Sigma.desc (fun i ↦ (D i).subschemeι)
```

## Tag 0E3J, a lemma

[Tag 0E3J](https://stacks.math.columbia.edu/tag/0E3J) in the Stacks Project.

**`AlgebraicGeometry.finrank_cohomologyOverField_one_le_invertibleCurveDegree_of_forall_not_isRationalTail`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/DualizingSheafDegree.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/DualizingSheafDegree.lean#L261).

> **Stacks Project, Tag 0E3J.** Let `X` be a proper scheme of dimension one over a field `k`
> with `H⁰(X, 𝒪_X) = k` and at-worst-nodal singularities. If `X` has no rational tail, then for
> every reduced connected closed subscheme `Y ⊆ X`, `Y ≠ X`, of dimension one,
> `deg(ω_X|_Y) ≥ dim_k H¹(Y, 𝒪_Y)`.
>
> Here `ω_X` is invertible
> (`AlgebraicGeometry.isInvertible_dualizingSheafOverField_of_hasAtWorstNodalSingularities`). If
> the inequality failed, then `deg(ω_X|_Y) < 0`; for `Y` irreducible this makes `Y` a rational
> tail, and otherwise some one-dimensional component `C` of `Y` has `deg(ω_X|_C) < 0`
> ([Stacks, Tag 0AYW]) and is a rational tail by the same analysis.

```lean
theorem finrank_cohomologyOverField_one_le_invertibleCurveDegree_of_forall_not_isRationalTail
    [IsProper (X ↘ Spec (.of k))] (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : Stacks.Curves.HasAtWorstNodalSingularities k X)
    (htail : ∀ C : X.IdealSheafData, ¬ IsRationalTail k X C)
    (Y : X.IdealSheafData) [IsReduced Y.subscheme] [ConnectedSpace Y.subscheme]
    (hY : topologicalKrullDim Y.subscheme = 1) (hYX : Y ≠ ⊥) :
    haveI := connectedSpace_of_isIso_globalSections k (X ↘ Spec (.of k))
    letI hω := isInvertible_dualizingSheafOverField_of_hasAtWorstNodalSingularities k X hdim
      hnodal
    letI := Stacks.AlgebraicGeometry.Tag09NY.isInvertible_modulePullback Y.subschemeι
      (Stacks.Duality.dualizingSheafOverField (X ↘ Spec (.of k))) hω
    (Module.finrank k (cohomologyOverField k (Y.subschemeι ≫ (X ↘ Spec (.of k)))
        (SheafOfModules.unit Y.subscheme.ringCatSheaf) 1) : ℤ) ≤
      invertibleCurveDegree k (Y.subschemeι ≫ (X ↘ Spec (.of k))) hY.le
        ((Scheme.Modules.pullback Y.subschemeι).obj
          (Stacks.Duality.dualizingSheafOverField (X ↘ Spec (.of k))))
```

## Tag 0E3K, a lemma

[Tag 0E3K](https://stacks.math.columbia.edu/tag/0E3K) in the Stacks Project.

**`AlgebraicGeometry.exists_planeCurveData_deg_two_of_forall_not_isRationalTail`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusZeroPositiveDegree/CanonicalNodal.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusZeroPositiveDegree/CanonicalNodal.lean#L94). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 0E3K, part (1).** Let `X` be a proper scheme of dimension one over a
> field `k` with `H⁰(X, 𝒪_X) = k`, with at-worst-nodal singularities and no rational tail. If `X`
> has genus `0`, then `X` is isomorphic to an irreducible plane conic and `ω_X^{⊗ -1}` is very
> ample.
>
> `ω_X` is invertible of degree `2g - 2 = -2` ([Stacks, Tag 0E37], [Stacks, Tag 0C19]) and
> satisfies the subcurve bound of [Stacks, Tag 0E3J], so
> `AlgebraicGeometry.exists_planeCurveData_deg_two_of_subcurve_bound` applies.

```lean
theorem exists_planeCurveData_deg_two_of_forall_not_isRationalTail
    [IsProper (X ↘ Spec (.of k))] (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X)
    (htail : ∀ C : X.IdealSheafData, ¬ IsRationalTail k X C)
    (hgenus : genus (X ↘ Spec (.of k)) = 0) :
    (∃ C : ProjectiveSpectrum.Proj.PlaneCurveData k, C.deg = 2 ∧ IrreducibleSpace C.Z ∧
      ∃ e : X ≅ C.Z, e.hom ≫ C.toSpec = X ↘ Spec (.of k)) ∧
    haveI := connectedSpace_of_isIso_globalSections k (X ↘ Spec (.of k))
    letI := isInvertible_dualizingSheafOverField_of_hasAtWorstNodalSingularities k X hdim hnodal
    letI := tensorPower_isInvertible X.presheaf X.ringCatSheaf.2
      (Stacks.Duality.dualizingSheafOverField (X ↘ Spec (.of k))) (-1)
    Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple (X ↘ Spec (.of k))
      (tensorPower X.presheaf X.ringCatSheaf.2
        (Stacks.Duality.dualizingSheafOverField (X ↘ Spec (.of k))) (-1))
```

**`AlgebraicGeometry.nonempty_dualizingSheafOverField_iso_unit_of_forall_not_isRationalTail`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusZeroPositiveDegree/CanonicalNodal.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusZeroPositiveDegree/CanonicalNodal.lean#L130). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 0E3K, part (2).** Let `X` be a proper scheme of dimension one over a
> field `k` with `H⁰(X, 𝒪_X) = k`, with at-worst-nodal singularities and no rational tail. If `X`
> has genus `1`, then `ω_X ≅ 𝒪_X`.
>
> `ω_X` is invertible of degree `2g - 2 = 0` with `h⁰(ω_X) = g = 1`, and satisfies the subcurve
> bound of [Stacks, Tag 0E3J]; so every component degree is nonnegative, they sum to `0`
> ([Stacks, Tag 0AYW]), and [Stacks, Tag 0E22] applies
> (`AlgebraicGeometry.isTrivial_of_subcurve_bound`).

```lean
theorem nonempty_dualizingSheafOverField_iso_unit_of_forall_not_isRationalTail
    [IsProper (X ↘ Spec (.of k))] (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X)
    (htail : ∀ C : X.IdealSheafData, ¬ IsRationalTail k X C)
    (hgenus : genus (X ↘ Spec (.of k)) = 1) :
    Nonempty (Stacks.Duality.dualizingSheafOverField (X ↘ Spec (.of k)) ≅
      SheafOfModules.unit X.ringCatSheaf)
```

**`AlgebraicGeometry.isGeneratedByGlobalSections_tensorPower_dualizingSheafOverField_of_forall_not_isRationalTail`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusZeroPositiveDegree/CanonicalNodal.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusZeroPositiveDegree/CanonicalNodal.lean#L164). The attribute's comment: “part (3)”.

> **Stacks Project, Tag 0E3K, part (3).** Let `X` be a proper scheme of dimension one over a
> field `k` with `H⁰(X, 𝒪_X) = k`, with at-worst-nodal singularities and no rational tail. If the
> genus of `X` is at least `2`, then `ω_X^{⊗ m}` is globally generated for every `m ≥ 2`.
>
> `ω_X` is invertible of degree `2g - 2` and satisfies the subcurve bound of [Stacks, Tag 0E3J],
> which with `g ≥ 2` and `m ≥ 2` gives the inequalities of [Stacks, Tag 0E3F]
> (`AlgebraicGeometry.isGeneratedByGlobalSections_tensorPower_of_subcurve_bound`).

```lean
theorem isGeneratedByGlobalSections_tensorPower_dualizingSheafOverField_of_forall_not_isRationalTail
    [IsProper (X ↘ Spec (.of k))] (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ (X ↘ Spec (.of k)).appTop)]
    (hnodal : HasAtWorstNodalSingularities k X)
    (htail : ∀ C : X.IdealSheafData, ¬ IsRationalTail k X C)
    (hgenus : 2 ≤ genus (X ↘ Spec (.of k))) (m : ℕ) (hm : 2 ≤ m) :
    haveI := connectedSpace_of_isIso_globalSections k (X ↘ Spec (.of k))
    letI := isInvertible_dualizingSheafOverField_of_hasAtWorstNodalSingularities k X hdim hnodal
    SheafOfModules.IsGeneratedByGlobalSections
      (tensorPower X.presheaf X.ringCatSheaf.2
        (Stacks.Duality.dualizingSheafOverField (X ↘ Spec (.of k))) m)
```

## Tag 0E3L, a lemma

[Tag 0E3L](https://stacks.math.columbia.edu/tag/0E3L) in the Stacks Project.

**`AlgebraicGeometry.IsIteratedContractionOfRationalTails.exists_planeCurveData_deg_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/Terminal.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/Terminal.lean#L60). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 0E3L, part (1).** Let `X` be a proper scheme of dimension one over a
> field `k` with `H⁰(X, 𝒪_X) = k` and at-worst-nodal singularities, and `X → X'` a chain of
> contractions of rational tails after which none are left. If `X` has genus `0`, then `X'` is an
> irreducible plane conic over `k`.

```lean
theorem exists_planeCurveData_deg_two (hgenus : genus fX = 0) :
    ∃ C : ProjectiveSpectrum.Proj.PlaneCurveData k, C.deg = 2 ∧ IrreducibleSpace C.Z ∧
      ∃ e : Y ≅ C.Z, e.hom ≫ C.toSpec = fY
```

**`AlgebraicGeometry.IsIteratedContractionOfRationalTails.nonempty_dualizingSheafOverField_iso_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/Terminal.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/Terminal.lean#L76). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 0E3L, part (2).** Let `X` be a proper scheme of dimension one over a
> field `k` with `H⁰(X, 𝒪_X) = k` and at-worst-nodal singularities, and `X → X'` a chain of
> contractions of rational tails after which none are left. If `X` has genus `1`, then
> `ω_{X'} ≅ 𝒪_{X'}`.

```lean
theorem nonempty_dualizingSheafOverField_iso_unit (hgenus : genus fX = 1) :
    haveI : IsProper fY := isProper_target hseq hdim hnodal
    Nonempty (Stacks.Duality.dualizingSheafOverField fY ≅ SheafOfModules.unit Y.ringCatSheaf)
```

**`AlgebraicGeometry.IsIteratedContractionOfRationalTails.isGeneratedByGlobalSections_tensorPower_dualizingSheafOverField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/Terminal.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/Terminal.lean#L92). The attribute's comment: “part (3)”.

> **Stacks Project, Tag 0E3L, part (3).** Let `X` be a proper scheme of dimension one over a
> field `k` with `H⁰(X, 𝒪_X) = k` and at-worst-nodal singularities, and `X → X'` a chain of
> contractions of rational tails after which none are left. If the genus of `X` is at least `2`,
> then `ω_{X'}` is invertible and `ω_{X'}^{⊗ m}` is globally generated for every `m ≥ 2`.

```lean
theorem isGeneratedByGlobalSections_tensorPower_dualizingSheafOverField
    (hgenus : 2 ≤ genus fX) (m : ℕ) (hm : 2 ≤ m) :
    letI : Y.Over (Spec (.of k)) := ⟨fY⟩
    haveI : IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ fY.appTop) :=
      isIso_globalSections_target hseq hdim hnodal
    haveI := connectedSpace_of_isIso_globalSections k fY
    haveI : IsProper fY := isProper_target hseq hdim hnodal
    letI : SheafOfModules.IsInvertible Y.presheaf Y.ringCatSheaf.2
        (Stacks.Duality.dualizingSheafOverField fY) :=
      @isInvertible_dualizingSheafOverField_of_hasAtWorstNodalSingularities k _ Y _ this _
        (topologicalKrullDim_target hseq hdim hnodal)
        (hasAtWorstNodalSingularities_target hseq hdim hnodal)
    SheafOfModules.IsGeneratedByGlobalSections
      (tensorPower Y.presheaf Y.ringCatSheaf.2 (Stacks.Duality.dualizingSheafOverField fY) m)
```

**`AlgebraicGeometry.IsIteratedContractionOfRationalTails.existsUnique_iso_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/TerminalBaseChange.lean, line 678](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/TerminalBaseChange.lean#L678). The attribute's comment: “compatibility with base field extensions”.

> **Stacks Project, Tag 0E3L, compatibility with extension of the ground field.** Let `X` be a
> proper scheme of dimension one over a field `k` with `H⁰(X, 𝒪_X) = k`, at-worst-nodal singularities
> and genus at least one, `c : X ⟶ Y` a chain of contractions of rational tails after which none
> are left, and `K/k` a field extension. For every chain `d : X_K ⟶ Z` of contractions of rational
> tails of `X_K` after which none are left, there is a unique isomorphism `e : Y_K ≅ Z` with
> `c_K ≫ e = d`: the formation of the contraction of all rational tails commutes with the base
> change to `K`.
>
> `d` factors through `c_K`
> (`AlgebraicGeometry.IsIteratedContractionOfRationalTails.exists_comp_eq_baseChange`, using
> [Stacks, Tag 0E3I]). Conversely `Y_K` is a nodal curve of positive genus without rational tails
> (`AlgebraicGeometry.forall_not_isRationalTail_baseChange`) and `𝒪_{Y_K} = (c_K)_*𝒪_{X_K}` by flat
> base change, so `c_K` factors through `d`
> (`IsIteratedContractionOfRationalTails.exists_comp_eq_of_forall_not_isRationalTail`).
> The two factorizations are mutually inverse, `c_K` and `d` being dominant onto reduced curves.

```lean
theorem IsIteratedContractionOfRationalTails.existsUnique_iso_baseChange (k K : Type u) [Field k]
    [Field K] [Algebra k K] {X Y : Scheme.{u}} {fX : X ⟶ Spec (.of k)} {fY : Y ⟶ Spec (.of k)}
    {c : X ⟶ Y} [IsProper fX] (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ fX.appTop)]
    (hnodal : letI : X.Over (Spec (.of k)) := ⟨fX⟩
      Stacks.Curves.HasAtWorstNodalSingularities k X)
    (hgenus : 1 ≤ genus fX)
    (hseq : IsIteratedContractionOfRationalTails k fX fY c)
    (hterminal : ∀ C : Y.IdealSheafData, ¬ @IsRationalTail k _ Y ⟨fY⟩ C)
    {Z : Scheme.{u}} {fZ : Z ⟶ Spec (.of K)} {d : pullback fX (Spec.map (CommRingCat.ofHom
        (algebraMap k K))) ⟶ Z}
    (hd : IsIteratedContractionOfRationalTails K (pullback.snd fX (Spec.map (CommRingCat.ofHom
        (algebraMap k K)))) fZ d)
    (hdterminal : ∀ C : Z.IdealSheafData, ¬ @IsRationalTail K _ Z ⟨fZ⟩ C) :
    ∃! e : pullback fY (Spec.map (CommRingCat.ofHom (algebraMap k K))) ≅ Z,
      pullback.map fX (Spec.map (CommRingCat.ofHom (algebraMap k K))) fY (Spec.map
          (CommRingCat.ofHom (algebraMap k K))) c (𝟙 _) (𝟙 _)
        (by rw [Category.comp_id, hseq.comp_structureMap]) (by simp) ≫ e.hom = d
```

**`AlgebraicGeometry.IsIteratedContractionOfRationalTails.existsUnique_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/Uniqueness.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ContractingRationalTails/Uniqueness.lean#L402). The attribute's comment: “independence of choices”.

> Let `X` be a proper scheme of dimension one over a field `k` with `H⁰(X, 𝒪_X) = k`,
> at-worst-nodal singularities and genus at least one. For two chains `c₁ : X ⟶ Y₁` and
> `c₂ : X ⟶ Y₂` of contractions of rational tails after which none are left, there is a unique
> isomorphism `e : Y₁ ≅ Y₂` with `c₁ ≫ e = c₂`.

```lean
theorem existsUnique_iso {X Y₁ Y₂ : Scheme.{u}} {fX : X ⟶ Spec (.of k)}
    {fY₁ : Y₁ ⟶ Spec (.of k)} {fY₂ : Y₂ ⟶ Spec (.of k)} {c₁ : X ⟶ Y₁} {c₂ : X ⟶ Y₂}
    [IsProper fX] (hdim : topologicalKrullDim X = 1)
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ fX.appTop)]
    (hnodal : letI : X.Over (Spec (.of k)) := ⟨fX⟩
      Stacks.Curves.HasAtWorstNodalSingularities k X)
    (hgenus : 1 ≤ genus fX)
    (hseq₁ : IsIteratedContractionOfRationalTails k fX fY₁ c₁)
    (hterminal₁ : ∀ C : Y₁.IdealSheafData, ¬ @IsRationalTail k _ Y₁ ⟨fY₁⟩ C)
    (hseq₂ : IsIteratedContractionOfRationalTails k fX fY₂ c₂)
    (hterminal₂ : ∀ C : Y₂.IdealSheafData, ¬ @IsRationalTail k _ Y₂ ⟨fY₂⟩ C) :
    ∃! e : Y₁ ≅ Y₂, c₁ ≫ e.hom = c₂
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.23, Tag 0E3G](https://stacks.math.columbia.edu/tag/0E3G)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
