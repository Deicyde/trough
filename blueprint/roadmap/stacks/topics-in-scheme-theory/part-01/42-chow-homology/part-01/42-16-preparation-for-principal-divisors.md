---
declaration: section
origin: cited
lean: Stacks.Chow.exists_primeDivisor_iff_codimension_one, Stacks.Chow.codimension_one_iff_schemeDeltaDimension, Stacks.Chow.deltaDimension_irreducibleComponent_isEffectiveCartierDivisor, AlgebraicGeometry.exists_isFinite_morphismRestrict_of_module_finite_functionField
statement: formalized
proof: formalized
---

# 42.16 Preparation for principal divisors

Section 42.16 of the Stacks Project, [Tag 02RI](https://stacks.math.columbia.edu/tag/02RI). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02RK, a lemma

[Tag 02RK](https://stacks.math.columbia.edu/tag/02RK) in the Stacks Project.

**`Stacks.Chow.exists_primeDivisor_iff_codimension_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/PrimeDivisorDimension.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/PrimeDivisorDimension.lean#L67). The attribute's comment: “prime_divisor_iff_delta_dimension”.

> **Stacks 02RK.** An integral closed subscheme of `X` is a prime divisor exactly when the
> closure of its generic point has codimension one in `X`. This is the definition of a prime
> divisor, read through the presentation of an integral closed subscheme by its ideal sheaf.

```lean
theorem exists_primeDivisor_iff_codimension_one {X : Scheme.{u}} (I : X.IdealSheafData)
    (hI : IsIntegral I.subscheme) :
    (∃ D : Stacks.Divisors.PrimeDivisor X, D.idealSheaf = I) ↔
      codimension (IrreducibleCloseds.closureSingleton (genericPointOf I hI)) = 1
```

**`Stacks.Chow.codimension_one_iff_schemeDeltaDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/PrimeDivisorDimension.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/PrimeDivisorDimension.lean#L98). The attribute's comment: “prime_divisor_iff_delta_dimension”.

> **Stacks 02RK.** An integral closed subscheme of an integral scheme `X` locally of finite
> type over the base has codimension one exactly when its delta-dimension is one less than that
> of `X`.

```lean
theorem codimension_one_iff_schemeDeltaDimension (C : ChowSituation.{u}) {X : Scheme.{u}}
    (f : X ⟶ C.S) [LocallyOfFiniteType f] [IsIntegral X] (I : X.IdealSheafData)
    (hI : IsIntegral I.subscheme) :
    codimension (IrreducibleCloseds.closureSingleton (genericPointOf I hI)) = 1 ↔
      schemeDeltaDimension C (I.subschemeι ≫ f) = schemeDeltaDimension C f + (-1 : ℤ)
```

**`Stacks.Chow.deltaDimension_irreducibleComponent_isEffectiveCartierDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/PrimeDivisorDimension.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/PrimeDivisorDimension.lean#L141). The attribute's comment: “cartier_component_delta_dimension”.

> **Stacks 02RK.** Every irreducible component of an effective Cartier divisor on an integral
> scheme locally of finite type over the base has delta-dimension one less than the ambient
> scheme.
>
> The generic point of such a component has ambient local ring of Krull dimension one, hence
> coheight one, which is exactly the hypothesis of
> `Stacks.Chow.deltaDimension_irreducibleComponent_of_coheight_eq_one`.

```lean
theorem deltaDimension_irreducibleComponent_isEffectiveCartierDivisor (C : ChowSituation.{u})
    {X : Scheme.{u}} (f : X ⟶ C.S) [LocallyOfFiniteType f] [IsIntegral X]
    (D : X.IdealSheafData) (hD : Stacks.Divisors.IsEffectiveCartierDivisor D)
    (Z : irreducibleComponents D.subscheme) :
    (deltaDimension C (D.subschemeι ≫ f)
        ⟨Z, Z.2.1, isClosed_of_mem_irreducibleComponents (Z : Set D.subscheme) Z.2⟩ : EInt) =
      schemeDeltaDimension C f + (-1 : ℤ)
```

## Tag 02RM, a lemma

[Tag 02RM](https://stacks.math.columbia.edu/tag/02RM) in the Stacks Project.

**`AlgebraicGeometry.exists_isFinite_morphismRestrict_of_module_finite_functionField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctionField/ProperFiniteCodimensionOne.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctionField/ProperFiniteCodimensionOne.lean#L52).

> **Stacks Project, Tag 02RM.** Let `f : X ⟶ Y` be a morphism of schemes and `ξ` a point of
> `Y`. Assume that `X` and `Y` are integral, that `Y` is locally Noetherian, that `f` is proper and
> dominant with `R(Y) ⊂ R(X)` finite, and that `dim (𝒪_{Y, ξ}) = 1`. Then there is an open
> neighbourhood `V` of `ξ` such that the restriction `f⁻¹(V) → V` is finite.

```lean
theorem exists_isFinite_morphismRestrict_of_module_finite_functionField
    {X Y : Scheme.{u}} (f : X ⟶ Y) (ξ : Y) [IsIntegral X] [IsIntegral Y]
    [IsLocallyNoetherian Y] [IsProper f] [IsDominant f]
    (hfin : letI := (functionFieldMap f).toAlgebra
      Module.Finite Y.functionField X.functionField)
    (hξ : ringKrullDim (Y.presheaf.stalk ξ) = 1) :
    ∃ V : Y.Opens, ξ ∈ V ∧ IsFinite (f ∣_ V)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.16, Tag 02RI](https://stacks.math.columbia.edu/tag/02RI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
