---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.RelativeProjSituation, AlgebraicGeometry.Space.RelativeProjSituation.relativeProjFunctorEquivF_map_mk, AlgebraicGeometry.Space.RelativeProjSituation.bijective_restrictCompactOpens, AlgebraicGeometry.Space.RelativeProjSituation.relativeProjπ_app_mk, AlgebraicGeometry.Space.GradedAlgebraPoints.F, AlgebraicGeometry.Space.RelativeProjSituation.isAlgebraicSpace_relativeProjFunctor, AlgebraicGeometry.Space.RelativeProjSituation.relativeProjPoints, AlgebraicGeometry.Space.RelativeProjSituation.isPullback_projComparison
statement: formalized
proof: formalized
---

# 71.11 Relative Proj

Section 71.11 of the Stacks Project, [Tag 0848](https://stacks.math.columbia.edu/tag/0848). 12 tags here are carried by 59 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0849, a situation

[Tag 0849](https://stacks.math.columbia.edu/tag/0849) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeProjSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProj.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProj.lean#L175).

> **Stacks 0849.** A scheme `S`, an algebraic space `X` over `S`, and a quasi-coherent graded
> `𝒪_X`-algebra, commutative and concentrated in nonnegative degrees: the data from which the
> relative homogeneous spectrum `Proj_X(𝒜)` is built.

```lean
structure RelativeProjSituation
```

## Tag 084A, an equation

[Tag 084A](https://stacks.math.columbia.edu/tag/084A) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeProjSituation.relativeProjFunctorEquivF_map_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorCompactOpens.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorCompactOpens.lean#L240). The attribute's comment: “functoriality: on quasi-compact test schemes the restriction map of F along h : T' -> T sends the class of a quadruple (d, f, L, psi) to the class of its pullback (d, f o h, h^*L, h^*psi)”.

> **Stacks 084A, functoriality: the restriction map of `F` is the pullback of quadruples.**
> For a morphism `τ : T' ⟶ T` of quasi-compact test objects and a point `x` of `F(T)` which is the
> class of a quadruple `(d, f, ℒ, ψ)`, the restriction of `x` to `T'` is the class of the pullback
> quadruple `(d, f ∘ τ, τ^*ℒ, τ^*ψ)`,
> `AlgebraicGeometry.Space.GradedAlgebraRestriction.quadrupleRestrict`.

```lean
theorem relativeProjFunctorEquivF_map_mk {T T' : BigFppfOver s.site s.base s.containsBase}
    (τ : T' ⟶ T) (hT : CompactSpace ((BigFppfOver.toScheme s.site s.base s.containsBase).obj T))
    (hT' : CompactSpace ((BigFppfOver.toScheme s.site s.base s.containsBase).obj T'))
    (x : s.relativeProjFunctor.obj (op T)) (f : yoneda.obj T ⟶ s.space.1) {d : ℤ} (hd : 0 < d)
    (P : (GradedAlgebraPoints.ofQuasicoherentFamily s.shrink.pointAlgebra).Quadruples T f d)
    (hx : s.relativeProjFunctorEquivF T hT x = GradedAlgebraPoints.F.mk _ f hd P) :
    s.relativeProjFunctorEquivF T' hT' (s.relativeProjFunctor.map τ.op x) =
      GradedAlgebraPoints.F.mk _ (yoneda.map τ ≫ f) hd
        (s.quadrupleRestriction.quadrupleRestrict τ f (yoneda.map τ ≫ f) rfl P)
```

**`AlgebraicGeometry.Space.RelativeProjSituation.bijective_restrictCompactOpens`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorCompactOpens.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorCompactOpens.lean#L275). The attribute's comment: “for an arbitrary test scheme T, F(T) is the limit of F(V) over the quasi-compact opens V of T: restricting to the quasi-compact opens is a bijection onto the compatible systems of classes of quadruples over them”.

> **Stacks 084A: for an arbitrary test scheme `T`, `F(T) = lim\_\{V ⊆ T quasi-compact open}
> F(V)`.**  The map sending a point `x` of `F(T)` to the family of its restrictions `x|\_V`, read as
> classes of quadruples over the quasi-compact opens `V` of `T`, is a bijection onto the families
> of classes of quadruples over the quasi-compact opens which are compatible with the restrictions
> `AlgebraicGeometry.Space.GradedAlgebraRestriction.FRestrict` along the inclusions.

```lean
theorem bijective_restrictCompactOpens (T : BigFppfOver s.site s.base s.containsBase) :
    Function.Bijective (s.restrictCompactOpens T)
```

**`AlgebraicGeometry.Space.RelativeProjSituation.relativeProjπ_app_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorCompactOpens.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FunctorCompactOpens.lean#L304). The attribute's comment: “the morphism F -> X of functors sends the class of a quadruple (d, f, L, psi) to f”.

> **Stacks 084A: the morphism `F ⟶ X` sends the quadruple `(d, f, ℒ, ψ)` to `f`.**  On a
> quasi-compact test object `T`, a point of `F(T)` which is the class of a quadruple
> `(d, f, ℒ, ψ)` is sent by `AlgebraicGeometry.Space.RelativeProjSituation.relativeProjπ` to the
> `T`-point `f` of `X`.

```lean
theorem relativeProjπ_app_mk (T : BigFppfOver s.site s.base s.containsBase)
    (hT : CompactSpace ((BigFppfOver.toScheme s.site s.base s.containsBase).obj T))
    (x : s.relativeProjFunctor.obj (op T)) (f : yoneda.obj T ⟶ s.space.1) {d : ℤ} (hd : 0 < d)
    (P : (GradedAlgebraPoints.ofQuasicoherentFamily s.shrink.pointAlgebra).Quadruples T f d)
    (hx : s.relativeProjFunctorEquivF T hT x = GradedAlgebraPoints.F.mk _ f hd P) :
    s.relativeProjπ.app (op T) x = yonedaEquiv f
```

**`AlgebraicGeometry.Space.GradedAlgebraPoints.F`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjQuadruples.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjQuadruples.lean#L179). The attribute's comment: “the value F(T) of the functor on a test object, as the union over d ≥ 1 of the quadruples (d, f : T → X, L, psi) modulo strict equivalence inside a degree and the equivalence of Tag 01NW across degrees, the restriction of the graded algebra to the scheme points of X being a datum; the functoriality in the test object and the inverse limit over the quasi-compact opens are not constructed, the pullback of a quadruple not being available”.

> **Stacks 084A.** The value `F(T)` on a test object of the functor of quadruples of the
> relative homogeneous spectrum of a quasi-coherent graded `𝒪_X`-algebra: the union over `d ≥ 1`
> of the sets of quadruples `(d, f : T → X, ℒ, ψ)` of degree `d`, modulo strict equivalence inside
> a degree and the equivalence of Tag 01NW across degrees.
>
> The identifications relate only quadruples over the same `T`-point of `X`, so the set is fibred
> over the `T`-points of `X`, which is the morphism a quadruple records.

```lean
def F (T : BigFppfOver B S hS) : Type (u + 1)
```

## Tag 084B, a lemma

[Tag 084B](https://stacks.math.columbia.edu/tag/084B) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeProjSituation.isAlgebraicSpace_relativeProjFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/AlgebraicSpace.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/AlgebraicSpace.lean#L107). The attribute's comment: “first assertion: the functor F of Tag 084A is an algebraic space”.

> **Stacks 084B, first assertion: the functor `F` of Stacks 084A is an algebraic space.**

```lean
theorem isAlgebraicSpace_relativeProjFunctor :
    IsAlgebraicSpace s.site s.base s.containsBase s.relativeProjFunctor
```

**`AlgebraicGeometry.Space.RelativeProjSituation.relativeProjPoints`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/AlgebraicSpace.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/AlgebraicSpace.lean#L121). The attribute's comment: “second assertion: for every morphism g : Z -> X from a scheme of the site, a canonical isomorphism Proj\_Z(g^*A) = Z x\_X F, as a cartesian square”.

> **Stacks 084B, second assertion: `Z ×_X F = Proj_Z(g^*𝒜)`.** For every scheme point
> `g : Z → X` an object of the site whose scheme is the relative Proj of the restriction `g^*𝒜`
> (`relativeProjPoints_algebra`), with a cartesian square identifying it with `Z ×_X F`.
>
> The restriction `g^*𝒜` is that of the re-presentation of `𝒜` with sections in the universe `u`
> (`smallAlgebra`, compared with `𝒜` by `smallAlgebraEquiv`); when the sections of `𝒜` already lie
> in `u` it is isomorphic to the restriction of `𝒜` itself by `shrinkPointAlgebraIso`.

```lean
def relativeProjPoints : RelativeProjPoints s.site s.base s.containsBase s.relativeProjπ
```

**`AlgebraicGeometry.Space.RelativeProjSituation.isPullback_projComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/AlgebraicSpace.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/AlgebraicSpace.lean#L139). The attribute's comment: “third assertion: the identifications Proj\_Z(g^*A) = Z x\_X F are compatible with further base change Z' -> Z, through the canonical base-change morphism of Tag 01O3”.

> **Stacks 084B, third assertion: compatibility with further base change.** For a morphism
> `h : Z' ⟶ Z` of test objects and a scheme point `g : Z → X`, the comparison morphism
> `Proj_{Z'}((g ∘ h)^*𝒜) ⟶ Proj_Z(g^*𝒜)` exhibits the source as `Z' ×_Z Proj_Z(g^*𝒜)`; it is
> compatible with the identifications with `Z ×_X F` and `Z' ×_X F` of the second assertion; and
> it is the canonical one: the identification `Proj_{Z'}((g ∘ h)^*𝒜) ≅ Proj_{Z'}(h^*(g^*𝒜))` of
> the restricted algebras followed by the base-change morphism of Tag 01O3.

```lean
theorem isPullback_projComparison {Z Z' : BigFppfOver s.site s.base s.containsBase}
    (g : yoneda.obj Z ⟶ s.space.1) (h : Z' ⟶ Z) :
    IsPullback (s.quadrupleRestriction.projComparison
      s.shrink.contains_relativeProj_pointAlgebra g h)
        (s.relativeProjPoints.fibreHom Z' (yoneda.map h ≫ g))
        (s.relativeProjPoints.fibreHom Z g) h ∧
      yoneda.map (s.quadrupleRestriction.projComparison
        s.shrink.contains_relativeProj_pointAlgebra g h) ≫
          s.relativeProjPoints.fibreToSpace Z g =
        s.relativeProjPoints.fibreToSpace Z' (yoneda.map h ≫ g) ∧
      (BigFppfOver.toScheme s.site s.base s.containsBase).map
          (s.quadrupleRestriction.projComparison s.shrink.contains_relativeProj_pointAlgebra g h) =
        (s.quadrupleRestriction.restrictProjIso g h).hom ≫
          Stacks.AlgebraicGeometry.RelativeProjBaseChangeTwist.baseChangeHom
            (s.shrink.pointAlgebra Z g)
            ((BigFppfOver.toScheme s.site s.base s.containsBase).map h)
```

## Tag 084C, a definition

[Tag 084C](https://stacks.math.columbia.edu/tag/084C) in the Stacks Project.

**`AlgebraicGeometry.Space.ProjDescentData.relativeProj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjDescent.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjDescent.lean#L167). The attribute's comment: “the relative Proj as an algebraic space over the base”.

> The relative homogeneous spectrum `Proj_X(𝒜)` of a quasi-coherent graded
> `𝒪_X`-algebra on an algebraic space `X`: the quotient of the relative Proj `P_U` of the algebra
> on an étale chart of `X` by the étale equivalence relation `P_R ⇉ P_U` that the descent datum
> provides.

```lean
noncomputable def relativeProj : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u
```

**`AlgebraicGeometry.Space.ProjDescentData.isAlgebraicSpace_relativeProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjDescent.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjDescent.lean#L173). The attribute's comment: “the relative Proj is an algebraic space”.

> The relative Proj of an algebraic space is an algebraic space over the base scheme.

```lean
theorem isAlgebraicSpace_relativeProj : IsAlgebraicSpace B S hS d.relativeProj
```

**`AlgebraicGeometry.Space.ProjDescentData.toBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjDescent.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjDescent.lean#L202). The attribute's comment: “the structure morphism of the relative Proj”.

> The structure morphism `π : Proj_X(𝒜) ⟶ X` of the relative Proj: the
> descent of `P_U ⟶ U ⟶ X` along the quotient map.

```lean
noncomputable def toBase : d.relativeProj ⟶ X
```

**`AlgebraicGeometry.Space.RelativeProjSituation.Proj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/Space.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/Space.lean#L44). The attribute's comment: “the relative Proj of A over X: the algebraic space F of Tag 084B”.

> The relative homogeneous spectrum `Proj_X(𝒜)` of a quasi-coherent graded `𝒪_X`-algebra on
> an algebraic space `X` over `S`: the algebraic space `F` of Stacks 084B.

```lean
def Proj : AlgebraicSpaces s.site s.base s.containsBase
```

**`AlgebraicGeometry.Space.RelativeProjSituation.π`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/Space.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/Space.lean#L49). The attribute's comment: “the structure morphism pi : Proj\_X(A) -> X”.

> The structure morphism `π : Proj_X(𝒜) ⟶ X` of the relative Proj.

```lean
def π : s.Proj ⟶ s.space
```

**`AlgebraicGeometry.Space.RelativeProjSituation.baseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/Space.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/Space.lean#L77). The attribute's comment: “the canonical isomorphism gamma : Proj\_U(phi^*A) -> Proj\_X(A) x\_X U over U”.

> For a scheme point `g : Z ⟶ X`, the canonical isomorphism
> `γ : Proj_Z(g^*𝒜) ≅ Proj_X(𝒜) ×_X Z` of Stacks 084B; the scheme of
> `s.relativeProjPoints.fibre Z g` is `Proj_Z(g^*𝒜)` by `s.relativeProjPoints.fibreIso Z g`.

```lean
def baseChangeIso (Z : BigFppfOver s.site s.base s.containsBase)
    (g : yoneda.obj Z ⟶ s.space.1) :
    yoneda.obj (s.relativeProjPoints.fibre Z g) ≅ pullback s.π.hom g
```

**`AlgebraicGeometry.Space.RelativeProjSituation.chartPresentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/Space.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/Space.lean#L310). The attribute's comment: “the etale covering P\_U -> Proj\_X(A) with P\_U x\_P P\_U = P\_R”.

> For an étale presentation `(U, R)` of `X`, the relative Projs `P_U = Proj_U(𝒜_U)` and
> `P_R = Proj_R(𝒜_R)` form an étale presentation of `Proj_X(𝒜)`: the chart
> `P_U = Proj_X(𝒜) ×_X U ⟶ Proj_X(𝒜)` is surjective and étale and `P_U ×_{Proj_X(𝒜)} P_U = P_R`,
> the two projections lying over the two maps `R ⇉ U` and exhibiting `P_R` as `P_U ×_U R` along
> each.

```lean
def chartPresentation : Presentation s.site s.base s.containsBase s.Proj.1 s.Proj.2
```

## Tag 084D, a lemma

[Tag 084D](https://stacks.math.columbia.edu/tag/084D) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeProjPoints.pointTwistAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPointTwists.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPointTwists.lean#L193). The attribute's comment: “the base-change clause: for every scheme point f : T -> X of the base, the sheaf of Z-graded algebras (+)\_\{n in Z} O(n) -- homogeneous pieces, multiplication and unit, which are the three fields of the type -- on the base change Proj\_T(f^*A) of the relative Proj, which d.fibreIso identifies with the scheme of T x\_X Proj\_X(A). It is Tag 01NR's graded algebra there, which is what the tag asks the base change to agree with. Quasi-coherence of the pieces is NOT part of this type; it is isQuasicoherent\_pointTwist below. The sheaf on Proj\_X(A) itself is NOT produced here”.

> **Stacks 084D, clause (1), after base change to a scheme point of the base.**  The
> quasi-coherent sheaf of `ℤ`-graded algebras `⨁_{n ∈ ℤ} 𝒪_{Proj_T(f^*𝒜)}(n)` on the base change
> `T ×_X Proj_X(𝒜)` of the relative Proj along the `T`-point `f` of `X`, with its multiplication
> and its unit.

```lean
noncomputable def pointTwistAlgebra :
    SchemeGradedAlgebra (relativeProj (d.algebra T f)).scheme
```

**`AlgebraicGeometry.Space.RelativeProjPoints.isQuasicoherent_pointTwist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPointTwists.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPointTwists.lean#L206). The attribute's comment: “the base-change clause, quasi-coherence half: every homogeneous twist O(n) on the base change Proj\_T(f^*A) of the relative Proj along a scheme point f : T -> X of the base is a quasi-coherent module”.

> **Stacks 084D, quasi-coherence of the twists after base change to a scheme point.**

```lean
theorem isQuasicoherent_pointTwist (n : ℤ) : (d.pointTwist T f n).IsQuasicoherent
```

**`AlgebraicGeometry.Space.RelativeProjPoints.pointPsi`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPointTwists.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPointTwists.lean#L241). The attribute's comment: “the base-change clause for psi: the degreewise maps of the canonical homomorphism psi : pi^*A -> (+)\_\{n >= 0} O(n) on the base change Proj\_T(f^*A) of the relative Proj along a scheme point f : T -> X of the base, in the adjoint form (f^*A)\_n -> (pi\_T)\_* O(n) that Tag 01NR produces psi in. This declaration is the family of maps and nothing more; that it preserves the unit, is multiplicative, and is Tag 01MP's homogeneous-section map on the charts are the three companion theorems pointPsi\_one, pointPsi\_mul and pointPsi\_chart below. psi on Proj\_X(A) itself is NOT produced here”.

> **Stacks 084D, clause (2), after base change to a scheme point of the base.**  The canonical
> homomorphism of graded algebras `ψ : π^*𝒜 ⟶ ⨁_{n ≥ 0} 𝒪(n)`, read at the `T`-point `f` of `X` in
> the adjoint form that Stacks 01NR produces: in each degree `n ≥ 0` a map
> `(f^*𝒜)_n ⟶ (π_T)_*𝒪_{Proj_T(f^*𝒜)}(n)`.
>
> That it is a homomorphism of graded algebras is `…pointPsi_one` and `…pointPsi_mul`, and
> `…pointPsi_chart` identifies it on the projective-spectrum charts with the absolute
> homogeneous-section map of Stacks 01MP, which is what makes it the canonical one.

```lean
noncomputable def pointPsi (n : ℕ) :
    (d.algebra T f).piece (n : ℤ) ⟶
      (Scheme.Modules.pushforward (relativeProj (d.algebra T f)).toBase).obj
        (d.pointTwist T f (n : ℤ))
```

**`AlgebraicGeometry.Space.RelativeProjPoints.pointPsiHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPointTwists.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPointTwists.lean#L304). The attribute's comment: “the base-change clause for psi as a homomorphism of graded algebras: on the base change Proj\_T(f^*A) of the relative Proj along a scheme point f : T -> X of the base, the canonical homomorphism psi : pi\_T^*(f^*A) -> (+)\_n O(n) of sheaves of Z-graded algebras (multiplicative by construction), whose degree-n components for n >= 0 are the adjoint transposes of pointPsi. psi on Proj\_X(A) itself is NOT produced here”.

> **Stacks 084D, clause (2), after base change to a scheme point of the base, as a
> homomorphism of graded algebras.**  The canonical homomorphism
>
> `ψ : π_T^*(f^*𝒜) ⟶ ⨁_{n ∈ ℤ} 𝒪_{Proj_T(f^*𝒜)}(n)`
>
> of sheaves of `ℤ`-graded algebras on `Proj_T(f^*𝒜)`, where `π_T : Proj_T(f^*𝒜) ⟶ T` is the
> structure morphism: the transpose across `π_T^* ⊣ (π_T)_*` of the homogeneous-section map
> `AlgebraicGeometry.Space.RelativeProjPoints.pointPsi`, assembled with its multiplicativity
> (`Stacks.AlgebraicGeometry.RelativeProjTwists.TwistData.psiTransposeHom`).  The source writes the
> target as `⨁_{n ≥ 0} 𝒪(n)`; since `π_T^*(f^*𝒜)` vanishes in negative degrees the two targets
> receive the same homomorphisms, and the components in degrees `n ≥ 0` are the transposes of
> `pointPsi` (`…pointPsiHom_app_natCast`).

```lean
noncomputable def pointPsiHom :
    Stacks.PullbackGradedAlgebra.pullbackGradedAlgebra
        (Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.ringedSpaceHom
          (relativeProj (d.algebra T f)).toBase)
        (Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.situationAlgebra (d.algebra T f))
        (Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.isSheafStruct _) ⟶
      d.pointTwistAlgebra T f
```

**`AlgebraicGeometry.Space.RelativeProjPoints.pointTwistTheta`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPointTwists.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPointTwists.lean#L334). The attribute's comment: “the base-change clause is compatible with further base change: for g : Z -> T the inverse image of (+)\_d O\_\{Proj\_T(f^*A)}(d) along the base-change morphism is (+)\_d O\_\{Proj\_Z(g^*f^*A)}(d) as Z-graded algebras. This is Tag 01O3's theta, and it is the scheme-point case of the theta of Tag 085C”.

> **Stacks 01O3 at a scheme point of the base: the base-change isomorphism `θ`.**  For a further
> morphism of schemes `g : Z ⟶ T`, the inverse image along the base-change morphism
> `Proj_Z(g^*f^*𝒜) ⟶ Proj_T(f^*𝒜)` of the twists at the point `f` is the graded algebra of twists
> of `Proj_Z(g^*f^*𝒜)`, as `ℤ`-graded algebras.
>
> This is what makes the base-change clause of Stacks 084D a *compatible* family rather than a
> statement at one point at a time, and it is the scheme-point case of the `θ` of Stacks 085C.

```lean
noncomputable def pointTwistTheta {Z : Scheme.{u}}
    (g : Z ⟶ (BigFppfOver.toScheme B S hS).obj T) :
    pbAlgS (baseChangeHom (d.algebra T f) g) (d.pointTwistAlgebra T f) ≅
      Stacks.AlgebraicGeometry.Tag07ZGTwist.twistAlgebra ((d.algebra T f).pullback g)
```

**`AlgebraicGeometry.Space.RelativeProjPoints.basePsi_pointTwistTheta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPointTwists.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPointTwists.lean#L356). The attribute's comment: “the base-change clause for psi, compatible with further base change: for g : Z -> T the base change along g of psi at the scheme point f, followed by Tag 01O3's theta (pointTwistTheta), is Tag 01NR's psi for Proj\_Z(g^*f^*A), degree by degree”.

> **The base-change clause of Stacks 084D for `ψ`, at a scheme point of the base.**  For a
> further morphism of schemes `g : Z ⟶ T`, the base change along `g` of the homogeneous-section
> map `ψ` of the twists at the point `f` — the morphism
> `g^*(f^*𝒜)_k ⟶ (π_Z)_* h^*𝒪_{Proj_T(f^*𝒜)}(k)` adjoint to
> `(f^*𝒜)_k ⟶ (π_T)_*𝒪(k) ⟶ (π_T)_* h_* h^*𝒪(k)`, where `h : Proj_Z(g^*f^*𝒜) ⟶ Proj_T(f^*𝒜)` is the
> base-change morphism (`Stacks.AlgebraicGeometry.RelativeProjBaseChangeTwist.basePsi`) — followed
> by the isomorphism `θ` of `AlgebraicGeometry.Space.RelativeProjPoints.pointTwistTheta` is the
> homogeneous-section map of Stacks 01NR for `Proj_Z(g^*f^*𝒜)`.
>
> So the isomorphism `θ` of the graded algebras of twists is compatible with `ψ`: base change
> carries the whole of Stacks 084D's datum at `f` — graded algebra and `ψ` — to Stacks 01NR's datum
> on `Proj_Z(g^*f^*𝒜)`.  The proof is the gluing statement
> `Stacks.AlgebraicGeometry.TwistExistenceBasis.glueIso_psi` behind `θ`.

```lean
theorem basePsi_pointTwistTheta {Z : Scheme.{u}} (g : Z ⟶ (BigFppfOver.toScheme B S hS).obj T)
    (k : ℕ) :
    basePsi (relativeProj (d.algebra T f)).toBase
        (relativeProj ((d.algebra T f).pullback g)).toBase g
        (baseChangeHom (d.algebra T f) g) (baseChangeHom_comp_toBase (d.algebra T f) g)
        (d.pointPsi T f k) ≫
      (Scheme.Modules.pushforward (relativeProj ((d.algebra T f).pullback g)).toBase).map
        ((d.pointTwistTheta T f g).hom.app (k : ℤ)) =
      (twistDataOfGradedAlgebra ((d.algebra T f).pullback g)).ψ k
```

**`AlgebraicGeometry.Space.RelativeProjSituation.twistGradedAlgebra_psi_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjTwistDescent/TwistAlgebraOfProj.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjTwistDescent/TwistAlgebraOfProj.lean#L321). The attribute's comment: “on the constructed relative Proj P = Proj\_X(A) itself: the quasi-coherent sheaf of Z-graded O\_P-algebras (+)\_n O\_P(n) (twistGradedAlgebra: pieces, quasi-coherence, multiplication, unit), the canonical psi : pi^*A -> (+)\_\{n >= 0} O\_P(n) as a homomorphism of graded algebras (multiplicative and unital), and for every scheme T -> X identifications of the base change with the graded algebra of Tag 01NR on Proj\_T(f^*A) carrying multiplication, unit and psi to those of Tag 01NR, natural in the scheme”.

> **Stacks 084D on the relative Proj `P = Proj_X(𝒜)` of Situation 0849.**  For any presentation
> `X = U/R` used to construct the twists:
>
> 1. `⨁_{n ∈ ℤ} 𝒪_P(n)` (`…RelativeProjSituation.twistGradedAlgebra`) is a quasi-coherent sheaf of
>    `ℤ`-graded `𝒪_P`-algebras: its homogeneous pieces are the twists `𝒪_P(n)`, quasi-coherent, and
>    its multiplication and unit are `…RelativeProjSituation.twistAlgebraMul` and
>    `…RelativeProjSituation.twistAlgebraUnit`;
> 2. the canonical `ψ_n : π^*𝒜_n ⟶ 𝒪_P(n)`, `n ≥ 0` (`…RelativeProjSituation.psiTwistHom`), is a
>    homomorphism of graded algebras `π^*𝒜 ⟶ ⨁_{n ≥ 0} 𝒪_P(n)`: it carries the multiplication and
>    the unit of `π^*𝒜` (`…RelativeProjSituation.psiSourceMul`,
>    `…RelativeProjSituation.psiSourceUnit`) to those of the twists;
> 3. its base change to any scheme `f : T ⟶ X` over `X` agrees with Stacks 01NR: there are
>    isomorphisms `e_{T,f,n} : (T ×_X P ⟶ P)^*𝒪_P(n) ≅ 𝒪(n)^a` with the twists of Stacks 01NR on
>    `T ×_X P = Proj_T(f^*𝒜)`, carrying the inverse images of the multiplication, of the unit and of
>    `ψ` to the multiplication, the unit and `ψ` of Stacks 01NR, and compatible with further base
>    change along any `τ : T' ⟶ T` (through the comparison of twists of Tag 01O3).

```lean
theorem twistGradedAlgebra_psi_baseChange :
    -- (1) the quasi-coherent sheaf of `ℤ`-graded algebras `⨁_{n ∈ ℤ} 𝒪_P(n)`
    (∀ n : ℤ, (s.twistGradedAlgebra Px).piece n = (s.twistModule Px n).obj) ∧
    (∀ n : ℤ, ((s.twistGradedAlgebra Px).piece n).IsQuasicoherentOnSite) ∧
    (∀ i j : ℤ,
      haveI := SmallEtale.instHasSheafify s.site s.base s.containsBase s.relativeProjFunctor
        AddCommGrpCat.{u}
      haveI := SmallEtale.instWEqualsLocallyBijective s.site s.base s.containsBase
        s.relativeProjFunctor AddCommGrpCat.{u}
      SheafOfModules.GradedAlgebra.mulSheaf.{u, u + 1, u, u}
          (J := SmallEtale.topology s.site s.base s.containsBase s.relativeProjFunctor)
          (s.twistGradedAlgebra Px) i j =
        (modulesTensorObjIso s.site s.base s.containsBase s.relativeProjFunctor
            s.isAlgebraicSpace_relativeProjFunctor (s.twistModule Px i).obj
            (s.twistModule Px j).obj).inv ≫ s.twistAlgebraMul Px i j) ∧
    (haveI := SmallEtale.instHasSheafify s.site s.base s.containsBase s.relativeProjFunctor
        AddCommGrpCat.{u}
     haveI := SmallEtale.instWEqualsLocallyBijective s.site s.base s.containsBase
        s.relativeProjFunctor AddCommGrpCat.{u}
     SheafOfModules.GradedAlgebra.oneHom.{u, u + 1, u}
          (J := SmallEtale.topology s.site s.base s.containsBase s.relativeProjFunctor)
          (s.twistGradedAlgebra Px) = s.twistAlgebraUnit Px) ∧
    -- (2) `ψ : π^*𝒜 ⟶ ⨁_{n ≥ 0} 𝒪_P(n)` is a homomorphism of graded algebras
    (∀ i j : ℕ, s.psiSourceMul (i : ℤ) (j : ℤ) ≫ s.psiTwistHom Px (i + j) =
      (s.psiTwistHom Px i ⊗ₘ s.psiTwistHom Px j) ≫ s.twistAlgebraMul Px (i : ℤ) (j : ℤ)) ∧
    s.psiSourceUnit ≫ s.psiTwistHom Px 0 = s.twistAlgebraUnit Px ∧
    -- (3) the base change to every scheme point is the graded algebra and `ψ` of Stacks 01NR
    ∃ e : ∀ (T : BigFppfOver s.site s.base s.containsBase) (f : yoneda.obj T ⟶ s.space.1) (n : ℤ),
        (modulePullback s.site s.base s.containsBase (s.fibreToSpaceHom T f)).obj
          (s.twistModule Px n).obj ≅
          ((representedQuasicoherentSchemeEquivalence s.site s.base s.containsBase
            (s.relativeProjPoints.fibre T f)).functor.obj (s.twistPieceQcoh T f n)).obj,
      (∀ (T : BigFppfOver s.site s.base s.containsBase) (f : yoneda.obj T ⟶ s.space.1)
        (i j : ℤ),
        (modulePullbackTensorIso s.site s.base s.containsBase (s.fibreToSpaceHom T f)
            (s.twistModule Px i).obj (s.twistModule Px j).obj).inv ≫
          (modulePullback s.site s.base s.containsBase (s.fibreToSpaceHom T f)).map
            (s.twistAlgebraMul Px i j) ≫ (e T f (i + j)).hom =
        ((e T f i).hom ⊗ₘ (e T f j).hom) ≫
          representedTensorChartMul s.site s.base s.containsBase (s.twistPieceMul T f i j)) ∧
      (∀ (T : BigFppfOver s.site s.base s.containsBase) (f : yoneda.obj T ⟶ s.space.1),
        (modulePullbackUnitIso s.site s.base s.containsBase (s.fibreToSpaceHom T f)).inv ≫
            (modulePullback s.site s.base s.containsBase (s.fibreToSpaceHom T f)).map
              (s.twistAlgebraUnit Px) ≫ (e T f 0).hom =
          representedUnitChartHom s.site s.base s.containsBase (s.twistPieceUnit T f)) ∧
      (∀ (T : BigFppfOver s.site s.base s.containsBase) (f : yoneda.obj T ⟶ s.space.1) (n : ℕ),
        (modulePullback s.site s.base s.containsBase (s.fibreToSpaceHom T f)).map
            (s.psiTwistHom Px n) ≫ (e T f (n : ℤ)).hom = s.fibrePsiHom T f n) ∧
      ∀ {T T' : BigFppfOver s.site s.base s.containsBase} (τ : T' ⟶ T)
        (f : yoneda.obj T ⟶ s.space.1)
        {y : s.relativeProjPoints.fibre T' (yoneda.map τ ≫ f) ⟶ s.relativeProjPoints.fibre T f}
        (hy : s.relativeProjPoints.LiesOver y τ) (n : ℤ),
        e T' (yoneda.map τ ≫ f) n =
          eqToIso (congrArg (fun k :
              (⟨yoneda.obj (s.relativeProjPoints.fibre T' (yoneda.map τ ≫ f)),
                isAlgebraicSpace_yoneda s.site s.base s.containsBase _⟩ :
                AlgebraicSpaces s.site s.base s.containsBase) ⟶
                  ⟨s.relativeProjFunctor, s.isAlgebraicSpace_relativeProjFunctor⟩ =>
              (modulePullback s.site s.base s.containsBase k).obj (s.twistModule Px n).obj)
              (s.representedSpaceMap_comp_fibreToSpaceHom τ f hy).symm) ≪≫
            attachedModuleIsoPullback
              (X := ⟨s.relativeProjFunctor, s.isAlgebraicSpace_relativeProjFunctor⟩)
              (s.twistModule Px n).obj (s.fibreToSpaceHom T f) y
              (e T f n) (s.twistPieceComparison τ rfl y hy n)
```

## Tag 085C, a lemma

[Tag 085C](https://stacks.math.columbia.edu/tag/085C) in the Stacks Project.

**`AlgebraicGeometry.Space.GradedAlgebraPoints.F.baseChangeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjBaseChange.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjBaseChange.lean#L155). The attribute's comment: “the canonical isomorphism r, as the bijection F'(T) ≃ X'(T) ×\_\{X(T)} F(T) of the proof, for every test object; the isomorphism theta of the twists is not stated”.

> **Stacks 085C.** The canonical isomorphism `r : Proj_{X'}(g^*𝒜) ⟶ X' ×_X Proj_X(𝒜)`, on the
> functor of quadruples: for every test object `T` a bijection `F'(T) ≃ X'(T) ×_{X(T)} F(T)`,
> where `F` is the functor of Tag 084A of `𝒜` on `X` and `F'` the one of `g^*𝒜` on `X'`.
>
> A quadruple `(d, f' : T → X', ℒ, ψ)` for `F'` goes to the pair `(f', (d, g ∘ f', ℒ, ψ))`, and a
> pair `(f', (d, f, ℒ, ψ))` goes back to `(d, f', ℒ, ψ)`; the two are mutually inverse.

```lean
def F.baseChangeEquiv (r : GradedAlgebraPoints B S hS X) (g : X' ⟶ X)
    (T : BigFppfOver B S hS) :
    (r.comap g).F T ≃ {p : (yoneda.obj T ⟶ X') × r.F T // F.point r p.2 = p.1 ≫ g}
```

**`AlgebraicGeometry.Space.GradedAlgebraPoints.F.baseChangeEquiv_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjBaseChange.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjBaseChange.lean#L167). The attribute's comment: “the map r sends a quadruple (d, f', L, psi) to the pair (f', (d, g f', L, psi))”.

> **Stacks 085C, the map `r` on a quadruple.** A quadruple `(d, f', ℒ, ψ)` of positive degree
> for `g^*𝒜` goes to the `X'`-point `f'` together with the quadruple `(d, g ∘ f', ℒ, ψ)`
> for `𝒜`.

```lean
theorem F.baseChangeEquiv_mk (r : GradedAlgebraPoints B S hS X) (g : X' ⟶ X)
    (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X') {d : ℤ} (hd : 0 < d)
    (P : (r.comap g).Quadruples T f d) :
    F.baseChangeEquiv r g T (F.mk (r.comap g) f hd P) =
      ⟨(f, F.mk r (f ≫ g) hd P), rfl⟩
```

**`AlgebraicGeometry.Space.GradedAlgebraPoints.F.baseChangeEquiv_symm_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjBaseChange.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjBaseChange.lean#L178). The attribute's comment: “the inverse of r sends (f', (d, g f', L, psi)) to the quadruple (d, f', L, psi)”.

> **Stacks 085C, the inverse of `r`.** The `X'`-point `f'` together with a quadruple
> `(d, g ∘ f', ℒ, ψ)` for `𝒜` of positive degree goes back to the quadruple `(d, f', ℒ, ψ)`
> for `g^*𝒜`.

```lean
theorem F.baseChangeEquiv_symm_mk (r : GradedAlgebraPoints B S hS X) (g : X' ⟶ X)
    (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X') {d : ℤ} (hd : 0 < d)
    (P : (r.comap g).Quadruples T f d) :
    (F.baseChangeEquiv r g T).symm ⟨(f, F.mk r (f ≫ g) hd P), rfl⟩ =
      F.mk (r.comap g) f hd P
```

**`AlgebraicGeometry.Space.RelativeProjPoints.fibreBaseChangeTheta`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjBaseChangePoints.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjBaseChangePoints.lean#L375). The attribute's comment: “the isomorphism theta over a scheme point f : T -> X' of X': an isomorphism of Z-graded algebras from the inverse image, along the base change of r to T (toScheme\_map\_pointEquivOver\_baseChangeIso), of (+)\_\{d in Z} O(d) on T x\_X Proj\_X(A) to (+)\_\{d in Z} O(d) on T x\_\{X'} Proj\_\{X'}(g^*A), both being Tag 084D's twists of Tag 01NR; theta as a map of sheaves on the algebraic space Proj\_\{X'}(g^*A) needs those twists on the space, i.e. 084B”.

> **Stacks 085C, the isomorphism `θ`, over a scheme point of `X'`.**
>
> The inverse image, along the base change `r_T` of
> `AlgebraicGeometry.Space.RelativeProjPoints.fibreBaseChangeIso`, of the sheaf of `ℤ`-graded
> algebras `⨁_{d ∈ ℤ} 𝒪(d)` on `T ×_X Proj_X(𝒜)` is the sheaf of `ℤ`-graded algebras
> `⨁_{d ∈ ℤ} 𝒪(d)` on `T ×_{X'} Proj_{X'}(g^*𝒜)`.
>
> The two twist algebras are Stacks 084D's, in the form
> `AlgebraicGeometry.Space.RelativeProjPoints.fibreTwistAlgebra`, so they are the twists of
> Stacks 01NR of the two restricted algebras; those restricted algebras are equal, and `r` is the
> isomorphism of the presented schemes that equality produces, so `θ` is
> `AlgebraicGeometry.Space.RelativeProjPoints.thetaOfAlgebraEq`.  That `fibreBaseChangeIso` is the
> base change of the isomorphism of algebraic spaces `r` is
> `AlgebraicGeometry.Space.RelativeProjBaseChangePoints.toScheme_map_pointEquivOver_baseChangeIso`;
> the compatibility of `θ` with `ψ` is `AlgebraicGeometry.Space.RelativeProjPoints.pointPsiHom_heq`.
> The source's `θ` on the algebraic space `Proj_{X'}(g^*𝒜)` itself needs the twists of Stacks 084D
> as sheaves on the space, which need Stacks 084B; see the module docstring.

```lean
def fibreBaseChangeTheta (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X') :
    pbAlgS (fibreBaseChangeIso d d' g halg T f).hom (d.fibreTwistAlgebra T (f ≫ g)) ≅
      d'.fibreTwistAlgebra T f
```

**`AlgebraicGeometry.Space.RelativeProjPoints.pointPsiHom_heq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjBaseChangePoints.lean, line 551](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjBaseChangePoints.lean#L551). The attribute's comment: “theta is compatible with psi: over a scheme point f : T -> X' the canonical homomorphism psi : pi\_T^*(f^*g^*A) -> (+)\_n O(n) of Tag 084D for Proj\_\{X'}(g^*A) is the one for Proj\_X(A) at f g, across the identification of the two restricted algebras”.

> **Stacks 085C: `θ` is compatible with `ψ`, over the scheme points of `X'`.**  Over a
> `T`-point `f` of `X'`, the canonical homomorphism of graded algebras
> `ψ : π_T^*(f^*g^*𝒜) ⟶ ⨁_{n ∈ ℤ} 𝒪(n)` of Stacks 084D for `Proj_{X'}(g^*𝒜)`
> (`AlgebraicGeometry.Space.RelativeProjPoints.pointPsiHom`) is the one for `Proj_X(𝒜)` at the
> image point `f ∘ g`, transported along the identification of the two restricted algebras: the
> source's `θ` carries `ψ` to `ψ`.  The graded algebras of twists themselves correspond in the same
> way (`…pointTwistAlgebra_heq`), and so do the identifications `θ` of Stacks 01O3 with every
> further base change (`…pointTwistTheta_heq`) and the `ψ` of Stacks 01NR after it
> (`AlgebraicGeometry.Space.RelativeProjPoints.basePsi_pointTwistTheta`).

```lean
theorem pointPsiHom_heq (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X') :
    HEq (d'.pointPsiHom T f) (d.pointPsiHom T (f ≫ g))
```

**`AlgebraicGeometry.Space.RelativeProjBaseChangePoints.baseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjBaseChangePoints.lean, line 687](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjBaseChangePoints.lean#L687). The attribute's comment: “the canonical isomorphism r : Proj\_\{X'}(g^*A) -> X' x\_X Proj\_X(A), as an isomorphism of presheaves on the big fppf site (that is, of algebraic spaces), natural in the test object; Proj\_X(A) and Proj\_\{X'}(g^*A) are given by Stacks 084B's presentations over the scheme points of the base, Proj\_X(A) not being constructed from A in this library (084B)”.

> **Stacks 085C, the canonical isomorphism `r : Proj_{X'}(g^*𝒜) ⟶ X' ×_X Proj_X(𝒜)`, as an
> isomorphism of algebraic spaces.**
>
> Let `g : X' ⟶ X` be a morphism of algebraic spaces over `S`, let `π : P ⟶ X` be presented as
> `Proj_X(𝒜)` and `π' : P' ⟶ X'` as its base change `Proj_{X'}(g^*𝒜)` in the sense of
> `AlgebraicGeometry.Space.RelativeProjBaseChangePoints`.  Then `P'` is isomorphic to the fibre
> product `X' ×_X P` as a presheaf on the big fppf site of `S`, that is, as an algebraic space.  At
> a test object `T` the isomorphism is the bijection
> `AlgebraicGeometry.Space.RelativeProjPoints.basePointEquivPullback`, which over a `T`-point `f` of
> `X'` sends a point of `P'` to the point of `P` over `f ∘ g` that the two identifications of
> Stacks 084B at `f` attach to it — the source's proof builds `r` on the values of the functors in
> the same way — and its naturality in the test object is
> `AlgebraicGeometry.Space.RelativeProjBaseChangePoints.basePointEquivPullback_restrict`.
>
> The relative Proj of an algebraic space is presented here, as for Stacks 084D, 085D and 085F,
> through its base changes to the scheme points of the base: the space `Proj_X(𝒜)` itself is not
> constructed from `𝒜` in this library, because Stacks 084B is not proved.

```lean
def baseChangeIso : P' ≅ pullback g π
```

**`AlgebraicGeometry.Space.RelativeProjBaseChangePoints.baseChangeIso_hom_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjBaseChangePoints.lean, line 713](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjBaseChangePoints.lean#L713). The attribute's comment: “r is an isomorphism over X': followed by the first projection X' x\_X Proj\_X(A) -> X' it is the structure morphism of Proj\_\{X'}(g^*A)”.

> **Stacks 085C: `r` is a morphism over `X'`.**  The isomorphism
> `r : Proj_{X'}(g^*𝒜) ⟶ X' ×_X Proj_X(𝒜)` followed by the first projection is the structure
> morphism of `Proj_{X'}(g^*𝒜)`.

```lean
theorem baseChangeIso_hom_fst : h.baseChangeIso.hom ≫ pullback.fst g π = π'
```

**`AlgebraicGeometry.Space.RelativeProjBaseChangePoints.baseChangeIso_hom_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjBaseChangePoints.lean, line 729](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjBaseChangePoints.lean#L729). The attribute's comment: “the description of r over the scheme points of X': over a point f : T -> X' the base change of r is the identification of Proj\_T(f^*g^*A) = T x\_\{X'} Proj\_\{X'}(g^*A) with Proj\_T((g f)^*A) = T x\_X Proj\_X(A) given by Stacks 084B”.

> **Stacks 085C: the description of `r` over the scheme points of `X'`.**  For a `T`-point `f`
> of `X'`, a morphism `r : T' ⟶ T` and a `T'`-point `u` of `P' = Proj_{X'}(g^*𝒜)` over `f ∘ r`, the
> second component of `r(u)` is the point of `P = Proj_X(𝒜)` over `f ∘ g ∘ r` that the
> identifications `Proj_T(f^*g^*𝒜) = T ×_{X'} P'` and `Proj_T((f g)^*𝒜) = T ×_X P` of Stacks 084B
> attach to `u` (`AlgebraicGeometry.Space.RelativeProjPoints.baseChangePointEquiv`).  So over every
> scheme `T` over `X'` the base change of `r` is the identification of the two scheme-level
> relative Projs of one graded algebra, which is how the source describes `r` étale locally; with
> `AlgebraicGeometry.Space.RelativeProjBaseChangePoints.baseChangeIso_hom_unique` it determines
> `r`.

```lean
theorem baseChangeIso_hom_snd (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X')
    {T' : BigFppfOver B S hS} (r : T' ⟶ T)
    (u : {u : yoneda.obj T' ⟶ P' // u ≫ π' = yoneda.map r ≫ f}) :
    u.1 ≫ h.baseChangeIso.hom ≫ pullback.snd g π =
      (baseChangePointEquiv d d' g h.algebra_eq T f r u).1
```

**`AlgebraicGeometry.Space.RelativeProjBaseChangePoints.toScheme_map_pointEquivOver_baseChangeIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjBaseChangePoints.lean, line 774](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjBaseChangePoints.lean#L774). The attribute's comment: “theta is taken across r: over a scheme point f : T -> X' the morphism of schemes T x\_\{X'} Proj\_\{X'}(g^*A) -> T x\_X Proj\_X(A) over T that r induces through the cartesian squares of Stacks 084B is fibreBaseChangeIso, the morphism along which fibreBaseChangeTheta pulls back the twists”.

> **Stacks 085C: the isomorphism `θ` is taken across `r`.**  Over a `T`-point `f` of `X'`, the
> morphism of schemes `T ×_{X'} Proj_{X'}(g^*𝒜) ⟶ T ×_X Proj_X(𝒜)` over `T` that `r` induces
> through the two cartesian squares of Stacks 084B is
> `AlgebraicGeometry.Space.RelativeProjPoints.fibreBaseChangeIso`.  So the isomorphism
> `AlgebraicGeometry.Space.RelativeProjPoints.fibreBaseChangeTheta`, which is stated as an
> isomorphism from the inverse image along `fibreBaseChangeIso` of the twists on `T ×_X Proj_X(𝒜)`,
> is the base change to `T` of the source's `θ : r^* pr₂^*(⨁_d 𝒪(d)) ⟶ ⨁_d 𝒪(d)`.

```lean
theorem toScheme_map_pointEquivOver_baseChangeIso (T : BigFppfOver B S hS)
    (f : yoneda.obj T ⟶ X') :
    (BigFppfOver.toScheme B S hS).map
        (d.pointEquivOver T (f ≫ g) (d'.fibreHom T f)
          ⟨d'.fibreToSpace T f ≫ h.baseChangeIso.hom ≫ pullback.snd g π,
            h.fibreToSpace_baseChangeIso_snd_comp T f⟩).1 =
      (fibreBaseChangeIso d d' g h.algebra_eq T f).hom
```

**`AlgebraicGeometry.Space.RelativeProjSituation.relativeProjBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/BaseChange.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/BaseChange.lean#L170). The attribute's comment: “the isomorphism r on the constructed relative Proj: Proj\_\{X'}(g^*A) ≅ X' x\_X Proj\_X(A), over X' and compatible with the projections”.

> **Stacks 085C, the isomorphism `r : Proj_{X'}(g^*𝒜) ⟶ X' ×_X Proj_X(𝒜)`**, for a morphism
> `g : X' ⟶ X` of algebraic spaces over `S` and the quasi-coherent graded `𝒪_X`-algebra `𝒜` of
> Situation 0849: an isomorphism of algebraic spaces from the relative Proj of `g^*𝒜` on `X'`
> (`relativeProjFunctor` of `s.pullback g`) to the fibre product of `g` and the structure morphism
> `Proj_X(𝒜) ⟶ X`.  It is an isomorphism over `X'` (`relativeProjBaseChangeIso_hom_fst`) and its
> second component is `relativeProjBaseChangeHom`, which sends the class of a quadruple
> `(d', f', ℒ', ψ')` to the class of `(d', g ∘ f', ℒ', ψ')`
> (`relativeProjBaseChangeIso_hom_snd`).

```lean
def relativeProjBaseChangeIso :
    (s.pullback g).relativeProjFunctor ≅ Limits.pullback g.hom s.relativeProjπ
```

**`AlgebraicGeometry.Space.RelativeProjSituation.relativeProjBaseChangeIso_hom_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/BaseChange.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/BaseChange.lean#L178). The attribute's comment: “r is an isomorphism over X', on the constructed relative Proj: r followed by the first projection X' x\_X Proj\_X(A) -> X' is the structure morphism Proj\_\{X'}(g^*A) -> X'”.

> **`r` is an isomorphism over `X'`.**

```lean
theorem relativeProjBaseChangeIso_hom_fst :
    (s.relativeProjBaseChangeIso g).hom ≫ Limits.pullback.fst g.hom s.relativeProjπ =
      (s.pullback g).relativeProjπ
```

**`AlgebraicGeometry.Space.RelativeProjSituation.relativeProjBaseChangeIso_hom_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/BaseChange.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/BaseChange.lean#L187). The attribute's comment: “r on the constructed relative Proj sends the class of a quadruple (d', f', L', psi') to (f', (d', g f', L', psi')): followed by the second projection it is the morphism Proj\_\{X'}(g^*A) -> Proj\_X(A) of quadruples”.

> **The second component of `r` is the morphism `(d', f', ℒ', ψ') ↦ (d', g ∘ f', ℒ', ψ')`.**

```lean
theorem relativeProjBaseChangeIso_hom_snd :
    (s.relativeProjBaseChangeIso g).hom ≫ Limits.pullback.snd g.hom s.relativeProjπ =
      s.relativeProjBaseChangeHom g
```

**`AlgebraicGeometry.Space.RelativeProjSituation.baseChangeTwistGradedAlgebraIsoOfPresentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjTwistDescent/BaseChangeThetaAlgebra.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjTwistDescent/BaseChangeThetaAlgebra.lean#L363). The attribute's comment: “theta for every presentation X = U/R of X (and X' = U'\_0/R'\_0 of X'), the twists of Proj\_\{X'}(g^*A) descended along the presentation of X' over U'\_0 x\_X U: the isomorphism r^* pr\_2^* (+)\_\{d in Z} O\_\{Proj\_X(A)}(d) -> (+)\_\{d in Z} O\_\{Proj\_\{X'}(g^*A)}(d) of Z-graded O\_\{Proj\_\{X'}(g^*A)}-algebras”.

> **Stacks 085C, the isomorphism `θ` of graded algebras, for any presentations of `X` and
> `X'`.**  For a presentation `X = U/R` the twists `𝒪_P(d)` of `P = Proj_X(𝒜)` are descended along
> it, and those of `P' = Proj_{X'}(g^*𝒜)` along the presentation `X' = U'/R'` with
> `U' = U'₀ ×_X U` obtained from any presentation `X' = U'₀/R'₀`
> (`AlgebraicGeometry.Space.Presentation.comap`); then
> `θ : r^* pr_2^* (⨁_d 𝒪_P(d)) ≅ ⨁_d 𝒪_{P'}(d)` is an isomorphism of `ℤ`-graded `𝒪_{P'}`-algebras
> (`AlgebraicGeometry.Space.RelativeProjSituation.baseChangeTwistGradedAlgebraIso`),
> with `h = pr_2 ∘ r` the morphism `Proj_{X'}(g^*𝒜) ⟶ Proj_X(𝒜)`.

```lean
def baseChangeTwistGradedAlgebraIsoOfPresentation
    (Px₀ : Presentation s.site s.base s.containsBase X'.obj X'.property) :
    ModulePullbackGradedAlgebraIso (s.relativeProjBaseChangeSpaceHom g) (s.twistGradedAlgebra Px)
      ((s.pullback g).twistGradedAlgebra (Px.comap g.hom Px₀))
```

## Tag 084E, a lemma

[Tag 084E](https://stacks.math.columbia.edu/tag/084E) in the Stacks Project.

**`AlgebraicGeometry.Space.isSeparated_relativeProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProj.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProj.lean#L375). References: EGA II (8.14.1), “more general”.

> **Stacks 084E.** In the relative Proj situation of Stacks 0849, the structure morphism
> `π : Proj_X(𝒜) ⟶ X` is separated.
>
> There is no hypothesis on the graded algebra.  The relative Proj enters through a surjective
> étale scheme chart of `X`, as Stacks 084B presents it.

```lean
theorem isSeparated_relativeProj {X P : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hP : IsAlgebraicSpace B S hS P) (π : P ⟶ X)
    {t : Stacks.RelativeProj.Situation.{u}} (d : RelativeProjChart B S hS π t) :
    IsSeparated B S hS π
```

**`AlgebraicGeometry.Space.isSeparated_relativeProj_of_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjChartSituation.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjChartSituation.lean#L314). The attribute's comment: “for a chart presentation whose chart situation is the restriction of the graded algebra of the space, rather than an unrelated situation on the chart”. References: EGA II (8.14.1), “more general”.

> **Stacks 084E, with the chart situation pinned to `𝒜`.** The structure morphism of the
> relative Proj is separated, with no hypothesis on the graded algebra.
>
> This is `AlgebraicGeometry.Space.isSeparated_relativeProj` read on the chart presentation whose
> situation is the restriction `𝒜|_V`.

```lean
theorem isSeparated_relativeProj_of_chart
    {P : (BigFppfOver s.site s.base s.containsBase)ᵒᵖ ⥤ Type u}
    (hP : IsAlgebraicSpace s.site s.base s.containsBase P) (π : P ⟶ s.space.1)
    (c : RelativeProjSituationChart s π) :
    IsSeparated s.site s.base s.containsBase π
```

**`AlgebraicGeometry.Space.RelativeProjSituation.isSeparated_relativeProjπ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/Separated.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/Separated.lean#L67). References: EGA II (8.14.1), “more general”.

> **Stacks 084E.** In Situation 0849 the structure morphism `π : Proj_X(𝒜) ⟶ X` of the
> relative homogeneous spectrum is separated.
>
> There is no hypothesis on the graded algebra, exactly as in the source. Over a surjective étale
> scheme chart `g : U ⟶ X` the base change of `π` is the scheme-level relative Proj of the
> restriction `g^*𝒜` (Stacks 084B), whose structure morphism is separated (Stacks 01O2), and
> separatedness descends along the chart (Stacks 03KM).

```lean
theorem isSeparated_relativeProjπ :
    IsSeparated s.site s.base s.containsBase s.relativeProjπ
```

## Tag 084F, a lemma

[Tag 084F](https://stacks.math.columbia.edu/tag/084F) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiCompact_relativeProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProj.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProj.lean#L392).

> **Stacks 084F.** In the relative Proj situation of Stacks 0849, the structure morphism
> `π : Proj_X(𝒜) ⟶ X` is quasi-compact if one of the following holds: `𝒜` is of finite type as a
> sheaf of `𝒜₀`-algebras; `𝒜` is generated by `𝒜₁` as an `𝒜₀`-algebra and `𝒜₁` is a finite type
> `𝒜₀`-module; or there is a finite type quasi-coherent `𝒜₀`-submodule `ℱ ⊆ 𝒜₊` such that
> `𝒜₊/ℱ𝒜` is a locally nilpotent sheaf of ideals of `𝒜/ℱ𝒜`.
>
> The relative Proj enters through a surjective étale scheme chart of `X`, as Stacks 084B
> presents it, and the three hypotheses are those of Stacks 07ZX on the restricted algebra living
> on that chart.

```lean
theorem isQuasiCompact_relativeProj {X P : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hP : IsAlgebraicSpace B S hS P) (hX : IsAlgebraicSpace B S hS X) (π : P ⟶ X)
    {t : Stacks.RelativeProj.Situation.{u}} (d : RelativeProjChart B S hS π t)
    (h : t.IsFiniteTypeOverDegreeZero ∨ t.IsFinitelyGeneratedInDegreeOne ∨
      t.HasNilpotentPositiveQuotient) :
    IsQuasiCompact B S hS π
```

**`AlgebraicGeometry.Space.isQuasiCompact_relativeProj_of_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjChartSituation.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjChartSituation.lean#L331). The attribute's comment: “with the three conditions read on the restriction of the graded algebra of the space to the chart, rather than on an unrelated situation on the chart”.

> **Stacks 084F, with the chart situation pinned to `𝒜`.** The structure morphism of the
> relative Proj is quasi-compact as soon as the restriction `𝒜|_V` satisfies one of the three
> conditions of Stacks 07ZX.
>
> The three conditions of the source are affine-local on the base, so for a quasi-coherent graded
> algebra on `X` they hold exactly when they hold for the restriction to a surjective étale chart;
> the version in `StacksFrontier.AlgebraicGeometry.Spaces.RelativeProj` can only state them for a
> situation unrelated to `𝒜`.

```lean
theorem isQuasiCompact_relativeProj_of_chart
    {P : (BigFppfOver s.site s.base s.containsBase)ᵒᵖ ⥤ Type u}
    (hP : IsAlgebraicSpace s.site s.base s.containsBase P) (π : P ⟶ s.space.1)
    (c : RelativeProjSituationChart s π)
    (h : c.situation.IsFiniteTypeOverDegreeZero ∨
      c.situation.IsFinitelyGeneratedInDegreeOne ∨ c.situation.HasNilpotentPositiveQuotient) :
    IsQuasiCompact s.site s.base s.containsBase π
```

**`AlgebraicGeometry.Space.RelativeProjSituation.isQuasiCompact_π`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/QuasiCompact.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/QuasiCompact.lean#L64).

> **Stacks 084F.** In Situation 0849 the structure morphism `π : Proj_X(𝒜) ⟶ X` is
> quasi-compact if, étale locally on `X`, one of the following holds: `𝒜` is of finite type as an
> `𝒜₀`-algebra; `𝒜` is generated by `𝒜₁` as an `𝒜₀`-algebra and `𝒜₁` is a finite type
> `𝒜₀`-module; there is a finite type `𝒜₀`-submodule `ℱ ⊆ 𝒜₊` such that `𝒜₊/ℱ𝒜` is a locally
> nilpotent sheaf of ideals of `𝒜/ℱ𝒜`. Each condition holds at every étale point exactly when it
> holds at one surjective étale point (`holdsAtEtalePoints_isFiniteTypeOverDegreeZero_iff` and its
> siblings in `StacksFrontier.AlgebraicGeometry.Spaces.RelativeProjPoint.EtaleLocalConditions`).

```lean
theorem isQuasiCompact_π
    (h : s.HoldsAtEtalePoints SheafGradedAlgebra.IsFiniteTypeOverDegreeZero ∨
      s.HoldsAtEtalePoints SheafGradedAlgebra.IsFinitelyGeneratedInDegreeOne ∨
      s.HoldsAtEtalePoints SheafGradedAlgebra.HasNilpotentPositiveQuotient) :
    IsQuasiCompact s.site s.base s.containsBase s.π.hom
```

## Tag 084G, a lemma

[Tag 084G](https://stacks.math.columbia.edu/tag/084G) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiniteType_relativeProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProj.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProj.lean#L408).

> **Stacks 084G.** In the relative Proj situation of Stacks 0849, if `𝒜` is of finite type as
> a sheaf of `𝒪_X`-algebras then the structure morphism `π : Proj_X(𝒜) ⟶ X` is of finite type.
>
> The relative Proj enters through a surjective étale scheme chart of `X`, as Stacks 084B
> presents it, and the hypothesis is that of Stacks 07ZY on the restricted algebra living on that
> chart.

```lean
theorem isFiniteType_relativeProj {X P : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hP : IsAlgebraicSpace B S hS P) (hX : IsAlgebraicSpace B S hS X) (π : P ⟶ X)
    {t : Stacks.RelativeProj.Situation.{u}} (d : RelativeProjChart B S hS π t)
    (h : t.IsFiniteType) :
    IsFiniteType B S hS π
```

**`AlgebraicGeometry.Space.isFiniteType_relativeProj_of_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjChartSituation.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjChartSituation.lean#L345). The attribute's comment: “with the finite type condition read on the restriction of the graded algebra of the space to the chart, rather than on an unrelated situation on the chart”.

> **Stacks 084G, with the chart situation pinned to `𝒜`.** The structure morphism of the
> relative Proj is of finite type as soon as the restriction `𝒜|_V` is of finite type as a sheaf of
> algebras.

```lean
theorem isFiniteType_relativeProj_of_chart
    {P : (BigFppfOver s.site s.base s.containsBase)ᵒᵖ ⥤ Type u}
    (hP : IsAlgebraicSpace s.site s.base s.containsBase P) (π : P ⟶ s.space.1)
    (c : RelativeProjSituationChart s π) (h : c.situation.IsFiniteType) :
    IsFiniteType s.site s.base s.containsBase π
```

**`AlgebraicGeometry.Space.RelativeProjSituation.isFiniteType_π`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FiniteType.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/FiniteType.lean#L72).

> **Stacks 084G.** In Situation 0849, if `𝒜` is of finite type as a sheaf of `𝒪_X`-algebras,
> the structure morphism `π : Proj_X(𝒜) ⟶ X` of the relative homogeneous spectrum is of finite
> type.
>
> The hypothesis is read étale locally, on the restriction `g^*𝒜` of Stacks 084B to every étale
> scheme point `g` of `X` (taken through the `u`-small re-presentation of `𝒜`, identified with `𝒜`
> by `smallAlgebraEquiv`); by `holdsAtEtalePoints_isFiniteType_iff` it suffices at one surjective
> étale scheme point.

```lean
theorem isFiniteType_π
    (hft : s.HoldsAtEtalePoints Stacks.AlgebraicGeometry.RelativeProjFiniteType.IsFiniteType) :
    IsFiniteType s.site s.base s.containsBase s.π.hom
```

## Tag 084H, a lemma

[Tag 084H](https://stacks.math.columbia.edu/tag/084H) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeProjSituation.universallyClosed_π`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/UniversallyClosed.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/UniversallyClosed.lean#L76).

> **Stacks 084H.** In Situation 0849, if `𝒪_X → 𝒜₀` is integral and `𝒜` is of finite type as
> an `𝒜₀`-algebra, the structure morphism `π : Proj_X(𝒜) ⟶ X` of the relative homogeneous spectrum
> is universally closed.
>
> Both hypotheses are read étale locally, on the restriction `g^*𝒜` of Stacks 084B to every étale
> scheme point `g` of `X` (taken through the `u`-small re-presentation of `𝒜`, identified with `𝒜`
> by `smallAlgebraEquiv`); by `holdsAtEtalePoints_isIntegralInDegreeZero_iff` and
> `holdsAtEtalePoints_isFiniteTypeOverDegreeZero_iff` it suffices at one surjective étale scheme
> point.

```lean
theorem universallyClosed_π
    (hint : s.HoldsAtEtalePoints SheafGradedAlgebra.IsIntegralInDegreeZero)
    (hft : s.HoldsAtEtalePoints SheafGradedAlgebra.IsFiniteTypeOverDegreeZero) :
    UniversallyClosed s.site s.base s.containsBase s.π.hom
```

**`AlgebraicGeometry.Space.universallyClosed_relativeProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjUniversallyClosed.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjUniversallyClosed.lean#L125).

> **Stacks 084H.** In the relative Proj situation of Stacks 0849, if the structure sheaf maps
> integrally into `𝒜₀` and `𝒜` is of finite type as an `𝒜₀`-algebra, then the structure morphism
> `π : Proj_X(𝒜) ⟶ X` is universally closed.
>
> The relative Proj enters through a surjective étale scheme chart of `X`, as Stacks 084B
> presents it, and the two hypotheses are the hypotheses of Stacks 07ZZ on the restricted algebra
> living on that chart. Universal closedness is étale local on the target — the leg used is
> `AlgebraicGeometry.Space.universallyClosed_of_etale_atlas` of Stacks 03IT — so the conclusion
> follows from the case of schemes, which is
> `Stacks.RelativeProj.Situation.universallyClosed_relativeProjToBase_of_isIntegralInDegreeZero`.

```lean
theorem universallyClosed_relativeProj {X P : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (π : P ⟶ X)
    {t : Stacks.RelativeProj.Situation.{u}} (d : RelativeProjChart B S hS π t)
    (hint : t.IsIntegralInDegreeZero) (hft : t.IsFiniteTypeOverDegreeZero) :
    UniversallyClosed B S hS π
```

## Tag 084I, a lemma

[Tag 084I](https://stacks.math.columbia.edu/tag/084I) in the Stacks Project.

**`Stacks.RelativeProj.Situation.properFiniteType_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProj/FiniteTypeConditions.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProj/FiniteTypeConditions.lean#L176). The attribute's comment: “the equivalence of the two finite-type conditions, both read over every affine open of the base”.

> **Stacks 084I.** For a relative `Proj` situation the two finite type conditions are
> equivalent: that the degree-zero part of the graded algebra is a finite type module over the
> structure sheaf and the graded algebra is of finite type over its degree-zero part, and that the
> degree-zero part is a finite type module over the structure sheaf and the graded algebra is of
> finite type over the structure sheaf.

```lean
theorem properFiniteType_tfae :
    List.TFAE
      [s.IsDegreeZeroFiniteType ∧ s.IsFiniteTypeOverDegreeZero,
        s.IsDegreeZeroFiniteType ∧ s.IsFiniteTypeOverBase]
```

**`AlgebraicGeometry.Space.RelativeProjSituation.properFiniteType_tfae_and_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFiniteTypeConditions.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjFiniteTypeConditions.lean#L234). The attribute's comment: “both assertions for Situation 0849: the equivalence of the two finite-type conditions, with finite type of A\_0 the finite type O\_X-module condition on the small etale site and the two algebra conditions read on the restriction of A to every etale chart, and properness of the structure morphism of the relative Proj under them, the relative Proj entering through its Tag 084B chart presentation on the restriction of A”.

> **Stacks 084I.** In Situation 0849 — `X` an algebraic space over a scheme `S` and `𝒜` a
> quasi-coherent graded `𝒪_X`-algebra — the following conditions are equivalent:
>
> 1. `𝒜₀` is a finite type `𝒪_X`-module and `𝒜` is of finite type as an `𝒜₀`-algebra,
> 2. `𝒜₀` is a finite type `𝒪_X`-module and `𝒜` is of finite type as an `𝒪_X`-algebra;
>
> and if they hold, the structure morphism `π : Proj_X(𝒜) ⟶ X` is proper.
>
> `𝒜₀` being of finite type is `SheafOfModules.IsFiniteTypeOnSite` of the degree-zero piece; the
> two algebra conditions are read on the restriction of `𝒜` to every étale chart.  The relative Proj
> `π : P ⟶ X` is any morphism of algebraic spaces presented, on a surjective étale chart, as the
> relative Proj of the restriction of `𝒜` (Stacks 084B), which is how the source's proof reaches
> the scheme case.

```lean
theorem properFiniteType_tfae_and_isProper :
    List.TFAE
        [SheafOfModules.IsFiniteTypeOnSite (s.algebra.piece 0) ∧ s.IsFiniteTypeOverDegreeZero,
          SheafOfModules.IsFiniteTypeOnSite (s.algebra.piece 0) ∧ s.IsFiniteTypeOverBase] ∧
      (SheafOfModules.IsFiniteTypeOnSite (s.algebra.piece 0) ∧ s.IsFiniteTypeOverDegreeZero →
        ∀ {P : (BigFppfOver s.site s.base s.containsBase)ᵒᵖ ⥤ Type u},
          IsAlgebraicSpace s.site s.base s.containsBase P → ∀ (π : P ⟶ s.space.1),
            RelativeProjSituationChart s π → IsProper s.site s.base s.containsBase π)
```

**`AlgebraicGeometry.Space.RelativeProjSituation.tfae_finiteType_and_isProper_π`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/Proper.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjPoint/Proper.lean#L169).

> **Stacks 084I.** In Situation 0849 — `X` an algebraic space over a scheme `S` and `𝒜` a
> quasi-coherent graded `𝒪_X`-algebra — the following conditions are equivalent:
>
> 1. `𝒜₀` is a finite type `𝒪_X`-module and `𝒜` is of finite type as an `𝒜₀`-algebra,
> 2. `𝒜₀` is a finite type `𝒪_X`-module and `𝒜` is of finite type as an `𝒪_X`-algebra;
>
> and if they hold, the structure morphism `π : Proj_X(𝒜) ⟶ X` of the relative homogeneous
> spectrum of Stacks 084C is proper.
>
> The conditions are read étale locally, on the restriction `g^*𝒜` of Stacks 084B to every étale
> scheme point `g` of `X`, as for Stacks 084G and 084H: `𝒜₀` of finite type is
> `SheafOfModules.IsFiniteType` of the degree-zero piece of `g^*𝒜`, and the two algebra conditions
> are the hypotheses of Stacks 084H and 084G.

```lean
theorem tfae_finiteType_and_isProper_π :
    List.TFAE
        [s.HoldsAtEtalePoints (fun A => SheafOfModules.IsFiniteType (A.piece 0)) ∧
            s.HoldsAtEtalePoints SheafGradedAlgebra.IsFiniteTypeOverDegreeZero,
          s.HoldsAtEtalePoints (fun A => SheafOfModules.IsFiniteType (A.piece 0)) ∧
            s.HoldsAtEtalePoints Stacks.AlgebraicGeometry.RelativeProjFiniteType.IsFiniteType] ∧
      (s.HoldsAtEtalePoints (fun A => SheafOfModules.IsFiniteType (A.piece 0)) ∧
          s.HoldsAtEtalePoints SheafGradedAlgebra.IsFiniteTypeOverDegreeZero →
        IsProper s.site s.base s.containsBase s.π.hom)
```

## Tag 085D, a lemma

[Tag 085D](https://stacks.math.columbia.edu/tag/085D) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeProjPoints.pointEquivF1`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProj.lean, line 744](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProj.lean#L744). The attribute's comment: “part (1): the relative Proj represents the functor of triples, over a point of the base”.

> **Stacks 085D, part (1), fibred over a point of the base.**
>
> For a quasi-coherent graded `𝒪_X`-algebra `𝒜` generated as an `𝒜₀`-algebra by `𝒜₁`, and
> `P = Proj_X(𝒜)`, the `T'`-points of `P` lying over a point `f` of `X` at `T` are the
> isomorphism classes of pairs `(ℒ, ψ)` with `ℒ` invertible on the scheme of `T'` and
> `ψ : f^*𝒜 ⟶ ⨁_{n ≥ 0} ℒ^{⊗ n}` a graded algebra map surjective in degree one — that is, the
> triples `(f ∘ r, ℒ, ψ)` of the functor `F₁`.
>
> The relative Proj enters through its base changes to schemes, as Stacks 084B presents them, and
> the scheme-level representing bijections of Stacks 01O4 are the hypothesis `rep`; the degree-one
> generation hypothesis of the source is `hgen`.

```lean
noncomputable def pointEquivF1 (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X)
    {T' : BigFppfOver B S hS} (r : T' ⟶ T) :
    {u : yoneda.obj T' ⟶ P // u ≫ π = yoneda.map r ≫ f} ≃
      F1 (d.algebra T f) TA ((BigFppfOver.toScheme B S hS).map r)
```

**`AlgebraicGeometry.Space.RelativeProjPoints.pointEquivF1_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProj.lean, line 765](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProj.lean#L765). The attribute's comment: “part (1): naturality of the representing bijection in the test object”.

> **Stacks 085D, part (1): the representing bijection is natural in the test object.**
>
> Restricting a `T'`-point of `P` along `r' : T'' ⟶ T'` pulls back the class of triples it
> represents.

```lean
theorem pointEquivF1_natural (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X)
    {T' T'' : BigFppfOver B S hS} (r : T' ⟶ T) (r' : T'' ⟶ T')
    (u : {u : yoneda.obj T' ⟶ P // u ≫ π = yoneda.map r ≫ f}) :
    d.pointEquivF1 TA i hgen rep T f (r' ≫ r) ⟨yoneda.map r' ≫ u.1, by
        rw [Category.assoc, u.2, ← Category.assoc, ← CategoryTheory.Functor.map_comp]⟩
      = (rep T f).pullbackClass ((BigFppfOver.toScheme B S hS).map r')
          (d.pointEquivF1 TA i hgen rep T f r u)
```

**`AlgebraicGeometry.Space.RelativeProjPoints.homEquivF1`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProj.lean, line 785](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProj.lean#L785). The attribute's comment: “part (1): the relative Proj represents the functor of triples”.

> **Stacks 085D, part (1).** The `T`-points of `P = Proj_X(𝒜)` are the isomorphism classes of
> triples `(f, ℒ, ψ)` of the functor `F₁`: a point `f` of `X` at `T`, an invertible module `ℒ` on
> the scheme of `T`, and a graded algebra map `f^*𝒜 ⟶ ⨁_{n ≥ 0} ℒ^{⊗ n}` surjective in degree one.
>
> The decomposition of a point of `P` by its image in `X` matches the decomposition of a triple by
> its first component, and over each point of `X` the two fibres agree by
> `AlgebraicGeometry.Space.RelativeProjPoints.pointEquivF1`.

```lean
noncomputable def homEquivF1 (T : BigFppfOver B S hS) :
    (yoneda.obj T ⟶ P) ≃ Σ f : yoneda.obj T ⟶ X, F1 (d.algebra T f) TA (𝟙 _)
```

**`AlgebraicGeometry.Space.RelativeProjSituation.relativeProjIsoF1OfGenerated`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjF1Generated.lean, line 442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjF1Generated.lean#L442). The attribute's comment: “part (1), on the constructed relative Proj: for a quasi-coherent graded O\_X-algebra A on an algebraic space X generated as an A\_0-algebra by A\_1 (over every affine object V of the small etale site of X, the ring of sections of A over V is generated by its degree-one part over its degree-zero part), the relative Proj P = relativeProjFunctor of Tags 084A-084B represents the functor F\_1 of isomorphism classes of triples (f : T -> X, L invertible on T, psi : f^*A -> ⨁\_\{n >= 0} L^\{tensor n} a map of graded O\_T-algebras surjective in degree one), as a natural isomorphism of functors on the big fppf site; F\_1 is functorial by pullback of triples (relativeProjF1Functor)”.

> **Stacks 085D, part (1), on the constructed relative Proj.** For a quasi-coherent graded
> `𝒪_X`-algebra `𝒜` on an algebraic space `X` generated as an `𝒜₀`-algebra by `𝒜₁`
> (`RelativeProjSituation.IsGeneratedInDegreeOne`: over every affine étale chart `V` of `X` the
> sections `⨁ₙ 𝒜ₙ(V)` are generated by `𝒜₁(V)` over `𝒜₀(V)`), the relative homogeneous spectrum
> `P = Proj_X(𝒜)` constructed in Stacks 084A–084B represents the functor `F₁` which sends `T` to
> the isomorphism classes of triples `(f, ℒ, ψ)`: `f : T → X`, `ℒ` an invertible `𝒪_T`-module, and
> `ψ : f^*𝒜 ⟶ ⨁_{n ≥ 0} ℒ^{⊗ n}` a map of graded `𝒪_T`-algebras inducing a surjection
> `f^*𝒜₁ ⟶ ℒ`.
>
> `F₁` is `relativeProjF1Functor`, functorial by pullback of triples; the isomorphism is inverse to
> the natural map `f1ToRelativeProj` sending a triple to the point of `P` it classifies (`P` is
> lifted to the universe of `F₁`). `TA` is the choice of tensor algebras needed to write
> `⨁_{n ≥ 0} ℒ^{⊗ n}`. It is `relativeProjIsoF1`, whose hypothesis on the restrictions of `𝒜` to
> the étale charts follows from generation of `𝒜` itself
> (`IsGeneratedInDegreeOne.isGeneratedInDegreeOneOnCharts`).

```lean
def relativeProjIsoF1OfGenerated (hgen : s.IsGeneratedInDegreeOne) :
    s.relativeProjFunctor ⋙ uliftFunctor.{u + 1} ≅ s.relativeProjF1Functor TA
```

**`AlgebraicGeometry.Space.RelativeProjPoints.pointEquivF1OfGenerated`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjRepresentsGenerated.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjRepresentsGenerated.lean#L196). The attribute's comment: “part (1), over a point of the base: for a quasi-coherent graded O\_X-algebra A generated as an A\_0-algebra by A\_1 and P = Proj\_X(A), the T'-points of P lying over a T-point f of X are in bijection with the strict isomorphism classes of pairs (L, psi) -- L invertible on the scheme of T' and psi : f^*A -> ⨁\_\{n >= 0} L^\{tensor n} a graded algebra map surjective in degree one -- that is, with the triples (f . r, L, psi) of F\_1 over f. The scheme-level representing bijections of Stacks 01O4 are proved from the degree-one generation, by ProjRepresentsF1.f1Bundle. P is given, as throughout this library's relative Proj of algebraic spaces, by its base changes T x\_X P = Proj\_T(f^*A) to the scheme points of X (RelativeProjPoints, the second assertion of Stacks 084B); TA is the choice of tensor algebras needed to write ⨁\_\{n >= 0} L^\{tensor n}. Parts (2) and (3) are epi\_psiTranspose\_pointTwistData\_one, isInvertible\_pointTwist and isIso\_mulSheaf\_pointTwistAlgebra”.

> **Stacks 085D, part (1), fibred over a point of the base.**
>
> For a quasi-coherent graded `𝒪_X`-algebra `𝒜` generated as an `𝒜₀`-algebra by `𝒜₁` and
> `P = Proj_X(𝒜)`, the `T'`-points of `P` lying over a point `f` of `X` at `T` are the strict
> isomorphism classes of pairs `(ℒ, ψ)` with `ℒ` invertible on the scheme of `T'` and
> `ψ : f^*𝒜 ⟶ ⨁_{n ≥ 0} ℒ^{⊗ n}` a graded algebra map surjective in degree one — that is, the
> triples `(f ∘ r, ℒ, ψ)` of the functor `F₁`.
>
> The relative Proj enters through its base changes to schemes, which is what Stacks 084B supplies
> and all the source's proof uses.  The degree-one generation hypothesis `hgen` is the source's
> own, and it is the only hypothesis: the scheme-level representing bijections of Stacks 01O4 are
> built from it by `Stacks.AlgebraicGeometry.ProjRepresentsF1.f1Bundle`, not assumed.

```lean
noncomputable def pointEquivF1OfGenerated (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X)
    {T' : BigFppfOver B S hS} (r : T' ⟶ T) :
    {u : yoneda.obj T' ⟶ P // u ≫ π = yoneda.map r ≫ f} ≃
      F1 (d.algebra T f) TA ((BigFppfOver.toScheme B S hS).map r)
```

**`AlgebraicGeometry.Space.RelativeProjPoints.pointEquivF1OfGenerated_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjRepresentsGenerated.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjRepresentsGenerated.lean#L213). The attribute's comment: “part (1), naturality of the representing bijection in the test object, under degree-one generation alone: restricting a T'-point of P along r' : T'' -> T' pulls back the class of triples it represents, along the pullback-of-classes operation of the scheme-level bijections that ProjRepresentsF1.f1Bundle builds from the degree-one generation”.

> **Stacks 085D, part (1): the representing bijection is natural in the test object.**
>
> Restricting a `T'`-point of `P` along `r' : T'' ⟶ T'` pulls back the class of triples it
> represents.  Only the degree-one generation hypothesis of the source enters; the scheme-level
> naturality it is read off is that of
> `Stacks.AlgebraicGeometry.ProjRepresentsF1.f1Bundle`.

```lean
theorem pointEquivF1OfGenerated_natural (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X)
    {T' T'' : BigFppfOver B S hS} (r : T' ⟶ T) (r' : T'' ⟶ T')
    (u : {u : yoneda.obj T' ⟶ P // u ≫ π = yoneda.map r ≫ f}) :
    d.pointEquivF1OfGenerated TA hgen T f (r' ≫ r) ⟨yoneda.map r' ≫ u.1, by
        rw [Category.assoc, u.2, ← Category.assoc, ← CategoryTheory.Functor.map_comp]⟩
      = (f1Bundle (d.algebra T f) TA (hgen T f)).pullbackClass
          ((BigFppfOver.toScheme B S hS).map r')
          (d.pointEquivF1OfGenerated TA hgen T f r u)
```

**`AlgebraicGeometry.Space.RelativeProjPoints.homEquivF1OfGenerated`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjRepresentsGenerated.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjRepresentsGenerated.lean#L243). The attribute's comment: “part (1): for a quasi-coherent graded O\_X-algebra A generated as an A\_0-algebra by A\_1, the T-points of P = Proj\_X(A) are in bijection with the strict isomorphism classes of triples (f, L, psi) of the functor F\_1 -- a T-point f of X, an invertible module L on the scheme of T, and a graded algebra map f^*A -> ⨁\_\{n >= 0} L^\{tensor n} surjective in degree one. The scheme-level representing bijections of Stacks 01O4 are proved from the degree-one generation, by ProjRepresentsF1.f1Bundle. P is given by its base changes T x\_X P = Proj\_T(f^*A) to the scheme points of X (RelativeProjPoints, the second assertion of Stacks 084B). F\_1 is given fibred over the points of X, with its functoriality in the test object over each point (pointEquivF1OfGenerated\_natural), because RelativeProjPoints does not record the comparison g^*(f^*A) = (f . g)^*A between restrictions at different points”.

> **Stacks 085D, part (1).** For a quasi-coherent graded `𝒪_X`-algebra `𝒜` generated as an
> `𝒜₀`-algebra by `𝒜₁`, the `T`-points of `P = Proj_X(𝒜)` are the strict isomorphism classes of
> triples `(f, ℒ, ψ)` of the functor `F₁`: a point `f` of `X` at `T`, an invertible module `ℒ` on
> the scheme of `T`, and a graded algebra map `f^*𝒜 ⟶ ⨁_{n ≥ 0} ℒ^{⊗ n}` surjective in degree one.
>
> The decomposition of a point of `P` by its image in `X` matches the decomposition of a triple by
> its first component, and over each point of `X` the two fibres agree by
> `AlgebraicGeometry.Space.RelativeProjPoints.pointEquivF1OfGenerated`.  Degree-one generation is
> the only hypothesis.

```lean
noncomputable def homEquivF1OfGenerated (T : BigFppfOver B S hS) :
    (yoneda.obj T ⟶ P) ≃ Σ f : yoneda.obj T ⟶ X, F1 (d.algebra T f) TA (𝟙 _)
```

**`AlgebraicGeometry.Space.RelativeProjPoints.epi_psiTranspose_pointTwistData_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjRepresentsGenerated.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjRepresentsGenerated.lean#L270). The attribute's comment: “part (2): for a quasi-coherent graded O\_X-algebra A generated as an A\_0-algebra by A\_1 and P = Proj\_X(A), the canonical map pi^*A\_1 -> O\_P(1) is surjective, at every scheme point f : T -> X of the base: the transpose pi\_T^*(f^*A)\_1 -> O(1) of the degree-one component of psi on T x\_X P = Proj\_T(f^*A) is an epimorphism of sheaves of modules”.

> **Stacks 085D, part (2).**  For a quasi-coherent graded `𝒪_X`-algebra `𝒜` generated as an
> `𝒜₀`-algebra by `𝒜₁` and `P = Proj_X(𝒜)`, the canonical map `π^*𝒜₁ ⟶ 𝒪_P(1)` is surjective:
> after base change to any scheme point `f : T ⟶ X` of the base it is the transpose
> `π_T^*(f^*𝒜)₁ ⟶ 𝒪(1)` of the degree-one component of `ψ` on `Proj_T(f^*𝒜)`, and that is an
> epimorphism by `Stacks.AlgebraicGeometry.RelativeProjDegreeOne.epi_psiTranspose`.

```lean
theorem epi_psiTranspose_pointTwistData_one (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X) :
    Epi (Stacks.AlgebraicGeometry.RelativeProjDegreeOne.psiTranspose (d.pointTwistData T f) 1)
```

**`AlgebraicGeometry.Space.RelativeProjPoints.isInvertible_pointTwist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjRepresentsGenerated.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjRepresentsGenerated.lean#L283). The attribute's comment: “part (3), invertibility: for a quasi-coherent graded O\_X-algebra A generated as an A\_0-algebra by A\_1 and P = Proj\_X(A), every O\_P(n), n in Z, is an invertible module, at every scheme point f : T -> X of the base: the twist O(n) on T x\_X P = Proj\_T(f^*A) is invertible”.

> **Stacks 085D, part (3), invertibility.**  For a quasi-coherent graded `𝒪_X`-algebra `𝒜`
> generated as an `𝒜₀`-algebra by `𝒜₁` and `P = Proj_X(𝒜)`, each twist `𝒪_P(n)` is invertible:
> after base change to any scheme point `f : T ⟶ X` of the base it is the twist `𝒪(n)` of
> `Proj_T(f^*𝒜)`, which is invertible by Stacks 01O4,
> `Stacks.AlgebraicGeometry.TwistMapsInvertible.twistDataOfGradedAlgebra_isInvertible`.

```lean
theorem isInvertible_pointTwist (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X) (n : ℤ) :
    AlgebraicGeometry.SheafOfModules.IsInvertible (relativeProj (d.algebra T f)).scheme.presheaf
      (relativeProj (d.algebra T f)).scheme.ringCatSheaf.2 (d.pointTwist T f n)
```

**`AlgebraicGeometry.Space.RelativeProjPoints.isIso_mulSheaf_pointTwistAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjRepresentsGenerated.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjRepresentsGenerated.lean#L298). The attribute's comment: “part (3), multiplication: for a quasi-coherent graded O\_X-algebra A generated as an A\_0-algebra by A\_1 and P = Proj\_X(A), the multiplication maps O\_P(n) (x) O\_P(m) -> O\_P(n+m) are isomorphisms for all integers n, m, at every scheme point f : T -> X of the base: the multiplication of the twists on T x\_X P = Proj\_T(f^*A) is an isomorphism in all degrees”.

> **Stacks 085D, part (3), multiplication.**  For a quasi-coherent graded `𝒪_X`-algebra `𝒜`
> generated as an `𝒜₀`-algebra by `𝒜₁` and `P = Proj_X(𝒜)`, the multiplication maps induce
> isomorphisms `𝒪_P(n) ⊗_{𝒪_P} 𝒪_P(m) ⟶ 𝒪_P(n + m)` for all integers `n` and `m`: after base
> change to any scheme point `f : T ⟶ X` of the base they are the multiplication maps of the twists
> of `Proj_T(f^*𝒜)`, which are isomorphisms by Stacks 01O4,
> `Stacks.AlgebraicGeometry.TwistMapsInvertible.isIso_mulSheaf_twistDataOfGradedAlgebra`.

```lean
theorem isIso_mulSheaf_pointTwistAlgebra (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ X)
    (n m : ℤ) :
    IsIso (_root_.SheafOfModules.GradedAlgebra.mulSheaf (d.pointTwistAlgebra T f) n m)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 71.11, Tag 0848](https://stacks.math.columbia.edu/tag/0848)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
