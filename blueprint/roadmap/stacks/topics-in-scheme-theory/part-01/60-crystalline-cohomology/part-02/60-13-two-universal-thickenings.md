---
declaration: section
origin: cited
lean: Crystalline.GlobalCrystallineSituation.firstOrderThickeningHom, Crystalline.GlobalCrystallineSituation.firstOrderThickeningSchemeMap, Crystalline.GlobalCrystallineSituation.firstOrderThickeningMapApp_isDPMorphism, Crystalline.GlobalCrystallineSituation.firstOrderThickeningDPMap, Crystalline.GlobalCrystallineSituation.firstOrderThickeningSchemeMap_comp_projHom, Crystalline.GlobalCrystallineSituation.firstOrderThickeningSchemeMap_comp_P₁Hom, Crystalline.GlobalCrystallineSituation.firstOrderThickeningSiteMap, Crystalline.GlobalCrystallineSituation.firstOrderThickeningSiteMap_comp_P₀
statement: formalized
proof: formalized
---

# 60.13 Two universal thickenings

Section 60.13 of the Stacks Project, [Tag 07KN](https://stacks.math.columbia.edu/tag/07KN). 2 tags here are carried by 138 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07J2, a remark

[Tag 07J2](https://stacks.math.columbia.edu/tag/07J2) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystalConnectionNaturality.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/CrystalConnectionNaturality.lean#L82). The attribute's comment: “the functoriality datum of the first-order thickening, in the shape in which the naturality clause of 07J6 consumes it”.

> **The functoriality datum of the first-order universal thickening of [Stacks, Tag 07J2].**
> For a morphism `g : (U, T, δ) ⟶ (U₁, T₁, δ₁)` of `CRIS(X/S)`, the induced morphism
> `(U, T', δ') ⟶ (U₁, T₁', δ₁')` of the site together with its two commutation relations, which
> `StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningFunctorial.lean` constructs as
> `Crystalline.GlobalCrystallineSituation.firstOrderThickeningSiteMap`,
> `Crystalline.GlobalCrystallineSituation.firstOrderThickeningSiteMap_comp_P₀` and
> `Crystalline.GlobalCrystallineSituation.firstOrderThickeningSiteMap_comp_P₁`.
>
> This is the input [Stacks, Tag 07J6] uses to turn its family of connections into a morphism of
> abelian sheaves on the site.

```lean
def firstOrderThickeningHom {A B : Thickening S} (g : A ⟶ B) : FirstOrderThickeningHom g
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningSchemeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningFunctorial.lean, line 367](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningFunctorial.lean#L367). The attribute's comment: “the morphism T' ⟶ T₁' of schemes”.

> **The morphism of schemes `T_A' ⟶ T_B'` between the first-order universal thickenings.**

```lean
public def firstOrderThickeningSchemeMap (g : A ⟶ B) :
    firstOrderThickeningScheme A.thickening.target S.S.scheme A.toBase.hom ⟶
      firstOrderThickeningScheme B.thickening.target S.S.scheme B.toBase.hom
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningMapApp_isDPMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningFunctorial.lean, line 387](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningFunctorial.lean#L387). The attribute's comment: “the map T' ⟶ T₁' is compatible with the divided powers δ'”.

> **The map on sections of the first-order thickenings is a homomorphism of divided power
> rings.**  It carries `J'_B = J_B ⊕ Ω_B` into `J'_A = J_A ⊕ Ω_A` because the ambient morphism does
> so on the first summand, and it commutes with `δ'` because the ambient morphism commutes with
> `δ` and the map on differentials is semilinear.

```lean
public theorem firstOrderThickeningMapApp_isDPMorphism (g : A ⟶ B)
    (U : B.thickening.target.scheme.Opens) :
    DividedPowers.IsDPMorphism
      (firstOrderThickeningDividedPowers B.thickening.target S.S.scheme B.toBase.hom (op U))
      (firstOrderThickeningDividedPowers A.thickening.target S.S.scheme A.toBase.hom
        (op (ambientHom g ⁻¹ᵁ U)))
      (firstOrderThickeningMapApp g (op U)).hom
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningDPMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningFunctorial.lean, line 424](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningFunctorial.lean#L424). The attribute's comment: “the morphism T' ⟶ T₁' of divided power schemes”.

> **The morphism of divided power schemes `(T_A', J_A', δ_A') ⟶ (T_B', J_B', δ_B')`** between
> the first-order universal thickenings.

```lean
public def firstOrderThickeningDPMap (g : A ⟶ B) :
    firstOrderThickeningDPScheme S A ⟶ firstOrderThickeningDPScheme S B
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningSchemeMap_comp_projHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningFunctorial.lean, line 442](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningFunctorial.lean#L442). The attribute's comment: “the map T' ⟶ T₁' commutes with p₀, for schemes”.

> **The map of first-order thickenings commutes with the first projection**, both sides
> carrying `(b, ω)` to `gh^# b`.

```lean
public theorem firstOrderThickeningSchemeMap_comp_projHom (g : A ⟶ B) :
    firstOrderThickeningSchemeMap g ≫
        firstOrderThickeningProjHom B.thickening.target S.S.scheme B.toBase.hom =
      firstOrderThickeningProjHom A.thickening.target S.S.scheme A.toBase.hom ≫ ambientHom g
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningSchemeMap_comp_P₁Hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningFunctorial.lean, line 454](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningFunctorial.lean#L454). The attribute's comment: “the map T' ⟶ T₁' commutes with p₁, for schemes”.

> **The map of first-order thickenings commutes with the second projection.**  This is the
> computation `dg ∘ d_B = d_A ∘ gh^#`: one side carries `b` to `(gh^# b, dg (d_B b))` and the
> other to `(gh^# b, d_A (gh^# b))`.

```lean
public theorem firstOrderThickeningSchemeMap_comp_P₁Hom (g : A ⟶ B) :
    firstOrderThickeningSchemeMap g ≫
        firstOrderThickeningP₁Hom B.thickening.target S.S.scheme B.toBase.hom =
      firstOrderThickeningP₁Hom A.thickening.target S.S.scheme A.toBase.hom ≫ ambientHom g
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningSiteMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningFunctorial.lean, line 464](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningFunctorial.lean#L464). The attribute's comment: “the functoriality (U, T, δ) ↦ (U, T', δ') of the first-order thickening”.

> **The morphism of `CRIS(X/S)` between the first-order universal thickenings** induced by a
> morphism `g` of `CRIS(X/S)`: the functoriality datum of [Stacks, Tag 07J2].

```lean
public def firstOrderThickeningSiteMap (g : A ⟶ B) :
    firstOrderThickeningObject S A ⟶ firstOrderThickeningObject S B
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningSiteMap_comp_P₀`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningFunctorial.lean, line 488](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningFunctorial.lean#L488). The attribute's comment: “the functoriality datum commutes with p₀, in CRIS(X/S)”.

> **The functoriality datum commutes with the first projection**, the left relation of
> [Stacks, Tag 07J2].

```lean
public theorem firstOrderThickeningSiteMap_comp_P₀ (g : A ⟶ B) :
    firstOrderThickeningSiteMap g ≫ firstOrderThickeningSiteP₀ S B =
      firstOrderThickeningSiteP₀ S A ≫ g
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningSiteMap_comp_P₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningFunctorial.lean, line 497](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningFunctorial.lean#L497). The attribute's comment: “the functoriality datum commutes with p₁, in CRIS(X/S)”.

> **The functoriality datum commutes with the second projection**, the right relation of
> [Stacks, Tag 07J2].

```lean
public theorem firstOrderThickeningSiteMap_comp_P₁ (g : A ⟶ B) :
    firstOrderThickeningSiteMap g ≫ firstOrderThickeningSiteP₁ S B =
      firstOrderThickeningSiteP₁ S A ≫ g
```

**`Crystalline.firstOrderThickeningSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean#L117). The attribute's comment: “the structure sheaf of the first-order thickening”.

> **The structure sheaf of the first-order universal thickening** `T'` of a divided power
> scheme `T` over `Y`: the square-zero extension `𝒪_T ⊕ Ω_{T/Y,δ}` of the structure sheaf of `T`
> by its sheaf of divided power differentials.

```lean
public def firstOrderThickeningSheaf : TopCat.Sheaf CommRingCat.{u} ↑T.scheme
```

**`Crystalline.firstOrderThickeningIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean#L141). The attribute's comment: “the extended ideal J' = J ⊕ Ω”.

> **The ideal `J' = J ⊕ Ω_{T/Y,δ}`** of the sections of `𝒪_{T'}` over an open: the sections
> whose component in `𝒪_T` lies in the divided power ideal of `T`.

```lean
public def firstOrderThickeningIdeal (W : (Opens ↑T.scheme)ᵒᵖ) :
    Ideal ↑((firstOrderThickeningPresheaf T Y f).obj W)
```

**`Crystalline.firstOrderThickeningDividedPowers`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean#L171). The attribute's comment: “the divided power structure on J'”.

> **The divided power structure `δ'` on the ideal `J' = J ⊕ Ω_{T/Y,δ}`**, given in degree
> `k + 1` by `(g, ω) ↦ (δ_{k+1} g, δ_k g · ω)` and in degree zero by `1`.

```lean
public def firstOrderThickeningDividedPowers (W : (Opens ↑T.scheme)ᵒᵖ) :
    DividedPowers (firstOrderThickeningIdeal T Y f W)
```

**`Crystalline.firstOrderThickening_mul_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean#L200). The attribute's comment: “the differentials are an ideal of square zero”.

> **The sheaf of divided power differentials is an ideal of square zero in `𝒪_{T'}`.**

```lean
public theorem firstOrderThickening_mul_eq_zero (W : (Opens ↑T.scheme)ᵒᵖ)
    {x y : ↑((firstOrderThickeningPresheaf T Y f).obj W)}
    (hx : sqZeroExtFst x = 0) (hy : sqZeroExtFst y = 0) : x * y = 0
```

**`Crystalline.firstOrderThickening_restriction_isDPMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean#L225). The attribute's comment: “the divided powers on J' are compatible with restriction”.

> **Every restriction map of `𝒪_{T'}` is compatible with the divided powers of `J'`**, so the
> rings of sections of `𝒪_{T'}` with the ideals `J'` and the structures `δ'` form a presheaf of
> divided power rings.

```lean
public theorem firstOrderThickening_restriction_isDPMorphism
    {W W' : (Opens ↑T.scheme)ᵒᵖ} (i : W ⟶ W') :
    DividedPowers.IsDPMorphism (firstOrderThickeningDividedPowers T Y f W)
      (firstOrderThickeningDividedPowers T Y f W')
      (((firstOrderThickeningPresheaf T Y f).map i).hom)
```

**`Crystalline.firstOrderThickeningP₀`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean#L285). The attribute's comment: “the map p₀”.

> **The first of the two maps `𝒪_T → 𝒪_{T'}`**, the inclusion `g ↦ (g, 0)`.

```lean
public def firstOrderThickeningP₀ : T.scheme.sheaf.obj ⟶ firstOrderThickeningPresheaf T Y f
```

**`Crystalline.firstOrderThickeningP₁`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean#L291). The attribute's comment: “the map p₁”.

> **The second of the two maps `𝒪_T → 𝒪_{T'}`**, the inclusion shifted by the universal
> divided power derivation: `g ↦ (g, d_{T/Y,δ} g)`.

```lean
public def firstOrderThickeningP₁ : T.scheme.sheaf.obj ⟶ firstOrderThickeningPresheaf T Y f
```

**`Crystalline.firstOrderThickeningProj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean#L300). The attribute's comment: “the quotient map”.

> **The projection `𝒪_{T'} → 𝒪_T`**, forgetting the differential component.

```lean
public def firstOrderThickeningProj : firstOrderThickeningPresheaf T Y f ⟶ T.scheme.sheaf.obj
```

**`Crystalline.firstOrderThickeningP₀_isDPMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean, line 335](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean#L335). The attribute's comment: “p₀ is compatible with the divided powers”.

> **`p₀` is compatible with the divided power structures on `J` and `J'`.**

```lean
public theorem firstOrderThickeningP₀_isDPMorphism (W : (Opens ↑T.scheme)ᵒᵖ) :
    DividedPowers.IsDPMorphism (T.dividedPowers.dividedPowers W)
      (firstOrderThickeningDividedPowers T Y f W)
      (((firstOrderThickeningP₀ T Y f).app W).hom)
```

**`Crystalline.firstOrderThickeningP₁_isDPMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean, line 349](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean#L349). The attribute's comment: “p₁ is compatible with the divided powers”.

> **`p₁` is compatible with the divided power structures on `J` and `J'`**, because the
> universal divided power derivation obeys the divided power chain rule.

```lean
public theorem firstOrderThickeningP₁_isDPMorphism (W : (Opens ↑T.scheme)ᵒᵖ) :
    DividedPowers.IsDPMorphism (T.dividedPowers.dividedPowers W)
      (firstOrderThickeningDividedPowers T Y f W)
      (((firstOrderThickeningP₁ T Y f).app W).hom)
```

**`Crystalline.firstOrderThickeningProj_isDPMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean, line 364](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean#L364). The attribute's comment: “the quotient map is compatible with the divided powers”.

> **The projection `𝒪_{T'} → 𝒪_T` is compatible with the divided power structures on `J'`
> and `J`.**

```lean
public theorem firstOrderThickeningProj_isDPMorphism (W : (Opens ↑T.scheme)ᵒᵖ) :
    DividedPowers.IsDPMorphism (firstOrderThickeningDividedPowers T Y f W)
      (T.dividedPowers.dividedPowers W) (((firstOrderThickeningProj T Y f).app W).hom)
```

**`Crystalline.firstOrderThickeningP₁_sub_P₀`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean#L386). The attribute's comment: “p₁ - p₀ is the universal derivation”.

> **The difference of the two maps `𝒪_T → 𝒪_{T'}` is the universal divided power derivation**,
> followed by the inclusion of `Ω_{T/Y,δ}` as the square-zero summand.

```lean
public theorem firstOrderThickeningP₁_sub_P₀ (W : (Opens ↑T.scheme)ᵒᵖ)
    (a : ↑(T.scheme.sheaf.obj.obj W)) :
    ((firstOrderThickeningP₁ T Y f).app W).hom a - ((firstOrderThickeningP₀ T Y f).app W).hom a =
      sqZeroExtMk 0 (sheafApp T Y f W.unop a)
```

**`Crystalline.firstOrderThickeningKernelEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean, line 401](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean#L401). The attribute's comment: “the ideal of the thickening is the differentials”.

> **The ideal of the first-order thickening `T → T'` is the sheaf of divided power
> differentials**: the kernel of `𝒪_{T'} → 𝒪_T` over an open is canonically `Ω_{T/Y,δ}`.

```lean
public def firstOrderThickeningKernelEquiv (W : (Opens ↑T.scheme)ᵒᵖ) :
    ↑((dpDifferentialsModules T Y f).obj W) ≃+
      RingHom.ker (((firstOrderThickeningProj T Y f).app W).hom)
```

**`Crystalline.firstOrderThickening_ker_sq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean, line 421](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickenings.lean#L421). The attribute's comment: “T → T' is a first-order thickening”.

> **`T → T'` is a first-order thickening**: the ideal of the projection `𝒪_{T'} → 𝒪_T` has
> square zero on every open.

```lean
public theorem firstOrderThickening_ker_sq (W : (Opens ↑T.scheme)ᵒᵖ) :
    RingHom.ker (((firstOrderThickeningProj T Y f).app W).hom) ^ 2 = ⊥
```

**`Crystalline.firstOrderThickeningScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L213). The attribute's comment: “the first-order thickening T' as a scheme”.

> **The first-order universal thickening `T'` as a scheme.**  The topological space of `T`
> equipped with the structure sheaf `𝒪_{T'} = 𝒪_T ⊕ Ω_{T/Y,δ}`; it is a scheme because it is
> isomorphic, as a locally ringed space, to the realization of the square-zero extension.

```lean
public def firstOrderThickeningScheme : Scheme.{u}
```

**`Crystalline.firstOrderThickeningι`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L247). The attribute's comment: “the immersion i : T ⟶ T' of schemes”.

> **The immersion `i : T ⟶ T'`**, whose map on sections is the projection
> `𝒪_{T'} ⟶ 𝒪_T`.

```lean
public def firstOrderThickeningι : T.scheme ⟶ firstOrderThickeningScheme T Y f
```

**`Crystalline.firstOrderThickeningProjHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 310](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L310). The attribute's comment: “the morphism p₀ : T' ⟶ T of schemes”.

> **The morphism `p₀ : T' ⟶ T`**, induced by the inclusion `g ↦ (g, 0)` of structure
> sheaves.

```lean
public def firstOrderThickeningProjHom : firstOrderThickeningScheme T Y f ⟶ T.scheme
```

**`Crystalline.firstOrderThickeningP₁Hom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 318](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L318). The attribute's comment: “the morphism p₁ : T' ⟶ T of schemes”.

> **The morphism `p₁ : T' ⟶ T`**, induced by the derivation-shifted inclusion
> `g ↦ (g, d_{T/Y,δ} g)` of structure sheaves.

```lean
public def firstOrderThickeningP₁Hom : firstOrderThickeningScheme T Y f ⟶ T.scheme
```

**`Crystalline.firstOrderThickeningι_comp_projHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 347](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L347). The attribute's comment: “the diagram relation p₀ ∘ i = id, for schemes”.

> **`p₀` retracts the immersion `i`.**

```lean
public theorem firstOrderThickeningι_comp_projHom :
    firstOrderThickeningι T Y f ≫ firstOrderThickeningProjHom T Y f = 𝟙 T.scheme
```

**`Crystalline.firstOrderThickeningι_comp_P₁Hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L354). The attribute's comment: “the diagram relation p₁ ∘ i = id, for schemes”.

> **`p₁` retracts the immersion `i`.**

```lean
public theorem firstOrderThickeningι_comp_P₁Hom :
    firstOrderThickeningι T Y f ≫ firstOrderThickeningP₁Hom T Y f = 𝟙 T.scheme
```

**`Crystalline.firstOrderThickeningι_isFirstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 377](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L377). The attribute's comment: “i : T ⟶ T' is a first-order thickening of schemes”.

> **The immersion `T ⟶ T'` is a first-order thickening of schemes**: its ideal sheaf has
> square zero, because the kernel of `𝒪_{T'} ⟶ 𝒪_T` over every open is the square-zero summand
> `Ω_{T/Y,δ}`.

```lean
public theorem firstOrderThickeningι_isFirstOrderThickening :
    Stacks.Thickenings.IsFirstOrderThickening (firstOrderThickeningι T Y f)
```

**`Crystalline.firstOrderThickeningιKernelEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 394](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L394). The attribute's comment: “the ideal sheaf of i is the sheaf of divided power differentials”.

> **The ideal sheaf of `i : T ⟶ T'` is `Ω_{T/Y,δ}`**: over every open, the kernel of the map
> on sections of `i` is canonically the module of divided power differentials.

```lean
public def firstOrderThickeningιKernelEquiv
    (W : (Opens ↑(firstOrderThickeningScheme T Y f))ᵒᵖ) :
    ↑((dpDifferentialsModules T Y f).obj (firstOrderThickeningOpen T Y f W)) ≃+
      RingHom.ker (((firstOrderThickeningι T Y f).c.app W).hom)
```

**`Crystalline.firstOrderThickeningP₁Hom_comp_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 428](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L428). The attribute's comment: “p₀ and p₁ agree over the base”.

> **`p₀` and `p₁` are morphisms over the base `Y`, and they agree there**: their difference is
> the universal divided power derivation, which kills every section pulled back from `Y`.

```lean
public theorem firstOrderThickeningP₁Hom_comp_base :
    firstOrderThickeningP₁Hom T Y f ≫ f = firstOrderThickeningProjHom T Y f ≫ f
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningIdealSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 511](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L511). The attribute's comment: “the ideal J' as a sheaf of ideals on T'”.

> **The extended ideal `J' = J ⊕ Ω_{T/S,δ}` as a sheaf of ideals on `T'`.**

```lean
public def firstOrderThickeningIdealSheaf :
    (SheafOfModules.unit (firstOrderThickeningScheme A.thickening.target S.S.scheme
      A.toBase.hom).ringCatSheaf).Submodule
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningIdealSheaf_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 572](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L572). The attribute's comment: “the ideal J' is quasi-coherent”.

> **The extended ideal `J'` is quasi-coherent**, being the ideal sheaf of the closed immersion
> `U ⟶ T'`.

```lean
public theorem firstOrderThickeningIdealSheaf_isQuasicoherent :
    (firstOrderThickeningIdealSheaf S A).toSheafOfModules.IsQuasicoherent
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningDPScheme`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 584](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L584). The attribute's comment: “T' with the ideal J' and the divided powers δ' is a divided power scheme”.

