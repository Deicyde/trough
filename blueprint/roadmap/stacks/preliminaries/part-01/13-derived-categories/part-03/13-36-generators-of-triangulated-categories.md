---
declaration: section
origin: cited
lean: CategoryTheory.ObjectProperty.triangEnvelopeIter_eq_and_triangEnvelopeIter_add, CategoryTheory.ObjectProperty.triangEnvelope_eq_iSup_and_isSaturated_and_le_iff, CategoryTheory.ObjectProperty.IsWeakTriangulatedGenerator, CategoryTheory.ObjectProperty.isWeakTriangulatedGenerator_iff, Stacks.TriangulatedGenerators.hom_vanishing_iff_gen, CategoryTheory.ObjectProperty.IsClassicalTriangulatedGenerator.isZero_of_rightOrthogonal_shiftClosure, CategoryTheory.ObjectProperty.IsClassicalTriangulatedGenerator.isStrongTriangulatedGenerator, CategoryTheory.ObjectProperty.triangEnvelope_singleton_le_of_sums_of_extensions_of_summands
statement: formalized
proof: formalized
---

# 13.36 Generators of triangulated categories

Section 13.36 of the Stacks Project, [Tag 09SI](https://stacks.math.columbia.edu/tag/09SI). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FX9, a lemma

[Tag 0FX9](https://stacks.math.columbia.edu/tag/0FX9) in the Stacks Project.

**`CategoryTheory.ObjectProperty.triangEnvelopeIter_eq_and_triangEnvelopeIter_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Generators.lean, line 408](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Generators.lean#L408).

> The descriptions of the levels of the triangulated envelope, [Stacks, Tag 0FX9]. Write
> `⟨P⟩ₙ₊₁ = P.triangEnvelopeIter n` (Mathlib counts extensions, so its index is one less than the
> source's). Then
>
> * `⟨P⟩₁ = smd(add(P[-∞, ∞]))` and `⟨P⟩ₙ₊₁ = smd(⟨P⟩₁ ⋆ ⟨P⟩ₙ)`: these are the source's definition
>   of the levels, so `P.triangEnvelopeIter` is the source's `⟨E⟩` for `P = {E}`;
> * `⟨P⟩ₙ₊₁ = smd(⟨P⟩ₙ ⋆ ⟨P⟩₁)` as well, so the bracketing of `⟨P⟩₁ ⋆ … ⋆ ⟨P⟩₁` is immaterial;
> * `⟨P⟩ₙ₊₁ = smd(⟨P⟩₁^{⋆ (n + 1)})`, the left and middle equalities of the source's display;
> * `⟨P⟩ₙ₊₁ = ⋃_{m} smd(add(P[-m, m])^{⋆ (n + 1)})`, the right-hand equality of the display,
>   with `P[-m, m]` spelled `⨆ i ∈ Set.Icc (-m) m, P.isoClosure.shift i`;
> * `⟨P⟩_{(n + 1) + (n' + 1)} = smd(⟨P⟩ₙ₊₁ ⋆ ⟨P⟩ₙ'₊₁)`, the second claim of the source.
>
> The source's ranges `n, n' ≥ 1` and `m ≥ 1` are `n, n', m : ℕ` here, the same unions since the
> families are monotone. An arbitrary property of objects `P` replaces the single object `E`; the
> source's statement is the case `P = ObjectProperty.singleton E`. `[IsTriangulated C]` is the
> source's "triangulated": the octahedron axiom gives the associativity of `⋆`
> ([Stacks, Tag 0FX1]) used in the second and last conjuncts.

```lean
public theorem triangEnvelopeIter_eq_and_triangEnvelopeIter_add [IsTriangulated C]
    (P : ObjectProperty C) :
    P.triangEnvelopeIter 0 = (P.shiftClosure ℤ).binaryProductsClosure.retractClosure ∧
    (∀ n : ℕ, P.triangEnvelopeIter (n + 1) =
      (extensionProduct (P.triangEnvelopeIter 0) (P.triangEnvelopeIter n)).retractClosure) ∧
    (∀ n : ℕ, P.triangEnvelopeIter (n + 1) =
      (extensionProduct (P.triangEnvelopeIter n) (P.triangEnvelopeIter 0)).retractClosure) ∧
    (∀ n : ℕ, P.triangEnvelopeIter n =
      ((P.triangEnvelopeIter 0).extensionProductIter n).retractClosure) ∧
    (∀ n : ℕ, P.triangEnvelopeIter n =
      ⨆ m : ℕ, ((⨆ i ∈ Set.Icc (-(m : ℤ)) (m : ℤ),
        P.isoClosure.shift i).binaryProductsClosure.extensionProductIter n).retractClosure) ∧
    ∀ n n' : ℕ, P.triangEnvelopeIter (n + n' + 1) =
      (extensionProduct (P.triangEnvelopeIter n) (P.triangEnvelopeIter n')).retractClosure
```

## Tag 0ATG, a lemma

[Tag 0ATG](https://stacks.math.columbia.edu/tag/0ATG) in the Stacks Project.

**`CategoryTheory.ObjectProperty.triangEnvelope_eq_iSup_and_isSaturated_and_le_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Generators.lean, line 482](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Generators.lean#L482). References: SGA 4½ Etat 0 (2.3.3), “more general”.

> The triangulated envelope `⟨P⟩ = ⋃ₙ ⟨P⟩ₙ` of a nonempty object property `P` of a
> triangulated category is the union over `n, m` of the subcategories `smd(add(P[-m, m])^{⋆ n})`;
> it is closed under isomorphisms (strictly full), saturated (thick) and a triangulated
> subcategory; and it is contained in a strictly full, saturated triangulated subcategory `Q`
> exactly when `P` is, so that it is the smallest such subcategory containing `P`.

```lean
public theorem triangEnvelope_eq_iSup_and_isSaturated_and_le_iff
    (P : ObjectProperty C) [P.Nonempty] [IsTriangulated C] :
    (P.triangEnvelope = ⨆ n : ℕ, ⨆ m : ℕ,
        ((⨆ i ∈ Set.Icc (-(m : ℤ)) (m : ℤ),
          P.isoClosure.shift i).binaryProductsClosure.extensionProductIter n).retractClosure) ∧
      P.triangEnvelope.IsClosedUnderIsomorphisms ∧ P.triangEnvelope.IsSaturated ∧
      P.triangEnvelope.IsTriangulated ∧
      ∀ Q : ObjectProperty C, Q.IsClosedUnderIsomorphisms → Q.IsSaturated → Q.IsTriangulated →
        (P.triangEnvelope ≤ Q ↔ P ≤ Q)
```

## Tag 09SJ, a definition

[Tag 09SJ](https://stacks.math.columbia.edu/tag/09SJ) in the Stacks Project.

**`CategoryTheory.ObjectProperty.IsWeakTriangulatedGenerator`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Generators.lean, line 512](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Generators.lean#L512). The attribute's comment: “(3)”.

> A property of objects `P` of a category `C` with zero morphisms and a shift by `ℤ` is a
> *weak generator*, or simply a *generator*, if every object `K` receiving only zero maps from the
> shifts of the objects satisfying `P` is zero; equivalently, if every nonzero object `K` admits an
> integer `n` and a nonzero map `E ⟶ K⟦n⟧` from an object `E` satisfying `P`
> (`isWeakTriangulatedGenerator_iff`).

```lean
public def IsWeakTriangulatedGenerator (P : ObjectProperty C) : Prop
```

**`CategoryTheory.ObjectProperty.isWeakTriangulatedGenerator_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Generators.lean, line 521](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Generators.lean#L521). The attribute's comment: “(3), in the source's literal form: for every nonzero K an integer n and a nonzero map E ⟶ K⟦n⟧”.

> A weak generator in the source's own words: `P` is a weak generator if and only if for every
> nonzero object `K` there are an object `E` satisfying `P`, an integer `n` and a nonzero map
> `E ⟶ K⟦n⟧`. For `P = ObjectProperty.singleton E` this is literally Definition
> [Stacks, Tag 09SJ\](3).

```lean
public theorem isWeakTriangulatedGenerator_iff (P : ObjectProperty C) :
    P.IsWeakTriangulatedGenerator ↔
      ∀ K : C, ¬ IsZero K → ∃ E, P E ∧ ∃ (n : ℤ) (f : E ⟶ K⟦n⟧), f ≠ 0
```

## Tag 09SK, a lemma

[Tag 09SK](https://stacks.math.columbia.edu/tag/09SK) in the Stacks Project.

**`Stacks.TriangulatedGenerators.hom_vanishing_iff_gen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Generators.lean, line 905](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Generators.lean#L905).

> Stacks tag `09SK` (Lemma 13.36.4). For objects `E, K` of a triangulated
> category `D`, the following are equivalent:
> 1. `Hom(E, K[i]) = 0` for all `i : ℤ`;
> 2. `Hom(E', K) = 0` for all `E' ∈ ⟨E⟩`.

```lean
theorem hom_vanishing_iff_gen (E K : D) :
    (∀ i : ℤ, ∀ f : E ⟶ (shiftFunctor D i).obj K, f = 0) ↔
      (∀ E' ∈ gen E, ∀ f : E' ⟶ K, f = 0)
```

## Tag 09SL, a lemma

[Tag 09SL](https://stacks.math.columbia.edu/tag/09SL) in the Stacks Project.

**`CategoryTheory.ObjectProperty.IsClassicalTriangulatedGenerator.isZero_of_rightOrthogonal_shiftClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Generators.lean, line 578](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Generators.lean#L578).

> **Stacks 09SL**: a classical generator of a (pre)triangulated category is a weak generator.
> If the triangulated envelope of an object property `P` is everything, then an object `Y` which
> receives only zero maps from the shifts of the objects of `P` — equivalently, an object `Y` with
> `Hom(X, Y⟦n⟧) = 0` for every `X` satisfying `P` and every `n : ℤ` — is a zero object.

```lean
public theorem IsClassicalTriangulatedGenerator.isZero_of_rightOrthogonal_shiftClosure
    {P : ObjectProperty C} (hP : P.IsClassicalTriangulatedGenerator) {Y : C}
    (hY : (P.shiftClosure ℤ).rightOrthogonal Y) : IsZero Y
```

## Tag 0FXA, a lemma

[Tag 0FXA](https://stacks.math.columbia.edu/tag/0FXA) in the Stacks Project.

**`CategoryTheory.ObjectProperty.IsClassicalTriangulatedGenerator.isStrongTriangulatedGenerator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Generators.lean, line 661](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Generators.lean#L661).

> **Stacks 0FXA**: in a triangulated category which has a strong generator, every classical
> generator is a strong generator. Here the ambient strong generator is a finite family of objects
> `X : ι → C` (the source's case is a single object, `ι = Unit`), and the classical generator is an
> object property `P` (the source's case is `P = ObjectProperty.singleton E`).

```lean
public theorem IsClassicalTriangulatedGenerator.isStrongTriangulatedGenerator [IsTriangulated C]
    {P : ObjectProperty C} (hP : P.IsClassicalTriangulatedGenerator)
    {ι : Type*} [Finite ι] {X : ι → C} (hX : (ofObj X).IsStrongTriangulatedGenerator) :
    P.IsStrongTriangulatedGenerator
```

## Tag 0ATH, a remark

[Tag 0ATH](https://stacks.math.columbia.edu/tag/0ATH) in the Stacks Project.

**`CategoryTheory.ObjectProperty.triangEnvelope_singleton_le_of_sums_of_extensions_of_summands`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/TriangulatedEnvelopeInduction.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/TriangulatedEnvelopeInduction.lean#L57).

> Let `E` be an object of a triangulated category and let `T` be a property of objects which
> is inherited by finite direct sums, satisfies the two-out-of-three property for distinguished
> triangles, is inherited by direct summands, and holds on all shifts of `E`. Then `T` holds on
> every object of the triangulated subcategory `⟨E⟩` generated by `E`.

```lean
theorem triangEnvelope_singleton_le_of_sums_of_extensions_of_summands
    [IsTriangulated C] (E : C) (T : ObjectProperty C)
    (_hsum : ∀ K L : C, T K → T L → T (K ⊞ L))
    (hext₁ : ∀ Tr ∈ distTriang C, T Tr.obj₂ → T Tr.obj₃ → T Tr.obj₁)
    (hext₂ : ∀ Tr ∈ distTriang C, T Tr.obj₁ → T Tr.obj₃ → T Tr.obj₂)
    (hext₃ : ∀ Tr ∈ distTriang C, T Tr.obj₁ → T Tr.obj₂ → T Tr.obj₃)
    (hsummand : ∀ K L : C, T (K ⊞ L) → T K ∧ T L)
    (hshift : ∀ n : ℤ, T ((CategoryTheory.shiftFunctor C n).obj E)) :
    (ObjectProperty.singleton E).triangEnvelope ≤ T
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.36, Tag 09SI](https://stacks.math.columbia.edu/tag/09SI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
