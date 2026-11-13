---
declaration: section
origin: cited
lean: Stacks.Divisors.negativeTwist', Stacks.Divisors.invertibleSheaf', Stacks.Divisors.invertibleSheaf_isInvertible, Stacks.Divisors.canonicalSection', Stacks.Divisors.invertibleSheafIsoInverseIdeal, Stacks.Divisors.negativeTwistIso, Stacks.Divisors.differenceTwist', Stacks.Divisors.negativeTwist
statement: formalized
proof: formalized
---

# 31.15 Effective Cartier divisors and invertible sheaves

Section 31.15 of the Stacks Project, [Tag 0C4S](https://stacks.math.columbia.edu/tag/0C4S). 11 tags here are carried by 55 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01WX, a definition

[Tag 01WX](https://stacks.math.columbia.edu/tag/01WX) in the Stacks Project.

**`Stacks.Divisors.negativeTwist'`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/DivisorInvertibleSheaf.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/DivisorInvertibleSheaf.lean#L100). The attribute's comment: “part (3): negative twist”.

> **Stacks Project, Tag 01WX (3).** The sheaf `𝒪_X(-D) = ℐ_D` of a closed subscheme
> `D ⊆ X`: its sheaf of ideals.

```lean
noncomputable abbrev negativeTwist' : SheafOfModules.{u} (structureSheafRing X.toRingedSpace)
```

**`Stacks.Divisors.invertibleSheaf'`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/DivisorInvertibleSheaf.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/DivisorInvertibleSheaf.lean#L107). The attribute's comment: “part (1): associated sheaf”.

> **Stacks Project, Tag 01WX (1).** The sheaf `𝒪_X(D) = SheafHom_{𝒪_X}(ℐ_D, 𝒪_X)` associated
> to a closed subscheme `D ⊆ X`. It is invertible as soon as `D` is an effective Cartier divisor;
> see `Stacks.Divisors.invertibleSheaf_isInvertible`.

```lean
noncomputable abbrev invertibleSheaf' : SheafOfModules.{u} (structureSheafRing X.toRingedSpace)
```

**`Stacks.Divisors.invertibleSheaf_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/DivisorInvertibleSheaf.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/DivisorInvertibleSheaf.lean#L143). The attribute's comment: “part (1): invertibility”.

> **Stacks Project, Tag 01WX (1).** The sheaf `𝒪_X(D)` of an effective Cartier divisor is
> invertible: the evaluation pairing `𝒪_X(D) ⊗ ℐ_D ⟶ 𝒪_X` trivializes it.

```lean
theorem invertibleSheaf_isInvertible [IsEffectiveCartierDivisor D] :
    AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf
      (structureSheafRing X.toRingedSpace).property (invertibleSheaf' D)
```

**`Stacks.Divisors.canonicalSection'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/DivisorInvertibleSheaf.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/DivisorInvertibleSheaf.lean#L168). The attribute's comment: “part (2): canonical section”.

> **Stacks Project, Tag 01WX (2).** The canonical section `1_D` of `𝒪_X(D)`: the global
> section corresponding to the inclusion of the ideal sheaf `ℐ_D` into `𝒪_X`.

```lean
noncomputable def canonicalSection' : (invertibleSheaf' D).sections
```

**`Stacks.Divisors.invertibleSheafIsoInverseIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/DivisorInvertibleSheaf.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/DivisorInvertibleSheaf.lean#L182). The attribute's comment: “part (1): inverse tensor power”.

> **Stacks Project, Tag 01WX (1).** The sheaf `𝒪_X(D)` of an effective Cartier divisor is the
> inverse tensor power `ℐ_D^{⊗ -1}` of its ideal sheaf: both are tensor inverses of `ℐ_D`, and a
> tensor inverse is unique up to a canonical isomorphism.

```lean
noncomputable def invertibleSheafIsoInverseIdeal [IsEffectiveCartierDivisor D] :
    Stacks.SheafOfModules.Invertible.tensorPower X.presheaf
        (structureSheafRing X.toRingedSpace).property (negativeTwist' D) (-1) ≅
      invertibleSheaf' D
```

**`Stacks.Divisors.negativeTwistIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/DivisorInvertibleSheaf.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/DivisorInvertibleSheaf.lean#L197). The attribute's comment: “part (3): inverse tensor power”.

> **Stacks Project, Tag 01WX (3).** The sheaf `𝒪_X(-D) = ℐ_D` is the inverse tensor power
> `𝒪_X(D)^{⊗ -1}`, which is the sense in which `𝒪_X(-D)` is the inverse of `𝒪_X(D)`.

```lean
noncomputable def negativeTwistIso [IsEffectiveCartierDivisor D] :
    Stacks.SheafOfModules.Invertible.tensorPower X.presheaf
        (structureSheafRing X.toRingedSpace).property (invertibleSheaf' D) (-1) ≅
      negativeTwist' D
```

**`Stacks.Divisors.differenceTwist'`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/DivisorInvertibleSheaf.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/DivisorInvertibleSheaf.lean#L214). The attribute's comment: “part (4): difference twist”.

> **Stacks Project, Tag 01WX (4).** The sheaf
> `𝒪_X(D - D') = 𝒪_X(D) ⊗_{𝒪_X} 𝒪_X(-D')` attached to a pair of closed subschemes.

```lean
noncomputable abbrev differenceTwist' : SheafOfModules.{u} (structureSheafRing X.toRingedSpace)
```

**`Stacks.Divisors.negativeTwist`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheaf.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheaf.lean#L123). The attribute's comment: “(3): O\_S(-D) = I\_D”.

> **Stacks Project, Tag 01WX (3).** The sheaf `𝒪_S(-D)` *is* the ideal sheaf `ℐ_D` of the
> closed subscheme `D ⊆ S`.

```lean
noncomputable abbrev negativeTwist : SheafOfModules.{u} (structureSheafRing X.toRingedSpace)
```

**`Stacks.Divisors.invertibleSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheaf.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheaf.lean#L136). The attribute's comment: “(1): O\_S(D) = SheafHom(I\_D, O\_S)”.

> **Stacks Project, Tag 01WX (1).** The sheaf `𝒪_S(D) = SheafHom_{𝒪_S}(ℐ_D, 𝒪_S)` associated
> to a closed subscheme `D ⊆ S`: the dual of its ideal sheaf.

```lean
noncomputable abbrev invertibleSheaf : SheafOfModules.{u} (structureSheafRing X.toRingedSpace)
```

**`Stacks.Divisors.differenceTwist`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheaf.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheaf.lean#L144). The attribute's comment: “(4): O\_S(D - D') = O\_S(D) tensor O\_S(-D')”.

> **Stacks Project, Tag 01WX (4).** The difference twist
> `𝒪_S(D - D') = 𝒪_S(D) ⊗_{𝒪_S} 𝒪_S(-D')`. The expression `D - D'` has no geometric meaning on
> its own; this is the definition of the sheaf it names.

```lean
noncomputable abbrev differenceTwist : SheafOfModules.{u} (structureSheafRing X.toRingedSpace)
```

**`Stacks.Divisors.isInvertible_invertibleSheaf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheaf.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheaf.lean#L197). The attribute's comment: “(1): O\_S(D) is invertible”.

> **Stacks Project, Tag 01WX (1).** The sheaf `𝒪_S(D)` of an effective Cartier divisor is
> invertible, which is what the tag's wording "the invertible sheaf `𝒪_S(D)`" asserts.
>
> This is Tag 0B8K (2) ⟹ (1) applied to the evaluation pairing: no trivializing cover is
> constructed, and no rank-one dual basis is assumed.

```lean
instance isInvertible_invertibleSheaf :
    AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj
      (structureSheafRing X.toRingedSpace).property (invertibleSheaf D)
```

**`Stacks.Divisors.invertibleSheafIsoNegativeTensorPower`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheaf.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheaf.lean#L216). The attribute's comment: “(1): O\_S(D) = I\_D^\{tensor -1}”.

> **Stacks Project, Tag 01WX (1):** `𝒪_S(D) = ℐ_D^{⊗ -1}`. The dual of the ideal sheaf is its
> negative first tensor power, by uniqueness of tensor inverses; the identification is the one
> normalized by `invertibleSheafPairing`, not an arbitrary isomorphism. That normalization needs
> no restatement here: this *is*
> `Stacks.SheafOfModules.Invertible.isoTensorPowerNegOne` at that pairing, so
> `Stacks.SheafOfModules.Invertible.isoTensorPowerNegOne_hom_tensor` applies to it directly and
> says that tensoring this isomorphism with `ℐ_D` carries the canonical trivialization of
> `ℐ_D^{⊗ -1} ⊗ ℐ_D` back to `invertibleSheafPairing`.

```lean
noncomputable def invertibleSheafIsoNegativeTensorPower :
    invertibleSheaf D ≅ Stacks.SheafOfModules.Invertible.tensorPower X.sheaf.obj
      (structureSheafRing X.toRingedSpace).property (negativeTwist D) (-1)
```

**`Stacks.Divisors.negativeTwistIsoNegativeTensorPower`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheaf.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheaf.lean#L228). The attribute's comment: “(3): O\_S(-D) = O\_S(D)^\{tensor -1}”.

> **Stacks Project, Tag 01WX (3):** `𝒪_S(-D) = 𝒪_S(D)^{⊗ -1}`. Together with the definition
> of `negativeTwist` this is the tag's full chain `𝒪_S(-D) = 𝒪_S(D)^{⊗ -1} = ℐ_D`. The
> identification is normalized by `invertibleSheafPairing'`, through the same
> `Stacks.SheafOfModules.Invertible.isoTensorPowerNegOne_hom_tensor`.

```lean
noncomputable def negativeTwistIsoNegativeTensorPower :
    negativeTwist D ≅ Stacks.SheafOfModules.Invertible.tensorPower X.sheaf.obj
      (structureSheafRing X.toRingedSpace).property (invertibleSheaf D) (-1)
```

**`Stacks.Divisors.canonicalSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheaf.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheaf.lean#L244). The attribute's comment: “(2): the canonical section”.

> **Stacks Project, Tag 01WX (2).** The canonical section `1 = 1_D`: the global section of
> `𝒪_S(D)` corresponding to the inclusion mapping `ℐ_D ⟶ 𝒪_S`.
>
> A section of `SheafHom(ℐ_D, 𝒪_S)` over an open `U` is a morphism `ℐ_D|_U ⟶ 𝒪_S|_U` of
> presheaves of modules on the slice site over `U` (Tag 03EM), so the global section in question
> is the restriction of `idealInclusion` to the slice site over `⊤`.

```lean
noncomputable def canonicalSection : (invertibleSheaf D).val.obj (op (⊤ : Opens X))
```

## Tag 0B3P, a lemma

[Tag 0B3P](https://stacks.math.columbia.edu/tag/0B3P) in the Stacks Project.

**`Stacks.CartierConormal.conormalSheafIsoNegativeTwist`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CartierConormal/Basic.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/CartierConormal/Basic.lean#L57). The attribute's comment: “conormal sheaf”. References: EGA II (8.9.4), “partial”.

> For an ideal sheaf datum `D` on a scheme `X`, the conormal sheaf of the closed immersion
> `D.subschemeι` is the restriction to the subscheme of the ideal sheaf `ℐ_D`, that is, of
> `𝒪_X(-D)`.

```lean
noncomputable def conormalSheafIsoNegativeTwist {X : Scheme.{u}} (D : X.IdealSheafData) :
    Stacks.Conormal.conormalSheaf D.subschemeι ≅
      (modulePullback D.subschemeι.toLRSHom.toShHom).obj
        (Stacks.ClosedImmersion.idealSheaf D.subschemeι.toLRSHom.toShHom)
```

**`Stacks.Divisors.conormalSheafIsoNegativeTwist_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalAlgebra/AffineGenerators.lean, line 578](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalAlgebra/AffineGenerators.lean#L578). The attribute's comment: “canonical ideal quotient”.

> **Stacks Project, Tag 0B3P**, the canonical-ideal-quotient clause: on an affine open `U` of
> `X` carrying an affine model `D ∩ U = Spec (Γ(X, U) ⧸ I)` of the closed subscheme `D`, the affine
> computation of the conormal sheaf of `D` sends the image of a section `x` of `ℐ_D` over `U` —
> pulled back to `D` by the unit of the adjunction and read on the conormal sheaf through
> `Stacks.Divisors.conormalSheafIsoNegativeTwist` — to the class of `x` modulo `I²`.
>
> The sheaf `𝒪_X(-D)` of Tag 01WX is the ideal sheaf `ℐ_D` itself, so this is the normalisation of
> both of Tag 0B3P's descriptions of the conormal sheaf at once.

```lean
theorem conormalSheafIsoNegativeTwist_apply {X : Scheme.{u}} (D : X.IdealSheafData)
    (U : X.Opens) (hU : IsAffineOpen U) (I : Ideal Γ(X, U))
    (e : Limits.pullback D.subschemeι U.ι ≅ Spec (.of (Γ(X, U) ⧸ I)))
    (he : Limits.pullback.snd D.subschemeι U.ι ≫ hU.isoSpec.hom =
      e.hom ≫ Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I)))
    (x : (Stacks.ClosedImmersion.idealSheaf D.subschemeι.toLRSHom.toShHom).val.obj (op U))
    (hx : (kernel.ι (SheafOfModules.unitToPushforwardObjUnit
      (structureSheafHom D.subschemeι.toLRSHom.toShHom))).val.app (op U) x ∈ I) :
    (Stacks.Conormal.affineConormalIsoCotangent D.subschemeι U hU I e he).hom.hom
        ((conormalSheafIsoNegativeTwist D).inv.val.app
          (op ((opensMap D.subschemeι.toLRSHom.toShHom).obj U))
          (((modulePullbackPushforwardAdjunction D.subschemeι.toLRSHom.toShHom).unit.app
            (Stacks.ClosedImmersion.idealSheaf
              D.subschemeι.toLRSHom.toShHom)).val.app (op U) x))
      = I.toCotangent ⟨(kernel.ι (SheafOfModules.unitToPushforwardObjUnit
          (structureSheafHom D.subschemeι.toLRSHom.toShHom))).val.app (op U) x, hx⟩
```

**`Stacks.Divisors.conormalSheafIsoNegativeTwist`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/NormalSheaf.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/NormalSheaf.lean#L280). The attribute's comment: “conormal sheaf”.

> **Stacks Project, Tag 0B3P**, the conormal-sheaf clause: the conormal sheaf of a closed
> subscheme `D ⊆ X` is the restriction `ℐ_D|_D = 𝒪_X(-D)|_D` of its ideal sheaf.
>
> The conormal sheaf of Tag 01R2 is computed through the `liftCoborder` factorization of the
> immersion; for a closed immersion the open through which it factors is the whole target
> (`coborderRange_eq_top`) and its open immersion is an isomorphism
> (`isIso_coborderRange_ι`), so `Stacks.ClosedImmersion.pullbackIdealSheafIso` identifies the two
> pullbacks. The sheaf `𝒪_X(-D)` of Tag 01WX is the ideal sheaf itself, so the right-hand side is
> both descriptions at once.

```lean
noncomputable def conormalSheafIsoNegativeTwist {X : Scheme.{u}} (D : X.IdealSheafData) :
    (modulePullback D.subschemeι.liftCoborder.toLRSHom.toShHom).obj
        (Stacks.ClosedImmersion.idealSheaf
          D.subschemeι.liftCoborder.toLRSHom.toShHom) ≅
      (modulePullback D.subschemeι.toLRSHom.toShHom).obj
        (Stacks.ClosedImmersion.idealSheaf D.subschemeι.toLRSHom.toShHom)
```

**`Stacks.Divisors.normalSheafIsoInvertibleSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/NormalSheaf.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/NormalSheaf.lean#L301). The attribute's comment: “normal sheaf”.

> **Stacks Project, Tag 0B3P**, the normal-sheaf clause: the normal sheaf of an effective
> Cartier divisor `D ⊆ X` is the restriction `𝒪_X(D)|_D` of its associated invertible sheaf
> `𝒪_X(D) = SheafHom(ℐ_D, 𝒪_X)`.
>
> There is no hypothesis beyond the divisor. The stalk formula of Tag 0098 for `modulePullback`
> along the closed immersion of `D`, which used to be carried here as
> `Stacks.RingedSpace.PullbackStalkFormula`, is a theorem
> (`Stacks.RingedSpace.pullbackStalkFormula`), so Tag 01CD is available outright as
> `Stacks.RingedSpace.isIso_comparison`.

```lean
noncomputable def normalSheafIsoInvertibleSheaf {X : Scheme.{u}} (D : X.IdealSheafData)
    [IsEffectiveCartierDivisor D] :
    normalSheaf D.subschemeι ≅
      (modulePullback D.subschemeι.toLRSHom.toShHom).obj
        (Stacks.SheafOfModules.dualSheaf X.sheaf.obj (structureSheafRing X.toRingedSpace).property
          (Stacks.ClosedImmersion.idealSheaf D.subschemeι.toLRSHom.toShHom))
```

**`Stacks.Divisors.normalSheafIsoInvertibleSheaf_eval`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/NormalSheafEvaluation.lean, line 494](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/NormalSheafEvaluation.lean#L494). The attribute's comment: “canonical evaluation”.

> Let `φ` be a section of `𝒪_X(D) = ℐ_D^∨` over `U` and `x` a section of `𝒪_X(-D) = ℐ_D` over
> `U`, both carried to `D` by the unit of `f^* ⊣ f_*` for the closed immersion `f` of `D`. The
> functional which `Stacks.Divisors.normalSheafIsoInvertibleSheaf` produces from `φ` on the
> conormal sheaf takes the image of `x` to the restriction of `φ(x)`.

```lean
theorem normalSheafIsoInvertibleSheaf_eval {X : Scheme.{u}} (D : X.IdealSheafData)
    [IsEffectiveCartierDivisor D] (U : Opens X)
    (φ : (dualSheaf X.sheaf.obj (structureSheafRing X.toRingedSpace).property
      (Stacks.ClosedImmersion.idealSheaf D.subschemeι.toLRSHom.toShHom)).val.obj (op U))
    (x : (Stacks.ClosedImmersion.idealSheaf
      D.subschemeι.toLRSHom.toShHom).val.obj (op U)) :
    evalSection D.subscheme.sheaf.obj
        ((modulePullback D.subschemeι.liftCoborder.toLRSHom.toShHom).obj
          (Stacks.ClosedImmersion.idealSheaf
            D.subschemeι.liftCoborder.toLRSHom.toShHom)).val
        (_root_.SheafOfModules.unit (Stacks.SheafOfModules.TensorSheafification.structureSheaf
          D.subscheme.sheaf.obj
          (structureSheafRing D.subscheme.toRingedSpace).property)).val
        (op ((opensMap D.subschemeι.toLRSHom.toShHom).obj U))
        ((normalSheafIsoInvertibleSheaf D).inv.val.app
          (op ((opensMap D.subschemeι.toLRSHom.toShHom).obj U))
          (((modulePullbackPushforwardAdjunction
              D.subschemeι.toLRSHom.toShHom).unit.app
            (dualSheaf X.sheaf.obj (structureSheafRing X.toRingedSpace).property
              (Stacks.ClosedImmersion.idealSheaf
                D.subschemeι.toLRSHom.toShHom))).val.app (op U) φ))
        ((conormalSheafIsoNegativeTwist D).inv.val.app
          (op ((opensMap D.subschemeι.toLRSHom.toShHom).obj U))
          (((modulePullbackPushforwardAdjunction
              D.subschemeι.toLRSHom.toShHom).unit.app
            (Stacks.ClosedImmersion.idealSheaf
              D.subschemeι.toLRSHom.toShHom)).val.app (op U) x)) =
      ((structureSheafHom D.subschemeι.toLRSHom.toShHom).hom.app (op U)).hom
        (evalSection X.sheaf.obj
          (Stacks.ClosedImmersion.idealSheaf D.subschemeι.toLRSHom.toShHom).val
          (_root_.SheafOfModules.unit (Stacks.SheafOfModules.TensorSheafification.structureSheaf
            X.sheaf.obj
            (structureSheafRing X.toRingedSpace).property)).val (op U) φ x)
```

## Tag 0C4T, a lemma

[Tag 0C4T](https://stacks.math.columbia.edu/tag/0C4T) in the Stacks Project.

**`Stacks.Divisors.shortExact_sumKernelMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartier/SumKernelMap.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartier/SumKernelMap.lean#L298). The attribute's comment: “with the kernel inclusion named, rather than existentially bound”. References: SGA 7 X (1.13), “more general”.

> **[Stacks, Tag 0C4T] with its kernel inclusion named.** For `D ⊆ D'` effective Cartier
> divisors on a scheme `X` and `C` an effective Cartier divisor with `D' = D + C`, the sequence
> `0 ⟶ 𝒪_X(-D)|_C ⟶ 𝒪_{D'} ⟶ 𝒪_D ⟶ 0` is short exact, with first map
> `Stacks.Divisors.sumKernelMap` and second map the canonical restriction.
>
> `Stacks.Divisors.addEffectiveCartierDivisor_shortExact` is the same assertion with the first map
> bound by an existential; this version is the one a consumer needs in order to state an equation
> about that map, and `Stacks.Divisors.eq_sumKernelMap` shows the two are about the same morphism.
> The sum is written `C * D` rather than `D * C` because the named morphism's type mentions it, so
> no `mul_comm` can be absorbed into a proof.

```lean
public theorem shortExact_sumKernelMap (D C : X.IdealSheafData)
    (hD : IsEffectiveCartierDivisor D) (hsub : C * D ≤ D) :
    (ShortComplex.mk (sumKernelMap D C hD)
      (Scheme.IdealSheafData.closedSubschemeRestriction hsub)
      (sumKernelMap_comp_closedSubschemeRestriction D C hD hsub)).ShortExact
```

**`Stacks.Divisors.addEffectiveCartierDivisor_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartier/SumSequence.lean, line 1070](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartier/SumSequence.lean#L1070).

> **Stacks Project, Tag 0C4T.**  Let `D ⊆ D'` be effective Cartier divisors on a scheme `X`
> and let `C` be an effective Cartier divisor with `D' = D + C`, which exists by
> [Stacks, Tag 02ON].  Then there is a short exact sequence
> `0 ⟶ 𝒪_X(-D)|_C ⟶ 𝒪_{D'} ⟶ 𝒪_D ⟶ 0` of `𝒪_X`-modules.

```lean
theorem addEffectiveCartierDivisor_shortExact (D D' C : X.IdealSheafData)
    (hD : IsEffectiveCartierDivisor D) (hsub : D' ≤ D) (hsum : D' = D * C) :
    ∃ f : (Scheme.Modules.pushforward C.subschemeι).obj
          ((Scheme.Modules.pullback C.subschemeι).obj (negativeTwist D)) ⟶
        Scheme.IdealSheafData.closedSubschemeStructureSheaf D',
      ∃ zero : f ≫ Scheme.IdealSheafData.closedSubschemeRestriction hsub = 0,
        (ShortComplex.mk f (Scheme.IdealSheafData.closedSubschemeRestriction hsub)
          zero).ShortExact
```

## Tag 02OP, a lemma

[Tag 02OP](https://stacks.math.columbia.edu/tag/02OP) in the Stacks Project.

**`Stacks.Divisors.invertibleSheafSumIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheafSum.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheafSum.lean#L323). The attribute's comment: “existence and distinguished-section compatibility”. References: EGA IV (21.2.8), “(21.2.8.3), special case”.

> The canonical identification `𝒪_X(D) ⊗_{𝒪_X} 𝒪_X(D') ≅ 𝒪_X(D + D')` of the tensor product
> of the invertible sheaves of two effective Cartier divisors with the invertible sheaf of their
> sum, carrying the pure tensor `1_D ⊗ 1_{D'}` of the canonical sections to the canonical section
> `1_{D + D'}`.

```lean
def invertibleSheafSumIso [IsEffectiveCartierDivisor D] [IsEffectiveCartierDivisor D'] :
    sumSheaf D D' ≅ invertibleSheaf' (D * D')
```

**`Stacks.Divisors.invertibleSheafSumIso_canonicalSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheafSum.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheafSum.lean#L330). The attribute's comment: “existence and distinguished-section compatibility”.

> Under `Stacks.Divisors.invertibleSheafSumIso` the pure tensor `1_D ⊗ 1_{D'}` of the canonical
> sections of `𝒪_X(D)` and `𝒪_X(D')` is the canonical section `1_{D + D'}` of `𝒪_X(D + D')`.

```lean
theorem invertibleSheafSumIso_canonicalSection
    [IsEffectiveCartierDivisor D] [IsEffectiveCartierDivisor D'] :
    Scheme.Modules.Hom.app (invertibleSheafSumIso D D').hom ⊤ (canonicalSectionTensor D D') =
      (canonicalSection' (D * D')).val (op ⊤)
```

**`Stacks.Divisors.invertibleSheafSumIso_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheafSum.lean, line 339](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheafSum.lean#L339). The attribute's comment: “uniqueness”.

> An isomorphism `𝒪_X(D) ⊗ 𝒪_X(D') ≅ 𝒪_X(D + D')` carrying `1_D ⊗ 1_{D'}` to `1_{D + D'}` is
> `Stacks.Divisors.invertibleSheafSumIso`.

```lean
theorem invertibleSheafSumIso_unique
    [IsEffectiveCartierDivisor D] [IsEffectiveCartierDivisor D']
    (e : sumSheaf D D' ≅ invertibleSheaf' (D * D'))
    (he : Scheme.Modules.Hom.app e.hom ⊤ (canonicalSectionTensor D D') =
      (canonicalSection' (D * D')).val (op ⊤)) :
    e = invertibleSheafSumIso D D'
```

## Tag 0C4U, a lemma

[Tag 0C4U](https://stacks.math.columbia.edu/tag/0C4U) in the Stacks Project.

**`Stacks.Divisors.invertibleSheafPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheafPullback.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheafPullback.lean#L194). The attribute's comment: “associated sheaf”.

> **Stacks Project, Tag 0C4U.** The canonical identification `f^* 𝒪_Y(D) ≅ 𝒪_X(f^{-1}D)` of
> the invertible sheaf of an effective Cartier divisor whose pullback is defined with the
> invertible sheaf of its inverse image.

```lean
def invertibleSheafPullbackIso :
    (Scheme.Modules.pullback f).obj (invertibleSheaf' D) ≅ invertibleSheaf' (D.comap f)
```

**`Stacks.Divisors.invertibleSheafPullbackIso_canonicalSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheafPullback.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSheafPullback.lean#L202). The attribute's comment: “canonical section”.

> **Stacks Project, Tag 0C4U.** Under the identification
> `Stacks.Divisors.invertibleSheafPullbackIso` the pullback of the canonical section `1_D` is the
> canonical section `1_{f^{-1}D}`.

```lean
theorem invertibleSheafPullbackIso_canonicalSection :
    Scheme.Modules.Hom.app (invertibleSheafPullbackIso f D).hom ⊤
        (pullbackCanonicalSection f D) =
      (canonicalSection' (D.comap f)).val (op ⊤)
```

## Tag 01WY, a definition

[Tag 01WY](https://stacks.math.columbia.edu/tag/01WY) in the Stacks Project.

**`AlgebraicGeometry.IsRegularSection`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/RegularSections.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/RegularSections.lean#L107).

> A global section is regular when multiplication by it gives a monomorphism
> from the structure sheaf to its module sheaf.

```lean
noncomputable abbrev IsRegularSection
    {L : SheafOfModules.{w}
      (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO)}
    (s : L.sections) : Prop
```

## Tag 01WZ, a lemma

[Tag 01WZ](https://stacks.math.columbia.edu/tag/01WZ) in the Stacks Project.

**`AlgebraicGeometry.isRegularSection_iff_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/RegularSections.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/RegularSections.lean#L257). The attribute's comment: “conditions (1) and (2)”.

> A section of the structure sheaf is regular if and only if its germ at every point is a
> nonzerodivisor.

```lean
theorem isRegularSection_iff_stalk
    (X : LocallyRingedSpace.{u})
    (f : (SheafOfModules.unit
      ((sheafCompose (Opens.grothendieckTopology X)
        (forget₂ CommRingCat.{u} RingCat.{u})).obj X.sheaf)).sections) :
    IsRegularSection X.presheaf
        ((Presheaf.isSheaf_iff_isSheaf_comp _ X.presheaf
          (forget₂ CommRingCat.{u} RingCat.{u})).mp X.IsSheaf) f ↔
      ∀ x : X, IsSMulRegular (X.presheaf.stalk x)
        (X.presheaf.germ ⊤ x trivial (f.val (.op ⊤)))
```

**`AlgebraicGeometry.isRegularSection_iff_affineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/RegularSections.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/RegularSections.lean#L300). The attribute's comment: “conditions (1) and (3)”.

> On a scheme, a section of the structure sheaf is regular if and only if its restriction
> to every affine open is a nonzerodivisor.

```lean
theorem isRegularSection_iff_affineOpen
    (X : Scheme.{u})
    (f : (SheafOfModules.unit
      ((sheafCompose (Opens.grothendieckTopology X)
        (forget₂ CommRingCat.{u} RingCat.{u})).obj X.sheaf)).sections) :
    IsRegularSection X.presheaf
        ((Presheaf.isSheaf_iff_isSheaf_comp _ X.presheaf
          (forget₂ CommRingCat.{u} RingCat.{u})).mp X.IsSheaf) f ↔
      ∀ U : X.Opens, IsAffineOpen U →
        IsSMulRegular Γ(X, U) (show Γ(X, U) from f.val (.op U))
```

**`AlgebraicGeometry.isRegularSection_iff_exists_affineOpenCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/RegularSections.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/RegularSections.lean#L319). The attribute's comment: “conditions (1) and (4)”.

> On a scheme, a section of the structure sheaf is regular if and only if its restrictions
> are nonzerodivisors on the members of some affine open covering.

```lean
theorem isRegularSection_iff_exists_affineOpenCover
    (X : Scheme.{u})
    (f : (SheafOfModules.unit
      ((sheafCompose (Opens.grothendieckTopology X)
        (forget₂ CommRingCat.{u} RingCat.{u})).obj X.sheaf)).sections) :
    IsRegularSection X.presheaf
        ((Presheaf.isSheaf_iff_isSheaf_comp _ X.presheaf
          (forget₂ CommRingCat.{u} RingCat.{u})).mp X.IsSheaf) f ↔
      ∃ (I : Type u) (U : I → X.Opens), IsOpenCover U ∧
        (∀ i, IsAffineOpen (U i) ∧
          IsSMulRegular Γ(X, U i) (show Γ(X, U i) from f.val (.op (U i))))
```

## Tag 02OQ, a definition

[Tag 02OQ](https://stacks.math.columbia.edu/tag/02OQ) in the Stacks Project.

**`Stacks.Divisors.zeroScheme`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinConstruction/ZeroScheme.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/GysinConstruction/ZeroScheme.lean#L56). The attribute's comment: “the closed subscheme construction”.

> **Stacks 02OQ.** The quasi-coherent ideal sheaf cutting out the zero scheme of a global
> section `s` of an invertible module `L` on `X`: on an affine open `U` it is generated by the
> values `φ (s|_U)` of the `Γ(X, U)`-linear functionals `φ` on `Γ(L, U)`. The closed subscheme
> itself is `(zeroScheme X L s).subscheme`, with closed immersion
> `(zeroScheme X L s).subschemeι`.

```lean
noncomputable abbrev zeroScheme (X : Scheme.{u}) (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : Γ(L, ⊤)) : X.IdealSheafData
```

**`Stacks.Divisors.zeroScheme_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ZeroSchemePullback/ZeroSchemeIdeal.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ZeroSchemePullback/ZeroSchemeIdeal.lean#L189). The attribute's comment: “the defining ideal”.

> **Stacks 02OQ**, the defining ideal. The ideal of the zero scheme of a global section `s` of
> an invertible module `L` on an affine open `U` is generated by the values `φ (s|_U)` of the
> `Γ(X, U)`-linear functionals on `Γ(L, U)`: the prescribed affine-local family is already an ideal
> sheaf, so `Scheme.IdealSheafData.ofIdeals` leaves it untouched.

```lean
theorem zeroScheme_ideal (X : Scheme.{u}) (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : Γ(L, ⊤)) (U : X.affineOpens) :
    (zeroScheme X L s).ideal U =
      Ideal.span {a : Γ(X, U.1) | ∃ φ : Γ(L, U.1) →ₗ[Γ(X, U.1)] Γ(X, U.1),
        a = φ (L.presheaf.map (homOfLE le_top).op s)}
```

**`AlgebraicGeometry.zeroScheme`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeData.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeData.lean#L198). The attribute's comment: “the closed subscheme construction”.

> The zero scheme of a global section `s` of an invertible module `L`, as a quasi-coherent sheaf
> of ideals: on an affine open it is the image of the dual map `s : L^{⊗ -1} ⟶ 𝒪_X`, i.e. the ideal
> generated by the values of `s` under the linear functionals on the sections of `L`.

```lean
noncomputable abbrev zeroScheme (X : Scheme.{u}) (L : X.Modules)
    [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : Γ(L, ⊤)) : X.IdealSheafData
```

**`AlgebraicGeometry.zeroScheme_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeData.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeData.lean#L208). The attribute's comment: “the defining ideal”.

> The defining ideal of the zero scheme on an affine open is the ideal generated by the values of
> the restricted section under the local linear functionals.

```lean
theorem zeroScheme_ideal (X : Scheme.{u}) (L : X.Modules)
    [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : Γ(L, ⊤)) (U : X.affineOpens) :
    (zeroScheme X L s).ideal U =
      Ideal.span {a : Γ(X, U.1) | ∃ φ : Γ(L, U.1) →ₗ[Γ(X, U.1)] Γ(X, U.1),
        a = φ (L.presheaf.map (homOfLE le_top).op s)}
```

**`Stacks.Tag02OQSectionIdeal.zeroScheme_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionIdeal/Qcoh.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SectionIdeal/Qcoh.lean#L204). The attribute's comment: “the defining ideal”.

> **Stacks Tag 02OQ, the defining ideal of the zero scheme.**  On every affine open the ideal of
> the zero scheme of a global section of an invertible module is the ideal generated by the values of
> the restricted section under all linear functionals there.
>
> `Scheme.IdealSheafData.ofIdeals` is a supremum and in general shrinks the family it is applied to;
> it does not here, because that family is already compatible with passage to a basic open and hence
> is itself an ideal sheaf.

```lean
theorem zeroScheme_ideal (L : X.Modules)
    [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (t : Γ(L, ⊤)) (U : X.affineOpens) :
    (Stacks.RegularSectionSequence.zeroScheme X L t).ideal U =
      Ideal.span {a : Γ(X, U.1) | ∃ φ : Γ(L, U.1) →ₗ[Γ(X, U.1)] Γ(X, U.1),
        a = φ (L.presheaf.map (homOfLE le_top).op t)}
```

## Tag 02OR, a lemma

[Tag 02OR](https://stacks.math.columbia.edu/tag/02OR) in the Stacks Project.

**`Stacks.Divisors.pullbackSection_eq_zero_iff_factorsThrough_zeroScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ZeroSchemePullback/Factorization.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ZeroSchemePullback/Factorization.lean#L378). The attribute's comment: “factorization”.

> A global section `s` of an invertible module `L` on `X` vanishes after pullback along
> `f : Y ⟶ X` if and only if `f` factors through the zero scheme of `s`.

```lean
theorem pullbackSection_eq_zero_iff_factorsThrough_zeroScheme
    (X : Scheme.{u}) (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : Γ(L, ⊤)) {Y : Scheme.{u}} (f : Y ⟶ X) :
    pullbackGlobalSections f L s = 0 ↔
      ∃ g : Y ⟶ (_root_.Stacks.Divisors.zeroScheme X L s).subscheme,
        g ≫ (_root_.Stacks.Divisors.zeroScheme X L s).subschemeι = f
```

**`AlgebraicGeometry.pullbackSection_eq_zero_iff_factorsThrough_zeroScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeFactorization.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeFactorization.lean#L210). The attribute's comment: “factorization”.

> **Stacks Tag 02OR (2).** A global section of an invertible module vanishes after pullback
> along `f` if and only if `f` factors through its zero scheme.

```lean
theorem pullbackSection_eq_zero_iff_factorsThrough_zeroScheme (X : Scheme.{u}) (L : X.Modules)
    [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L] (s : Γ(L, ⊤))
    {Y : Scheme.{u}} (f : Y ⟶ X) :
    pullbackGlobalSections f L s = 0 ↔
      ∃ g : Y ⟶ (zeroScheme X L s).subscheme,
        g ≫ (zeroScheme X L s).subschemeι = f
```

**`AlgebraicGeometry.zeroScheme_isGreatest_vanishingClosedSubscheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeFactorization.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeFactorization.lean#L275). The attribute's comment: “maximal”.

> **Stacks Tag 02OR (1).** Among the closed subschemes on which the section pulls back to
> zero, the zero scheme is the largest. Closed subschemes are ordered by their ideal sheaves, and
> geometric inclusion is the reverse of that order, which is why the statement is about the order
> dual.

```lean
theorem zeroScheme_isGreatest_vanishingClosedSubscheme (X : Scheme.{u}) (L : X.Modules)
    [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L] (s : Γ(L, ⊤)) :
    IsGreatest
      {I : (X.IdealSheafData)ᵒᵈ |
        pullbackGlobalSections (OrderDual.ofDual I).subschemeι L s = 0}
      (OrderDual.toDual (zeroScheme X L s))
```

**`AlgebraicGeometry.isLocallyPrincipal_zeroScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeProperties.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeProperties.lean#L81). The attribute's comment: “locally\_principal”.

> **Stacks Tag 02OR (3).** The zero scheme of a global section of an invertible module is a
> locally principal closed subscheme: on the trivializing opens its ideal is generated by the one
> function representing the section.

```lean
theorem isLocallyPrincipal_zeroScheme (X : Scheme.{u}) (L : X.Modules)
    [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : Γ(L, ⊤)) : Stacks.Divisors.IsLocallyPrincipal (zeroScheme X L s)
```

**`AlgebraicGeometry.isEffectiveCartierDivisor_zeroScheme_iff_isRegularSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeRegular.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeRegular.lean#L221). The attribute's comment: “cartier\_iff\_regular”.

> **Stacks Project, Tag 02OR (4).** The zero scheme of a global section `s` of an invertible
> module is an effective Cartier divisor if and only if `s` is a nonzerodivisor.

```lean
theorem isEffectiveCartierDivisor_zeroScheme_iff_isRegularSection (s : L.sections) :
    Stacks.Divisors.IsEffectiveCartierDivisor (zeroScheme X L (s.eval (op ⊤))) ↔
      IsRegularSection X.sheaf.obj X.ringCatSheaf.property s
```

## Tag 01X0, a lemma

[Tag 01X0](https://stacks.math.columbia.edu/tag/01X0) in the Stacks Project.

**`Stacks.Divisors.canonicalSection_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/CanonicalSectionRegular.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/CanonicalSectionRegular.lean#L180). The attribute's comment: “canonical\_section\_regular”.

> **The first clause of [Stacks, Tag 01X0].** For `D ⊆ X` an effective Cartier divisor on a
> scheme, the canonical section `1_D` of `𝒪_X(D)` is a regular section.
>
> Tensoring with `ℐ_D` is an autoequivalence of the category of `𝒪_X`-modules, since `ℐ_D` is
> invertible, so it is faithful and therefore reflects monomorphisms; and
> `Stacks.Divisors.evaluation_canonicalHom` identifies the image of `1_D` under it, up to the left
> unitor and the evaluation isomorphism, with the inclusion `ℐ_D ⟶ 𝒪_X`, which is a kernel
> morphism and hence a monomorphism.

```lean
theorem canonicalSection_isRegular [IsEffectiveCartierDivisor D] :
    AlgebraicGeometry.IsRegularSection X.presheaf
      (structureSheafRing X.toRingedSpace).property (canonicalSection' D)
```

**`AlgebraicGeometry.existsUnique_invertibleSheafIso_zeroScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularSectionCorrespondence.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularSectionCorrespondence.lean#L250). The attribute's comment: “regular\_section\_divisor”.

> **There is a unique isomorphism from the invertible sheaf of the zero scheme of a regular
> section to the original invertible sheaf that sends its canonical section to that section.**
> This is [Stacks, Tag 01X0] (2): for `s` a regular section of an invertible `𝒪_X`-module `L` the
> zero scheme `D = Z(s)` is an effective Cartier divisor
> (`AlgebraicGeometry.isEffectiveCartierDivisor_zeroScheme_iff_isRegularSection`) and `𝒪_X(D) ≅ L`
> by a unique isomorphism matching `1_D` with `s`.
>
> Existence is `AlgebraicGeometry.invertibleSheafIsoZeroSchemeOfIsRegularSection` and its section
> identity; uniqueness is `AlgebraicGeometry.eq_id_of_sectionsMap_eq`, applied to the endomorphism
> of `L` built from two such isomorphisms.

```lean
theorem existsUnique_invertibleSheafIso_zeroScheme (X : Scheme.{u}) (L : X.Modules)
    [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L] (s : L.sections)
    (hs : IsRegularSection X.sheaf.obj X.ringCatSheaf.property s) :
    ∃! e : Stacks.Divisors.invertibleSheaf' (zeroScheme X L (s.eval (op ⊤))) ≅ L,
      Scheme.Modules.Hom.app e.hom ⊤
          ((Stacks.Divisors.canonicalSection'
            (zeroScheme X L (s.eval (op ⊤)))).eval (op ⊤)) = s.eval (op ⊤)
```

**`AlgebraicGeometry.effectiveCartierDivisor_equiv_regularSectionClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularSectionCorrespondence.lean, line 398](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularSectionCorrespondence.lean#L398). The attribute's comment: “divisor\_regular\_section\_equiv”. References: EGA IV (21.3.3), “(ii)”.

> **The canonical bijection between the effective Cartier divisors on a scheme and the
> isomorphism classes of invertible modules with a regular global section**
> ([Stacks, Tag 01X0]).
>
> Forwards a divisor `D` goes to the class of `(𝒪_X(D), 1_D)`; backwards a pair `(L, s)` goes to
> the zero scheme `Z(s)`, which is well defined on classes by
> `AlgebraicGeometry.RegularSectionPair.zeroScheme_eq_of_isIsomorphic`. The two round trips are
> `Z(1_D) = D` (`Stacks.Divisors.zeroScheme_canonicalSection`) and
> `(𝒪_X(Z(s)), 1_{Z(s)}) ≅ (L, s)`
> (`AlgebraicGeometry.invertibleSheafIsoZeroSchemeOfIsRegularSection`).

```lean
def effectiveCartierDivisor_equiv_regularSectionClass (X : Scheme.{u}) :
    EffectiveCartierDivisor X ≃ RegularSectionClass X
```

**`AlgebraicGeometry.effectiveCartierDivisor_equiv_regularSectionClass_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularSectionCorrespondence.lean, line 413](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularSectionCorrespondence.lean#L413). The attribute's comment: “divisor\_regular\_section\_equiv”.

> **The forward map of the bijection of [Stacks, Tag 01X0] sends an effective Cartier divisor
> to the isomorphism class of its invertible sheaf with its canonical section**, which is a regular
> section.

```lean
theorem effectiveCartierDivisor_equiv_regularSectionClass_apply (D : EffectiveCartierDivisor X) :
    ∃ h : IsRegularSection X.sheaf.obj X.ringCatSheaf.property
        (Stacks.Divisors.canonicalSection' D.1),
      effectiveCartierDivisor_equiv_regularSectionClass X D =
        RegularSectionPair.classOf
          ⟨Stacks.Divisors.invertibleSheaf' D.1,
            @Stacks.Divisors.isInvertible_divisorSheaf X D.1 D.2,
            Stacks.Divisors.canonicalSection' D.1, h⟩
```

**`AlgebraicGeometry.effectiveCartierDivisor_equiv_regularSectionClass_symm_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularSectionCorrespondence.lean, line 427](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularSectionCorrespondence.lean#L427). The attribute's comment: “divisor\_regular\_section\_equiv”.

> **The inverse map of the bijection of [Stacks, Tag 01X0] sends the class of a regular-section
> pair to the effective Cartier divisor cut out by its zero scheme.** The equation holds for every
> representative of the class.

```lean
theorem effectiveCartierDivisor_equiv_regularSectionClass_symm_apply (P : RegularSectionPair X) :
    ∃ h : Stacks.Divisors.IsEffectiveCartierDivisor P.zeroScheme,
      (effectiveCartierDivisor_equiv_regularSectionClass X).symm P.classOf = ⟨P.zeroScheme, h⟩
```

**`Stacks.Divisors.zeroScheme_canonicalSection'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeCanonicalSection.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeCanonicalSection.lean#L196). The attribute's comment: “zeroScheme\_canonicalSection”.

> **`Z(1_D) = D`.** The zero scheme of the canonical section of `𝒪_X(D)` is `D` itself: the
> composite `D ↦ (𝒪_X(D), 1_D) ↦ Z(1_D)` is the identity.

```lean
theorem zeroScheme_canonicalSection' :
    zeroScheme X (modulesInvertibleSheaf D) (canonicalSection D) = D
```

**`Stacks.Divisors.isRegularSection_canonicalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeCanonicalSection.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeCanonicalSection.lean#L210). The attribute's comment: “canonical\_section\_regular”.

> The canonical section `1_D` of `𝒪_X(D)` is a regular section, i.e. a nonzerodivisor
> ([Stacks, Tag 01WY]).

```lean
theorem isRegularSection_canonicalSections :
    IsRegularSection X.sheaf.obj X.ringCatSheaf.property (canonicalSections D)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.isEffectiveCartierDivisor_zeroScheme_iff_isRegularSection`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeRegular.lean#L221), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Divisors/RegularSectionCorrespondence.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularSectionCorrespondence.lean#L236) (StacksFrontier): “regular\_section\_divisor”.

## Tag 0C6K, a remark

[Tag 0C6K](https://stacks.math.columbia.edu/tag/0C6K) in the Stacks Project.

**`Stacks.Divisors.shortExact_divisor_normal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/DivisorNormalSequence.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/DivisorNormalSequence.lean#L92). The attribute's comment: “divisor\_normal\_sequence”.

> **Stacks Tag 0C6K, the label `divisor_normal_sequence`.** For an effective Cartier divisor
> `D ⊆ X` with inclusion `i`, the normal sheaf `𝒩_{D/X}` is the restriction `i^* 𝒪_X(D)`, and
>
> `0 ⟶ 𝒪_X ⟶ 𝒪_X(D) ⟶ i_* 𝒩_{D/X} ⟶ 0`
>
> is short exact, the first map being multiplication by the canonical section `1_D` and the second
> the unit of `i^* ⊣ i_*` followed by the pushforward of that identification.

```lean
theorem shortExact_divisor_normal :
    let i := D.subschemeι
    let L : X.Modules := invertibleSheaf D
    let N : D.subscheme.Modules := normalSheaf i
    ∃ e : (Scheme.Modules.pullback i).obj L ≅ N,
      let O : X.Modules := SheafOfModules.unit X.ringCatSheaf
      let f : O ⟶ L := L.unitHomEquiv.symm (canonicalSections D)
      let g : L ⟶ (Scheme.Modules.pushforward i).obj N :=
        (Scheme.Modules.pullbackPushforwardAdjunction i).unit.app L ≫
          (Scheme.Modules.pushforward i).map e.hom
      ∃ h : f ≫ g = 0, (ShortComplex.mk f g h).ShortExact
```

**`AlgebraicGeometry.shortExact_zeroScheme_ideal_of_isRegularSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularSectionIdealSequence.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularSectionIdealSequence.lean#L204). The attribute's comment: “regular\_section\_ideal\_sequence”.

> **Stacks Tag 0C6K, the label `regular_section_ideal_sequence`.** For an invertible module
> `L` on a scheme `X` and a regular global section `s` of `L` ([Stacks, Tag 01WY]), the sequence
>
> `0 ⟶ L^{⊗ -1} ⟶ 𝒪_X ⟶ i_* 𝒪_{Z(s)} ⟶ 0`
>
> is short exact, where `i` is the inclusion of the zero scheme of `s`, the first map is
> multiplication by `s` through the canonical trivialization `L^{⊗ -1} ⊗ L ≅ 𝒪_X` and the second
> is restriction to the zero scheme.

```lean
theorem shortExact_zeroScheme_ideal_of_isRegularSection (s : L.sections)
    (hs : IsRegularSection X.sheaf.obj X.ringCatSheaf.property s) :
    let i := (zeroScheme X L (s.eval (op ⊤))).subschemeι
    let Linv : X.Modules := inverseTensorPower X L
    let u : Linv ⟶ SheafOfModules.unit X.ringCatSheaf :=
      ((ρ_ Linv).inv ≫ Linv ◁ L.unitHomEquiv.symm s) ≫ (inverseTensorPowerIsoUnit X L).hom
    let q : SheafOfModules.unit X.ringCatSheaf ⟶
        (Scheme.Modules.pushforward i).obj
          (SheafOfModules.unit (zeroScheme X L (s.eval (op ⊤))).subscheme.ringCatSheaf) :=
      SheafOfModules.unitToPushforwardObjUnit i.toRingCatSheafHom
    ∃ h : u ≫ q = 0, (ShortComplex.mk u q h).ShortExact
```

**`AlgebraicGeometry.isEffectiveCartierDivisor_zeroScheme_and_shortExact_sequences`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularSectionRemark.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularSectionRemark.lean#L68).

> **Stacks Tag 0C6K.** Let `X` be a scheme.
>
> 1. For an invertible `𝒪_X`-module `L` and a regular section `s` of `L` ([Stacks, Tag 01WY]),
>    with `i` the inclusion of the zero scheme `Z(s)`: `Z(s)` is an effective Cartier divisor on
>    `X`, the sequence `0 ⟶ 𝒪_X ⟶ L ⟶ i_* i^* L ⟶ 0` is short exact (first map multiplication by
>    `s`, second the unit of `i^* ⊣ i_*`), and the sequence `0 ⟶ L^{⊗ -1} ⟶ 𝒪_X ⟶ i_* 𝒪_{Z(s)} ⟶ 0`
>    is short exact (first map multiplication by `s` read through `L^{⊗ -1} ⊗ L ≅ 𝒪_X`, second
>    restriction to the zero scheme).
> 2. For an effective Cartier divisor `D ⊆ X` with inclusion `i`: the normal sheaf `𝒩_{D/X}` is
>    `i^* 𝒪_X(D)` and `0 ⟶ 𝒪_X ⟶ 𝒪_X(D) ⟶ i_* 𝒩_{D/X} ⟶ 0` is short exact (first map
>    multiplication by the canonical section `1_D`), and `0 ⟶ ℐ_D ⟶ 𝒪_X ⟶ i_* 𝒪_D ⟶ 0` is short
>    exact.

```lean
theorem isEffectiveCartierDivisor_zeroScheme_and_shortExact_sequences (X : Scheme.{u}) :
    (∀ (L : X.Modules) [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
        (s : L.sections), IsRegularSection X.sheaf.obj X.ringCatSheaf.property s →
      Stacks.Divisors.IsEffectiveCartierDivisor (zeroScheme X L (s.eval (op ⊤))) ∧
      (let i := (zeroScheme X L (s.eval (op ⊤))).subschemeι
        let O : X.Modules := SheafOfModules.unit X.ringCatSheaf
        let f : O ⟶ L := L.unitHomEquiv.symm s
        let g : L ⟶ (Scheme.Modules.pushforward i).obj ((Scheme.Modules.pullback i).obj L) :=
          (Scheme.Modules.pullbackPushforwardAdjunction i).unit.app L
        ∃ h : f ≫ g = 0, (ShortComplex.mk f g h).ShortExact) ∧
      (let i := (zeroScheme X L (s.eval (op ⊤))).subschemeι
        let Linv : X.Modules := inverseTensorPower X L
        let u : Linv ⟶ SheafOfModules.unit X.ringCatSheaf :=
          ((ρ_ Linv).inv ≫ Linv ◁ L.unitHomEquiv.symm s) ≫ (inverseTensorPowerIsoUnit X L).hom
        let q : SheafOfModules.unit X.ringCatSheaf ⟶
            (Scheme.Modules.pushforward i).obj
              (SheafOfModules.unit (zeroScheme X L (s.eval (op ⊤))).subscheme.ringCatSheaf) :=
          SheafOfModules.unitToPushforwardObjUnit i.toRingCatSheafHom
        ∃ h : u ≫ q = 0, (ShortComplex.mk u q h).ShortExact)) ∧
    (∀ (D : X.IdealSheafData) [Stacks.Divisors.IsEffectiveCartierDivisor D],
      (let i := D.subschemeι
        let L : X.Modules := Stacks.Divisors.invertibleSheaf D
        let N : D.subscheme.Modules := Stacks.Divisors.normalSheaf i
        ∃ e : (Scheme.Modules.pullback i).obj L ≅ N,
          let O : X.Modules := SheafOfModules.unit X.ringCatSheaf
          let f : O ⟶ L := L.unitHomEquiv.symm (Stacks.Divisors.canonicalSections D)
          let g : L ⟶ (Scheme.Modules.pushforward i).obj N :=
            (Scheme.Modules.pullbackPushforwardAdjunction i).unit.app L ≫
              (Scheme.Modules.pushforward i).map e.hom
          ∃ h : f ≫ g = 0, (ShortComplex.mk f g h).ShortExact) ∧
      ∃ hz : Stacks.IdealSheafSequence.divisorIdealMap D ≫
          Stacks.IdealSheafSequence.divisorQuotientMap D = 0,
        (ShortComplex.mk (Stacks.IdealSheafSequence.divisorIdealMap D)
          (Stacks.IdealSheafSequence.divisorQuotientMap D) hz).ShortExact)
```

**`AlgebraicGeometry.exists_cokernelIso_unit_zeroScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeExactSequence.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeExactSequence.lean#L234). The attribute's comment: “regular\_section\_sequence”.

> For an invertible module `L` on a scheme `X` and a global section `s`, the unit of the
> pullback–pushforward adjunction along the inclusion `i` of the zero scheme `Z(s)` realizes
> `i_* i^* L` as the cokernel of multiplication by `s`.
>
> No regularity hypothesis on `s` is needed.

```lean
theorem exists_cokernelIso_unit_zeroScheme (s : L.sections) :
    let i := (zeroScheme X L (s.eval (op ⊤))).subschemeι
    ∃ e : cokernel (L.unitHomEquiv.symm s) ≅
        (Scheme.Modules.pushforward i).obj ((Scheme.Modules.pullback i).obj L),
      cokernel.π (L.unitHomEquiv.symm s) ≫ e.hom =
        (Scheme.Modules.pullbackPushforwardAdjunction i).unit.app L
```

**`AlgebraicGeometry.shortExact_zeroScheme_of_isRegularSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeExactSequence.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/ZeroSchemeExactSequence.lean#L269). The attribute's comment: “regular\_section\_sequence”.

> For an invertible module `L` on a scheme `X` and a regular global section `s`
> ([Stacks, Tag 01WY]), the sequence `0 ⟶ 𝒪_X ⟶ L ⟶ i_* i^* L ⟶ 0` is short exact, where `i` is the
> inclusion of the zero scheme of `s`.

```lean
theorem shortExact_zeroScheme_of_isRegularSection (s : L.sections)
    (hs : IsRegularSection X.sheaf.obj X.ringCatSheaf.property s) :
    let i := (zeroScheme X L (s.eval (op ⊤))).subschemeι
    let O : X.Modules := SheafOfModules.unit X.ringCatSheaf
    let f : O ⟶ L := L.unitHomEquiv.symm s
    let g : L ⟶ (Scheme.Modules.pushforward i).obj ((Scheme.Modules.pullback i).obj L) :=
      (Scheme.Modules.pullbackPushforwardAdjunction i).unit.app L
    ∃ h : f ≫ g = 0, (ShortComplex.mk f g h).ShortExact
```

**`Stacks.IdealSheafSequence.divisorIdeal_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/IdealSheafSequence/Basic.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/IdealSheafSequence/Basic.lean#L116). The attribute's comment: “divisor\_ideal\_sequence”. References: SGA 6 X (5.2.2), “more general”.

> **Stacks Tag 0C6K, the label `divisor_ideal_sequence`.** For a closed subscheme `D` of a
> scheme `X` with inclusion `i`, the canonical sequence `0 ⟶ ℐ_D ⟶ 𝒪_X ⟶ i_* 𝒪_D ⟶ 0` of sheaves
> of `𝒪_X`-modules is short exact.
>
> The effective-Cartier hypothesis of Tag 0C6K is not used: it is what makes `ℐ_D` the invertible
> module `𝒪_X(-D)`, and the exactness of the sequence does not depend on it.

```lean
theorem divisorIdeal_shortExact :
    ∃ hz : divisorIdealMap D ≫ divisorQuotientMap D = 0,
      (ShortComplex.mk (divisorIdealMap D) (divisorQuotientMap D) hz).ShortExact
```

**`Stacks.Tag0C6KSectionIdeal.exists_cokernelIso_zeroScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionIdeal/Basic.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SectionIdeal/Basic.lean#L204). The attribute's comment: “regular\_section\_sequence”.

> **The first assertion of Stacks Tag 0C6K's label `regular_section_sequence`.** For `L` an
> invertible `𝒪_X`-module and `s` a global section of `L`, the restriction map
> `L ⟶ i_* (L|_{Z(s)})` to the zero scheme of `s` *is* the cokernel of multiplication by `s`,
> compatibly with the cokernel projection. No regularity of `s` is used, as in the source.

```lean
theorem exists_cokernelIso_zeroScheme (L : SheafOfModules.{u} X.ringCatSheaf)
    [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L] (s : L.sections) :
    ∃ e : cokernel (L.unitHomEquiv.symm s) ≅
        (SheafOfModules.pushforward.{u} (Stacks.RegularSectionSequence.zeroScheme X L
            (s.eval (op ⊤))).subschemeι.toRingCatSheafHom).obj
          ((SheafOfModules.pullback.{u} (Stacks.RegularSectionSequence.zeroScheme X L
            (s.eval (op ⊤))).subschemeι.toRingCatSheafHom).obj L),
      cokernel.π (L.unitHomEquiv.symm s) ≫ e.hom =
        Stacks.RegularSectionSequence.restrictionUnit
          (Stacks.RegularSectionSequence.zeroScheme X L (s.eval (op ⊤))) L
```

**`Stacks.Tag0C6KSectionIdeal.shortExact_zeroScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionIdeal/Basic.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SectionIdeal/Basic.lean#L222). The attribute's comment: “regular\_section\_sequence”.

> **The second assertion of Stacks Tag 0C6K's label `regular_section_sequence`.** For `s` a
> *regular* global section of an invertible module — regularity being monicity of multiplication by
> `s`, which is Stacks Tag 01WY and is literally the hypothesis below — the sequence
> `0 ⟶ 𝒪_X ⟶ L ⟶ i_* (L|_{Z(s)}) ⟶ 0` is short exact.

```lean
theorem shortExact_zeroScheme (L : SheafOfModules.{u} X.ringCatSheaf)
    [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L] (s : L.sections)
    [Mono (L.unitHomEquiv.symm s)] :
    ∃ h : L.unitHomEquiv.symm s ≫ Stacks.RegularSectionSequence.restrictionUnit
        (Stacks.RegularSectionSequence.zeroScheme X L (s.eval (op ⊤))) L = 0,
      (ShortComplex.mk (L.unitHomEquiv.symm s)
        (Stacks.RegularSectionSequence.restrictionUnit
          (Stacks.RegularSectionSequence.zeroScheme X L (s.eval (op ⊤))) L) h).ShortExact
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.15, Tag 0C4S](https://stacks.math.columbia.edu/tag/0C4S)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
