---
declaration: section
origin: cited
lean: AlgebraicGeometry.FiniteFreeAlgebra.existsUnique_map_universalRingStructure, AlgebraicGeometry.FiniteFreeAlgebra.structureConstantsOver, AlgebraicGeometry.FiniteFreeAlgebra.structureConstantsBaseChange, AlgebraicGeometry.FiniteFreeAlgebra.structureConstantsBaseChangePoints, AlgebraicGeometry.FiniteFreeAlgebra.structureConstantsBaseChangePoints_naturality, AlgebraicGeometry.Space.structureConstantsSiteObject, AlgebraicGeometry.Space.structureConstantsSpaceOver, AlgebraicGeometry.Space.isAlgebraicSpace_structureConstantsSpaceOver
statement: formalized
proof: formalized
---

# 97.13 The finite Hilbert stack of a point

Section 97.13 of the Stacks Project, [Tag 05YL](https://stacks.math.columbia.edu/tag/05YL). 4 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05YM, an equation

[Tag 05YM](https://stacks.math.columbia.edu/tag/05YM) in the Stacks Project.

**`AlgebraicGeometry.FiniteFreeAlgebra.existsUnique_map_universalRingStructure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/CanonicalIdentification.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/CanonicalIdentification.lean#L98). The attribute's comment: “for every scheme `T`, the point `x : T ⟶ Spec(R_univ)` corresponds to the extension of the universal algebra along the ring map `R_univ → Γ(T, 𝒪_T)` induced by `x`; this is a bijection, natural in `T`”.

> **Stacks 05YM.** For every scheme `T`, every free `d`-dimensional algebra over `Γ(T, 𝒪_T)`
> is the extension of the universal algebra `m_univ` along the ring map induced by exactly one
> morphism `T ⟶ X = Spec(R_univ)`; and the resulting identification of `X(T)` with free
> `d`-dimensional algebras over `Γ(T, 𝒪_T)` commutes with pullback along every morphism of
> schemes.

```lean
theorem existsUnique_map_universalRingStructure :
    (∀ (T : Scheme.{u}) (m : FiniteFreeAlgebra Γ(T, ⊤) d),
      ∃! x : T ⟶ scheme.{u} d, map (classifyingRingHom x) (universalRingStructure d) = m) ∧
    ∀ {T U : Scheme.{u}} (f : T ⟶ U) (x : U ⟶ scheme.{u} d),
      map f.appTop.hom (map (classifyingRingHom x) (universalRingStructure d)) =
        map (classifyingRingHom (f ≫ x)) (universalRingStructure d)
```

**`AlgebraicGeometry.FiniteFreeAlgebra.structureConstantsOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/StructureConstantsSpace.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/StructureConstantsSpace.lean#L58). The attribute's comment: “the scheme of structure constants over the integers”.

> The scheme of structure constants, as a scheme over the integers.

```lean
noncomputable abbrev structureConstantsOver : Over (Spec (CommRingCat.of (ULift.{u} ℤ)))
```

**`AlgebraicGeometry.FiniteFreeAlgebra.structureConstantsBaseChange`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/StructureConstantsSpace.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/StructureConstantsSpace.lean#L64). The attribute's comment: “the scheme of structure constants over a general base”.

> The scheme `X_S` of structure constants over a scheme `S`, obtained by base change from the
> integers.

```lean
noncomputable abbrev structureConstantsBaseChange (S : Scheme.{u}) : Over S
```

**`AlgebraicGeometry.FiniteFreeAlgebra.structureConstantsBaseChangePoints`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/StructureConstantsSpace.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/StructureConstantsSpace.lean#L82). The attribute's comment: “the points of the scheme of structure constants over a general base”.

> The points of `X_S` over a scheme `T` over `S` are the free `d`-dimensional algebras over
> `Γ(T, 𝒪_T)`.

```lean
noncomputable def structureConstantsBaseChangePoints (S : Scheme.{u}) (T : Over S) :
    (T ⟶ structureConstantsBaseChange.{u} d S) ≃ FiniteFreeAlgebra Γ(T.left, ⊤) d
```

**`AlgebraicGeometry.FiniteFreeAlgebra.structureConstantsBaseChangePoints_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/StructureConstantsSpace.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/StructureConstantsSpace.lean#L90). The attribute's comment: “the points of the scheme of structure constants over a general base”.

> `AlgebraicGeometry.FiniteFreeAlgebra.structureConstantsBaseChangePoints` is natural in the
> scheme over `S`: restricting a point along `f` extends the scalars of its structure constants
> along the induced map of global sections.

```lean
theorem structureConstantsBaseChangePoints_naturality (S : Scheme.{u}) {T U : Over S}
    (f : T ⟶ U) (x : U ⟶ structureConstantsBaseChange.{u} d S) :
    FiniteFreeAlgebra.map f.left.appTop.hom
        (structureConstantsBaseChangePoints d S U x) =
      structureConstantsBaseChangePoints d S T (f ≫ x)
```

**`AlgebraicGeometry.Space.structureConstantsSiteObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/StructureConstantsSpace.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/StructureConstantsSpace.lean#L127). The attribute's comment: “the scheme of structure constants as an object of the site”.

> The scheme `X_S` of structure constants over `S`, read as an object of the big fppf site
> over `S`.

```lean
noncomputable def structureConstantsSiteObject : BigFppfOver 𝒞 S hS
```

**`AlgebraicGeometry.Space.structureConstantsSpaceOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/StructureConstantsSpace.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/StructureConstantsSpace.lean#L134). The attribute's comment: “the scheme of structure constants as an object over an algebraic space”.

> The algebraic space `B ×_S X_S` over an algebraic space `B` over `S`, as an object of the
> slice of presheaves on the big fppf site over `B`.

```lean
noncomputable def structureConstantsSpaceOver (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u) :
    Over B
```

**`AlgebraicGeometry.Space.isAlgebraicSpace_structureConstantsSpaceOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/StructureConstantsSpace.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/StructureConstantsSpace.lean#L140). The attribute's comment: “the scheme of structure constants as an object over an algebraic space”.

> The presheaf underlying `B ×_S X_S` is an algebraic space over `S`.

```lean
theorem isAlgebraicSpace_structureConstantsSpaceOver (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (hB : IsAlgebraicSpace 𝒞 S hS B) :
    IsAlgebraicSpace 𝒞 S hS
      (B ⨯ yoneda.obj (structureConstantsSiteObject 𝒞 S hS d))
```

## Tag 05YN, an equation

[Tag 05YN](https://stacks.math.columbia.edu/tag/05YN) in the Stacks Project.

**`AlgebraicGeometry.FiniteFreeAlgebra.presheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/Presheaf.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/Presheaf.lean#L290).

> The presheaf in groupoids `FA_d` of free rank-`d` commutative algebra structures and their
> isomorphisms.

```lean
noncomputable def presheaf (B : BigFppfSite.{u}) (d : ℕ) [NeZero d] : Presheaf B d
```

## Tag 05YP, a lemma

[Tag 05YP](https://stacks.math.columbia.edu/tag/05YP) in the Stacks Project.

**`AlgebraicGeometry.FiniteFreeAlgebra.presheaf_actionGroupoid`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/ActionGroupoid.lean, line 1093](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/ActionGroupoid.lean#L1093).

> Conjugation defines an action on the scheme of structure constants, and `FA_d` is
> naturally isomorphic to its action-groupoid functor, by the representing equivalence on objects
> and the inverse matrices on arrows.

```lean
public theorem presheaf_actionGroupoid
    (B : BigFppfSite.{u}) (d : ℕ) [NeZero d]
    (F : Presheaf B d) :
    ∃ (laws : ConjugationPreservesAlgebraLaws.{u} d)
      (P : ActionGroupoidPresheaf B d laws)
      (η : F.functor ≅ P.toFunctor),
      (∀ (T : B.Schemesᵒᵖ) (x : F.functor.obj T),
        (η.hom.app T).obj x =
          ((representation.{u} d).equiv T.unop.1).symm
            (F.objectEquiv T x)) ∧
      (∀ (T : B.Schemesᵒᵖ) (x y : F.functor.obj T) (e : x ⟶ y),
        (P.arrowEquiv T _ _ ((η.hom.app T).map e)).1.1 =
          (F.arrowEquiv T x y e).matrix⁻¹)
```

## Tag 05YQ, a proposition

[Tag 05YQ](https://stacks.math.columbia.edu/tag/05YQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_finiteCoverFibered`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/FiniteCoverAlgebraicStack.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/FiniteCoverAlgebraicStack.lean#L68). The attribute's comment: “the second assertion: `ℋ_d` is an algebraic stack over `S`, transported along the equivalence of the first assertion from the quotient stack `[X/G]` of the conjugation action, which is an algebraic stack by Stacks 04TK”.

> The category `ℋ_d` of degree-`d` finite locally free covers over the big fppf site over `S`
> is an algebraic stack over `S`.

```lean
theorem isAlgebraicStack_finiteCoverFibered :
    IsAlgebraicStack.{u, w} 𝒞 S hS (finiteCoverFibered 𝒞 S hS d).val
```

**`AlgebraicGeometry.FiniteFreeAlgebra.nonempty_isEquivalenceOver_finiteCover_conjugationQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/FiniteCoverStructureConstants.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/FiniteCoverStructureConstants.lean#L84). The attribute's comment: “the category of degree-`d` finite locally free covers is equivalent, over the big fppf site over `S`, to the quotient stack `[X/G]` of the conjugation action of the unit-fixing subgroup `G` of `GL_d` on the scheme `X` of structure constants”.

> The category `ℋ_d` of degree-`d` finite locally free covers is equivalent, over the big fppf
> site over `S`, to the quotient stack `[X/G]` of the conjugation action of the unit-fixing subgroup
> `G ⊆ GL_d` on the scheme `X` of structure constants of free `d`-dimensional algebras, by the
> extension of `AlgebraicGeometry.FiniteFreeAlgebra.specQuotientPrestack` across the stackification
> `AlgebraicGeometry.Stack.toQuotientStack`.

```lean
theorem nonempty_isEquivalenceOver_finiteCover_conjugationQuotient :
    Nonempty (Functor.IsEquivalenceOver
      (Space.structureConstantsQuotientStack 𝒞 S hS d (Space.terminalSpace 𝒞 S hS)).p
      (Functor.uliftHomProj (AlgebraicGeometry.Stack.finiteCoverProjection
        (B := 𝒞) (S := S) (hS := hS) (d := d)))
      (Functor.Stackification.extend
        (AlgebraicGeometry.Stack.isFibredOneMorphism_toQuotientStack
          (conjugationGroupoidInSpaces 𝒞 S hS d (isAlgebraicSpace_conjugationGroup 𝒞 S hS d)
          (isAlgebraicSpace_conjugationObject 𝒞 S hS d)))
        (isFibredOneMorphism_specQuotientPrestack
          (conjugationGroupoidInSpaces 𝒞 S hS d (isAlgebraicSpace_conjugationGroup 𝒞 S hS d)
          (isAlgebraicSpace_conjugationObject 𝒞 S hS d))
          (conjugationGroupoidIso 𝒞 S hS d))
        (AlgebraicGeometry.Stack.isLocallyBijective_toQuotientStack
          (conjugationGroupoidInSpaces 𝒞 S hS d (isAlgebraicSpace_conjugationGroup 𝒞 S hS d)
          (isAlgebraicSpace_conjugationObject 𝒞 S hS d)))
        (isStack_uliftHomProj_finiteCoverProjection 𝒞 S hS d).isMorSheaf
        (AlgebraicGeometry.Stack.essImage_toQuotientStack
          (conjugationGroupoidInSpaces 𝒞 S hS d (isAlgebraicSpace_conjugationGroup 𝒞 S hS d)
          (isAlgebraicSpace_conjugationObject 𝒞 S hS d)))
        (isStack_uliftHomProj_finiteCoverProjection 𝒞 S hS d).hasEffectiveDescent))
```

**`AlgebraicGeometry.FiniteFreeAlgebra.algEquivCarrierOfIsUnit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/LocalUnitBasis.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/LocalUnitBasis.lean#L179). The attribute's comment: “clause (b) of the proof over an affine base: inverting one coordinate of the unit presents the algebra as the algebra of a free `d`-dimensional structure”.

> If one coordinate of the unit becomes invertible in `S`, the base changed algebra `S ⊗[R] A` is
> the algebra of a free `d`-dimensional structure over `S`.

```lean
noncomputable def algEquivCarrierOfIsUnit (b : Module.Basis (Fin d) R A) (i : Fin d)
    (hi : IsUnit (algebraMap R S (b.repr 1 i))) :
    (S ⊗[R] A) ≃ₐ[S] Carrier (structureOfIsUnit S b i hi)
```

**`AlgebraicGeometry.FiniteFreeAlgebra.exists_structure_algEquiv_localizationAway`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/LocalUnitBasis.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/LocalUnitBasis.lean#L202). The attribute's comment: “clause (b) of the proof over an affine base, on the standard open cover cut out by the coordinates of the unit”.

> Over each member of the standard open cover of `Spec R` cut out by the coordinates of the unit,
> the algebra is the algebra of a free `d`-dimensional structure.

```lean
theorem exists_structure_algEquiv_localizationAway (b : Module.Basis (Fin d) R A) (i : Fin d) :
    ∃ m : FiniteFreeAlgebra (Localization.Away (b.repr 1 i)) d,
      Nonempty ((Localization.Away (b.repr 1 i) ⊗[R] A) ≃ₐ[Localization.Away (b.repr 1 i)]
        Carrier m)
```

**`AlgebraicGeometry.FiniteFreeAlgebra.algEquivCarrierOfBasis`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/OfBasis.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/OfBasis.lean#L105). The attribute's comment: “transport of the multiplication along a basis whose first vector is the unit, over an affine base”.

> An algebra that is free of rank `d` on a basis whose first vector is the unit is isomorphic,
> as an `R`-algebra, to the algebra of the structure constants of that basis.

```lean
noncomputable def algEquivCarrierOfBasis (b : Module.Basis (Fin d) R A) (hb : b 0 = 1) :
    A ≃ₐ[R] Carrier (ofBasis b hb)
```

**`AlgebraicGeometry.FiniteFreeAlgebra.isFiniteLocallyFreeOfRank_specCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/Spectrum.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/Spectrum.lean#L66). The attribute's comment: “the degree-`d` clause for the spectrum of a free `d`-dimensional structure over a ring, in the affine case”.

> The spectrum of the algebra of a free `d`-dimensional structure is finite locally free of
> degree `d` over the base.

```lean
theorem isFiniteLocallyFreeOfRank_specCover (m : FiniteFreeAlgebra R d) :
    Stacks.Morphisms.IsFiniteLocallyFreeOfRank (specCover m).hom d
```

**`AlgebraicGeometry.FiniteFreeAlgebra.structureIsoEquivSpecIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/Spectrum.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/Spectrum.lean#L112). The attribute's comment: “clause (a) of the proof over an affine base: `Isom (m, n)` is `Isom (Spec m, Spec n)` as schemes over the base”.

> The isomorphisms of two free `d`-dimensional structures over `R` are exactly the
> isomorphisms of their spectra as schemes over `Spec R`.

```lean
noncomputable def structureIsoEquivSpecIso (m n : FiniteFreeAlgebra R d) :
    StructureIso m n ≃ (specCover m ≅ specCover n)
```

**`AlgebraicGeometry.FiniteFreeAlgebra.Carrier.basis`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/StructureAlgebra.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/StructureAlgebra.lean#L319). The attribute's comment: “the module underlying the algebra of a free `d`-dimensional structure is free of rank `d`, the affine core of the degree-`d` clause for the relative spectrum of `m`”.

> The module underlying the algebra of a free `d`-dimensional structure is free with basis the
> `d` standard basis vectors.

```lean
noncomputable def basis (m : FiniteFreeAlgebra R d) : Module.Basis (Fin d) R (Carrier m)
```

**`AlgebraicGeometry.FiniteFreeAlgebra.structureIsoEquivAlgEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/StructureAlgebra.lean, line 524](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FiniteFreeAlgebra/StructureAlgebra.lean#L524). The attribute's comment: “clause (a) of the proof, in algebraic form: the isomorphisms of two free `d`-dimensional structures are exactly the algebra isomorphisms of the associated algebras”.

> The isomorphisms of two free `d`-dimensional structures over a ring are exactly the
> `R`-algebra isomorphisms of the two associated algebras.

```lean
noncomputable def structureIsoEquivAlgEquiv (m n : FiniteFreeAlgebra R d) :
    StructureIso m n ≃ (Carrier m ≃ₐ[R] Carrier n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 97.13, Tag 05YL](https://stacks.math.columbia.edu/tag/05YL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
