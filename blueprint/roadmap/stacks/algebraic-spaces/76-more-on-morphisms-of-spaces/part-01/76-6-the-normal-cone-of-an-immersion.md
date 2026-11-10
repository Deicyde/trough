---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.conormalAlgebra, AlgebraicGeometry.Space.conormalAlgebraOfImmersion, AlgebraicGeometry.Space.conormalAlgebraPiece, AlgebraicGeometry.Space.conormalAlgebraPiecePushforwardIso, AlgebraicGeometry.Space.isoConormalAlgebraPiece, AlgebraicGeometry.Space.conormalAlgebraDegreeZeroIso, AlgebraicGeometry.Space.symmetricAlgebraToConormalAlgebra, AlgebraicGeometry.Space.symmetricAlgebraToConormalAlgebraOfImmersion
statement: formalized
proof: formalized
---

# 76.6 The normal cone of an immersion

Section 76.6 of the Stacks Project, [Tag 09RM](https://stacks.math.columbia.edu/tag/09RM). 7 tags here are carried by 26 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09RN, a definition

[Tag 09RN](https://stacks.math.columbia.edu/tag/09RN) in the Stacks Project.

**`AlgebraicGeometry.Space.conormalAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebra.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebra.lean#L211). The attribute's comment: “the conormal algebra of a closed immersion”.

> **Stacks Project, Tag 09RN.**  The conormal algebra `𝒞_{Z/X,*}` of a closed immersion
> `i : Z ⟶ X` of algebraic spaces: the inverse image along `i` of the sheaf of graded
> `𝒪_X`-algebras `⨁_{n ≥ 0} 𝓘ⁿ`, for `𝓘` the ideal sheaf of `i`.
>
> Its degree-`n` piece is `i^*(𝓘ⁿ)`, which is the `𝒪_Z`-module the source describes as
> `𝓘ⁿ/𝓘ⁿ⁺¹`; the module documentation records why, and that the identification is deferred, as
> it is in the degree-one case `AlgebraicGeometry.Space.conormalModule`.

```lean
noncomputable def conormalAlgebra (i : Z ⟶ X) :
    SheafOfModules.GradedAlgebra.{u, u} (structureRingSheaf B S hS Z)
```

**`AlgebraicGeometry.Space.conormalAlgebraOfImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebra.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebra.lean#L319). The attribute's comment: “the conormal algebra of an immersion”.

> **Stacks Project, Tag 09RN.**  The conormal algebra `𝒞_{Z/X,*}` of an immersion
> `i : Z ⟶ X` of algebraic spaces: the conormal algebra of the closed immersion of `Z` into the
> complement `X ∖ ∂Z` of the boundary of its image, through which `i` factors by Stacks 04CE.
>
> Its degree-`n` piece is the inverse image along that closed immersion of the `n`-th power of
> the ideal sheaf of `Z` in `X ∖ ∂Z`, which is the `𝒪_Z`-module the source describes as
> `𝓘ⁿ/𝓘ⁿ⁺¹`.

```lean
noncomputable def conormalAlgebraOfImmersion (hX : IsAlgebraicSpace B S hS X₀)
    (hZ : IsAlgebraicSpace B S hS Z₀) (i : Z₀ ⟶ X₀) (hi : IsImmersion B S hS i) :
    SheafOfModules.GradedAlgebra.{u, u}
      (structureRingSheaf B S hS (⟨Z₀, hZ⟩ : AlgebraicSpaces B S hS))
```

**`AlgebraicGeometry.Space.conormalAlgebraPiece`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/ClosedImmersion/ConormalAlgebra.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/ClosedImmersion/ConormalAlgebra.lean#L205). The attribute's comment: “the homogeneous pieces, as inverse images of the ideal powers, for a closed subspace”. References: EGA IV (16.1.2), “I^n/I^\{n+1} pieces”.

> **The homogeneous pieces of the conormal algebra of a closed subspace.**  The degree-`n`
> piece `𝒞_{Z/X, n}` of the conormal algebra of a closed subspace `Z` of an algebraic space `X`
> is the inverse image along the inclusion `i : Z ⟶ X` of the `n`-th power of the defining ideal
> sheaf `𝓘_Z ⊆ 𝒪_X` of Stacks 03MB.

```lean
noncomputable def conormalAlgebraPiece (X : AlgebraicSpaces B S hS)
    (Z : ClosedSubspaces B S hS X.1) (n : ℕ) :
    Modules.{u, u} B S hS Z.1.toFunctor Z.2.1
```

## Tag 09RP, an equation

[Tag 09RP](https://stacks.math.columbia.edu/tag/09RP) in the Stacks Project.

**`AlgebraicGeometry.Space.conormalAlgebraPiecePushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraDegreeN.lean, line 480](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraDegreeN.lean#L480).

> **Stacks 09RP.**  For a closed subspace `Z` of an algebraic space `X` with inclusion `i` and
> defining ideal sheaf `𝓘`, the direct image of the degree-`n` piece of the conormal algebra is the
> degree-`n` graded piece of `𝓘`:
>
> `i_*𝒞_{Z/X, n} = 𝓘ⁿ/𝓘ⁿ⁺¹`.
>
> The degree-`n` piece is `AlgebraicGeometry.Space.conormalAlgebraPiece`, the inverse image
> `i^*(𝓘ⁿ)` of Stacks 09RN; in degree one it is the conormal module of Stacks 04CN, and in degree
> zero the inverse image of the structure sheaf of `X`.  The identification with `𝓘ⁿ/𝓘ⁿ⁺¹` is the
> inverse of the unit of Stacks 03LU, transported along
> `AlgebraicGeometry.Space.pullbackConormalGradedPieceIso`;
> `AlgebraicGeometry.Space.isoConormalAlgebraPiece` records that it determines `𝒞_{Z/X, n}` up to
> isomorphism, which is what makes the equation of the source an identification and not merely the
> assertion that some module has that direct image.

```lean
def conormalAlgebraPiecePushforwardIso (n : ℕ) :
    (modulePushforward B S hS (subspaceInclusion B S hS X Z)).obj
        (conormalAlgebraPiece B S hS X Z n) ≅ conormalGradedPiece B S hS X Z n
```

**`AlgebraicGeometry.Space.isoConormalAlgebraPiece`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraDegreeN.lean, line 498](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraDegreeN.lean#L498). The attribute's comment: “the characterizing property 76.6.1.1 determines 𝒞\_\{Z/X, n} up to isomorphism”.

> **The degree-`n` piece of the conormal algebra is determined by Stacks 09RP.**  An
> `𝒪_Z`-module whose direct image along the inclusion is `𝓘ⁿ/𝓘ⁿ⁺¹` is isomorphic to `𝒞_{Z/X, n}`,
> because the direct image of modules along a closed immersion is fully faithful (Stacks 04CJ,
> part (2)).  This is the uniqueness clause behind the equality sign of the source.
>
> The source introduces 76.6.1.1 by saying that `𝒞_{Z/X, n}` is "characterized by the property"
> `i_*𝒞_{Z/X, n} = 𝓘ⁿ/𝓘ⁿ⁺¹`; this is that characterization, and it is what licenses reading
> `AlgebraicGeometry.Space.conormalAlgebraPiecePushforwardIso` as the equality sign of the
> source rather than as the weaker assertion that some module has that direct image.

```lean
def isoConormalAlgebraPiece (n : ℕ) (Cc : Modules.{u, u} B S hS Z.1.toFunctor Z.2.1)
    (e : (modulePushforward B S hS (subspaceInclusion B S hS X Z)).obj Cc ≅
      conormalGradedPiece B S hS X Z n) :
    Cc ≅ conormalAlgebraPiece B S hS X Z n
```

**`AlgebraicGeometry.Space.conormalAlgebraDegreeZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraDegreeZero.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraDegreeZero.lean#L157). The attribute's comment: “degree zero”.

> For a closed subspace `Z` of an algebraic space `X` with
> inclusion `i` and defining ideal sheaf `𝓘`, the direct image of the structure sheaf of `Z` is the
> quotient of the structure sheaf of `X` by `𝓘`:
>
> `i_*𝒞_{Z/X, 0} = i_*𝒪_Z = 𝒪_X/𝓘 = 𝓘⁰/𝓘¹`.
>
> The isomorphism is induced by the structure projection.

```lean
noncomputable def conormalAlgebraDegreeZeroIso :
    cokernel (definingIdealSheaf B S hS X Z).ι ≅ pushforwardStructureSheaf B S hS X Z
```

## Tag 09RQ, an equation

[Tag 09RQ](https://stacks.math.columbia.edu/tag/09RQ) in the Stacks Project.

**`AlgebraicGeometry.Space.symmetricAlgebraToConormalAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSymmetricAlgebra.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSymmetricAlgebra.lean#L165). The attribute's comment: “the canonical map from the symmetric algebra on the conormal module”.

> **Stacks Project, Tag 09RQ, Equation 76.6.1.2.**  Let `i : Z ⟶ X` be a morphism of algebraic
> spaces and let `A` be a sheaf of graded `𝒪_Z`-algebras which is the symmetric algebra on the
> conormal module `𝒞_{Z/X} = (𝒞_{Z/X,*})_1`, with degree-one generator `ι`.  Then there is a
> canonical unital homomorphism of sheaves of graded `𝒪_Z`-algebras
>
> `Sym^*(𝒞_{Z/X}) ⟶ 𝒞_{Z/X,*}`,
>
> the unique one extending the identity of the conormal module.
>
> It exists because the degree-`(1,1)` multiplication of the conormal algebra is commutative, by
> `AlgebraicGeometry.Space.conormalAlgebra_mul_one_one_comm`, which is exactly the condition the
> universal property of the symmetric algebra tests a degree-one generator against.

```lean
noncomputable def symmetricAlgebraToConormalAlgebra (i : Z ⟶ X)
    (A : SheafOfModules.GradedAlgebra.{u, u} (structureRingSheaf B S hS Z))
    (ι : (conormalAlgebra B S hS i).piece 1 ⟶ A.piece 1)
    (hA : SheafOfModules.GradedAlgebra.IsSymmetricAlgebra A ι) :
    SheafOfModules.GradedAlgebra.UnitalHom A (conormalAlgebra B S hS i)
```

**`AlgebraicGeometry.Space.symmetricAlgebraToConormalAlgebraOfImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSymmetricAlgebra.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSymmetricAlgebra.lean#L211). The attribute's comment: “the canonical map from the symmetric algebra, for an immersion”.

> **Stacks Project, Tag 09RQ for an immersion.**  The canonical map
> `Sym^*(𝒞_{Z/X}) ⟶ 𝒞_{Z/X,*}` of Equation 76.6.1.2 for an immersion `i : Z ⟶ X`, taken through
> the closed factorisation of Stacks 04CE which defines
> `AlgebraicGeometry.Space.conormalAlgebraOfImmersion`.

```lean
noncomputable def symmetricAlgebraToConormalAlgebraOfImmersion
    (hX : IsAlgebraicSpace B S hS X₀) (hZ : IsAlgebraicSpace B S hS Z₀) (i : Z₀ ⟶ X₀)
    (hi : IsImmersion B S hS i)
    (A : SheafOfModules.GradedAlgebra.{u, u}
      (structureRingSheaf B S hS (⟨Z₀, hZ⟩ : AlgebraicSpaces B S hS)))
    (ι : (conormalAlgebraOfImmersion B S hS hX hZ i hi).piece 1 ⟶ A.piece 1)
    (hA : SheafOfModules.GradedAlgebra.IsSymmetricAlgebra A ι) :
    SheafOfModules.GradedAlgebra.UnitalHom A
      (conormalAlgebraOfImmersion B S hS hX hZ i hi)
```

## Tag 09RR, a lemma

[Tag 09RR](https://stacks.math.columbia.edu/tag/09RR) in the Stacks Project.

**`AlgebraicGeometry.Space.conormalAlgebraEtaleRestrictionPieceIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraEtaleRestriction.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraEtaleRestriction.lean#L137). The attribute's comment: “the conormal algebra of an etale localisation, in each degree”.

> Let `i : Z ⟶ X` be a morphism of algebraic spaces, let `φ : U ⟶ X` be étale and let
> `Z_U = U ×_X Z` with projections `p : Z_U ⟶ Z` and `i_U : Z_U ⟶ U`. Then the inverse image along
> `p` of the degree-`n` piece of the conormal algebra of `i` is the degree-`n` piece of the conormal
> algebra of `i_U`:
>
> `(𝒞_{Z/X,*}|_{Z_U})_n = p^*(𝒞_{Z/X,*})_n ≅ (𝒞_{Z_U/U,*})_n`.
>
> The isomorphism is the square comparison `p^*i^* ≅ i_U^*φ^*` of
> `AlgebraicGeometry.Space.modulePullbackSquareCompIso`, then the inverse image along `i_U` of the
> identification of `φ^*` with étale restriction of [Stacks Project, Tag 03LW], then the equality
> `𝓘ⁿ|_U = 𝓘_Uⁿ` of the powers of the kernel ideal sheaves.

```lean
noncomputable def conormalAlgebraEtaleRestrictionPieceIso (p : ZU ⟶ Z) (iU : ZU ⟶ U) (i : Z ⟶ X)
    (φ : U ⟶ X) (sq : IsPullback p iU i φ) (hφ : IsEtale B S hS φ.hom) (n : ℤ) :
    (modulePullback B S hS p).obj ((conormalAlgebra B S hS i).piece n) ≅
      (conormalAlgebra B S hS iU).piece n
```

**`AlgebraicGeometry.Space.conormalAlgebraEtaleRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraEtaleRestrictionGraded.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraEtaleRestrictionGraded.lean#L331). The attribute's comment: “the conormal algebra of an etale localisation, as graded algebras”.

> **Stacks 09RR.**  Let `i : Z ⟶ X` be a morphism of algebraic spaces, let `φ : U ⟶ X` be
> étale and let `Z_U = U ×_X Z`, with projections `p : Z_U ⟶ Z` and `i_U : Z_U ⟶ U`.  Then the
> restriction `p^*𝒞_{Z/X,*}` of the conormal algebra of `i` is the conormal algebra of `i_U`, as
> sheaves of graded `𝒪_{Z_U}`-algebras:
>
> `𝒞_{Z/X,*}|_{Z_U} = p^*𝒞_{Z/X,*} ≅ 𝒞_{Z_U/U,*}`.
>
> The isomorphism is canonical: it is the multiplicative composition comparison
> `p^*i^* ≅ (i_U ≫ φ)^* ≅ i_U^*φ^*` of Stacks 03LU followed by the inverse image along `i_U` of the
> identification `φ^*(⨁ 𝓘ⁿ) = ⨁ 𝓘_Uⁿ` of the graded algebras of the powers of the kernel ideal
> sheaves, which is Stacks 03LW in each degree.
>
> No hypothesis is imposed on `i` and `U` is an arbitrary algebraic space étale over `X`; for an
> immersion `i` and a scheme `U` this is the statement of Stacks 09RR.

```lean
noncomputable def conormalAlgebraEtaleRestrictionIso (p : ZU ⟶ Z) (iU : ZU ⟶ U) (i : Z ⟶ X)
    (φ : U ⟶ X) (sq : IsPullback p iU i φ) (hφ : IsEtale B S hS φ.hom) :
    (gradedPull (X := smallEtaleRingedTopos B S hS ZU) (Y := smallEtaleRingedTopos B S hS Z)
        (smallEtaleRingedToposHom B S hS p)).obj (conormalAlgebra B S hS i) ≅
      conormalAlgebra B S hS iU
```

**`AlgebraicGeometry.Space.conormalAlgebraEtaleRestrictionIso_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraEtaleRestrictionGraded.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraEtaleRestrictionGraded.lean#L388). The attribute's comment: “functoriality in U of the identification of conormal algebras”.

> **Stacks 09RR, functoriality in `U`.**  Let `i : Z ⟶ X` be a morphism of algebraic spaces and
> let `φ : U ⟶ X`, `φ' : U' ⟶ X` be étale, with cartesian squares `Z_U = U ×_X Z` and
> `Z_{U'} = U' ×_X Z`.  Let `ψ : U' ⟶ U` be a morphism over `X` and `q : Z_{U'} ⟶ Z_U` the
> induced morphism, so that `q ≫ p = p'` and `q ≫ i_U = i_{U'} ≫ ψ`.  Then the identification
> `𝒞_{Z/X,*}|_{Z_{U'}} ≅ 𝒞_{Z_{U'}/U',*}` of Stacks 09RR along `φ'` is the identification
> along `φ`, restricted along `q`, followed by the identification along `ψ`:
>
> `p'^*𝒞_{Z/X,*} ≅ q^*p^*𝒞_{Z/X,*} ≅ q^*𝒞_{Z_U/U,*} ≅ 𝒞_{Z_{U'}/U',*}`.

```lean
theorem conormalAlgebraEtaleRestrictionIso_comp (p : ZU ⟶ Z) (iU : ZU ⟶ U) (i : Z ⟶ X)
    (φ : U ⟶ X) (sq : IsPullback p iU i φ) (hφ : IsEtale B S hS φ.hom) (p' : ZU' ⟶ Z)
    (iU' : ZU' ⟶ U') (φ' : U' ⟶ X) (sq' : IsPullback p' iU' i φ')
    (hφ' : IsEtale B S hS φ'.hom) (ψ : U' ⟶ U) (hψφ : ψ ≫ φ = φ') (q : ZU' ⟶ ZU)
    (hqp : q ≫ p = p') (hqi : q ≫ iU = iU' ≫ ψ) :
    conormalAlgebraEtaleRestrictionIso B S hS p' iU' i φ' sq' hφ' =
      (gradedAlgebraPullbackCompIsoOfEq B S hS q p p' hqp.symm).app (conormalAlgebra B S hS i) ≪≫
        (gradedPull (X := smallEtaleRingedTopos B S hS ZU') (Y := smallEtaleRingedTopos B S hS ZU)
            (smallEtaleRingedToposHom B S hS q)).mapIso
          (conormalAlgebraEtaleRestrictionIso B S hS p iU i φ sq hφ) ≪≫
        conormalAlgebraEtaleRestrictionIso B S hS q iU' iU ψ
          (isPullback_of_comp_eq B S hS sq sq' ψ hψφ q hqp hqi)
          (isEtale_of_comp_eq B S hS ψ hφ hφ' hψφ)
```

**`AlgebraicGeometry.Space.conormalAlgebraOfImmersionEtaleRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraEtaleRestrictionGraded.lean, line 468](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraEtaleRestrictionGraded.lean#L468). The attribute's comment: “the conormal algebra of an immersion, restricted to an etale U, as graded algebras”.

> **Stacks 09RR, for the conormal algebra of an immersion as defined in Stacks 09RN.**  Let
> `i : Z ⟶ X` be an immersion of algebraic spaces, let `φ : U ⟶ X` be étale and let
> `Z_U = U ×_X Z`, with projections `p : Z_U ⟶ Z` and `i_U : Z_U ⟶ U`; then `i_U` is an
> immersion and
>
> `𝒞_{Z/X,*}|_{Z_U} = p^*𝒞_{Z/X,*} ≅ 𝒞_{Z_U/U,*}`
>
> as sheaves of graded `𝒪_{Z_U}`-algebras, where both conormal algebras are those of Stacks 09RN,
> `AlgebraicGeometry.Space.conormalAlgebraOfImmersion`.
>
> It is `AlgebraicGeometry.Space.conormalAlgebraEtaleRestrictionIso` read through the
> identification `AlgebraicGeometry.Space.conormalAlgebraIsoConormalAlgebraOfImmersion` on both
> sides.

```lean
noncomputable def conormalAlgebraOfImmersionEtaleRestrictionIso (hX : IsAlgebraicSpace B S hS X₀)
    (hZ : IsAlgebraicSpace B S hS Z₀) (i : Z₀ ⟶ X₀) (hi : IsImmersion B S hS i)
    {U ZU : AlgebraicSpaces B S hS} (p : ZU ⟶ ⟨Z₀, hZ⟩) (iU : ZU ⟶ U) (φ : U ⟶ ⟨X₀, hX⟩)
    (sq : IsPullback p iU
      (ObjectProperty.homMk i : (⟨Z₀, hZ⟩ : AlgebraicSpaces B S hS) ⟶ ⟨X₀, hX⟩) φ)
    (hφ : IsEtale B S hS φ.hom) :
    (gradedPull (X := smallEtaleRingedTopos B S hS ZU)
        (Y := smallEtaleRingedTopos B S hS ⟨Z₀, hZ⟩) (smallEtaleRingedToposHom B S hS p)).obj
        (conormalAlgebraOfImmersion B S hS hX hZ i hi) ≅
      conormalAlgebraOfImmersion B S hS U.2 ZU.2 iU.hom (isImmersion_of_isPullback B S hS sq hi)
```

**`AlgebraicGeometry.Space.conormalAlgebraOfImmersionEtaleRestrictionIso_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraEtaleRestrictionGraded.lean, line 494](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraEtaleRestrictionGraded.lean#L494). The attribute's comment: “functoriality in U, for the conormal algebra of an immersion”.

> **Stacks 09RR, functoriality in `U`, for the conormal algebra of an immersion as defined in
> Stacks 09RN.**  Let `i : Z ⟶ X` be an immersion and let `φ : U ⟶ X`, `φ' : U' ⟶ X` be étale, with
> cartesian squares `Z_U = U ×_X Z` and `Z_{U'} = U' ×_X Z`.  Let `ψ : U' ⟶ U` be a morphism over
> `X` and `q : Z_{U'} ⟶ Z_U` the induced morphism, so that `q ≫ p = p'` and `q ≫ i_U = i_{U'} ≫ ψ`.
> Then the identification `𝒞_{Z/X,*}|_{Z_{U'}} ≅ 𝒞_{Z_{U'}/U',*}` along `φ'` is the identification
> along `φ`, restricted along `q`, followed by the identification along `ψ` for the immersion
> `i_U`.

```lean
theorem conormalAlgebraOfImmersionEtaleRestrictionIso_comp (hX : IsAlgebraicSpace B S hS X₀)
    (hZ : IsAlgebraicSpace B S hS Z₀) (i : Z₀ ⟶ X₀) (hi : IsImmersion B S hS i)
    {U ZU U' ZU' : AlgebraicSpaces B S hS} (p : ZU ⟶ ⟨Z₀, hZ⟩) (iU : ZU ⟶ U)
    (φ : U ⟶ ⟨X₀, hX⟩)
    (sq : IsPullback p iU
      (ObjectProperty.homMk i : (⟨Z₀, hZ⟩ : AlgebraicSpaces B S hS) ⟶ ⟨X₀, hX⟩) φ)
    (hφ : IsEtale B S hS φ.hom) (p' : ZU' ⟶ ⟨Z₀, hZ⟩) (iU' : ZU' ⟶ U') (φ' : U' ⟶ ⟨X₀, hX⟩)
    (sq' : IsPullback p' iU'
      (ObjectProperty.homMk i : (⟨Z₀, hZ⟩ : AlgebraicSpaces B S hS) ⟶ ⟨X₀, hX⟩) φ')
    (hφ' : IsEtale B S hS φ'.hom) (ψ : U' ⟶ U) (hψφ : ψ ≫ φ = φ') (q : ZU' ⟶ ZU)
    (hqp : q ≫ p = p') (hqi : q ≫ iU = iU' ≫ ψ) :
    conormalAlgebraOfImmersionEtaleRestrictionIso B S hS hX hZ i hi p' iU' φ' sq' hφ' =
      (gradedAlgebraPullbackCompIsoOfEq B S hS q p p' hqp.symm).app
          (conormalAlgebraOfImmersion B S hS hX hZ i hi) ≪≫
        (gradedPull (X := smallEtaleRingedTopos B S hS ZU') (Y := smallEtaleRingedTopos B S hS ZU)
            (smallEtaleRingedToposHom B S hS q)).mapIso
          (conormalAlgebraOfImmersionEtaleRestrictionIso B S hS hX hZ i hi p iU φ sq hφ) ≪≫
        conormalAlgebraOfImmersionEtaleRestrictionIso B S hS U.2 ZU.2 iU.hom
          (isImmersion_of_isPullback B S hS sq hi) q iU' ψ
          (isPullback_of_comp_eq B S hS sq sq' ψ hψφ q hqp hqi)
          (isEtale_of_comp_eq B S hS ψ hφ hφ' hψφ)
```

## Tag 09RS, a lemma

[Tag 09RS](https://stacks.math.columbia.edu/tag/09RS) in the Stacks Project.

**`AlgebraicGeometry.Space.conormalAlgebraOfImmersionSquareMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraOfImmersionSquareMap.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraOfImmersionSquareMap.lean#L229). The attribute's comment: “the canonical map f^*𝒞\_\{Z'/X',*} ⟶ 𝒞\_\{Z/X,*} for immersions i, i', on the conormal algebras of immersions of Tag 09RN”.

> **[Stacks Project, Tag 09RS] for a square of immersions, on the conormal algebras of
> [Stacks Project, Tag 09RN].**  Let
>
> ```
> Z --i--→ X
> |        |
> f        g
> ↓        ↓
> Z' -i'-→ X'
> ```
>
> be a commutative square of algebraic spaces over `S` with `i` and `i'` immersions.  There is a
> canonical homomorphism of sheaves of graded `𝒪_Z`-algebras
>
> `f^*𝒞_{Z'/X',*} ⟶ 𝒞_{Z/X,*}`,
>
> where `𝒞_{Z/X,*}` is the conormal algebra of the immersion `i`, that is of its closed
> factorisation `i₀ : Z ⟶ X ∖ ∂Z` (`AlgebraicGeometry.Space.conormalAlgebraOfImmersion`), and
> likewise for `i'`.
>
> It is the inverse image along `f` of the inverse of the isomorphism
> `AlgebraicGeometry.Space.conormalAlgebraOfImmersionIso` for `i'`, then the composition
> comparison `f^*𝟙^* ≅ f^*`, then the canonical map
> `AlgebraicGeometry.Space.conormalAlgebraSquareMap` of the commutative square with edges `i₀`,
> `ι ≫ g`, `f` and `i'`; the last is built from `g^♯` exactly as in the source's proof.

```lean
noncomputable def conormalAlgebraOfImmersionSquareMap (i : 𝒵 ⟶ 𝒳) (i' : 𝒵' ⟶ 𝒳')
    (f : 𝒵 ⟶ 𝒵') (g : 𝒳 ⟶ 𝒳') (hsq : i ≫ g = f ≫ i') (hi : IsImmersion B S hS i.hom)
    (hi' : IsImmersion B S hS i'.hom) :
    (gradedPull (X := smallEtaleRingedTopos B S hS 𝒵) (Y := smallEtaleRingedTopos B S hS 𝒵')
        (smallEtaleRingedToposHom B S hS f)).obj
        (conormalAlgebraOfImmersion B S hS hX' hZ' i'.hom hi') ⟶
      conormalAlgebraOfImmersion B S hS hX hZ i.hom hi
```

**`AlgebraicGeometry.Space.conormalAlgebraSquareMapOfPullbackHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraSquareMap.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraSquareMap.lean#L323). The attribute's comment: “the canonical map, given the ambient homomorphism g^*(⨁ 𝓙ⁿ) ⟶ ⨁ 𝓘ⁿ”.

> **The canonical map of conormal algebras of [Stacks Project, Tag 09RS], given the ambient
> graded homomorphism.**  Let
>
> ```
> Z --i--→ X
> |        |
> f        g
> ↓        ↓
> Z' -i'-→ X'
> ```
>
> be a commutative square of algebraic spaces, `hsq : i ≫ g = f ≫ i'`.  Write
> `𝓘 = Ker(i^♯) ⊆ 𝒪_X` and `𝓙 = Ker((f ≫ i')^♯) ⊆ 𝒪_{X'}` for the kernel ideal sheaf of the
> diagonal.  Given a homomorphism of sheaves of graded `𝒪_X`-algebras
>
> `Ψ : g^*(⨁_{n ≥ 0} 𝓙ⁿ) ⟶ ⨁_{n ≥ 0} 𝓘ⁿ`
>
> on the ambient space, there is a canonical homomorphism of sheaves of graded `𝒪_Z`-algebras
>
> `f^*𝒞_{Z'/X',*} ⟶ 𝒞_{Z/X,*}`.
>
> It is the composite of the two factors of the source's proof: the unconditional first factor
> `AlgebraicGeometry.Space.conormalAlgebraPullbackCompMap`, which carries `f^*𝒞_{Z'/X',*}` into the
> conormal algebra `𝒞_{Z/X',*}` of the diagonal and rests on the containment of kernel ideal
> sheaves `AlgebraicGeometry.Space.kernelIdealSheaf_le_comp`, followed by the ambient factor
> `AlgebraicGeometry.Space.conormalAlgebraAmbientSquareMapOfPullbackHom`, which descends `Ψ` from
> `X` to `Z` along the Stacks 03LU composition comparison.
>
> `Ψ` is a hypothesis and not the conclusion: it is a homomorphism upstairs on the ambient space
> `X` between the graded algebras of the powers of the two kernel ideal sheaves, whereas the
> conclusion is a homomorphism downstairs on `Z` between the conormal algebras of the two vertical
> arrows.  The module documentation of
> `StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraAmbientGradedTransport.lean` records that no
> such `Ψ` is constructed yet and what its construction is waiting for.
>
> The statement takes `i` and `i'` to be arbitrary morphisms, where Stacks 09RS takes them to be
> immersions; nothing here uses any property of them, so this is strictly more general and
> specialises to the source's statement.

```lean
noncomputable def conormalAlgebraSquareMapOfPullbackHom (i : Z ⟶ X) (i' : Z' ⟶ X') (f : Z ⟶ Z')
    (g : X ⟶ X') (hsq : i ≫ g = f ≫ i')
    (Ψ : (gradedPull (X := smallEtaleRingedTopos B S hS X)
          (Y := smallEtaleRingedTopos B S hS X') (smallEtaleRingedToposHom B S hS g)).obj
        (kernelIdealGradedAlgebra B S hS (f ≫ i')) ⟶ kernelIdealGradedAlgebra B S hS i) :
    (gradedPull (X := smallEtaleRingedTopos B S hS Z)
        (Y := smallEtaleRingedTopos B S hS Z')
        (smallEtaleRingedToposHom B S hS f)).obj (conormalAlgebra B S hS i') ⟶
      conormalAlgebra B S hS i
```

**`AlgebraicGeometry.Space.conormalAlgebraSquareMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/KernelIdealGradedPushforward.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/KernelIdealGradedPushforward.lean#L377). The attribute's comment: “the canonical map f^*𝒞\_\{Z'/X',*} ⟶ 𝒞\_\{Z/X,*} of graded algebras”.

> **[Stacks Project, Tag 09RS]: the canonical map of conormal algebras of a commutative
> square.**  Let
>
> ```
> Z --i--→ X
> |        |
> f        g
> ↓        ↓
> Z' -i'-→ X'
> ```
>
> be a commutative square of algebraic spaces over `S`, `hsq : i ≫ g = f ≫ i'`.  There is a
> canonical homomorphism of sheaves of graded `𝒪_Z`-algebras
>
> `f^*𝒞_{Z'/X',*} ⟶ 𝒞_{Z/X,*}`.
>
> It is `AlgebraicGeometry.Space.conormalAlgebraSquareMapOfPullbackHom` at the ambient
> homomorphism `AlgebraicGeometry.Space.kernelIdealGradedPullbackHom : g^*(⨁ 𝓙ⁿ) ⟶ ⨁ 𝓘ⁿ` induced
> by `g^♯`, where `𝓘 = Ker(i^♯)` and `𝓙 = Ker((f ≫ i')^♯)`: the first factor
> `f^*𝒞_{Z'/X',*} ⟶ 𝒞_{Z/X',*}` comes from the containment `Ker((i')^♯) ⊆ 𝓙`, and the second
> factor `𝒞_{Z/X',*} ⟶ 𝒞_{Z/X,*}` is the inverse image along `i` of the ambient homomorphism, read
> through the Stacks 03LU composition comparison `(f ≫ i')^* ≅ i^* g^*`.  This is the source's
> proof: `g^♯` carries `g^{-1}((𝓘')ⁿ)` into `𝓘ⁿ`, and pulling back to `Z`, with
> `i^{-1}g^{-1} = f^{-1}(i')^{-1}`, gives the map in each degree.
>
> The statement takes `i` and `i'` to be arbitrary morphisms, where Stacks 09RS takes them to be
> immersions; nothing here uses any property of them.

```lean
noncomputable def conormalAlgebraSquareMap (i : Z ⟶ X) (i' : Z' ⟶ X') (f : Z ⟶ Z')
    (g : X ⟶ X') (hsq : i ≫ g = f ≫ i') :
    (gradedPull (X := smallEtaleRingedTopos B S hS Z)
        (Y := smallEtaleRingedTopos B S hS Z')
        (smallEtaleRingedToposHom B S hS f)).obj (conormalAlgebra B S hS i') ⟶
      conormalAlgebra B S hS i
```

## Tag 09RT, a lemma

[Tag 09RT](https://stacks.math.columbia.edu/tag/09RT) in the Stacks Project.

**`AlgebraicGeometry.Space.epi_conormalAlgebraOfImmersionSquareMap_app_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraOfImmersionSquareMapCartesian.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraOfImmersionSquareMapCartesian.lean#L159). The attribute's comment: “surjectivity: for a cartesian square with i, i' immersions, the canonical map f^*𝒞\_\{Z'/X',*} ⟶ 𝒞\_\{Z/X,*} of Tag 09RS on the conormal algebras of immersions of Tag 09RN is surjective in every degree”.

> **[Stacks Project, Tag 09RT], surjectivity, on the conormal algebras of immersions.**  Let
>
> ```
> Z --i--→ X
> |        |
> f        g
> ↓        ↓
> Z' -i'-→ X'
> ```
>
> be a cartesian square of algebraic spaces with `i` and `i'` immersions.  Then the canonical map
> `f^*𝒞_{Z'/X',*} ⟶ 𝒞_{Z/X,*}` of [Stacks Project, Tag 09RS] between the conormal algebras of the
> immersions of [Stacks Project, Tag 09RN]
> (`AlgebraicGeometry.Space.conormalAlgebraOfImmersionSquareMap`) is surjective: it is an
> epimorphism of `𝒪_Z`-modules in every degree.
>
> The map is two isomorphisms followed by the canonical map of the square of the closed
> factorisation of `i`, which is cartesian
> (`AlgebraicGeometry.Space.isPullback_immersionClosedFactorization_comp`), so that
> `AlgebraicGeometry.Space.epi_conormalAlgebraSquareMap_app_of_isPullback` applies.

```lean
theorem epi_conormalAlgebraOfImmersionSquareMap_app_of_isPullback {i : 𝒵 ⟶ 𝒳} {i' : 𝒵' ⟶ 𝒳'}
    {f : 𝒵 ⟶ 𝒵'} {g : 𝒳 ⟶ 𝒳'} (sq : IsPullback i f g i') (hi : IsImmersion B S hS i.hom)
    (hi' : IsImmersion B S hS i'.hom) (n : ℤ) :
    Epi ((conormalAlgebraOfImmersionSquareMap B S hS hZ hX hZ' hX' i i' f g sq.w hi hi').app
      n)
```

**`AlgebraicGeometry.Space.isIso_conormalAlgebraOfImmersionSquareMap_of_isPullback_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraOfImmersionSquareMapCartesian.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraOfImmersionSquareMapCartesian.lean#L199). The attribute's comment: “flat case: for a cartesian square with i, i' immersions and g flat, the canonical map f^*𝒞\_\{Z'/X',*} ⟶ 𝒞\_\{Z/X,*} of Tag 09RS on the conormal algebras of immersions of Tag 09RN is an isomorphism of graded algebras”.

> **[Stacks Project, Tag 09RT], the flat case, on the conormal algebras of immersions.**  Let
>
> ```
> Z --i--→ X
> |        |
> f        g
> ↓        ↓
> Z' -i'-→ X'
> ```
>
> be a cartesian square of algebraic spaces with `i` and `i'` immersions.  If `g` is flat, the
> canonical map `f^*𝒞_{Z'/X',*} ⟶ 𝒞_{Z/X,*}` of [Stacks Project, Tag 09RS] between the conormal
> algebras of the immersions of [Stacks Project, Tag 09RN]
> (`AlgebraicGeometry.Space.conormalAlgebraOfImmersionSquareMap`) is an isomorphism of sheaves of
> graded `𝒪_Z`-algebras.
>
> The map is two isomorphisms followed by the canonical map of the square of the closed
> factorisation of `i`, which is cartesian
> (`AlgebraicGeometry.Space.isPullback_immersionClosedFactorization_comp`) with flat right edge
> `ι ≫ g` (an open immersion is étale, hence flat, and flatness composes), so that
> `AlgebraicGeometry.Space.isIso_conormalAlgebraSquareMap_of_isPullback_of_isFlat` applies.

```lean
theorem isIso_conormalAlgebraOfImmersionSquareMap_of_isPullback_of_isFlat {i : 𝒵 ⟶ 𝒳}
    {i' : 𝒵' ⟶ 𝒳'} {f : 𝒵 ⟶ 𝒵'} {g : 𝒳 ⟶ 𝒳'} (sq : IsPullback i f g i')
    (hi : IsImmersion B S hS i.hom) (hi' : IsImmersion B S hS i'.hom)
    (hg : IsFlat B S hS g.hom) :
    IsIso (conormalAlgebraOfImmersionSquareMap B S hS hZ hX hZ' hX' i i' f g sq.w hi hi')
```

**`AlgebraicGeometry.Space.epi_conormalAlgebraSquareMap_app_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraSquareMapCartesian.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraSquareMapCartesian.lean#L245). The attribute's comment: “surjectivity: for a cartesian square with i' (hence i) an immersion, the canonical map f^*𝒞\_\{Z'/X',*} ⟶ 𝒞\_\{Z/X,*} of Tag 09RS is surjective in every degree”.

> **[Stacks Project, Tag 09RT], surjectivity.**  Let
>
> ```
> Z --i--→ X
> |        |
> f        g
> ↓        ↓
> Z' -i'-→ X'
> ```
>
> be a cartesian square of algebraic spaces with `i'` (hence `i`) an immersion.  Then the canonical
> map `f^*𝒞_{Z'/X',*} ⟶ 𝒞_{Z/X,*}` of [Stacks Project, Tag 09RS] is surjective: it is an
> epimorphism of `𝒪_Z`-modules in every degree.
>
> In degree `n ≥ 0` the map is the inverse image along `i` of the degree-`n` ambient comparison,
> preceded by two isomorphisms; that comparison is induced by pullback of regular functions
> (`AlgebraicGeometry.Space.isInducedByPullback_conormalAlgebraSquareAmbientComparison_app`), so its
> inverse image along `i` is an epimorphism by
> `AlgebraicGeometry.Space.epi_modulePullback_map_of_isPullback`.  In negative degrees the target
> vanishes.

```lean
theorem epi_conormalAlgebraSquareMap_app_of_isPullback (sq : IsPullback i f g i')
    (hi' : IsImmersion B S hS i'.hom) (n : ℤ) :
    Epi ((conormalAlgebraSquareMap B S hS i i' f g sq.w).app n)
```

**`AlgebraicGeometry.Space.isIso_conormalAlgebraSquareMap_of_isPullback_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraSquareMapCartesian.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraSquareMapCartesian.lean#L310). The attribute's comment: “flat case: for a cartesian square with i' (hence i) an immersion and g flat, the canonical map f^*𝒞\_\{Z'/X',*} ⟶ 𝒞\_\{Z/X,*} of Tag 09RS is an isomorphism of graded algebras”.

> **[Stacks Project, Tag 09RT], the flat case.**  Let
>
> ```
> Z --i--→ X
> |        |
> f        g
> ↓        ↓
> Z' -i'-→ X'
> ```
>
> be a cartesian square of algebraic spaces with `i'` (hence `i`) an immersion.  If `g` is flat,
> the canonical map `f^*𝒞_{Z'/X',*} ⟶ 𝒞_{Z/X,*}` of [Stacks Project, Tag 09RS] is an isomorphism
> of sheaves of graded `𝒪_Z`-algebras.
>
> Degreewise this is
> `AlgebraicGeometry.Space.isIso_conormalAlgebraSquareMap_app_of_isPullback_of_isFlat`, whose
> nonnegative degrees are `AlgebraicGeometry.Space.isIso_modulePullback_map_of_isPullback_of_isFlat`
> for the ambient comparison; a degreewise isomorphism of sheaves of graded algebras is an
> isomorphism.

```lean
theorem isIso_conormalAlgebraSquareMap_of_isPullback_of_isFlat (sq : IsPullback i f g i')
    (hi' : IsImmersion B S hS i'.hom) (hg : IsFlat B S hS g.hom) :
    IsIso (conormalAlgebraSquareMap B S hS i i' f g sq.w)
```

**`AlgebraicGeometry.Space.epi_conormalAlgebraSquareMapOfPullbackHom_app_of_nonneg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraSquareMapDegreePropagation.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraSquareMapDegreePropagation.lean#L223). The attribute's comment: “the surjectivity clause, in every nonnegative degree; the cartesian hypothesis is NOT consumed, three inputs being carried: hunit, h0 and h1, the degree-one one being Tag 04CQ's surjectivity clause in ideal-sheaf form transported to this square; the flat clause is isIso\_conormalAlgebraSquareMapOfPullbackHom\_app\_of\_isFlat”.

> **The surjectivity clause of [Stacks Project, Tag 09RT].**  The canonical map
> `f^*𝒞_{Z'/X',*} ⟶ 𝒞_{Z/X,*}` of [Stacks Project, Tag 09RS] is surjective in every nonnegative
> degree.
>
> The ambient comparison is surjective in every nonnegative degree by
> `AlgebraicGeometry.Space.epi_conormalAlgebraSquareAmbientComparison_app_of_nonneg`, and the
> canonical map is in each degree the inverse image along `i` of the ambient comparison preceded by
> two isomorphisms.
>
> Three inputs are carried: that the ambient comparison carries the unit, and its surjectivity in
> the degrees zero and one — the conclusions of
> `AlgebraicGeometry.Space.epi_structureSheafMap` and of
> `AlgebraicGeometry.Space.epi_idealSheafMap`, the ideal-sheaf form of
> [Stacks Project, Tag 04CQ]'s surjectivity clause, transported to this square.  The square being
> cartesian is therefore not consumed, and neither is either vertical arrow being an immersion.
> What is proved is that the three suffice: surjectivity propagates from the degrees zero and one
> to every degree.  The module documentation says why none of the three is available in the
> library, and why carrying the degree-one one is carrying 04CQ's conclusion and not this tag's.

```lean
theorem epi_conormalAlgebraSquareMapOfPullbackHom_app_of_nonneg (i : Z ⟶ X) (i' : Z' ⟶ X')
    (f : Z ⟶ Z') (g : X ⟶ X') (hsq : i ≫ g = f ≫ i')
    (Ψ : (gradedPull (X := smallEtaleRingedTopos B S hS X)
          (Y := smallEtaleRingedTopos B S hS X') (smallEtaleRingedToposHom B S hS g)).obj
        (kernelIdealGradedAlgebra B S hS (f ≫ i')) ⟶ kernelIdealGradedAlgebra B S hS i)
    (hunit : SheafOfModules.sectionsMap
        ((conormalAlgebraSquareAmbientComparison B S hS i i' f g Ψ).app 0)
        ((gradedPull (X := smallEtaleRingedTopos B S hS X)
            (Y := smallEtaleRingedTopos B S hS X')
            (smallEtaleRingedToposHom B S hS g)).obj
          (kernelIdealGradedAlgebra B S hS i')).one =
      (kernelIdealGradedAlgebra B S hS i).one)
    (h0 : Epi ((conormalAlgebraSquareAmbientComparison B S hS i i' f g Ψ).app 0))
    (h1 : Epi ((conormalAlgebraSquareAmbientComparison B S hS i i' f g Ψ).app 1))
    (n : ℤ) (hn : 0 ≤ n) :
    Epi ((conormalAlgebraSquareMapOfPullbackHom B S hS i i' f g hsq Ψ).app n)
```

**`AlgebraicGeometry.Space.isIso_conormalAlgebraSquareMapOfPullbackHom_app_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraSquareMapFlatClause.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebraSquareMapFlatClause.lean#L246). The attribute's comment: “the flat clause: an isomorphism in every nonnegative degree when g is flat, flatness consumed through exactness of the inverse image; the cartesian hypothesis is NOT consumed, four inputs being carried: hunit, h0, h1 (Tag 04CQ's flat half transported) and hiota (the n-th power analogue of idealSheafMap\_comp\_ι); see the module docs”.

> **The flat clause of [Stacks Project, Tag 09RT].**  If `g` is flat — that is, if the morphism
> of small étale ringed topoi it induces is flat in the sense of [Stacks Project, Tag 04JB] — then
> the canonical map `f^*𝒞_{Z'/X',*} ⟶ 𝒞_{Z/X,*}` of [Stacks Project, Tag 09RS] is an isomorphism in
> every nonnegative degree.
>
> Flatness is consumed in the injectivity half, through the exactness of the inverse image along a
> flat morphism.  Four inputs are carried: that the ambient comparison carries the unit, its
> invertibility in the degrees zero and one — the conclusions of
> `AlgebraicGeometry.Space.isIso_structureSheafMap` and of the flat half of
> [Stacks Project, Tag 04CQ], `AlgebraicGeometry.Space.isIso_idealSheafMap_of_isFlat`, transported
> to this square — and the compatibility of the comparison with the embeddings of the powers of the
> two ideal sheaves into the two structure sheaves, whose degree-one instance is
> `AlgebraicGeometry.Space.idealSheafMap_comp_ι`.  The square being cartesian is therefore not
> consumed, and neither is either vertical arrow being an immersion.  What is proved is that the
> four suffice: surjectivity and injectivity propagate from the degrees zero and one to every
> degree.  The module documentation says why none of the four is available in the library.

```lean
theorem isIso_conormalAlgebraSquareMapOfPullbackHom_app_of_isFlat (i : Z ⟶ X) (i' : Z' ⟶ X')
    (f : Z ⟶ Z') (g : X ⟶ X') (hsq : i ≫ g = f ≫ i')
    (Ψ : (gradedPull (X := smallEtaleRingedTopos B S hS X)
          (Y := smallEtaleRingedTopos B S hS X') (smallEtaleRingedToposHom B S hS g)).obj
        (kernelIdealGradedAlgebra B S hS (f ≫ i')) ⟶ kernelIdealGradedAlgebra B S hS i)
    (hg : (smallEtaleRingedToposHom B S hS g).IsFlat)
    (hunit : SheafOfModules.sectionsMap
        ((conormalAlgebraSquareAmbientComparison B S hS i i' f g Ψ).app 0)
        ((gradedPull (X := smallEtaleRingedTopos B S hS X)
            (Y := smallEtaleRingedTopos B S hS X')
            (smallEtaleRingedToposHom B S hS g)).obj
          (kernelIdealGradedAlgebra B S hS i')).one =
      (kernelIdealGradedAlgebra B S hS i).one)
    (h0 : IsIso ((conormalAlgebraSquareAmbientComparison B S hS i i' f g Ψ).app 0))
    (h1 : IsIso ((conormalAlgebraSquareAmbientComparison B S hS i i' f g Ψ).app 1))
    (hι : ∀ n : ℤ, 0 ≤ n →
      (conormalAlgebraSquareAmbientComparison B S hS i i' f g Ψ).app n ≫
          (kernelIdealSheafZPow B S hS i n).ι =
        (modulePullback B S hS g).map (kernelIdealSheafZPow B S hS i' n).ι ≫
          structureSheafMap B S hS g)
    (n : ℤ) (hn : 0 ≤ n) :
    IsIso ((conormalAlgebraSquareMapOfPullbackHom B S hS i i' f g hsq Ψ).app n)
```

## Tag 09RU, a definition

[Tag 09RU](https://stacks.math.columbia.edu/tag/09RU) in the Stacks Project.

**`AlgebraicGeometry.Space.immersionNormalCone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalConeRelativeSpectrum.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalConeRelativeSpectrum.lean#L155). The attribute's comment: “the normal cone C\_ZX = Spec\_Z(C\_\{Z/X,*}) of an immersion, as an algebraic space affine over Z”.

> **Stacks Project, Tag 09RU.  The normal cone `C_ZX = \underline{Spec}_Z(𝒞_{Z/X,*})` of an
> immersion `i : Z ⟶ X` of algebraic spaces**, as an algebraic space affine over `Z`: the relative
> spectrum (Stacks 081W) of the conormal algebra of Stacks 09RN.  Its structure morphism is affine
> (this is the `AffineOver` property) and the direct image of its structure sheaf is `𝒞_{Z/X,*}`
> (`AlgebraicGeometry.Space.immersionNormalConePushforwardIso`).

```lean
def immersionNormalCone (hX : IsAlgebraicSpace B S hS X₀) (hZ : IsAlgebraicSpace B S hS Z₀)
    (i : Z₀ ⟶ X₀) (hi : IsImmersion B S hS i) :
    AffineOver B S hS (⟨Z₀, hZ⟩ : AlgebraicSpaces B S hS)
```

**`AlgebraicGeometry.Space.immersionNormalConePushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalConeRelativeSpectrum.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalConeRelativeSpectrum.lean#L167). The attribute's comment: “the direct image of the structure sheaf of the normal cone C\_ZX is the conormal algebra C\_\{Z/X,*}, i.e. C\_ZX = Spec\_Z(C\_\{Z/X,*})”.

> **Stacks Project, Tag 09RU.  `C_ZX` is the relative spectrum of `𝒞_{Z/X,*}`**: for its
> projection `π : C_ZX ⟶ Z`, `π_* 𝒪_{C_ZX} ≅ 𝒞_{Z/X,*}` as sheaves of commutative
> `𝒪_Z`-algebras.

```lean
def immersionNormalConePushforwardIso (hX : IsAlgebraicSpace B S hS X₀)
    (hZ : IsAlgebraicSpace B S hS Z₀) (i : Z₀ ⟶ X₀) (hi : IsImmersion B S hS i) :
    pushforwardAlgebra B S hS (immersionNormalCone B S hS hX hZ i hi).obj ≅
      conormalAlgebraSheafOfImmersion B S hS hX hZ i hi
```

**`AlgebraicGeometry.Space.immersionNormalBundle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalConeRelativeSpectrum.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalConeRelativeSpectrum.lean#L180). The attribute's comment: “the normal bundle N\_ZX = Spec\_Z(Sym(C\_\{Z/X})) of an immersion, as an algebraic space affine over Z”.

> **Stacks Project, Tag 09RU.  The normal bundle `N_ZX = \underline{Spec}_Z(Sym(𝒞_{Z/X}))` of
> an immersion `i : Z ⟶ X` of algebraic spaces**, as an algebraic space affine over `Z`: the
> relative spectrum (Stacks 081W) of the symmetric algebra on the conormal sheaf `𝒞_{Z/X}` of
> Stacks 04CN.  Its structure morphism is affine and the direct image of its structure sheaf is
> `Sym(𝒞_{Z/X})` (`AlgebraicGeometry.Space.immersionNormalBundlePushforwardIso`).

```lean
def immersionNormalBundle (hX : IsAlgebraicSpace B S hS X₀) (hZ : IsAlgebraicSpace B S hS Z₀)
    (i : Z₀ ⟶ X₀) (hi : IsImmersion B S hS i) :
    AffineOver B S hS (⟨Z₀, hZ⟩ : AlgebraicSpaces B S hS)
```

**`AlgebraicGeometry.Space.immersionNormalBundlePushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalConeRelativeSpectrum.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalConeRelativeSpectrum.lean#L192). The attribute's comment: “the direct image of the structure sheaf of the normal bundle N\_ZX is Sym(C\_\{Z/X}), i.e. N\_ZX = Spec\_Z(Sym(C\_\{Z/X}))”.

> **Stacks Project, Tag 09RU.  `N_ZX` is the relative spectrum of `Sym(𝒞_{Z/X})`**: for its
> projection `π : N_ZX ⟶ Z`, `π_* 𝒪_{N_ZX} ≅ Sym(𝒞_{Z/X})` as sheaves of commutative
> `𝒪_Z`-algebras.

```lean
def immersionNormalBundlePushforwardIso (hX : IsAlgebraicSpace B S hS X₀)
    (hZ : IsAlgebraicSpace B S hS Z₀) (i : Z₀ ⟶ X₀) (hi : IsImmersion B S hS i) :
    pushforwardAlgebra B S hS (immersionNormalBundle B S hS hX hZ i hi).obj ≅
      conormalSymmetricAlgebraSheafOfImmersion B S hS hX hZ i hi
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.6, Tag 09RM](https://stacks.math.columbia.edu/tag/09RM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