> **The divided power scheme `(T', J', δ')`.**  The scheme `T'`, the quasi-coherent ideal
> `J' = J ⊕ Ω_{T/S,δ}` and the divided power structure `δ'` of [Stacks, Tag 07J2].

```lean
public abbrev firstOrderThickeningDPScheme : DividedPowerScheme.{u}
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningProjDP`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 598](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L598). The attribute's comment: “p₀ is a morphism of divided power schemes”.

> **`p₀ : T' ⟶ T` is a morphism of divided power schemes.**

```lean
public def firstOrderThickeningProjDP :
    firstOrderThickeningDPScheme S A ⟶ A.thickening.target
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningP₁DP`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 606](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L606). The attribute's comment: “p₁ is a morphism of divided power schemes”.

> **`p₁ : T' ⟶ T` is a morphism of divided power schemes.**

```lean
public def firstOrderThickeningP₁DP :
    firstOrderThickeningDPScheme S A ⟶ A.thickening.target
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningιDP`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 614](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L614). The attribute's comment: “i is a morphism of divided power schemes”.

> **`i : T ⟶ T'` is a morphism of divided power schemes.**

```lean
public def firstOrderThickeningιDP :
    A.thickening.target ⟶ firstOrderThickeningDPScheme S A
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningSchemeThickening`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 623](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L623). The attribute's comment: “U ⟶ T' is a divided power thickening”.

