---
declaration: section
origin: cited
lean: CategoryTheory.IsCompactObject, CategoryTheory.isClosedUnderIsomorphisms_isTriangulated_isSaturated_and_isIdempotentComplete_isCompactObject, CategoryTheory.Pretriangulated.exists_isHomotopyColimit_of_compactlyGenerated, CategoryTheory.Pretriangulated.exists_fac_triangEnvelope_of_isCompactObject, CategoryTheory.Pretriangulated.IsCompactlyGenerated, CategoryTheory.ObjectProperty.isWeakTriangulatedGenerator_ofObj_iff, CategoryTheory.ObjectProperty.isWeakTriangulatedGenerator_iff_triangEnvelope_eq_isCompactObject_and_isCompactlyGenerated
statement: formalized
proof: formalized
---

# 13.37 Compact objects

Section 13.37 of the Stacks Project, [Tag 09SM](https://stacks.math.columbia.edu/tag/09SM). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07LS, a definition

[Tag 07LS](https://stacks.math.columbia.edu/tag/07LS) in the Stacks Project.

**`CategoryTheory.IsCompactObject`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/CompactObjects/ThickSubcategory.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/CompactObjects/ThickSubcategory.lean#L106).

> An object `K` of a preadditive category is *compact* if for every family `E : I → C` whose
> direct sum exists, the map `⨁ i, (K ⟶ E i) → (K ⟶ ∐ E)` sending a finitely supported family
> `(f i)` to `∑ i, f i ≫ Sigma.ι E i` is bijective; that is, a morphism from `K` into a direct sum
> factors through a finite subsum in exactly one way.

```lean
public class IsCompactObject (K : C) : Prop
```

## Tag 09QH, a lemma

[Tag 09QH](https://stacks.math.columbia.edu/tag/09QH) in the Stacks Project.

**`CategoryTheory.isClosedUnderIsomorphisms_isTriangulated_isSaturated_and_isIdempotentComplete_isCompactObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/CompactObjects/ThickSubcategory.lean, line 532](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/CompactObjects/ThickSubcategory.lean#L532).

> The compact objects of a pre-triangulated category `D` with direct sums form the objects of a
> Karoubian, saturated, strictly full, pre-triangulated subcategory of `D`: the property of being
> compact is closed under isomorphisms, is a triangulated subcategory of `D`, is saturated (closed
> under direct summands), and idempotents split in the full subcategory it spans.

```lean
public theorem
    isClosedUnderIsomorphisms_isTriangulated_isSaturated_and_isIdempotentComplete_isCompactObject :
    ObjectProperty.IsClosedUnderIsomorphisms (IsCompactObject.{w, _, _} (C := D)) ∧
      ObjectProperty.IsTriangulated (IsCompactObject.{w, _, _} (C := D)) ∧
      ObjectProperty.IsSaturated (IsCompactObject.{w, _, _} (C := D)) ∧
      IsIdempotentComplete
        (ObjectProperty.FullSubcategory (IsCompactObject.{w, _, _} (C := D)))
```

## Tag 09SN, a lemma

[Tag 09SN](https://stacks.math.columbia.edu/tag/09SN) in the Stacks Project.

**`CategoryTheory.Pretriangulated.exists_isHomotopyColimit_of_compactlyGenerated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/CompactObjects/CellStructure.lean, line 723](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/CompactObjects/CellStructure.lean#L723).

> **Stacks 09SN**. Let `D` be a pre-triangulated category with direct sums and let `E : ι → D`
> be a family of compact objects such that `⨁ E i` generates `D`, i.e. the only objects right
> orthogonal to all shifts of the `E i` are the zero objects. Then every object `X` of `D` is a
> derived colimit `X = hocolim Xₙ` of a system `F : ℕ ⥤ D` whose first term `F.obj 0` is a direct
> sum of shifts of the `E i` and each of whose transition morphisms `Xₙ ⟶ Xₙ₊₁` fits into a
> distinguished triangle `Yₙ ⟶ Xₙ ⟶ Xₙ₊₁ ⟶ Yₙ⟦1⟧` with `Yₙ` a direct sum of shifts of the `E i`.

```lean
public theorem exists_isHomotopyColimit_of_compactlyGenerated
    {ι : Type v} (E : ι → D) [∀ i, IsCompactObject.{v} (E i)]
    (hE : ∀ Y : D, ((ofObj E).shiftClosure ℤ).rightOrthogonal Y → IsZero Y) (X : D) :
    ∃ F : ℕ ⥤ D,
      IsHomotopyColimit F X ∧
      (⨆ J : Type v, ((ofObj E).shiftClosure ℤ).colimitsOfShape (Discrete J)) (F.obj 0) ∧
      ∀ n : ℕ, ∃ Y : D,
        (⨆ J : Type v, ((ofObj E).shiftClosure ℤ).colimitsOfShape (Discrete J)) Y ∧
        ∃ (f : Y ⟶ F.obj n) (g : F.obj (n + 1) ⟶ Y⟦(1 : ℤ)⟧),
          Triangle.mk f (F.map (homOfLE (Nat.le_succ n))) g ∈ distTriang D
```

## Tag 09SP, a lemma

[Tag 09SP](https://stacks.math.columbia.edu/tag/09SP) in the Stacks Project.

**`CategoryTheory.Pretriangulated.exists_fac_triangEnvelope_of_isCompactObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/CompactObjects/CompactGenerators.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/CompactObjects/CompactGenerators.lean#L323).

> **Stacks 09SP**. Let `D` be a triangulated category with direct sums, `E : ι → D` a family of
> compact objects, and `X : ℕ → D` a system of cell attachments as in [Stacks, Tag 09SN]: `X 0` is
> a direct sum of shifts of the `E i` and each `X (n + 1)` fits into a distinguished triangle
> `Yₙ ⟶ X n ⟶ X (n + 1) ⟶ Yₙ⟦1⟧` with `Yₙ` a direct sum of shifts of the `E i`. Then every
> morphism `φ : C ⟶ X n` from a compact object `C` factors as `C ⟶ Z ⟶ X n` with `Z` an object of
> the triangulated envelope `⟨E_{i₁} ⊕ … ⊕ E_{i_t}⟩` of a finite direct sum of the `E i`.

```lean
public theorem exists_fac_triangEnvelope_of_isCompactObject
    {ι : Type v} (E : ι → D) [∀ i, IsCompactObject.{v} (E i)] {X : ℕ → D}
    (hX₀ : (⨆ J : Type v, ((ofObj E).shiftClosure ℤ).colimitsOfShape (Discrete J)) (X 0))
    (hX : ∀ n : ℕ, ∃ Y : D,
      (⨆ J : Type v, ((ofObj E).shiftClosure ℤ).colimitsOfShape (Discrete J)) Y ∧
        ∃ (f : Y ⟶ X n) (g : X n ⟶ X (n + 1)) (h : X (n + 1) ⟶ Y⟦(1 : ℤ)⟧),
          Triangle.mk f g h ∈ distTriang D)
    {C : D} [IsCompactObject.{v} C] {n : ℕ} (φ : C ⟶ X n) :
    ∃ (s : Finset ι) (Z : D), (ObjectProperty.singleton (∐ fun i : s ↦ E i)).triangEnvelope Z ∧
      ∃ (a : C ⟶ Z) (b : Z ⟶ X n), a ≫ b = φ
```

## Tag 09SQ, a definition

[Tag 09SQ](https://stacks.math.columbia.edu/tag/09SQ) in the Stacks Project.

**`CategoryTheory.Pretriangulated.IsCompactlyGenerated`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/CompactObjects/CellStructure.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/CompactObjects/CellStructure.lean#L142).

> A category `D` with a shift by `ℤ` is *compactly generated* if there is a family `E : ι → D`
> of compact objects, indexed by a type `ι : Type w`, which is a weak generator: the only objects of
> `D` receiving only zero maps from the shifts `(E i)⟦n⟧` are the zero objects. When `D` has direct
> sums indexed by `Type w` this says that `⨁ E i` generates `D`, as in Definition
> [Stacks, Tag 09SQ] — see `ObjectProperty.isWeakTriangulatedGenerator_ofObj_iff`.

```lean
public def IsCompactlyGenerated : Prop
```

**`CategoryTheory.ObjectProperty.isWeakTriangulatedGenerator_ofObj_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/CompactObjects/CompactGenerators.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/CompactObjects/CompactGenerators.lean#L396). The attribute's comment: “the source's form of the generation condition: the direct sum ∐ E is a weak generator”.

> A family of objects is a weak generator if and only if its direct sum is one: for a family
> `E : ι → C` whose coproduct exists, the property of belonging to `E` is a weak generator exactly
> when the single object `∐ E` is. This identifies the family-wise condition with the source's
> condition on `⨁ E i` in Definition [Stacks, Tag 09SQ].

```lean
public theorem isWeakTriangulatedGenerator_ofObj_iff {C : Type u} [Category.{v} C]
    [HasZeroMorphisms C] [HasShift C ℤ] {ι : Type w} (E : ι → C) [HasCoproduct E] :
    (ofObj E).IsWeakTriangulatedGenerator ↔
      (ObjectProperty.singleton (∐ E)).IsWeakTriangulatedGenerator
```

## Tag 09SR, a proposition

[Tag 09SR](https://stacks.math.columbia.edu/tag/09SR) in the Stacks Project.

**`CategoryTheory.ObjectProperty.isWeakTriangulatedGenerator_iff_triangEnvelope_eq_isCompactObject_and_isCompactlyGenerated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/CompactObjects/CompactGenerators.lean, line 714](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/CompactObjects/CompactGenerators.lean#L714).

> **Stacks 09SR**. Let `D` be a triangulated category with direct sums and let `E` be a compact
> object of `D`. Then `E` is a weak generator of `D` if and only if `E` is a classical generator of
> the subcategory `D_c` of compact objects, i.e. the triangulated envelope `⟨E⟩` is exactly the
> property of being a compact object, and `D` is compactly generated.

```lean
public theorem
    isWeakTriangulatedGenerator_iff_triangEnvelope_eq_isCompactObject_and_isCompactlyGenerated
    (E : D) [IsCompactObject.{v} E] :
    (ObjectProperty.singleton E).IsWeakTriangulatedGenerator ↔
      (ObjectProperty.singleton E).triangEnvelope = IsCompactObject.{v, _, _} (C := D) ∧
        IsCompactlyGenerated.{v} D
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.37, Tag 09SM](https://stacks.math.columbia.edu/tag/09SM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
