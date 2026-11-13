---
declaration: section
origin: cited
lean: closedUnderDirectSums_add_star_add, closedUnderDirectSums_smd_add, CategoryTheory.ObjectProperty.retractClosure_extensionProductIter_isClosedUnderBinaryProducts_and_add, Stacks.TriangulatedGenerators.isoClosure_strictMap_biSup_shift_eq_and_strictMap_operations_le, Stacks.TriangulatedGenerators.retractClosure_extensionProductIter_biSup_shift_inverseImage_of_le, DerivedCategory.prop_retractClosure_extensionProductIter_of_prop_homology_and_of_prop_X, CategoryTheory.Functor.isZero_obj_shift_of_retractClosure_extensionProductIter
statement: formalized
proof: formalized
---

# 13.35 Operations on full subcategories

Section 13.35 of the Stacks Project, [Tag 0FX0](https://stacks.math.columbia.edu/tag/0FX0). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FX3, a lemma

[Tag 0FX3](https://stacks.math.columbia.edu/tag/0FX3) in the Stacks Project.

**`closedUnderDirectSums_add_star_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/OperationsOnFullSubcategories.lean, line 859](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/OperationsOnFullSubcategories.lean#L859). The attribute's comment: “(1)”.

> **Stacks 0FX3 (1).** `add 𝒜 ⋆ add ℬ` is closed under direct sums:
> for all `X, X' ∈ add 𝒜 ⋆ add ℬ` we have `X ⊞ X' ∈ add 𝒜 ⋆ add ℬ`.
>
> Proof (as in the source): pick distinguished triangles `T : A → X → B → A[1]`
> and `T' : A' → X' → B' → A'[1]` with `A, A' ∈ add 𝒜`, `B, B' ∈ add ℬ`. The product
> triangle `productTriangle ![T, T']` is distinguished (`productTriangle_distinguished`),
> its legs are the `Fin 2`-products of the legs of `T, T'`, which via `finProd2` are the
> binary biproducts `A ⊞ A'`, `X ⊞ X'`, `B ⊞ B'`. Since `add` is closed under `⊞`
> (`add_closedUnderDirectSums`) and under iso (`add_iso`), `A ⊞ A' ∈ add 𝒜`,
> `B ⊞ B' ∈ add ℬ`, and the middle object is iso to `X ⊞ X'`.

```lean
theorem closedUnderDirectSums_add_star_add (𝒜 ℬ : Set C) :
    ClosedUnderDirectSums (add 𝒜 ⋆ add ℬ)
```

**`closedUnderDirectSums_smd_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/OperationsOnFullSubcategories.lean, line 887](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/OperationsOnFullSubcategories.lean#L887). The attribute's comment: “(2)”.

> **Stacks 0FX3 (2).** `smd (add 𝒜)` is closed under direct sums:
> for all `X, X' ∈ smd (add 𝒜)` we have `X ⊞ X' ∈ smd (add 𝒜)`.
>
> Proof (as in the source): write `A ≅ X ⊞ Y`, `A' ≅ X' ⊞ Y'` with
> `A, A' ∈ add 𝒜`. Then `A ⊞ A' ∈ add 𝒜` (`add_closedUnderDirectSums`) and
> `A ⊞ A' ≅ (X ⊞ Y) ⊞ (X' ⊞ Y') ≅ (X ⊞ X') ⊞ (Y ⊞ Y')` (`biprodRearrange`),
> exhibiting `X ⊞ X'` as a direct summand of `A ⊞ A' ∈ add 𝒜`.

```lean
theorem closedUnderDirectSums_smd_add (𝒜 : Set C) :
    ClosedUnderDirectSums (smd (add 𝒜))
```

## Tag 0FX4, a lemma

[Tag 0FX4](https://stacks.math.columbia.edu/tag/0FX4) in the Stacks Project.

**`CategoryTheory.ObjectProperty.retractClosure_extensionProductIter_isClosedUnderBinaryProducts_and_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/OperationsOnFullSubcategories.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/OperationsOnFullSubcategories.lean#L202).

> For a full subcategory `P` of a triangulated category which is closed under direct sums,
> the subcategory `smd(P^{⋆ (n + 1)})` of direct summands of `n`-fold extensions of objects of
> `P` is strictly full, closed under direct sums and closed under direct summands, and these
> subcategories are additive in the number of factors:
> `smd(P^{⋆ (n + m + 1)}) = smd(smd(P^{⋆ (n + 1)}) ⋆ smd(P^{⋆ (m + 1)}))`. Taking
> `P = add(A)` this is the Stacks project's `Cₙ = smd(add(A)^{⋆ n})`, strictly full, closed under
> direct sums and direct summands, with `C_{n + m} = smd(Cₙ ⋆ C_m)`.

```lean
theorem retractClosure_extensionProductIter_isClosedUnderBinaryProducts_and_add
    (P : ObjectProperty C) [P.IsClosedUnderBinaryProducts] [IsTriangulated C] (n m : ℕ) :
    (P.extensionProductIter n).retractClosure.IsClosedUnderIsomorphisms ∧
      (P.extensionProductIter n).retractClosure.IsClosedUnderBinaryProducts ∧
      (P.extensionProductIter n).retractClosure.IsStableUnderRetracts ∧
      (P.extensionProductIter (n + m + 1)).retractClosure =
        (extensionProduct (P.extensionProductIter n).retractClosure
          (P.extensionProductIter m).retractClosure).retractClosure
```

## Tag 0FX5, a remark

[Tag 0FX5](https://stacks.math.columbia.edu/tag/0FX5) in the Stacks Project.

**`Stacks.TriangulatedGenerators.isoClosure_strictMap_biSup_shift_eq_and_strictMap_operations_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/ExactFunctorBoundedOperations.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/ExactFunctorBoundedOperations.lean#L215). The attribute's comment: “Each of `F(𝒜[a, b]) = F(𝒜)[a, b]` (for any set of shifts, up to isomorphism), `F(smd(𝒜)) ⊂ smd(F(𝒜))`, `F(add(𝒜)) ⊂ add(F(𝒜))`, `F(𝒜 ⋆ ℬ) ⊂ F(𝒜) ⋆ F(ℬ)` and `F(𝒜^{⋆ n}) ⊂ F(𝒜)^{⋆ n}`, with `F(𝒜) = 𝒜.strictMap F`.”.

> **The operations on full subcategories are compatible with an exact functor.** Let
> `F : C ⥤ D` be an exact functor of pretriangulated categories, and for a full subcategory `A` of
> `C` write `F(A)` for the full subcategory `A.strictMap F` of the objects `F X` with `X ∈ A`.
> Then, for full subcategories `A`, `B` of `C`, every set `S` of shifts and every `n`:
> * `F(A[S]) = F(A)[S]` up to isomorphism, where `A[S]` consists of the objects `X ≅ Y⟦-i⟧` with
>   `Y ∈ A` and `i ∈ S`; for `S = [a, b] ∩ ℤ`, `-∞ ≤ a ≤ b ≤ ∞`, this is `F(A[a, b]) = F(A)[a, b]`;
> * `F(smd(A)) ⊂ smd(F(A))`;
> * `F(add(A)) ⊂ add(F(A))`;
> * `F(A ⋆ B) ⊂ F(A) ⋆ F(B)`;
> * `F(A^{⋆ (n + 1)}) ⊂ F(A)^{⋆ (n + 1)}`, the source's `F(A^{⋆ n}) ⊂ F(A)^{⋆ n}` for `n ≥ 1`
>   factors, `A.extensionProductIter n` having `n + 1` factors.

```lean
theorem isoClosure_strictMap_biSup_shift_eq_and_strictMap_operations_le
    (A B : ObjectProperty C) (S : Set ℤ) (n : ℕ) :
    ((⨆ i ∈ S, A.isoClosure.shift i).strictMap F).isoClosure =
        ⨆ i ∈ S, (A.strictMap F).isoClosure.shift i ∧
      A.retractClosure.strictMap F ≤ (A.strictMap F).retractClosure ∧
      A.binaryProductsClosure.strictMap F ≤ (A.strictMap F).binaryProductsClosure ∧
      (extensionProduct A B).strictMap F ≤ extensionProduct (A.strictMap F) (B.strictMap F) ∧
      (A.extensionProductIter n).strictMap F ≤ (A.strictMap F).extensionProductIter n
```

**`Stacks.TriangulatedGenerators.retractClosure_extensionProductIter_biSup_shift_inverseImage_of_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/ExactFunctorBoundedOperations.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/ExactFunctorBoundedOperations.lean#L240). The attribute's comment: “The composite `F(smd(add(𝒜[c, d])^{⋆ n})) ⊂ smd(add(F(𝒜)[c, d])^{⋆ n})`.”.

> **The bounded-shift form of `smd(add(P[c, d])^{⋆ n})` is functorial along an exact functor.**
> Let `F : C ⥤ D` be an exact functor of pretriangulated categories, let `P` be a property of
> objects of `C` and `Q` one of `D`, and suppose `F` carries every object satisfying `P` to one
> satisfying `Q`. Then `F` carries `smd(add(P[c, d])^{⋆ n})` into `smd(add(Q[c, d])^{⋆ n})`: the
> shift interval `[c, d]` and the number `n` of extensions are the same on both sides.
>
> This composes the compatibilities of Derived Categories, Remark 13.35.5 ([Stacks, Tag 0FX5])
> for the explicit subcategories `Cₙ = smd(add(E[c, d])^{⋆ n})` built from a bounded range of
> shifts as in [Stacks, Tag 0FX9]. Tracking the interval is the content: the
> unbounded-shift form `Stacks.TriangulatedGenerators.triangEnvelopeIter_inverseImage_of_le`,
> stated with `ObjectProperty.triangEnvelopeIter`, gives no control on which shifts of `Q` the
> image uses.

```lean
theorem retractClosure_extensionProductIter_biSup_shift_inverseImage_of_le
    {P : ObjectProperty C} {Q : ObjectProperty D} (h : ∀ ⦃X : C⦄, P X → Q (F.obj X))
    (c d : ℤ) (n : ℕ) :
    ((⨆ i ∈ Set.Icc c d, P.isoClosure.shift i).binaryProductsClosure.extensionProductIter n
      ).retractClosure ≤
      ((((⨆ i ∈ Set.Icc c d, Q.isoClosure.shift i).binaryProductsClosure.extensionProductIter n
        ).retractClosure).inverseImage F)
```

## Tag 0FX7, a lemma

[Tag 0FX7](https://stacks.math.columbia.edu/tag/0FX7) in the Stacks Project.

**`DerivedCategory.prop_retractClosure_extensionProductIter_of_prop_homology_and_of_prop_X`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/OperationsOnFullSubcategories.lean, line 541](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/OperationsOnFullSubcategories.lean#L541).

> Let `C` be an abelian category and `E` a class of objects of `C`, viewed inside the derived
> category `D(C)`. Let `a ≤ b`. (1) If the cohomology of `K : D(C)` vanishes outside `[a, b]` and
> each `H^i(K)` with `i ∈ [a, b]` is a direct summand of a finite direct sum of objects of `E`, then
> `K` is a direct summand of a `(b - a)`-fold extension of finite direct sums of objects of `E`
> placed in degrees `[a, b]`, that is, `K ∈ smd(add(E[a, b])^{⋆ (b - a + 1)})`. (2) The same
> conclusion holds for `K = Q.obj L` when `L` is a cochain complex vanishing outside `[a, b]` whose
> terms `L^i` with `i ∈ [a, b]` are direct summands of finite direct sums of objects of `E`. The
> special cases where the objects `H^i(K)`, resp. `L^i`, are themselves in `E` are parts (1) and (3)
> of [Stacks, Tag 0FX7].

```lean
theorem prop_retractClosure_extensionProductIter_of_prop_homology_and_of_prop_X
    (E : ObjectProperty C) {a b : ℤ} (hab : a ≤ b) :
    (∀ (K : DerivedCategory C) [K.IsGE a] [K.IsLE b],
        (∀ i ∈ Set.Icc a b,
          E.binaryProductsClosure.retractClosure ((homologyFunctor C i).obj K)) →
        ((⨆ i ∈ Set.Icc a b,
            E.map (singleFunctor C i)).binaryProductsClosure.extensionProductIter
          (b - a).toNat).retractClosure K) ∧
    (∀ (L : CochainComplex C ℤ) [L.IsStrictlyGE a] [L.IsStrictlyLE b],
        (∀ i ∈ Set.Icc a b, E.binaryProductsClosure.retractClosure (L.X i)) →
        ((⨆ i ∈ Set.Icc a b,
            E.map (singleFunctor C i)).binaryProductsClosure.extensionProductIter
          (b - a).toNat).retractClosure (Q.obj L))
```

## Tag 0FX8, a lemma

[Tag 0FX8](https://stacks.math.columbia.edu/tag/0FX8) in the Stacks Project.

**`CategoryTheory.Functor.isZero_obj_shift_of_retractClosure_extensionProductIter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/OperationsOnFullSubcategories.lean, line 659](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/OperationsOnFullSubcategories.lean#L659).

> Let `H : C ⥤ A` be a homological functor from a triangulated category to an abelian category,
> with `H^i(X) = H(X⟦i⟧)`, and let `E` be a class of objects of `C` such that `H^i(E) = 0` for
> `E ∈ E` and `i ∉ [a, b]`. Then every object `X` which is a direct summand of an `n`-fold extension
> of finite direct sums of objects `E⟦-j⟧` with `E ∈ E` and `j ∈ [c, d]` satisfies `H^i(X) = 0` for
> `i ∉ [a + c, b + d]`. In the notation of [Stacks, Tag 0FX0], for
> `X ∈ smd(add(E[c, d])^{⋆ (n + 1)})` we have `H^i(X) = 0` for `i ∉ [a + c, b + d]`; the window does
> not depend on the number of extensions, so it is sharper than the window `[-m + na, m + nb]` of
> [Stacks, Tag 0FX8], which it implies for `a ≤ 0 ≤ b`, `c = -m`, `d = m`.

```lean
theorem isZero_obj_shift_of_retractClosure_extensionProductIter
    (H : C ⥤ A) [H.IsHomological] (E : ObjectProperty C) {a b : ℤ}
    (hE : ∀ ⦃Y : C⦄, E Y → ∀ i ∉ Set.Icc a b, IsZero (H.obj (Y⟦i⟧)))
    (c d : ℤ) (n : ℕ) {X : C}
    (hX : ((⨆ j ∈ Set.Icc c d,
      E.isoClosure.shift j).binaryProductsClosure.extensionProductIter n).retractClosure X)
    {i : ℤ} (hi : i ∉ Set.Icc (a + c) (b + d)) :
    IsZero (H.obj (X⟦i⟧))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.35, Tag 0FX0](https://stacks.math.columbia.edu/tag/0FX0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
