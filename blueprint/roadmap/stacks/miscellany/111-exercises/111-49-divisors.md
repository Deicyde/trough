---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.mono_toTotalQuotientSheaf, AlgebraicGeometry.Scheme.shortExact_unitGroupSheaf, AlgebraicGeometry.Scheme.CartierDivisor, AlgebraicGeometry.exists_affineOpen_local_representation, AlgebraicGeometry.cartierWeilDivisor, AlgebraicGeometry.cartierWeilDivisor_apply, AlgebraicGeometry.cartierWeilDivisor_apply_of_germ_eq_zero, AlgebraicGeometry.cartierWeilDivisor_apply_of_local_eq
statement: formalized
proof: formalized
---

# 111.49 Divisors

Section 111.49 of the Stacks Project, [Tag 02AQ](https://stacks.math.columbia.edu/tag/02AQ). 1 tag here is carried by 21 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02AR, a definition

[Tag 02AR](https://stacks.math.columbia.edu/tag/02AR) in the Stacks Project.

**`AlgebraicGeometry.Scheme.mono_toTotalQuotientSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/CartierDivisor.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/CartierDivisor.lean#L164). The attribute's comment: “unit\_sheaf\_sequence”.

> **Stacks 02AR part (6).** The structure sheaf of a scheme is a subsheaf of its sheaf of
> total quotient rings.

```lean
theorem Scheme.mono_toTotalQuotientSheaf (Y : Scheme.{u}) :
    Mono Y.toTotalQuotientSheaf
```

**`AlgebraicGeometry.Scheme.shortExact_unitGroupSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/CartierDivisor.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/CartierDivisor.lean#L171). The attribute's comment: “unit\_sheaf\_sequence”.

> **Stacks 02AR part (6).** The sequence `0 ⟶ 𝒪_X^* ⟶ 𝒦_X^* ⟶ 𝒦_X^*/𝒪_X^* ⟶ 0` of
> unit-group sheaves of a scheme is short exact.

```lean
theorem Scheme.shortExact_unitGroupSheaf (Y : Scheme.{u}) :
    (ShortComplex.mk (unitGroupSheafMap Y.toTotalQuotientSheaf)
      (unitGroupQuotientMap Y.toTotalQuotientSheaf) (by
        change (presheafToSheaf (Opens.grothendieckTopology Y.toPresheafedSpace)
            AddCommGrpCat.{u}).map (unitGroupMap Y.toTotalQuotientSheaf) ≫
          (presheafToSheaf (Opens.grothendieckTopology Y.toPresheafedSpace)
            AddCommGrpCat.{u}).map
            (cokernel.π (unitGroupMap Y.toTotalQuotientSheaf)) = 0
        rw [← Functor.map_comp]
        simp)).ShortExact
```

**`AlgebraicGeometry.Scheme.CartierDivisor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/CartierDivisor.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/CartierDivisor.lean#L187). The attribute's comment: “cartier\_divisor”.

> **Stacks 02AR part (7).** A Cartier divisor on a scheme is a global section of the quotient
> sheaf `𝒦_X^*/𝒪_X^*`.

```lean
abbrev Scheme.CartierDivisor (Y : Scheme.{u}) : Type u
```

**`AlgebraicGeometry.exists_affineOpen_local_representation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/CartierWeilDivisor.lean, line 576](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/CartierWeilDivisor.lean#L576). The attribute's comment: “cartier\_weil\_divisor”.

> **Tag 02AR part (8), the local presentation of clause (b).** Near any point of a locally
> Noetherian integral scheme, a Cartier divisor is the image of a unit of the sheaf of total
> quotient rings over an affine open neighbourhood, and that unit is the fraction `a / b` of two
> regular functions on that neighbourhood with `b` nonzero.

```lean
theorem exists_affineOpen_local_representation [IsIntegral X] [IsLocallyNoetherian X]
    (τ : X.CartierDivisor) (x : X) :
    ∃ (U : X.Opens) (_ : IsAffineOpen U) (_ : x ∈ U) (a b : Γ(X, U)) (_ : b ≠ 0)
      (v : (unitGroupPresheaf X.totalQuotientSheaf).obj (op U)),
      (Additive.toMul v).val * X.toTotalQuotientSheaf.hom.app (op U) b =
          X.toTotalQuotientSheaf.hom.app (op U) a ∧
        (unitGroupQuotientSheaf X.toTotalQuotientSheaf).presheaf.map (homOfLE le_top).op τ =
          (rawUnitGroupQuotientMap X.toTotalQuotientSheaf).app (op U) v
```

**`AlgebraicGeometry.cartierWeilDivisor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/CartierWeilDivisor.lean, line 724](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/CartierWeilDivisor.lean#L724). The attribute's comment: “cartier\_weil\_divisor”.

> **Stacks 02AR part (8).** The Weil divisor `[τ] = Σ v_Z(τ) [Z]` of a Cartier divisor on a
> Noetherian integral scheme.

```lean
def cartierWeilDivisor [IsNoetherian X] [IsIntegral X] (τ : X.CartierDivisor) : WeilDivisor X
```

**`AlgebraicGeometry.cartierWeilDivisor_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/CartierWeilDivisor.lean, line 731](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/CartierWeilDivisor.lean#L731). The attribute's comment: “cartier\_weil\_divisor”.

> **Stacks 02AR part (8).** The coefficient of `[τ]` at a prime divisor is the order
> `v_Z(τ)`.

```lean
theorem cartierWeilDivisor_apply [IsNoetherian X] [IsIntegral X] (τ : X.CartierDivisor)
    (Z : PrimeDivisor X) :
    (cartierWeilDivisor τ).1 Z = cartierMultiplicity τ Z.genericPoint
```

**`AlgebraicGeometry.cartierWeilDivisor_apply_of_germ_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/CartierWeilDivisor.lean, line 739](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/CartierWeilDivisor.lean#L739). The attribute's comment: “cartier\_weil\_divisor”.

> **Stacks 02AR part (8), clause (a).** The coefficient of `[τ]` vanishes at a prime divisor at
> whose generic point the germ of `τ` is zero.

```lean
theorem cartierWeilDivisor_apply_of_germ_eq_zero [IsNoetherian X] [IsIntegral X]
    (τ : X.CartierDivisor) (Z : PrimeDivisor X)
    (hτ : (unitGroupQuotientSheaf X.toTotalQuotientSheaf).presheaf.Γgerm Z.genericPoint τ = 0) :
    (cartierWeilDivisor τ).1 Z = 0
```

**`AlgebraicGeometry.cartierWeilDivisor_apply_of_local_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/CartierWeilDivisor.lean, line 748](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/CartierWeilDivisor.lean#L748). The attribute's comment: “cartier\_weil\_divisor”.

> **Stacks 02AR part (8), clause (b).** The coefficient of `[τ]` at a prime divisor computed
> from a local presentation `a / b` of `τ` on an open neighbourhood of its generic point.

```lean
theorem cartierWeilDivisor_apply_of_local_eq [IsNoetherian X] [IsIntegral X]
    (τ : X.CartierDivisor) (Z : PrimeDivisor X) (U : X.Opens) (hξ : Z.genericPoint ∈ U)
    (a b : Γ(X, U)) (hb : b ≠ 0)
    (v : (unitGroupPresheaf X.totalQuotientSheaf).obj (op U))
    (hab : (Additive.toMul v).val * X.toTotalQuotientSheaf.hom.app (op U) b =
      X.toTotalQuotientSheaf.hom.app (op U) a)
    (hτ : (unitGroupQuotientSheaf X.toTotalQuotientSheaf).presheaf.map (homOfLE le_top).op τ =
      (rawUnitGroupQuotientMap X.toTotalQuotientSheaf).app (op U) v) :
    (cartierWeilDivisor τ).1 Z =
      ((Module.length (X.presheaf.stalk Z.genericPoint)
        ((X.presheaf.stalk Z.genericPoint) ⧸
          Ideal.span {X.presheaf.germ U Z.genericPoint hξ a})).toNat : ℤ) -
      ((Module.length (X.presheaf.stalk Z.genericPoint)
        ((X.presheaf.stalk Z.genericPoint) ⧸
          Ideal.span {X.presheaf.germ U Z.genericPoint hξ b})).toNat : ℤ)
```

**`AlgebraicGeometry.effectiveCartierWeilDivisor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartierWeilDivisor.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartierWeilDivisor.lean#L314). The attribute's comment: “effective\_cartier\_weil\_divisor”.

> **Stacks 02AR part (5).** The Weil divisor `[D] = Σ v_Z(D) [Z]` of an effective Cartier
> divisor on a Noetherian integral scheme.
>
> The hypothesis is not used by the term — the coefficient family of an arbitrary ideal sheaf is
> already finitely supported — but it is what makes the coefficients the orders of Tag 02AR,
> since only for an effective Cartier divisor is the local length finite.

```lean
def effectiveCartierWeilDivisor [IsNoetherian X] [IsIntegral X] (I : X.IdealSheafData)
    (_hI : Stacks.Divisors.IsEffectiveCartierDivisor I) : WeilDivisor X
```

**`AlgebraicGeometry.effectiveCartierWeilDivisor_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartierWeilDivisor.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartierWeilDivisor.lean#L323). The attribute's comment: “effective\_cartier\_weil\_divisor”.

> **Stacks 02AR part (5).** The coefficient of `[D]` at a prime divisor is the order
> `v_Z(D)`.

```lean
theorem effectiveCartierWeilDivisor_apply [IsNoetherian X] [IsIntegral X]
    (I : X.IdealSheafData) (hI : Stacks.Divisors.IsEffectiveCartierDivisor I)
    (Z : PrimeDivisor X) :
    (effectiveCartierWeilDivisor I hI).1 Z = effectiveCartierMultiplicity I Z
```

**`AlgebraicGeometry.effectiveCartierWeilDivisor_apply_of_notMem_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartierWeilDivisor.lean, line 331](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartierWeilDivisor.lean#L331). The attribute's comment: “effective\_cartier\_weil\_divisor”.

> **Stacks 02AR part (5), clause (a).** The coefficient of `[D]` at a prime divisor whose
> generic point lies outside `D` is zero.

```lean
theorem effectiveCartierWeilDivisor_apply_of_notMem_support [IsNoetherian X] [IsIntegral X]
    (I : X.IdealSheafData) (hI : Stacks.Divisors.IsEffectiveCartierDivisor I)
    (Z : PrimeDivisor X) (hZ : Z.genericPoint ∉ I.support) :
    (effectiveCartierWeilDivisor I hI).1 Z = 0
```

**`AlgebraicGeometry.effectiveCartierWeilDivisor_apply_of_ideal_eq_span`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartierWeilDivisor.lean, line 352](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartierWeilDivisor.lean#L352). The attribute's comment: “effective\_cartier\_weil\_divisor”.

> **Stacks 02AR part (5), clause (b).** When the generic point of `Z` lies in `D`, the
> coefficient of `[D]` at `Z` is the length of `𝒪_{X, Z} / (f)` for the nonzerodivisor `f` that
> defines `D` on an affine open neighbourhood of that generic point, as in part (4).

```lean
theorem effectiveCartierWeilDivisor_apply_of_ideal_eq_span [IsNoetherian X] [IsIntegral X]
    {I : X.IdealSheafData} (hI : Stacks.Divisors.IsEffectiveCartierDivisor I)
    (Z : PrimeDivisor X) {U : X.affineOpens} (hxU : Z.genericPoint ∈ U.1) {f : Γ(X, U.1)}
    (hf : I.ideal U = Ideal.span {f}) :
    (effectiveCartierWeilDivisor I hI).1 Z =
      ((Module.length (X.presheaf.stalk Z.genericPoint)
        ((X.presheaf.stalk Z.genericPoint) ⧸
          Ideal.span {(X.presheaf.germ U.1 Z.genericPoint hxU).hom f})).toNat : ℤ)
```

**`AlgebraicGeometry.Scheme.totalQuotientSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TotalQuotient.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TotalQuotient.lean#L83). The attribute's comment: “total\_quotient\_sheaf”. References: EGA IV (20.1.3).

> The sheaf of total quotient rings of a scheme. It is the sheafification of the presheaf
> which, on each open set, localizes the ring of regular functions at the sections whose germs
> are nonzerodivisors everywhere on that open set.

```lean
noncomputable abbrev Scheme.totalQuotientSheaf (Y : Scheme.{u}) :
    TopCat.Sheaf CommRingCat.{u} Y
```

**`AlgebraicGeometry.Scheme.toTotalQuotientSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TotalQuotient.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TotalQuotient.lean#L90). The attribute's comment: “total\_quotient\_sheaf”.

> The canonical morphism from the structure sheaf to the sheaf of total quotient rings,
> giving the latter its structure as a sheaf of `𝒪_X`-algebras.

```lean
noncomputable def Scheme.toTotalQuotientSheaf (Y : Scheme.{u}) :
    Y.sheaf ⟶ Y.totalQuotientSheaf
```

**`AlgebraicGeometry.PrimeDivisor.algebraMap_stalk_functionField_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RationalFunctionWeilDivisor.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RationalFunctionWeilDivisor.lean#L68). The attribute's comment: “prime\_divisor”.

> **Stacks 02AR part (2), the local ring as a subring.** On an integral scheme the local ring
> `𝒪_{X, Z}` at the generic point of a prime divisor `Z` embeds into the function field `K(X)`.

```lean
theorem PrimeDivisor.algebraMap_stalk_functionField_injective [IsIntegral X]
    (Z : PrimeDivisor X) :
    Function.Injective
      (algebraMap (X.presheaf.stalk Z.genericPoint) X.functionField)
```

**`AlgebraicGeometry.rationalFunctionWeilDivisor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RationalFunctionWeilDivisor.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RationalFunctionWeilDivisor.lean#L79). The attribute's comment: “rational\_function\_weil\_divisor”.

> **Stacks 02AR part (3).** The Weil divisor `Σ v_Z(f) [Z]` of a nonzero rational function `f`
> on a Noetherian integral scheme: the coefficient at a prime divisor `Z` is the order of vanishing
> of `f` at the generic point of `Z`.

```lean
def rationalFunctionWeilDivisor [IsNoetherian X] [IsIntegral X] (f : X.functionFieldˣ) :
    WeilDivisor X
```

**`AlgebraicGeometry.rationalFunctionWeilDivisor_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RationalFunctionWeilDivisor.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RationalFunctionWeilDivisor.lean#L86). The attribute's comment: “rational\_function\_weil\_divisor”.

> **Stacks 02AR part (3).** The coefficient of the Weil divisor of a rational function at a
> prime divisor `Z` is the order `v_Z(f)`.

```lean
theorem rationalFunctionWeilDivisor_apply [IsNoetherian X] [IsIntegral X]
    (f : X.functionFieldˣ) (Z : PrimeDivisor X) :
    (rationalFunctionWeilDivisor X f).1 Z = X.ord (f : X.functionField) Z.genericPoint
```

**`AlgebraicGeometry.rationalFunctionWeilDivisor_apply_of_eq_algebraMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RationalFunctionWeilDivisor.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RationalFunctionWeilDivisor.lean#L94). The attribute's comment: “rational\_function\_weil\_divisor”.

> **Stacks 02AR part (3), clause (b).** If the rational function `f` lies in the local ring
> `𝒪_{X, Z}`, its coefficient at `Z` is the length of `𝒪_{X, Z} / (f)`.

```lean
theorem rationalFunctionWeilDivisor_apply_of_eq_algebraMap [IsNoetherian X] [IsIntegral X]
    (f : X.functionFieldˣ) (Z : PrimeDivisor X) (a : X.presheaf.stalk Z.genericPoint)
    (hf : (f : X.functionField) = algebraMap _ X.functionField a) :
    (rationalFunctionWeilDivisor X f).1 Z =
      ((Module.length (X.presheaf.stalk Z.genericPoint)
        ((X.presheaf.stalk Z.genericPoint) ⧸ Ideal.span {a})).toNat : ℤ)
```

**`AlgebraicGeometry.rationalFunctionWeilDivisor_apply_of_eq_algebraMap_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RationalFunctionWeilDivisor.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RationalFunctionWeilDivisor.lean#L109). The attribute's comment: “rational\_function\_weil\_divisor”.

> **Stacks 02AR part (3), clause (a).** If the rational function `f` is a unit of the local
> ring `𝒪_{X, Z}`, its coefficient at `Z` is zero.

```lean
theorem rationalFunctionWeilDivisor_apply_of_eq_algebraMap_unit [IsNoetherian X] [IsIntegral X]
    (f : X.functionFieldˣ) (Z : PrimeDivisor X) (u : (X.presheaf.stalk Z.genericPoint)ˣ)
    (hf : (f : X.functionField) =
      algebraMap _ X.functionField (u : X.presheaf.stalk Z.genericPoint)) :
    (rationalFunctionWeilDivisor X f).1 Z = 0
```

**`AlgebraicGeometry.rationalFunctionWeilDivisor_apply_of_eq_div`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RationalFunctionWeilDivisor.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RationalFunctionWeilDivisor.lean#L124). The attribute's comment: “rational\_function\_weil\_divisor”.

> **Stacks 02AR part (3), clause (c).** If the rational function is a fraction `f = a / b` of
> two elements of the local ring `𝒪_{X, Z}`, its coefficient at `Z` is the difference of the
> lengths of `𝒪_{X, Z} / (a)` and `𝒪_{X, Z} / (b)`.

```lean
theorem rationalFunctionWeilDivisor_apply_of_eq_div [IsNoetherian X] [IsIntegral X]
    (f : X.functionFieldˣ) (Z : PrimeDivisor X) (a b : X.presheaf.stalk Z.genericPoint)
    (hf : (f : X.functionField) =
      algebraMap _ X.functionField a / algebraMap _ X.functionField b) :
    (rationalFunctionWeilDivisor X f).1 Z =
      ((Module.length (X.presheaf.stalk Z.genericPoint)
        ((X.presheaf.stalk Z.genericPoint) ⧸ Ideal.span {a})).toNat : ℤ) -
      ((Module.length (X.presheaf.stalk Z.genericPoint)
        ((X.presheaf.stalk Z.genericPoint) ⧸ Ideal.span {b})).toNat : ℤ)
```

**`AlgebraicGeometry.mem_nonZeroDivisors_of_mem_submonoidPresheafOfStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Meromorphic/TotalQuotientSheafSections.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Meromorphic/TotalQuotientSheafSections.lean#L80). The attribute's comment: “total\_quotient\_sheaf”.

> **Stacks 02AR part (6), the denominators are nonzerodivisors.** For a sheaf of commutative
> rings, a section over an open set whose germ at every point of that open set is a nonzerodivisor
> is itself a nonzerodivisor in the ring of sections. This is the inclusion of the denominator
> submonoid `S_U` of the total quotient presheaf into the nonzerodivisors, and it needs no
> hypothesis on the open set.

```lean
theorem mem_nonZeroDivisors_of_mem_submonoidPresheafOfStalk
    (O : TopCat.Sheaf CommRingCat.{u} X) {U : Opens X} {b : O.presheaf.obj (op U)}
    (hb : b ∈ (O.presheaf.submonoidPresheafOfStalk
      fun y => (O.presheaf.stalk y)⁰).obj (op U)) :
    b ∈ (O.presheaf.obj (op U))⁰
```

Declarations registered for the tag:

- [`AlgebraicGeometry.PrimeDivisor`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/PrimeDivisor.lean#L58), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Divisors/PrimeDivisorStalk.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/PrimeDivisorStalk.lean#L143) (StacksFrontier): “prime\_divisor”.
- [`AlgebraicGeometry.WeilDivisor`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/PrimeDivisor.lean#L90), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Divisors/PrimeDivisorStalk.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/PrimeDivisorStalk.lean#L145) (StacksFrontier): “weil\_divisor”.
- [`Stacks.Divisors.IsEffectiveCartierDivisor`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartier.lean#L79), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Divisors/PrimeDivisorStalk.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/PrimeDivisorStalk.lean#L147) (StacksFrontier): “effective\_cartier\_divisor”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 111.49, Tag 02AQ](https://stacks.math.columbia.edu/tag/02AQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
