---
declaration: section
origin: cited
lean: AlgebraicGeometry.isUniversallyPureRelative_of_support_isProperOver, AlgebraicGeometry.isUniversallyPureRelative_of_isProper, AlgebraicGeometry.isSchemeUniversallyPureRelative_of_isProper, AlgebraicGeometry.isPureRelative_iff_isFinite_schemeTheoreticSupport, AlgebraicGeometry.isUniversallyPureRelative_iff_isFinite_schemeTheoreticSupport, AlgebraicGeometry.isSchemePureRelative_iff_isFinite, AlgebraicGeometry.universallyPure_of_flat_geometricallyIntegral, AlgebraicGeometry.isUniversallyPureRelative_of_pushforward_isLocallyProjective
statement: formalized
proof: formalized
---

# 38.17 Examples of relatively pure sheaves

Section 38.17 of the Stacks Project, [Tag 05K2](https://stacks.math.columbia.edu/tag/05K2). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05K3, a lemma

[Tag 05K3](https://stacks.math.columbia.edu/tag/05K3) in the Stacks Project.

**`AlgebraicGeometry.isUniversallyPureRelative_of_support_isProperOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/ProperSupport.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/ProperSupport.lean#L116). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 05K3, part (1).** A finite type quasi-coherent module whose support is
> proper over the base is universally pure relative to that base.

```lean
theorem isUniversallyPureRelative_of_support_isProperOver {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [QuasiCompact f] (F : X.Modules) [F.IsFiniteType]
    [F.IsQuasicoherent]
    (hF : IsProperOver f (⟨SheafOfModules.supp F, SheafOfModules.isClosed_supp F⟩ : Closeds X)) :
    IsUniversallyPureRelative f F
```

**`AlgebraicGeometry.isUniversallyPureRelative_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/ProperSupport.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/ProperSupport.lean#L154). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 05K3, part (2).** A finite type quasi-coherent module on a scheme which
> is proper over the base is universally pure relative to that base.

```lean
theorem isUniversallyPureRelative_of_isProper {X S : Scheme.{u}} (f : X ⟶ S) [IsProper f]
    (F : X.Modules) [F.IsFiniteType] [F.IsQuasicoherent] :
    IsUniversallyPureRelative f F
```

**`AlgebraicGeometry.isSchemeUniversallyPureRelative_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/ProperSupport.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/ProperSupport.lean#L164). The attribute's comment: “part (3)”.

> **Stacks Project, Tag 05K3, part (3).** A proper scheme is universally pure over its base.

```lean
theorem isSchemeUniversallyPureRelative_of_isProper {X S : Scheme.{u}} (f : X ⟶ S) [IsProper f] :
    @IsUniversallyPureRelative.{u} X S f _ _ (SheafOfModules.unit.{u} X.ringCatSheaf)
      (structureSheaf_isFiniteType X)
      (Stacks.AlgebraicGeometry.AffineQcohPushforward.isQuasicoherent_unit X)
```

## Tag 05K4, a lemma

[Tag 05K4](https://stacks.math.columbia.edu/tag/05K4) in the Stacks Project.

**`AlgebraicGeometry.isPureRelative_iff_isFinite_schemeTheoreticSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/FiniteSupport.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/FiniteSupport.lean#L363). The attribute's comment: “conditions (1) and (2)”.

> **Stacks Project, Tag 05K4, conditions (1) and (2).** Let `f : X ⟶ S` be separated of finite
> type and let `ℱ` be a finite type quasi-coherent `𝒪_X`-module with finite support on every fibre
> of `f`. Then `ℱ` is pure relative to `S` if and only if its scheme-theoretic support is finite
> over `S`.

```lean
theorem isPureRelative_iff_isFinite_schemeTheoreticSupport {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [QuasiCompact f] [IsSeparated f] (F : X.Modules) [F.IsFiniteType]
    [F.IsQuasicoherent]
    (hfinite : ∀ s : S,
      (SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι s)).obj F)).Finite) :
    IsPureRelative f F ↔
      IsFinite ((Scheme.Modules.schemeTheoreticSupport F).subschemeι ≫ f)
```

**`AlgebraicGeometry.isUniversallyPureRelative_iff_isFinite_schemeTheoreticSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/FiniteSupport.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/FiniteSupport.lean#L400). The attribute's comment: “conditions (2) and (3)”.

> **Stacks Project, Tag 05K4, conditions (2) and (3).** Let `f : X ⟶ S` be separated of finite
> type and let `ℱ` be a finite type quasi-coherent `𝒪_X`-module with finite support on every fibre
> of `f`. Then `ℱ` is universally pure relative to `S` if and only if its scheme-theoretic support
> is finite over `S`.

```lean
theorem isUniversallyPureRelative_iff_isFinite_schemeTheoreticSupport {X S : Scheme.{u}}
    (f : X ⟶ S) [LocallyOfFiniteType f] [QuasiCompact f] [IsSeparated f] (F : X.Modules)
    [F.IsFiniteType] [F.IsQuasicoherent]
    (hfinite : ∀ s : S,
      (SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι s)).obj F)).Finite) :
    IsUniversallyPureRelative f F ↔
      IsFinite ((Scheme.Modules.schemeTheoreticSupport F).subschemeι ≫ f)
