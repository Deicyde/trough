---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.IsUniversallyCatenary, AlgebraicGeometry.Scheme.isUniversallyCatenary_of_locallyOfFiniteType, AlgebraicGeometry.Scheme.isUniversallyCatenary_tfae, AlgebraicGeometry.Scheme.isUniversallyCatenary_iff_stalk_isUniversallyCatenary, AlgebraicGeometry.Scheme.isUniversallyCatenary_iff_irreducibleComponents, AlgebraicGeometry.Scheme.isUniversallyCatenary_of_locallyOfFiniteType_over_field, AlgebraicGeometry.Scheme.isUniversallyCatenary_of_locallyOfFiniteType_over_isCohenMacaulay, AlgebraicGeometry.Scheme.isUniversallyCatenary_of_locallyOfFiniteType_over_int
statement: formalized
proof: formalized
---

# 29.17 Universally catenary schemes

Section 29.17 of the Stacks Project, [Tag 02J7](https://stacks.math.columbia.edu/tag/02J7). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02J8, a definition

[Tag 02J8](https://stacks.math.columbia.edu/tag/02J8) in the Stacks Project.

**`AlgebraicGeometry.Scheme.IsUniversallyCatenary`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/UniversallyCatenary.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/UniversallyCatenary.lean#L56).

> A locally Noetherian scheme `S` is **universally catenary** if every scheme locally of
> finite type over `S` is catenary.

```lean
def IsUniversallyCatenary (S : Scheme.{u}) [IsLocallyNoetherian S] : Prop
```

## Tag 02J9, a lemma

[Tag 02J9](https://stacks.math.columbia.edu/tag/02J9) in the Stacks Project.

**`AlgebraicGeometry.Scheme.isUniversallyCatenary_of_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/UniversallyCatenary.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/UniversallyCatenary.lean#L75). The attribute's comment: “inheritance”. References: EGA IV (10.6.1), “(i), condition 2° for X”.

> A scheme locally of finite type over a locally Noetherian universally catenary scheme is
> universally catenary.

```lean
theorem isUniversallyCatenary_of_locallyOfFiniteType
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] [IsLocallyNoetherian S]
    (hS : IsUniversallyCatenary S) :
    @IsUniversallyCatenary X
      (AlgebraicGeometry.LocallyOfFiniteType.isLocallyNoetherian f)
```

**`AlgebraicGeometry.Scheme.isUniversallyCatenary_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RecoveryCatenary/LocalCriteria.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RecoveryCatenary/LocalCriteria.lean#L44). The attribute's comment: “local\_criteria”.

> For a locally Noetherian scheme, universal catenarity is equivalent to holding on an open
> covering, to universal catenarity of the ring of sections over every affine open, and to that
> ring-theoretic condition holding over the members of one affine open covering.

```lean
theorem isUniversallyCatenary_tfae (S : Scheme.{u}) [IsLocallyNoetherian S] :
    List.TFAE [
      IsUniversallyCatenary S,
      ∃ (ι : Type u) (U : ι → S.Opens),
        IsOpenCover U ∧ ∀ i, IsUniversallyCatenary (U i).toScheme,
      ∀ U : S.affineOpens, Ring.IsUniversallyCatenary Γ(S, U),
      ∃ (ι : Type u) (U : ι → S.affineOpens),
        IsOpenCover (fun i ↦ (U i : S.Opens)) ∧
          ∀ i, Ring.IsUniversallyCatenary Γ(S, U i)]
```

## Tag 02JA, a lemma

[Tag 02JA](https://stacks.math.columbia.edu/tag/02JA) in the Stacks Project.

**`AlgebraicGeometry.Scheme.isUniversallyCatenary_iff_stalk_isUniversallyCatenary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RecoveryCatenary/Stalk.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RecoveryCatenary/Stalk.lean#L110). References: EGA IV (5.6.3).

> A locally Noetherian scheme is universally catenary if and only if each of its local rings
> is universally catenary.

```lean
theorem isUniversallyCatenary_iff_stalk_isUniversallyCatenary
    (S : Scheme.{u}) [IsLocallyNoetherian S] :
    IsUniversallyCatenary S ↔
      ∀ s : S, Ring.IsUniversallyCatenary (S.presheaf.stalk s)
```

## Tag 0G42, a lemma

[Tag 0G42](https://stacks.math.columbia.edu/tag/0G42) in the Stacks Project.

**`AlgebraicGeometry.Scheme.isUniversallyCatenary_iff_irreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RecoveryCatenary/IrreducibleComponents.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RecoveryCatenary/IrreducibleComponents.lean#L92).

> A locally Noetherian scheme is universally catenary if and only if its reduced
> irreducible components are universally catenary.

```lean
theorem isUniversallyCatenary_iff_irreducibleComponents
    (S : Scheme.{u}) [IsLocallyNoetherian S] :
    IsUniversallyCatenary S ↔
      ∀ Z : irreducibleComponents S,
        let I : S.IdealSheafData := Scheme.IdealSheafData.vanishingIdeal
          ⟨Z.1, isClosed_of_mem_irreducibleComponents Z.1 Z.2⟩
        let : IsLocallyNoetherian I.subscheme :=
          LocallyOfFiniteType.isLocallyNoetherian I.subschemeι
        IsUniversallyCatenary I.subscheme
```

## Tag 02JB, a lemma

[Tag 02JB](https://stacks.math.columbia.edu/tag/02JB) in the Stacks Project.

**`AlgebraicGeometry.Scheme.isUniversallyCatenary_of_locallyOfFiniteType_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/UniversallyCatenaryExamples.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/UniversallyCatenaryExamples.lean#L217). The attribute's comment: “part (1)”. References: EGA IV (10.7.1), “2° over a field”.

> **Stacks Project, Tag 02JB, part (1).** A scheme locally of finite type over a field is
> universally catenary.

```lean
theorem isUniversallyCatenary_of_locallyOfFiniteType_over_field (k : Type u) [Field k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f] :
    @IsUniversallyCatenary X (LocallyOfFiniteType.isLocallyNoetherian f)
```

**`AlgebraicGeometry.Scheme.isUniversallyCatenary_of_locallyOfFiniteType_over_isCohenMacaulay`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/UniversallyCatenaryExamples.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/UniversallyCatenaryExamples.lean#L229). The attribute's comment: “part (2)”. References: EGA IV (10.6.1), “(i), special case”; EGA IV (10.7.1), “more general”; EGA IV (5.2.5), “more general”; SGA 6 X (1.5), “more general”.

> **Stacks Project, Tag 02JB, part (2).** A scheme locally of finite type over a locally
> Noetherian Cohen–Macaulay scheme is universally catenary.

```lean
theorem isUniversallyCatenary_of_locallyOfFiniteType_over_isCohenMacaulay {X S : Scheme.{u}}
    (f : X ⟶ S) [LocallyOfFiniteType f] [IsLocallyNoetherian S] (hS : IsCohenMacaulay S) :
    @IsUniversallyCatenary X (LocallyOfFiniteType.isLocallyNoetherian f)
```

**`AlgebraicGeometry.Scheme.isUniversallyCatenary_of_locallyOfFiniteType_over_int`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/UniversallyCatenaryExamples.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/UniversallyCatenaryExamples.lean#L249). The attribute's comment: “part (3)”. References: EGA IV (10.6.1), “(i), special case”; EGA IV (10.7.1), “2° over Z”.

> **Stacks Project, Tag 02JB, part (3).** A scheme locally of finite type over the integers is
> universally catenary. The base is `Spec (ULift ℤ)`, the terminal scheme of the ambient universe,
> so this is the statement for a scheme in an arbitrary universe.

```lean
theorem isUniversallyCatenary_of_locallyOfFiniteType_over_int {X : Scheme.{u}}
    (f : X ⟶ Spec (.of (ULift.{u} ℤ))) [LocallyOfFiniteType f] :
    @IsUniversallyCatenary X (LocallyOfFiniteType.isLocallyNoetherian f)
```

**`AlgebraicGeometry.Scheme.isUniversallyCatenary_of_locallyOfFiniteType_over_dimOneDomain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/UniversallyCatenaryExamples.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/UniversallyCatenaryExamples.lean#L258). The attribute's comment: “part (4)”.

> **Stacks Project, Tag 02JB, part (4).** A scheme locally of finite type over a
> one-dimensional Noetherian domain is universally catenary.

```lean
theorem isUniversallyCatenary_of_locallyOfFiniteType_over_dimOneDomain (A : Type u) [CommRing A]
    [IsNoetherianRing A] [IsDomain A] (hA : ringKrullDim A = 1) {X : Scheme.{u}}
    (f : X ⟶ Spec (.of A)) [LocallyOfFiniteType f] :
    @IsUniversallyCatenary X (LocallyOfFiniteType.isLocallyNoetherian f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.17, Tag 02J7](https://stacks.math.columbia.edu/tag/02J7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
