---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsRegularInCodimension, AlgebraicGeometry.HasPropertySk, AlgebraicGeometry.isRegular_iff_forall_isRegularInCodimension, AlgebraicGeometry.isCohenMacaulay_iff_forall_hasPropertySk, AlgebraicGeometry.isReduced_iff_hasPropertyS1_and_isRegularInCodimension_zero, AlgebraicGeometry.isNormal_iff_hasPropertySk_two_and_isRegularInCodimension_one, AlgebraicGeometry.isRegular_of_isNormal_of_topologicalKrullDim_le_one, AlgebraicGeometry.isCohenMacaulay_of_isNormal_of_topologicalKrullDim_le_two
statement: formalized
proof: formalized
---

# 28.12 Serre's conditions

Section 28.12 of the Stacks Project, [Tag 033P](https://stacks.math.columbia.edu/tag/033P). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 033Q, a definition

[Tag 033Q](https://stacks.math.columbia.edu/tag/033Q) in the Stacks Project.

**`AlgebraicGeometry.IsRegularInCodimension`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Serre.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Serre.lean#L76). The attribute's comment: “property\_rk”. References: EGA IV (5.8.2).

> A scheme is regular in codimension `k` (has property `(R_k)`) if each of its local rings of
> Krull dimension at most `k` is regular.

```lean
public abbrev IsRegularInCodimension (X : Scheme) (k : ℕ) : Prop
```

**`AlgebraicGeometry.HasPropertySk`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Serre.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Serre.lean#L83). The attribute's comment: “property\_sk”.

> Serre's property `(Sₖ)` for a locally Noetherian scheme: at every point, the depth of the
> local ring is at least the minimum of `k` and the dimension of that local ring.

```lean
def HasPropertySk (X : Scheme.{u}) [IsLocallyNoetherian X] (k : ℕ) : Prop
```

## Tag 0B3C, a lemma

[Tag 0B3C](https://stacks.math.columbia.edu/tag/0B3C) in the Stacks Project.

**`AlgebraicGeometry.isRegular_iff_forall_isRegularInCodimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/RegularCharacterization.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/RegularCharacterization.lean#L288).

> **Stacks Project, Tag 0B3C.** A locally Noetherian scheme is regular if and only if it is
> regular in codimension `k` for every nonnegative integer `k`.

```lean
theorem isRegular_iff_forall_isRegularInCodimension (X : Scheme.{u}) [IsLocallyNoetherian X] :
    IsRegular X ↔ ∀ k : ℕ, IsRegularInCodimension X k
```

## Tag 0342, a lemma

[Tag 0342](https://stacks.math.columbia.edu/tag/0342) in the Stacks Project.

**`AlgebraicGeometry.isCohenMacaulay_iff_forall_hasPropertySk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/CohenMacaulayCharacterization.lean, line 498](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/CohenMacaulayCharacterization.lean#L498).

> A locally Noetherian scheme is Cohen–Macaulay if and only if it satisfies Serre's condition
> `(Sₖ)` for every nonnegative integer `k`.

```lean
theorem isCohenMacaulay_iff_forall_hasPropertySk
    (X : Scheme.{u}) [IsLocallyNoetherian X] :
    IsCohenMacaulay X ↔ ∀ k : ℕ, HasPropertySk X k
```

## Tag 0344, a lemma

[Tag 0344](https://stacks.math.columbia.edu/tag/0344) in the Stacks Project.

**`AlgebraicGeometry.isReduced_iff_hasPropertyS1_and_isRegularInCodimension_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Serre.lean, line 281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Serre.lean#L281). References: EGA IV (5.8.5); EGA IV (7.3.9).

> A locally Noetherian scheme is reduced if and only if it satisfies Serre's conditions `(S₁)`
> and `(R₀)`.

```lean
public theorem isReduced_iff_hasPropertyS1_and_isRegularInCodimension_zero
    (X : Scheme.{u}) [IsLocallyNoetherian X] :
    IsReduced X ↔
      HasPropertySk X 1 ∧ IsRegularInCodimension X 0
```

## Tag 0345, a lemma

[Tag 0345](https://stacks.math.columbia.edu/tag/0345) in the Stacks Project.

**`AlgebraicGeometry.isNormal_iff_hasPropertySk_two_and_isRegularInCodimension_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Serre.lean, line 377](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Serre.lean#L377). References: EGA II (7.3.7), “partial”; EGA IV (5.8.6); EGA IV (7.3.9).

> **Serre's criterion for normality, Stacks Project, Tag 0345.** A locally Noetherian scheme is
> normal if and only if it satisfies Serre's condition `(S₂)` and is regular in codimension one.

```lean
public theorem isNormal_iff_hasPropertySk_two_and_isRegularInCodimension_one (X : Scheme.{u})
    [IsLocallyNoetherian X] :
    IsNormal X ↔ HasPropertySk X 2 ∧ IsRegularInCodimension X 1
```

## Tag 0BX2, a lemma

[Tag 0BX2](https://stacks.math.columbia.edu/tag/0BX2) in the Stacks Project.

**`AlgebraicGeometry.isRegular_of_isNormal_of_topologicalKrullDim_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/NormalRegular.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/NormalRegular.lean#L65). References: EGA IV (5.8.6), “(i), dim ≤ 1”.

> A locally Noetherian normal scheme of dimension at most one is regular.

```lean
public theorem isRegular_of_isNormal_of_topologicalKrullDim_le_one (X : Scheme.{u})
    [IsLocallyNoetherian X] [IsNormal X] (hX : topologicalKrullDim X ≤ 1) :
    IsRegular X
```

## Tag 0B3D, a lemma

[Tag 0B3D](https://stacks.math.columbia.edu/tag/0B3D) in the Stacks Project.

**`AlgebraicGeometry.isCohenMacaulay_of_isNormal_of_topologicalKrullDim_le_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/CohenMacaulayCharacterization.lean, line 517](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/CohenMacaulayCharacterization.lean#L517). References: EGA IV (5.8.6), “(ii), dim ≤ 2”.

> **Stacks Project, Tag 0B3D.** A locally Noetherian normal scheme of dimension at most two is
> Cohen–Macaulay.

```lean
theorem isCohenMacaulay_of_isNormal_of_topologicalKrullDim_le_two (X : Scheme.{u})
    [IsLocallyNoetherian X] [IsNormal X] (hX : topologicalKrullDim X ≤ 2) :
    IsCohenMacaulay X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.12, Tag 033P](https://stacks.math.columbia.edu/tag/033P)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
