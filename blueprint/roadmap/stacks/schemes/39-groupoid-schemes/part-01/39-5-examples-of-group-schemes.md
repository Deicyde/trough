---
declaration: section
origin: cited
lean: AlgebraicGeometry.multiplicativeGroup, AlgebraicGeometry.multiplicativeGroupCanonicallyOver, AlgebraicGeometry.multiplicativeGroupMultiplication, AlgebraicGeometry.unitsOfGlobalSections_representableBy_multiplicativeGroup, AlgebraicGeometry.multiplicativeGroupGrpObj_mul, AlgebraicGeometry.multiplicativeGroupBaseChange, AlgebraicGeometry.multiplicativeGroupBaseChangeGrpObj, AlgebraicGeometry.baseChangePointsIsoMultiplicativeGroupPoints
statement: formalized
proof: formalized
---

# 39.5 Examples of group schemes

Section 39.5 of the Stacks Project, [Tag 047F](https://stacks.math.columbia.edu/tag/047F). 6 tags here are carried by 56 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 022U, an example

[Tag 022U](https://stacks.math.columbia.edu/tag/022U) in the Stacks Project.

**`AlgebraicGeometry.multiplicativeGroup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean#L86). The attribute's comment: “multiplicative\_group\_scheme\_underlying\_scheme”. References: SGA 3 I (4.3.2).

> **Stacks Project, Tag 022U.** The underlying scheme of the multiplicative group over the
> integers is the spectrum of the Laurent polynomial ring `ℤ[T, T⁻¹]`.

```lean
noncomputable abbrev multiplicativeGroup
```

**`AlgebraicGeometry.multiplicativeGroupCanonicallyOver`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean#L90). The attribute's comment: “multiplicative\_group\_scheme\_underlying\_scheme”.

> The canonical structure morphism from the multiplicative group scheme to `Spec ℤ`.

```lean
noncomputable instance multiplicativeGroupCanonicallyOver :
    multiplicativeGroup.CanonicallyOver (Spec (.of ℤ))
```

**`AlgebraicGeometry.multiplicativeGroupMultiplication`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean#L124). The attribute's comment: “multiplication”.

> **Stacks Project, Tag 022U.** Multiplication on the multiplicative group is the scheme
> morphism induced by `T ↦ T ⊗ T` on coordinate rings, after the canonical identification of the
> fibre product with the spectrum of the tensor product.

```lean
noncomputable def multiplicativeGroupMultiplication :
    pullback (multiplicativeGroup ↘ Spec (.of ℤ))
      (multiplicativeGroup ↘ Spec (.of ℤ)) ⟶ multiplicativeGroup
```

**`AlgebraicGeometry.unitsOfGlobalSections_representableBy_multiplicativeGroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean#L219). The attribute's comment: “represents\_units”. References: EGA IV (20.2.8), “Morphisms V → Spec Z[T”; SGA 3 I (4.3.2).

> **Stacks Project, Tag 022U.** The functor assigning to a scheme the units in its ring of
> global sections is represented by the multiplicative group scheme `Spec (ℤ[T, T⁻¹])`.

```lean
theorem unitsOfGlobalSections_representableBy_multiplicativeGroup :
    Nonempty
      ((Scheme.Γ ⋙ forget₂ CommRingCat CommMonCat ⋙ CommMonCat.units ⋙
          forget CommGrpCat).RepresentableBy (multiplicativeGroupULift : Scheme.{u}))
```

**`AlgebraicGeometry.multiplicativeGroupGrpObj_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean, line 263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean#L263). The attribute's comment: “group\_scheme”.

> **Stacks Project, Tag 022U.** Multiplication in the multiplicative group scheme is the
> morphism induced by `T ↦ T ⊗ T` on Laurent polynomial coordinate rings.

```lean
theorem multiplicativeGroupGrpObj_mul :
    μ[multiplicativeGroup.asOver (Spec (.of ℤ))].left =
      multiplicativeGroupMultiplication
```

**`AlgebraicGeometry.multiplicativeGroupBaseChange`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean#L274). The attribute's comment: “base\_change”.

> **Stacks Project, Tag 022U.** The multiplicative group over `S` is the base change of
> `Spec (ℤ[T, T⁻¹])` along the unique morphism from `S` to `Spec ℤ`.

```lean
noncomputable abbrev multiplicativeGroupBaseChange (S : Scheme.{u}) : Scheme.{u}
```

**`AlgebraicGeometry.multiplicativeGroupBaseChangeGrpObj`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean#L446). The attribute's comment: “base\_change”. References: SGA 3 I (4.3.2).

> **Stacks Project, Tag 022U.** The base change of the multiplicative group to any scheme `S`
> is a group scheme over `S`. Its structure is induced by the specified representation of the
> group-valued global-units functor, and hence is not an arbitrary transported group law.

```lean
noncomputable instance multiplicativeGroupBaseChangeGrpObj (S : Scheme.{u}) :
    GrpObj (Scheme.asOver (multiplicativeGroupBaseChange S) S)
```

**`AlgebraicGeometry.baseChangePointsIsoMultiplicativeGroupPoints`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean, line 456](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean#L456). The attribute's comment: “base\_change”.

> **Stacks Project, Tag 022U.** For every `S`-scheme `T`, the universal property of base change
> canonically identifies `S`-morphisms from `T` to the multiplicative group over `S` with scheme
> morphisms from `T` to the integral multiplicative group. The natural isomorphism records
> compatibility with every morphism of `S`-schemes.

```lean
noncomputable def baseChangePointsIsoMultiplicativeGroupPoints (S : Scheme.{u}) :
    yoneda.obj (Scheme.asOver (multiplicativeGroupBaseChange S) S) ≅
      (Over.forget S).op ⋙ yoneda.obj multiplicativeGroupULift
```

**`AlgebraicGeometry.baseChangePointsIsoMultiplicativeGroupPoints_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean, line 490](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean#L490). The attribute's comment: “base\_change”.

> The forward map in `AlgebraicGeometry.baseChangePointsIsoMultiplicativeGroupPoints` is
> composition with the first pullback projection. This characterizes the isomorphism and its
> canonical orientation.

```lean
theorem baseChangePointsIsoMultiplicativeGroupPoints_hom_app
    (S : Scheme.{u}) (T : (Over S)ᵒᵖ)
    (f : T.unop ⟶ Scheme.asOver (multiplicativeGroupBaseChange S) S) :
    (baseChangePointsIsoMultiplicativeGroupPoints S).hom.app T f =
      f.left ≫ pullback.fst
        (multiplicativeGroupULift ↘ Spec (.of (ULift.{u} ℤ)))
        (specULiftZIsTerminal.from S)
```

**`AlgebraicGeometry.baseChangePointsIsoGlobalUnits`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean, line 502](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean#L502). The attribute's comment: “base\_change”. References: SGA 3 I (4.3.2), “G\_\{m,S}(T)=Γ(T,O\_T)^*”.

> **Stacks Project, Tag 022U.** The group of `T`-points of the multiplicative group over `S` is
> canonically the unit group `Γ(T, 𝒪_T)ˣ`, naturally in the `S`-scheme `T`.

```lean
noncomputable def baseChangePointsIsoGlobalUnits (S : Scheme.{u}) :
    yonedaGrpObj (Scheme.asOver (multiplicativeGroupBaseChange S) S) ≅ globalUnits S
```

**`AlgebraicGeometry.baseChangePointsIsoGlobalUnits_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean, line 512](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean#L512). The attribute's comment: “base\_change”.

> The forward map in `AlgebraicGeometry.baseChangePointsIsoGlobalUnits` sends a point to the
> pullback of the Laurent coordinate along its composite with the first pullback projection.
> Besides characterizing the natural isomorphism, this pins down the multiplication on the group
> scheme as multiplication of global units.

```lean
theorem baseChangePointsIsoGlobalUnits_hom_app
    (S : Scheme.{u}) (T : (Over S)ᵒᵖ)
    (f : T.unop ⟶ Scheme.asOver (multiplicativeGroupBaseChange S) S) :
    (baseChangePointsIsoGlobalUnits S).hom.app T f =
    multiplicativeGroupPointUnit
        (f.left ≫ pullback.fst
          (multiplicativeGroupULift ↘ Spec (.of (ULift.{u} ℤ)))
          (specULiftZIsTerminal.from S))
```

Declarations registered for the tag:

- [`LaurentPolynomial.instHopfAlgebra`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LaurentPolynomial.instHopfAlgebra#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean#L225) (StacksFrontier): “group\_scheme”. References: EGA II (8.3.9), “partial, special case”; SGA 3 I (4.3.2), “special case”; SGA 3 VIIA (3.3), “special case”.
- [`AlgebraicGeometry.instGrpObjSpecAsOverSpec`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instGrpObjSpecAsOverSpec#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Multiplicative.lean#L229) (StacksFrontier): “group\_scheme”. References: SGA 3 I (4.2), “partial”; SGA 3 VIIA (3.3), “partial”; SGA 3 VIIA (3.3.0), “partial”; SGA 3 VIIB (2.1), “(i), special case”; SGA 3 VIIB (2.2.1), “partial”.
- [`AlgebraicGeometry.smooth_multiplicativeGroupULift`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/MultiplicativeSmoothDimension.lean#L105), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/MultiplicativeSmooth.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/MultiplicativeSmooth.lean#L51) (StacksFrontier): “the structure morphism is smooth”.

## Tag 040M, an example

[Tag 040M](https://stacks.math.columbia.edu/tag/040M) in the Stacks Project.

**`AlgebraicGeometry.rootsOfUnity`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/RootsOfUnity.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/RootsOfUnity.lean#L96). The attribute's comment: “roots\_of\_unity\_scheme”. References: SGA 3 I (4.4.4), “μ\_n = Spec Z[x]/(x^n-1)”; SGA 1 XI (6.1), “special case”.

> **Stacks Project, Tag 040M.** The scheme of `n`-th roots of unity over the integers is
> `Spec (ℤ[X] / (Xⁿ - 1))`.

```lean
noncomputable abbrev rootsOfUnity (n : ℕ) : Scheme.{u}
```

**`AlgebraicGeometry.rootsOfUnityCanonicallyOver`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/RootsOfUnity.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/RootsOfUnity.lean#L101). The attribute's comment: “roots\_of\_unity\_scheme”.

> The canonical structure morphism from the scheme of roots of unity to the integer base.

```lean
noncomputable instance rootsOfUnityCanonicallyOver (n : ℕ) :
    (rootsOfUnity n).CanonicallyOver (Spec (.of (ULift.{u} ℤ)))
```

**`AlgebraicGeometry.rootsOfUnityBaseChange`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/RootsOfUnity.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/RootsOfUnity.lean#L112). The attribute's comment: “roots\_of\_unity\_scheme”. References: SGA 3 I (4.4.4), “μ\_\{n,S}”; SGA 1 XI (6.1); SGA 3 VIIB (2.5.2.A), “partial”.

> **Stacks Project, Tag 040M.** The scheme of `n`-th roots of unity over `S` is the base change
> of the scheme of roots of unity over the integers along the unique map from `S` to the integer
> base.

```lean
noncomputable abbrev rootsOfUnityBaseChange (n : ℕ) (S : Scheme.{u}) : Scheme.{u}
```

**`AlgebraicGeometry.rootsOfUnitySections_representableBy_rootsOfUnity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/RootsOfUnity.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/RootsOfUnity.lean#L230). The attribute's comment: “representability”. References: SGA 1 XI (6.1), “special case”.

> **Stacks Project, Tag 040M.** The functor of units in global sections whose `n`-th power is
> one is represented by `Spec (ℤ[X] / (Xⁿ - 1))`.

```lean
theorem rootsOfUnitySections_representableBy_rootsOfUnity (n : ℕ) (hn : 0 < n) :
    Nonempty ((rootsOfUnitySections n).RepresentableBy (rootsOfUnity n : Scheme.{u}))
```

**`AlgebraicGeometry.rootsOfUnityGrpObj`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/RootsOfUnity.lean, line 473](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/RootsOfUnity.lean#L473). The attribute's comment: “group\_scheme”. References: SGA 3 I (4.4.4).

> The group-object structure on the scheme of positive-order roots of unity over the
> integers.

```lean
noncomputable instance rootsOfUnityGrpObj (n : ℕ) [Fact (0 < n)] :
    GrpObj (Over.mk (rootsOfUnity n ↘ Spec (.of (ULift.{u} ℤ))))
```

**`AlgebraicGeometry.rootsOfUnityGrpObj_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/RootsOfUnity.lean, line 481](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/RootsOfUnity.lean#L481). The attribute's comment: “group\_scheme”.

> **Stacks Project, Tag 040M.** The scheme of `n`-th roots of unity is a group scheme over
> the integers, with multiplication induced by `X ↦ X ⊗ X` on coordinate rings.

```lean
theorem rootsOfUnityGrpObj_mul (n : ℕ) (hn : 0 < n) :
    (letI : Fact (0 < n) := ⟨hn⟩
    μ[Over.mk (rootsOfUnity n ↘ Spec (.of (ULift.{u} ℤ)))].left =
      rootsOfUnityMultiplication n)
```

**`AlgebraicGeometry.rootsOfUnitySectionsOver_representableBy_rootsOfUnityBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/RootsOfUnity.lean, line 651](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/RootsOfUnity.lean#L651). The attribute's comment: “base\_change\_points”. References: SGA 1 XI (6.1); SGA 3 I (4.4.4); SGA 3 VIIA (4.1.4), “partial”.

> **Stacks Project, Tag 040M.** For every scheme `S`, the base change to `S` of the scheme of
> `n`-th roots of unity represents, naturally in an `S`-scheme `T`, the units in `Γ(T, 𝒪_T)` whose
> `n`-th power is one. The representing universal element is the pullback of the polynomial
> coordinate `X` along the base-change projection.

```lean
theorem rootsOfUnitySectionsOver_representableBy_rootsOfUnityBaseChange
    (n : ℕ) (hn : 0 < n) (S : Scheme.{u}) :
    ((Over.forget S).op ⋙ rootsOfUnitySections n).IsRepresentedBy
      (rootsOfUnityBaseChangeUniversalRoot n hn S)
```

**`AlgebraicGeometry.rootsOfUnityGroupOverFunctor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/RootsOfUnity.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/RootsOfUnity.lean#L73). The attribute's comment: “relative\_functor\_of\_points”. References: SGA 1 XI (6.1); SGA 3 I (4.4.4); SGA 3 VIIA (4.1.4).

> The group-valued functor on schemes over `S` whose value on `T` is the group of `n`-th roots
> of unity in `Γ(T, 𝒪_T)`.

```lean
noncomputable abbrev rootsOfUnityGroupOverFunctor (n : ℕ) (S : Scheme.{u}) :
    (Over S)ᵒᵖ ⥤ GrpCat.{u}
```

**`AlgebraicGeometry.rootsOfUnityBaseChangeOverGrpObj`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/RootsOfUnity.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/RootsOfUnity.lean#L90). The attribute's comment: “base\_change\_group\_scheme”. References: SGA 1 XI (6.1); SGA 3 I (4.4.4); SGA 3 VIIB (2.5.2.A), “more general”.

> **Stacks Project, Tag 040M.** The base change of the group scheme of `n`-th roots of unity
> to a scheme `S` is a group scheme over `S`.

```lean
noncomputable instance rootsOfUnityBaseChangeOverGrpObj (n : ℕ) [Fact (0 < n)]
    (S : Scheme.{u}) : GrpObj (rootsOfUnityBaseChangeOver n S)
```

**`AlgebraicGeometry.rootsOfUnityBaseChangeGroupPointsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/RootsOfUnity.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/RootsOfUnity.lean#L127). The attribute's comment: “relative\_functor\_of\_points”. References: SGA 3 I (4.4.4), “μ\_n(T)=\{f : f^n=1}”; SGA 1 XI (6.1); SGA 3 VIIA (4.1.4), “partial”; SGA 3 VIIB (2.5.2.A), “more general”.

> **Stacks Project, Tag 040M.** For every scheme `S`, the group-valued functor of points of
> the group scheme `μₙ,S` of `n`-th roots of unity is naturally isomorphic to the group of `n`-th
> roots of unity in the global sections of the varying `S`-scheme.

```lean
noncomputable def rootsOfUnityBaseChangeGroupPointsIso (n : ℕ) [Fact (0 < n)] (S : Scheme.{u}) :
    yonedaGrpObj (rootsOfUnityBaseChangeOver n S) ≅ rootsOfUnityGroupOverFunctor n S
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.GrpObjAsOverPullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.GrpObjAsOverPullback#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/RootsOfUnity.lean, line 548](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/RootsOfUnity.lean#L548) (StacksFrontier): “base\_change\_group\_scheme”.
- [`CategoryTheory.Functor.obj.μ_def`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.obj.μ_def#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/RootsOfUnity.lean, line 549](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/RootsOfUnity.lean#L549) (StacksFrontier): “base\_change\_group\_scheme”.

## Tag 022V, an example

[Tag 022V](https://stacks.math.columbia.edu/tag/022V) in the Stacks Project.

**`AlgebraicGeometry.additiveGroup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Additive.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Additive.lean#L83). The attribute's comment: “additive\_group\_underlying\_scheme”. References: SGA 3 I (4.3.1), “the scheme G\_a”.

> **Stacks Project, Tag 022V.** The underlying scheme of the additive group over the integers
> is the spectrum of the polynomial ring `ℤ[X]`.

```lean
noncomputable abbrev additiveGroup : Scheme.{u}
```

**`AlgebraicGeometry.additiveGroupCanonicallyOver`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Additive.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Additive.lean#L88). The attribute's comment: “additive\_group\_underlying\_scheme”.

> The canonical structure morphism from the additive group scheme to the spectrum of the
> universe-polymorphic copy of `ℤ`, induced by the inclusion of constant polynomials.

```lean
noncomputable instance additiveGroupCanonicallyOver :
    additiveGroup.CanonicallyOver (Spec (.of (ULift.{u} ℤ)))
```

**`AlgebraicGeometry.additionMorphism_pullbackSpecIso`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Additive.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Additive.lean#L117). The attribute's comment: “addition\_morphism”. References: SGA 3 I (4.3.1), “Δ(T)=T⊗1+1⊗T”.

> **Stacks Project, Tag 022V.** Under the canonical identification of the fibre product
> with `Spec (R[X] ⊗[R] R[X])`, addition is induced by the ring map sending
> `X` to `X ⊗ 1 + 1 ⊗ X`.

```lean
lemma additionMorphism_pullbackSpecIso :
    (pullbackSpecIso (ULift.{u} ℤ) (Polynomial (ULift.{u} ℤ))
      (Polynomial (ULift.{u} ℤ))).inv ≫ additionMorphism =
      Spec.map (CommRingCat.ofHom additionRingHom)
```

**`AlgebraicGeometry.additiveGroupGrpObj`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Additive.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Additive.lean#L125). The attribute's comment: “additive\_group\_scheme”.

> The group-object structure on the affine line over the integers.

```lean
noncomputable instance additiveGroupGrpObj :
    GrpObj (Over.mk (additiveGroup ↘ Spec (.of (ULift.{u} ℤ))))
```

**`AlgebraicGeometry.additiveGroupGrpObj_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Additive.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Additive.lean#L156). The attribute's comment: “additive\_group\_scheme”.

> **Stacks Project, Tag 022V.** Multiplication in the additive group scheme is the usual
> addition morphism.

```lean
theorem additiveGroupGrpObj_mul :
    μ[Over.mk (additiveGroup ↘ Spec (.of (ULift.{u} ℤ)))].left = additionMorphism
```

**`AlgebraicGeometry.additiveGroupBaseChangeGrpObj`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Additive.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Additive.lean#L167). The attribute's comment: “base\_change\_group\_scheme”. References: SGA 3 I (4.3.1), “G\_\{a,S} group over S”.

> **Stacks Project, Tag 022V.** The base change of the additive group scheme to every scheme
> `S` is a group scheme over `S`, with the canonical pullbacks of the integral group operations.

```lean
noncomputable instance additiveGroupBaseChangeGrpObj (S : Scheme.{u}) :
    GrpObj (Scheme.asOver (additiveGroupBaseChange S) S)
```

**`AlgebraicGeometry.globalSections_representableBy_additiveGroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Additive.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Additive.lean#L380). The attribute's comment: “representability”. References: SGA 3 I (4.3.1), “partial”.

> **Stacks Project, Tag 022V.** The set-valued global-sections functor on schemes is
> represented by the additive group scheme `Spec (ℤ[X])`.

```lean
theorem globalSections_representableBy_additiveGroup :
    Nonempty ((Scheme.Γ ⋙ forget CommRingCat).RepresentableBy (additiveGroup : Scheme.{u}))
```

**`AlgebraicGeometry.additiveGroupBaseChangePointsIsoGlobalSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Additive.lean, line 535](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Additive.lean#L535). The attribute's comment: “relative\_functor\_of\_points”. References: SGA 3 I (4.3.1), “more general”.

> **Stacks Project, Tag 022V.** For every scheme `S`, the group-valued functor of points of
> the additive group scheme over `S` is naturally isomorphic to the additive group of global
> sections of the varying `S`-scheme.

```lean
noncomputable def additiveGroupBaseChangePointsIsoGlobalSections (S : Scheme.{u}) :
    yonedaGrpObj (Scheme.asOver (additiveGroupBaseChange S) S) ≅ globalSectionsAdditive S
```

**`AlgebraicGeometry.additiveGroupBaseChangePointsIsoGlobalSections_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Additive.lean, line 551](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Additive.lean#L551). The attribute's comment: “relative\_functor\_of\_points”.

> Under the canonical identification of additive-group points with global sections, a point is
> sent to the pullback of the universal polynomial coordinate along its projection to the integral
> additive group. This characterizes the natural isomorphism.

```lean
theorem additiveGroupBaseChangePointsIsoGlobalSections_hom_app
    (S : Scheme.{u}) (T : (Over S)ᵒᵖ)
    (f : T.unop ⟶ Scheme.asOver (additiveGroupBaseChange S) S) :
    (additiveGroupBaseChangePointsIsoGlobalSections S).hom.app T f =
      additiveGroupPointSection
        (f.left ≫ pullback.fst
          (additiveGroup ↘ Spec (.of (ULift.{u} ℤ)))
          (specULiftZIsTerminal.from S))
```

## Tag 022W, an example

[Tag 022W](https://stacks.math.columbia.edu/tag/022W) in the Stacks Project.

**`AlgebraicGeometry.generalLinearScheme`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/GeneralLinear.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/GeneralLinear.lean#L97). The attribute's comment: “general\_linear\_scheme”.

> The general linear scheme `GL_n` over the integers.

```lean
noncomputable abbrev generalLinearScheme (n : ℕ) : Scheme.{u}
```

**`AlgebraicGeometry.generalLinearGroup_representableBy_generalLinearScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/GeneralLinear.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/GeneralLinear.lean#L287). The attribute's comment: “representability”. References: SGA 3 XX (5.1), “special case”.

> **Stacks Project, Tag 022W.** The functor of invertible `n` by `n`
> matrices over global sections is represented by the general linear scheme `GL_n`.

```lean
theorem generalLinearGroup_representableBy_generalLinearScheme (n : ℕ) :
    Nonempty ((generalLinearGroupFunctor.{u} n ⋙ forget GrpCat).RepresentableBy
      (generalLinearScheme.{u} n))
```

**`AlgebraicGeometry.generalLinearSchemeGrpObj`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/GeneralLinear.lean, line 331](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/GeneralLinear.lean#L331). The attribute's comment: “multiplication”.

> **Stacks Project, Tag 022W.** The general linear scheme over the integers is a group
> scheme.

```lean
noncomputable instance generalLinearSchemeGrpObj (n : ℕ) :
    GrpObj (Over.mk (generalLinearStructureMorphism.{u} n))
```

**`AlgebraicGeometry.exists_multiplicationRingHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/GeneralLinear.lean, line 420](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/GeneralLinear.lean#L420). The attribute's comment: “multiplication”.

> **Stacks Project, Tag 022W.** Multiplication on the general linear scheme is induced by
> the coordinate-ring homomorphism sending `xᵢⱼ` to `∑ k, xᵢₖ ⊗ xₖⱼ`.

```lean
theorem exists_multiplicationRingHom (n : ℕ) :
    ∃ f : generalLinearCoordinateRing.{u} n →+* generalLinearTensorSquare.{u} n,
      ((pullbackSpecIso (ULift.{u} ℤ) (generalLinearCoordinateRing.{u} n)
          (generalLinearCoordinateRing.{u} n)).inv ≫
          μ[Over.mk (generalLinearStructureMorphism.{u} n)].left =
            Spec.map (CommRingCat.ofHom f)) ∧
        ∀ i j : Fin n,
          f (algebraMap (MvPolynomial (Fin n × Fin n) (ULift.{u} ℤ))
              (generalLinearCoordinateRing.{u} n) (MvPolynomial.X (i, j))) =
            ∑ k : Fin n,
          @TensorProduct.tmul (ULift.{u} ℤ) CommRing.toCommSemiring
                (generalLinearCoordinateRing.{u} n) (generalLinearCoordinateRing.{u} n)
                CommRing.toCommSemiring.toAddCommMonoid
                CommRing.toCommSemiring.toAddCommMonoid
                Algebra.toModule Algebra.toModule
                (algebraMap (MvPolynomial (Fin n × Fin n) (ULift.{u} ℤ))
                  (generalLinearCoordinateRing.{u} n) (MvPolynomial.X (i, k)))
                (algebraMap (MvPolynomial (Fin n × Fin n) (ULift.{u} ℤ))
                  (generalLinearCoordinateRing.{u} n) (MvPolynomial.X (k, j)))
```

**`AlgebraicGeometry.generalLinearBaseChange`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/GeneralLinear.lean, line 488](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/GeneralLinear.lean#L488). The attribute's comment: “base\_change”.

> The general linear group scheme over `S`, obtained by base change from `Spec ℤ`.

```lean
noncomputable abbrev generalLinearBaseChange (n : ℕ) (S : Scheme.{u}) : Over S
```

**`AlgebraicGeometry.baseChangePointsIsoGeneralLinearPoints`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/GeneralLinear.lean, line 524](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/GeneralLinear.lean#L524). The attribute's comment: “base\_change”.

> Points of the base change are naturally points of the integral general linear scheme.

```lean
noncomputable def baseChangePointsIsoGeneralLinearPoints (n : ℕ) (S : Scheme.{u}) :
    yoneda.obj (generalLinearBaseChange n S) ≅
      (Over.forget S).op ⋙ yoneda.obj (generalLinearScheme n)
```

**`AlgebraicGeometry.baseChangePointsIsoGeneralLinearPoints_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/GeneralLinear.lean, line 545](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/GeneralLinear.lean#L545). The attribute's comment: “base\_change”.

> The pointwise map of the base-change comparison is composition with the first projection.

```lean
theorem baseChangePointsIsoGeneralLinearPoints_hom_app (n : ℕ) (S : Scheme.{u})
    (T : (Over S)ᵒᵖ) (f : T.unop ⟶ generalLinearBaseChange n S) :
    (baseChangePointsIsoGeneralLinearPoints n S).hom.app T f =
      f.left ≫ pullback.fst (generalLinearStructureMorphism.{u} n)
        (specULiftZIsTerminal.from S)
```

**`AlgebraicGeometry.generalLinearBaseChangeGrpObj`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/GeneralLinear.lean, line 554](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/GeneralLinear.lean#L554). The attribute's comment: “base\_change”.

> Base change preserves the group-scheme structure of the general linear group.

```lean
noncomputable instance generalLinearBaseChangeGrpObj (n : ℕ) (S : Scheme.{u}) :
    GrpObj (generalLinearBaseChange n S)
```

**`AlgebraicGeometry.baseChangeGroupPointsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/GeneralLinear.lean, line 658](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/GeneralLinear.lean#L658). The attribute's comment: “base\_change”. References: SGA 3 I (4.5), “GL\_n representability”.

> The group-valued points of the base-changed scheme are invertible matrices over global
> sections, naturally in the scheme over `S`.

```lean
noncomputable def baseChangeGroupPointsIso (n : ℕ) (S : Scheme.{u}) :
    yonedaGrpObj (generalLinearBaseChange n S) ≅ generalLinearGroupOverFunctor n S
```

**`AlgebraicGeometry.baseChangeGroupPointsIso_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/GeneralLinear.lean, line 672](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/GeneralLinear.lean#L672). The attribute's comment: “base\_change”.

> The canonical comparison sends an `S`-point to the invertible matrix obtained by pulling
> back the generic coordinates from the integral general linear scheme.

```lean
theorem baseChangeGroupPointsIso_hom_app (n : ℕ) (S : Scheme.{u})
    (T : (Over S)ᵒᵖ) (f : T.unop ⟶ generalLinearBaseChange n S) (i j : Fin n) :
    ((baseChangeGroupPointsIso n S).hom.app T f).val i j =
      (Scheme.Γ.map
        (f.left ≫ pullback.fst (generalLinearStructureMorphism.{u} n)
          (specULiftZIsTerminal.from S)).op).hom (generalLinearCoordinateSection n i j)
```

## Tag 022X, an example

[Tag 022X](https://stacks.math.columbia.edu/tag/022X) in the Stacks Project.

**`AlgebraicGeometry.generalLinearSchemeGrpObjOverIntegers`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Determinant.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Determinant.lean#L92). The attribute's comment: “det\_over\_integers”.

> The group scheme structure of `GLₙ` over the integers.

```lean
noncomputable instance generalLinearSchemeGrpObjOverIntegers (n : ℕ) :
    GrpObj (Over.mk (generalLinearStructureMorphismOverIntegers n))
```

**`AlgebraicGeometry.generalLinearSchemeGrpObjOverIntegers_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Determinant.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Determinant.lean#L280). The attribute's comment: “det\_over\_integers”.

> Multiplication on `GLₙ` is matrix multiplication, on generic matrix entries.

```lean
theorem generalLinearSchemeGrpObjOverIntegers_mul (n : ℕ) :
    ∃ m : generalLinearCoordinateRing.{0} n →+* generalLinearTensorSquareOverIntegers n,
      (pullbackSpecIso ℤ (generalLinearCoordinateRing.{0} n)
        (generalLinearCoordinateRing.{0} n)).inv ≫
          μ[Over.mk (generalLinearStructureMorphismOverIntegers n)].left =
            Spec.map (CommRingCat.ofHom m) ∧
      (∀ i j : Fin n,
        m (algebraMap (MvPolynomial (Fin n × Fin n) (ULift.{0} ℤ))
          (generalLinearCoordinateRing.{0} n) (MvPolynomial.X (i, j))) =
          ∑ k : Fin n,
          @TensorProduct.tmul ℤ CommRing.toCommSemiring
              (generalLinearCoordinateRing.{0} n) (generalLinearCoordinateRing.{0} n)
              CommRing.toCommSemiring.toAddCommMonoid CommRing.toCommSemiring.toAddCommMonoid
              Algebra.toModule Algebra.toModule
              (algebraMap (MvPolynomial (Fin n × Fin n) (ULift.{0} ℤ))
                (generalLinearCoordinateRing.{0} n) (MvPolynomial.X (i, k)))
                (algebraMap (MvPolynomial (Fin n × Fin n) (ULift.{0} ℤ))
                  (generalLinearCoordinateRing.{0} n) (MvPolynomial.X (k, j))))
```

**`AlgebraicGeometry.determinantGroupSchemeMorphismOverIntegers`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Determinant.lean, line 554](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Determinant.lean#L554). The attribute's comment: “det\_over\_integers”.

> The determinant as a morphism of group schemes over `Spec ℤ`.

```lean
noncomputable def determinantGroupSchemeMorphismOverIntegers (n : ℕ) :
    Grp.mk (Over.mk (generalLinearStructureMorphismOverIntegers n)) ⟶
      Grp.mk (multiplicativeGroup.asOver (Spec (.of ℤ)))
```

**`AlgebraicGeometry.determinantGroupSchemeMorphismOverIntegers_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Determinant.lean, line 563](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Determinant.lean#L563). The attribute's comment: “det\_over\_integers”.

> On coordinate rings, determinant sends the Laurent variable to the generic determinant.

```lean
theorem determinantGroupSchemeMorphismOverIntegers_spec (n : ℕ) :
    ∃ g : LaurentPolynomial ℤ →+* generalLinearCoordinateRing.{0} n,
      (determinantGroupSchemeMorphismOverIntegers n).hom.hom.left =
        Spec.map (CommRingCat.ofHom g) ∧
        g (LaurentPolynomial.T 1) =
          algebraMap (MvPolynomial (Fin n × Fin n) (ULift.{0} ℤ))
            (generalLinearCoordinateRing.{0} n) (generalLinearDeterminant.{0} n)
```

**`AlgebraicGeometry.determinantGroupSchemeMorphismOverULiftIntegers`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/DeterminantBaseChange.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/DeterminantBaseChange.lean#L207). The attribute's comment: “det\_after\_base\_change”.

> The determinant morphism of group schemes over the universe-lifted integers.

```lean
noncomputable def determinantGroupSchemeMorphismOverULiftIntegers (n : ℕ) :
    Grp.mk (Over.mk (generalLinearStructureMorphism.{u} n)) ⟶
      Grp.mk (multiplicativeGroupULift.asOver (Spec (.of (ULift.{u} ℤ))))
```

**`AlgebraicGeometry.determinantGroupSchemeMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/DeterminantBaseChange.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/DeterminantBaseChange.lean#L245). The attribute's comment: “det\_after\_base\_change”.

> The determinant morphism from the base-changed general linear group scheme to the
> base-changed multiplicative group scheme.

```lean
noncomputable def determinantGroupSchemeMorphism (n : ℕ) (S : Scheme.{u}) :
    Grp.mk (generalLinearBaseChange n S) ⟶
      Grp.mk (Scheme.asOver (multiplicativeGroupBaseChange S) S)
```

**`AlgebraicGeometry.determinantGroupSchemeMorphism_isBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/DeterminantBaseChange.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/DeterminantBaseChange.lean#L283). The attribute's comment: “det\_after\_base\_change”.

> The underlying scheme morphism is the pullback of the universal determinant
> over the universe-lifted integers, for every base scheme in that universe.

```lean
theorem determinantGroupSchemeMorphism_isBaseChange (n : ℕ) (S : Scheme.{u}) :
    (determinantGroupSchemeMorphism n S).hom.hom =
      (Over.pullback (specULiftZIsTerminal.from S)).map
        (determinantGroupSchemeMorphismOverULiftIntegers n).hom.hom
```

**`AlgebraicGeometry.determinantGroupSchemeMorphism_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/DeterminantBaseChange.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/DeterminantBaseChange.lean#L319). The attribute's comment: “det\_after\_base\_change”.

> The base-changed determinant sends an invertible matrix over the global sections of
> an `S`-scheme to its determinant, viewed as a global unit.

```lean
theorem determinantGroupSchemeMorphism_apply (n : ℕ) (S : Scheme.{u})
    (T : (Over S)ᵒᵖ) (f : T.unop ⟶ generalLinearBaseChange n S) :
    (baseChangePointsIsoGlobalUnits S).hom.app T
        (((yonedaGrp.map (determinantGroupSchemeMorphism n S)).app T) f) =
      Matrix.GeneralLinearGroup.det ((baseChangeGroupPointsIso n S).hom.app T f)
```

**`AlgebraicGeometry.determinantGroupSchemeMorphism_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/DeterminantBaseChange.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/DeterminantBaseChange.lean#L373). The attribute's comment: “det\_after\_base\_change”.

> After projecting the base-changed morphism to the integral models, it is the
> integral determinant morphism. The coefficient map compares `ℤ` with `ULift ℤ`.

```lean
theorem determinantGroupSchemeMorphism_baseChange (n : ℕ) (S : Scheme.{0}) :
    (determinantGroupSchemeMorphism n S).hom.hom.left ≫
        pullback.fst (multiplicativeGroupULift ↘ Spec (.of (ULift.{0} ℤ)))
          (specULiftZIsTerminal.from S) ≫
        Spec.map (CommRingCat.ofHom
          (AddMonoidAlgebra.mapRingHom ℤ
            (ULift.ringEquiv.{0, 0}.symm.toRingHom : ℤ →+* ULift.{0} ℤ))) =
      pullback.fst (generalLinearStructureMorphism.{0} n) (specULiftZIsTerminal.from S) ≫
        (determinantGroupSchemeMorphismOverIntegers n).hom.hom.left
```

## Tag 03YW, an example

[Tag 03YW](https://stacks.math.columbia.edu/tag/03YW) in the Stacks Project.

**`AlgebraicGeometry.constantSchemeOverIntegers`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Constant.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Constant.lean#L84). The attribute's comment: “constant\_group\_scheme\_construction”.

> The scheme `G_{Spec ℤ}`, before equipping it with its group structure.

```lean
abbrev constantSchemeOverIntegers (G : Type v) [Small.{u} G] : Scheme.{u}
```

**`AlgebraicGeometry.constantGroupSchemeStructure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Constant.lean, line 342](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Constant.lean#L342). The attribute's comment: “constant\_group\_scheme\_construction”.

> The group-object structure on the coproduct of copies of `Spec ℤ` indexed by `G`, whose
> multiplication sends the component `(g, h)` to the component `g * h`.

```lean
def constantGroupSchemeStructure (G : Type v) [Small.{u} G] [Group G] :
    { s : GrpObj (constantSchemeOverIntegersObj G) // IsConstantGroupSchemeStructure G s }
```

**`AlgebraicGeometry.constantGroupScheme`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Constant.lean, line 353](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Constant.lean#L353). The attribute's comment: “constant\_group\_scheme\_construction”. References: SGA 3 VIII (1.0.3).

> The constant group scheme `G_S`, obtained by base-changing `G_{Spec ℤ}` to `S`.

```lean
abbrev constantGroupScheme (G : Type v) [Small.{u} G] [Group G] (S : Scheme.{u}) :
    Grp (Over S)
```

**`AlgebraicGeometry.constantSchemeOverIntegersPointsIsoLocallyConstantMaps`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Constant.lean, line 665](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Constant.lean#L665). The attribute's comment: “representability\_over\_integers”. References: SGA 3 I (1.8), “special case”; SGA 3 VIII (1.3), “special case”; SGA 3 VIII (1.4), “special case”.

> The canonical group-valued functor-of-points isomorphism for the constant group scheme
> over `Spec ℤ`.

```lean
def constantSchemeOverIntegersPointsIsoLocallyConstantMaps (G : Type v) [Small.{u} G] [Group G] :
    (yonedaGrp.obj (⟨constantSchemeOverIntegersObj G⟩ : Grp (Over (⊤_ Scheme.{u}))) ⋙
      GrpCat.uliftFunctor.{v}) ≅ locallyConstantMapsOverIntegers G
```

**`AlgebraicGeometry.constantSchemeOverIntegersPointsIsoLocallyConstantMaps_component`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Constant.lean, line 673](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Constant.lean#L673). The attribute's comment: “representability\_over\_integers”.

> The canonical isomorphism sends the inclusion of the component indexed by `g` to the
> constant function with value `g`.

```lean
theorem constantSchemeOverIntegersPointsIsoLocallyConstantMaps_component
    (G : Type v) [Small.{u} G] [Group G] (g : G) :
    ((constantSchemeOverIntegersPointsIsoLocallyConstantMaps G).hom.app
      (Opposite.op (Over.mk (𝟙 (⊤_ Scheme.{u})))))
        (ULift.up (constantComponent G g)) = LocallyConstant.const (⊤_ Scheme.{u}) g
```

**`AlgebraicGeometry.locallyConstantMaps_representableBy_constantSchemeOverIntegers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Constant.lean, line 685](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Constant.lean#L685). The attribute's comment: “representability\_over\_integers”. References: SGA 3 VIII (1.3), “partial”.

> The functor assigning to a scheme the group of locally constant maps to `G` is represented
> by the underlying scheme of the constant group scheme over `Spec ℤ`.

```lean
theorem locallyConstantMaps_representableBy_constantSchemeOverIntegers
    (G : Type v) [Small.{u} G] [Group G] :
    Nonempty ((locallyConstantMaps G ⋙ forget GrpCat).RepresentableBy
      (constantSchemeOverIntegers G))
```

**`AlgebraicGeometry.constantGroupSchemePointsIsoLocallyConstantMaps`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Constant.lean, line 819](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/Constant.lean#L819). The attribute's comment: “relative\_functor\_of\_points”. References: SGA 3 I (1.8), “special case”; SGA 3 VIII (1.3), “partial”; SGA 3 VIII (1.4), “partial”.

> The group-valued functor of points of the constant group scheme `G_S` is naturally
> isomorphic to the functor of locally constant `G`-valued maps. Under this isomorphism
> multiplication is pointwise multiplication of functions.

```lean
def constantGroupSchemePointsIsoLocallyConstantMaps (G : Type v) [Small.{u} G] [Group G]
    (S : Scheme.{u}) :
    (yonedaGrp.obj (constantGroupScheme G S) ⋙ GrpCat.uliftFunctor.{v}) ≅
      locallyConstantMapsOver G S
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.5, Tag 047F](https://stacks.math.columbia.edu/tag/047F)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
