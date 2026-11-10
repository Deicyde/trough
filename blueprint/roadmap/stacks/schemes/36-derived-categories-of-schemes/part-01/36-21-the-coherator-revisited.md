---
declaration: section
origin: cited
lean: Stacks.Duality.Coherator.isLeftAdjoint_quasiCoherentι, Stacks.Duality.Coherator.exists_isTriangulated_rightAdjoint_quasiCoherentι, Stacks.Duality.coheratorDerivedPushforwardIso, Stacks.Duality.coheratorDerivedPushforwardIsoOfQcqs, Stacks.Duality.Coherator.mayerVietorisTriangle, Stacks.Duality.Coherator.mayerVietorisTriangle_distinguished, Stacks.Duality.Coherator.exists_distTriang_rightAdjoint_quasiCoherentι, Stacks.Duality.Coherator.exists_coherator_distTriang
statement: formalized
proof: formalized
---

# 36.21 The coherator revisited

Section 36.21 of the Stacks Project, [Tag 0CQZ](https://stacks.math.columbia.edu/tag/0CQZ). 5 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CR0, a lemma

[Tag 0CR0](https://stacks.math.columbia.edu/tag/0CR0) in the Stacks Project.

**`Stacks.Duality.Coherator.isLeftAdjoint_quasiCoherentι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/QcqsCoherator.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/QcqsCoherator.lean#L183).

> Let `X` be a quasi-compact and quasi-separated scheme. The inclusion functor
> `D_QCoh(𝒪_X) ⥤ D(𝒪_X)` has a right adjoint `DQ_X`.

```lean
theorem isLeftAdjoint_quasiCoherentι : (quasiCoherentι X).IsLeftAdjoint
```

**`Stacks.Duality.Coherator.exists_isTriangulated_rightAdjoint_quasiCoherentι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/QcqsCoherator.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/QcqsCoherator.lean#L190). The attribute's comment: “the coherator is exact”.

> For a quasi-compact quasi-separated scheme `X` the inclusion `D_QCoh(𝒪_X) ⥤ D(𝒪_X)` has a
> right adjoint `DQ_X` together with a `Functor.CommShift ℤ` structure making the adjunction
> triangulated.

```lean
theorem exists_isTriangulated_rightAdjoint_quasiCoherentι :
    ∃ (DQ : DerivedCategory X.Modules ⥤ quasiCoherentDerivedCategory X)
      (adj : quasiCoherentι X ⊣ DQ) (_ : DQ.CommShift ℤ), adj.IsTriangulated
```

## Tag 0CR1, a lemma

[Tag 0CR1](https://stacks.math.columbia.edu/tag/0CR1) in the Stacks Project.

**`Stacks.Duality.coheratorDerivedPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/DerivedPushforwardCommutation.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/DerivedPushforwardCommutation.lean#L132).

> **Derived direct image commutes with the coherator.** Let `f : X ⟶ Y` be a morphism of
> schemes along which `Rf_*` preserves quasi-coherence of cohomology — as it does whenever `f` is
> quasi-compact and quasi-separated, by [Stacks, Tag 08D5] part (1) — and suppose the inclusions
> `D_QCoh ⥤ D` admit right adjoints `DQ_X` and `DQ_Y` on `X` and on `Y`. Then the two functors
> `D(𝒪_X) ⥤ D_QCoh(𝒪_Y)` given by `Rf_* ∘ DQ_X` and by `DQ_Y ∘ Rf_*` are canonically isomorphic.
>
> Both are right adjoint to `Lf^* : D_QCoh(𝒪_Y) ⥤ D(𝒪_X)`, which lands in `D_QCoh(𝒪_X)` by
> [Stacks, Tag 08DW] part (1), so they are identified by uniqueness of right adjoints.

```lean
def coheratorDerivedPushforwardIso :
    DQX ⋙ quasiCoherentDerivedPushforward f hpush ≅ derivedPushforward f ⋙ DQY
```

**`Stacks.Duality.coheratorDerivedPushforwardIsoOfQcqs`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/DerivedPushforwardCommutationQcqs.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/DerivedPushforwardCommutationQcqs.lean#L63).

> Derived direct image commutes with the coherator. Let `f : X ⟶ Y` be a quasi-compact and
> quasi-separated morphism of schemes and suppose the inclusions `D_QCoh ⥤ D` admit right adjoints
> `DQ_X` and `DQ_Y` on `X` and on `Y`. Then
>
> `Rf_* ∘ DQ_X ≅ DQ_Y ∘ Rf_*`
>
> as functors `D(𝒪_X) ⥤ D_QCoh(𝒪_Y)`.
>
> This is `Stacks.Duality.coheratorDerivedPushforwardIso` with its preservation hypothesis
> discharged: for a quasi-compact and quasi-separated morphism `Rf_*` sends `D_QCoh(𝒪_X)` into
> `D_QCoh(𝒪_Y)`, which is part (1) of [Stacks, Tag 08D5] in the form
> `Stacks.Duality.isQuasicoherent_homology_derivedPushforward`.

```lean
def coheratorDerivedPushforwardIsoOfQcqs :
    DQX ⋙ quasiCoherentDerivedPushforward f (isQuasicoherent_homology_derivedPushforward f) ≅
      derivedPushforward f ⋙ DQY
```

## Tag 0CR2, a remark

[Tag 0CR2](https://stacks.math.columbia.edu/tag/0CR2) in the Stacks Project.

**`Stacks.Duality.Coherator.mayerVietorisTriangle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/MayerVietorisTriangle.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/MayerVietorisTriangle.lean#L186). The attribute's comment: “the canonical triangle, as data”.

> The canonical triangle
>
> `DQ_X(K) ⟶ Rj_{U,*}DQ_U(K|_U) ⊕ Rj_{V,*}DQ_V(K|_V) ⟶ Rj_{U ∩ V,*}DQ_{U ∩ V}(K|_{U ∩ V}) ⟶`
>
> attached to a scheme `X`, two opens `U`, `V` of `X`, coherators `DQ_X`, `DQ_U`, `DQ_V`,
> `DQ_{U ∩ V}` with `DQ_X` commuting with the shift, an object `K` of `D(𝒪_X)`, and the last two maps
> `mor₂`, `mor₃` of the Mayer--Vietoris triangle of [Stacks, Tag 08BV] for the cover `X = U ∪ V`.
>
> It is the image under `DQ_X` of that Mayer--Vietoris triangle, conjugated by
> `Stacks.Duality.Coherator.mayerVietorisMiddleIso` and
> `Stacks.Duality.Coherator.mayerVietorisThirdIso`: the first map is `DQ_X` of the canonical
> `biprod.lift` of the two units of `j_W^* ⊣ Rj_{W,*}` followed by the middle identification, the
> second is `DQ_X(mor₂)` read through both identifications, and the third is `DQ_X(mor₃)` read
> through the third identification and the commutation of `DQ_X` with the shift.

```lean
def mayerVietorisTriangle [DQX.CommShift ℤ]
    (mor₂ : restrictPushforward U K ⊞ restrictPushforward V K ⟶ restrictPushforward (U ⊓ V) K)
    (mor₃ : restrictPushforward (U ⊓ V) K ⟶ K⟦(1 : ℤ)⟧) :
    Triangle (quasiCoherentDerivedCategory X)
```

**`Stacks.Duality.Coherator.mayerVietorisTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/MayerVietorisTriangle.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/MayerVietorisTriangle.lean#L242). The attribute's comment: “the distinguished triangle of the tag, over arbitrary coherators”.

> Let `X` be a quasi-compact and quasi-separated scheme, let `X = U ∪ V` with `U` and `V`
> quasi-compact open, and let `DQ_X`, `DQ_U`, `DQ_V`, `DQ_{U ∩ V}` be coherators — right adjoints of
> the inclusions `D_QCoh ⥤ D`. Then for every object `K` of `D(𝒪_X)` there is a distinguished
> triangle
>
> `DQ_X(K) ⟶ Rj_{U,*}DQ_U(K|_U) ⊕ Rj_{V,*}DQ_V(K|_V) ⟶ Rj_{U ∩ V,*}DQ_{U ∩ V}(K|_{U ∩ V}) ⟶`
>
> in `D_QCoh(𝒪_X)`.

```lean
theorem mayerVietorisTriangle_distinguished (hUV : U ⊔ V = ⊤) :
    ∃ (f : DQX.obj K ⟶
          coheratorPushforwardOpens U DQU K ⊞ coheratorPushforwardOpens V DQV K)
      (g : coheratorPushforwardOpens U DQU K ⊞ coheratorPushforwardOpens V DQV K ⟶
          coheratorPushforwardOpens (U ⊓ V) DQUV K)
      (h : coheratorPushforwardOpens (U ⊓ V) DQUV K ⟶ (DQX.obj K)⟦(1 : ℤ)⟧),
      Triangle.mk f g h ∈ distTriang (quasiCoherentDerivedCategory X)
```

**`Stacks.Duality.Coherator.exists_distTriang_rightAdjoint_quasiCoherentι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/QcqsMayerVietorisTriangle.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/QcqsMayerVietorisTriangle.lean#L118). The attribute's comment: “the distinguished triangle at the coherators of `X`, `U`, `V` and `U ∩ V` supplied by Tag 0CR0”.

> **[Stacks, Tag 0CR2].** Let `X` be a quasi-compact and quasi-separated scheme covered by two
> quasi-compact opens, `X = U ∪ V`, and write `DQ_Z` for the coherator of `Z`, the right adjoint of
> the inclusion `D_QCoh(𝒪_Z) ⥤ D(𝒪_Z)` whose existence for `Z` quasi-compact and quasi-separated is
> [Stacks, Tag 0CR0] (`Stacks.Duality.Coherator.isLeftAdjoint_quasiCoherentι`). Then for every
> object `K` of `D(𝒪_X)` there is a distinguished triangle
>
> `DQ_X(K) ⟶ Rj_{U,*}DQ_U(K|_U) ⊕ Rj_{V,*}DQ_V(K|_V) ⟶ Rj_{U ∩ V,*}DQ_{U ∩ V}(K|_{U ∩ V}) ⟶`
>
> in `D_QCoh(𝒪_X)`.
>
> The four coherators are the ones [Stacks, Tag 0CR0] produces at `X`, `U`, `V` and `U ∩ V`: the
> three opens are quasi-compact — `U ∩ V` because `X` is quasi-separated — and quasi-separated,
> being opens of a quasi-separated scheme. The triangle is then
> `Stacks.Duality.Coherator.mayerVietorisTriangle_distinguished` at those coherators.

```lean
theorem exists_distTriang_rightAdjoint_quasiCoherentι (hUV : U ⊔ V = ⊤)
    (K : DerivedCategory X.Modules) :
    letI := isLeftAdjoint_quasiCoherentι X
    letI := isLeftAdjoint_quasiCoherentι U.toScheme
    letI := isLeftAdjoint_quasiCoherentι V.toScheme
    letI := isLeftAdjoint_quasiCoherentι (U ⊓ V).toScheme
    ∃ (f : (quasiCoherentι X).rightAdjoint.obj K ⟶
          coheratorPushforwardOpens U (quasiCoherentι U.toScheme).rightAdjoint K ⊞
            coheratorPushforwardOpens V (quasiCoherentι V.toScheme).rightAdjoint K)
      (g : coheratorPushforwardOpens U (quasiCoherentι U.toScheme).rightAdjoint K ⊞
            coheratorPushforwardOpens V (quasiCoherentι V.toScheme).rightAdjoint K ⟶
          coheratorPushforwardOpens (U ⊓ V) (quasiCoherentι (U ⊓ V).toScheme).rightAdjoint K)
      (h : coheratorPushforwardOpens (U ⊓ V) (quasiCoherentι (U ⊓ V).toScheme).rightAdjoint K ⟶
          ((quasiCoherentι X).rightAdjoint.obj K)⟦(1 : ℤ)⟧),
      Triangle.mk f g h ∈ distTriang (quasiCoherentDerivedCategory X)
```

**`Stacks.Duality.Coherator.exists_coherator_distTriang`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/QcqsMayerVietorisTriangle.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/QcqsMayerVietorisTriangle.lean#L156). The attribute's comment: “coherators of the four schemes exist and the triangle of the tag is distinguished for them”.

> **[Stacks, Tag 0CR2], in existential form.** For a quasi-compact quasi-separated scheme `X`
> covered by two quasi-compact opens, `X = U ∪ V`, there are coherators `DQ_X`, `DQ_U`, `DQ_V`,
> `DQ_{U ∩ V}` of `X`, `U`, `V` and `U ∩ V` — right adjoints of the inclusions
> `D_QCoh(𝒪_Z) ⥤ D(𝒪_Z)`, [Stacks, Tag 0CR0] — such that every object `K` of `D(𝒪_X)` sits in a
> distinguished triangle
>
> `DQ_X(K) ⟶ Rj_{U,*}DQ_U(K|_U) ⊕ Rj_{V,*}DQ_V(K|_V) ⟶ Rj_{U ∩ V,*}DQ_{U ∩ V}(K|_{U ∩ V}) ⟶`
>
> in `D_QCoh(𝒪_X)`. A coherator is unique up to a canonical isomorphism, so this is the same
> assertion as `Stacks.Duality.Coherator.exists_distTriang_rightAdjoint_quasiCoherentι`, read
> without naming the right adjoints.

```lean
theorem exists_coherator_distTriang (hUV : U ⊔ V = ⊤) :
    ∃ (DQX : DerivedCategory X.Modules ⥤ quasiCoherentDerivedCategory X)
      (DQU : DerivedCategory U.toScheme.Modules ⥤ quasiCoherentDerivedCategory U.toScheme)
      (DQV : DerivedCategory V.toScheme.Modules ⥤ quasiCoherentDerivedCategory V.toScheme)
      (DQUV : DerivedCategory (U ⊓ V).toScheme.Modules ⥤
        quasiCoherentDerivedCategory (U ⊓ V).toScheme)
      (_ : quasiCoherentι X ⊣ DQX) (_ : quasiCoherentι U.toScheme ⊣ DQU)
      (_ : quasiCoherentι V.toScheme ⊣ DQV) (_ : quasiCoherentι (U ⊓ V).toScheme ⊣ DQUV),
      ∀ K : DerivedCategory X.Modules,
        ∃ (f : DQX.obj K ⟶
              coheratorPushforwardOpens U DQU K ⊞ coheratorPushforwardOpens V DQV K)
          (g : coheratorPushforwardOpens U DQU K ⊞ coheratorPushforwardOpens V DQV K ⟶
              coheratorPushforwardOpens (U ⊓ V) DQUV K)
          (h : coheratorPushforwardOpens (U ⊓ V) DQUV K ⟶ (DQX.obj K)⟦(1 : ℤ)⟧),
          Triangle.mk f g h ∈ distTriang (quasiCoherentDerivedCategory X)
```

## Tag 0CSA, a lemma

[Tag 0CSA](https://stacks.math.columbia.edu/tag/0CSA) in the Stacks Project.

**`Stacks.Duality.Coherator.exists_isGE_isLE_coherator_obj_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/UnconditionalBoundedness.lean, line 401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/UnconditionalBoundedness.lean#L401).

> **[Stacks, Tag 0CSA].** Let `X` be a quasi-compact and quasi-separated scheme and let
> `DQ_X : D(𝒪_X) ⥤ D_QCoh(𝒪_X)` be a coherator of `X`, i.e. a right adjoint of the inclusion
> `ι : D_QCoh(𝒪_X) ⥤ D(𝒪_X)` with the adjunction triangulated — the exact functor `DQ_X` of
> [Stacks, Tag 0CR0]. Then there is an integer `N`, depending only on `X` and on `DQ_X` and in
> particular not on `K`, `a` or `b`, such that for every object `K` of `D(𝒪_X)` and all integers
> `a`, `b`, if `H^i(U, K) = 0` for every affine open `U ⊆ X` and every `i ∉ [a, b]`, then the
> cohomology sheaves `H^i(DQ_X(K))` vanish for `i ∉ [a, b + N]`.
>
> This is `Stacks.Duality.Coherator.exists_isGE_isLE_coherator_obj`, the source's induction over the
> quasi-compact opens of `X` ([Stacks, Tag 08DR]), with its three inputs supplied: the two
> Mayer–Vietoris triangles of [Stacks, Tag 08BV] are
> `Stacks.Duality.Coherator.isMayerVietorisApex_restrictPushforward_sup` and
> `Stacks.Duality.Coherator.isMayerVietorisApex_self`, and the affine base case is
> `Stacks.Duality.Coherator.hasCoheratorBoundAt_of_isAffineOpen`.

```lean
theorem exists_isGE_isLE_coherator_obj_of_qcqs (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X]
    (DQ : DerivedCategory X.Modules ⥤ quasiCoherentDerivedCategory X)
    (adj : quasiCoherentι X ⊣ DQ) [DQ.CommShift ℤ] [adj.IsTriangulated] :
    ∃ N : ℤ, ∀ (a b : ℤ) (K : DerivedCategory X.Modules), AffineAmplitudeIn X a b K →
      ((quasiCoherentι X).obj (DQ.obj K)).IsGE a ∧
        ((quasiCoherentι X).obj (DQ.obj K)).IsLE (b + N)
```

## Tag 0CSB, an example

[Tag 0CSB](https://stacks.math.columbia.edu/tag/0CSB) in the Stacks Project.

**`AlgebraicGeometry.isZero_cohomology_of_isDerivedLimit_single_of_isAffineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/Coherator/InverseLimitAffineCohomology.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/Coherator/InverseLimitAffineCohomology.lean#L110). The attribute's comment: “the cohomology computation on an affine open: H^i(U, R lim 𝓕ₙ) = 0 for i outside [0, 1]”.

> **[Stacks, Tag 0CSB].** Let `X` be a scheme, let `(𝓕ₙ)` be an inverse system of
> quasi-coherent `𝒪_X`-modules and let `L` be a derived limit in `D(𝒪_X)` of the system `(𝓕ₙ)`
> placed in degree zero. Then `H^i(U, L) = 0` for every affine open `U ⊆ X` and every `i` outside
> `[0, 1]`.
>
> Sections over `U` commute with derived limits, so `RΓ(U, L) = R lim RΓ(U, 𝓕ₙ)`, and each
> `RΓ(U, 𝓕ₙ)` is concentrated in degree zero because `𝓕ₙ` is quasi-coherent and `U` is affine. In
> the Milnor short exact sequence `0 → lim¹ H^{i-1}(U, 𝓕ₙ) → H^i(U, L) → lim H^i(U, 𝓕ₙ) → 0` both
> outer terms then vanish as soon as `i ≠ 0` and `i ≠ 1`.

```lean
theorem isZero_cohomology_of_isDerivedLimit_single_of_isAffineOpen (X : Scheme.{u})
    (𝓕 : ℕᵒᵖ ⥤ X.Modules) (hqc : ∀ n : ℕ, (𝓕.obj ⟨n⟩).IsQuasicoherent)
    [HasProduct fun n : ℕ ↦ (𝓕 ⋙ DerivedCategory.singleFunctor X.Modules 0).obj ⟨n⟩]
    (L : DerivedCategory.{u + 1} X.Modules)
    (hL : IsDerivedLimit (𝓕 ⋙ DerivedCategory.singleFunctor X.Modules 0) L)
    (U : X.Opens) (hU : IsAffineOpen U) (i : ℤ) (hi0 : i ≠ 0) (hi1 : i ≠ 1) :
    IsZero ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} i).obj
      ((derivedSectionsOverObject (schemeOpensRingedSite X) U).obj L))
```

**`Stacks.Duality.Coherator.exists_isGE_isLE_coherator_obj_of_isDerivedLimit_single`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/Coherator/InverseLimitBounded.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/Coherator/InverseLimitBounded.lean#L185). The attribute's comment: “the conclusion that the R lim in D_QCoh(𝒪_X), i.e. DQ_X(R lim 𝓕ₙ), lies in D^b_QCoh(𝒪_X), for every coherator DQ of X”.

> **[Stacks, Tag 0CSB].** Let `X` be a quasi-compact and quasi-separated scheme, let `DQ` be a
> coherator of `X` and let `L` be a derived limit in `D(𝒪_X)` of an inverse system `(𝓕ₙ)` of
> quasi-coherent `𝒪_X`-modules placed in degree zero. Then `DQ L` lies in `D^b_QCoh(𝒪_X)`: its
> cohomology sheaves vanish below degree `0` and above degree `1 + N` for some `N` depending only
> on `X` and `DQ`.
>
> The affine amplitude of `L` is `[0, 1]`, so this is the boundedness property of the coherator,
> [Stacks, Tag 0CSA] in the form
> `Stacks.Duality.Coherator.exists_isGE_isLE_coherator_obj_of_qcqs`, applied with `a = 0` and
> `b = 1`.

```lean
theorem exists_isGE_isLE_coherator_obj_of_isDerivedLimit_single (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X]
    (DQ : DerivedCategory X.Modules ⥤ quasiCoherentDerivedCategory X)
    (adj : quasiCoherentι X ⊣ DQ) [DQ.CommShift ℤ] [adj.IsTriangulated]
    (𝓕 : ℕᵒᵖ ⥤ X.Modules) (hqc : ∀ n : ℕ, (𝓕.obj ⟨n⟩).IsQuasicoherent)
    [HasProduct fun n : ℕ ↦ (𝓕 ⋙ DerivedCategory.singleFunctor X.Modules 0).obj ⟨n⟩]
    (L : DerivedCategory X.Modules)
    (hL : IsDerivedLimit (𝓕 ⋙ DerivedCategory.singleFunctor X.Modules 0) L) :
    ∃ N : ℤ, ((quasiCoherentι X).obj (DQ.obj L)).IsGE 0 ∧
      ((quasiCoherentι X).obj (DQ.obj L)).IsLE (1 + N)
```

**`Stacks.Duality.Coherator.isDerivedLimit_coherator_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/Coherator/InverseLimitQuasiCoherent.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/Coherator/InverseLimitQuasiCoherent.lean#L147). The attribute's comment: “the identification DQ_X(R lim 𝓕ₙ) = (R lim in D_QCoh(𝒪_X))(𝓕ₙ), for every coherator DQ of X, i.e. every exact right adjoint of the inclusion; one exists on any quasi-compact quasi-separated scheme by Stacks 0CR0, `Stacks.Duality.Coherator.exists_isTriangulated_rightAdjoint_quasiCoherentι`”.

> **[Stacks, Tag 0CSB].** Let `X` be a scheme and let `DQ` be a right adjoint of the inclusion
> `D_QCoh(𝒪_X) ⥤ D(𝒪_X)` which makes the adjunction triangulated. If `L` is a derived limit in
> `D(𝒪_X)` of an inverse system `F` of objects of `D_QCoh(𝒪_X)`, then `DQ L` is a derived limit of
> `F` in `D_QCoh(𝒪_X)`.
>
> Right adjoints preserve products, so `DQ` preserves the product of the system; it is exact, so it
> carries the triangle witnessing the derived limit to one of the same shape. The inclusion is fully
> faithful, so the unit of the adjunction identifies `F ⋙ ι ⋙ DQ` with `F`.

```lean
theorem isDerivedLimit_coherator_obj
    (DQ : DerivedCategory (SheafOfModules.{u} X.ringCatSheaf) ⥤
      (derivedQuasiCoherent X).FullSubcategory)
    (adj : (derivedQuasiCoherent X).ι ⊣ DQ) [DQ.CommShift ℤ] [adj.IsTriangulated]
    (F : ℕᵒᵖ ⥤ (derivedQuasiCoherent X).FullSubcategory)
    [HasProduct fun n : ℕ ↦ (F ⋙ (derivedQuasiCoherent X).ι).obj (op n)]
    (L : DerivedCategory (SheafOfModules.{u} X.ringCatSheaf))
    (hL : IsDerivedLimit (F ⋙ (derivedQuasiCoherent X).ι) L) :
    ∃ h : HasProduct fun n : ℕ ↦ F.obj (op n),
      letI := h
      IsDerivedLimit F (DQ.obj L)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.21, Tag 0CQZ](https://stacks.math.columbia.edu/tag/0CQZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
