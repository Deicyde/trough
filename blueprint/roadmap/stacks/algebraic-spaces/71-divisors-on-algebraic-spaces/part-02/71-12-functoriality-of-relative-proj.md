---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.RelativeProjHomPoints.relativeMapSubfunctor, AlgebraicGeometry.Space.RelativeProjHomPoints.mem_relativeMapSubfunctor_iff, AlgebraicGeometry.Space.RelativeProjHomPoints.relativeMapSpaceHom, AlgebraicGeometry.Space.RelativeProjHomPoints.relativeMapSpaceHom_comp, AlgebraicGeometry.Space.RelativeProjHomPoints.app_relativeMapSpaceHom, AlgebraicGeometry.Space.RelativeProjHomPoints.relativeMapSubfunctor_unique, AlgebraicGeometry.Space.RelativeProjHomPoints.relativeMapSpaceHom_unique, AlgebraicGeometry.Space.RelativeProjHomPoints.isOpenSubspace_relativeMapSubfunctor
statement: formalized
proof: formalized
---

# 71.12 Functoriality of relative proj

Section 71.12 of the Stacks Project, [Tag 085E](https://stacks.math.columbia.edu/tag/085E). 5 tags here are carried by 36 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 085F, a lemma

[Tag 085F](https://stacks.math.columbia.edu/tag/085F) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeProjHomPoints.relativeMapSubfunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean, line 578](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean#L578). The attribute's comment: “the open subspace U(ψ) of Q”.

> **Tag 085F, the open subspace `U(ψ) ⊆ Q`.** The subfunctor of `Q = Proj_X(ℬ)` whose
> `T`-points are the points lying in the domain of definition of `ψ`: those whose section of the
> scheme-level relative Proj of `ℬ|_T` factors through the open `U(ψ|_T)` of Tag 07ZG.

```lean
def relativeMapSubfunctor : Subfunctor Q
```

**`AlgebraicGeometry.Space.RelativeProjHomPoints.mem_relativeMapSubfunctor_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean, line 598](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean#L598). The attribute's comment: “the étale-local description of the open subspace U(ψ)”.

> **Tag 085F's étale-local description of the open subspace.** A point of `Q` lying over a
> point `f` of the base at `T`, along any `r : T' ⟶ T`, belongs to `U(ψ)` exactly when its section
> of the scheme-level relative Proj of `ℬ|_T` factors through the open `U(ψ|_T)` of Tag 07ZG.
>
> Read at an étale chart `W` of `X` and `r = 𝟙`, this is the assertion `U(ψ) ×_X W = U(ψ|_W)` of
> the source.

```lean
theorem mem_relativeMapSubfunctor_iff (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X)
    {T' : BigFppfOver B S hS} (r : T' ⟶ T) (u : yoneda.obj T' ⟶ Q)
    (hu : u ≫ πQ = yoneda.map r ≫ f) :
    yonedaEquiv u ∈ hψ.relativeMapSubfunctor.obj (op T') ↔
      dQ.sectionOfPoint T f r u hu ⁻¹ᵁ (hψ.hom T f).relativeMapDomain = ⊤
```

**`AlgebraicGeometry.Space.RelativeProjHomPoints.relativeMapSpaceHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean, line 617](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean#L617). The attribute's comment: “the morphism r\_ψ : U(ψ) ⟶ P”.

> **Tag 085F, the morphism `r_ψ : U(ψ) ⟶ P` of algebraic spaces.** On a `T`-point of `U(ψ)`
> it is the point of `P = Proj_X(𝒜)` whose section of the scheme-level relative Proj of `𝒜|_T` is
> obtained from the section of `ℬ|_T` by the morphism `r_{ψ|_T}` of Tag 07ZG.

```lean
def relativeMapSpaceHom : hψ.relativeMapSubfunctor.toFunctor ⟶ P
```

**`AlgebraicGeometry.Space.RelativeProjHomPoints.relativeMapSpaceHom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean, line 629](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean#L629). The attribute's comment: “the morphism r\_ψ is a morphism over X”.

> **Tag 085F: the morphism `r_ψ` is a morphism over `X`.**

```lean
theorem relativeMapSpaceHom_comp :
    hψ.relativeMapSpaceHom ≫ πP = hψ.relativeMapSubfunctor.ι ≫ πQ
```

**`AlgebraicGeometry.Space.RelativeProjHomPoints.app_relativeMapSpaceHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean, line 648](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean#L648). The attribute's comment: “the étale-local description of the morphism r\_ψ”.

> **Tag 085F's étale-local description of the morphism `r_ψ`.** On a point of `U(ψ)` lying
> over a point `f` of the base at `T`, along any `r : T' ⟶ T`, the morphism `r_ψ` produces the
> point of `P` whose section of the scheme-level relative Proj of `𝒜|_T` is the one the morphism
> `r_{ψ|_T}` of Tag 07ZG produces; that last identification is
> `AlgebraicGeometry.Space.sectionOfPoint_pointHomOn`.
>
> Read at an étale chart `W` of `X` and `r = 𝟙`, this is the assertion that `r_ψ` restricted to
> `U(ψ) ×_X W` is the morphism `r_{ψ|_W}` of the source.

```lean
theorem app_relativeMapSpaceHom (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X)
    {T' : BigFppfOver B S hS} (r : T' ⟶ T) (u : yoneda.obj T' ⟶ Q)
    (hu : u ≫ πQ = yoneda.map r ≫ f) (hd : IsDefinedOn dP dQ hψ.hom T f r u hu)
    (hx : yonedaEquiv u ∈ hψ.relativeMapSubfunctor.obj (op T')) :
    hψ.relativeMapSpaceHom.app (op T') ⟨yonedaEquiv u, hx⟩ =
      yonedaEquiv (pointHomOn dP dQ hψ.hom T f r u hu hd)
```

**`AlgebraicGeometry.Space.RelativeProjHomPoints.relativeMapSubfunctor_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean, line 661](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean#L661). The attribute's comment: “the étale-local description determines U(ψ)”.

> **Tag 085F's description determines the open subspace.** A subfunctor of `Q` whose points
> are exactly the points in the domain of definition of `ψ` is `U(ψ)`.

```lean
theorem relativeMapSubfunctor_unique (G : Subfunctor Q)
    (hG : ∀ (T : BigFppfOver B S hS) (u : yoneda.obj T ⟶ Q),
      yonedaEquiv u ∈ G.obj (op T) ↔ IsDefined dP dQ hψ.hom T u) :
    G = hψ.relativeMapSubfunctor
```

**`AlgebraicGeometry.Space.RelativeProjHomPoints.relativeMapSpaceHom_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean, line 675](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean#L675). The attribute's comment: “the étale-local description determines r\_ψ”.

> **Tag 085F's description determines the morphism.** A morphism out of `U(ψ)` whose value at
> every point is the point of `P` the scheme-level morphism `r_{ψ|_T}` of Tag 07ZG produces is
> `r_ψ`.

```lean
theorem relativeMapSpaceHom_unique (k : hψ.relativeMapSubfunctor.toFunctor ⟶ P)
    (hk : ∀ (Y : (BigFppfOver B S hS)ᵒᵖ) (y : Q.obj Y)
      (hy : y ∈ hψ.relativeMapSubfunctor.obj Y),
      k.app Y ⟨y, hy⟩ = yonedaEquiv (pointHomAt dP dQ hψ.hom Y.unop (yonedaEquiv.symm y)
        ((hψ.mem_relativeMapSubfunctor_obj y).1 hy))) :
    k = hψ.relativeMapSpaceHom
```

**`AlgebraicGeometry.Space.RelativeProjHomPoints.isOpenSubspace_relativeMapSubfunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean, line 802](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean#L802). The attribute's comment: “U(ψ) is an open subspace of Q”.

> **Tag 085F: `U(ψ)` is an open subspace of `Q = Proj_X(ℬ)`.**

```lean
theorem isOpenSubspace_relativeMapSubfunctor (hQ : IsAlgebraicSpace B S hS Q) :
    IsOpenSubspace B S hS hψ.relativeMapSubfunctor
```

**`AlgebraicGeometry.Space.RelativeProjHomPoints.relativeTwistSpaceMap`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean, line 862](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean#L862). The attribute's comment: “the third component: the map θ on the n-th twists, over a scheme point of the base — the scheme-level θ of Tag 07ZG for the restricted map, which is what the tag's étale-local characterization of θ asks for”.

> **Tag 085F, the third component: the map `θ` on the twists, over a scheme point of the
> base.**  For every `n : ℤ`,
>
> `θ_n : r_ψ^*𝒪_P(n) ⟶ 𝒪_Q(n)|_{U(ψ)}`,
>
> read over the scheme point `(T, f)` of `X` as the map Tag 07ZG attaches to the restriction
> `ψ|_{T,f}` — a *single* morphism of sheaves of modules on the whole of `U(ψ|_{T,f})`, namely
> `Stacks.AlgebraicGeometry.Tag07ZGTwist.relativeTwistMap`.
>
> This is `θ` itself, not a chart-by-chart approximation of it: Tag 085F *characterizes* `θ` by the
> property that its restriction to `U(ψ) ×_X W` is the scheme-level `θ` of `ψ|_W` for every scheme
> `W` étale over `X`, and that restriction is exactly what this is.  The characterization is
> `AlgebraicGeometry.Space.RelativeProjHomPoints.relativeTwistSpaceMap_chart` and
> `…relativeTwistSpaceMap_unique`.

```lean
abbrev relativeTwistSpaceMap (hψ : RelativeProjHomPoints dP dQ)
    (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X) (n : ℤ) :
    (Scheme.Modules.pullback (relativeMapHom (hψ.hom T f))).obj (dP.pointTwist T f n) ⟶
      (Scheme.Modules.pullback (hψ.hom T f).relativeMapDomain.ι).obj (dQ.pointTwist T f n)
```

**`AlgebraicGeometry.Space.RelativeProjHomPoints.relativeTwistAlgebraSpaceHom`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean, line 878](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean#L878). The attribute's comment: “the third component as a map of ℤ-graded algebras, over a scheme point of the base”.

> **Tag 085F, the third component as a map of `ℤ`-graded algebras.**  The source asks for `θ`
> as a homomorphism
>
> `θ : r_ψ^*(⨁_{d ∈ ℤ} 𝒪_P(d)) ⟶ ⨁_{d ∈ ℤ} 𝒪_{U(ψ)}(d)`
>
> of sheaves of `ℤ`-graded algebras, not only for the degreewise family; over a scheme point of the
> base that is `Stacks.AlgebraicGeometry.Tag07ZGTwist.relativeTwistAlgebraHom`, whose degree-`n`
> component is `AlgebraicGeometry.Space.RelativeProjHomPoints.relativeTwistSpaceMap`.

```lean
abbrev relativeTwistAlgebraSpaceHom (hψ : RelativeProjHomPoints dP dQ)
    (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X)
```

**`AlgebraicGeometry.Space.RelativeProjHomPoints.relativeTwistSpaceMap_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean, line 899](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean#L899). The attribute's comment: “the étale-local description of θ, read on the affine charts of a scheme point of the base”.

> **Tag 085F's étale-local description of `θ`.**  Over the piece of `U(ψ|_{T,f})` lying over an
> affine open `U` of the scheme point `T` of the base, `θ_n` is Tag 01MY's comparison map for the
> induced homomorphism `Γ(U, 𝒜|_T) ⟶ Γ(U, ℬ|_T)` of graded rings of sections, conjugated by the
> chart identifications of Tag 01NR.
>
> This is the affine-local reading of the étale-local description; the étale-local description
> itself — that `θ` restricted to `U(ψ) ×_X W` is the scheme-level `θ` of `ψ|_W` — holds by
> construction, `AlgebraicGeometry.Space.RelativeProjHomPoints.relativeTwistSpaceMap` being that
> restriction.

```lean
theorem relativeTwistSpaceMap_chart (hψ : RelativeProjHomPoints dP dQ)
    (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X) (n : ℤ)
    (U : ((BigFppfOver.toScheme B S hS).obj T).affineOpens) :
    (Scheme.Modules.pullback (pieceIncl (hψ.hom T f) U)).map (hψ.relativeTwistSpaceMap T f n) =
      relativeTwistChart (hψ.hom T f) n U
```

**`AlgebraicGeometry.Space.RelativeProjHomPoints.relativeTwistSpaceMap_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean, line 910](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean#L910). The attribute's comment: “the étale-local description determines θ”.

> **Tag 085F's description determines `θ`.**  A map on the `n`-th twists whose restriction to
> the piece over every affine open of the scheme point of the base is Tag 01MY's comparison map
> there is `θ_n`.

```lean
theorem relativeTwistSpaceMap_unique (hψ : RelativeProjHomPoints dP dQ)
    (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X) (n : ℤ)
    {θ : (Scheme.Modules.pullback (relativeMapHom (hψ.hom T f))).obj (dP.pointTwist T f n) ⟶
      (Scheme.Modules.pullback (hψ.hom T f).relativeMapDomain.ι).obj (dQ.pointTwist T f n)}
    (hθ : ∀ U : ((BigFppfOver.toScheme B S hS).obj T).affineOpens,
      (Scheme.Modules.pullback (pieceIncl (hψ.hom T f) U)).map θ =
        relativeTwistChart (hψ.hom T f) n U) :
    θ = hψ.relativeTwistSpaceMap T f n
```

**`AlgebraicGeometry.Space.RelativeProjSituation.relativeMapTriple_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorialityTriple.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorialityTriple.lean#L66). The attribute's comment: “the triple (U(ψ), r\_ψ, θ) with θ a map of graded algebras, its description by the triple of Tag 07ZG over the scheme points of X, and its uniqueness”.

> **Stacks 085F.** Let `ψ : 𝒜 ⟶ ℬ` be a map of quasi-coherent graded `𝒪_X`-algebras on an
> algebraic space `X`, `P = Proj_X(𝒜)`, `Q = Proj_X(ℬ)`, and `X = U/R` a presentation. Then:
> 1. `U(ψ) ⊆ Q` is an open subspace, and `r_ψ : U(ψ) ⟶ P` is a morphism over `X`;
> 2. `θ : r_ψ^*(⨁_d 𝒪_P(d)) ⟶ ι^*(⨁_d 𝒪_Q(d))` is a map of `ℤ`-graded `𝒪_{U(ψ)}`-algebras
>    whose degree-`d` component is the glued map `θ_d`, which is, on `U(ψ) ×_X U`, the component
>    `θ_d` of Tag 07ZG for `ψ|_U`;
> 3. over every scheme point `f : T ⟶ X`, `U(ψ) ×_X T` is `U(ψ|_T)` of Tag 07ZG and `r_ψ` there
>    is `r_{ψ|_T}`;
> 4. these properties determine `U(ψ)`, `r_ψ`, the `θ_d` and `θ`.

```lean
theorem relativeMapTriple_spec :
    IsOpenSubspace B S hS (𝔥).relativeMapSubfunctor ∧
    (relativeMapSpaceMor h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k ψ).hom ≫ (𝔰₁).relativeProjπ =
      (relativeMapSpaceι h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k ψ).hom ≫ (𝔰₂).relativeProjπ ∧
    (∀ n : ℤ, type_of% (twistAlgebraHomOfMul_app h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k ψ Px
      (twistMap_mul h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k ψ Px) n)) ∧
    (∀ n : ℤ, type_of% (isDescendedChartHom_twistMap h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k ψ Px n)) ∧
    (∀ (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X.1) {T' : BigFppfOver B S hS}
      (r : T' ⟶ T) (v : yoneda.obj T' ⟶ (𝔰₂).relativeProjFunctor)
      (hv : v ≫ (𝔰₂).relativeProjπ = yoneda.map r ≫ f),
      type_of% ((𝔥).mem_relativeMapSubfunctor_iff T f r v hv)) ∧
    (∀ (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X.1) {T' : BigFppfOver B S hS}
      (r : T' ⟶ T) (v : yoneda.obj T' ⟶ (𝔰₂).relativeProjFunctor)
      (hv : v ≫ (𝔰₂).relativeProjπ = yoneda.map r ≫ f)
      (hd : IsDefinedOn (𝔰₁).relativeProjPoints (𝔰₂).relativeProjPoints (𝔥).hom T f r v hv)
      (hx : yonedaEquiv v ∈ (𝔥).relativeMapSubfunctor.obj (op T')),
      type_of% ((𝔥).app_relativeMapSpaceHom T f r v hv hd hx)) ∧
    (∀ G : Subfunctor (𝔰₂).relativeProjFunctor,
      type_of% ((𝔥).relativeMapSubfunctor_unique G)) ∧
    (∀ k : (𝔥).relativeMapSubfunctor.toFunctor ⟶ (𝔰₁).relativeProjFunctor,
      type_of% ((𝔥).relativeMapSpaceHom_unique k)) ∧
    (∀ (n : ℤ) (χ : type_of% (twistMap h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k ψ Px n)),
      type_of% (eq_twistMap h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k ψ Px n (χ := χ))) ∧
    (∀ θ' : SheafOfModules.GradedAlgebra.Hom
        ((gradedPull (X := smallEtaleRingedTopos B S hS 𝒢)
          (Y := smallEtaleRingedTopos B S hS (projSpace₁ h₁c h₁n h₁q h₁k))
          (smallEtaleRingedToposHom B S hS
            (relativeMapSpaceMor h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k ψ))).obj
          ((𝔰₁).twistGradedAlgebra Px))
        ((gradedPull (X := smallEtaleRingedTopos B S hS 𝒢)
          (Y := smallEtaleRingedTopos B S hS (projSpace₂ h₂c h₂n h₂q h₂k))
          (smallEtaleRingedToposHom B S hS
            (relativeMapSpaceι h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k ψ))).obj
          ((𝔰₂).twistGradedAlgebra Px)),
      type_of% (eq_twistAlgebraHomOfMul h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k ψ Px
        (twistMap_mul h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k ψ Px) θ'))
```

## Tag 085G, a lemma

[Tag 085G](https://stacks.math.columbia.edu/tag/085G) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeProjHomPoints.comp_relativeMapSubfunctor_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean, line 1161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean#L1161). The attribute's comment: “the domain U(ψ ∘ φ) lies in U(ψ)”.

> **Tag 085G, the first assertion: `U(ψ ∘ φ) ⊆ U(ψ)`.**

```lean
theorem comp_relativeMapSubfunctor_le :
    (hφ.comp hψ).relativeMapSubfunctor ≤ hψ.relativeMapSubfunctor
```

**`AlgebraicGeometry.Space.RelativeProjHomPoints.mem_comp_relativeMapSubfunctor_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean, line 1176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean#L1176). The attribute's comment: “U(ψ ∘ φ) is the inverse image of U(φ) under r\_ψ”.

> **Tag 085G, the first assertion: `U(ψ ∘ φ) = r_ψ^{-1}(U(φ))`.** A point of
> `R = Proj_X(𝒞)` lying in `U(ψ)` lies in `U(ψ ∘ φ)` exactly when its image under
> `r_ψ : U(ψ) ⟶ Q` lies in `U(φ)`.
>
> Together with `AlgebraicGeometry.Space.RelativeProjHomPoints.comp_relativeMapSubfunctor_le`
> this is the equality `U(ψ ∘ φ) = r_ψ^{-1}(U(φ))` of the source.  (The source writes the
> right-hand side of that equality as `r_φ^{-1}(U(ψ))`, which does not typecheck: `r_φ` is defined
> on an open of `Q` and takes values in `P`, while `U(ψ)` is an open of `R`.  The reading above is
> the one the scheme-level analogue Tag 07ZH states, and it is the one the second assertion — which
> the source states identically in both tags — requires.)

```lean
theorem mem_comp_relativeMapSubfunctor_iff (Y : (BigFppfOver B S hS)ᵒᵖ) (y : R.obj Y)
    (hy : y ∈ hψ.relativeMapSubfunctor.obj Y) :
    y ∈ (hφ.comp hψ).relativeMapSubfunctor.obj Y ↔
      hψ.relativeMapSpaceHom.app Y ⟨y, hy⟩ ∈ hφ.relativeMapSubfunctor.obj Y
```

**`AlgebraicGeometry.Space.RelativeProjHomPoints.app_comp_relativeMapSpaceHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean, line 1187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctoriality.lean#L1187). The attribute's comment: “the morphism r\_\{ψ ∘ φ} is r\_φ after r\_ψ”.

> **Tag 085G, the second assertion: `r_{ψ ∘ φ} = r_φ ∘ r_ψ|_{U(ψ ∘ φ)}`.**

```lean
theorem app_comp_relativeMapSpaceHom (Y : (BigFppfOver B S hS)ᵒᵖ) (y : R.obj Y)
    (hy : y ∈ hψ.relativeMapSubfunctor.obj Y)
    (hc : y ∈ (hφ.comp hψ).relativeMapSubfunctor.obj Y)
    (hc2 : hψ.relativeMapSpaceHom.app Y ⟨y, hy⟩ ∈ hφ.relativeMapSubfunctor.obj Y) :
    (hφ.comp hψ).relativeMapSpaceHom.app Y ⟨y, hc⟩ =
      hφ.relativeMapSpaceHom.app Y ⟨hψ.relativeMapSpaceHom.app Y ⟨y, hy⟩, hc2⟩
```

**`AlgebraicGeometry.Space.RelativeProjHomPoints.relativeTwistSpaceMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctorialityComp.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctorialityComp.lean#L150). The attribute's comment: “(3): θ\_ψ ∘ r\_ψ^*θ\_φ = θ\_\{ψ ∘ φ}, in every degree n and over every scheme point (T, f) of X, where Tag 085F's θ is given: the inverse image of θ\_φ along the restriction r\_ψ|\_\{U(ψ ∘ φ)} : U(ψ ∘ φ) ⟶ U(φ), followed by the restriction of θ\_ψ to U(ψ ∘ φ), is θ\_\{ψ ∘ φ}, up to the canonical inverse-image isomorphisms”.

> **Tag 085G, the third assertion: `θ_ψ ∘ r_ψ^*θ_φ = θ_{ψ ∘ φ}`**, over a scheme point
> `(T, f)` of the base and in degree `n`.  The `n`-th map on twists of the composite is the inverse
> image along the restriction of `r_ψ` to `U(ψ ∘ φ)` of the `n`-th map on twists of `φ`, followed
> by the inverse image along the inclusion of `U(ψ ∘ φ)` into `U(ψ)` of the `n`-th map on twists of
> `ψ`; the remaining factors are the inverse-image isomorphisms that identify the sources and
> targets, named by the first two assertions at that point.
>
> The source's "obvious notation" `r_ψ^*θ_φ` is the inverse image of
> `θ_φ : r_φ^*𝒪_P(n) ⟶ 𝒪_{U(φ)}(n)` along `r_ψ|_{U(ψ ∘ φ)} : U(ψ ∘ φ) ⟶ U(φ)`, a map
> `r_ψ^*r_φ^*𝒪_P(n) ⟶ r_ψ^*𝒪_Q(n)` over `U(ψ ∘ φ)`; it is composed with `θ_ψ` restricted to
> `U(ψ ∘ φ)`, and `r_ψ^*r_φ^* = r_{ψ ∘ φ}^*` by the second assertion.  Tag 085F's `θ` is, in this
> library, `AlgebraicGeometry.Space.RelativeProjHomPoints.relativeTwistSpaceMap`, its restriction
> over every scheme point `(T, f)` of `X`, so this is the assertion over every such point.  The
> source's `θ` is a map of `ℤ`-graded algebras, and such a map is determined by its components, so
> the degreewise identity is the identity of graded maps.

```lean
theorem relativeTwistSpaceMap_comp (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X) (n : ℤ) :
    (Scheme.Modules.pullbackCongr
          (relativeMapHomRestrict_comp_relativeMapHom (hφ.hom T f) (hψ.hom T f))).inv.app
        (relativeTwist (dP.algebra T f) n) ≫
      (Scheme.Modules.pullbackComp (relativeMapHomRestrict (hφ.hom T f) (hψ.hom T f))
          (relativeMapHom (hφ.hom T f))).inv.app (relativeTwist (dP.algebra T f) n) ≫
      (Scheme.Modules.pullback (relativeMapHomRestrict (hφ.hom T f) (hψ.hom T f))).map
          (hφ.relativeTwistSpaceMap T f n) ≫
      (Scheme.Modules.pullbackComp (relativeMapHomRestrict (hφ.hom T f) (hψ.hom T f))
          (hφ.hom T f).relativeMapDomain.ι).hom.app (relativeTwist (dQ.algebra T f) n) ≫
      (Scheme.Modules.pullbackCongr
          (relativeMapHomRestrict_comp_ι (hφ.hom T f) (hψ.hom T f))).hom.app
        (relativeTwist (dQ.algebra T f) n) ≫
      (Scheme.Modules.pullbackComp
          ((relativeProj (dR.algebra T f)).scheme.homOfLE
            (relativeMapDomain_comp_le (hφ.hom T f) (hψ.hom T f)))
          (relativeMapHom (hψ.hom T f))).inv.app (relativeTwist (dQ.algebra T f) n) ≫
      (Scheme.Modules.pullback ((relativeProj (dR.algebra T f)).scheme.homOfLE
          (relativeMapDomain_comp_le (hφ.hom T f) (hψ.hom T f)))).map
        (hψ.relativeTwistSpaceMap T f n) ≫
      (Scheme.Modules.pullbackComp ((relativeProj (dR.algebra T f)).scheme.homOfLE
            (relativeMapDomain_comp_le (hφ.hom T f) (hψ.hom T f)))
          (hψ.hom T f).relativeMapDomain.ι).hom.app (relativeTwist (dR.algebra T f) n) ≫
      (Scheme.Modules.pullbackCongr (Scheme.homOfLE_ι (relativeProj (dR.algebra T f)).scheme
          (relativeMapDomain_comp_le (hφ.hom T f) (hψ.hom T f)))).hom.app
        (relativeTwist (dR.algebra T f) n) =
      (hφ.comp hψ).relativeTwistSpaceMap T f n
```

**`AlgebraicGeometry.Space.RelativeProjSituation.homPoints_comp_relativeMap_twist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/HomPointsComp.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/HomPointsComp.lean#L136). The attribute's comment: “the tag's three assertions for the relative Projs of Situation 0849 and the data of Tag 085F attached to the algebra maps: U(ψ ∘ φ) = r\_ψ^\{-1}(U(φ)) as subfunctors of R (the source prints r\_φ^\{-1}(U(ψ)), which is type-incorrect, the names φ and ψ being interchanged), r\_\{ψ ∘ φ} = r\_φ ∘ r\_ψ|\_\{U(ψ ∘ φ)}, and θ\_ψ ∘ r\_ψ^*θ\_φ = θ\_\{ψ ∘ φ} at every scheme point of the base, where Tag 085F's θ is given”.

> **[Stacks, Tag 085G].** Let `S` be a scheme, `X` an algebraic space over `S`, and `𝒜₁`, `𝒜₂`,
> `𝒜₃` quasi-coherent graded `𝒪_X`-algebras (Situation 0849), with relative Projs
> `P = Proj_X(𝒜₁)`, `Q = Proj_X(𝒜₂)` and `R = Proj_X(𝒜₃)`.  Let `φ : 𝒜₁ ⟶ 𝒜₂` and
> `ψ : 𝒜₂ ⟶ 𝒜₃` be graded `𝒪_X`-algebra maps, and write `U(-)`, `r_-` and `θ_-` for the data of
> Tag 085F attached to `φ`, `ψ` and `ψ ∘ φ` (`φ.comp ψ`) through
> `AlgebraicGeometry.Space.RelativeProjSituation.homPoints`.  Then
>
> 0. the map of graded algebras over the scheme points of the base attached to `ψ ∘ φ` is the
>   composite of those attached to `φ` and `ψ`;
> 1. `U(ψ ∘ φ) = r_ψ^{-1}(U(φ))`, as subfunctors of `R` (the image under the inclusion of `U(ψ)` of
>   the inverse image of `U(φ)` along `r_ψ`; the source prints `r_φ^{-1}(U(ψ))`, which does not
>   typecheck, the names `φ` and `ψ` being interchanged, see the module docstring);
> 2. `r_{ψ ∘ φ} = r_φ ∘ r_ψ|_{U(ψ ∘ φ)}`, with `r_ψ|_{U(ψ ∘ φ)} : U(ψ ∘ φ) ⟶ U(φ)` the restriction
>   `AlgebraicGeometry.Space.RelativeProjHomPoints.compRestrict`;
> 3. `θ_ψ ∘ r_ψ^*θ_φ = θ_{ψ ∘ φ}`: over every scheme point `(T, f)` of `X` — where Tag 085F's `θ`
>   is given — and in every degree `n`, the map on twists of the composite is the inverse image of
>   `θ_φ` along the restriction of `r_ψ`, followed by the inverse image of `θ_ψ` along the inclusion
>   of `U(ψ ∘ φ)` into `U(ψ)`, up to the inverse-image isomorphisms identifying sources and targets.
>
> There are no hypotheses beyond the data.

```lean
theorem homPoints_comp_relativeMap_twist :
    𝔥ψφ = (𝔥φ).comp (𝔥ψ) ∧
      (𝔥ψφ).relativeMapSubfunctor =
        ((𝔥φ).relativeMapSubfunctor.preimage (𝔥ψ).relativeMapSpaceHom).image
          (𝔥ψ).relativeMapSubfunctor.ι ∧
      (𝔥φ).compRestrict (𝔥ψ)
          (homPoints_comp h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k h₃c h₃n h₃q h₃k φ ψ) ≫
          (𝔥φ).relativeMapSpaceHom = (𝔥ψφ).relativeMapSpaceHom ∧
      ∀ (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X.1) (n : ℤ),
        (Scheme.Modules.pullbackCongr
              (relativeMapHomRestrict_comp_relativeMapHom ((𝔥φ).hom T f) ((𝔥ψ).hom T f))).inv.app
            (relativeTwist (𝔡₁ T f) n) ≫
          (Scheme.Modules.pullbackComp (relativeMapHomRestrict ((𝔥φ).hom T f) ((𝔥ψ).hom T f))
              (relativeMapHom ((𝔥φ).hom T f))).inv.app
            (relativeTwist (𝔡₁ T f) n) ≫
          (Scheme.Modules.pullback (relativeMapHomRestrict ((𝔥φ).hom T f) ((𝔥ψ).hom T f))).map
              ((𝔥φ).relativeTwistSpaceMap T f n) ≫
          (Scheme.Modules.pullbackComp (relativeMapHomRestrict ((𝔥φ).hom T f) ((𝔥ψ).hom T f))
              ((𝔥φ).hom T f).relativeMapDomain.ι).hom.app
            (relativeTwist (𝔡₂ T f) n) ≫
          (Scheme.Modules.pullbackCongr
              (relativeMapHomRestrict_comp_ι ((𝔥φ).hom T f) ((𝔥ψ).hom T f))).hom.app
            (relativeTwist (𝔡₂ T f) n) ≫
          (Scheme.Modules.pullbackComp
              ((relativeProj (𝔡₃ T f)).scheme.homOfLE
                (relativeMapDomain_comp_le ((𝔥φ).hom T f) ((𝔥ψ).hom T f)))
              (relativeMapHom ((𝔥ψ).hom T f))).inv.app
            (relativeTwist (𝔡₂ T f) n) ≫
          (Scheme.Modules.pullback ((relativeProj (𝔡₃ T f)).scheme.homOfLE
              (relativeMapDomain_comp_le ((𝔥φ).hom T f) ((𝔥ψ).hom T f)))).map
            ((𝔥ψ).relativeTwistSpaceMap T f n) ≫
          (Scheme.Modules.pullbackComp
              ((relativeProj (𝔡₃ T f)).scheme.homOfLE
                (relativeMapDomain_comp_le ((𝔥φ).hom T f) ((𝔥ψ).hom T f)))
              ((𝔥ψ).hom T f).relativeMapDomain.ι).hom.app
            (relativeTwist (𝔡₃ T f) n) ≫
          (Scheme.Modules.pullbackCongr
              (Scheme.homOfLE_ι (relativeProj (𝔡₃ T f)).scheme
                (relativeMapDomain_comp_le ((𝔥φ).hom T f) ((𝔥ψ).hom T f)))).hom.app
            (relativeTwist (𝔡₃ T f) n) =
          ((𝔥φ).comp (𝔥ψ)).relativeTwistSpaceMap T f n
```

## Tag 085H, a lemma

[Tag 085H](https://stacks.math.columbia.edu/tag/085H) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjTwistCompare.NotIsoExample.not_isIso_relativeTwistMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjTwistCompare/NotIsoExampleScheme.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjTwistCompare/NotIsoExampleScheme.lean#L258). The attribute's comment: “(3), second half: the maps θ are not isomorphisms in general, even if A → B is surjective: A = R[x,y]/(x²) with deg x = 1, deg y = 2, B = A/(x) on Spec R, θ₁ is not an iso”.

> **The comparison map `θ₁ : r_ψ^*𝒪(1) ⟶ 𝒪(1)` of Stacks 07ZG for `ψ : A~ ⟶ B~` on `Spec R` is
> not an isomorphism**, although `ψ` is surjective in every degree (`epi_sheafHom_app`).

```lean
theorem not_isIso_relativeTwistMap :
    ¬ IsIso (relativeTwistMap (sheafHom R) ((1 : ℕ) : ℤ))
```

**`AlgebraicGeometry.Space.isDefinedOn_of_eventually_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctorialityEventual.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctorialityEventual.lean#L111). The attribute's comment: “part (1): every point of Q lies in the domain of definition”.

> If every restriction of `ψ` is an epimorphism in all sufficiently large degrees then every
> point of `Q = Proj_X(ℬ)` lies in the domain of definition of `ψ`.

```lean
theorem isDefinedOn_of_eventually_epi
    (hsurj : ∀ (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X),
      ∀ᶠ d : ℕ in atTop, Epi ((ψ T f).app (d : ℤ)))
    (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X) {T' : BigFppfOver B S hS}
    (r : T' ⟶ T) (u : yoneda.obj T' ⟶ Q) (hu : u ≫ πQ = yoneda.map r ≫ f) :
    IsDefinedOn dP dQ ψ T f r u hu
```

**`AlgebraicGeometry.Space.isClosedImmersion_pointRelativeMapHom_of_eventually_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctorialityEventual.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctorialityEventual.lean#L230). The attribute's comment: “part (2): a closed immersion over each scheme point of the base”.

> If every restriction of `ψ` is an epimorphism in all sufficiently large degrees then over each
> scheme point `(T, f)` of `X` the morphism `r_{ψ|_{T,f}} : Proj_T(ℬ|_T) ⟶ Proj_T(𝒜|_T)` of Stacks
> 07ZG is a closed immersion of schemes.

```lean
theorem isClosedImmersion_pointRelativeMapHom_of_eventually_epi
    (hsurj : ∀ (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X),
      ∀ᶠ d : ℕ in atTop, Epi ((ψ T f).app (d : ℤ)))
    (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X) :
    _root_.AlgebraicGeometry.IsClosedImmersion (relativeMapHom (ψ T f))
```

**`AlgebraicGeometry.Space.epi_pointTwistMap_of_eventually_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctorialityEventual.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctorialityEventual.lean#L241). The attribute's comment: “part (3): the maps on twists are surjective, chart by chart”.

> If every restriction of `ψ` is an epimorphism in all sufficiently large degrees then, over
> every affine open of every scheme point of the base, the comparison maps of Stacks 01MY on the
> `n`-th twist are epimorphisms.

```lean
theorem epi_pointTwistMap_of_eventually_epi
    (hsurj : ∀ (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X),
      ∀ᶠ d : ℕ in atTop, Epi ((ψ T f).app (d : ℤ)))
    (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X)
    {V : ((BigFppfOver.toScheme B S hS).obj T).Opens} (hV : IsAffineOpen V) (n : ℤ) :
    Epi ((Stacks.AlgebraicGeometry.ProjTwistCompare.projMapData ((dP.algebra T f).grading V)
      ((dQ.algebra T f).grading V) ((ψ T f).sectionHom V)).twistMap n)
```

**`AlgebraicGeometry.Space.RelativeProjHomPoints.relativeMapSubfunctor_eq_top_of_eventually_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctorialityEventual.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctorialityEventual.lean#L290). The attribute's comment: “part (1): U(ψ) = Q”.

> If every restriction of `ψ` is an epimorphism in all sufficiently large degrees then the open
> subspace `U(ψ)` of Stacks 085F is all of `Q = Proj_X(ℬ)`.

```lean
theorem relativeMapSubfunctor_eq_top_of_eventually_epi
    (hsurj : ∀ (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X),
      ∀ᶠ d : ℕ in atTop, Epi ((hψ.hom T f).app (d : ℤ))) :
    hψ.relativeMapSubfunctor = ⊤
```

**`AlgebraicGeometry.Space.RelativeProjSituation.relativeMapSubfunctor_homPoints_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorialityClosedImmersion.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorialityClosedImmersion.lean#L218). The attribute's comment: “(1): U(ψ) = Q”.

> **Stacks 085H (1) for the canonical relative Projs: `U(ψ) = Q`.** If `ψ_d : 𝒜₁,d ⟶ 𝒜₂,d` is
> surjective for `d ≫ 0`, the open subspace `U(ψ)` of Stacks 085F is all of
> `Q = Proj_X(𝒜₂)`. This is also Stacks 085J (1), whose hypotheses contain these.

```lean
theorem relativeMapSubfunctor_homPoints_eq_top
    (hsurj : ∀ᶠ d : ℕ in atTop, Presheaf.IsLocallySurjective (SmallEtale.topology B S hS X.1)
      ((PresheafOfModules.toPresheaf _).map (ψ.app (d : ℤ)).val)) :
    (homPoints h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k ψ).relativeMapSubfunctor = ⊤
```

**`AlgebraicGeometry.Space.RelativeProjSituation.isClosedImmersion_relativeMapSpaceHom_homPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorialityClosedImmersion.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorialityClosedImmersion.lean#L232). The attribute's comment: “(2): r\_ψ : Q ⟶ P is a closed immersion”.

> **Stacks 085H (2) for the canonical relative Projs: `r_ψ` is a closed immersion.** If
> `ψ_d : 𝒜₁,d ⟶ 𝒜₂,d` is surjective for `d ≫ 0`, the morphism `r_ψ : U(ψ) ⟶ Proj_X(𝒜₁)` of
> Stacks 085F, whose source is all of `Proj_X(𝒜₂)` by `relativeMapSubfunctor_homPoints_eq_top`, is
> a closed immersion of algebraic spaces. This is also Stacks 085J (2), whose hypotheses contain
> these.

```lean
theorem isClosedImmersion_relativeMapSpaceHom_homPoints
    (hsurj : ∀ᶠ d : ℕ in atTop, Presheaf.IsLocallySurjective (SmallEtale.topology B S hS X.1)
      ((PresheafOfModules.toPresheaf _).map (ψ.app (d : ℤ)).val)) :
    IsClosedImmersion B S hS (homPoints h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k ψ).relativeMapSpaceHom
```

**`AlgebraicGeometry.Space.RelativeProjSituation.epi_twistMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorialityTwistGluedSurjective.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorialityTwistGluedSurjective.lean#L86). The attribute's comment: “(3), first half: the maps θ : r\_ψ^*O\_P(n) → O\_Q(n) are surjective (θ the glued map of 085F, twistMap), for ψ\_d surjective for d ≫ 0”.

> **Stacks 085H (3), surjectivity: the maps `θ : r_ψ^*𝒪_P(n) ⟶ 𝒪_Q(n)` are surjective** when
> `ψ_d` is surjective for `d ≫ 0`.

```lean
theorem epi_twistMap
    (hsurj : ∀ᶠ d : ℕ in atTop, Presheaf.IsLocallySurjective (SmallEtale.topology B S hS X.1)
      ((PresheafOfModules.toPresheaf _).map (ψ.app (d : ℤ)).val))
    (Px : Presentation B S hS X.1 X.2) (n : ℤ) :
    Epi (twistMap h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k ψ Px n)
```

## Tag 085I, a lemma

[Tag 085I](https://stacks.math.columbia.edu/tag/085I) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeProjSituation.relativeMapSubfunctor_homPoints_eq_top_of_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorialityIsIso.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorialityIsIso.lean#L84). The attribute's comment: “(1): U(ψ) = Q, for ψ\_d : A\_d → B\_d an isomorphism for d ≫ 0”.

> **Stacks 085I (1): `U(ψ) = Q`.** If `ψ_d : 𝒜₁,d ⟶ 𝒜₂,d` is an isomorphism for `d ≫ 0`, the
> open subspace `U(ψ)` of Stacks 085F is all of `Q = Proj_X(𝒜₂)`.

```lean
theorem relativeMapSubfunctor_homPoints_eq_top_of_isIso
    (hiso : ∀ᶠ d : ℕ in atTop, IsIso (ψ.app (d : ℤ))) :
    (homPoints h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k ψ).relativeMapSubfunctor = ⊤
```

**`AlgebraicGeometry.Space.RelativeProjSituation.isIso_relativeMapSpaceHom_homPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorialityIsIso.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorialityIsIso.lean#L95). The attribute's comment: “(2): r\_ψ : Q → P is an isomorphism, for ψ\_d an isomorphism for d ≫ 0”.

> **Stacks 085I (2): `r_ψ : Q ⟶ P` is an isomorphism.** If `ψ_d : 𝒜₁,d ⟶ 𝒜₂,d` is an
> isomorphism for `d ≫ 0`, the morphism `r_ψ : U(ψ) ⟶ Proj_X(𝒜₁)` of Stacks 085F, whose source is
> all of `Q = Proj_X(𝒜₂)` by `relativeMapSubfunctor_homPoints_eq_top_of_isIso`, is an isomorphism
> of algebraic spaces.

```lean
theorem isIso_relativeMapSpaceHom_homPoints
    (hiso : ∀ᶠ d : ℕ in atTop, IsIso (ψ.app (d : ℤ))) :
    IsIso (homPoints h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k ψ).relativeMapSpaceHom
```

**`AlgebraicGeometry.Space.RelativeProjSituation.isIso_twistMap_of_eventually_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorialityIsIso.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorialityIsIso.lean#L107). The attribute's comment: “(3): the maps θ : r\_ψ^*O\_P(n) → O\_Q(n) are isomorphisms (θ the glued map of 085F, twistMap), for ψ\_d an isomorphism for d ≫ 0”.

> **Stacks 085I (3): the maps `θ : r_ψ^*𝒪_P(n) ⟶ 𝒪_Q(n)` are isomorphisms** when `ψ_d` is an
> isomorphism for `d ≫ 0`. Here `θ_n` is the glued map of Stacks 085F (`twistMap`), built along a
> presentation `Px` of `X`; it is read on the chart of `Px`, where it is the `θ_n` of Stacks 07ZG for
> the restriction of `ψ`, an isomorphism by Stacks 07ZJ (3).

```lean
theorem isIso_twistMap_of_eventually_isIso
    (hiso : ∀ᶠ d : ℕ in atTop, IsIso (ψ.app (d : ℤ)))
    (Px : Presentation B S hS X.1 X.2) (n : ℤ) :
    IsIso (twistMap h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k ψ Px n)
```

## Tag 085J, a lemma

[Tag 085J](https://stacks.math.columbia.edu/tag/085J) in the Stacks Project.

**`AlgebraicGeometry.Space.isDefinedOn_of_eventually_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctorialityEventual.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctorialityEventual.lean#L111). The attribute's comment: “part (1): every point of Q lies in the domain of definition”.

> If every restriction of `ψ` is an epimorphism in all sufficiently large degrees then every
> point of `Q = Proj_X(ℬ)` lies in the domain of definition of `ψ`.

```lean
theorem isDefinedOn_of_eventually_epi
    (hsurj : ∀ (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X),
      ∀ᶠ d : ℕ in atTop, Epi ((ψ T f).app (d : ℤ)))
    (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X) {T' : BigFppfOver B S hS}
    (r : T' ⟶ T) (u : yoneda.obj T' ⟶ Q) (hu : u ≫ πQ = yoneda.map r ≫ f) :
    IsDefinedOn dP dQ ψ T f r u hu
```

**`AlgebraicGeometry.Space.isClosedImmersion_pointRelativeMapHom_of_eventually_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctorialityEventual.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctorialityEventual.lean#L230). The attribute's comment: “part (2): a closed immersion over each scheme point of the base”.

> If every restriction of `ψ` is an epimorphism in all sufficiently large degrees then over each
> scheme point `(T, f)` of `X` the morphism `r_{ψ|_{T,f}} : Proj_T(ℬ|_T) ⟶ Proj_T(𝒜|_T)` of Stacks
> 07ZG is a closed immersion of schemes.

```lean
theorem isClosedImmersion_pointRelativeMapHom_of_eventually_epi
    (hsurj : ∀ (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X),
      ∀ᶠ d : ℕ in atTop, Epi ((ψ T f).app (d : ℤ)))
    (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X) :
    _root_.AlgebraicGeometry.IsClosedImmersion (relativeMapHom (ψ T f))
```

**`AlgebraicGeometry.Space.isIso_pointTwistMap_of_generatedInDegreeOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctorialityEventual.lean, line 266](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctorialityEventual.lean#L266). The attribute's comment: “part (3): the maps on twists are isomorphisms, chart by chart”.

> If every restriction of `ψ` is an epimorphism in all sufficiently large degrees and `𝒜` is
> generated in degree one over every affine open of every scheme point of the base, the comparison
> maps of Stacks 01MY on the twists over those affine opens are isomorphisms.

```lean
theorem isIso_pointTwistMap_of_generatedInDegreeOne
    (hsurj : ∀ (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X),
      ∀ᶠ d : ℕ in atTop, Epi ((ψ T f).app (d : ℤ)))
    (hgen : ∀ (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X)
      (U : ((BigFppfOver.toScheme B S hS).obj T).Opens), IsAffineOpen U →
        (dP.algebra T f).IsGeneratedInDegreeOneAt U)
    (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X)
    {V : ((BigFppfOver.toScheme B S hS).obj T).Opens} (hV : IsAffineOpen V) (n : ℤ) :
    IsIso ((Stacks.AlgebraicGeometry.ProjTwistCompare.projMapData ((dP.algebra T f).grading V)
      ((dQ.algebra T f).grading V) ((ψ T f).sectionHom V)).twistMap n)
```

**`AlgebraicGeometry.Space.RelativeProjHomPoints.relativeMapSubfunctor_eq_top_of_eventually_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctorialityEventual.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFunctorialityEventual.lean#L290). The attribute's comment: “part (1): U(ψ) = Q”.

> If every restriction of `ψ` is an epimorphism in all sufficiently large degrees then the open
> subspace `U(ψ)` of Stacks 085F is all of `Q = Proj_X(ℬ)`.

```lean
theorem relativeMapSubfunctor_eq_top_of_eventually_epi
    (hsurj : ∀ (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X),
      ∀ᶠ d : ℕ in atTop, Epi ((hψ.hom T f).app (d : ℤ))) :
    hψ.relativeMapSubfunctor = ⊤
```

**`AlgebraicGeometry.Space.RelativeProjSituation.relativeMapSubfunctor_homPoints_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorialityClosedImmersion.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorialityClosedImmersion.lean#L218). The attribute's comment: “(1): U(ψ) = Q”.

> **Stacks 085H (1) for the canonical relative Projs: `U(ψ) = Q`.** If `ψ_d : 𝒜₁,d ⟶ 𝒜₂,d` is
> surjective for `d ≫ 0`, the open subspace `U(ψ)` of Stacks 085F is all of
> `Q = Proj_X(𝒜₂)`. This is also Stacks 085J (1), whose hypotheses contain these.

```lean
theorem relativeMapSubfunctor_homPoints_eq_top
    (hsurj : ∀ᶠ d : ℕ in atTop, Presheaf.IsLocallySurjective (SmallEtale.topology B S hS X.1)
      ((PresheafOfModules.toPresheaf _).map (ψ.app (d : ℤ)).val)) :
    (homPoints h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k ψ).relativeMapSubfunctor = ⊤
```

**`AlgebraicGeometry.Space.RelativeProjSituation.isClosedImmersion_relativeMapSpaceHom_homPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorialityClosedImmersion.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorialityClosedImmersion.lean#L232). The attribute's comment: “(2): r\_ψ : Q ⟶ P is a closed immersion”.

> **Stacks 085H (2) for the canonical relative Projs: `r_ψ` is a closed immersion.** If
> `ψ_d : 𝒜₁,d ⟶ 𝒜₂,d` is surjective for `d ≫ 0`, the morphism `r_ψ : U(ψ) ⟶ Proj_X(𝒜₁)` of
> Stacks 085F, whose source is all of `Proj_X(𝒜₂)` by `relativeMapSubfunctor_homPoints_eq_top`, is
> a closed immersion of algebraic spaces. This is also Stacks 085J (2), whose hypotheses contain
> these.

```lean
theorem isClosedImmersion_relativeMapSpaceHom_homPoints
    (hsurj : ∀ᶠ d : ℕ in atTop, Presheaf.IsLocallySurjective (SmallEtale.topology B S hS X.1)
      ((PresheafOfModules.toPresheaf _).map (ψ.app (d : ℤ)).val)) :
    IsClosedImmersion B S hS (homPoints h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k ψ).relativeMapSpaceHom
```

**`AlgebraicGeometry.Space.RelativeProjSituation.isIso_twistMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorialityTwistGluedSurjective.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorialityTwistGluedSurjective.lean#L98). The attribute's comment: “(3): the maps θ : r\_ψ^*O\_P(n) → O\_Q(n) are isomorphisms (θ the glued map of 085F, twistMap), for ψ\_d surjective for d ≫ 0 and A generated by A\_1 over A\_0”.

> **Stacks 085J (3): the maps `θ : r_ψ^*𝒪_P(n) ⟶ 𝒪_Q(n)` are isomorphisms** when `ψ_d` is
> surjective for `d ≫ 0` and `𝒜₁` is generated by its degree-one part over its degree-zero part.

```lean
theorem isIso_twistMap
    (hsurj : ∀ᶠ d : ℕ in atTop, Presheaf.IsLocallySurjective (SmallEtale.topology B S hS X.1)
      ((PresheafOfModules.toPresheaf _).map (ψ.app (d : ℤ)).val))
    (hgen : (𝔰₁).IsGeneratedInDegreeOne) (Px : Presentation B S hS X.1 X.2) (n : ℤ) :
    IsIso (twistMap h₁c h₁n h₁q h₁k h₂c h₂n h₂q h₂k ψ Px n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 71.12, Tag 085E](https://stacks.math.columbia.edu/tag/085E)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
