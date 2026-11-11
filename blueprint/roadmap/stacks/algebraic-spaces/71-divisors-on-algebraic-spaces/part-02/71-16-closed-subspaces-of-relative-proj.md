---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.closedSubspaceSectionMap, AlgebraicGeometry.Space.closedSubspaceGradedIdeal, AlgebraicGeometry.Space.isQuasicoherentOnSite_closedSubspaceGradedIdealObj, AlgebraicGeometry.Space.C1359Bridge.exists_iso_quotientProjHom_psiKernelGradedIdeal, AlgebraicGeometry.Space.exists_finiteType_chartDegreeSubmodule, AlgebraicGeometry.Space.closedSubspaceDegreeProducts_le_ker, AlgebraicGeometry.Space.RelativeProjSituation.exists_finiteType_iso_quotientProjHom, AlgebraicGeometry.Space.RelativeProjSituation.exists_finiteType_degreeSubmodule_range_eq_quotientProj
statement: formalized
proof: formalized
---

# 71.16 Closed subspaces of relative proj

Section 71.16 of the Stacks Project, [Tag 085K](https://stacks.math.columbia.edu/tag/085K). 4 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 085L, a lemma

[Tag 085L](https://stacks.math.columbia.edu/tag/085L) in the Stacks Project.

**`AlgebraicGeometry.Space.closedSubspaceSectionMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjClosedSubspaceIdeal.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjClosedSubspaceIdeal.lean#L249). The attribute's comment: “the canonical map 𝒜 ⟶ ⨁ π\_*((i\_*𝒪\_Z)(d)), degreewise, built from the carried twists 𝒪\_P(d) and homogeneous section maps of Tag 01NR”.

> **The canonical map `𝒜_d ⟶ π_*((i_*𝒪_Z)(d))` of Stacks 085L**, in degree `d`: the
> homogeneous section map `𝒜_d ⟶ π_*(𝒪_P(d))` of Stacks 01MP followed by the direct image of the
> twist `𝒪_P(d) ⟶ (i_*𝒪_Z)(d)` of the structure map of the closed subspace.
>
> The source states the map into the direct sum over `d ≥ 0`; it is graded, and this is its
> degree-`d` component.  Only the twists are carried: the composite itself is the one the source
> names.

```lean
def closedSubspaceSectionMap (T : ClosedSubspaceTwistSections s P π) (i : Z ⟶ P) (d : ℕ) :
    s.algebra.piece (d : ℤ) ⟶ twistedStructureDirectImage T i d
```

**`AlgebraicGeometry.Space.closedSubspaceGradedIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjClosedSubspaceIdeal.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjClosedSubspaceIdeal.lean#L260). The attribute's comment: “the graded ideal ℐ ⊆ 𝒜, degreewise, as the kernel of that canonical map”.

> **The graded ideal `ℐ ⊆ 𝒜` of Stacks 085L**, in degree `d`: the sectionwise kernel of the
> canonical map, as a submodule of the degree-`d` piece of `𝒜`.
>
> This is the kernel of the map the source writes down, not a choice of ideal with the right
> properties; the only carried ingredient is the twists.

```lean
def closedSubspaceGradedIdeal (T : ClosedSubspaceTwistSections s P π) (i : Z ⟶ P) (d : ℕ) :
    (s.algebra.piece (d : ℤ)).Submodule
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_closedSubspaceGradedIdealObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjClosedSubspaceIdeal.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjClosedSubspaceIdeal.lean#L308). The attribute's comment: “ℐ is a quasi-coherent 𝒪\_X-module, degreewise; granted only Tag 03M9 for π as quasi-coherence of the direct images π\_*((i\_*𝒪\_Z)(d)), the kernel clause of Tag 03M1(3) being discharged from the closure lemma, and built from the carried twists of Tag 01NR”.

> **Stacks 085L, the quasi-coherence of `ℐ`.**  The degree-`d` piece of the graded ideal cut
> out by a closed subspace of the relative Proj is a quasi-coherent `𝒪_X`-module.
>
> There is exactly one carried input, and it is one the source cites.  `hpush` is Stacks 03M9 for
> `π`, in the form in which the source uses it: the direct image along `π` of the quasi-coherent
> module `(i_*𝒪_Z)(d)` is quasi-coherent — this is where quasi-compactness of `π` and its
> separatedness (Stacks 084E) enter.  It is carried because the library's Stacks 03M9,
> `AlgebraicGeometry.Space.pushforward_isQuasicoherentOnSite_of_chartwiseKernel`, is itself
> conditional on the exact sequence of Stacks 03M8.
>
> The kernel clause of Stacks 03M1(3) is **not** carried: it is discharged from
> `AlgebraicGeometry.Space.isClosedUnderKernels_quasicoherentSheaves_smallEtale`, whose own
> Stacks 03DX(2) input is already proved for the small étale site.  The `letI` ascribes it at this
> module's spelling of the structure ring sheaf, which instance resolution does not identify with
> the `RingedSite.ringSheaf` spelling of that lemma on its own.  Quasi-coherence of `𝒜_d` is a
> field of the relative Proj situation of Stacks 0849.

```lean
theorem isQuasicoherentOnSite_closedSubspaceGradedIdealObj
    (T : ClosedSubspaceTwistSections s P π) (i : Z ⟶ P)
    (hpush : ∀ d : ℕ, (twistedStructureDirectImage T i d).IsQuasicoherentOnSite) (d : ℕ) :
    (closedSubspaceGradedIdealObj T i d).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.C1359Bridge.exists_iso_quotientProjHom_psiKernelGradedIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjClosedSubspaceKernelProj.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjClosedSubspaceKernelProj.lean#L55). The attribute's comment: “Z ≅ Proj\_X(𝒜/ℐ) over P for π quasi-compact, ℐ the kernel of 𝒜 ⟶ ⨁\_\{d ≥ 0} π\_*((i\_*𝒪\_Z)(d))”.

> **Stacks 085L.**  Let `π : P = Proj_X(𝒜) ⟶ X` be the relative Proj of a quasi-coherent graded
> `𝒪_X`-algebra on an algebraic space `X` (twists `𝒪_P(d)` and `ψ` built from a presentation of
> `X`), and `i : Z ⟶ P` a closed subspace.  Let `ℐ ⊆ 𝒜` be the kernel of the canonical map
> `𝒜 ⟶ ⨁_{d ≥ 0} π_*((i_*𝒪_Z)(d))`: in degree `d ≥ 0` the sections killed by the adjoint
> `𝒜_d ⟶ π_*𝒪_P(d)` of `ψ_d` followed by `π_*` of `𝒪_P(d) ⟶ i_*i^*𝒪_P(d) = (i_*𝒪_Z)(d)`, and
> `ℐ_n = 𝒜_n = 0` for `n < 0`.  If `π` is quasi-compact, `ℐ` is a quasi-coherent graded ideal and
> there is an isomorphism `Z ≅ Proj_X(𝒜/ℐ)` over `P`.

```lean
theorem exists_iso_quotientProjHom_psiKernelGradedIdeal
    (hi : IsClosedImmersion s.site s.base s.containsBase i.hom)
    (hπ : IsQuasiCompact s.site s.base s.containsBase s.π.hom) :
    (∀ (d : ℕ) (V : (SmallEtale s.site s.base s.containsBase s.space.1)ᵒᵖ)
        (x : (s.algebra.piece (d : ℤ)).val.obj V),
        x ∈ ((psiKernelGradedIdeal s Px i hi hπ).piece (d : ℤ)).obj V ↔
          (psiKernelMap s Px i d (s.psiTwistHom Px d)).val.app V x = 0) ∧
      ∃ e : Z ≅ (psiKernelGradedIdeal s Px i hi hπ).quotientSituation.Proj,
        e.hom ≫ (psiKernelGradedIdeal s Px i hi hπ).quotientProjHom = i
```

## Tag 085M, a lemma

[Tag 085M](https://stacks.math.columbia.edu/tag/085M) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_finiteType_chartDegreeSubmodule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjChartSituation.lean, line 416](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjChartSituation.lean#L416). The attribute's comment: “the chart half: over an affine étale chart V of X there are d > 0 and a quasi-coherent finite type submodule ℱ of the module restriction (𝒜\_d)|\_V cutting out a closed subscheme of finite presentation of Proj\_V(𝒜|\_V), with no hypothesis beyond the tag's own, exactly as the scheme case Tag 0802. The globalization of ℱ to a submodule of 𝒜\_d on X — the colimit clause of Tag 0829, still resting on Tag 07V9 — and the descent of the presentation to X are NOT claimed, so the existence assertion of Tag 085M on X is not delivered here”.

> **Stacks 085M on an affine étale chart.**
>
> Let `𝒜` be the quasi-coherent graded `𝒪_X`-algebra of a relative Proj situation on an algebraic
> space `X`, let `V` be an étale chart of `X` with affine underlying scheme, and let `𝒜|_V` be the
> restriction of Stacks 01NN carried by `AlgebraicGeometry.Space.relativeProjChartSheafAlgebra`.
> For a closed subscheme `i : Z ⟶ Proj_V(𝒜|_V)` of finite presentation with `Proj_V(𝒜|_V) ⟶ V`
> quasi-compact there are a degree `d > 0` and a quasi-coherent finite type submodule
> `ℱ ⊆ (𝒜_d)|_V` of the **module restriction of `𝒜_d`** with `Z = Proj_V((𝒜|_V)/ℱ(𝒜|_V))`.
>
> This is the step of the source's proof reading "by the case of schemes, Divisors 0802, applied
> over `U`".  Compactness and quasi-separatedness of the base, which Stacks 0802 asks for, are
> discharged from affineness of the chart; the graded algebra is not an input but the restriction of
> `𝒜`, by `AlgebraicGeometry.Space.relativeProjChartSheafAlgebra_piece`, which is what makes the
> submodule a submodule of `(𝒜_d)|_V`.
>
> Neither the globalization of `ℱ` to a submodule of `𝒜_d` on `X` nor the descent of the
> presentation to `X` is claimed; see *What is not proved* in the module documentation.

```lean
theorem exists_finiteType_chartDegreeSubmodule
    (hV : _root_.AlgebraicGeometry.IsAffine (chartScheme V)) {Z : Scheme.{u}}
    (i : Z ⟶ (relativeProj (relativeProjChartSheafAlgebra s V hqc)).scheme)
    [_root_.AlgebraicGeometry.IsClosedImmersion i]
    [_root_.AlgebraicGeometry.QuasiCompact
      (relativeProj (relativeProjChartSheafAlgebra s V hqc)).toBase]
    (hi : _root_.AlgebraicGeometry.FinitePresentation i) :
    ∃ d : ℕ, 0 < d ∧
      ∃ ℱ : (restrictToChartScheme s.site s.base s.containsBase s.space.1 s.space.2
          (s.algebra.piece (d : ℤ)) V).Submodule,
        ℱ.toSheafOfModules.IsQuasicoherent ∧
          SheafOfModules.IsFiniteType.{u, u, u} ℱ.toSheafOfModules ∧
            Nonempty (DegreeQuotientPresentation
              (relativeProjChartSheafAlgebra s V hqc) i ℱ)
```

**`AlgebraicGeometry.Space.closedSubspaceDegreeProducts_le_ker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjClosedSubspaceFiniteType.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjClosedSubspaceFiniteType.lean#L221). The attribute's comment: “the containment Z ⊆ Proj\_X(𝒜/ℱ𝒜) in graded-ideal form: the graded ideal ℱ𝒜 generated by ℱ ⊆ 𝒜\_d is killed by every degreewise, bidegree-(d,e)-multiplicative map of graded algebras killing ℱ. The existence of d > 0 and of the finite type quasi-coherent ℱ is not claimed”.

> **Stacks 085M, the containment `Z ⊆ Proj_X(𝒜/ℱ𝒜)`, in graded-ideal form.**
>
> Let `ψ : 𝒜 ⟶ ℬ` be a degreewise map of graded `𝒪_X`-algebras which is multiplicative in the
> bidegree `(d, e)`, and suppose every local section of `ℱ ⊆ 𝒜_d` is killed by `ψ` — that is, `ℱ`
> consists of equations for the closed subspace `ℬ` presents.  Then every local section of the
> graded ideal `ℱ𝒜` in degree `d + e` is killed by `ψ` as well, so `ℱ𝒜` is contained in the graded
> ideal of that closed subspace.
>
> This is the step of the source's proof reading "`Z ⊆ Z'` since `ℱ𝒜 ⊆ ℐ`".  Its content is the
> passage from the objectwise products to the ideal they generate: the kernel of `ψ` has local
> membership, so a section of `𝒜_{d+e}` that is only *locally* a sum of products `a · b` with
> `a` a section of `ℱ` is killed by `ψ` too.
>
> Neither the degree `d > 0` nor the finite type submodule `ℱ` of the source's conclusion is
> produced here; see *What is not proved* in the module documentation.

```lean
theorem closedSubspaceDegreeProducts_le_ker
    {ℬ : SheafOfModules.GradedAlgebra.{u, u, u, u + 1}
      (structureRingSheaf s.site s.base s.containsBase s.space)}
    (ψ : ∀ n : ℤ, s.algebra.piece n ⟶ ℬ.piece n)
    (hmul : ∀ (U : (SmallEtale s.site s.base s.containsBase s.space.1)ᵒᵖ)
      (a : (s.algebra.piece d).val.obj U) (b : (s.algebra.piece e).val.obj U),
      (ψ (d + e)).val.app U ((s.algebra.mul d e).app U a b) =
        (ℬ.mul d e).app U ((ψ d).val.app U a) ((ψ e).val.app U b))
    {ℱ : (s.algebra.piece d).Submodule}
    (hℱ : ℱ ≤ Stacks.SheafOfModules.kerSubmodule (ψ d)) :
    closedSubspaceDegreeProducts s d e ℱ ≤
      Stacks.SheafOfModules.kerSubmodule (ψ (d + e))
```

**`AlgebraicGeometry.Space.RelativeProjSituation.exists_finiteType_iso_quotientProjHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjClosedSubspaceFiniteTypeIdealOfZ.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjClosedSubspaceFiniteTypeIdealOfZ.lean#L50).

> Let `X` be a quasi-compact and quasi-separated algebraic space, `𝒜` a quasi-coherent graded
> `𝒪_X`-algebra whose relative Proj `π : Proj_X(𝒜) ⟶ X` is quasi-compact, and
> `i : Z ⟶ Proj_X(𝒜)` a closed immersion locally of finite presentation. Then there are `d > 0`
> and a quasi-coherent `𝒪_X`-submodule `ℱ ⊆ 𝒜_d` of finite type such that `Z = Proj_X(𝒜/ℱ𝒜)` as
> closed subspaces of `Proj_X(𝒜)`.

```lean
theorem exists_finiteType_iso_quotientProjHom (s : RelativeProjSituation.{u, u})
    (hXqc : IsQuasiCompactSpace s.site s.base s.containsBase s.space.1)
    (hXqs : IsAbsolutelyQuasiSeparated s.site s.base s.containsBase
      (BigFppfSite.contains_terminal s.site) s.space.1)
    (hπ : IsQuasiCompact s.site s.base s.containsBase s.π.hom)
    {Z : AlgebraicSpaces s.site s.base s.containsBase} (i : Z ⟶ s.Proj)
    (hi : IsClosedImmersion s.site s.base s.containsBase i.hom)
    (hfp : IsLocallyOfFinitePresentation s.site s.base s.containsBase i.hom) :
    ∃ d : ℕ, 0 < d ∧ ∃ (F : (s.algebra.piece (d : ℤ)).Submodule)
      (hF : F.toSheafOfModules.IsQuasicoherentOnSite), F.toSheafOfModules.IsFiniteType ∧
        ∃ e : Z ≅ (GradedIdeal.ofDegree s F hF).quotientSituation.Proj,
          e.hom ≫ (GradedIdeal.ofDegree s F hF).quotientProjHom = i
```

## Tag 085N, a lemma

[Tag 085N](https://stacks.math.columbia.edu/tag/085N) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeProjSituation.exists_finiteType_degreeSubmodule_range_eq_quotientProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjClosedSubspaceQuotientPresentation.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjClosedSubspaceQuotientPresentation.lean#L235). The attribute's comment: “the relative Proj P = Proj\_X(𝒜) of Stacks 084A-084B; clause (a) is the equality of the ranges of i : Z ⟶ P and of the closed immersion Proj\_X(𝒜/ℱ𝒜) ⟶ P, clause (b) the disjointness from U of the support of 𝒜\_d/ℱ; the closed subspace written i : Z → X in the source is i : Z ⟶ P, which condition (3) and clause (a) require”.

> **Stacks 085N.**  Let `X` be a quasi-compact and quasi-separated algebraic space over `S`,
> `𝒜` a quasi-coherent graded `𝒪_X`-algebra and `π : P = Proj_X(𝒜) ⟶ X` its relative Proj
> (Stacks 084A–084B).  Let `i : Z ⟶ P` be a closed subspace and `U ⊆ |X|` open.  Assume
> (1) `π` quasi-compact, (2) `i` of finite presentation, (3) `|U| ∩ |π|(|i|(|Z|)) = ∅`,
> (4) `U` quasi-compact and (5) every `𝒜_n` of finite type.  Then there are `d > 0` and a
> quasi-coherent `𝒪_X`-submodule of finite type `ℱ ⊆ 𝒜_d` with (a) `Z = Proj_X(𝒜/ℱ𝒜)` and
> (b) the support of `𝒜_d/ℱ` disjoint from `U`.
>
> Clause (a) says that `Z` and the closed subspace `Proj_X(𝒜/ℱ𝒜) ⟶ P`
> (`AlgebraicGeometry.Space.RelativeProjSituation.quotientProjHom` of the graded ideal `ℱ𝒜`,
> `AlgebraicGeometry.Space.RelativeProjSituation.degreeIdeal`) have the same range in `P`; clause
> (b) is disjointness from `U` of the support (Stacks 04KA) of the cokernel of `ℱ ⊆ 𝒜_d`.
> "`X` quasi-separated" is `AlgebraicGeometry.Space.IsAbsolutelyQuasiSeparated` (Stacks 03BS).
> The source writes the closed subspace as `i : Z → X`; its hypothesis (3) and conclusion (a) place
> `Z` in `P`, and it is formalized as `i : Z ⟶ P`.

```lean
theorem exists_finiteType_degreeSubmodule_range_eq_quotientProj
    (hX : IsQuasiCompactSpace s.site s.base s.containsBase s.space.1)
    (hXqs : IsAbsolutelyQuasiSeparated s.site s.base s.containsBase s.site.contains_terminal
      s.space.1)
    {Z : AlgebraicSpaces s.site s.base s.containsBase} (i : Z.1 ⟶ s.relativeProjFunctor)
    (hi : IsClosedImmersion s.site s.base s.containsBase i)
    (hπ : IsQuasiCompact s.site s.base s.containsBase s.relativeProjπ)
    (hfp : IsFinitePresentation s.site s.base s.containsBase i)
    {U : Set (points s.site s.base s.containsBase s.space.1)}
    (hZU : Disjoint U (Set.range fun z ↦
      pointsMap s.site s.base s.containsBase s.relativeProjFunctor s.relativeProjπ
        (pointsMap s.site s.base s.containsBase Z.1 i z)))
    (hU : IsOpen U) (hUc : IsCompact U)
    (hA : ∀ n : ℤ, SheafOfModules.IsFiniteType (s.algebra.piece n)) :
    ∃ (d : ℕ) (_ : 0 < d) (ℱ : (s.algebra.piece (d : ℤ)).Submodule)
      (hℱ : ℱ.toSheafOfModules.IsQuasicoherentOnSite),
      SheafOfModules.IsFiniteType ℱ.toSheafOfModules ∧
        Subfunctor.range i = Subfunctor.range (s.quotientProjHom (s.degreeIdeal ℱ)
          (s.isQuasicoherentOnSite_degreeIdeal_piece ℱ hℱ)) ∧
        Disjoint (supportOfSheaf s.site s.base s.containsBase s.space.1
          ((SheafOfModules.toSheaf (structureRingSheaf s.site s.base s.containsBase
            s.space)).obj (cokernel ℱ.ι))) U
```

**`AlgebraicGeometry.Space.exists_finiteType_degreeSubmodule_disjoint_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjClosedSubspaceSupport.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjClosedSubspaceSupport.lean#L223). The attribute's comment: “the relative Proj P = Proj\_X(𝒜) of Stacks 084A-084B; clause (a) as the data ClosedSubspaceDegreeQuotientPresentation (Z identified over P with Proj\_X(𝒜/ℱ𝒜) and its closed immersion into P), clause (b) the disjointness from U of the support of 𝒜\_d/ℱ; the closed subspace written i : Z → X in the source is i : Z ⟶ P, which condition (3) and clause (a) require”.

> **Stacks 085N.**  Let `S` be a scheme, `X` a quasi-compact and quasi-separated algebraic
> space over `S` and `𝒜` a quasi-coherent graded `𝒪_X`-algebra; let `π : P = Proj_X(𝒜) ⟶ X` be the
> relative Proj (`…RelativeProjSituation.relativeProjFunctor`), let `i : Z ⟶ P` be a closed subspace
> and let `U` be an open of `|X|`.  Assume (1) `π` quasi-compact, (2) `i` of finite presentation,
> (3) `|U| ∩ |π|(|i|(|Z|)) = ∅`, (4) `U` quasi-compact and (5) every `𝒜_n` of finite type.  Then
> there are a degree `d > 0` and a quasi-coherent finite type `𝒪_X`-submodule `ℱ ⊆ 𝒜_d` with
> (a) `Z = Proj_X(𝒜/ℱ𝒜)` and (b) the support of `𝒜_d/ℱ` disjoint from `U`.
>
> Clause (a) is the structure `AlgebraicGeometry.Space.ClosedSubspaceDegreeQuotientPresentation`,
> the form in which Stacks 085M records the same assertion; clause (b) is disjointness from `U` of
> the support of Stacks 04KA of the cokernel of `ℱ ⊆ 𝒜_d`.  This is
> `…RelativeProjSituation.exists_finiteType_degreeSubmodule_range_eq_quotientProj`, whose clause (a)
> is the equality of the ranges of `i` and of `Proj_X(𝒜/ℱ𝒜) ⟶ P`, read through
> `…RelativeProjSituation.nonempty_closedSubspaceDegreeQuotientPresentation_of_range_eq`.

```lean
theorem exists_finiteType_degreeSubmodule_disjoint_support
    (hX : IsQuasiCompactSpace s.site s.base s.containsBase s.space.1)
    (hXqs : IsAbsolutelyQuasiSeparated s.site s.base s.containsBase s.site.contains_terminal
      s.space.1)
    {Z : AlgebraicSpaces s.site s.base s.containsBase}
    (i : Z ⟶ (⟨s.relativeProjFunctor, s.isAlgebraicSpace_relativeProjFunctor⟩ :
      AlgebraicSpaces s.site s.base s.containsBase))
    (hi : IsClosedImmersion s.site s.base s.containsBase i.hom)
    (hπ : IsQuasiCompact s.site s.base s.containsBase s.relativeProjπ)
    (hfp : IsFinitePresentation s.site s.base s.containsBase i.hom)
    {U : Set (points s.site s.base s.containsBase s.space.1)}
    (hZU : Disjoint U (Set.range fun z ↦
      pointsMap s.site s.base s.containsBase s.relativeProjFunctor s.relativeProjπ
        (pointsMap s.site s.base s.containsBase Z.1 i.hom z)))
    (hU : IsOpen U) (hUc : IsCompact U)
    (hA : ∀ n : ℤ, SheafOfModules.IsFiniteType (s.algebra.piece n)) :
    ∃ (d : ℕ) (hd : 0 < d) (ℱ : (s.algebra.piece (d : ℤ)).Submodule),
      ℱ.toSheafOfModules.IsQuasicoherentOnSite ∧
        SheafOfModules.IsFiniteType ℱ.toSheafOfModules ∧
          Nonempty (ClosedSubspaceDegreeQuotientPresentation i hd ℱ) ∧
            Disjoint (supportOfSheaf s.site s.base s.containsBase s.space.1
              ((SheafOfModules.toSheaf (structureRingSheaf s.site s.base s.containsBase
                s.space)).obj (cokernel ℱ.ι))) U
```

## Tag 0B4I, a lemma

[Tag 0B4I](https://stacks.math.columbia.edu/tag/0B4I) in the Stacks Project.

**`AlgebraicGeometry.Space.projectiveBundleSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProjectiveBundle/SectionsClassification.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProjectiveBundle/SectionsClassification.lean#L70). The attribute's comment: “the bijection between sections of P(E) -> X and invertible quotients of E”.

> **The bijection of Stacks 0B4I** between the sections of `π : 𝐏(ℰ) ⟶ X` and the isomorphism
> classes of invertible quotients of `ℰ`, characterized in
> `projectiveBundle_sections_invertibleQuotients`.

```lean
def projectiveBundleSectionsEquiv :
    {σ : X ⟶ relativeProjSymmetricAlgebra X E hE hb // σ ≫ projectiveBundleπ X E hE hb = 𝟙 X} ≃
      InvertibleQuotientClass X E
```

**`AlgebraicGeometry.Space.projectiveBundle_sections_invertibleQuotients`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProjectiveBundle/SectionsClassification.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProjectiveBundle/SectionsClassification.lean#L123). The attribute's comment: “the bijection between sections of P(E) -> X and invertible quotients of E, its characterization at scheme points, sections are closed immersions, and compatibility with base change”.

> **Stacks 0B4I: sections of `𝐏(ℰ) ⟶ X`, invertible quotients of `ℰ`, and base change.**
>
> Let `X` be an algebraic space and `ℰ` a quasi-coherent `𝒪_X`-module, with projective bundle
> `π : 𝐏(ℰ) = Proj_X(Sym(ℰ)) ⟶ X` (Stacks 084C).
>
> 1. **The bijection** `projectiveBundleSectionsEquiv` between the sections `σ` of `π` and the
>    isomorphism classes of surjections `ℰ ⟶ ℒ` onto invertible `𝒪_X`-modules is the canonical one:
>    it sends `σ` to `c` exactly when, at every scheme point `x : T ⟶ X`, the point `x ≫ σ` of
>    `𝐏(ℰ)` over `x` corresponds to the pullback of `c` to `T` under the identification of the points
>    of `𝐏(ℰ)` over `x` with the invertible quotients of `x^*ℰ`
>    (`pointsEquivInvertibleQuotientClass`: Stacks 084B, the comparison of `x^*Sym(ℰ)` with
>    `Sym(x^*ℰ)`, and Stacks 0B3V on `T`).
> 2. Every section of `π` is a closed immersion.
> 3. **Compatibility with base change**: for `g : X' ⟶ X`, the square formed by
>    `projectiveBundleBaseChange : 𝐏(g^*ℰ) ⟶ 𝐏(ℰ)`, the two projections and `g` is cartesian, and
>    a section `σ'` of `𝐏(g^*ℰ) ⟶ X'` lying over a section `σ` of `𝐏(ℰ) ⟶ X` corresponds to the
>    pullback along `g` of the invertible quotient `σ` corresponds to.
>
> The homogeneous sections of `Sym(ℰ)` (and of `Sym(g^*ℰ)`) are bounded by the cutoff of the site
> (`SymmetricAlgebraBounded`), the set-theoretic convention of Situation 0849 under which the
> relative Proj is an algebraic space over the chosen site.

```lean
theorem projectiveBundle_sections_invertibleQuotients :
    (∀ (σ : {σ : X ⟶ relativeProjSymmetricAlgebra X E hE hb //
          σ ≫ projectiveBundleπ X E hE hb = 𝟙 X})
        (c : InvertibleQuotientClass X E),
      projectiveBundleSectionsEquiv X E hE hb σ = c ↔
        ∀ (T : BigFppfOver B S hS) (x : yoneda.obj T ⟶ X.1),
          pointsEquivInvertibleQuotientClass X E hE hb T x ⟨x ≫ σ.1.hom,
            comp_section_comp (projectiveBundleπ X E hE hb).hom x
              (congrArg InducedCategory.Hom.hom σ.2)⟩ = pointRestrictClass X E T x c) ∧
    (∀ σ : X ⟶ relativeProjSymmetricAlgebra X E hE hb, σ ≫ projectiveBundleπ X E hE hb = 𝟙 X →
      IsClosedImmersion B S hS σ.hom) ∧
    (∀ (X' : AlgebraicSpaces B S hS) (g : X' ⟶ X)
        (hb' : SymmetricAlgebraBounded X' ((modulePullback B S hS g).obj E)),
      IsPullback (projectiveBundleBaseChange X E hE hb g hb').hom
          (projectiveBundleπ X' _ (isQuasicoherentOnSite_modulePullback_projectiveBundle X E hE g)
            hb').hom
          (projectiveBundleπ X E hE hb).hom g.hom ∧
        ∀ (σ : {σ : X ⟶ relativeProjSymmetricAlgebra X E hE hb //
            σ ≫ projectiveBundleπ X E hE hb = 𝟙 X})
          (σ' : {σ' : X' ⟶ relativeProjSymmetricAlgebra X' ((modulePullback B S hS g).obj E)
              (isQuasicoherentOnSite_modulePullback_projectiveBundle X E hE g) hb' //
            σ' ≫ projectiveBundleπ X' _ _ hb' = 𝟙 X'}),
          σ'.1 ≫ projectiveBundleBaseChange X E hE hb g hb' = g ≫ σ.1 →
            projectiveBundleSectionsEquiv X' _ _ hb' σ' =
              invertibleQuotientBaseChangeClass g (Iso.refl _)
                (projectiveBundleSectionsEquiv X E hE hb σ))
```

**`AlgebraicGeometry.Space.projectiveBundle_sectionConormalIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProjectiveBundle/SectionsConormalClassification.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProjectiveBundle/SectionsConormalClassification.lean#L68). The attribute's comment: “the canonical isomorphism Ker(E -> L) tensor L^\{-1} = conormal sheaf of sigma(X) in P(E), and its compatibility with base change”.

> **Stacks 0B4I, the conormal isomorphism and its base change.**  For a section `σ` of
> `𝐏(ℰ) ⟶ X` corresponding to `q : ℰ ⟶ ℒ` there is a unique `Ker(q) ⊗ ℒ^{⊗ -1} ≅ 𝒞_{σ(X)/𝐏(ℰ)}`
> restricting on every étale chart to the chart isomorphism of Stacks 0B3V; along `g : X' ⟶ X` with
> `σ'` over `σ`, these isomorphisms for `q` and `g^*q` commute with the base-change maps.

```lean
theorem projectiveBundle_sectionConormalIso :
    (∀ (σ : X ⟶ relativeProjSymmetricAlgebra X E hE hb) (hσ : σ ≫ projectiveBundleπ X E hE hb = 𝟙 X)
        (Q : InvertibleQuotient X E)
        (hQ : projectiveBundleSectionsEquiv X E hE hb ⟨σ, hσ⟩ = Quotient.mk _ Q),
      ∃! φ : sectionConormalSource X E Q ≅ sectionConormalTarget X E hE hb σ hσ,
        ∀ U : SmallEtale B S hS X.1, (chartModuleRestriction B S hS X U).map φ.hom =
          (sectionConormalChartFamilyOf X E hE Q hb σ hσ
            (fun (T : BigFppfOver B S hS) (x : yoneda.obj T ⟶ X.1) =>
        haveI : IsInvertible (structureCommRings B S hS X) (structureRingSheaf B S hS X).property
            Q.L := Q.invertible.toAlgebraicGeometry
        (CategoryTheory.Functor.compBifunctorMap (𝒞 := ((BigFppfOver.toScheme B S hS).obj
            T).Modules) (iC := Scheme.Modules.instCategory)
        (Stacks.SheafOfModules.Tensor.sheafTensor ⟨((BigFppfOver.toScheme B S hS).obj T).presheaf,
          Presheaf.isSheaf_of_isSheaf_comp _ ((BigFppfOver.toScheme B S hS).obj T).presheaf
            (forget₂ CommRingCat RingCat) ((BigFppfOver.toScheme B S hS).obj T).ringCatSheaf.2⟩)
        ((zariskiReadingFunctor T).map (modulePullbackTensorIso B S hS (pointHom x) (kernel Q.q)
            (Stacks.SheafOfModules.Invertible.tensorPower (structureCommRings B S hS X)
            (structureRingSheaf B S hS X).property Q.L (-1))).hom ≫ ((zariskiReadingTensorObjIso T
            ((modulePullback B S hS (pointHom x)).obj (kernel Q.q)) ((modulePullback B S hS
            (pointHom x)).obj (Stacks.SheafOfModules.Invertible.tensorPower (structureCommRings B S
            hS X) (structureRingSheaf B S hS X).property Q.L (-1)))
            (isQuasicoherentOnSite_modulePullback_of_isQuasicoherentOnSite B S hS (pointHom x)
            (kernel Q.q) (isQuasicoherentOnSite_kernel_q X E hE Q))
            (isQuasicoherentOnSite_modulePullback_of_isQuasicoherentOnSite B S hS (pointHom x)
            (Stacks.SheafOfModules.Invertible.tensorPower (structureCommRings B S hS X)
            (structureRingSheaf B S hS X).property Q.L (-1))
            (isQuasicoherentOnSite_invertibleTensorPower X Q.L (-1)))).hom ≫
            (monoidalTensorSheafTensorIso ((BigFppfOver.toScheme B S hS).obj T)
            ((zariskiReadingFunctor T).obj ((modulePullback B S hS (pointHom x)).obj (kernel Q.q)))
            ((zariskiReadingFunctor T).obj ((modulePullback B S hS (pointHom x)).obj
            (Stacks.SheafOfModules.Invertible.tensorPower (structureCommRings B S hS X)
            (structureRingSheaf B S hS X).property Q.L (-1))))).hom))
        (kernelPointReadingHom X E hE Q T x) (inversePointReadingIso X T x Q.L).hom))
            (fun T x hx => isIso_conormalSourcePointReading_of_isEtale X E hE Q T x hx) hQ U).hom) ∧
    (∀ (X' : AlgebraicSpaces B S hS) (g : X' ⟶ X)
        (hb' : SymmetricAlgebraBounded X' ((modulePullback B S hS g).obj E))
        (σ : X ⟶ relativeProjSymmetricAlgebra X E hE hb) (hσ : σ ≫ projectiveBundleπ X E hE hb = 𝟙
            X)
        (σ' : X' ⟶ relativeProjSymmetricAlgebra X' ((modulePullback B S hS g).obj E)
          (isQuasicoherentOnSite_modulePullback_projectiveBundle X E hE g) hb')
        (hσ' : σ' ≫ projectiveBundleπ X' ((modulePullback B S hS g).obj E)
          (isQuasicoherentOnSite_modulePullback_projectiveBundle X E hE g) hb' = 𝟙 X')
        (comm : σ' ≫ (projectiveBundleBaseChange X E hE hb g hb') = g ≫ σ)
        (Q : InvertibleQuotient X E)
        (hQ : projectiveBundleSectionsEquiv X E hE hb ⟨σ, hσ⟩ = Quotient.mk _ Q)
        (φ : sectionConormalSource X E Q ≅ sectionConormalTarget X E hE hb σ hσ)
        (hφ : ∀ U : SmallEtale B S hS X.1, (chartModuleRestriction B S hS X U).map φ.hom =
            (sectionConormalChartFamilyOf X E hE Q hb σ hσ
            (fun (T : BigFppfOver B S hS) (x : yoneda.obj T ⟶ X.1) =>
          (haveI : IsInvertible (structureCommRings B S hS X) (structureRingSheaf B S hS X).property
              Q.L := Q.invertible.toAlgebraicGeometry
          (CategoryTheory.Functor.compBifunctorMap (𝒞 := ((BigFppfOver.toScheme B S hS).obj
              T).Modules) (iC := Scheme.Modules.instCategory)
          (Stacks.SheafOfModules.Tensor.sheafTensor ⟨((BigFppfOver.toScheme B S hS).obj T).presheaf,
            Presheaf.isSheaf_of_isSheaf_comp _ ((BigFppfOver.toScheme B S hS).obj T).presheaf
              (forget₂ CommRingCat RingCat) ((BigFppfOver.toScheme B S hS).obj T).ringCatSheaf.2⟩)
          ((zariskiReadingFunctor T).map (modulePullbackTensorIso B S hS (pointHom x) (kernel Q.q)
              (Stacks.SheafOfModules.Invertible.tensorPower (structureCommRings B S hS X)
              (structureRingSheaf B S hS X).property Q.L (-1))).hom ≫ ((zariskiReadingTensorObjIso T
              ((modulePullback B S hS (pointHom x)).obj (kernel Q.q)) ((modulePullback B S hS
              (pointHom x)).obj (Stacks.SheafOfModules.Invertible.tensorPower (structureCommRings B
              S hS X) (structureRingSheaf B S hS X).property Q.L (-1)))
              (isQuasicoherentOnSite_modulePullback_of_isQuasicoherentOnSite B S hS (pointHom x)
              (kernel Q.q) (isQuasicoherentOnSite_kernel_q X E hE Q))
              (isQuasicoherentOnSite_modulePullback_of_isQuasicoherentOnSite B S hS (pointHom x)
              (Stacks.SheafOfModules.Invertible.tensorPower (structureCommRings B S hS X)
              (structureRingSheaf B S hS X).property Q.L (-1))
              (isQuasicoherentOnSite_invertibleTensorPower X Q.L (-1)))).hom ≫
              (monoidalTensorSheafTensorIso ((BigFppfOver.toScheme B S hS).obj T)
              ((zariskiReadingFunctor T).obj ((modulePullback B S hS (pointHom x)).obj (kernel
              Q.q))) ((zariskiReadingFunctor T).obj ((modulePullback B S hS (pointHom x)).obj
              (Stacks.SheafOfModules.Invertible.tensorPower (structureCommRings B S hS X)
              (structureRingSheaf B S hS X).property Q.L (-1))))).hom))
          (kernelPointReadingHom X E hE Q T x) (inversePointReadingIso X T x Q.L).hom)))
            (fun T x hx => isIso_conormalSourcePointReading_of_isEtale X E hE Q T x hx) hQ U).hom)
        (φ' : sectionConormalSource X' ((modulePullback B S hS g).obj E) (Q.baseChange g (Iso.refl
            _)) ≅ sectionConormalTarget X' ((modulePullback B S hS g).obj E)
            (isQuasicoherentOnSite_modulePullback_projectiveBundle X E hE g) hb' σ' hσ')
        (hφ' : ∀ V : SmallEtale B S hS X'.1, (chartModuleRestriction B S hS X' V).map φ'.hom =
            (sectionConormalChartFamilyOf X' ((modulePullback B S hS g).obj E)
                (isQuasicoherentOnSite_modulePullback_projectiveBundle X E hE g) (Q.baseChange g
                (Iso.refl _)) hb' σ' hσ'
            (fun (T : BigFppfOver B S hS) (x : yoneda.obj T ⟶ X'.1) =>
          (haveI : IsInvertible (structureCommRings B S hS X') (structureRingSheaf B S hS
              X').property (Q.baseChange g (Iso.refl _)).L := (Q.baseChange g (Iso.refl
              _)).invertible.toAlgebraicGeometry
          (CategoryTheory.Functor.compBifunctorMap (𝒞 := ((BigFppfOver.toScheme B S hS).obj
              T).Modules) (iC := Scheme.Modules.instCategory)
          (Stacks.SheafOfModules.Tensor.sheafTensor ⟨((BigFppfOver.toScheme B S hS).obj T).presheaf,
            Presheaf.isSheaf_of_isSheaf_comp _ ((BigFppfOver.toScheme B S hS).obj T).presheaf
              (forget₂ CommRingCat RingCat) ((BigFppfOver.toScheme B S hS).obj T).ringCatSheaf.2⟩)
          ((zariskiReadingFunctor T).map (modulePullbackTensorIso B S hS (pointHom x) (kernel
              (Q.baseChange g (Iso.refl _)).q) (Stacks.SheafOfModules.Invertible.tensorPower
              (structureCommRings B S hS X') (structureRingSheaf B S hS X').property (Q.baseChange g
              (Iso.refl _)).L (-1))).hom ≫ ((zariskiReadingTensorObjIso T ((modulePullback B S hS
              (pointHom x)).obj (kernel (Q.baseChange g (Iso.refl _)).q)) ((modulePullback B S hS
              (pointHom x)).obj (Stacks.SheafOfModules.Invertible.tensorPower (structureCommRings B
              S hS X') (structureRingSheaf B S hS X').property (Q.baseChange g (Iso.refl _)).L
              (-1))) (isQuasicoherentOnSite_modulePullback_of_isQuasicoherentOnSite B S hS (pointHom
              x) (kernel (Q.baseChange g (Iso.refl _)).q) (isQuasicoherentOnSite_kernel_q X'
              ((modulePullback B S hS g).obj E)
              (isQuasicoherentOnSite_modulePullback_projectiveBundle X E hE g) (Q.baseChange g
              (Iso.refl _)))) (isQuasicoherentOnSite_modulePullback_of_isQuasicoherentOnSite B S hS
              (pointHom x) (Stacks.SheafOfModules.Invertible.tensorPower (structureCommRings B S hS
              X') (structureRingSheaf B S hS X').property (Q.baseChange g (Iso.refl _)).L (-1))
              (isQuasicoherentOnSite_invertibleTensorPower X' (Q.baseChange g (Iso.refl _)).L
              (-1)))).hom ≫ (monoidalTensorSheafTensorIso ((BigFppfOver.toScheme B S hS).obj T)
              ((zariskiReadingFunctor T).obj ((modulePullback B S hS (pointHom x)).obj (kernel
              (Q.baseChange g (Iso.refl _)).q))) ((zariskiReadingFunctor T).obj ((modulePullback B S
              hS (pointHom x)).obj (Stacks.SheafOfModules.Invertible.tensorPower (structureCommRings
              B S hS X') (structureRingSheaf B S hS X').property (Q.baseChange g (Iso.refl _)).L
              (-1))))).hom))
          (kernelPointReadingHom X' ((modulePullback B S hS g).obj E)
              (isQuasicoherentOnSite_modulePullback_projectiveBundle X E hE g) (Q.baseChange g
              (Iso.refl _)) T x) (inversePointReadingIso X' T x (Q.baseChange g (Iso.refl
              _)).L).hom)))
            (fun T x hx => isIso_conormalSourcePointReading_of_isEtale X' ((modulePullback B S hS
                g).obj E) (isQuasicoherentOnSite_modulePullback_projectiveBundle X E hE g)
                (Q.baseChange g (Iso.refl _)) T x hx) (projectiveBundleSectionsEquiv_baseChange_mk X
                E hE hb g hb' σ hσ σ' hσ' comm Q hQ) V).hom),
      (@CategoryStruct.comp _ _ ((modulePullback B S hS g).obj
          (haveI : IsInvertible (structureCommRings B S hS X) (structureRingSheaf B S hS X).property
              Q.L := Q.invertible.toAlgebraicGeometry; (MonoidalCategory.tensorObj (C := Modules.{u,
              u} B S hS X.1 X.2) (kernel Q.q) (Stacks.SheafOfModules.Invertible.tensorPower
              (structureCommRings B S hS X) (structureRingSheaf B S hS X).property Q.L (-1)))))
              ((modulePullback B S hS g).obj (conormalModuleOfImmersion B S hS
              (relativeProjSymmetricAlgebra X E hE hb).2 X.2 σ.hom
          (isImmersion_of_isClosedImmersion B S hS
            (isClosedImmersion_of_section_projectiveBundleπ X E hE hb σ hσ))))
                (conormalModuleOfImmersion B S hS (relativeProjSymmetricAlgebra X' ((modulePullback
                B S hS g).obj E) (isQuasicoherentOnSite_modulePullback_projectiveBundle X E hE g)
                hb').2 X'.2 σ'.hom
          (isImmersion_of_isClosedImmersion B S hS
            (isClosedImmersion_of_section_projectiveBundleπ X' ((modulePullback B S hS g).obj E)
                (isQuasicoherentOnSite_modulePullback_projectiveBundle X E hE g) hb' σ' hσ')))
                ((modulePullback B S hS g).map (X :=
                (haveI : IsInvertible (structureCommRings B S hS X) (structureRingSheaf B S hS
                    X).property Q.L := Q.invertible.toAlgebraicGeometry; (MonoidalCategory.tensorObj
                    (C := Modules.{u, u} B S hS X.1 X.2) (kernel Q.q)
                    (Stacks.SheafOfModules.Invertible.tensorPower (structureCommRings B S hS X)
                    (structureRingSheaf B S hS X).property Q.L (-1))))) (Y :=
                    (conormalModuleOfImmersion B S hS (relativeProjSymmetricAlgebra X E hE hb).2 X.2
                    σ.hom
          (isImmersion_of_isClosedImmersion B S hS
            (isClosedImmersion_of_section_projectiveBundleπ X E hE hb σ hσ)))) φ.hom)
                (sectionConormalTargetBaseChangeHom X E hE hb σ hσ g hb' σ' hσ' comm)) =
                (@CategoryStruct.comp _ _ ((modulePullback B S hS g).obj
                (haveI : IsInvertible (structureCommRings B S hS X) (structureRingSheaf B S hS
                    X).property Q.L := Q.invertible.toAlgebraicGeometry; (MonoidalCategory.tensorObj
                    (C := Modules.{u, u} B S hS X.1 X.2) (kernel Q.q)
                    (Stacks.SheafOfModules.Invertible.tensorPower (structureCommRings B S hS X)
                    (structureRingSheaf B S hS X).property Q.L (-1)))))
                (haveI : IsInvertible (structureCommRings B S hS X') (structureRingSheaf B S hS
                    X').property (Q.baseChange g (Iso.refl _)).L := (Q.baseChange g (Iso.refl
                    _)).invertible.toAlgebraicGeometry; (MonoidalCategory.tensorObj (C :=
                    Modules.{u, u} B S hS X'.1 X'.2) (kernel (Q.baseChange g (Iso.refl _)).q)
                    (Stacks.SheafOfModules.Invertible.tensorPower (structureCommRings B S hS X')
                    (structureRingSheaf B S hS X').property (Q.baseChange g (Iso.refl _)).L (-1))))
                    (conormalModuleOfImmersion B S hS (relativeProjSymmetricAlgebra X'
                    ((modulePullback B S hS g).obj E)
                    (isQuasicoherentOnSite_modulePullback_projectiveBundle X E hE g) hb').2 X'.2
                    σ'.hom
          (isImmersion_of_isClosedImmersion B S hS
            (isClosedImmersion_of_section_projectiveBundleπ X' ((modulePullback B S hS g).obj E)
                (isQuasicoherentOnSite_modulePullback_projectiveBundle X E hE g) hb' σ' hσ')))
                (sectionConormalSourceBaseChangeHom X E Q g) (Iso.hom (X :=
                (haveI : IsInvertible (structureCommRings B S hS X') (structureRingSheaf B S hS
                    X').property (Q.baseChange g (Iso.refl _)).L := (Q.baseChange g (Iso.refl
                    _)).invertible.toAlgebraicGeometry; (MonoidalCategory.tensorObj (C :=
                    Modules.{u, u} B S hS X'.1 X'.2) (kernel (Q.baseChange g (Iso.refl _)).q)
                    (Stacks.SheafOfModules.Invertible.tensorPower (structureCommRings B S hS X')
                    (structureRingSheaf B S hS X').property (Q.baseChange g (Iso.refl _)).L (-1)))))
                    (Y := (conormalModuleOfImmersion B S hS (relativeProjSymmetricAlgebra X'
                    ((modulePullback B S hS g).obj E)
                    (isQuasicoherentOnSite_modulePullback_projectiveBundle X E hE g) hb').2 X'.2
                    σ'.hom
          (isImmersion_of_isClosedImmersion B S hS
            (isClosedImmersion_of_section_projectiveBundleπ X' ((modulePullback B S hS g).obj E)
                (isQuasicoherentOnSite_modulePullback_projectiveBundle X E hE g) hb' σ' hσ'))))
                φ')))
```

**`AlgebraicGeometry.Space.TautologicalDatum.pullbackQuotient`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SectionsInvertibleQuotients.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SectionsInvertibleQuotients.lean#L203). The attribute's comment: “the invertible quotient attached to a section, given the 03LU unit law”.

> The invertible quotient of `E` classified by a section of `π`.

```lean
def pullbackQuotient (D : TautologicalDatum π E) {σ : X ⟶ P} (hσ : σ ≫ π = 𝟙 X) :
    InvertibleQuotient X E
```

**`AlgebraicGeometry.Space.TautologicalDatum.sectionsEquivInvertibleQuotients`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SectionsInvertibleQuotients.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SectionsInvertibleQuotients.lean#L283). The attribute's comment: “the bijection, for a universal tautological datum, given the 03LU unit law”.

> The bijection between the sections of `π` and the invertible quotients of `E` up to
> isomorphism, for a universal tautological datum, sending a section to the quotient it pulls
> back.

```lean
def sectionsEquivInvertibleQuotients (D : TautologicalDatum π E) (hD : IsUniversal hc D) :
    { σ : X ⟶ P // σ ≫ π = 𝟙 X } ≃ InvertibleQuotientClass X E
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 71.16, Tag 085K](https://stacks.math.columbia.edu/tag/085K)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