> **The divided power thickening `U ⟶ T'`**: a thickening of schemes whose defining ideal is
> the divided power ideal `J'`.

```lean
public abbrev firstOrderThickeningSchemeThickening : SchemeThickening.{u}
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningObject`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 641](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L641). The attribute's comment: “(U, T', δ') is an object of CRIS(X/S)”.

> **`(U, T', δ')` is an object of `CRIS(X/S)`.**  This is the assertion of [Stacks, Tag 07J2]
> that the first-order universal thickening of an object of the crystalline category is again an
> object of it: `T'` with the ideal `J' = J ⊕ Ω_{T/S,δ}` and the divided powers `δ'` is a divided
> power scheme, `U ⟶ T'` is a divided power thickening, and `T' ⟶ S` is `p₀` followed by the
> structure morphism of `T`.

```lean
public abbrev firstOrderThickeningObject : Thickening S
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningSiteι`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 659](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L659). The attribute's comment: “the morphism i of CRIS(X/S)”.

> **The morphism `i : (U, T, δ) ⟶ (U, T', δ')` of `CRIS(X/S)`.**

```lean
public def firstOrderThickeningSiteι : A ⟶ firstOrderThickeningObject S A
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningSiteP₀`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 677](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L677). The attribute's comment: “the morphism p₀ of CRIS(X/S)”.

> **The morphism `p₀ : (U, T', δ') ⟶ (U, T, δ)` of `CRIS(X/S)`.**

```lean
public def firstOrderThickeningSiteP₀ : firstOrderThickeningObject S A ⟶ A
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningSiteP₁`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 695](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L695). The attribute's comment: “the morphism p₁ of CRIS(X/S)”.

> **The morphism `p₁ : (U, T', δ') ⟶ (U, T, δ)` of `CRIS(X/S)`.**  It is a morphism over the
> divided power base because `p₁` and `p₀` agree after composing with the structure morphism of
> `T`, the universal divided power derivation killing every section pulled back from `S`.

```lean
public def firstOrderThickeningSiteP₁ : firstOrderThickeningObject S A ⟶ A
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningSiteι_comp_P₀`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 720](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L720). The attribute's comment: “the diagram relation p₀ ∘ i = id in CRIS(X/S)”.

> **`p₀ ∘ i = id` in `CRIS(X/S)`**, the left relation of the diagram of
> [Stacks, Tag 07J2].

```lean
public theorem firstOrderThickeningSiteι_comp_P₀ :
    firstOrderThickeningSiteι S A ≫ firstOrderThickeningSiteP₀ S A = 𝟙 A
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningSiteι_comp_P₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 730](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L730). The attribute's comment: “the diagram relation p₁ ∘ i = id in CRIS(X/S)”.

> **`p₁ ∘ i = id` in `CRIS(X/S)`**, the right relation of the diagram of
> [Stacks, Tag 07J2].

```lean
public theorem firstOrderThickeningSiteι_comp_P₁ :
    firstOrderThickeningSiteι S A ≫ firstOrderThickeningSiteP₁ S A = 𝟙 A
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningSiteι_isFirstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 741](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L741). The attribute's comment: “i is a first-order thickening with ideal sheaf Ω\_\{T/S,δ}”.

> **`i : (U, T, δ) ⟶ (U, T', δ')` is a first-order thickening whose ideal sheaf is
> `Ω_{T/S,δ}`**, which is the restriction `(Ω_{X/S})_T` of the crystalline differentials by
> [Stacks, Tag 07IZ].

```lean
public theorem firstOrderThickeningSiteι_isFirstOrderThickening :
    Stacks.Thickenings.IsFirstOrderThickening
      (firstOrderThickeningSiteι S A).targetHom.hom
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningSiteKernelEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 752](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L752). The attribute's comment: “the ideal sheaf of i is the restriction of Ω\_\{X/S} to T”.

> **The ideal sheaf of `i : T ⟶ T'` is `(Ω_{X/S})_T`**, the restriction of the crystalline
> differentials to the ambient scheme of the object — which is the spelling in which
> [Stacks, Tag 07J2] states it.  Over every open the kernel of the map on sections of `i` is the
> sheaf `Ω_{T/S,δ}` of divided power differentials, and [Stacks, Tag 07IZ] identifies that sheaf
> with `(Ω_{X/S})_T`.

```lean
public def firstOrderThickeningSiteKernelEquiv
    (W : (Opens ↑(firstOrderThickeningScheme A.thickening.target S.S.scheme
      A.toBase.hom))ᵒᵖ) :
    ↑((restrictedCrysDifferentialsSheaf S A).val.obj
        (firstOrderThickeningOpen A.thickening.target S.S.scheme A.toBase.hom W)) ≃+
      RingHom.ker (((firstOrderThickeningι A.thickening.target S.S.scheme
        A.toBase.hom).c.app W).hom)
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningCrysObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 773](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L773). The attribute's comment: “(U, T', δ') is an object of Cris(X/S)”.

> **`(U, T', δ')` is an object of the small crystalline category `Cris(X/S)`** whenever
> `(U, T, δ)` is.  The construction leaves the map `U ⟶ X` untouched, so it is still an open
> immersion; this is the assertion of [Stacks, Tag 07J2] in the category in which the remark
> states it.

```lean
public def firstOrderThickeningCrysObject : CrystallineThickening S
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningCrysι`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 778](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L778). The attribute's comment: “the morphism i of the diagram in Cris(X/S)”.

> **The morphism `i : (U, T, δ) ⟶ (U, T', δ')` of `Cris(X/S)`.**

```lean
public def firstOrderThickeningCrysι : B ⟶ firstOrderThickeningCrysObject S B
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningCrysP₀`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 783](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L783). The attribute's comment: “the morphism p₀ of the diagram in Cris(X/S)”.

> **The morphism `p₀ : (U, T', δ') ⟶ (U, T, δ)` of `Cris(X/S)`.**

```lean
public def firstOrderThickeningCrysP₀ : firstOrderThickeningCrysObject S B ⟶ B
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningCrysP₁`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 788](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L788). The attribute's comment: “the morphism p₁ of the diagram in Cris(X/S)”.

> **The morphism `p₁ : (U, T', δ') ⟶ (U, T, δ)` of `Cris(X/S)`.**

```lean
public def firstOrderThickeningCrysP₁ : firstOrderThickeningCrysObject S B ⟶ B
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningCrysι_comp_P₀`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 794](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L794). The attribute's comment: “the diagram relation p₀ ∘ i = id in Cris(X/S)”.

> **`p₀ ∘ i = id` in `Cris(X/S)`**, the left relation of the diagram of
> [Stacks, Tag 07J2].

```lean
public theorem firstOrderThickeningCrysι_comp_P₀ :
    firstOrderThickeningCrysι S B ≫ firstOrderThickeningCrysP₀ S B = 𝟙 B