```

**`AlgebraicGeometry.isSchemePureRelative_iff_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/FiniteSupport.lean, line 414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/FiniteSupport.lean#L414). The attribute's comment: “in particular: quasi-finite separated morphisms”.

> **Stacks Project, Tag 05K4, in particular.** A separated quasi-finite scheme over `S` is pure
> relative to `S` if and only if its structure morphism is finite.

```lean
theorem isSchemePureRelative_iff_isFinite {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [QuasiCompact f] [LocallyQuasiFinite f] [IsSeparated f] :
    IsSchemePureRelative f ↔ IsFinite f
```

## Tag 05K5, a lemma

[Tag 05K5](https://stacks.math.columbia.edu/tag/05K5) in the Stacks Project.

**`AlgebraicGeometry.universallyPure_of_flat_geometricallyIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/GeometricallyIntegralFibres.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/GeometricallyIntegralFibres.lean#L67).

> **Stacks Project, Tag 05K5.** A flat finite type morphism with geometrically integral
> fibres has universally pure structure sheaf over its base.

```lean
theorem universallyPure_of_flat_geometricallyIntegral {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [QuasiCompact f] [Flat f] [GeometricallyIntegral f] :
    @IsUniversallyPureRelative.{u} X S f _ _
      (SheafOfModules.unit.{u} X.ringCatSheaf)
      (structureSheaf_isFiniteType X)
      (Stacks.AlgebraicGeometry.AffineQcohPushforward.isQuasicoherent_unit X)
```

## Tag 05K6, a lemma

[Tag 05K6](https://stacks.math.columbia.edu/tag/05K6) in the Stacks Project.

**`AlgebraicGeometry.isUniversallyPureRelative_of_pushforward_isLocallyProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/LocallyProjectivePurity.lean, line 788](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/LocallyProjectivePurity.lean#L788).

> **Stacks Project, Tag 05K6.** For an affine morphism of finite type, a finite type
> quasi-coherent module with locally projective direct image is universally pure over the base.
>
> The affine base change used along the way is the third assertion of Stacks Tag 02KG,
> `Stacks.AlgebraicGeometry.AffineBaseChangeLocality.baseChangeIso`, bound to `bc` below and
> threaded through the private lemmas in the shape in which they take it.

```lean
public theorem isUniversallyPureRelative_of_pushforward_isLocallyProjective
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] [IsAffineHom f]
    (F : X.Modules) [F.IsFiniteType] [F.IsQuasicoherent]
    (hF : Scheme.Modules.IsLocallyProjective ((Scheme.Modules.pushforward f).obj F)) :
    IsUniversallyPureRelative f F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.17, Tag 05K2](https://stacks.math.columbia.edu/tag/05K2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
