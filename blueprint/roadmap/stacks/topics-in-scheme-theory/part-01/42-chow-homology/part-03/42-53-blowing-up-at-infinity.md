---
declaration: section
origin: cited
lean: Stacks.Chow.blowupAtInfinity, Stacks.Chow.blowupAtInfinityToLine, Stacks.Chow.exceptionalIdealAtInfinity, Stacks.Chow.fibreIdealAtInfinity, Stacks.Chow.fibreIdealAtInfinity_le_exceptionalIdealAtInfinity, Stacks.Chow.isEffectiveCartierDivisor_fibreIdealAtInfinity, Stacks.Chow.exists_isEffectiveCartierDivisor_fibreIdealAtInfinity_eq, Stacks.Chow.blowUpToBlowupAtInfinity
statement: formalized
proof: formalized
---

# 42.53 Blowing up at infinity

Section 42.53 of the Stacks Project, [Tag 0FBG](https://stacks.math.columbia.edu/tag/0FBG). 3 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FBG, the section

[Tag 0FBG](https://stacks.math.columbia.edu/tag/0FBG) in the Stacks Project.

**`Stacks.Chow.blowupAtInfinity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean#L220). The attribute's comment: “the scheme W, the blowup of 𝐏¹_X in the centre ∞(Z)”.

> **The deformation space `W` of Stacks 0FBG**: the blowup of `𝐏¹_X` in the centre `∞(Z)`.

```lean
def blowupAtInfinity : Scheme.{u}
```

**`Stacks.Chow.blowupAtInfinityToLine`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean#L225). The attribute's comment: “the structure morphism b : W ⟶ 𝐏¹_X of the blowup at infinity”.

> **The structure morphism `b : W ⟶ 𝐏¹_X`** of the blowup at infinity.

```lean
def blowupAtInfinityToLine : blowupAtInfinity ℐ ⟶ relativeProjectiveLine X
```

**`Stacks.Chow.exceptionalIdealAtInfinity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean#L235). The attribute's comment: “the exceptional divisor E ⊆ W of the blowup at infinity”.

> The ideal of the exceptional divisor `E ⊆ W`: the inverse image of the centre `∞(Z)`
> along `b`.

```lean
def exceptionalIdealAtInfinity : (blowupAtInfinity ℐ).IdealSheafData
```

**`Stacks.Chow.fibreIdealAtInfinity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean#L241). The attribute's comment: “the fibre at infinity W_∞ ⊆ W, the inverse image of (𝐏¹_X)_∞ under b”.

> The ideal of the fibre at infinity `W_∞ ⊆ W`: the inverse image along `b` of the divisor at
> infinity `(𝐏¹_X)_∞`.

```lean
def fibreIdealAtInfinity : (blowupAtInfinity ℐ).IdealSheafData
```

**`Stacks.Chow.fibreIdealAtInfinity_le_exceptionalIdealAtInfinity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean#L252). The attribute's comment: “E ⊆ W_∞ as closed subschemes of W”.

> `E` is contained in `W_∞`: the centre `∞(Z)` contains the divisor at infinity, so its
> inverse image along `b` does too.

```lean
theorem fibreIdealAtInfinity_le_exceptionalIdealAtInfinity :
    fibreIdealAtInfinity ℐ ≤ exceptionalIdealAtInfinity ℐ
```

**`Stacks.Chow.isEffectiveCartierDivisor_fibreIdealAtInfinity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean#L261). The attribute's comment: “W_∞ is an effective Cartier divisor on W”.

> The fibre at infinity `W_∞` is an effective Cartier divisor on `W`: the divisor at infinity
> of `𝐏¹_X` is one, and the inverse image of an effective Cartier divisor under a blowup is again
> one.

```lean
theorem isEffectiveCartierDivisor_fibreIdealAtInfinity :
    Stacks.Divisors.IsEffectiveCartierDivisor (fibreIdealAtInfinity ℐ)
```

**`Stacks.Chow.exists_isEffectiveCartierDivisor_fibreIdealAtInfinity_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean#L271). The attribute's comment: “W_∞ is the sum of E and a second effective Cartier divisor on W”.

> **The fibre at infinity decomposes as `W_∞ = D + E`.** Both `E` and `W_∞` are effective
> Cartier divisors on `W` and `E ⊆ W_∞`, so `W_∞` is the sum of `E` and a third effective Cartier
> divisor `D`, written in the ideal-sheaf presentation `ℐ_{W_∞} = ℐ_E · ℐ_D`. That `D` is the
> divisor `X'` is `Stacks.Chow.eq_strictTransformIdealAtInfinity_of_mul_eq`.

```lean
theorem exists_isEffectiveCartierDivisor_fibreIdealAtInfinity_eq :
    ∃ D : (blowupAtInfinity ℐ).IdealSheafData,
      Stacks.Divisors.IsEffectiveCartierDivisor D ∧
        fibreIdealAtInfinity ℐ = exceptionalIdealAtInfinity ℐ * D
```

**`Stacks.Chow.blowUpToBlowupAtInfinity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean#L295). The attribute's comment: “the closed immersion X' ⟶ W of the square, X' the blowup of X in Z”.

> **The closed immersion `X' ⟶ W`** of the commutative square of Stacks 0FBG: the blowup `X'`
> of `X` in `Z` is the classifying morphism of `X' ⟶ X ⟶ 𝐏¹_X` for the centre `∞(Z)`.

```lean
def blowUpToBlowupAtInfinity : blowUp ℐ ⟶ blowupAtInfinity ℐ
```

**`Stacks.Chow.blowUpToBlowupAtInfinity_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean#L309). The attribute's comment: “commutativity of the square X' ⟶ W ⟶ 𝐏¹_X = X' ⟶ X ⟶ 𝐏¹_X”.

> The square of Stacks 0FBG commutes: `X' ⟶ W ⟶ 𝐏¹_X` equals `X' ⟶ X ⟶ 𝐏¹_X`.

```lean
theorem blowUpToBlowupAtInfinity_comp :
    blowUpToBlowupAtInfinity ℐ ≫ blowupAtInfinityToLine ℐ =
      blowUpToBase ℐ ≫ lineInfinitySection X
```

**`Stacks.Chow.comap_exceptionalIdealAtInfinity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean#L325). The attribute's comment: “(3): X' ∩ E is the exceptional divisor of X' ⟶ X”.

> **Stacks 0FBG, assertion (3).** The inverse image of the exceptional divisor `E ⊆ W` on
> `X'` is the exceptional divisor of the blowup `X' ⟶ X` of `X` in `Z`; that is, `X' ∩ E` is the
> exceptional divisor of `X' ⟶ X`.

```lean
theorem comap_exceptionalIdealAtInfinity :
    (exceptionalIdealAtInfinity ℐ).comap (blowUpToBlowupAtInfinity ℐ) = exceptionalIdeal ℐ
```

**`Stacks.Chow.lineToBlowupAtInfinity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean#L370). The attribute's comment: “(8): the closed immersion 𝐏¹_Z ⟶ W”.

> **Stacks 0FBG, assertion (8), the morphism.** The closed immersion `𝐏¹_Z ⟶ W`: the
> classifying morphism for the centre `∞(Z)` of the inclusion `𝐏¹_Z ⟶ 𝐏¹_X`, along which `∞(Z)`
> pulls back to the divisor at infinity of `𝐏¹_Z`.

```lean
def lineToBlowupAtInfinity :
    relativeProjectiveLine ℐ.subscheme ⟶ blowupAtInfinity ℐ
```

**`Stacks.Chow.lineToBlowupAtInfinity_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean#L383). The attribute's comment: “(8): the composite of 𝐏¹_Z ⟶ W with b is the inclusion 𝐏¹_Z ⟶ 𝐏¹_X”.

> **Stacks 0FBG, assertion (8), the triangle.** The composite of `𝐏¹_Z ⟶ W` with `b` is the
> inclusion morphism `𝐏¹_Z ⟶ 𝐏¹_X`.

```lean
theorem lineToBlowupAtInfinity_comp :
    lineToBlowupAtInfinity ℐ ≫ blowupAtInfinityToLine ℐ =
      projectiveLineBaseChange ℐ.subschemeι
```

**`Stacks.Chow.isIso_blowupAtInfinityToLine_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreBlowup.lean#L421). The attribute's comment: “(1): b is an isomorphism over 𝐀¹_X ∪ 𝐏¹_{X ∖ Z}”.

> **Stacks 0FBG, assertion (1).** The blowup at infinity is an isomorphism over
> `𝐀¹_X ∪ 𝐏¹_{X ∖ Z}`: that open misses the centre, and a blowup is an isomorphism over the
> complement of its centre.

```lean
theorem isIso_blowupAtInfinityToLine_restrict :
    IsIso (blowupAtInfinityToLine ℐ ∣_ isomorphismLocusAtInfinity ℐ)
```

**`Stacks.Chow.fibreIdealAtInfinity_eq_mul_strictTransformIdealAtInfinity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreDivisor.lean, line 524](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreDivisor.lean#L524). The attribute's comment: “(4): W_∞ = X' + E as effective Cartier divisors on W”.

> `W_∞ = X' + E` as effective Cartier divisors on `W`, in the
> ideal-sheaf presentation `ℐ_{W_∞} = ℐ_E · ℐ_{X'}`.

```lean
theorem fibreIdealAtInfinity_eq_mul_strictTransformIdealAtInfinity :
    fibreIdealAtInfinity ℐ =
      exceptionalIdealAtInfinity ℐ * strictTransformIdealAtInfinity ℐ
```

**`Stacks.Chow.isEffectiveCartierDivisor_strictTransformIdealAtInfinity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreDivisor.lean, line 532](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreDivisor.lean#L532). The attribute's comment: “(2): X' is an effective Cartier divisor on W”.

> The strict transform `X'` is an effective Cartier divisor on `W`.

```lean
theorem isEffectiveCartierDivisor_strictTransformIdealAtInfinity :
    Stacks.Divisors.IsEffectiveCartierDivisor (strictTransformIdealAtInfinity ℐ)
```

**`Stacks.Conormal.projectivizedNormalCone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/ProjectivizedNormalCone.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/ProjectivizedNormalCone.lean#L84). The attribute's comment: “the scheme Proj_Z(C_{Z/X,*}) of clause (6), as a relative Proj over Z”.

> **The projectivized normal cone `P_ZX = Proj_Z(𝒞_{Z/X,*})`** of an immersion `i : Z ⟶ X`:
> the relative `Proj` over `Z` of the conormal algebra. This is the scheme appearing in clause (6)
> of [Stacks, Tag 0FBG].

```lean
def projectivizedNormalCone : Scheme.{u}
```

## Tag 0FBH, an item

[Tag 0FBH](https://stacks.math.columbia.edu/tag/0FBH) in the Stacks Project.

**`Stacks.Chow.support_compl_strictTransformIdealOnExceptional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreNormalCone.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreNormalCone.lean#L110). The attribute's comment: “E ∖ (X' ∩ E) = E ∖ X' as open subschemes of E”.

> The open subscheme `E ∖ (X' ∩ E)` of the exceptional divisor is the inverse image of the open
> `W ∖ X'`, so `E ∖ (X' ∩ E) = E ∖ X'`.

```lean
theorem support_compl_strictTransformIdealOnExceptional :
    (strictTransformIdealOnExceptional ℐ).support.compl =
      (exceptionalIdealAtInfinity ℐ).subschemeι ⁻¹ᵁ
        (strictTransformIdealAtInfinity ℐ).support.compl
```

**`Stacks.Chow.mem_pow_infinityChartIdeal_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreNormalCone.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreNormalCone.lean#L229). The attribute's comment: “the powers of J = (I, s): the coefficient of s^j lies in I^(m-j)”.

> **The powers of `J = (I, s)`.** A polynomial lies in `Jᵐ` exactly when its coefficient of
> `sʲ` lies in `I^(m - j)` for every `j`, so `Jᵐ = Iᵐ ⊕ sI^(m-1) ⊕ ⋯ ⊕ sᵐA ⊕ s^(m+1)A ⊕ ⋯`.

```lean
theorem mem_pow_infinityChartIdeal_iff {I : Ideal A} {m : ℕ} {f : A[X]} :
    f ∈ infinityChartIdeal I ^ m ↔ ∀ j, f.coeff j ∈ I ^ (m - j)
```

**`Stacks.Chow.infinityChartMk_mem_fibreIdeal_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreNormalCone.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreNormalCone.lean#L386). The attribute's comment: “on D₊(S) the ideal (s) consists of the fractions p/s^N with p in J^(N+1)”.

> **`s` cuts the chart down to the associated graded ring.** The fraction `p/sᴺ` on the chart
> `A[s][J/s]` is divisible by `s` exactly when `p` lies in `J^(N+1)`.

```lean
theorem infinityChartMk_mem_fibreIdeal_iff {I : Ideal A} {N : ℕ} {q : A[X]}
    (hq : q ∈ infinityChartIdeal I ^ N) :
    infinityChartMk I N q hq ∈ infinityChartFibreIdeal I ↔
      q ∈ infinityChartIdeal I ^ (N + 1)
```

**`Stacks.Chow.conormalEquivInfinityChartFibre`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreNormalCone.lean, line 738](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreNormalCone.lean#L738). The attribute's comment: “the quotient of A[s][J/s] by s is the conormal algebra of I in A”.

> The quotient of the affine blowup algebra `A[s][J/s]`, `J = (I, s)`, by the element `s`
> cutting out the exceptional divisor is the conormal algebra `A/I ⊕ I/I² ⊕ I²/I³ ⊕ ⋯` of `I` in
> `A`.

```lean
def conormalEquivInfinityChartFibre (I : Ideal A) :
    AssociatedGraded.gradedRing I ≃+*
      (infinityChartAlgebra I ⧸ infinityChartFibreIdeal I)
```

**`Stacks.Chow.normalConeToExceptionalDivisor_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreNormalConeIso.lean, line 811](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreNormalConeIso.lean#L811). The attribute's comment: “E ∖ X' = E ∖ (X' ∩ E) = Spec_Z(C_{Z/X,*}) = C_ZX: an open immersion C_ZX → E with image E ∖ (X' ∩ E) = E ∖ X', over X”.

> Let `Z ⊆ X` be the closed subscheme of a quasi-coherent ideal `i.ker`, let `W` be the blowup
> of `𝐏¹_X` in `∞(Z)`, with exceptional divisor `E` and strict transform `X'` of `X`. Then
>
>   `E ∖ X' = E ∖ (X' ∩ E) = Spec_Z(𝒞_{Z/X,*}) = C_ZX`:
>
> the morphism `normalConeToExceptionalDivisor : C_ZX ⟶ E` is an open immersion whose image is
> `E ∖ (X' ∩ E)`, which is the inverse image `E ∖ X'` of `W ∖ X'`, and it is a morphism over `X`
> (so the identification is one of schemes over `Z`).

```lean
theorem normalConeToExceptionalDivisor_spec :
    IsOpenImmersion (normalConeToExceptionalDivisor i) ∧
      (normalConeToExceptionalDivisor i).opensRange =
        (strictTransformIdealOnExceptional i.ker).support.compl ∧
      (strictTransformIdealOnExceptional i.ker).support.compl =
        (exceptionalIdealAtInfinity i.ker).subschemeι ⁻¹ᵁ
          (strictTransformIdealAtInfinity i.ker).support.compl ∧
      normalConeToExceptionalDivisor i ≫ (exceptionalIdealAtInfinity i.ker).subschemeι ≫
          blowupAtInfinityToBase i.ker =
        Stacks.Conormal.normalConeToBase i ≫ i
```

**`Stacks.Chow.normalConeToFibreAtInfinity_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreNormalConeIso.lean, line 872](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreNormalConeIso.lean#L872). The attribute's comment: “the open immersion j : C_ZX → W_∞ of 0FBK: image W_∞ ∖ X', through E, over X”.

> The morphism `j : C_ZX ⟶ W_∞` of Stacks 0FBK is an open immersion with image `W_∞ ∖ X'`, it
> factors through the exceptional divisor as `C_ZX ≅ E ∖ X' ⊆ E`, and it lies over `X`:
> `C_ZX ⟶ W_∞ ⟶ X` is `C_ZX ⟶ Z ⟶ X`.

```lean
theorem normalConeToFibreAtInfinity_spec :
    IsOpenImmersion (normalConeToFibreAtInfinity i f) ∧
      (normalConeToFibreAtInfinity i f).opensRange =
        modificationFibreAtInfinityComplStrictTransform i.ker f ∧
      normalConeToFibreAtInfinity i f ≫
          modificationInclusionAtInfinity f (blowupAtInfinityToProjectiveLineProduct i.ker f) =
        normalConeToExceptionalDivisor i ≫ (exceptionalIdealAtInfinity i.ker).subschemeι ∧
      normalConeToFibreAtInfinity i f ≫
          modificationProjectionAtInfinity f (blowupAtInfinityToProjectiveLineProduct i.ker f) =
        Stacks.Conormal.normalConeToBase i ≫ i
```

## Tag 0FE9, an item

[Tag 0FE9](https://stacks.math.columbia.edu/tag/0FE9) in the Stacks Project.

**`Stacks.Chow.lineToBlowupAtInfinity_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreLineAtInfinity.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/InfinityCentreLineAtInfinity.lean#L233). The attribute's comment: “a closed immersion P¹_Z → W over P¹_X whose base change by ∞ is Z → C_ZX → E → W_∞, the first arrow the vertex of the cone”.

> Let `Z ⊆ X` be the closed subscheme of the closed immersion `i`, let `b : W ⟶ 𝐏¹_X` be the
> blowup of `𝐏¹_X` in `∞(Z)`, with exceptional divisor `E` and fibre at infinity `W_∞`. Then
> `lineToBlowupAtInfinity : 𝐏¹_Z ⟶ W` is a closed immersion, its composite with `b` is the
> inclusion `𝐏¹_Z ⟶ 𝐏¹_X`, and its base change by `∞` (along `W_∞ ⟶ W`, with `(𝐏¹_Z)_∞ = Z`) is
> the composite `Z ⟶ C_ZX ⟶ E ⟶ W_∞` of the vertex of the normal cone, the open immersion
> `C_ZX ⟶ E` and the inclusion `E ⊆ W_∞`.

```lean
theorem lineToBlowupAtInfinity_spec :
    IsClosedImmersion (lineToBlowupAtInfinity i.ker) ∧
      lineToBlowupAtInfinity i.ker ≫ blowupAtInfinityToLine i.ker =
        projectiveLineBaseChange i.ker.subschemeι ∧
      IsPullback (i.toImage ≫ lineInfinitySection i.ker.subscheme)
        (normalConeZeroSection i ≫ normalConeToExceptionalDivisor i ≫
          Scheme.IdealSheafData.inclusion
            (fibreIdealAtInfinity_le_exceptionalIdealAtInfinity i.ker))
        (lineToBlowupAtInfinity i.ker) (fibreIdealAtInfinity i.ker).subschemeι
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.53, Tag 0FBG](https://stacks.math.columbia.edu/tag/0FBG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