```

**`Crystalline.GlobalCrystallineSituation.firstOrderThickeningCrysι_comp_P₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean, line 802](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/UniversalThickeningScheme.lean#L802). The attribute's comment: “the diagram relation p₁ ∘ i = id in Cris(X/S)”.

> **`p₁ ∘ i = id` in `Cris(X/S)`**, the right relation of the diagram of
> [Stacks, Tag 07J2].

```lean
public theorem firstOrderThickeningCrysι_comp_P₁ :
    firstOrderThickeningCrysι S B ≫ firstOrderThickeningCrysP₁ S B = 𝟙 B
```

## Tag 07J3, a remark

[Tag 07J3](https://stacks.math.columbia.edu/tag/07J3) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningSiteData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystalConnectionSecondOrder.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/CrystalConnectionSecondOrder.lean#L84). The attribute's comment: “the second-order thickening as an object of CRIS(X/S) together with q₁₂ and the two relations q₁ = q₁₂ ∘ p₀, q₂ = q₁₂ ∘ p₁, in the shape in which the integrability argument of 07J6 consumes them”.

> **The second-order universal thickening of [Stacks, Tag 07J3] as an object of `CRIS(X/S)`,
> with the morphism `q₁₂` and the two relations the integrability argument consumes.**  Every field
> is a declaration of
> `StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean`: the object is
> `Crystalline.GlobalCrystallineSituation.secondOrderThickeningObject`, the morphisms are
> `Crystalline.GlobalCrystallineSituation.secondOrderThickeningSiteQ₁₂`,
> `Crystalline.GlobalCrystallineSituation.secondOrderThickeningSiteQ₁` and
> `Crystalline.GlobalCrystallineSituation.secondOrderThickeningSiteQ₂`, and the two relations are
> `Crystalline.GlobalCrystallineSituation.secondOrderThickeningSiteQ₁₂_comp_P₀` and
> `Crystalline.GlobalCrystallineSituation.secondOrderThickeningSiteQ₁₂_comp_P₁`.

```lean
def secondOrderThickeningSiteData (A : Thickening S) : SecondOrderThickeningSiteData A
```

**`Crystalline.secondOrderThickeningPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1230). The attribute's comment: “the structure sheaf of the second-order thickening”.

> **The structure sheaf of the second-order universal thickening** `T''` of a divided power
> scheme `T` over `Y`: the presheaf of commutative rings
> `𝒪_T ⊕ Ω_{T/Y,δ} ⊕ Ω_{T/Y,δ} ⊕ Ω²_{T/Y,δ}` whose multiplication is corrected in the last
> coordinate by the exterior product of the two middle coordinates.  All four summands are
> sheaves.

```lean
public def secondOrderThickeningPresheaf : (Opens ↑T.scheme)ᵒᵖ ⥤ CommRingCat.{u}
```

**`Crystalline.secondOrderThickeningSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1237). The attribute's comment: “the structure sheaf of the second-order thickening is a sheaf”.

> **The structure sheaf of the second-order universal thickening**, as a sheaf: all four
> summands `𝒪_T`, `Ω_{T/Y,δ}`, `Ω_{T/Y,δ}` and `Ω²_{T/Y,δ}` are sheaves, so the second-order
> extension satisfies the sheaf condition.

```lean
public def secondOrderThickeningSheaf : TopCat.Sheaf CommRingCat.{u} ↑T.scheme
```

**`Crystalline.secondOrderThickening_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1251). The attribute's comment: “the multiplication of the second-order thickening”.

> **The multiplication of `𝒪_{T''}` in coordinates.**

```lean
public theorem secondOrderThickening_mul (W : (Opens ↑T.scheme)ᵒᵖ)
    (x y : SecondOrderExt (dpWedge T Y f) W) :
    (secondOrderExtFst (x * y) = secondOrderExtFst x * secondOrderExtFst y ∧
      secondOrderExtLeft (x * y) =
        secondOrderExtFst x • secondOrderExtLeft y +
          secondOrderExtFst y • secondOrderExtLeft x) ∧
    secondOrderExtRight (x * y) =
        secondOrderExtFst x • secondOrderExtRight y +
          secondOrderExtFst y • secondOrderExtRight x ∧
      secondOrderExtTop (x * y) =
        secondOrderExtFst x • secondOrderExtTop y + secondOrderExtFst y • secondOrderExtTop x +
          (dpWedge T Y f).app W (secondOrderExtLeft x) (secondOrderExtRight y) +
          (dpWedge T Y f).app W (secondOrderExtLeft y) (secondOrderExtRight x)
```

**`Crystalline.secondOrderThickeningIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1269). The attribute's comment: “the ideal J'' of the second-order thickening”.

> **The ideal `J''` of the second-order universal thickening**: the inverse image of the
> divided power ideal of `T` under the projection `𝒪_{T''} → 𝒪_T`.

```lean
public def secondOrderThickeningIdeal (W : (Opens ↑T.scheme)ᵒᵖ) :
    Ideal (SecondOrderExt (dpWedge T Y f) W)
```

**`Crystalline.secondOrderThickeningDividedPowers`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1276). The attribute's comment: “the divided power structure on J''”.

> **The divided power structure `δ''` on the ideal `J''`** of the second-order universal
> thickening.

```lean
public def secondOrderThickeningDividedPowers (W : (Opens ↑T.scheme)ᵒᵖ) :
    DividedPowers (secondOrderThickeningIdeal T Y f W)
```

**`Crystalline.secondOrderThickeningDividedPowers_dpow_add_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1284). The attribute's comment: “the divided power formula on J''”.

> **The displayed formula for `δ''`**:
> `δ''\_\{k+2}(f, ω₁, ω₂, η) = (δ\_\{k+2} f, δ\_\{k+1} f · ω₁, δ\_\{k+1} f · ω₂,
> δ\_\{k+1} f · η + δ\_k f · ω₁ ∧ ω₂)`.

```lean
public theorem secondOrderThickeningDividedPowers_dpow_add_two (W : (Opens ↑T.scheme)ᵒᵖ) (k : ℕ)
    {x : SecondOrderExt (dpWedge T Y f) W} (hx : x ∈ secondOrderThickeningIdeal T Y f W) :
    (secondOrderThickeningDividedPowers T Y f W).dpow (k + 2) x =
      secondOrderExtMk
        ((T.dividedPowers.dividedPowers W).dpow (k + 2) (secondOrderExtFst x))
        ((T.dividedPowers.dividedPowers W).dpow (k + 1) (secondOrderExtFst x) •
          secondOrderExtLeft x)
        ((T.dividedPowers.dividedPowers W).dpow (k + 1) (secondOrderExtFst x) •
          secondOrderExtRight x)
        ((T.dividedPowers.dividedPowers W).dpow (k + 1) (secondOrderExtFst x) •
            secondOrderExtTop x +
          (T.dividedPowers.dividedPowers W).dpow k (secondOrderExtFst x) •
            (dpWedge T Y f).app W (secondOrderExtLeft x) (secondOrderExtRight x))
```

**`Crystalline.secondOrderThickening_restriction_isDPMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1303). The attribute's comment: “the divided powers on J'' are compatible with restriction”.

> **Every restriction map of `𝒪_{T''}` is compatible with the divided powers of `J''`**, so the
> rings of sections of `𝒪_{T''}` with the ideals `J''` and the structures `δ''` form a presheaf of
> divided power rings.

```lean
public theorem secondOrderThickening_restriction_isDPMorphism
    {W W' : (Opens ↑T.scheme)ᵒᵖ} (i : W ⟶ W') :
    DividedPowers.IsDPMorphism (secondOrderThickeningDividedPowers T Y f W)
      (secondOrderThickeningDividedPowers T Y f W')
      (secondOrderExtRingHom (dpWedge T Y f) i)
```

**`Crystalline.secondOrderThickeningQ₀`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1340](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1340). The attribute's comment: “the map q₀”.

> **The first of the three maps `𝒪_T → 𝒪_{T''}`**, `f ↦ (f, 0, 0, 0)`.

```lean
public def secondOrderThickeningQ₀ :
    T.scheme.sheaf.obj ⟶ secondOrderThickeningPresheaf T Y f
```

**`Crystalline.secondOrderThickeningQ₁`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1348). The attribute's comment: “the map q₁”.

> **The second of the three maps `𝒪_T → 𝒪_{T''}`**, `f ↦ (f, d f, 0, 0)`.

```lean
public def secondOrderThickeningQ₁ :
    T.scheme.sheaf.obj ⟶ secondOrderThickeningPresheaf T Y f
```

**`Crystalline.secondOrderThickeningQ₂`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1359](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1359). The attribute's comment: “the map q₂”.

> **The third of the three maps `𝒪_T → 𝒪_{T''}`**, `f ↦ (f, d f, d f, 0)`.  It is
> multiplicative because the exterior product is antisymmetric.

```lean
public def secondOrderThickeningQ₂ :
    T.scheme.sheaf.obj ⟶ secondOrderThickeningPresheaf T Y f
```

**`Crystalline.secondOrderThickeningQ₀₁`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1384](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1384). The attribute's comment: “the map q₀₁”.

> **The map `q₀₁ : 𝒪_{T'} → 𝒪_{T''}`**, `(f, ω) ↦ (f, ω, 0, 0)`.

```lean
public def secondOrderThickeningQ₀₁ :
    firstOrderThickeningPresheaf T Y f ⟶ secondOrderThickeningPresheaf T Y f
```

**`Crystalline.secondOrderThickeningQ₀₂`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1394](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1394). The attribute's comment: “the map q₀₂”.

> **The map `q₀₂ : 𝒪_{T'} → 𝒪_{T''}`**, `(f, ω) ↦ (f, ω, ω, 0)`.  It is multiplicative
> because the exterior product is antisymmetric.

```lean
public def secondOrderThickeningQ₀₂ :
    firstOrderThickeningPresheaf T Y f ⟶ secondOrderThickeningPresheaf T Y f
```

**`Crystalline.secondOrderThickeningQ₀_isDPMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1406](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1406). The attribute's comment: “q₀ is compatible with the divided powers”.

> **`q₀` is compatible with the divided power structures on `J` and `J''`.**

```lean
public theorem secondOrderThickeningQ₀_isDPMorphism (W : (Opens ↑T.scheme)ᵒᵖ) :
    DividedPowers.IsDPMorphism (T.dividedPowers.dividedPowers W)
      (secondOrderThickeningDividedPowers T Y f W)
      (((secondOrderThickeningQ₀ T Y f).app W).hom)
