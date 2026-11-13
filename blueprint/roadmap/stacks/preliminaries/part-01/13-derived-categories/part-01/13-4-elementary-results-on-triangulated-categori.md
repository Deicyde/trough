---
declaration: section
origin: cited
lean: Stacks.CategoryTheory.ComponentwiseInvertibility.isIso_of_five, comp_middle_zero_of_endomorphisms, CategoryTheory.Pretriangulated.complete_distinguished_triangle_morphism₂_idempotent, CategoryTheory.Pretriangulated.distinguished_cocone_triangle, CategoryTheory.Pretriangulated.exists_iso_of_arrow_iso, CategoryTheory.Pretriangulated.Triangle.hom_ext_of_hom₁_eq_of_hom₃_eq, CategoryTheory.Pretriangulated.Triangle.distinguished_iff_of_isZero₃, CategoryTheory.Pretriangulated.Triangle.isZero₃_iff_isIso₁
statement: formalized
proof: formalized
---

# 13.4 Elementary results on triangulated categories

Section 13.4 of the Stacks Project, [Tag 05QN](https://stacks.math.columbia.edu/tag/05QN). 20 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 10 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 014A, a lemma

[Tag 014A](https://stacks.math.columbia.edu/tag/014A) in the Stacks Project.

**`Stacks.CategoryTheory.ComponentwiseInvertibility.isIso_of_five`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/ComponentwiseInvertibility.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/ComponentwiseInvertibility.lean#L124). The attribute's comment: “the rotation `two of (a, b, c) isomorphisms give the third` in the case `a, b` give `c`, in an arbitrary pretriangulated category. The five independent morphisms with four commuting squares are a weaker hypothesis than a morphism of triangles, which forces the fourth and fifth to be `a⟦1⟧'` and `b⟦1⟧'`; Mathlib's `isIso₃_of_isIso₁₂` consumes a morphism of triangles and so does not apply in this form, and the proof here is from the exactness of the Yoneda sequences of the two triangles rather than from it. The other two rotations, for data that is a morphism of triangles, are Mathlib's `isIso₁_of_isIso₂₃` and `isIso₂_of_isIso₁₃`”.

> **The five lemma in a pretriangulated category.**  Two distinguished triangles connected by
> five morphisms whose four consecutive squares commute, with the first, second, fourth and fifth
> invertible, have invertible third morphism.

```lean
theorem isIso_of_five {C : Type*} [Category* C] [HasShift C ℤ] [Preadditive C]
    [HasZeroObject C] [∀ n : ℤ, (shiftFunctor C n).Additive] [Pretriangulated C]
    (T T' : Triangle C) (hT : T ∈ distTriang C) (hT' : T' ∈ distTriang C)
    (a₁ : T.obj₁ ⟶ T'.obj₁) (a₂ : T.obj₂ ⟶ T'.obj₂) (a₃ : T.obj₃ ⟶ T'.obj₃)
    (a₄ : T.obj₁⟦(1 : ℤ)⟧ ⟶ T'.obj₁⟦(1 : ℤ)⟧)
    (a₅ : T.obj₂⟦(1 : ℤ)⟧ ⟶ T'.obj₂⟦(1 : ℤ)⟧)
    (ha₁ : IsIso a₁) (ha₂ : IsIso a₂) (ha₄ : IsIso a₄) (ha₅ : IsIso a₅)
    (h₁ : T.mor₁ ≫ a₂ = a₁ ≫ T'.mor₁)
    (h₂ : T.mor₂ ≫ a₃ = a₂ ≫ T'.mor₂)
    (h₃ : T.mor₃ ≫ a₄ = a₃ ≫ T'.mor₃)
    (h₄ : T.mor₁⟦(1 : ℤ)⟧' ≫ a₅ = a₄ ≫ T'.mor₁⟦(1 : ℤ)⟧') :
    IsIso a₃
```

## Tag 05QP, a lemma

[Tag 05QP](https://stacks.math.columbia.edu/tag/05QP) in the Stacks Project.

**`comp_middle_zero_of_endomorphisms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Elementary.lean, line 842](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Elementary.lean#L842).

> If `(0, b, 0)` and `(0, b', 0)` are endomorphisms of a distinguished triangle
> `T = (X, Y, Z, f, g, h)`, then the composite of their middle components vanishes,
> i.e. `b ∘ b' = 0` (written `ψ.hom₂ ≫ φ.hom₂ = 0` in Lean's diagrammatic order
> with `b = φ.hom₂`, `b' = ψ.hom₂`).

```lean
theorem comp_middle_zero_of_endomorphisms (T : Triangle C)
    (hT : T ∈ distinguishedTriangles)
    (φ ψ : TriangleMorphism T T)
    (hφ₁ : φ.hom₁ = 0)
    (hψ₃ : ψ.hom₃ = 0) :
    ψ.hom₂ ≫ φ.hom₂ = 0
```

## Tag 05QQ, a lemma

[Tag 05QQ](https://stacks.math.columbia.edu/tag/05QQ) in the Stacks Project.

**`CategoryTheory.Pretriangulated.complete_distinguished_triangle_morphism₂_idempotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Elementary.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Elementary.lean#L220).

> Let `T = (X, Y, Z, f, g, h)` be a distinguished triangle in
> a pre-triangulated category, and let `a : X ⟶ X`, `c : Z ⟶ Z` be idempotents
> such that `h ≫ a⟦1⟧' = c ≫ h`. Then `(a, c)` extends to an *idempotent*
> endomorphism `φ : T ⟶ T` of the triangle, i.e. there is `b : Y ⟶ Y` with
> `b ≫ b = b` making `(a, b, c)` an endomorphism of `T`.

```lean
theorem complete_distinguished_triangle_morphism₂_idempotent (T : Triangle C)
    (hT : T ∈ distTriang C) (a : T.obj₁ ⟶ T.obj₁) (c : T.obj₃ ⟶ T.obj₃)
    (comm : T.mor₃ ≫ a⟦(1 : ℤ)⟧' = c ≫ T.mor₃) (ha : a ≫ a = a) (hc : c ≫ c = c) :
    ∃ φ : T ⟶ T, φ ≫ φ = φ ∧ φ.hom₁ = a ∧ φ.hom₃ = c
```

## Tag 014B, a lemma

[Tag 014B](https://stacks.math.columbia.edu/tag/014B) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Pretriangulated.distinguished_cocone_triangle`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pretriangulated.distinguished_cocone_triangle#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Triangulated/Elementary.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Elementary.lean#L120) (StacksFrontier): “existence of a distinguished triangle on a morphism”.
- [`CategoryTheory.Pretriangulated.exists_iso_of_arrow_iso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pretriangulated.exists_iso_of_arrow_iso#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Triangulated/Elementary.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Elementary.lean#L122) (StacksFrontier): “uniqueness up to a (nonunique) isomorphism of triangles”.

## Tag 0FWZ, a lemma

[Tag 0FWZ](https://stacks.math.columbia.edu/tag/0FWZ) in the Stacks Project.

**`CategoryTheory.Pretriangulated.Triangle.hom_ext_of_hom₁_eq_of_hom₃_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Elementary.lean, line 584](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Elementary.lean#L584).

> A morphism of distinguished triangles is determined by its outer two components, as
> soon as one of the following five vanishing conditions holds:
> `Hom(Y, X') = 0`, or `Hom(Z, Y') = 0`, or `Hom(X, X') = Hom(Z, X') = 0`, or
> `Hom(Z, X') = Hom(Z, Z') = 0`, or `Hom(X[1], Z') = Hom(Z, X') = 0`.

```lean
theorem Triangle.hom_ext_of_hom₁_eq_of_hom₃_eq {T T' : Triangle C}
    (hT : T ∈ distTriang C) (hT' : T' ∈ distTriang C) (φ ψ : T ⟶ T')
    (h₁ : φ.hom₁ = ψ.hom₁) (h₃ : φ.hom₃ = ψ.hom₃)
    (H : (∀ u : T.obj₂ ⟶ T'.obj₁, u = 0) ∨
      (∀ u : T.obj₃ ⟶ T'.obj₂, u = 0) ∨
      ((∀ u : T.obj₁ ⟶ T'.obj₁, u = 0) ∧ ∀ u : T.obj₃ ⟶ T'.obj₁, u = 0) ∨
      ((∀ u : T.obj₃ ⟶ T'.obj₁, u = 0) ∧ ∀ u : T.obj₃ ⟶ T'.obj₃, u = 0) ∨
      ((∀ u : T.obj₁⟦(1 : ℤ)⟧ ⟶ T'.obj₃, u = 0) ∧ ∀ u : T.obj₃ ⟶ T'.obj₁, u = 0)) :
    φ = ψ
```

## Tag 05QR, a lemma

[Tag 05QR](https://stacks.math.columbia.edu/tag/05QR) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Pretriangulated.Triangle.distinguished_iff_of_isZero₃`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pretriangulated.Triangle.distinguished_iff_of_isZero₃#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Triangulated/Elementary.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Elementary.lean#L239) (StacksFrontier): “(1) ⟺ (2)”.
- [`CategoryTheory.Pretriangulated.Triangle.isZero₃_iff_isIso₁`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pretriangulated.Triangle.isZero₃_iff_isIso₁#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Triangulated/Elementary.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Elementary.lean#L241) (StacksFrontier): “(1) ⟺ (3)”.
- [`CategoryTheory.Pretriangulated.Triangle.isZero₃_of_isIso₁`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pretriangulated.Triangle.isZero₃_of_isIso₁#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Triangulated/Elementary.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Elementary.lean#L243) (StacksFrontier): “(1) ⟹ (3)”.

## Tag 05QS, a lemma

[Tag 05QS](https://stacks.math.columbia.edu/tag/05QS) in the Stacks Project.

**`productTriangle_distinguished_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Elementary.lean, line 959](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Elementary.lean#L959).

> The direct sum of two triangles is distinguished if and only if both summand triangles are
> distinguished. Here `T : WalkingPair → Triangle C` packages the pair `(T₁, T₂)`, and
> `productTriangle T` is the direct-sum triangle `T₁ ⊕ T₂`.

```lean
theorem productTriangle_distinguished_iff
    {C : Type*} [Category C] [Preadditive C] [HasZeroObject C] [HasShift C ℤ]
    [∀ n : ℤ, (CategoryTheory.shiftFunctor C n).Additive] [CategoryTheory.Pretriangulated C]
    [HasBinaryBiproducts C] (T : WalkingPair → Triangle C) :
    (productTriangle T ∈ distTriang C) ↔
      (∀ p : WalkingPair, T p ∈ distTriang C)
```

## Tag 05QT, a lemma

[Tag 05QT](https://stacks.math.columbia.edu/tag/05QT) in the Stacks Project.

**`CategoryTheory.Pretriangulated.isIso_biprod_desc_of_distTriang`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Elementary.lean, line 271](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Elementary.lean#L271). The attribute's comment: “(2): for any right inverse `s` of `g`, the map `f ⊕ s : X ⊕ Z ⟶ Y` is an isomorphism.”.

> Let `T = (X, Y, Z, f, g, h)` be a distinguished triangle in a
> pre-triangulated category. For any right inverse `s : Z ⟶ Y` of `g`, the map
> `f ⊕ s : X ⊕ Z ⟶ Y` is an isomorphism.

```lean
theorem isIso_biprod_desc_of_distTriang (T : Triangle C) (hT : T ∈ distTriang C)
    (s : T.obj₃ ⟶ T.obj₂) (hs : s ≫ T.mor₂ = 𝟙 T.obj₃) :
    IsIso (biprod.desc T.mor₁ s)
```

**`CategoryTheory.Pretriangulated.exists_section_mor₂_of_mor₃_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Elementary.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Elementary.lean#L280). The attribute's comment: “(1): if `h = 0`, then `g` has a right inverse `s : Z ⟶ Y`.”.

> Let `T = (X, Y, Z, f, g, h)` be a distinguished triangle in a pre-triangulated category.
> If `h = 0`, then `g` has a right inverse `s : Z ⟶ Y`.

```lean
theorem exists_section_mor₂_of_mor₃_eq_zero (T : Triangle C) (hT : T ∈ distTriang C)
    (h : T.mor₃ = 0) : ∃ s : T.obj₃ ⟶ T.obj₂, s ≫ T.mor₂ = 𝟙 T.obj₃
```

Declarations registered for the tag:

- [`CategoryTheory.Pretriangulated.binaryBiproductTriangle_distinguished`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pretriangulated.binaryBiproductTriangle_distinguished#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Triangulated/Elementary.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Elementary.lean#L287) (StacksFrontier): “(3): for any objects `X'`, `Z'` the triangle `(X', X' ⊕ Z', Z', (1, 0), (0, 1), 0)` is distinguished.”.

## Tag 05QU, a lemma

[Tag 05QU](https://stacks.math.columbia.edu/tag/05QU) in the Stacks Project.

**`hasKernel_iff_hasCokernel_iff_split`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Elementary.lean, line 1117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Elementary.lean#L1117).

> In a pre-triangulated category `C`, for a
> morphism `f : X ⟶ Y` the following are equivalent:
>
> 1. `f` has a kernel;
> 2. `f` has a cokernel;
> 3. there are objects `K, Z, Q` with `f` isomorphic, in the arrow category, to the
>    composite of the second projection `K ⊞ Z ⟶ Z` with the first coprojection
>    `Z ⟶ Z ⊞ Q`, namely `biprod.snd ≫ biprod.inl`.

```lean
theorem hasKernel_iff_hasCokernel_iff_split (C : Type*) [Category C] [HasZeroObject C]
    [Preadditive C] [HasShift C ℤ] [∀ n : ℤ, (shiftFunctor C n).Additive] [Pretriangulated C]
    {X Y : C} (f : X ⟶ Y) :
    [HasKernel f,
     HasCokernel f,
     ∃ (K Z Q : C),
       Nonempty (Arrow.mk f ≅ Arrow.mk (biprod.snd ≫ biprod.inl : K ⊞ Z ⟶ Z ⊞ Q))].TFAE
```

## Tag 0CRG, a lemma

[Tag 0CRG](https://stacks.math.columbia.edu/tag/0CRG) in the Stacks Project.

**`CategoryTheory.Pretriangulated.shiftFunctor_preservesProductsCoproducts_and_productCoproductTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Elementary.lean, line 485](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Elementary.lean#L485).

> Let `C` be a pre-triangulated category and `I` an index type.
> (1)(a) The shift functors preserve `I`-indexed products, i.e. if `∏ Xᵢ` exists then
> `(∏ Xᵢ)⟦n⟧` together with the shifted projections is a product of the `Xᵢ⟦n⟧`;
> (1)(b) dually, they preserve `I`-indexed coproducts.
> (2)(a) If `Xᵢ → Yᵢ → Zᵢ → Xᵢ⟦1⟧` is a family of distinguished triangles whose products
> exist, then `∏ Xᵢ → ∏ Yᵢ → ∏ Zᵢ → (∏ Xᵢ)⟦1⟧` is distinguished;
> (2)(b) if their coproducts exist, then `∐ Xᵢ → ∐ Yᵢ → ∐ Zᵢ → (∐ Xᵢ)⟦1⟧` is distinguished.

```lean
theorem
    shiftFunctor_preservesProductsCoproducts_and_productCoproductTriangle_distinguished
    (I : Type w) :
    (∀ n : ℤ, PreservesLimitsOfShape (Discrete I) (CategoryTheory.shiftFunctor C n)) ∧
    (∀ n : ℤ, PreservesColimitsOfShape (Discrete I) (CategoryTheory.shiftFunctor C n)) ∧
    (∀ T : I → Triangle C, (∀ i, T i ∈ distTriang C) →
      ∀ [HasProduct fun i => (T i).obj₁] [HasProduct fun i => (T i).obj₂]
        [HasProduct fun i => (T i).obj₃] [HasProduct fun i => (T i).obj₁⟦(1 : ℤ)⟧],
        productTriangle T ∈ distTriang C) ∧
    (∀ T : I → Triangle C, (∀ i, T i ∈ distTriang C) →
      ∀ [HasCoproduct fun i => (T i).obj₁] [HasCoproduct fun i => (T i).obj₂]
        [HasCoproduct fun i => (T i).obj₃],
        Triangle.mk (Limits.Sigma.map fun i => (T i).mor₁)
            (Limits.Sigma.map fun i => (T i).mor₂)
            (Limits.Sigma.desc fun i =>
              (T i).mor₃ ≫ (Limits.Sigma.ι (fun i => (T i).obj₁) i)⟦(1 : ℤ)⟧') ∈
          distTriang C)
```

## Tag 05QW, a lemma

[Tag 05QW](https://stacks.math.columbia.edu/tag/05QW) in the Stacks Project.

**`CategoryTheory.Pretriangulated.isIdempotentComplete_of_hasCountableProducts_or_coproducts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Elementary.lean, line 341](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Elementary.lean#L341).

> A pre-triangulated category in which every object has a countable power
> `∏_{n : ℕ} Z` is Karoubian, i.e. idempotent complete; and so is one in which every object has a
> countable copower `∐_{n : ℕ} Z`. In particular a pre-triangulated category with countable
> products, or with countable coproducts, is Karoubian.

```lean
theorem isIdempotentComplete_of_hasCountableProducts_or_coproducts :
    (∀ [∀ Z : C, HasProduct fun _ : ℕ => Z], IsIdempotentComplete C) ∧
      (∀ [∀ Z : C, HasCoproduct fun _ : ℕ => Z], IsIdempotentComplete C)
```

## Tag 014C, a lemma

[Tag 014C](https://stacks.math.columbia.edu/tag/014C) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.IsTriangulated.mk'`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.IsTriangulated.mk'#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch13.lean#L37) (StacksFrontier).

## Tag 05QX, a lemma

[Tag 05QX](https://stacks.math.columbia.edu/tag/05QX) in the Stacks Project.

**`Stacks.Triangulated.SubcategoryWithTriangles.statement1`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Functor.lean, line 748](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Functor.lean#L748).

> **Statement 1** (Tag 05QX, equivalence of (1) and (2)). For an additive full
> subcategory `D'` (described by `P`) of a pre-triangulated category `D`,
> condition (1) (there *exists* a set `T'` making `(D', T')` a pre-triangulated
> subcategory) is equivalent to condition (2).
>
> PROOF SKETCH. `(1) ⇒ (2)`: destruct the existential witness `T'` and apply
> `condition2_of_isPretri` (Sub-lemma C). `(2) ⇒ (1)`: provide
> `restrictedTriangles P` as the witness, valid by `restrictedTriangles_isPretri`
> (Sub-lemma D).

```lean
theorem statement1 (P : ObjectProperty C)
    (hP : IsAdditiveFullSubcategory P) :
    Condition1 P ↔ Condition2 P
```

**`Stacks.Triangulated.SubcategoryWithTriangles.statement2`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Functor.lean, line 772](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Functor.lean#L772).

> **Statement 2** (Tag 05QX, characterization of `T'`). When the equivalent
> conditions hold, the set `T'` is uniquely determined: *any* `T'` making
> `(D', T')` a pre-triangulated subcategory coincides with the set of all
> distinguished triangles of `D` whose three vertices lie in `D'`
> (`restrictedTriangles P`), and this set indeed makes `(D', T')` a
> pre-triangulated subcategory.
>
> The two conjuncts express precisely this: (a) any valid `T'` equals
> `restrictedTriangles P` (uniqueness, quantified over an arbitrary candidate
> `T'`), and (b) `restrictedTriangles P` is itself valid (given condition (2)).
>
> PROOF SKETCH. The first conjunct is `unique_restrictedTriangles` (Sub-lemma E),
> applied to each candidate `T'`. The second conjunct is
> `restrictedTriangles_isPretri` (Sub-lemma D).

```lean
theorem statement2 (P : ObjectProperty C)
    (hP : IsAdditiveFullSubcategory P) :
    (∀ T' : Set (Triangle C),
        IsPretriangulatedSubcategoryWithTriangles P T' →
          T' = restrictedTriangles P) ∧
      (Condition2 P →
        IsPretriangulatedSubcategoryWithTriangles P (restrictedTriangles P))
```

**`Stacks.Triangulated.SubcategoryWithTriangles.statement3`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Functor.lean, line 803](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Functor.lean#L803).

> **Statement 3** (Tag 05QX, the triangulated case). If `D` is moreover a
> triangulated category (it satisfies the octahedral condition TR4), then
> conditions (1) and (2) are further equivalent to:
> `(D', restrictedTriangles P)` is a *triangulated* subcategory of `D`, i.e. it is
> a pre-triangulated subcategory whose induced pre-triangulated structure on `D'`
> again satisfies TR4 (the octahedral axiom internal to `D'`, with the full
> morphism-of-triangles compatibility conditions).
>
> PROOF SKETCH. First conjunct `Condition1 P ↔ Condition2 P`: this is exactly
> `statement1 P hP`. Second conjunct `Condition2 P ↔
> IsTriangulatedSubcategoryWithTriangles P (restrictedTriangles P)`:
> * `(⇒)`: from `Condition2 P`, the pre-triangulated half is
>   `restrictedTriangles_isPretri P hP h2` (Sub-lemma D), and the octahedral half
>   is `internalTR4_restrictedTriangles P hP` (Sub-lemma F); package them into the
>   `IsTriangulatedSubcategoryWithTriangles` structure (constructor from its
>   `toIsPretriangulatedSubcategoryWithTriangles` field plus `internalTR4`).
> * `(⇐)`: an `IsTriangulatedSubcategoryWithTriangles P (restrictedTriangles P)`
>   contains (via `.toIsPretriangulatedSubcategoryWithTriangles`) a witness for
>   `Condition1 P`; convert to `Condition2 P` through `condition2_of_isPretri`
>   (Sub-lemma C), or equivalently the forward direction of `statement1`.

```lean
theorem statement3 (P : ObjectProperty C)
    (hP : IsAdditiveFullSubcategory P) [IsTriangulated C] :
    (Condition1 P ↔ Condition2 P) ∧
      (Condition2 P ↔
        IsTriangulatedSubcategoryWithTriangles P (restrictedTriangles P))
```

## Tag 05QY, a lemma

[Tag 05QY](https://stacks.math.columbia.edu/tag/05QY) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.IsTriangulated.instAdditive`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.IsTriangulated.instAdditive#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Triangulated/Functor.lean, line 823](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Functor.lean#L823) (StacksFrontier).

## Tag 05SQ, a lemma

[Tag 05SQ](https://stacks.math.columbia.edu/tag/05SQ) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.map_distinguished_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.map_distinguished_iff#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Triangulated/Elementary.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Elementary.lean#L114) (StacksFrontier).

## Tag 014Y, a lemma

[Tag 014Y](https://stacks.math.columbia.edu/tag/014Y) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.IsTriangulated.instComp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.IsTriangulated.instComp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch13.lean#L22) (StacksFrontier).

## Tag 05QZ, a lemma

[Tag 05QZ](https://stacks.math.columbia.edu/tag/05QZ) in the Stacks Project.

**`main_statement_comp_triangulated_homological`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/HomologicalFunctor.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/HomologicalFunctor.lean#L84). The attribute's comment: “(1)”.

> **Statement 1** (Stacks 13.4.20, first part). If `F : D' → D` is an exact
> (triangulated) functor between pre-triangulated categories and `H : D → A` is a
> homological functor to an abelian category, then the composition `F ⋙ H` is a
> homological functor.

```lean
theorem main_statement_comp_triangulated_homological
    {D' : Type u₁} {D : Type u₂} {A : Type u₃}
    [Category.{v₁} D'] [Category.{v₂} D] [Category.{v₃} A]
    [HasShift D' ℤ] [HasShift D ℤ]
    [HasZeroObject D'] [HasZeroObject D]
    [Preadditive D'] [Preadditive D]
    [∀ (n : ℤ), (shiftFunctor D' n).Additive] [∀ (n : ℤ), (shiftFunctor D n).Additive]
    [Pretriangulated D'] [Pretriangulated D] [Abelian A]
    (F : D' ⥤ D) [F.CommShift ℤ] [F.IsTriangulated]
    (H : D ⥤ A) [H.IsHomological] :
    (F ⋙ H).IsHomological
```

**`main_statement_comp_homological_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/HomologicalFunctor.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/HomologicalFunctor.lean#L105). The attribute's comment: “(2)”.

> **Statement 2** (Stacks 13.4.20, second part). If `H : D → A` is a
> homological functor and `G : A → A'` is an exact functor of abelian categories
> (additive and preserving finite limits and colimits), then the composition
> `H ⋙ G` is a homological functor.

```lean
theorem main_statement_comp_homological_exact
    {D : Type u₁} {A : Type u₂} {A' : Type u₃}
    [Category.{v₁} D] [Category.{v₂} A] [Category.{v₃} A']
    [HasShift D ℤ] [HasZeroObject D] [Preadditive D]
    [∀ (n : ℤ), (shiftFunctor D n).Additive]
    [Pretriangulated D] [Abelian A] [Abelian A']
    (H : D ⥤ A) [H.IsHomological]
    (G : A ⥤ A') [G.Additive] [PreservesFiniteLimits G] [PreservesFiniteColimits G] :
    (H ⋙ G).IsHomological
```

## Tag 0151, a lemma

[Tag 0151](https://stacks.math.columbia.edu/tag/0151) in the Stacks Project.

**`CategoryTheory.Functor.DeltaFunctorStructure.comp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Functor.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Functor.lean#L164). The attribute's comment: “(1)”.

> **Stacks 0151 (1).** If `G : 𝒜 ⥤ 𝒟` is a `δ`-functor and `F : 𝒟 ⥤ 𝒟'` is an exact functor
> of pre-triangulated categories, then `F ∘ G` is a `δ`-functor, with connecting morphisms
> `δ'_{A → B → C} = ξ_{G(A)} ∘ F(δ_{A → B → C})`, where `ξ : F(X⟦1⟧) ≅ F(X)⟦1⟧` is the
> commutation of `F` with the shift (`DeltaFunctorStructure.comp_δ`).

```lean
public noncomputable def DeltaFunctorStructure.comp (d : G.DeltaFunctorStructure 𝒜 𝒟)
    {𝒟' : Type u₃} [Category.{v₃} 𝒟'] [HasZeroObject 𝒟'] [HasShift 𝒟' ℤ] [Preadditive 𝒟']
    [∀ n : ℤ, (shiftFunctor 𝒟' n).Additive] [Pretriangulated 𝒟']
    (F : 𝒟 ⥤ 𝒟') [F.CommShift ℤ] [F.IsTriangulated] :
    (G ⋙ F).DeltaFunctorStructure 𝒜 𝒟'
```

**`CategoryTheory.Functor.DeltaFunctorStructure.precomp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Functor.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Functor.lean#L180). The attribute's comment: “(2)”.

> **Stacks 0151 (2).** If `G : 𝒜 ⥤ 𝒟` is a `δ`-functor and `H : 𝒜' ⥤ 𝒜` is an exact functor
> of abelian categories, then `G ∘ H` is a `δ`-functor, with connecting morphisms
> `δ''_{A → B → C} = δ_{H(A) → H(B) → H(C)}` (`DeltaFunctorStructure.precomp_δ`).

```lean
public noncomputable def DeltaFunctorStructure.precomp (d : G.DeltaFunctorStructure 𝒜 𝒟)
    {𝒜' : Type u₄} [Category.{v₄} 𝒜'] [Abelian 𝒜'] (H : 𝒜' ⥤ 𝒜)
    [H.PreservesZeroMorphisms] [PreservesFiniteLimits H] [PreservesFiniteColimits H] :
    (H ⋙ G).DeltaFunctorStructure 𝒜' 𝒟
```

## Tag 05SR, a lemma

[Tag 05SR](https://stacks.math.columbia.edu/tag/05SR) in the Stacks Project.

**`CategoryTheory.Functor.DeltaFunctorStructure.isCohomologicalDeltaFunctor_comp_shift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Elementary.lean, line 784](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Elementary.lean#L784).

> A homological functor composed with a `δ`-functor is a cohomological `δ`-functor. Let
> `G : 𝒜 ⥤ 𝒟` be a `δ`-functor from an abelian category to a pre-triangulated category, with
> `δ`-functor structure `h`, let `H : 𝒟 ⥤ ℬ` be a homological functor into an abelian category, and
> assume `H ⁻¹(G(A)) = 0` for every `A` in `𝒜`. Let `δ` be the connecting
> morphism `H ⁿ(G(C)) ⟶ H ⁿ⁺¹(G(A))` that the long exact homology sequence of `H` attaches to the
> image under `G` of a short exact sequence `0 ⟶ A ⟶ B ⟶ C ⟶ 0` of `𝒜`. Then
> `{H ⁿ ∘ G, δ}_{n ≥ 0}` is a cohomological `δ`-functor from `𝒜` to `ℬ`: the functors `H ⁿ ∘ G`
> are additive, the sequence
> `0 ⟶ H ⁰(G(A)) ⟶ H ⁰(G(B)) ⟶ H ⁰(G(C)) ⟶ H ¹(G(A)) ⟶ H ¹(G(B)) ⟶ ⋯` is exact, and `δ` is
> natural in the short exact sequence.

```lean
theorem isCohomologicalDeltaFunctor_comp_shift (h : DeltaFunctorStructure 𝒜 𝒟 G)
    (H : 𝒟 ⥤ ℬ) [H.IsHomological] [H.ShiftSequence ℤ]
    (hH : ∀ A : 𝒜, IsZero ((H.shift (-1 : ℤ)).obj (G.obj A)))
    (δ : ∀ {S : ShortComplex 𝒜}, S.ShortExact → ∀ n : ℕ,
      (G ⋙ H.shift (n : ℤ)).obj S.X₃ ⟶ (G ⋙ H.shift ((n : ℤ) + 1)).obj S.X₁)
    (hδ : ∀ {S : ShortComplex 𝒜} (hS : S.ShortExact) (n : ℕ), δ hS n =
      H.homologySequenceδ (Triangle.mk (G.map S.f) (G.map S.g) (h.δ hS)) n ((n : ℤ) + 1) rfl) :
    (∀ n : ℕ, (G ⋙ H.shift (n : ℤ)).Additive) ∧
    (∀ {S : ShortComplex 𝒜}, S.ShortExact → Mono ((G ⋙ H.shift (0 : ℤ)).map S.f)) ∧
    (∀ {S : ShortComplex 𝒜} (_ : S.ShortExact) (n : ℕ),
      ∃ hz : (G ⋙ H.shift (n : ℤ)).map S.f ≫ (G ⋙ H.shift (n : ℤ)).map S.g = 0,
        (ShortComplex.mk _ _ hz).Exact) ∧
    (∀ {S : ShortComplex 𝒜} (hS : S.ShortExact) (n : ℕ),
      ∃ hz : (G ⋙ H.shift (n : ℤ)).map S.g ≫ δ hS n = 0,
        (ShortComplex.mk _ _ hz).Exact) ∧
    (∀ {S : ShortComplex 𝒜} (hS : S.ShortExact) (n : ℕ),
      ∃ hz : δ hS n ≫ (G ⋙ H.shift ((n : ℤ) + 1)).map S.f = 0,
        (ShortComplex.mk _ _ hz).Exact) ∧
    (∀ {S S' : ShortComplex 𝒜} (hS : S.ShortExact) (hS' : S'.ShortExact) (φ : S ⟶ S') (n : ℕ),
      (G ⋙ H.shift (n : ℤ)).map φ.τ₃ ≫ δ hS' n =
        δ hS n ≫ (G ⋙ H.shift ((n : ℤ) + 1)).map φ.τ₁)
```

## Tag 05R0, a proposition

[Tag 05R0](https://stacks.math.columbia.edu/tag/05R0) in the Stacks Project.

**`CategoryTheory.Triangulated.exists_nine_diagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Elementary.lean, line 659](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Elementary.lean#L659).

> Let `C` be a triangulated category. Given a commutative square
> `u₁ ≫ b₁ = a₁ ≫ v₁` and distinguished triangles `(u₁, u₂, u₃)`, `(v₁, v₂, v₃)` on its two
> horizontal morphisms and `(a₁, a₂, a₃)`, `(b₁, b₂, b₃)` on its two vertical ones, there are an
> object `Z''`, a third row `(w₁, w₂, w₃)` and a third column `(c₁, c₂, c₃)`, both distinguished
> triangles, such that the resulting `4 × 4` diagram — whose fourth row and fourth column are the
> first row and the first column shifted by `1` — has all its squares commutative, except the
> lower right one, which anticommutes.

```lean
theorem exists_nine_diagram {X Y Z X' Y' Z' X'' Y'' : C}
    {u₁ : X ⟶ Y} {u₂ : Y ⟶ Z} {u₃ : Z ⟶ X⟦(1 : ℤ)⟧}
    (hu : Triangle.mk u₁ u₂ u₃ ∈ distTriang C)
    {v₁ : X' ⟶ Y'} {v₂ : Y' ⟶ Z'} {v₃ : Z' ⟶ X'⟦(1 : ℤ)⟧}
    (hv : Triangle.mk v₁ v₂ v₃ ∈ distTriang C)
    {a₁ : X ⟶ X'} {a₂ : X' ⟶ X''} {a₃ : X'' ⟶ X⟦(1 : ℤ)⟧}
    (ha : Triangle.mk a₁ a₂ a₃ ∈ distTriang C)
    {b₁ : Y ⟶ Y'} {b₂ : Y' ⟶ Y''} {b₃ : Y'' ⟶ Y⟦(1 : ℤ)⟧}
    (hb : Triangle.mk b₁ b₂ b₃ ∈ distTriang C)
    (comm : u₁ ≫ b₁ = a₁ ≫ v₁) :
    ∃ (Z'' : C) (w₁ : X'' ⟶ Y'') (w₂ : Y'' ⟶ Z'') (w₃ : Z'' ⟶ X''⟦(1 : ℤ)⟧)
      (c₁ : Z ⟶ Z') (c₂ : Z' ⟶ Z'') (c₃ : Z'' ⟶ Z⟦(1 : ℤ)⟧),
      Triangle.mk w₁ w₂ w₃ ∈ distTriang C ∧ Triangle.mk c₁ c₂ c₃ ∈ distTriang C ∧
      u₂ ≫ c₁ = b₁ ≫ v₂ ∧ u₃ ≫ a₁⟦(1 : ℤ)⟧' = c₁ ≫ v₃ ∧
      v₁ ≫ b₂ = a₂ ≫ w₁ ∧ v₂ ≫ c₂ = b₂ ≫ w₂ ∧ v₃ ≫ a₂⟦(1 : ℤ)⟧' = c₂ ≫ w₃ ∧
      w₁ ≫ b₃ = a₃ ≫ u₁⟦(1 : ℤ)⟧' ∧ w₂ ≫ c₃ = b₃ ≫ u₂⟦(1 : ℤ)⟧' ∧
      w₃ ≫ a₃⟦(1 : ℤ)⟧' = -(c₃ ≫ u₃⟦(1 : ℤ)⟧')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.4, Tag 05QN](https://stacks.math.columbia.edu/tag/05QN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
