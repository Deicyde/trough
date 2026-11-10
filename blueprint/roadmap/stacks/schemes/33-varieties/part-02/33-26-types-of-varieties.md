---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsProperVariety, AlgebraicGeometry.IsSmoothVariety, AlgebraicGeometry.IsProjectiveVariety, AlgebraicGeometry.isProjectiveVariety_iff_isProjectiveMorphism, AlgebraicGeometry.isProjectiveVariety_iff_isProjective', AlgebraicGeometry.IsQuasiProjectiveVariety, AlgebraicGeometry.isQuasiProjectiveVariety_iff_isHQuasiProjective, AlgebraicGeometry.IsAffine
statement: formalized
proof: formalized
---

# 33.26 Types of varieties

Section 33.26 of the Stacks Project, [Tag 04L0](https://stacks.math.columbia.edu/tag/04L0). 2 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04L1, a definition

[Tag 04L1](https://stacks.math.columbia.edu/tag/04L1) in the Stacks Project.

**`AlgebraicGeometry.IsProperVariety`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Basic.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Basic.lean#L59). The attribute's comment: “proper_variety”.

> A variety over a field is proper when its structure morphism to the spectrum of the field
> is proper.

```lean
class IsProperVariety (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) : Prop
    extends IsVariety k f, IsProper f
```

**`AlgebraicGeometry.IsSmoothVariety`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Basic.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Basic.lean#L81). The attribute's comment: “smooth_variety”.

> A variety over a field is smooth when its structure morphism to the spectrum of the field
> is smooth.

```lean
class IsSmoothVariety (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) : Prop extends IsVariety k f, Smooth f
```

**`AlgebraicGeometry.IsProjectiveVariety`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Projective.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Projective.lean#L83). The attribute's comment: “projective_variety”.

> **Stacks Project, Tag 04L1.** A variety over a field is projective when its structure
> morphism to the spectrum of the field is H-projective, equivalently projective.

```lean
class IsProjectiveVariety (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) : Prop extends IsVariety k f
```

**`AlgebraicGeometry.isProjectiveVariety_iff_isProjectiveMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Projective.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Projective.lean#L99). The attribute's comment: “projective_variety_closed_subscheme”.

> **Stacks Project, Tag 04L1, clause (2), the form cited to [Stacks, Tag 01WB].** For a
> variety, being a projective variety is equivalent to H-projectivity of its structure morphism,
> that is, to `X` being isomorphic over `k` to a closed subscheme of `ℙⁿ_k` for some `n`.

```lean
theorem isProjectiveVariety_iff_isProjectiveMorphism (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsVariety k f] :
    IsProjectiveVariety k f ↔ IsProjectiveMorphism f
```

**`AlgebraicGeometry.isProjectiveVariety_iff_isProjective'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Projective.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Projective.lean#L112). The attribute's comment: “projective_variety_2”.

> **Stacks Project, Tag 04L1, clause (2).** A projective variety is exactly a variety whose
> structure morphism to the spectrum of the field is projective.
>
> The source defines the notion by projectivity of the structure morphism and observes, citing
> [Stacks, Tag 01WB], that it amounts to `X` being isomorphic to a closed subscheme of `ℙⁿ_k` for
> some `n`, which is the H-projectivity carried by the class. The two agree over the affine base
> `Spec k` by `AlgebraicGeometry.isProjective_iff_isProjectiveMorphism_of_isAffine`.

```lean
theorem isProjectiveVariety_iff_isProjective' (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) :
    IsProjectiveVariety k f ↔ IsVariety k f ∧ IsProjective f
```

**`AlgebraicGeometry.IsQuasiProjectiveVariety`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Projective.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Projective.lean#L134). The attribute's comment: “quasi_projective_variety”.

> **Stacks Project, Tag 04L1.** A variety over a field is quasi-projective when its structure
> morphism to the spectrum of the field is quasi-projective.

```lean
class IsQuasiProjectiveVariety (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) : Prop extends IsVariety k f
```

**`AlgebraicGeometry.isQuasiProjectiveVariety_iff_isHQuasiProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Projective.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Projective.lean#L162). The attribute's comment: “quasi_projective_variety_locally_closed_subscheme”.

> **Stacks Project, Tag 04L1, clause (3).** A quasi-projective variety is exactly a variety
> whose structure morphism is H-quasi-projective, that is, admits a quasi-compact immersion into
> `ℙⁿ_k` over `k` for some `n`, which realizes `X` as a locally closed subscheme of `ℙⁿ_k`.
>
> This is the identification the source records by citing [Stacks, Tag 01VZ]; over the affine base
> `Spec k` it is `AlgebraicGeometry.isQuasiProjective_iff_isHQuasiProjective_of_isAffine`.

```lean
theorem isQuasiProjectiveVariety_iff_isHQuasiProjective (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) :
    IsQuasiProjectiveVariety k f ↔ IsVariety k f ∧ IsHQuasiProjective f
```

Declarations registered for the tag:

- [`AlgebraicGeometry.IsAffine`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsAffine#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Basic.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Basic.lean#L53) (StacksFrontier): “affine_variety_2”. References: EGA I (1.7.1).

## Tag 04L2, a lemma

[Tag 04L2](https://stacks.math.columbia.edu/tag/04L2) in the Stacks Project.

**`AlgebraicGeometry.isSeparable_globalSections_of_isProperVariety`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/ProperVarietyGlobalSections.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/ProperVarietyGlobalSections.lean#L76). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 04L2, part (2).** For a geometrically reduced proper variety over a
> field `k`, the field of global functions is separable over `k`.

```lean
theorem isSeparable_globalSections_of_isProperVariety
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [IsProperVariety k f] [GeometricallyReduced f] :
    letI : Algebra k Γ(X, ⊤) := ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom.toAlgebra
    Algebra.IsSeparable k Γ(X, ⊤)
```

**`AlgebraicGeometry.isPurelyInseparable_globalSections_of_isProperVariety`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/ProperVarietyGlobalSections.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/ProperVarietyGlobalSections.lean#L94). The attribute's comment: “part (3)”.

> **Stacks Project, Tag 04L2, part (3).** For a geometrically irreducible proper variety over a
> field `k`, the field of global functions is purely inseparable over `k`.

```lean
theorem isPurelyInseparable_globalSections_of_isProperVariety
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [IsProperVariety k f] [GeometricallyIrreducible f] :
    letI : Algebra k Γ(X, ⊤) := ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom.toAlgebra
    IsPurelyInseparable k Γ(X, ⊤)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.isField_of_universallyClosed`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isField_of_universallyClosed#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/ProperVarietyGlobalSections.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/ProperVarietyGlobalSections.lean#L58) (StacksFrontier): “part (1), field”.
- [`AlgebraicGeometry.finite_appTop_of_universallyClosed`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.finite_appTop_of_universallyClosed#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/ProperVarietyGlobalSections.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/ProperVarietyGlobalSections.lean#L59) (StacksFrontier): “part (1), finite extension”.
- [`AlgebraicGeometry.isIso_globalSections_of_geometricallyIntegral`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ProperGlobalSections.lean#L85), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/ProperVarietyGlobalSections.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/ProperVarietyGlobalSections.lean#L108) (StacksFrontier): “part (4)”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.26, Tag 04L0](https://stacks.math.columbia.edu/tag/04L0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