```

**`Crystalline.secondOrderThickeningQ₁_isDPMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1420](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1420). The attribute's comment: “q₁ is compatible with the divided powers”.

> **`q₁` is compatible with the divided power structures on `J` and `J''`**, because the
> universal divided power derivation obeys the divided power chain rule and the exterior product of
> a differential with zero vanishes.

```lean
public theorem secondOrderThickeningQ₁_isDPMorphism (W : (Opens ↑T.scheme)ᵒᵖ) :
    DividedPowers.IsDPMorphism (T.dividedPowers.dividedPowers W)
      (secondOrderThickeningDividedPowers T Y f W)
      (((secondOrderThickeningQ₁ T Y f).app W).hom)
```

**`Crystalline.secondOrderThickeningQ₂_isDPMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1434](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1434). The attribute's comment: “q₂ is compatible with the divided powers”.

> **`q₂` is compatible with the divided power structures on `J` and `J''`**, because the
> universal divided power derivation obeys the divided power chain rule and the exterior product of
> a differential with itself vanishes.

```lean
public theorem secondOrderThickeningQ₂_isDPMorphism (W : (Opens ↑T.scheme)ᵒᵖ) :
    DividedPowers.IsDPMorphism (T.dividedPowers.dividedPowers W)
      (secondOrderThickeningDividedPowers T Y f W)
      (((secondOrderThickeningQ₂ T Y f).app W).hom)
```

**`Crystalline.secondOrderThickeningQ₀₁_isDPMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1447](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1447). The attribute's comment: “q₀₁ is compatible with the divided powers”.

> **`q₀₁` is compatible with the divided power structures on `J'` and `J''`.**

```lean
public theorem secondOrderThickeningQ₀₁_isDPMorphism (W : (Opens ↑T.scheme)ᵒᵖ) :
    DividedPowers.IsDPMorphism (firstOrderThickeningDividedPowers T Y f W)
      (secondOrderThickeningDividedPowers T Y f W)
      (((secondOrderThickeningQ₀₁ T Y f).app W).hom)
```

**`Crystalline.secondOrderThickeningQ₀₂_isDPMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1461](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1461). The attribute's comment: “q₀₂ is compatible with the divided powers”.

> **`q₀₂` is compatible with the divided power structures on `J'` and `J''`**, because the
> exterior product of a differential with itself vanishes.

```lean
public theorem secondOrderThickeningQ₀₂_isDPMorphism (W : (Opens ↑T.scheme)ᵒᵖ) :
    DividedPowers.IsDPMorphism (firstOrderThickeningDividedPowers T Y f W)
      (secondOrderThickeningDividedPowers T Y f W)
      (((secondOrderThickeningQ₀₂ T Y f).app W).hom)
```

**`Crystalline.secondOrderThickeningQ₀_eq_Q₀₁_comp_P₀`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1478](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1478). The attribute's comment: “q₀ = q₀₁ ∘ p₀”.

> **`q₀ = q₀₁ ∘ p₀`.**

```lean
public theorem secondOrderThickeningQ₀_eq_Q₀₁_comp_P₀ :
    firstOrderThickeningP₀ T Y f ≫ secondOrderThickeningQ₀₁ T Y f =
      secondOrderThickeningQ₀ T Y f
```

**`Crystalline.secondOrderThickeningQ₁_eq_Q₀₁_comp_P₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1485](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1485). The attribute's comment: “q₁ = q₀₁ ∘ p₁”.

> **`q₁ = q₀₁ ∘ p₁`.**

```lean
public theorem secondOrderThickeningQ₁_eq_Q₀₁_comp_P₁ :
    firstOrderThickeningP₁ T Y f ≫ secondOrderThickeningQ₀₁ T Y f =
      secondOrderThickeningQ₁ T Y f
```

**`Crystalline.secondOrderThickeningQ₀_eq_Q₀₂_comp_P₀`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1492](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1492). The attribute's comment: “q₀ = q₀₂ ∘ p₀”.

> **`q₀ = q₀₂ ∘ p₀`.**

```lean
public theorem secondOrderThickeningQ₀_eq_Q₀₂_comp_P₀ :
    firstOrderThickeningP₀ T Y f ≫ secondOrderThickeningQ₀₂ T Y f =
      secondOrderThickeningQ₀ T Y f
```

**`Crystalline.secondOrderThickeningQ₂_eq_Q₀₂_comp_P₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean, line 1499](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickening.lean#L1499). The attribute's comment: “q₂ = q₀₂ ∘ p₁”.

> **`q₂ = q₀₂ ∘ p₁`.**

```lean
public theorem secondOrderThickeningQ₂_eq_Q₀₂_comp_P₁ :
    firstOrderThickeningP₁ T Y f ≫ secondOrderThickeningQ₀₂ T Y f =
      secondOrderThickeningQ₂ T Y f
```

**`Crystalline.secondOrderThickeningQ₁₂`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningDeRham.lean, line 595](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningDeRham.lean#L595). The attribute's comment: “the map q₁₂”.

> **The map `q₁₂ : 𝒪_{T'} → 𝒪_{T''}`**, `(f, ω) ↦ (f, d f, ω, d ω)`.  It is multiplicative
> because the de Rham differential obeys the Leibniz rule
> `d (f η + g ω) = f (d η) + g (d ω) + (d f) ∧ η + (d g) ∧ ω`, which is exactly the correction term
> of the second-order multiplication.

```lean
public def secondOrderThickeningQ₁₂ :
    firstOrderThickeningPresheaf T Y f ⟶ secondOrderThickeningPresheaf T Y f
```

**`Crystalline.secondOrderThickeningQ₁₂_isDPMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningDeRham.lean, line 649](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningDeRham.lean#L649). The attribute's comment: “q₁₂ is compatible with the divided powers”.

> **`q₁₂` is compatible with the divided power structures on `J'` and `J''`**, because the
> universal divided power derivation obeys the divided power chain rule and the de Rham
> differential obeys its divided power Leibniz rule
> `d (δ_{k+1}(f) ω) = δ_{k+1}(f) (d ω) + δ_k(f) ((d f) ∧ ω)`.

```lean
public theorem secondOrderThickeningQ₁₂_isDPMorphism (W : (Opens ↑T.scheme)ᵒᵖ) :
    DividedPowers.IsDPMorphism (firstOrderThickeningDividedPowers T Y f W)
      (secondOrderThickeningDividedPowers T Y f W)
      (((secondOrderThickeningQ₁₂ T Y f).app W).hom)
```

**`Crystalline.secondOrderThickeningQ₁_eq_Q₁₂_comp_P₀`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningDeRham.lean, line 676](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningDeRham.lean#L676). The attribute's comment: “q₁ = q₁₂ ∘ p₀”.

> **`q₁ = q₁₂ ∘ p₀`**, the two-form coordinate because the de Rham differential of the zero
> differential vanishes.

```lean
public theorem secondOrderThickeningQ₁_eq_Q₁₂_comp_P₀ :
    firstOrderThickeningP₀ T Y f ≫ secondOrderThickeningQ₁₂ T Y f =
      secondOrderThickeningQ₁ T Y f
```

**`Crystalline.secondOrderThickeningQ₂_eq_Q₁₂_comp_P₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningDeRham.lean, line 685](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningDeRham.lean#L685). The attribute's comment: “q₂ = q₁₂ ∘ p₁”.

> **`q₂ = q₁₂ ∘ p₁`**, the two-form coordinate because the de Rham differential kills every
> exact differential.

```lean
public theorem secondOrderThickeningQ₂_eq_Q₁₂_comp_P₁ :
    firstOrderThickeningP₁ T Y f ≫ secondOrderThickeningQ₁₂ T Y f =
      secondOrderThickeningQ₂ T Y f
```

**`Crystalline.secondOrderThickening_ker_cube`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningOrder.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningOrder.lean#L301). The attribute's comment: “T → T'' is a second-order thickening of sheaves of rings”.

> **`T → T''` is a second-order thickening**: the ideal of the projection `𝒪_{T''} → 𝒪_T` has
> vanishing cube on every open.  Its square lies in the top summand, and the top summand
> annihilates it.

```lean
public theorem secondOrderThickening_ker_cube (W : (Opens ↑T.scheme)ᵒᵖ) :
    RingHom.ker (secondOrderExtFstHom (dpWedge T Y f) W) ^ 3 = ⊥
```

**`Crystalline.secondOrderThickeningScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L256). The attribute's comment: “the second-order thickening T'' as a scheme”.

> **The second-order universal thickening `T''` as a scheme.**  The topological space of `T`
> equipped with the structure sheaf
> `𝒪_{T''} = 𝒪_T ⊕ Ω_{T/Y,δ} ⊕ Ω_{T/Y,δ} ⊕ Ω²_{T/Y,δ}`; it is a scheme because it is isomorphic,
> as a locally ringed space, to the realization of the square-zero extension of `𝒪_{T'}` by
> `K`.

```lean
public def secondOrderThickeningScheme : Scheme.{u}
```

**`Crystalline.secondOrderThickeningι`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L291). The attribute's comment: “the immersion T' ⟶ T'' of schemes”.

> **The immersion `j : T' ⟶ T''`**, whose map on sections is the projection
> `𝒪_{T''} ⟶ 𝒪_{T'}`.

```lean
public def secondOrderThickeningι :
    firstOrderThickeningScheme T Y f ⟶ secondOrderThickeningScheme T Y f
```

**`Crystalline.secondOrderThickeningιT`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L306). The attribute's comment: “the immersion T ⟶ T'' of schemes”.

> **The immersion `T ⟶ T''`**: the immersion `T ⟶ T'` followed by `T' ⟶ T''`.  Its map on
> sections is `Crystalline.secondOrderThickeningFstProj`, the projection `𝒪_{T''} ⟶ 𝒪_T`.

```lean
public def secondOrderThickeningιT : T.scheme ⟶ secondOrderThickeningScheme T Y f
```

