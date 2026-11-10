---
declaration: section
origin: cited
lean: Stacks.Chow.properPushforward_principalDivisorCycle, Stacks.Chow.lineZeroDivisor, Stacks.Chow.lineInfinityDivisor, Stacks.Chow.zeroScheme_lineZeroDivisor, Stacks.Chow.zeroScheme_lineInfinityDivisor, Stacks.Chow.isTrivial_pullback_divisorSheaf_lineZeroDivisor, Stacks.Chow.isTrivial_pullback_divisorSheaf_lineInfinityDivisor, Stacks.Chow.graphProjection_isProper
statement: formalized
proof: formalized
---

# 42.18 Principal divisors and pushforward

Section 42.18 of the Stacks Project, [Tag 02RS](https://stacks.math.columbia.edu/tag/02RS). 4 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02RT, a lemma

[Tag 02RT](https://stacks.math.columbia.edu/tag/02RT) in the Stacks Project.

**`Stacks.Chow.properPushforward_principalDivisorCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PrincipalDivisorPushforward.lean, line 802](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/PrincipalDivisorPushforward.lean#L802).

> **Stacks 02RT.** For a dominant proper morphism `p : X ⟶ Y` of integral schemes locally of
> finite type over the base with `dim_δ(X) = dim_δ(Y) = n`, the proper pushforward of the principal
> divisor of a nonzero rational function `f` on `X` is the principal divisor of the norm of `f` in
> the extension `R(Y) ⊆ R(X)` of function fields.

```lean
theorem properPushforward_principalDivisorCycle (C : ChowSituation.{u}) {X Y : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    [IsIntegral X] [IsIntegral Y] {n : ℤ}
    (hnX : schemeDeltaDimension C sX = (n : EInt))
    (hnY : schemeDeltaDimension C sY = (n : EInt))
    (p : X ⟶ Y) [IsProper p] [IsDominant p] (hp : p ≫ sY = sX)
    (f : X.functionField) (hf : f ≠ 0) :
    letI : Algebra Y.functionField X.functionField := (dominantFunctionFieldMap p).toAlgebra
    properPushforward C sX sY p hp (n - 1) (principalDivisorCycle C sX hnX f) =
      principalDivisorCycle C sY hnY (Algebra.norm Y.functionField f)
```

## Tag 0F93, an equation

[Tag 0F93](https://stacks.math.columbia.edu/tag/0F93) in the Stacks Project.

**`Stacks.Chow.lineZeroDivisor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisor.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisor.lean#L303). The attribute's comment: “the divisor D₀ ⊆ ℙ¹_S”.

> The zero divisor `D₀ ⊆ ℙ¹_S`: the closed subscheme cut out by the kernel ideal sheaf of
> the zero section, equivalently the scheme-theoretic image of that section.

```lean
def lineZeroDivisor (S : Scheme.{u}) : (relativeProjectiveLine S).IdealSheafData
```

**`Stacks.Chow.lineInfinityDivisor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisor.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisor.lean#L309). The attribute's comment: “the divisor D₀ ⊆ ℙ¹_S”.

> The infinity divisor `D_∞ ⊆ ℙ¹_S`: the closed subscheme cut out by the kernel ideal sheaf
> of the infinity section.

```lean
def lineInfinityDivisor (S : Scheme.{u}) : (relativeProjectiveLine S).IdealSheafData
```

**`Stacks.Chow.zeroScheme_lineZeroDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisor/SectionPresentation.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisor/SectionPresentation.lean#L68). The attribute's comment: “D₀ is the zero scheme of a global section of an invertible module”.

> **Stacks 0F93, the zero divisor as a zero scheme.** `D₀ ⊆ ℙ¹_S` is the zero scheme of a
> global section of an invertible module, namely of the canonical section `1_{D₀}` of
> `𝒪(D₀)`.

```lean
theorem zeroScheme_lineZeroDivisor (S : Scheme.{u}) :
    Stacks.Divisors.zeroScheme (relativeProjectiveLine S)
        (Stacks.Divisors.divisorSheaf (lineZeroDivisor S))
        (Stacks.Divisors.divisorSheafGlobalSection (lineZeroDivisor S)) =
      lineZeroDivisor S
```

**`Stacks.Chow.zeroScheme_lineInfinityDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisor/SectionPresentation.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisor/SectionPresentation.lean#L79). The attribute's comment: “D_∞ is the zero scheme of a global section of an invertible module”.

> **Stacks 0F93, the infinity divisor as a zero scheme.** `D_∞ ⊆ ℙ¹_S` is the zero scheme of a
> global section of an invertible module, namely of the canonical section `1_{D_∞}` of
> `𝒪(D_∞)`.

```lean
theorem zeroScheme_lineInfinityDivisor (S : Scheme.{u}) :
    Stacks.Divisors.zeroScheme (relativeProjectiveLine S)
        (Stacks.Divisors.divisorSheaf (lineInfinityDivisor S))
        (Stacks.Divisors.divisorSheafGlobalSection (lineInfinityDivisor S)) =
      lineInfinityDivisor S
```

**`Stacks.Chow.isTrivial_pullback_divisorSheaf_lineZeroDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisor/SectionPresentation.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisor/SectionPresentation.lean#L224). The attribute's comment: “the normal bundle of D₀ is trivial”.

> **Stacks 0F93, the trivial normal bundle of `D₀`.** The invertible module `𝒪(D₀)` restricts
> trivially to `D₀`: the support of `D₀` lies in the chart `𝔸¹_S`, where `D₀` is cut out by the
> coordinate, a regular global function.

```lean
theorem isTrivial_pullback_divisorSheaf_lineZeroDivisor (S : Scheme.{u}) :
    AlgebraicGeometry.SheafOfModules.IsTrivial
      (lineZeroDivisor S).subscheme.sheaf.obj (lineZeroDivisor S).subscheme.ringCatSheaf.property
      ((Scheme.Modules.pullback (lineZeroDivisor S).subschemeι).obj
        (Stacks.Divisors.divisorSheaf (lineZeroDivisor S)))
```

**`Stacks.Chow.isTrivial_pullback_divisorSheaf_lineInfinityDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisor/SectionPresentation.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisor/SectionPresentation.lean#L238). The attribute's comment: “the normal bundle of D_∞ is trivial”.

> **Stacks 0F93, the trivial normal bundle of `D_∞`.** The invertible module `𝒪(D_∞)`
> restricts trivially to `D_∞`: the support of `D_∞` lies in the second chart, where `D_∞` is cut
> out by the coordinate of that chart, a regular global function.

```lean
theorem isTrivial_pullback_divisorSheaf_lineInfinityDivisor (S : Scheme.{u}) :
    AlgebraicGeometry.SheafOfModules.IsTrivial
      (lineInfinityDivisor S).subscheme.sheaf.obj
      (lineInfinityDivisor S).subscheme.ringCatSheaf.property
      ((Scheme.Modules.pullback (lineInfinityDivisor S).subschemeι).obj
        (Stacks.Divisors.divisorSheaf (lineInfinityDivisor S)))
```

## Tag 02RQ, a lemma

[Tag 02RQ](https://stacks.math.columbia.edu/tag/02RQ) in the Stacks Project.

**`Stacks.Chow.graphProjection_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisor.lean, line 516](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisor.lean#L516). The attribute's comment: “part (1): properness of the projection”.

> **Part (1) of Stacks Project, Tag 02RQ.** The projection `p : Y ⟶ X` is proper. No
> hypothesis on `X`, on `U` or on the section is needed: `Y` is closed in `X ×_S ℙ¹_S`, which is
> proper over `X`.

```lean
theorem graphProjection_isProper {X S : Scheme.{u}} (sX : X ⟶ S) (U : X.Opens)
    (s : Γ(X, U)) : IsProper (graphProjection sX U s)
```

**`Stacks.Chow.isIso_graphProjection_morphismRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisorCycles/GraphConstruction.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisorCycles/GraphConstruction.lean#L95). The attribute's comment: “part (2)”.

> **Part (2) of Stacks Project, Tag 02RQ.** The restriction `p|_{p⁻¹(U)} : p⁻¹(U) ⟶ U` of the
> projection `p : Y ⟶ X` is an isomorphism.

```lean
theorem isIso_graphProjection_morphismRestrict (U : X.Opens) (s : Γ(X, U)) :
    IsIso (graphProjection sX U s ∣_ U)
```

**`Stacks.Chow.isPullbackDefined_graphFibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisorCycles/GraphConstruction.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisorCycles/GraphConstruction.lean#L105). The attribute's comment: “part (3)”.

> **Part (3) of Stacks Project, Tag 02RQ.** The pullbacks `Y₀ = q⁻¹D₀` and `Y_∞ = q⁻¹D_∞` of
> the zero and infinity divisors of `ℙ¹_S` along `q : Y ⟶ ℙ¹_S` are defined.

```lean
theorem isPullbackDefined_graphFibres [IsIntegral X] (U : X.Opens) [Nonempty U.toScheme]
    (g : (Γ(X, U))ˣ) :
    Stacks.Divisors.IsPullbackDefined (graphLineProjection sX U ↑g) (lineZeroDivisor C.S) ∧
      Stacks.Divisors.IsPullbackDefined (graphLineProjection sX U ↑g)
        (lineInfinityDivisor C.S)
```

**`Stacks.Chow.principalDivisorCycle_graphClosure_eq_fibreCycles_sub`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisorCycles/GraphConstruction.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisorCycles/GraphConstruction.lean#L120). The attribute's comment: “part (4)”.

> **Part (4) of Stacks Project, Tag 02RQ.** On `Y`, the principal divisor of the rational
> function `f` is the difference `[Y₀]_{n-1} - [Y_∞]_{n-1}` of the cycles of the two fibres.
>
> Here `f` on `Y` is the pullback of the invertible section `g` to the dense open `p⁻¹(U)`, carried
> to the function field by `Stacks.Chow.rationalFunctionsEquivFunctionField`.

```lean
theorem principalDivisorCycle_graphClosure_eq_fibreCycles_sub [IsIntegral X] (n : ℤ)
    (dimX : schemeDeltaDimension C sX = (n : EInt)) (U : X.Opens) [Nonempty U.toScheme]
    (g : (Γ(X, U))ˣ) :
    principalDivisorCycle C (graphBaseMorphism sX U ↑g)
        (schemeDeltaDimension_graphClosure_of_chowSituation C sX n dimX U g)
        ((rationalFunctionsEquivFunctionField (graphClosure sX U ↑g)).1
          ↑(graphRationalFunction sX U g (graphPreimageDense_of_chowSituation C sX U ↑g))) =
      cycleAssociatedToClosedSubscheme C (graphBaseMorphism sX U ↑g)
          (graphZeroFiber sX U ↑g).subschemeι (n - 1) -
        cycleAssociatedToClosedSubscheme C (graphBaseMorphism sX U ↑g)
          (graphInfinityFiber sX U ↑g).subschemeι (n - 1)
```

**`Stacks.Chow.principalDivisorCycle_eq_properPushforward_graphClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisorCycles/GraphConstruction.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisorCycles/GraphConstruction.lean#L137). The attribute's comment: “part (5)”.

> **Part (5) of Stacks Project, Tag 02RQ.** The principal divisor of `f` on `X` is the proper
> pushforward along `p : Y ⟶ X` of the principal divisor of `f` on `Y`.

```lean
theorem principalDivisorCycle_eq_properPushforward_graphClosure [IsIntegral X] (n : ℤ)
    (dimX : schemeDeltaDimension C sX = (n : EInt)) (f : (rationalFunctions X)ˣ) (U : X.Opens)
    [Nonempty U.toScheme] (g : (Γ(X, U))ˣ)
    (f_eq : ofSection X ⟨U, dense_opens_of_nonempty U⟩ ↑g = (f : rationalFunctions X)) :
    principalDivisorCycle C sX dimX ((rationalFunctionsEquivFunctionField X).1 ↑f) =
      properPushforward C (graphBaseMorphism sX U ↑g) sX (graphProjection sX U ↑g) rfl (n - 1)
        (principalDivisorCycle C (graphBaseMorphism sX U ↑g)
          (schemeDeltaDimension_graphClosure_of_chowSituation C sX n dimX U g)
          ((rationalFunctionsEquivFunctionField (graphClosure sX U ↑g)).1
            ↑(graphRationalFunction sX U g (graphPreimageDense_of_chowSituation C sX U ↑g))))
```

**`Stacks.Chow.principalDivisorCycle_eq_imageFibreCycles_sub`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisorCycles/GraphConstruction.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/UniversalPrincipalDivisorCycles/GraphConstruction.lean#L153). The attribute's comment: “part (6)”.

> **Part (6) of Stacks Project, Tag 02RQ.** Viewing `Y₀` and `Y_∞` as closed subschemes of `X`
> through `p : Y ⟶ X`, the principal divisor of `f` on `X` is `[Y₀]_{n-1} - [Y_∞]_{n-1}`.

```lean
theorem principalDivisorCycle_eq_imageFibreCycles_sub [IsIntegral X] (n : ℤ)
    (dimX : schemeDeltaDimension C sX = (n : EInt)) (f : (rationalFunctions X)ˣ) (U : X.Opens)
    [Nonempty U.toScheme] (g : (Γ(X, U))ˣ)
    (f_eq : ofSection X ⟨U, dense_opens_of_nonempty U⟩ ↑g = (f : rationalFunctions X)) :
    principalDivisorCycle C sX dimX ((rationalFunctionsEquivFunctionField X).1 ↑f) =
      cycleAssociatedToClosedSubscheme C sX
          ((graphZeroFiber sX U ↑g).subschemeι ≫ graphProjection sX U ↑g) (n - 1) -
        cycleAssociatedToClosedSubscheme C sX
          ((graphInfinityFiber sX U ↑g).subschemeι ≫ graphProjection sX U ↑g) (n - 1)
```

## Tag 02RU, a lemma

[Tag 02RU](https://stacks.math.columbia.edu/tag/02RU) in the Stacks Project.

**`Stacks.Chow.properPushforward_principalDivisorCycle_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProjectiveLineDivisorDegree/ProperCurve.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ProjectiveLineDivisorDegree/ProperCurve.lean#L41). The attribute's comment: “pushforward of the principal divisor”.

> **The degree of a principal divisor on a proper curve over a field vanishes.** For a Chow
> situation whose base is the spectrum of a field with vanishing dimension function, a proper
> integral `X` of delta-dimension one over that base, and an invertible rational function `f` on `X`,
> the proper pushforward of `div(f)` to the base is zero.

```lean
theorem properPushforward_principalDivisorCycle_eq_zero
    (k : Type u) [Field k] (C : ChowSituation.{u})
    (hS : C.S = AlgebraicGeometry.Spec (.of k))
    (hδ : ∀ p : C.S, C.dimensionFunction p = 0)
    {X : Scheme.{u}} (c : X ⟶ C.S) [IsProper c] [IsIntegral X]
    (hdim : schemeDeltaDimension C c = (1 : EInt))
    (f : (rationalFunctions X)ˣ) :
    properPushforward C c (𝟙 C.S) c (by simp) 0
      (principalDivisorCycle C c hdim ((rationalFunctionsEquivFunctionField X).1 ↑f)) = 0
```

**`Stacks.Chow.principalDivisorDegree_eq_zero_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProjectiveLineDivisorDegree/ProperCurve.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ProjectiveLineDivisorDegree/ProperCurve.lean#L62). The attribute's comment: “displayed-sum form”.

> **Stacks 02RU in the displayed-sum form.** For a proper integral curve over a field the
> weighted sum `∑_x ord_x(f) · [κ(x) : k]` of the orders of vanishing of an invertible rational
> function vanishes. This is the other form of
> `Stacks.Chow.properPushforward_principalDivisorCycle_eq_zero`, the two being identified by
> `Stacks.Chow.properPushforward_principalDivisorCycle_eq_zero_iff`.

```lean
theorem principalDivisorDegree_eq_zero_of_isProper
    (k : Type u) [Field k] (C : ChowSituation.{u})
    (hS : C.S = AlgebraicGeometry.Spec (.of k))
    (hδ : ∀ p : C.S, C.dimensionFunction p = 0)
    {X : Scheme.{u}} (c : X ⟶ C.S) [IsProper c] [IsIntegral X] [IsLocallyNoetherian X]
    (hdim : schemeDeltaDimension C c = (1 : EInt))
    (f : (rationalFunctions X)ˣ) :
    principalDivisorDegree c ((rationalFunctionsEquivFunctionField X).1 ↑f) = 0
```

**`Stacks.Chow.principalDivisorDegree_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardPrincipal/NormalizationDescent.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardPrincipal/NormalizationDescent.lean#L163). The attribute's comment: “the displayed sum”.

> **Stacks Project, Tag 02RU.** Let `X` be an integral scheme of dimension one, proper over a
> field `k`. Then the degree of the principal divisor of a nonzero rational function `f` on `X`
> vanishes:
>
>   `∑_{x ∈ X} ord_x(f) · [κ(x) : k] = 0`.
>
> The normalization `ν : X^ν ⟶ X` is a proper dominant birational morphism from a normal curve, so
> the normal case applies to the image `F` of `f` in `R(X^ν)`, and the norm formula of Stacks 02RT
> identifies `deg div_{X^ν}(F)` with `deg div_X(Nm(F)) = deg div_X(f)`.

```lean
theorem principalDivisorDegree_eq_zero (k : Type u) [Field k] (X : Scheme.{u})
    [X.Over (AlgebraicGeometry.Spec (.of k))]
    [IsCurve k (X ↘ AlgebraicGeometry.Spec (.of k))]
    [IsProper (X ↘ AlgebraicGeometry.Spec (.of k))] [IsLocallyNoetherian X]
    (f : X.functionField) (hf : f ≠ 0) :
    principalDivisorDegree (X ↘ AlgebraicGeometry.Spec (.of k)) f = 0
```

**`Stacks.Chow.properPushforward_principalDivisorCycle_eq_zero_of_isCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardPrincipal/NormalizationDescent.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardPrincipal/NormalizationDescent.lean#L219). The attribute's comment: “the pushforward of the principal divisor”.

> **Stacks Project, Tag 02RU**, in its cycle form: the proper pushforward to `Spec k` of the
> principal divisor of a nonzero rational function on a proper integral curve vanishes.

```lean
theorem properPushforward_principalDivisorCycle_eq_zero_of_isCurve (k : Type u) [Field k]
    (X : Scheme.{u}) [X.Over (AlgebraicGeometry.Spec (.of k))]
    [IsCurve k (X ↘ AlgebraicGeometry.Spec (.of k))]
    [IsProper (X ↘ AlgebraicGeometry.Spec (.of k))] [IsLocallyNoetherian X]
    (c : X ⟶ (fieldChowSituation k).S) [IsProper c]
    (hc : c = X ↘ AlgebraicGeometry.Spec (.of k))
    (hdim : schemeDeltaDimension (fieldChowSituation k) c = ((1 : ℤ) : EInt))
    (f : X.functionField) (hf : f ≠ 0) :
    properPushforward (fieldChowSituation k) c (𝟙 (fieldChowSituation k).S) c
        (Category.comp_id c) 0
      (principalDivisorCycle (fieldChowSituation k) c hdim f) = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.18, Tag 02RS](https://stacks.math.columbia.edu/tag/02RS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
