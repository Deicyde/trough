---
declaration: section
origin: cited
lean: HomotopyCategory.Pretriangulated.distinguishedTriangles, HomotopyCategory.distinguished_iff_iso_trianglehOfDegreewiseSplit, CochainComplex.trianglehOfDegreewiseSplit, exists_octahedron_of_termwiseSplitInj, HomotopyCategory.instIsTriangulatedIntUp, HomotopyCategory.instPretriangulatedIntUp, HomotopyCategory.isTriangulated_minus_bounded, CategoryTheory.Functor.isTriangulated_mapHomotopyCategoryMinus
statement: formalized
proof: formalized
---

# 13.10 Distinguished triangles in the homotopy category

Section 13.10 of the Stacks Project, [Tag 014P](https://stacks.math.columbia.edu/tag/014P). 7 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 014Q, a definition

[Tag 014Q](https://stacks.math.columbia.edu/tag/014Q) in the Stacks Project.

Declarations registered for the tag:

- [`HomotopyCategory.Pretriangulated.distinguishedTriangles`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomotopyCategory.Pretriangulated.distinguishedTriangles#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L82) (StacksFrontier): “the distinguished triangles of the homotopy category”. References: SGA 4½ Etat 0 (1.2.2); SGA 6 I (1.1.5), “partial”; SGA 4 XVII (1.1.1), “distinguished triangles”.
- [`HomotopyCategory.distinguished_iff_iso_trianglehOfDegreewiseSplit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomotopyCategory.distinguished_iff_iso_trianglehOfDegreewiseSplit#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L88) (StacksFrontier): “a triangle is distinguished iff it is isomorphic to the triangle of a termwise split exact sequence”. References: SGA 4 XVII (1.1.1), “distinguished <=> split”; SGA 4½ Etat 0 (1.2.4), “ρ essentially surjective”; SGA 7 XIII (1.4.2), “partial”.
- [`CochainComplex.trianglehOfDegreewiseSplit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.trianglehOfDegreewiseSplit#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L90) (StacksFrontier): “the triangle associated to a termwise split exact sequence”. References: SGA 7 XIII (1.4.2), “partial”; SGA 4½ Etat 0 (1.2.4), “triangle from semi-split”; SGA 4 XVII (1.1.1), “triangle of split seq”.

## Tag 014R, a lemma

[Tag 014R](https://stacks.math.columbia.edu/tag/014R) in the Stacks Project.

**`exists_octahedron_of_termwiseSplitInj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 1329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L1329).

> **Theorem (Stacks Tag 014R, Lemma 13.10.2).**
> Let `A` be an additive category and let `α : Acx → Bcx` and `β : Bcx → Ccx` be termwise split
> injections of complexes. Then there exist complexes `Q₁ Q₂ Q₃` of `A`, morphisms
> `p₁ : Q(Bcx) → Q(Q₁)`, `p₂ : Q(Ccx) → Q(Q₂)`, `p₃ : Q(Ccx) → Q(Q₃)` and connecting morphisms
> `d₁ : Q(Q₁) → Q(Acx)⟦1⟧`, `d₂ : Q(Q₂) → Q(Acx)⟦1⟧`, `d₃ : Q(Q₃) → Q(Bcx)⟦1⟧` in `K(A)` such that:
>
> * the three triangles
>   `(Q(Acx), Q(Bcx), Q(Q₁), Q(α), p₁, d₁)`,
>   `(Q(Acx), Q(Ccx), Q(Q₂), Q(β ∘ α), p₂, d₂)`,
>   `(Q(Bcx), Q(Ccx), Q(Q₃), Q(β), p₃, d₃)`
>   are distinguished triangles of `K(A)`; and
>
> * axiom TR4 (Definition 6) holds for these three distinguished triangles with respect to the
>   composable morphisms `Q(α)` and `Q(β)`.

```lean
theorem exists_octahedron_of_termwiseSplitInj
    {Acx Bcx Ccx : Cpx A}
    (α : TermwiseSplitInj Acx Bcx) (β : TermwiseSplitInj Bcx Ccx) :
    ∃ (Q₁ Q₂ Q₃ : Cpx A)
      (p₁ : (Qfun A).obj Bcx ⟶ (Qfun A).obj Q₁)
      (p₂ : (Qfun A).obj Ccx ⟶ (Qfun A).obj Q₂)
      (p₃ : (Qfun A).obj Ccx ⟶ (Qfun A).obj Q₃)
      (d₁ : (Qfun A).obj Q₁ ⟶ ((Qfun A).obj Acx)⟦(1 : ℤ)⟧)
      (d₂ : (Qfun A).obj Q₂ ⟶ ((Qfun A).obj Acx)⟦(1 : ℤ)⟧)
      (d₃ : (Qfun A).obj Q₃ ⟶ ((Qfun A).obj Bcx)⟦(1 : ℤ)⟧),
      -- The three distinguished triangles `(X, Y, Q(Q_i), f, p_i, d_i)`.
      letI T₁ : Triangle (HoCat A) := Triangle.mk ((Qfun A).map α.hom) p₁ d₁
      letI T₂ : Triangle (HoCat A) := Triangle.mk ((Qfun A).map (α.hom ≫ β.hom)) p₂ d₂
      letI T₃ : Triangle (HoCat A) := Triangle.mk ((Qfun A).map β.hom) p₃ d₃
      IsDistinguished T₁ ∧ IsDistinguished T₂ ∧ IsDistinguished T₃ ∧
      -- Axiom TR4 (Definition 6) for these three distinguished triangles, with respect to the
      -- composable morphisms `f = Q(α) : Q(Acx) → Q(Bcx)` and `g = Q(β) : Q(Bcx) → Q(Ccx)`.
      TR4Holds ((Qfun A).map α.hom) ((Qfun A).map β.hom) T₁ T₂ T₃
        rfl rfl rfl rfl rfl rfl
```

## Tag 014S, a proposition

[Tag 014S](https://stacks.math.columbia.edu/tag/014S) in the Stacks Project.

Declarations registered for the tag:

- [`HomotopyCategory.instIsTriangulatedIntUp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomotopyCategory.instIsTriangulatedIntUp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch13.lean#L60) (StacksFrontier): “`K(A)` with its translation functors and distinguished triangles is a triangulated category (TR4, on top of the pre-triangulated structure)”. References: SGA 4 Vbis (2.5.1), “more general”; SGA 4 XVII (2.2.9), “(i), special case”; SGA 4½ Etat 0 (1.2.2), “partial”; SGA 6 I (1.1.5), “K(C_X) is triangulated”.
- [`HomotopyCategory.instPretriangulatedIntUp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomotopyCategory.instPretriangulatedIntUp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch13.lean#L63) (StacksFrontier): “the pre-triangulated structure of `K(A)` (TR1, TR2, TR3)”. References: SGA 4 Vbis (2.5.1), “partial”; SGA 4 XVII (2.2.9), “(i)”; SGA 4½ Etat 0 (1.2.2), “partial”; SGA 6 I (1.1.5), “partial”.
- [`HomotopyCategory.distinguished_iff_iso_trianglehOfDegreewiseSplit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomotopyCategory.distinguished_iff_iso_trianglehOfDegreewiseSplit#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch13.lean#L65) (StacksFrontier): “Mathlib's distinguished triangles (mapping cones) are the Stacks ones: the triangles isomorphic to the triangle of a termwise split exact sequence”. References: SGA 4 XVII (1.1.1), “distinguished <=> split”; SGA 4½ Etat 0 (1.2.4), “ρ essentially surjective”; SGA 7 XIII (1.4.2), “partial”.

## Tag 05RQ, a lemma

[Tag 05RQ](https://stacks.math.columbia.edu/tag/05RQ) in the Stacks Project.

**`HomotopyCategory.isTriangulated_minus_bounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 559](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L559). The attribute's comment: “K⁻(A) and K^b(A); K⁺(A) is (HomotopyCategory.plus A).IsTriangulated”. References: SGA 6 I (1.1.5), “K^-, K^b triangulated”; SGA 4 XVII (2.2.10), “(A), special case”; SGA 4½ Etat 0 (1.2.3), “(A)”.

> **Stacks 05RQ.** Let `A` be an additive category. The categories `K⁻(A)` of complexes
> bounded above and `K^b(A)` of bounded complexes are full triangulated subcategories of `K(A)`.
> For `K⁺(A)` this is `(HomotopyCategory.plus A).IsTriangulated`.

```lean
public theorem isTriangulated_minus_bounded
    (A : Type*) [Category* A] [Preadditive A] [HasZeroObject A] [HasBinaryBiproducts A] :
    ((CochainComplex.minus A).strictMap (quotient A (ComplexShape.up ℤ))).IsTriangulated ∧
      ((CochainComplex.plus A ⊓ CochainComplex.minus A).strictMap
        (quotient A (ComplexShape.up ℤ))).IsTriangulated
```

## Tag 014X, a lemma

[Tag 014X](https://stacks.math.columbia.edu/tag/014X) in the Stacks Project.

**`CategoryTheory.Functor.isTriangulated_mapHomotopyCategoryMinus`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L355). The attribute's comment: “bounded-above homotopy categories”.

> **Stacks 014X (bounded above).** An additive functor induces an exact
> functor on bounded-above homotopy categories of cochain complexes.

```lean
instance isTriangulated_mapHomotopyCategoryMinus [HasZeroObject C] [HasBinaryBiproducts C]
    [HasZeroObject D] [HasBinaryBiproducts D] :
    F.mapHomotopyCategoryMinus.IsTriangulated
```

**`CategoryTheory.Functor.isTriangulated_mapHomotopyCategoryBounded`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L378). The attribute's comment: “bounded homotopy categories”.

> **Stacks 014X (bounded).** An additive functor induces an exact functor on
> bounded homotopy categories of cochain complexes.

```lean
instance isTriangulated_mapHomotopyCategoryBounded [HasZeroObject C] [HasBinaryBiproducts C]
    [HasZeroObject D] [HasBinaryBiproducts D] :
    F.mapHomotopyCategoryBounded.IsTriangulated
```

**`mapHomotopyCategory_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L393). The attribute's comment: “unbounded homotopy categories”. References: SGA 4 Vbis (2.5.1), “more general”; SGA 4 XVII (7.3.3), “special case”; SGA 6 I (1.1.5), “partial”.

> **Stacks 014X (unbounded).** An additive functor induces an exact functor
> on homotopy categories of cochain complexes.

```lean
theorem mapHomotopyCategory_isTriangulated
    (𝒜 𝓑 : Type*) [Category 𝒜] [Category 𝓑]
    [Preadditive 𝒜] [HasZeroObject 𝒜] [HasBinaryBiproducts 𝒜]
    [Preadditive 𝓑] [HasZeroObject 𝓑] [HasBinaryBiproducts 𝓑]
    (F : 𝒜 ⥤ 𝓑) [F.Additive] :
    (F.mapHomotopyCategory (ComplexShape.up ℤ)).IsTriangulated
```

**`mapHomotopyCategoryPlus_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L404). The attribute's comment: “bounded-below homotopy categories”.

> **Stacks 014X (bounded below).** An additive functor induces an exact
> functor on bounded-below homotopy categories of cochain complexes.

```lean
theorem mapHomotopyCategoryPlus_isTriangulated
    (𝒜 𝓑 : Type*) [Category 𝒜] [Category 𝓑]
    [Preadditive 𝒜] [HasZeroObject 𝒜] [HasBinaryBiproducts 𝒜]
    [Preadditive 𝓑] [HasZeroObject 𝓑] [HasBinaryBiproducts 𝓑]
    (F : 𝒜 ⥤ 𝓑) [F.Additive] :
    F.mapHomotopyCategoryPlus.IsTriangulated
```

## Tag 0G6C, a lemma

[Tag 0G6C](https://stacks.math.columbia.edu/tag/0G6C) in the Stacks Project.

**`HomotopyCategory.exists_trianglehOfDegreewiseSplit_of_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 593](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L593). References: SGA 4 XVII (1.1.1), “every antidist. arises”; SGA 4½ Etat 0 (1.2.4), “ρ ess. surjective”.

> **A distinguished triangle of `K(𝒜)` is the triangle of a degreewise split short exact
> sequence of complexes, after changing its middle term.** Let `𝒜` be an additive category and
> let `(A^•, B, C^•, a, b, c)` be a distinguished triangle of `K(𝒜)` whose outer terms are the
> complexes `A^•` and `C^•`. Then there are a complex `(B')^•` and maps `f : A^• ⟶ (B')^•`,
> `g : (B')^• ⟶ C^•` with `f ≫ g = 0` whose degreewise evaluations
> `0 → A^n → (B')^n → C^n → 0` are split short exact sequences, and an isomorphism
> `e : B ≅ (B')^•` in `K(𝒜)` with `a ≫ e = f`, `e ≫ g = b` and such that `c` is the connecting
> morphism of the sequence, i.e. `(𝟙, e, 𝟙)` is an isomorphism of distinguished triangles from
> `(A^•, B, C^•, a, b, c)` to `(A^•, (B')^•, C^•, f, g, c)`.

```lean
public theorem exists_trianglehOfDegreewiseSplit_of_distinguished
    {𝒜 : Type u} [Category.{v} 𝒜] [Preadditive 𝒜] [HasZeroObject 𝒜] [HasBinaryBiproducts 𝒜]
    {A C : CochainComplex 𝒜 ℤ} {B : HomotopyCategory 𝒜 (ComplexShape.up ℤ)}
    (a : (quotient 𝒜 (ComplexShape.up ℤ)).obj A ⟶ B)
    (b : B ⟶ (quotient 𝒜 (ComplexShape.up ℤ)).obj C)
    (c : (quotient 𝒜 (ComplexShape.up ℤ)).obj C ⟶
      ((quotient 𝒜 (ComplexShape.up ℤ)).obj A)⟦(1 : ℤ)⟧)
    (hT : Triangle.mk a b c ∈ distTriang (HomotopyCategory 𝒜 (ComplexShape.up ℤ))) :
    ∃ (B' : CochainComplex 𝒜 ℤ) (f : A ⟶ B') (g : B' ⟶ C) (w : f ≫ g = 0)
      (σ : ∀ n, ((ShortComplex.mk f g w).map (eval 𝒜 (ComplexShape.up ℤ) n)).Splitting)
      (e : B ≅ (quotient 𝒜 (ComplexShape.up ℤ)).obj B'),
      a ≫ e.hom = (quotient 𝒜 (ComplexShape.up ℤ)).map f ∧
        e.hom ≫ (quotient 𝒜 (ComplexShape.up ℤ)).map g = b ∧
        c = (trianglehOfDegreewiseSplit (.mk f g w) σ).mor₃
```

## Tag 0G6E, a remark

[Tag 0G6E](https://stacks.math.columbia.edu/tag/0G6E) in the Stacks Project.

**`Stacks.SheafOfModules.Tensor.bifunctor_homotopy_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/BifunctorReductionMachinery/TensorIsTriangulated.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/BifunctorReductionMachinery/TensorIsTriangulated.lean#L104). The attribute's comment: “(1)”. References: SGA 4 XVII (7.3.3), “special case”; SGA 4½ Etat 0 (1.3.3), “partial”.

> **The general reduction (Derived Categories, Remark 13.10.9 / tag 0G6E).**
> For additive categories `A, B, D` with `D` having the countable direct sums
> needed to form the relevant total complexes, and any functor `F : A ⥤ B ⥤ D`
> additive (bilinear on morphisms) in each variable, fixing one complex variable
> `G^•` and taking `Tot` of the resulting double complex yields an exact functor of
> homotopy categories `K(B) ⥤ K(D)` (here the fixed complex is the LEFT factor).
> Statements 1 and 2 are the instances `A = B = D = Mod(O)`, `F = ⊗_O = sheafTensor`.

```lean
theorem bifunctor_homotopy_isTriangulated
    {A B D : Type*} [Category A] [Category B] [Category D]
    [Preadditive A] [Preadditive B] [Preadditive D]
    [HasZeroObject A] [HasZeroObject B] [HasZeroObject D]
    [HasBinaryBiproducts A] [HasBinaryBiproducts B] [HasBinaryBiproducts D]
    (F : A ⥤ B ⥤ D) [F.Additive] [∀ X, (F.obj X).Additive]
    [∀ (K₁ : HomologicalComplex A (ComplexShape.up ℤ))
        (K₂ : HomologicalComplex B (ComplexShape.up ℤ)),
        K₁.HasMapBifunctor K₂ F (ComplexShape.up ℤ)]
    (G : HomologicalComplex A (ComplexShape.up ℤ)) :
    ∃ (Φ : HomotopyCategory B (ComplexShape.up ℤ) ⥤ HomotopyCategory D (ComplexShape.up ℤ))
      (ξ : Φ.CommShift ℤ),
      Φ.Additive ∧
        Nonempty (HomotopyCategory.quotient B (ComplexShape.up ℤ) ⋙ Φ ≅
          (F.map₂HomologicalComplex (ComplexShape.up ℤ) (ComplexShape.up ℤ)
              (ComplexShape.up ℤ)).obj G ⋙
            HomotopyCategory.quotient D (ComplexShape.up ℤ)) ∧
          (letI := ξ; Φ.IsTriangulated)
```

**`Stacks.SheafOfModules.Tensor.bifunctor_homotopy_flip_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/BifunctorReductionMachinery/TensorIsTriangulated.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/BifunctorReductionMachinery/TensorIsTriangulated.lean#L129). The attribute's comment: “(2)”. References: SGA 4 XVII (7.3.3), “special case”; SGA 4½ Etat 0 (1.3.3), “partial”.

> **Stacks 0G6E (2).** The right-variable version of
> `bifunctor_homotopy_isTriangulated`: fixing a complex of `B` and totalizing in the `A`
> variable gives an exact functor `K(A) ⟶ K(D)`.

```lean
theorem bifunctor_homotopy_flip_isTriangulated
    {A B D : Type*} [Category A] [Category B] [Category D]
    [Preadditive A] [Preadditive B] [Preadditive D]
    [HasZeroObject A] [HasZeroObject B] [HasZeroObject D]
    [HasBinaryBiproducts A] [HasBinaryBiproducts B] [HasBinaryBiproducts D]
    (F : A ⥤ B ⥤ D) [F.Additive] [∀ X, (F.obj X).Additive]
    [∀ (K₁ : HomologicalComplex A (ComplexShape.up ℤ))
        (K₂ : HomologicalComplex B (ComplexShape.up ℤ)),
        K₁.HasMapBifunctor K₂ F (ComplexShape.up ℤ)]
    (G : HomologicalComplex B (ComplexShape.up ℤ)) :
    ∃ (Φ : HomotopyCategory A (ComplexShape.up ℤ) ⥤
        HomotopyCategory D (ComplexShape.up ℤ))
      (ξ : Φ.CommShift ℤ),
      Φ.Additive ∧
        Nonempty (HomotopyCategory.quotient A (ComplexShape.up ℤ) ⋙ Φ ≅
          (F.map₂HomologicalComplex (ComplexShape.up ℤ) (ComplexShape.up ℤ)
              (ComplexShape.up ℤ)).flip.obj G ⋙
            HomotopyCategory.quotient D (ComplexShape.up ℤ)) ∧
          (letI := ξ; Φ.IsTriangulated)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.10, Tag 014P](https://stacks.math.columbia.edu/tag/014P)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