**`Crystalline.secondOrderThickeningQ₀₁Hom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 367](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L367). The attribute's comment: “the morphism q₀₁ : T'' ⟶ T' of schemes”.

> **The morphism `q₀₁ : T'' ⟶ T'`**, induced by the map `(g, ω) ↦ (g, ω, 0, 0)` of structure
> sheaves.

```lean
public def secondOrderThickeningQ₀₁Hom :
    secondOrderThickeningScheme T Y f ⟶ firstOrderThickeningScheme T Y f
```

**`Crystalline.secondOrderThickeningQ₀₂Hom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L381). The attribute's comment: “the morphism q₀₂ : T'' ⟶ T' of schemes”.

> **The morphism `q₀₂ : T'' ⟶ T'`**, induced by the map `(g, ω) ↦ (g, ω, ω, 0)` of structure
> sheaves.

```lean
public def secondOrderThickeningQ₀₂Hom :
    secondOrderThickeningScheme T Y f ⟶ firstOrderThickeningScheme T Y f
```

**`Crystalline.secondOrderThickeningQ₁₂Hom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 395](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L395). The attribute's comment: “the morphism q₁₂ : T'' ⟶ T' of schemes”.

> **The morphism `q₁₂ : T'' ⟶ T'`**, induced by the map
> `(g, ω) ↦ (g, d g, ω, d ω)` of structure sheaves.

```lean
public def secondOrderThickeningQ₁₂Hom :
    secondOrderThickeningScheme T Y f ⟶ firstOrderThickeningScheme T Y f
```

**`Crystalline.secondOrderThickeningQ₀Hom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 410](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L410). The attribute's comment: “the morphism q₀ : T'' ⟶ T of schemes”.

> **The morphism `q₀ : T'' ⟶ T`**, the composite of `q₀₁` with `p₀`; on sections this is the
> relation `q₀ = q₀₁ ∘ p₀` of [Stacks, Tag 07J3].

```lean
public def secondOrderThickeningQ₀Hom : secondOrderThickeningScheme T Y f ⟶ T.scheme
```

**`Crystalline.secondOrderThickeningQ₁Hom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 416](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L416). The attribute's comment: “the morphism q₁ : T'' ⟶ T of schemes”.

> **The morphism `q₁ : T'' ⟶ T`**, the composite of `q₀₁` with `p₁`; on sections this is the
> relation `q₁ = q₀₁ ∘ p₁`.

```lean
public def secondOrderThickeningQ₁Hom : secondOrderThickeningScheme T Y f ⟶ T.scheme
```

**`Crystalline.secondOrderThickeningQ₂Hom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 422](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L422). The attribute's comment: “the morphism q₂ : T'' ⟶ T of schemes”.

> **The morphism `q₂ : T'' ⟶ T`**, the composite of `q₁₂` with `p₁`; on sections this is the
> relation `q₂ = q₁₂ ∘ p₁`.

```lean
public def secondOrderThickeningQ₂Hom : secondOrderThickeningScheme T Y f ⟶ T.scheme
```

**`Crystalline.secondOrderThickeningQ₀Hom_eq_Q₀₁_comp_P₀`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 496](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L496). The attribute's comment: “the relation q₀ = q₀₁ ∘ p₀, for schemes”.

> **`q₀ = q₀₁ ∘ p₀` for schemes**, the first relation of [Stacks, Tag 07J3]; it holds by the
> definition of `q₀`.

```lean
public theorem secondOrderThickeningQ₀Hom_eq_Q₀₁_comp_P₀ :
    secondOrderThickeningQ₀₁Hom T Y f ≫ firstOrderThickeningProjHom T Y f =
      secondOrderThickeningQ₀Hom T Y f
```

**`Crystalline.secondOrderThickeningQ₁Hom_eq_Q₀₁_comp_P₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 502](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L502). The attribute's comment: “the relation q₁ = q₀₁ ∘ p₁, for schemes”.

> **`q₁ = q₀₁ ∘ p₁` for schemes**; it holds by the definition of `q₁`.

```lean
public theorem secondOrderThickeningQ₁Hom_eq_Q₀₁_comp_P₁ :
    secondOrderThickeningQ₀₁Hom T Y f ≫ firstOrderThickeningP₁Hom T Y f =
      secondOrderThickeningQ₁Hom T Y f
```

**`Crystalline.secondOrderThickeningQ₂Hom_eq_Q₁₂_comp_P₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 508](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L508). The attribute's comment: “the relation q₂ = q₁₂ ∘ p₁, for schemes”.

> **`q₂ = q₁₂ ∘ p₁` for schemes**; it holds by the definition of `q₂`.

```lean
public theorem secondOrderThickeningQ₂Hom_eq_Q₁₂_comp_P₁ :
    secondOrderThickeningQ₁₂Hom T Y f ≫ firstOrderThickeningP₁Hom T Y f =
      secondOrderThickeningQ₂Hom T Y f
```

**`Crystalline.secondOrderThickeningQ₁Hom_eq_Q₁₂_comp_P₀`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 515](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L515). The attribute's comment: “the relation q₁ = q₁₂ ∘ p₀, for schemes”.

> **`q₁ = q₁₂ ∘ p₀` for schemes**, which on sections is
> `Crystalline.secondOrderThickeningQ₁_eq_Q₁₂_comp_P₀`.

```lean
public theorem secondOrderThickeningQ₁Hom_eq_Q₁₂_comp_P₀ :
    secondOrderThickeningQ₁₂Hom T Y f ≫ firstOrderThickeningProjHom T Y f =
      secondOrderThickeningQ₁Hom T Y f
```

**`Crystalline.secondOrderThickeningQ₀Hom_eq_Q₀₂_comp_P₀`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 527](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L527). The attribute's comment: “the relation q₀ = q₀₂ ∘ p₀, for schemes”.

> **`q₀ = q₀₂ ∘ p₀` for schemes**, which on sections is
> `Crystalline.secondOrderThickeningQ₀_eq_Q₀₂_comp_P₀`.

```lean
public theorem secondOrderThickeningQ₀Hom_eq_Q₀₂_comp_P₀ :
    secondOrderThickeningQ₀₂Hom T Y f ≫ firstOrderThickeningProjHom T Y f =
      secondOrderThickeningQ₀Hom T Y f
```

**`Crystalline.secondOrderThickeningQ₂Hom_eq_Q₀₂_comp_P₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 539](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L539). The attribute's comment: “the relation q₂ = q₀₂ ∘ p₁, for schemes”.

> **`q₂ = q₀₂ ∘ p₁` for schemes**, which on sections is
> `Crystalline.secondOrderThickeningQ₂_eq_Q₀₂_comp_P₁`.

```lean
public theorem secondOrderThickeningQ₂Hom_eq_Q₀₂_comp_P₁ :
    secondOrderThickeningQ₀₂Hom T Y f ≫ firstOrderThickeningP₁Hom T Y f =
      secondOrderThickeningQ₂Hom T Y f
```

**`Crystalline.secondOrderThickeningι_isFirstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 570](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L570). The attribute's comment: “T' ⟶ T'' is a first-order thickening of schemes”.

> **`T' ⟶ T''` is a first-order thickening of schemes**: its ideal sheaf has square zero,
> because the kernel of `𝒪_{T''} ⟶ 𝒪_{T'}` over every open is the square-zero ideal
> `K = 0 ⊕ 0 ⊕ Ω_{T/Y,δ} ⊕ Ω²_{T/Y,δ}`.

```lean
public theorem secondOrderThickeningι_isFirstOrderThickening :
    Stacks.Thickenings.IsFirstOrderThickening (secondOrderThickeningι T Y f)
```

**`Crystalline.secondOrderThickeningιT_isNthOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 596](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L596). The attribute's comment: “T → T'' is a second-order thickening of schemes”.

> **`T → T''` is a second-order thickening of schemes**, which is the description of `T''` in
> [Stacks, Tag 07J3].  The ideal sheaf of `T ⟶ T''` is the kernel of `𝒪_{T''} ⟶ 𝒪_T`, whose cube
> vanishes on every open by `Crystalline.secondOrderThickening_ker_cube`.
>
> The order is *not* obtained by composing the two first-order thickenings `T ⟶ T'` and
> `T' ⟶ T''`: a composite of two first-order thickenings is in general only of order three — for
> `Z = Spec k[x]/(x⁴)`, the closed subschemes cut out by `(x²)` and by `(x)` give first-order
> thickenings whose composite has `(x)³ ≠ 0` — and what makes the order here two is the explicit
> vanishing of the cube in the sheaf-level computation.

```lean
public theorem secondOrderThickeningιT_isNthOrderThickening :
    Stacks.Thickenings.IsNthOrderThickening 2 (secondOrderThickeningιT T Y f)
```

**`Crystalline.secondOrderThickeningιT_comp_Q₀Hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 688](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L688). The attribute's comment: “the relation q₀ ∘ (T ⟶ T'') = id”.

> **`q₀` retracts the immersion `T ⟶ T''`.**

```lean
public theorem secondOrderThickeningιT_comp_Q₀Hom :
    secondOrderThickeningιT T Y f ≫ secondOrderThickeningQ₀Hom T Y f = 𝟙 T.scheme
```

**`Crystalline.secondOrderThickeningιT_comp_Q₁Hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 697](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L697). The attribute's comment: “the relation q₁ ∘ (T ⟶ T'') = id”.

> **`q₁` retracts the immersion `T ⟶ T''`.**

```lean
public theorem secondOrderThickeningιT_comp_Q₁Hom :
    secondOrderThickeningιT T Y f ≫ secondOrderThickeningQ₁Hom T Y f = 𝟙 T.scheme
```

**`Crystalline.secondOrderThickeningιT_comp_Q₂Hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 706](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L706). The attribute's comment: “the relation q₂ ∘ (T ⟶ T'') = id”.

> **`q₂` retracts the immersion `T ⟶ T''`.**

```lean
public theorem secondOrderThickeningιT_comp_Q₂Hom :
    secondOrderThickeningιT T Y f ≫ secondOrderThickeningQ₂Hom T Y f = 𝟙 T.scheme
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningIdealSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 739](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L739). The attribute's comment: “the ideal J'' as a sheaf of ideals on T''”.

