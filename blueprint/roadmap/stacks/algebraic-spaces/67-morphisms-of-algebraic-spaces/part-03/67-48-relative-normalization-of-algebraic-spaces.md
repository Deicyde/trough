---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.AlgebraSheaf.range_integralClosureInclusion_app_eq_integralClosure', AlgebraicGeometry.Space.AlgebraSheaf.isQuasicoherent_integralClosureSheaf, AlgebraicGeometry.Space.AlgebraSheaf.integralClosureSheaf, AlgebraicGeometry.Space.AlgebraSheaf.integralClosureInclusion, AlgebraicGeometry.Space.normalizationIn, AlgebraicGeometry.Space.toNormalizationIn, AlgebraicGeometry.Space.normalizationInQcqsHom, AlgebraicGeometry.Space.isAffineHom_normalizationInQcqsHom
statement: formalized
proof: formalized
---

# 67.48 Relative normalization of algebraic spaces

Section 67.48 of the Stacks Project, [Tag 0BAZ](https://stacks.math.columbia.edu/tag/0BAZ). 11 tags here are carried by 37 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0820, a lemma

[Tag 0820](https://stacks.math.columbia.edu/tag/0820) in the Stacks Project.

**`AlgebraicGeometry.Space.AlgebraSheaf.range_integralClosureInclusion_app_eq_integralClosure'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralClosureQuasicoherent.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntegralClosureQuasicoherent.lean#L357). The attribute's comment: “the sections of the integral closure over an affine chart”.

> The sections of the integral closure of the structure sheaf in a quasi-coherent algebra
> sheaf over an affine étale chart are the integral closure of the ring of functions on the chart
> in the sections of the algebra over it.

```lean
theorem range_integralClosureInclusion_app_eq_integralClosure'
    (A : AlgebraSheaf.{u, u} B S hS F hF) (hA : A.IsQuasicoherent) (U : SmallEtale B S hS F)
    (hU : IsAffine ((SmallEtale.toOver B S hS F ⋙ BigFppfOver.toScheme B S hS).obj U)) :
    letI : Algebra ((structureSheaf B S hS F hF).obj.obj (op U))
        (A.right.obj.obj (op U)) := (A.algebraMap (op U)).toAlgebra
    Set.range (((integralClosureInclusion A).right.hom.app (op U)).hom) =
      (integralClosure ((structureSheaf B S hS F hF).obj.obj (op U))
        (A.right.obj.obj (op U)) : Set _)
```

**`AlgebraicGeometry.Space.AlgebraSheaf.isQuasicoherent_integralClosureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralClosureQuasicoherent.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntegralClosureQuasicoherent.lean#L410). The attribute's comment: “quasi-coherence of the integral closure”.

> **Quasi-coherence of the integral closure.**  The integral closure of the structure sheaf in a
> quasi-coherent sheaf of `𝒪_F`-algebras is again a quasi-coherent sheaf of `𝒪_F`-algebras.

```lean
theorem isQuasicoherent_integralClosureSheaf (A : AlgebraSheaf.{u, u} B S hS F hF)
    (hA : A.IsQuasicoherent) : (integralClosureSheaf A).IsQuasicoherent
```

## Tag 0821, a definition

[Tag 0821](https://stacks.math.columbia.edu/tag/0821) in the Stacks Project.

**`AlgebraicGeometry.Space.AlgebraSheaf.integralClosureSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralClosureSheaf.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntegralClosureSheaf.lean#L356). The attribute's comment: “the integral closure of the structure sheaf in an algebra”.

> **The integral closure of the structure sheaf in an algebra sheaf.**  Its sections over a
> chart are the locally integral sections of `A`, and the structure-algebra map is the one of
> `A`, whose values are integral.
>
> This is the subalgebra of Stacks 0820 as data, which is what Stacks 0821 names; the two
> assertions the source makes about it are discussed in the implementation notes.

```lean
def integralClosureSheaf (A : AlgebraSheaf.{u, m} B S hS F hF) :
    AlgebraSheaf.{u, m} B S hS F hF
```

**`AlgebraicGeometry.Space.AlgebraSheaf.integralClosureInclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralClosureSheaf.lean, line 368](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntegralClosureSheaf.lean#L368). The attribute's comment: “the inclusion exhibiting the integral closure as a subalgebra”.

> The inclusion of the integral closure into the algebra, as a morphism of algebra sheaves.
> On each chart it is the inclusion of the subring of locally integral sections.  It is what makes
> the integral closure a *subalgebra* of `A`, as Stacks 0821 names it.

```lean
def integralClosureInclusion (A : AlgebraSheaf.{u, m} B S hS F hF) :
    integralClosureSheaf A ⟶ A
```

## Tag 0822, a definition

[Tag 0822](https://stacks.math.columbia.edu/tag/0822) in the Stacks Project.

**`AlgebraicGeometry.Space.normalizationIn`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationIn.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationIn.lean#L115). The attribute's comment: “the normalization of X in Y”.

> **The normalization of `X` in `Y`.**  For a morphism `f : Y ⟶ X` of algebraic spaces whose
> direct image `f_* 𝒪_Y` is quasi-coherent, it is the relative spectrum
> `ν : X' = \underline{Spec}_X(𝒪') ⟶ X` of the integral closure `𝒪'` of `𝒪_X` in `f_* 𝒪_Y`,
> regarded as an algebraic space affine over `X`.

```lean
def normalizationIn (f : Y ⟶ X)
    (hqc' : (AlgebraSheaf.integralClosureSheaf
      (pushforwardAlgebra B S hS (Over.mk f))).IsQuasicoherent) :
    AffineOver B S hS X
```

**`AlgebraicGeometry.Space.toNormalizationIn`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationIn.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationIn.lean#L146). The attribute's comment: “the canonical factorization of f through the normalization”.

> **The canonical morphism `f' : Y ⟶ X'` to the normalization of `X` in `Y`**, as a morphism
> over `X`.  It is the factorization `Y ⟶ \underline{Spec}_X(f_* 𝒪_Y)` of Stacks 081X followed by
> the morphism of relative spectra induced by the inclusion `𝒪' ⊂ f_* 𝒪_Y`.

```lean
def toNormalizationIn (f : Y ⟶ X)
    (hqc : (pushforwardAlgebra B S hS (Over.mk f)).IsQuasicoherent)
    (hqc' : (AlgebraSheaf.integralClosureSheaf
      (pushforwardAlgebra B S hS (Over.mk f))).IsQuasicoherent)
    (hid : pushforwardAlgebra B S hS (idAffineOver B S hS Y).obj ≅ unitAlgebra B S hS Y) :
    Over.mk f ⟶ (normalizationIn B S hS E f hqc').obj
```

**`AlgebraicGeometry.Space.normalizationInQcqsHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqs.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqs.lean#L150). The attribute's comment: “the normalization ν : X' = Spec_X(𝒪') ⟶ X of X in Y, for f qcqs”.

> **The normalization morphism `ν : X' ⟶ X` of `X` in `Y`** (Definition 0822), for a
> quasi-compact quasi-separated `f : Y ⟶ X`.  It is affine
> (`AlgebraicGeometry.Space.isAffineHom_normalizationInQcqsHom`) with `ν_* 𝒪_{X'}` the integral
> closure `𝒪'` of `𝒪_X` in `f_* 𝒪_Y` (`AlgebraicGeometry.Space.normalizationInQcqsPushforwardIso`),
> which is what `X' = \underline{Spec}_X(𝒪')` means.

```lean
def normalizationInQcqsHom : normalizationInQcqs B S hS f hfqc hfqs ⟶ X
```

**`AlgebraicGeometry.Space.isAffineHom_normalizationInQcqsHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqs.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqs.lean#L155). The attribute's comment: “ν : X' ⟶ X is affine, X' being a relative spectrum over X”.

> **`ν : X' ⟶ X` is affine.**

```lean
theorem isAffineHom_normalizationInQcqsHom :
    IsAffineHom B S hS (normalizationInQcqsHom B S hS f hfqc hfqs).hom
```

**`AlgebraicGeometry.Space.normalizationInQcqsPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqs.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqs.lean#L163). The attribute's comment: “ν_* 𝒪_{X'} = 𝒪', i.e. X' = Spec_X(𝒪')”.

> **`ν_* 𝒪_{X'} ≅ 𝒪'`**: the direct image of the structure sheaf of the normalization is the
> integral closure of `𝒪_X` in `f_* 𝒪_Y`, as sheaves of `𝒪_X`-algebras.  With affineness of `ν`
> this identifies `X'` with `\underline{Spec}_X(𝒪')`.

```lean
def normalizationInQcqsPushforwardIso :
    pushforwardAlgebra B S hS (Over.mk (normalizationInQcqsHom B S hS f hfqc hfqs)) ≅
      AlgebraSheaf.integralClosureSheaf (pushforwardAlgebra B S hS (Over.mk f))
```

**`AlgebraicGeometry.Space.toNormalizationInQcqs`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqs.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqs.lean#L306). The attribute's comment: “the canonical morphism f' : Y ⟶ X'”.

> **The canonical morphism `f' : Y ⟶ X'`** of Definition 0822: on a `T`-point `y` of `Y` it is
> the unique morphism `T ⟶ X'` over `X` inducing `ν_* 𝒪_{X'} ≅ 𝒪' ⊂ f_* 𝒪_Y ⟶ (f ∘ y)_* 𝒪_T`.

```lean
def toNormalizationInQcqs : Y ⟶ normalizationInQcqs B S hS f hfqc hfqs
```

**`AlgebraicGeometry.Space.toNormalizationInQcqs_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqs.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqs.lean#L321). The attribute's comment: “the natural factorization Y ⟶ X' ⟶ X of f”.

> **The factorization of Definition 0822: `ν ∘ f' = f`.**

```lean
theorem toNormalizationInQcqs_comp :
    toNormalizationInQcqs f hfqc hfqs ≫ normalizationInQcqsHom B S hS f hfqc hfqs = f
```

## Tag 0ABP, a lemma

[Tag 0ABP](https://stacks.math.columbia.edu/tag/0ABP) in the Stacks Project.

**`AlgebraicGeometry.Space.etaleAlgebraRestrictionIntegralClosureIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInComparison.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInComparison.lean#L276). The attribute's comment: “part (1), étale base change: the integral closure of the structure sheaf in an algebra is unchanged by restriction along an étale morphism, which is the construction of the normalization commuting with étale base change. The geometric form, for the relative spectra, is `normalizationInBaseChangeIso`.”.

> **Stacks 0ABP, part (1), at the level of algebras.**  The integral closure of the structure
> sheaf in an algebra commutes with restriction along an étale morphism `g : W ⟶ X`.
>
> This is the whole of the source's reason for part (1): the normalization of `X` in `Y` is the
> relative spectrum of the integral closure of `𝒪_X` in `f_* 𝒪_Y`, and that construction is
> étale-local, hence "commutes with étale base change".

```lean
def etaleAlgebraRestrictionIntegralClosureIso (g : W ⟶ X) (hg : IsEtale B S hS g.hom)
    (A : AlgebraSheaf.{u, m} B S hS X.1 X.2) :
    (etaleAlgebraRestriction B S hS g hg).obj (AlgebraSheaf.integralClosureSheaf A) ≅
      AlgebraSheaf.integralClosureSheaf ((etaleAlgebraRestriction B S hS g hg).obj A)
```

**`AlgebraicGeometry.Space.normalizationInBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInComparison.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInComparison.lean#L373). The attribute's comment: “part (1), étale base change, in its geometric form. `halg` is the identification of the algebra pullback of Stacks 081V along an étale morphism with étale restriction and `hbc` is Stacks 03LX for the direct image of the structure sheaf, read as algebras; neither is part (1), and the module docstring records why each is carried. The content of part (1) is `etaleAlgebraRestrictionIntegralClosureIso`, which is unconditional.”.

> **Stacks 0ABP, part (1).**  For an étale morphism `g : W ⟶ X` the fibre product
> `W ×_X X'` is the normalization of `W` in `W ×_X Y`.
>
> The identification of the two algebras is étale-locality of the integral closure,
> `etaleAlgebraRestrictionIntegralClosureIso`, together with `halg` and `hbc`; the identification
> of the two relative spectra is the base-change clause of Stacks 081V.

```lean
def normalizationInBaseChangeIso {Y YW : AlgebraicSpaces B S hS}
    (g : W ⟶ X) (hg : IsEtale B S hS g.hom) (f : Y ⟶ X) (p : YW ⟶ Y) (fW : YW ⟶ W)
    (_sq : IsPullback p fW f g)
    (hqc' : (AlgebraSheaf.integralClosureSheaf
      (pushforwardAlgebra B S hS (Over.mk f))).IsQuasicoherent)
    (hqcW' : (AlgebraSheaf.integralClosureSheaf
      (pushforwardAlgebra B S hS (Over.mk fW))).IsQuasicoherent)
    (halg : C.algebraPullback g ≅ etaleAlgebraRestriction.{u, u} B S hS g hg)
    (hbc : (etaleAlgebraRestriction.{u, u} B S hS g hg).obj
        (pushforwardAlgebra B S hS (Over.mk f)) ≅
      pushforwardAlgebra B S hS (Over.mk fW)) :
    (C.affineBaseChange g).obj (normalizationIn B S hS E f hqc') ≅
      normalizationIn B S hS E fW hqcW'
```

**`AlgebraicGeometry.Space.normalizationInRepresentableIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInComparison.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInComparison.lean#L420). The attribute's comment: “part (2), comparison with the normalization of schemes. `Z` is the scheme normalization `AlgebraicGeometry.Scheme.Hom.normalization` of Stacks 035E, read inside the site as an algebraic space affine over `X`, and `hcmp` identifies its direct image of the structure sheaf with the integral closure of `𝒪_X` in `f_* 𝒪_Y`. That identification is the source's computation of `ν⁻¹(U)`. It is *not* Descent, Proposition 03DX(2): that proposition for the small étale site of an algebraic space is available here, unconditionally, as `AlgebraicGeometry.Space.isQuasicoherentOnSite_iff_isCartesianOnAffineCharts`, and it compares the sections over two affine charts rather than computing the sections of the integral closure. The module docstring lists what `hcmp` still needs.”.

> **Stacks 0ABP, part (2).**  Let `X` and `Y` be representable, by `X₀` and `Y₀`, and let
> `N₀` represent the normalization of the scheme `X₀` in the scheme `Y₀` of Stacks 035E.  Then the
> normalization `X'` of `X` in `Y` is representable by `N₀`.

```lean
def normalizationInRepresentableIso {Y : AlgebraicSpaces B S hS} (f : Y ⟶ X)
    (hqc' : (AlgebraSheaf.integralClosureSheaf
      (pushforwardAlgebra B S hS (Over.mk f))).IsQuasicoherent)
    {X₀ Y₀ N₀ : BigFppfOver B S hS} (_eX : X.1 ≅ yoneda.obj X₀) (_eY : Y.1 ≅ yoneda.obj Y₀)
    (f₀ : Y₀ ⟶ X₀) (_hf₀ : yoneda.map f₀ = _eY.inv ≫ f.hom ≫ _eX.hom)
    [QuasiCompact ((BigFppfOver.toScheme B S hS).map f₀)]
    [QuasiSeparated ((BigFppfOver.toScheme B S hS).map f₀)]
    (_hN : (BigFppfOver.toScheme B S hS).obj N₀ ≅
      ((BigFppfOver.toScheme B S hS).map f₀).normalization)
    (Z : AffineOver B S hS X) (eZ : Z.obj.left.1 ≅ yoneda.obj N₀)
    (hcmp : pushforwardAlgebra B S hS Z.obj ≅
      AlgebraSheaf.integralClosureSheaf (pushforwardAlgebra B S hS (Over.mk f))) :
    (normalizationIn B S hS E f hqc').obj.left.1 ≅ yoneda.obj N₀
```

**`AlgebraicGeometry.Space.isRepresentable_normalizationIn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInComparison.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInComparison.lean#L440). The attribute's comment: “part (2), representability of the normalization. The hypotheses are those of `normalizationInRepresentableIso`.”.

> **Stacks 0ABP, part (2), representability.**  In the representable case the normalization
> `X'` of `X` in `Y` is representable.

```lean
theorem isRepresentable_normalizationIn {Y : AlgebraicSpaces B S hS} (f : Y ⟶ X)
    (hqc' : (AlgebraSheaf.integralClosureSheaf
      (pushforwardAlgebra B S hS (Over.mk f))).IsQuasicoherent)
    {X₀ Y₀ N₀ : BigFppfOver B S hS} (eX : X.1 ≅ yoneda.obj X₀) (eY : Y.1 ≅ yoneda.obj Y₀)
    (f₀ : Y₀ ⟶ X₀) (hf₀ : yoneda.map f₀ = eY.inv ≫ f.hom ≫ eX.hom)
    [QuasiCompact ((BigFppfOver.toScheme B S hS).map f₀)]
    [QuasiSeparated ((BigFppfOver.toScheme B S hS).map f₀)]
    (hN : (BigFppfOver.toScheme B S hS).obj N₀ ≅
      ((BigFppfOver.toScheme B S hS).map f₀).normalization)
    (Z : AffineOver B S hS X) (eZ : Z.obj.left.1 ≅ yoneda.obj N₀)
    (hcmp : pushforwardAlgebra B S hS Z.obj ≅
      AlgebraSheaf.integralClosureSheaf (pushforwardAlgebra B S hS (Over.mk f))) :
    (normalizationIn B S hS E f hqc').obj.left.1.IsRepresentable
```

**`AlgebraicGeometry.Space.isRelativeNormalization_normalizationInQcqs_etaleBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqsComparison.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqsComparison.lean#L100). The attribute's comment: “part (1): for W ⟶ X étale, W ×_X X' is the normalization of W in W ×_X Y”.

> **Stacks 0ABP, part (1).**  Let `f : Y ⟶ X` be a quasi-compact and quasi-separated morphism
> of algebraic spaces over `S`, with normalization `Y ⟶ X' ⟶ X` (Definition 0822), and let
> `g : W ⟶ X` be étale.  Let `P = W ×_X X'` and `Y' = W ×_X Y`, with `f'_P : Y' ⟶ P` the base
> change of `f' : Y ⟶ X'`.  Then `Y' ⟶ P ⟶ W` is the normalization of `W` in `Y'`: it has the
> universal property of Stacks 0823, and it is joined to the normalization of `W` in `Y'` of
> Definition 0822 by a unique isomorphism compatible with both factorizations.

```lean
theorem isRelativeNormalization_normalizationInQcqs_etaleBaseChange
    {W P Y' : AlgebraicSpaces B S hS} (g : W ⟶ X) (hg : IsEtale B S hS g.hom)
    (i : P ⟶ normalizationInQcqs B S hS f hfqc hfqs) (νP : P ⟶ W)
    (hP : IsPullback i νP (normalizationInQcqsHom B S hS f hfqc hfqs) g)
    (j : Y' ⟶ Y) (fW : Y' ⟶ W) (hY : IsPullback j fW f g) (f'P : Y' ⟶ P)
    (h₁ : f'P ≫ i = j ≫ toNormalizationInQcqs f hfqc hfqs) (h₂ : f'P ≫ νP = fW) :
    IsRelativeNormalization B S hS fW.hom νP.hom f'P.hom ∧
      ∃ (hWqc : IsQuasiCompact B S hS fW.hom) (hWqs : IsQuasiSeparated B S hS fW.hom),
        ∃! e : (normalizationInQcqs B S hS fW hWqc hWqs).1 ≅ P.1,
          (toNormalizationInQcqs fW hWqc hWqs).hom ≫ e.hom = f'P.hom ∧
            e.hom ≫ νP.hom = (normalizationInQcqsHom B S hS fW hWqc hWqs).hom
```

**`AlgebraicGeometry.Space.isRepresentable_normalizationInQcqs_and_iso_normalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqsComparison.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqsComparison.lean#L158). The attribute's comment: “part (2): for X and Y representable, X' is representable and canonically isomorphic to the normalization of the scheme X in the scheme Y of 035E”.

> **Stacks 0ABP, part (2).**  Let `f : Y ⟶ X` be a quasi-compact and quasi-separated morphism
> of algebraic spaces over `S` with `X` and `Y` representable, by objects `X₀` and `Y₀` of the
> site, and let `f₀ : Y₀ ⟶ X₀` be the induced morphism.  Then the normalization `X'` of `X` in `Y`
> (Definition 0822) is representable, and canonically isomorphic to the normalization of the scheme
> `X₀` in the scheme `Y₀` (Morphisms, Section 035E): there is an object `N₀` of the site whose
> underlying scheme is that normalization, compatibly with both of its legs, and a unique
> isomorphism `X' ≅ N₀` compatible with both factorizations.

```lean
theorem isRepresentable_normalizationInQcqs_and_iso_normalization {X₀ Y₀ : BigFppfOver B S hS}
    (eX : X.1 ≅ yoneda.obj X₀) (eY : Y.1 ≅ yoneda.obj Y₀) (f₀ : Y₀ ⟶ X₀)
    (hf₀ : yoneda.map f₀ = eY.inv ≫ f.hom ≫ eX.hom) :
    (normalizationInQcqs B S hS f hfqc hfqs).1.IsRepresentable ∧
      ∃ (_ : QuasiCompact ((BigFppfOver.toScheme B S hS).map f₀))
        (_ : QuasiSeparated ((BigFppfOver.toScheme B S hS).map f₀))
        (N₀ : BigFppfOver B S hS) (t : Y₀ ⟶ N₀) (ν₀ : N₀ ⟶ X₀)
        (e : (BigFppfOver.toScheme B S hS).obj N₀ ≅
          ((BigFppfOver.toScheme B S hS).map f₀).normalization),
        (BigFppfOver.toScheme B S hS).map t ≫ e.hom =
            ((BigFppfOver.toScheme B S hS).map f₀).toNormalization ∧
          e.hom ≫ ((BigFppfOver.toScheme B S hS).map f₀).fromNormalization =
            (BigFppfOver.toScheme B S hS).map ν₀ ∧
          ∃! φ : (normalizationInQcqs B S hS f hfqc hfqs).1 ≅ yoneda.obj N₀,
            (toNormalizationInQcqs f hfqc hfqs).hom ≫ φ.hom = eY.hom ≫ yoneda.map t ∧
              φ.hom ≫ yoneda.map ν₀ = (normalizationInQcqsHom B S hS f hfqc hfqs).hom ≫ eX.hom
```

## Tag 0823, a lemma

[Tag 0823](https://stacks.math.columbia.edu/tag/0823) in the Stacks Project.

**`AlgebraicGeometry.Space.isIntegralHom_normalizationInQcqsHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqsUniversalProperty.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqsUniversalProperty.lean#L90). The attribute's comment: “property (1): ν is integral”.

> **Stacks 0823, property (1): the normalization `ν : X' ⟶ X` is integral.**  It is the
> relative spectrum of the integral closure `𝒪'`, an integral `𝒪_X`-algebra.

```lean
theorem isIntegralHom_normalizationInQcqsHom :
    IsIntegralHom B S hS (normalizationInQcqsHom B S hS f hfqc hfqs).hom
```

**`AlgebraicGeometry.Space.isRelativeNormalization_normalizationInQcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqsUniversalProperty.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqsUniversalProperty.lean#L116). The attribute's comment: “properties (1) and (2) hold for the normalization f = ν ∘ f' of Stacks 0822”.

> **Stacks 0823, properties (1) and (2) for the normalization of Stacks 0822.**  Let
> `f : Y ⟶ X` be a quasi-compact and quasi-separated morphism of algebraic spaces over `S`, and
> `f = ν ∘ f'` its factorization through the normalization `ν : X' ⟶ X` of `X` in `Y`.  Then `ν` is
> integral, and for every factorization `f = π ∘ g` with `π : Z ⟶ X` an integral morphism of
> algebraic spaces over `S` there is a unique `h : X' ⟶ Z` with `h ∘ f' = g` and `π ∘ h = ν`.

```lean
theorem isRelativeNormalization_normalizationInQcqs :
    IsRelativeNormalization B S hS f.hom (normalizationInQcqsHom B S hS f hfqc hfqs).hom
      (toNormalizationInQcqs f hfqc hfqs).hom
```

**`AlgebraicGeometry.Space.isRelativeNormalization_iff_exists_iso_normalizationInQcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqsUniversalProperty.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqsUniversalProperty.lean#L168). The attribute's comment: “the factorization through the normalization is characterized by (1) and (2)”.

> **Stacks 0823: the normalization is characterized by properties (1) and (2).**  Let
> `f : Y ⟶ X` be quasi-compact and quasi-separated.  A factorization `f = ν'' ∘ f''` of `f` through
> an algebraic space `X''` has properties (1) and (2) — `ν''` integral, and every factorization of
> `f` through an integral morphism receiving a unique compatible morphism from `X''` — if and only
> if it is isomorphic to the factorization `f = ν ∘ f'` through the normalization of `X` in `Y`;
> the isomorphism is then unique, by
> `AlgebraicGeometry.Space.existsUnique_iso_normalizationInQcqs_of_isRelativeNormalization`.

```lean
theorem isRelativeNormalization_iff_exists_iso_normalizationInQcqs
    {X'' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX'' : IsAlgebraicSpace B S hS X'')
    (ν'' : X'' ⟶ X.1) (f'' : Y.1 ⟶ X'') :
    IsRelativeNormalization B S hS f.hom ν'' f'' ↔
      ∃ e : (normalizationInQcqs B S hS f hfqc hfqs).1 ≅ X'',
        (toNormalizationInQcqs f hfqc hfqs).hom ≫ e.hom = f'' ∧
          e.hom ≫ ν'' = (normalizationInQcqsHom B S hS f hfqc hfqs).hom
```

**`AlgebraicGeometry.Space.isRelativeNormalization_comparison_normalizationInQcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqsUniversalProperty.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqsUniversalProperty.lean#L188). The attribute's comment: “moreover, in (2) the morphism h : X' ⟶ Z is the normalization of Z in Y”.

> **Stacks 0823, the final clause.**  Let `f : Y ⟶ X` be quasi-compact and quasi-separated,
> let `f = π ∘ g` with `π : Z ⟶ X` an integral morphism of algebraic spaces, and let `h : X' ⟶ Z`
> be the morphism of property (2), so `h ∘ f' = g` and `π ∘ h = ν`.  Then `h : X' ⟶ Z` is the
> normalization of `Z` in `Y`: the factorization `g = h ∘ f'` has properties (1) and (2) for `g`,
> and it is uniquely isomorphic to the factorization of `g` through the normalization of `Z` in
> `Y` of Stacks 0822, `g` being quasi-compact and quasi-separated.

```lean
theorem isRelativeNormalization_comparison_normalizationInQcqs {Z : AlgebraicSpaces B S hS}
    (π : Z ⟶ X) (hπ : IsIntegralHom B S hS π.hom) (g : Y ⟶ Z) (hg : g ≫ π = f)
    (h : normalizationInQcqs B S hS f hfqc hfqs ⟶ Z)
    (hh : toNormalizationInQcqs f hfqc hfqs ≫ h = g)
    (hhπ : h ≫ π = normalizationInQcqsHom B S hS f hfqc hfqs) :
    IsRelativeNormalization B S hS g.hom h.hom (toNormalizationInQcqs f hfqc hfqs).hom ∧
      ∃ (hgqc : IsQuasiCompact B S hS g.hom) (hgqs : IsQuasiSeparated B S hS g.hom),
        ∃! e : (normalizationInQcqs B S hS g hgqc hgqs).1 ≅
            (normalizationInQcqs B S hS f hfqc hfqs).1,
          (toNormalizationInQcqs g hgqc hgqs).hom ≫ e.hom =
              (toNormalizationInQcqs f hfqc hfqs).hom ∧
            e.hom ≫ h.hom = (normalizationInQcqsHom B S hS g hgqc hgqs).hom
```

**`AlgebraicGeometry.Space.IsRelativeNormalization.existsUnique_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInUniversalProperty.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInUniversalProperty.lean#L165). The attribute's comment: “properties (1) and (2) characterize the factorization”.

> **Stacks 0823, the characterization.**  Two factorizations of `f` through an integral
> morphism of algebraic spaces which both have the universal property are joined by a unique
> isomorphism compatible with the two factorizations and the two integral morphisms.

```lean
theorem existsUnique_iso {ν' : X'' ⟶ X} {f'' : Y ⟶ X''}
    (h : IsRelativeNormalization B S hS f ν f')
    (h' : IsRelativeNormalization B S hS f ν' f'')
    (hX' : IsAlgebraicSpace B S hS X') (hX'' : IsAlgebraicSpace B S hS X'') :
    ∃! e : X' ≅ X'', f' ≫ e.hom = f'' ∧ e.hom ≫ ν' = ν
```

**`AlgebraicGeometry.Space.IsRelativeNormalization.comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInUniversalProperty.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInUniversalProperty.lean#L184). The attribute's comment: “moreover, the comparison morphism is the normalization of Z in Y”.

> **Stacks 0823, the final clause.**  Let `f = π ∘ g` be a factorization of `f` through an
> integral morphism `π : Z ⟶ X`, and let `k : X' ⟶ Z` be the comparison morphism supplied by the
> universal property.  Then `k` exhibits `X'` as the normalization of `Z` in `Y`.

```lean
theorem comparison {Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (h : IsRelativeNormalization B S hS f ν f')
    (hX : IsAlgebraicSpace B S hS X) (hZ : IsAlgebraicSpace B S hS Z)
    {π : Z ⟶ X} (hπ : IsIntegralHom B S hS π) {g : Y ⟶ Z}
    {k : X' ⟶ Z} (hk : f' ≫ k = g) (hkν : k ≫ π = ν) :
    IsRelativeNormalization B S hS g k f'
```

**`AlgebraicGeometry.Space.isRelativeNormalization_toNormalizationIn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInUniversalProperty.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInUniversalProperty.lean#L370). The attribute's comment: “the canonical factorization has properties (1) and (2)”.

> **Stacks 0823, properties (1) and (2) for the canonical factorization.**  The factorization
> `f = ν ∘ f'` of `f` through the normalization `ν : X' ⟶ X` of `X` in `Y` has `ν` integral, and
> every factorization of `f` through an integral morphism `π : Z ⟶ X` of algebraic spaces
> receives a unique morphism `h : X' ⟶ Z` with `f' ∘ h = g` and `π ∘ h = ν`.

```lean
theorem isRelativeNormalization_toNormalizationIn
    (P : RelativeSpecUniversalProperty B S hS E C)
    (D : IntegralAlgebraDictionary B S hS E) (f : Y ⟶ X)
    (hqc : (pushforwardAlgebra B S hS (Over.mk f)).IsQuasicoherent)
    (hqc' : (AlgebraSheaf.integralClosureSheaf
      (pushforwardAlgebra B S hS (Over.mk f))).IsQuasicoherent)
    (hid : pushforwardAlgebra B S hS (idAffineOver B S hS Y).obj ≅ unitAlgebra B S hS Y)
    (hloc : (pushforwardAlgebra B S hS (Over.mk f)).IsIntegralLocalOnAffineCharts) :
    IsRelativeNormalization B S hS f.hom
      (normalizationIn B S hS E f hqc').obj.hom.hom
      (toNormalizationIn B S hS E C f hqc hqc' hid).left.hom
```

## Tag 0AYF, a lemma

[Tag 0AYF](https://stacks.math.columbia.edu/tag/0AYF) in the Stacks Project.

**`AlgebraicGeometry.Space.IsRelativeNormalization.hasEtaleLocalProperty_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RelativeNormalization.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RelativeNormalization.lean#L197).

> **Stacks 0AYF.** The normalization of an algebraic space `X` in a reduced algebraic space
> `Y` is reduced.
>
> Reducedness is asked of an algebraic space as the étale-local property of schemes of Tag 03E6.
> The reduction of the normalization is constructed here rather than taken as an input: it is
> `AlgebraicGeometry.Space.reduction`, the reduced induced structure of Tag 03IQ on the whole
> point set of `X'`.

```lean
theorem hasEtaleLocalProperty_isReduced (hnorm : IsRelativeNormalization B S hS f ν f')
    (hX' : IsAlgebraicSpace B S hS X') (hY : IsAlgebraicSpace B S hS Y)
    (hYred : HasEtaleLocalProperty B S hS Y fun T : Scheme.{u} => IsReduced T) :
    HasEtaleLocalProperty B S hS X' fun T : Scheme.{u} => IsReduced T
```

## Tag 0AYG, a lemma

[Tag 0AYG](https://stacks.math.columbia.edu/tag/0AYG) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.exists_genericPoint_irreducibleComponent_mapping_to`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/RelativeGenericPoints.lean#L42), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean, line 1150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean#L1150) (StacksFrontier).

## Tag 0824, a lemma

[Tag 0824](https://stacks.math.columbia.edu/tag/0824) in the Stacks Project.

**`AlgebraicGeometry.Space.isRelativeNormalization_coproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RelativeNormalization.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RelativeNormalization.lean#L298).

> **Stacks 0824.** Let `f : Y ⟶ X` be a morphism of algebraic spaces over `S` whose source
> is a disjoint union of finitely many algebraic spaces `Y i`, and let `X' i` be the
> normalization of `X` in `Y i`. Then a disjoint union of the `X' i` is the normalization of `X`
> in `Y`.
>
> The normalization morphism is integral because its base change along a morphism from an affine
> object of the site is the induced morphism out of the coproduct of the base changes of the
> summands, which is a finite coproduct of integral morphisms of schemes; the universal property
> is checked summand by summand, each factorization of `f` through an integral morphism
> restricting to one of `f i`.

```lean
theorem isRelativeNormalization_coproduct {I : Type v} [Finite I]
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (F : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : ∀ i, IsAlgebraicSpace B S hS (F i))
    (Y : Sheaf (BigFppfOver.topology B S hS) (Type u))
    (ι : ∀ i, (⟨F i, (hF i).isSheaf⟩ :
      Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶ Y)
    (hY : IsColimit (Cofan.mk Y ι)) (f : Y.obj ⟶ X)
    (N : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hN : ∀ i, IsAlgebraicSpace B S hS (N i))
    (νs : ∀ i, N i ⟶ X) (fs : ∀ i, F i ⟶ N i)
    (hnorm : ∀ i, IsRelativeNormalization B S hS ((ι i).hom ≫ f) (νs i) (fs i))
    (P : Sheaf (BigFppfOver.topology B S hS) (Type u))
    (κ : ∀ i, (⟨N i, (hN i).isSheaf⟩ :
      Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶ P)
    (hP : IsColimit (Cofan.mk P κ))
    (ν : P.obj ⟶ X) (hν : ∀ i, (κ i).hom ≫ ν = νs i)
    (f' : Y.obj ⟶ P.obj) (hf' : ∀ i, (ι i).hom ≫ f' = fs i ≫ (κ i).hom) :
    IsRelativeNormalization B S hS f ν f'
```

## Tag 0A0Q, a lemma

[Tag 0A0Q](https://stacks.math.columbia.edu/tag/0A0Q) in the Stacks Project.

**`AlgebraicGeometry.Space.isIntegral_pushforwardAlgebra_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DirectImageSectionsGlobalFunctions.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DirectImageSectionsGlobalFunctions.lean#L344). The attribute's comment: “first sentence: f_*O_X is integral over O_Y; only universal closedness of f is used”. References: EGA II (7.3.11), “Integrality of Γ(X”.

> **Stacks 0A0Q, first assertion.**  For a universally closed morphism `f : X ⟶ Y` of
> algebraic spaces over `S`, the direct image `f_*𝒪_X` is integral over `𝒪_Y`.
>
> The assertion is étale local on `Y`: on an affine étale scheme chart `V` of `Y` the sections of
> `f_*𝒪_X` are the global regular functions on the algebraic space `X ×_Y V`
> (`AlgebraicGeometry.Space.directImageSectionsToGlobalFunctions`, which is injective), the
> projection `X ×_Y V ⟶ V` is universally closed because `f` is, and the global functions of a
> universally closed algebraic space over an affine base are integral over the base
> (`AlgebraicGeometry.Space.isIntegral_globalFunctions_of_universallyClosed`).

```lean
theorem isIntegral_pushforwardAlgebra_of_universallyClosed (f : X ⟶ Y)
    (huc : UniversallyClosed B S hS f.hom) :
    (pushforwardAlgebra B S hS (Over.mk f)).IsIntegral
```

**`AlgebraicGeometry.Space.isIso_pushforwardAlgebraMap_toNormalizationInQcqsOver_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInUniversallyClosed.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInUniversallyClosed.lean#L118). The attribute's comment: “second sentence: the normalization X ⟶ Y' ⟶ Y of Y in X induces ν_*O_{Y'} ≅ f_*O_X, i.e. Y' = Spec_Y(f_*O_X) with the factorization of 081X”.

> **Stacks 0A0Q, second sentence: the normalization of `Y` in `X` is
> `\underline{Spec}_Y(f_*𝒪_X)`.**  Let `f : X ⟶ Y` be a quasi-compact, quasi-separated and
> universally closed morphism of algebraic spaces, and let `X ⟶ Y' ⟶ Y` be the normalization of
> `Y` in `X` (Stacks 0822; `ν : Y' ⟶ Y` is affine).  Then the map `ν_*𝒪_{Y'} ⟶ f_*𝒪_X` of
> `𝒪_Y`-algebras induced by the canonical morphism `f' : X ⟶ Y'` is an isomorphism, so
> `Y' = \underline{Spec}_Y(f_*𝒪_X)` and `f'` is the canonical morphism of Stacks 081X.
>
> The map induced by `f'` is `ν_*𝒪_{Y'} ≅ 𝒪' ⊂ f_*𝒪_X`
> (`AlgebraicGeometry.Space.pushforwardAlgebraMap_toNormalizationInQcqsOver`), and the inclusion
> of the integral closure `𝒪'` is all of `f_*𝒪_X` because `f_*𝒪_X` is integral over `𝒪_Y`, the
> first sentence of the tag.

```lean
theorem isIso_pushforwardAlgebraMap_toNormalizationInQcqsOver_of_universallyClosed :
    IsIso (pushforwardAlgebraMap B S hS (toNormalizationInQcqsOver f hfqc hfqs))
```

**`AlgebraicGeometry.Space.existsUnique_iso_normalizationInQcqs_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInUniversallyClosed.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInUniversallyClosed.lean#L133). The attribute's comment: “second sentence: the normalization of Y in X is, uniquely, the factorization X ⟶ Spec_Y(f_*O_X) ⟶ Y of 081X”.

> **Stacks 0A0Q, second sentence, as an identification of factorizations.**  For a
> quasi-compact, quasi-separated and universally closed `f : X ⟶ Y`, every factorization
> `X ⟶ Z ⟶ Y` of `f` of the kind Stacks 081X constructs — `Z` affine over `Y` and the induced map
> `(Z ⟶ Y)_*𝒪_Z ⟶ f_*𝒪_X` an isomorphism, i.e. `Z = \underline{Spec}_Y(f_*𝒪_X)` with its
> canonical morphism from `X` — is the normalization of `Y` in `X`: there is a unique isomorphism
> `Y' ≅ Z` over `Y` from the normalization carrying the canonical `f' : X ⟶ Y'` to `X ⟶ Z`.

```lean
theorem existsUnique_iso_normalizationInQcqs_of_universallyClosed
    (Z : AffineOver B S hS Y) (g : Over.mk f ⟶ Z.obj)
    [IsIso (pushforwardAlgebraMap B S hS g)] :
    ∃! k : (normalizationInQcqsAffineOver B S hS f hfqc hfqs).obj ≅ Z.obj,
      toNormalizationInQcqsOver f hfqc hfqs ≫ k.hom = g
```

**`AlgebraicGeometry.Space.isIso_integralClosureInclusion_pushforwardAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PushforwardStructureSheafIntegral.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PushforwardStructureSheafIntegral.lean#L266). The attribute's comment: “second assertion: the normalization of Y in X is the factorization through Spec_Y(f_*O_X), with the integrality of f_*O_X assumed rather than proved”.

> For a morphism `f : X ⟶ Y` of algebraic spaces whose direct image `f_*𝒪_X` is integral over
> `𝒪_Y`, the inclusion of the integral closure `𝒪'` of `𝒪_Y` in `f_*𝒪_X` is an isomorphism of algebra
> sheaves, so `𝒪' = f_*𝒪_X` and the normalization of `Y` in `X` — the relative spectrum of `𝒪'`,
> Stacks 0821 — is the factorization `X ⟶ Spec_Y(f_*𝒪_X) ⟶ Y` of Stacks 081X.

```lean
theorem isIso_integralClosureInclusion_pushforwardAlgebra (f : X ⟶ Y)
    (hf : (pushforwardAlgebra B S hS (Over.mk f)).IsIntegral) :
    IsIso (AlgebraSheaf.integralClosureInclusion (pushforwardAlgebra B S hS (Over.mk f)))
```

## Tag 0825, a lemma

[Tag 0825](https://stacks.math.columbia.edu/tag/0825) in the Stacks Project.

**`AlgebraicGeometry.Space.normalizationInIsoOfIsIntegralHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInIntegralMorphism.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInIntegralMorphism.lean#L82).

> **Stacks 0825.**  The integral closure of `X` in `Y` is `Y`: for an integral morphism
> `f : Y ⟶ X` of algebraic spaces whose direct image `f_* 𝒪_Y` is integral over `𝒪_X`, the
> normalization `X' ⟶ X` of `X` in `Y` is canonically isomorphic to `Y` over `X`.

```lean
def normalizationInIsoOfIsIntegralHom (f : Y ⟶ X) (hf : IsIntegralHom B S hS f.hom)
    (hqc' : (AlgebraSheaf.integralClosureSheaf
      (pushforwardAlgebra B S hS (Over.mk f))).IsQuasicoherent)
    (hint : (pushforwardAlgebra B S hS (Over.mk f)).IsIntegral) :
    (normalizationIn B S hS E f hqc').obj ≅ Over.mk f
```

**`AlgebraicGeometry.Space.normalizationInIsoOfIsIntegralHom'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInIntegralMorphismSupplement.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInIntegralMorphismSupplement.lean#L37).

> For an integral morphism `f : Y ⟶ X` of algebraic spaces, the normalization `X' ⟶ X` of `X`
> in `Y` is canonically isomorphic to `Y` over `X`.

```lean
def normalizationInIsoOfIsIntegralHom' (f : Y ⟶ X) (hf : IsIntegralHom B S hS f.hom)
    (hqc' : (AlgebraSheaf.integralClosureSheaf
      (pushforwardAlgebra B S hS (Over.mk f))).IsQuasicoherent) :
    (normalizationIn B S hS E f hqc').obj ≅ Over.mk f
```

**`AlgebraicGeometry.Space.isIso_toNormalizationInQcqs_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqsIntegral.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqsIntegral.lean#L112).

> **Stacks 0825.**  Let `f : Y ⟶ X` be an integral morphism of algebraic spaces over `S`.  Then
> the integral closure of `X` in `Y` is equal to `Y`: the canonical morphism `f' : Y ⟶ X'` of
> Stacks 0822 from `Y` to the normalization `ν : X' ⟶ X` of `X` in `Y` is an isomorphism.
>
> An integral morphism is quasi-compact and quasi-separated, so the normalization is defined at no
> further hypothesis.  By Stacks 0415 `f` is affine and universally closed; universal closedness
> makes `f_* 𝒪_Y` integral over `𝒪_X` (Stacks 0A0Q), so the integral closure `𝒪' = ν_* 𝒪_{X'}` is
> all of `f_* 𝒪_Y`, and since `Y` and `X'` are both affine over `X`, direct image reflects that
> isomorphism of algebras to `f'`.

```lean
theorem isIso_toNormalizationInQcqs_of_isIntegralHom (f : Y ⟶ X)
    (hf : IsIntegralHom B S hS f.hom) :
    IsIso (toNormalizationInQcqs f
      (isQuasiCompact_of_isIntegralHom f.hom Y.property X.property hf)
      (isQuasiSeparated_of_isIntegralHom f.hom Y.property X.property hf))
```

**`AlgebraicGeometry.Space.isRelativeNormalization_id_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQuasiFiniteLocus.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQuasiFiniteLocus.lean#L100). The attribute's comment: “in the form of the characterization of Tag 0823: an integral morphism is the normalization of its target in its source”.

> **Stacks 0825, in the form of the characterization of Tag 0823.** An integral morphism
> `f : X ⟶ Y` of algebraic spaces over `S` is the normalization of `Y` in `X`: the factorization
> of `f` as the identity of `X` followed by `f` itself has the two characterizing properties.
>
> Integrality of the second factor is the hypothesis, and a factorization `f = g ≫ π` through an
> integral morphism `π : Z ⟶ Y` already has `g` as a morphism out of `X`, which is therefore the
> unique morphism compatible with the two factorizations.

```lean
theorem isRelativeNormalization_id_of_isIntegralHom (hf : IsIntegralHom B S hS f) :
    IsRelativeNormalization B S hS f f (𝟙 X)
```

## Tag 0BB0, a lemma

[Tag 0BB0](https://stacks.math.columbia.edu/tag/0BB0) in the Stacks Project.

**`AlgebraicGeometry.Space.IsRelativeNormalization.isFinite_of_isNagata`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RelativeNormalizationNagata.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RelativeNormalizationNagata.lean#L286). The attribute's comment: “granted Tag 081V, the relative spectrum of a quasi-coherent algebra on an algebraic space, in the shape of the hypothesis hdom: over an affine étale chart of the base the functions on the chart base change of the normalization embed into the functions on an affine surjective étale cover of the corresponding part of the source”.

> **Stacks 0BB0.** Let `f : Y ⟶ X` be a quasi-separated morphism of finite type of algebraic
> spaces over `S` with `X` Nagata and `Y` reduced. Then the normalization `ν : X' ⟶ X` of `X`
> in `Y` is finite.
>
> Nagata-ness and reducedness are the étale-local properties of schemes of Tag 03E6. The
> hypothesis `hdom` is the affine-chart description of the normalization of Tag 0822: over an
> affine étale chart of `X` the functions on the base change of `X'` embed into the functions on
> an affine surjective étale cover of the part of `Y` over the chart.

```lean
theorem IsRelativeNormalization.isFinite_of_isNagata
    (hnorm : IsRelativeNormalization B S hS f ν f')
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hX' : IsAlgebraicSpace B S hS X')
    (hXnagata : HasEtaleLocalProperty B S hS X fun Z : Scheme.{u} => IsNagataScheme Z)
    (hYred : HasEtaleLocalProperty B S hS Y fun Z : Scheme.{u} => IsReduced Z)
    (hft : IsFiniteType B S hS f) (_hqs : IsQuasiSeparated B S hS f)
    (hdom : ∀ (V N W : BigFppfOver B S hS) (q : yoneda.obj V ⟶ X) (n : N ⟶ V)
      (i : yoneda.obj N ⟶ X') (w : yoneda.obj W ⟶ Limits.pullback q f) (c : W ⟶ N),
      IsAffine ((BigFppfOver.toScheme B S hS).obj V) →
      IsAffine ((BigFppfOver.toScheme B S hS).obj W) →
      (MorphismProperty.inverseImage
        (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf q →
      IsPullback i (yoneda.map n) ν q →
      (MorphismProperty.inverseImage
        (@AlgebraicGeometry.Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf w →
      IsEtale B S hS w →
      yoneda.map c ≫ i = w ≫ Limits.pullback.snd q f ≫ f' →
      Function.Injective ((BigFppfOver.toScheme B S hS).map c).appTop.hom) :
    IsFinite B S hS ν
```

**`AlgebraicGeometry.Space.IsRelativeNormalization.isFinite_of_isNagata_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RelativeNormalizationNagataFinite.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RelativeNormalizationNagataFinite.lean#L283).

> Let `f : Y ⟶ X` be a quasi-separated morphism of finite type of algebraic spaces over `S` with
> `X` Nagata and `Y` reduced. Then the normalization `ν : X' ⟶ X` of `X` in `Y`, any factorization
> `Y ⟶ X' ⟶ X` of `f` satisfying `AlgebraicGeometry.Space.IsRelativeNormalization`, is finite.

```lean
theorem IsRelativeNormalization.isFinite_of_isNagata_of_isReduced
    (hnorm : IsRelativeNormalization B S hS f ν f')
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hX' : IsAlgebraicSpace B S hS X')
    (hXnagata : HasEtaleLocalProperty B S hS X fun Z : Scheme.{u} => IsNagataScheme Z)
    (hYred : HasEtaleLocalProperty B S hS Y fun Z : Scheme.{u} => IsReduced Z)
    (hft : IsFiniteType B S hS f) (_hqs : IsQuasiSeparated B S hS f) :
    IsFinite B S hS ν
```

**`AlgebraicGeometry.Space.isFinite_normalizationInQcqsHom_of_isNagata`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqsNagataFinite.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqsNagataFinite.lean#L51).

> **Stacks 0BB0.** Let `f : Y ⟶ X` be a morphism of algebraic spaces over `S` such that `X`
> is Nagata, `f` is quasi-separated of finite type, and `Y` is reduced. Then the normalization
> `ν : X' ⟶ X` of `X` in `Y` (Stacks 0822) is finite.
>
> Being Nagata and being reduced are the étale-local properties of schemes of Tag 03E6; the
> quasi-compactness that the normalization of Stacks 0822 requires of `f` is the second half of
> `f` being of finite type.

```lean
theorem isFinite_normalizationInQcqsHom_of_isNagata {X Y : AlgebraicSpaces B S hS} (f : Y ⟶ X)
    (hXnagata : HasEtaleLocalProperty B S hS X.1 fun Z : Scheme.{u} => IsNagataScheme Z)
    (hYred : HasEtaleLocalProperty B S hS Y.1 fun Z : Scheme.{u} => IsReduced Z)
    (hft : IsFiniteType B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom) :
    IsFinite B S hS (normalizationInQcqsHom B S hS f hft.2 hfqs).hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.48, Tag 0BAZ](https://stacks.math.columbia.edu/tag/0BAZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