> **The extended ideal `J''` as a sheaf of ideals on `T''`**: the sections of `𝒪_{T''}` whose
> component in `𝒪_T` lies in the divided power ideal `J` of `T`.

```lean
public def secondOrderThickeningIdealSheaf :
    (SheafOfModules.unit (secondOrderThickeningScheme A.thickening.target S.S.scheme
      A.toBase.hom).ringCatSheaf).Submodule
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningIdealSheaf_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 799](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L799). The attribute's comment: “the ideal J'' is quasi-coherent”.

> **The extended ideal `J''` is quasi-coherent**, being the ideal sheaf of the closed immersion
> `U ⟶ T''`.

```lean
public theorem secondOrderThickeningIdealSheaf_isQuasicoherent :
    (secondOrderThickeningIdealSheaf S A).toSheafOfModules.IsQuasicoherent
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningDPScheme`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 809](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L809). The attribute's comment: “T'' with the ideal J'' and the divided powers δ'' is a divided power scheme”.

> **The divided power scheme `(T'', J'', δ'')`.**  The scheme `T''`, the quasi-coherent ideal
> `J''` and the divided power structure `δ''` of [Stacks, Tag 07J3].

```lean
public abbrev secondOrderThickeningDPScheme : DividedPowerScheme.{u}
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningQ₀DP`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 825](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L825). The attribute's comment: “q₀ is a morphism of divided power schemes”.

> **`q₀ : T'' ⟶ T` is a morphism of divided power schemes.**

```lean
public def secondOrderThickeningQ₀DP :
    secondOrderThickeningDPScheme S A ⟶ A.thickening.target
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningQ₁DP`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 833](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L833). The attribute's comment: “q₁ is a morphism of divided power schemes”.

> **`q₁ : T'' ⟶ T` is a morphism of divided power schemes.**

```lean
public def secondOrderThickeningQ₁DP :
    secondOrderThickeningDPScheme S A ⟶ A.thickening.target
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningQ₂DP`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 841](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L841). The attribute's comment: “q₂ is a morphism of divided power schemes”.

> **`q₂ : T'' ⟶ T` is a morphism of divided power schemes.**

```lean
public def secondOrderThickeningQ₂DP :
    secondOrderThickeningDPScheme S A ⟶ A.thickening.target
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningQ₀₁DP`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 851](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L851). The attribute's comment: “q₀₁ is a morphism of divided power schemes”.

> **`q₀₁ : T'' ⟶ T'` is a morphism of divided power schemes.**

```lean
public def secondOrderThickeningQ₀₁DP :
    secondOrderThickeningDPScheme S A ⟶ firstOrderThickeningDPScheme S A
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningQ₀₂DP`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 859](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L859). The attribute's comment: “q₀₂ is a morphism of divided power schemes”.

> **`q₀₂ : T'' ⟶ T'` is a morphism of divided power schemes.**

```lean
public def secondOrderThickeningQ₀₂DP :
    secondOrderThickeningDPScheme S A ⟶ firstOrderThickeningDPScheme S A
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningQ₁₂DP`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 867](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L867). The attribute's comment: “q₁₂ is a morphism of divided power schemes”.

> **`q₁₂ : T'' ⟶ T'` is a morphism of divided power schemes.**

```lean
public def secondOrderThickeningQ₁₂DP :
    secondOrderThickeningDPScheme S A ⟶ firstOrderThickeningDPScheme S A
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningSchemeThickening`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 878](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L878). The attribute's comment: “U ⟶ T'' is a divided power thickening”.

> **The divided power thickening `U ⟶ T''`**: a thickening of schemes whose defining ideal is
> the divided power ideal `J''`.

```lean
public abbrev secondOrderThickeningSchemeThickening : SchemeThickening.{u}
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningObject`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 897](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L897). The attribute's comment: “(U, T'', δ'') is an object of CRIS(X/S)”.

> **`(U, T'', δ'')` is an object of `CRIS(X/S)`.**  This is the final assertion of
> [Stacks, Tag 07J3]: the second-order universal thickening of an object of the crystalline
> category is again an object of it.  `T''` with the ideal
> `J'' = J ⊕ Ω_{T/S,δ} ⊕ Ω_{T/S,δ} ⊕ Ω²_{T/S,δ}` and the divided powers `δ''` of the remark is a
> divided power scheme, `U ⟶ T''` is a divided power thickening, and `T'' ⟶ S` is `q₀` followed by
> the structure morphism of `T`.

```lean
public abbrev secondOrderThickeningObject : Thickening S
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningSiteQ₀`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 917](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L917). The attribute's comment: “the morphism q₀ of CRIS(X/S)”.

> **The morphism `q₀ : (U, T'', δ'') ⟶ (U, T, δ)` of `CRIS(X/S)`.**

```lean
public def secondOrderThickeningSiteQ₀ : secondOrderThickeningObject S A ⟶ A
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningSiteQ₁`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 935](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L935). The attribute's comment: “the morphism q₁ of CRIS(X/S)”.

> **The morphism `q₁ : (U, T'', δ'') ⟶ (U, T, δ)` of `CRIS(X/S)`.**  It is a morphism over the
> divided power base because `q₁` and `q₀` agree after composing with the structure morphism of
> `T`.

```lean
public def secondOrderThickeningSiteQ₁ : secondOrderThickeningObject S A ⟶ A
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningSiteQ₂`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 958](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L958). The attribute's comment: “the morphism q₂ of CRIS(X/S)”.

> **The morphism `q₂ : (U, T'', δ'') ⟶ (U, T, δ)` of `CRIS(X/S)`.**

```lean
public def secondOrderThickeningSiteQ₂ : secondOrderThickeningObject S A ⟶ A
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningSiteQ₀₁`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 981](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L981). The attribute's comment: “the morphism q₀₁ of CRIS(X/S)”.

> **The morphism `q₀₁ : (U, T'', δ'') ⟶ (U, T', δ')` of `CRIS(X/S)`.**

```lean
public def secondOrderThickeningSiteQ₀₁ :
    secondOrderThickeningObject S A ⟶ firstOrderThickeningObject S A
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningSiteQ₀₂`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1011](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1011). The attribute's comment: “the morphism q₀₂ of CRIS(X/S)”.

> **The morphism `q₀₂ : (U, T'', δ'') ⟶ (U, T', δ')` of `CRIS(X/S)`.**

```lean
public def secondOrderThickeningSiteQ₀₂ :
    secondOrderThickeningObject S A ⟶ firstOrderThickeningObject S A
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningSiteQ₁₂`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1041](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1041). The attribute's comment: “the morphism q₁₂ of CRIS(X/S)”.

> **The morphism `q₁₂ : (U, T'', δ'') ⟶ (U, T', δ')` of `CRIS(X/S)`.**

```lean
public def secondOrderThickeningSiteQ₁₂ :
    secondOrderThickeningObject S A ⟶ firstOrderThickeningObject S A
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningSiteQ₀₁_comp_P₀`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1073](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1073). The attribute's comment: “the relation q₀ = q₀₁ ∘ p₀ in CRIS(X/S)”.

> **`q₀ = q₀₁ ∘ p₀` in `CRIS(X/S)`**, one of the six relations of [Stacks, Tag 07J3].

```lean
public theorem secondOrderThickeningSiteQ₀₁_comp_P₀ :
    secondOrderThickeningSiteQ₀₁ S A ≫ firstOrderThickeningSiteP₀ S A =
      secondOrderThickeningSiteQ₀ S A
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningSiteQ₀₁_comp_P₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1081](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1081). The attribute's comment: “the relation q₁ = q₀₁ ∘ p₁ in CRIS(X/S)”.

> **`q₁ = q₀₁ ∘ p₁` in `CRIS(X/S)`**, one of the six relations of [Stacks, Tag 07J3].

```lean
public theorem secondOrderThickeningSiteQ₀₁_comp_P₁ :
    secondOrderThickeningSiteQ₀₁ S A ≫ firstOrderThickeningSiteP₁ S A =
      secondOrderThickeningSiteQ₁ S A
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningSiteQ₁₂_comp_P₀`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1089](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1089). The attribute's comment: “the relation q₁ = q₁₂ ∘ p₀ in CRIS(X/S)”.

> **`q₁ = q₁₂ ∘ p₀` in `CRIS(X/S)`**, one of the six relations of [Stacks, Tag 07J3].

```lean
public theorem secondOrderThickeningSiteQ₁₂_comp_P₀ :
    secondOrderThickeningSiteQ₁₂ S A ≫ firstOrderThickeningSiteP₀ S A =
      secondOrderThickeningSiteQ₁ S A
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningSiteQ₁₂_comp_P₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1097](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1097). The attribute's comment: “the relation q₂ = q₁₂ ∘ p₁ in CRIS(X/S)”.

> **`q₂ = q₁₂ ∘ p₁` in `CRIS(X/S)`**, one of the six relations of [Stacks, Tag 07J3].

```lean
public theorem secondOrderThickeningSiteQ₁₂_comp_P₁ :
    secondOrderThickeningSiteQ₁₂ S A ≫ firstOrderThickeningSiteP₁ S A =
      secondOrderThickeningSiteQ₂ S A
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningSiteQ₀₂_comp_P₀`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1105). The attribute's comment: “the relation q₀ = q₀₂ ∘ p₀ in CRIS(X/S)”.

> **`q₀ = q₀₂ ∘ p₀` in `CRIS(X/S)`**, one of the six relations of [Stacks, Tag 07J3].

```lean
public theorem secondOrderThickeningSiteQ₀₂_comp_P₀ :
    secondOrderThickeningSiteQ₀₂ S A ≫ firstOrderThickeningSiteP₀ S A =
      secondOrderThickeningSiteQ₀ S A
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningSiteQ₀₂_comp_P₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1113). The attribute's comment: “the relation q₂ = q₀₂ ∘ p₁ in CRIS(X/S)”.

> **`q₂ = q₀₂ ∘ p₁` in `CRIS(X/S)`**, one of the six relations of [Stacks, Tag 07J3].

```lean
public theorem secondOrderThickeningSiteQ₀₂_comp_P₁ :
    secondOrderThickeningSiteQ₀₂ S A ≫ firstOrderThickeningSiteP₁ S A =
      secondOrderThickeningSiteQ₂ S A
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningCrysObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1128). The attribute's comment: “(U, T'', δ'') is an object of Cris(X/S)”.

> **`(U, T'', δ'')` is an object of the small crystalline category `Cris(X/S)`** whenever
> `(U, T, δ)` is.  The construction leaves the map `U ⟶ X` untouched, so it is still an open
> immersion; this is the assertion of [Stacks, Tag 07J3] in the category in which the remark states
> it.

```lean
public def secondOrderThickeningCrysObject : CrystallineThickening S
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningCrysQ₀`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1133). The attribute's comment: “the morphism q₀ of the diagram in Cris(X/S)”.

> **The morphism `q₀ : (U, T'', δ'') ⟶ (U, T, δ)` of `Cris(X/S)`.**

```lean
public def secondOrderThickeningCrysQ₀ : secondOrderThickeningCrysObject S B ⟶ B
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningCrysQ₁`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1138). The attribute's comment: “the morphism q₁ of the diagram in Cris(X/S)”.

> **The morphism `q₁ : (U, T'', δ'') ⟶ (U, T, δ)` of `Cris(X/S)`.**

```lean
public def secondOrderThickeningCrysQ₁ : secondOrderThickeningCrysObject S B ⟶ B
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningCrysQ₂`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1143). The attribute's comment: “the morphism q₂ of the diagram in Cris(X/S)”.

> **The morphism `q₂ : (U, T'', δ'') ⟶ (U, T, δ)` of `Cris(X/S)`.**

```lean
public def secondOrderThickeningCrysQ₂ : secondOrderThickeningCrysObject S B ⟶ B
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningCrysQ₀₁`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1148). The attribute's comment: “the morphism q₀₁ of the diagram in Cris(X/S)”.

> **The morphism `q₀₁ : (U, T'', δ'') ⟶ (U, T', δ')` of `Cris(X/S)`.**

```lean
public def secondOrderThickeningCrysQ₀₁ :
    secondOrderThickeningCrysObject S B ⟶ firstOrderThickeningCrysObject S B
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningCrysQ₀₂`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1154). The attribute's comment: “the morphism q₀₂ of the diagram in Cris(X/S)”.

> **The morphism `q₀₂ : (U, T'', δ'') ⟶ (U, T', δ')` of `Cris(X/S)`.**

```lean
public def secondOrderThickeningCrysQ₀₂ :
    secondOrderThickeningCrysObject S B ⟶ firstOrderThickeningCrysObject S B
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningCrysQ₁₂`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1160). The attribute's comment: “the morphism q₁₂ of the diagram in Cris(X/S)”.

> **The morphism `q₁₂ : (U, T'', δ'') ⟶ (U, T', δ')` of `Cris(X/S)`.**

```lean
public def secondOrderThickeningCrysQ₁₂ :
    secondOrderThickeningCrysObject S B ⟶ firstOrderThickeningCrysObject S B
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningCrysQ₀₁_comp_P₀`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1166). The attribute's comment: “the relation q₀ = q₀₁ ∘ p₀ in Cris(X/S)”.

> **`q₀ = q₀₁ ∘ p₀` in `Cris(X/S)`.**

```lean
public theorem secondOrderThickeningCrysQ₀₁_comp_P₀ :
    secondOrderThickeningCrysQ₀₁ S B ≫ firstOrderThickeningCrysP₀ S B =
      secondOrderThickeningCrysQ₀ S B
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningCrysQ₀₁_comp_P₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1173). The attribute's comment: “the relation q₁ = q₀₁ ∘ p₁ in Cris(X/S)”.

> **`q₁ = q₀₁ ∘ p₁` in `Cris(X/S)`.**

```lean
public theorem secondOrderThickeningCrysQ₀₁_comp_P₁ :
    secondOrderThickeningCrysQ₀₁ S B ≫ firstOrderThickeningCrysP₁ S B =
      secondOrderThickeningCrysQ₁ S B
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningCrysQ₁₂_comp_P₀`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1180). The attribute's comment: “the relation q₁ = q₁₂ ∘ p₀ in Cris(X/S)”.

> **`q₁ = q₁₂ ∘ p₀` in `Cris(X/S)`.**

```lean
public theorem secondOrderThickeningCrysQ₁₂_comp_P₀ :
    secondOrderThickeningCrysQ₁₂ S B ≫ firstOrderThickeningCrysP₀ S B =
      secondOrderThickeningCrysQ₁ S B
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningCrysQ₁₂_comp_P₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1187). The attribute's comment: “the relation q₂ = q₁₂ ∘ p₁ in Cris(X/S)”.

> **`q₂ = q₁₂ ∘ p₁` in `Cris(X/S)`.**

```lean
public theorem secondOrderThickeningCrysQ₁₂_comp_P₁ :
    secondOrderThickeningCrysQ₁₂ S B ≫ firstOrderThickeningCrysP₁ S B =
      secondOrderThickeningCrysQ₂ S B
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningCrysQ₀₂_comp_P₀`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1194). The attribute's comment: “the relation q₀ = q₀₂ ∘ p₀ in Cris(X/S)”.

> **`q₀ = q₀₂ ∘ p₀` in `Cris(X/S)`.**

```lean
public theorem secondOrderThickeningCrysQ₀₂_comp_P₀ :
    secondOrderThickeningCrysQ₀₂ S B ≫ firstOrderThickeningCrysP₀ S B =
      secondOrderThickeningCrysQ₀ S B
```

**`Crystalline.GlobalCrystallineSituation.secondOrderThickeningCrysQ₀₂_comp_P₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean, line 1201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningScheme.lean#L1201). The attribute's comment: “the relation q₂ = q₀₂ ∘ p₁ in Cris(X/S)”.

> **`q₂ = q₀₂ ∘ p₁` in `Cris(X/S)`.**

```lean
public theorem secondOrderThickeningCrysQ₀₂_comp_P₁ :
    secondOrderThickeningCrysQ₀₂ S B ≫ firstOrderThickeningCrysP₁ S B =
      secondOrderThickeningCrysQ₂ S B
```

**`Crystalline.GlobalCrystallineSituation.crysSheafRingMap_q₀₁_add_q₁₂_diffSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningSections.lean, line 367](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningSections.lean#L367). The attribute's comment: “the first formula of the remark on the sections over an object: on a section of the square-zero summand of 𝒪\_\{T'}, q₀₁ + q₁₂ = q₀₂ + d, the two-form d ω being read through the top summand Ω² of 𝒪\_\{T''}”.

> **The first formula of [Stacks, Remark 60.14.5, Tag 07J3] on sections over an object.**  On a
> section `ω` of the square-zero summand `Ω_{T/S,δ}` of `𝒪_{T'}` the three maps out of `𝒪_{T'}` of
> the remark satisfy
>
> `q₀₁^* ω + q₁₂^* ω = q₀₂^* ω + d ω`,
>
> the two-form `d ω` being read in `𝒪_{T''}` through the top summand.  Indeed
> `q₀₁ (0, ω) = (0, ω, 0, 0)`, `q₁₂ (0, ω) = (0, 0, ω, d ω)` and `q₀₂ (0, ω) = (0, ω, ω, 0)`.  This
> is the identity `q₀₁^* ω + q₁₂^* ω - q₀₂^* ω = d ω` that the proof of [Stacks, Tag 07J6] reads off
> the remark.

```lean
theorem crysSheafRingMap_q₀₁_add_q₁₂_diffSection (A : Thickening S)
    (ω : crysDiffSections A) :
    crysSheafRingMap (secondOrderThickeningSiteQ₀₁ S A)
          (firstOrderThickeningDiffSection A ω) +
        crysSheafRingMap (secondOrderThickeningSiteQ₁₂ S A)
          (firstOrderThickeningDiffSection A ω) =
      crysSheafRingMap (secondOrderThickeningSiteQ₀₂ S A)
          (firstOrderThickeningDiffSection A ω) +
        secondOrderTopSection A (crysDeRham A ω)
```

**`Crystalline.GlobalCrystallineSituation.crysSheafRingMap_q₁₂_mul_q₀₁_diffSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningSections.lean, line 388](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SecondOrderThickeningSections.lean#L388). The attribute's comment: “the second formula of the remark on the sections over an object: the product in 𝒪\_\{T''} of a differential read through q₁₂ with one read through q₀₁ is their exterior product in the other order, read through the top summand Ω²”.

> **The second formula of [Stacks, Remark 60.14.5, Tag 07J3] on sections over an object.**  The
> product in `𝒪_{T''}` of a section of the square-zero summand of `𝒪_{T'}` read through `q₁₂` with
> one read through `q₀₁` is their exterior product, in the other order:
>
> `q₁₂^* ω · q₀₁^* ω' = ω' ∧ ω`.

```lean
theorem crysSheafRingMap_q₁₂_mul_q₀₁_diffSection (A : Thickening S)
    (ω ω' : crysDiffSections A) :
    crysSheafRingMap (secondOrderThickeningSiteQ₁₂ S A)
          (firstOrderThickeningDiffSection A ω) *
        crysSheafRingMap (secondOrderThickeningSiteQ₀₁ S A)
          (firstOrderThickeningDiffSection A ω') =
      secondOrderTopSection A (crysWedgeSections A ω' ω)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.13, Tag 07KN](https://stacks.math.columbia.edu/tag/07KN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
