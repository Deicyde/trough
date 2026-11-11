---
declaration: section
origin: cited
lean: CategoryTheory.Functor.IsRightDerivedValueAt, CategoryTheory.Functor.IsLeftDerivedValueAt, StacksDerivedFunctor.rightDerivedMap, StacksDerivedFunctor.rightDerivedMap_spec, StacksDerivedFunctor.rightDerivedMap_unique, StacksDerivedFunctor.leftDerivedMap, StacksDerivedFunctor.leftDerivedMap_spec, StacksDerivedFunctor.leftDerivedMap_unique
statement: formalized
proof: formalized
---

# 13.14 Derived functors in general

Section 13.14 of the Stacks Project, [Tag 05S7](https://stacks.math.columbia.edu/tag/05S7). 16 tags here are carried by 29 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05S9, a definition

[Tag 05S9](https://stacks.math.columbia.edu/tag/05S9) in the Stacks Project.

**`CategoryTheory.Functor.IsRightDerivedValueAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/DefinedAt.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/DefinedAt.lean#L171). References: SGA 4 XVII (1.2.1), “(ii)”; SGA 4 XVII (5.5.5), “right derivable at K”.

> **Stacks 05S9(1)**. The cocone `c` on the ind-object
> `X/W ⟶ 𝒟'`, `(s : X ⟶ X') ↦ F(X')`
> exhibits its vertex `c.pt` as a *value of the right derived functor `RF` at `X`*: the ind-object
> is essentially constant with value `c.pt`, i.e. there are an index `s₀` and a section
> `r : c.pt ⟶ F(X'₀)` of the coprojection at `s₀` such that every transition morphism of the
> ind-object factors through `r` after enlarging the index.
>
> Accordingly, `RF` *is defined at* `X` means `∃ c, F.IsRightDerivedValueAt W X c`, and the value
> `RF(X)` is `c.pt`.

```lean
public def IsRightDerivedValueAt (F : D ⥤ D') (W : MorphismProperty D) (X : D)
    (c : Cocone (MorphismProperty.Under.forget W ⊤ X ⋙ Under.forget X ⋙ F)) : Prop
```

**`CategoryTheory.Functor.IsLeftDerivedValueAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/DefinedAt.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/DefinedAt.lean#L188). References: SGA 4 XVII (5.5.5), “left derivable at K”.

> **Stacks 05S9(2)**. The cone `c` on the pro-object
> `W/X ⟶ 𝒟'`, `(s : X' ⟶ X) ↦ F(X')`
> exhibits its vertex `c.pt` as a *value of the left derived functor `LF` at `X`*: the pro-object
> is essentially constant with value `c.pt`, i.e. there are an index `s₀` and a retraction
> `r : F(X'₀) ⟶ c.pt` of the projection at `s₀` such that every transition morphism of the
> pro-object factors through `r` after refining the index.
>
> Accordingly, `LF` *is defined at* `X` means `∃ c, F.IsLeftDerivedValueAt W X c`, and the value
> `LF(X)` is `c.pt`.

```lean
public def IsLeftDerivedValueAt (F : D ⥤ D') (W : MorphismProperty D) (X : D)
    (c : Cone (MorphismProperty.Over.forget W ⊤ X ⋙ Over.forget X ⋙ F)) : Prop
```

## Tag 05SA, a lemma

[Tag 05SA](https://stacks.math.columbia.edu/tag/05SA) in the Stacks Project.

**`StacksDerivedFunctor.rightDerivedMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Morphisms.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Morphisms.lean#L415). The attribute's comment: “(1), the morphism itself; `rightDerivedMap_spec` is its defining property and `rightDerivedMap_unique` is its uniqueness”.

> The morphism `RF(f) : RF X ⟶ RF Y` induced by `f : X ⟶ Y` between two values, characterised
> by `rightDerivedMap_spec` together with `rightDerivedMap_unique`.

```lean
noncomputable def rightDerivedMap [S.HasLeftCalculusOfFractions]
    (hX : F.IsRightDerivedValueAt S X cX) (_hY : F.IsRightDerivedValueAt S Y cY) (f : X ⟶ Y) :
    cX.pt ⟶ cY.pt
```

**`StacksDerivedFunctor.rightDerivedMap_spec`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Morphisms.lean, line 422](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Morphisms.lean#L422). The attribute's comment: “(1), the defining property of `rightDerivedMap`”.

> `RF(f)` makes each square of Statement 1 commute.

```lean
lemma rightDerivedMap_spec [S.HasLeftCalculusOfFractions]
    (hX : F.IsRightDerivedValueAt S X cX) (hY : F.IsRightDerivedValueAt S Y cY) (f : X ⟶ Y)
    (X' Y' : C) (s : X ⟶ X') (s' : Y ⟶ Y') (f' : X' ⟶ Y') (hs : S s) (hs' : S s')
    (hsq : f ≫ s' = s ≫ f') :
    cX.ι.app (Under.mk ⊤ s hs) ≫ rightDerivedMap S F hX hY f =
      F.map f' ≫ cY.ι.app (Under.mk ⊤ s' hs')
```

**`StacksDerivedFunctor.rightDerivedMap_unique`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Morphisms.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Morphisms.lean#L432). The attribute's comment: “(1), uniqueness of `rightDerivedMap`”.

> `RF(f)` is the only morphism with that property.

```lean
lemma rightDerivedMap_unique [S.HasLeftCalculusOfFractions]
    (hX : F.IsRightDerivedValueAt S X cX) (hY : F.IsRightDerivedValueAt S Y cY) (f : X ⟶ Y)
    (φ : cX.pt ⟶ cY.pt)
    (hφ : ∀ (X' Y' : C) (s : X ⟶ X') (s' : Y ⟶ Y') (f' : X' ⟶ Y')
      (hs : S s) (hs' : S s') (_ : f ≫ s' = s ≫ f'),
      cX.ι.app (Under.mk ⊤ s hs) ≫ φ = F.map f' ≫ cY.ι.app (Under.mk ⊤ s' hs')) :
    φ = rightDerivedMap S F hX hY f
```

**`StacksDerivedFunctor.leftDerivedMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Morphisms.lean, line 445](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Morphisms.lean#L445). The attribute's comment: “(2), the morphism itself; `leftDerivedMap_spec` is its defining property and `leftDerivedMap_unique` is its uniqueness”.

> The morphism `LF(f) : LF X ⟶ LF Y` induced by `f : X ⟶ Y` between two values, characterised
> by `leftDerivedMap_spec` together with `leftDerivedMap_unique`.

```lean
noncomputable def leftDerivedMap [S.HasRightCalculusOfFractions]
    (_hX : F.IsLeftDerivedValueAt S X dX) (hY : F.IsLeftDerivedValueAt S Y dY) (f : X ⟶ Y) :
    dX.pt ⟶ dY.pt
```

**`StacksDerivedFunctor.leftDerivedMap_spec`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Morphisms.lean, line 452](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Morphisms.lean#L452). The attribute's comment: “(2), the defining property of `leftDerivedMap`”.

> `LF(f)` makes each square of Statement 2 commute.

```lean
lemma leftDerivedMap_spec [S.HasRightCalculusOfFractions]
    (hX : F.IsLeftDerivedValueAt S X dX) (hY : F.IsLeftDerivedValueAt S Y dY) (f : X ⟶ Y)
    (X' Y' : C) (s : X' ⟶ X) (s' : Y' ⟶ Y) (f' : X' ⟶ Y') (hs : S s) (hs' : S s')
    (hsq : s ≫ f = f' ≫ s') :
    leftDerivedMap S F hX hY f ≫ dY.π.app (Over.mk ⊤ s' hs') =
      dX.π.app (Over.mk ⊤ s hs) ≫ F.map f'
```

**`StacksDerivedFunctor.leftDerivedMap_unique`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Morphisms.lean, line 462](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Morphisms.lean#L462). The attribute's comment: “(2), uniqueness of `leftDerivedMap`”.

> `LF(f)` is the only morphism with that property.

```lean
lemma leftDerivedMap_unique [S.HasRightCalculusOfFractions]
    (hX : F.IsLeftDerivedValueAt S X dX) (hY : F.IsLeftDerivedValueAt S Y dY) (f : X ⟶ Y)
    (φ : dX.pt ⟶ dY.pt)
    (hφ : ∀ (X' Y' : C) (s : X' ⟶ X) (s' : Y' ⟶ Y) (f' : X' ⟶ Y')
      (hs : S s) (hs' : S s') (_ : s ≫ f = f' ≫ s'),
      φ ≫ dY.π.app (Over.mk ⊤ s' hs') = dX.π.app (Over.mk ⊤ s hs) ≫ F.map f') :
    φ = leftDerivedMap S F hX hY f
```

## Tag 05SB, a lemma

[Tag 05SB](https://stacks.math.columbia.edu/tag/05SB) in the Stacks Project.

**`CategoryTheory.Functor.exists_isRightDerivedValueAt_iff_and_isIso_of_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Morphisms.lean, line 912](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Morphisms.lean#L912).

> **Stacks 05SB**(1). Let `F : C ⥤ H` be a functor, `W` a class of morphisms of
> `C` with left calculus of fractions and `s : X ⟶ Y` a morphism in `W`. Then:
>
> * the right derived functor of `F` is defined at `X` if and only if it is defined
>   at `Y`, definedness being essential constancy of the ind-object on `X/W` as in
>   Stacks 05S9;
> * if `c` is a value of `RF` at `X` and `d` is a value of `RF` at `Y`, there is a
>   morphism `φ : RF(X) ⟶ RF(Y)` compatible with the coprojections of `c` and `d`
>   along every square `a.hom ≫ f = s ≫ b.hom` — that is, the map `RF(s)` of Stacks
>   05SA — and `φ` is an isomorphism.
>
> Item (2) of the source, for the left derived functor, is this statement applied to
> `F.op`, `W.op` and `s.op`.

```lean
public theorem Functor.exists_isRightDerivedValueAt_iff_and_isIso_of_mem
    (F : C ⥤ H) (W : MorphismProperty C) [W.HasLeftCalculusOfFractions]
    {X Y : C} {s : X ⟶ Y} (hs : W s) :
    ((∃ c, F.IsRightDerivedValueAt W X c) ↔ (∃ d, F.IsRightDerivedValueAt W Y d)) ∧
      ∀ {c : Cocone (MorphismProperty.Under.forget W ⊤ X ⋙ Under.forget X ⋙ F)}
        {d : Cocone (MorphismProperty.Under.forget W ⊤ Y ⋙ Under.forget Y ⋙ F)},
        F.IsRightDerivedValueAt W X c → F.IsRightDerivedValueAt W Y d →
          ∃ φ : c.pt ⟶ d.pt,
            (∀ (a : W.Under ⊤ X) (b : W.Under ⊤ Y) (f : a.right ⟶ b.right),
              a.hom ≫ f = s ≫ b.hom → c.ι.app a ≫ φ = F.map f ≫ d.ι.app b) ∧ IsIso φ
```

## Tag 05SU, a lemma

[Tag 05SU](https://stacks.math.columbia.edu/tag/05SU) in the Stacks Project.

**`StacksDerivedShift.rightDerived_definedAt_iff_shift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Shift/ValueShift.lean, line 509](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Shift/ValueShift.lean#L509). The attribute's comment: “(1)”.

> **Statement (1) — `RF` and shifts (definedness biconditional).**
> `RF` is defined at `X` if and only if `RF` is defined at `X[n]`.

```lean
theorem rightDerived_definedAt_iff_shift (X : D) (n : ℤ) :
    (∃ c, F.IsRightDerivedValueAt S X c) ↔ ∃ c, F.IsRightDerivedValueAt S (X⟦n⟧) c
```

**`StacksDerivedShift.rightDerived_value_shift_iso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Shift/ValueShift.lean, line 524](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Shift/ValueShift.lean#L524). The attribute's comment: “(1)”.

> **Statement (1) — canonical isomorphism of values `RF(X)[n] ≅ RF(X[n])`.**
> Given a value `c` of `RF` at `X` and a value `d` of `RF` at `X[n]`, this is the canonical
> isomorphism `c.pt⟦n⟧ ≅ d.pt`, returned as genuine `Iso` *data*: `shiftCocone` exhibits
> `c.pt⟦n⟧` as a value at `X[n]`, a value is a colimit cocone, and the isomorphism is the
> comparison of the two colimit cocones.

```lean
noncomputable def rightDerived_value_shift_iso (X : D) (n : ℤ)
    {c : Cocone (MorphismProperty.Under.forget S ⊤ X ⋙ Under.forget X ⋙ F)}
    (hc : F.IsRightDerivedValueAt S X c)
    {d : Cocone (MorphismProperty.Under.forget S ⊤ (X⟦n⟧) ⋙ Under.forget (X⟦n⟧) ⋙ F)}
    (hd : F.IsRightDerivedValueAt S (X⟦n⟧) d) :
    c.pt⟦n⟧ ≅ d.pt
```

**`StacksDerivedShift.leftDerived_definedAt_iff_shift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Shift/ValueShift.lean, line 700](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Shift/ValueShift.lean#L700). The attribute's comment: “(2)”.

> **Statement (2) — `LF` and shifts (definedness biconditional).**
> `LF` is defined at `X` if and only if `LF` is defined at `X[n]`.

```lean
theorem leftDerived_definedAt_iff_shift (X : D) (n : ℤ) :
    (∃ c, F.IsLeftDerivedValueAt S X c) ↔ ∃ c, F.IsLeftDerivedValueAt S (X⟦n⟧) c
```

**`StacksDerivedShift.leftDerived_value_shift_iso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Shift/ValueShift.lean, line 714](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Shift/ValueShift.lean#L714). The attribute's comment: “(2)”.

> **Statement (2) — canonical isomorphism of values `LF(X)[n] ≅ LF(X[n])`.**
> Given a value `c` of `LF` at `X` and a value `d` of `LF` at `X[n]`, this is the canonical
> isomorphism `c.pt⟦n⟧ ≅ d.pt`: `shiftCone` exhibits `c.pt⟦n⟧` as a value at `X[n]`, a value is a
> limit cone, and the isomorphism is the comparison of the two limit cones.

```lean
noncomputable def leftDerived_value_shift_iso (X : D) (n : ℤ)
    {c : Cone (MorphismProperty.Over.forget S ⊤ X ⋙ Over.forget X ⋙ F)}
    (hc : F.IsLeftDerivedValueAt S X c)
    {d : Cone (MorphismProperty.Over.forget S ⊤ (X⟦n⟧) ⋙ Over.forget (X⟦n⟧) ⋙ F)}
    (hd : F.IsLeftDerivedValueAt S (X⟦n⟧) d) :
    c.pt⟦n⟧ ≅ d.pt
```

## Tag 05SC, a lemma

[Tag 05SC](https://stacks.math.columbia.edu/tag/05SC) in the Stacks Project.

**`CategoryTheory.Functor.exists_isRightDerivedValueAt_and_isLeftDerivedValueAt_and_triangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Triangle/LeftDerived.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Triangle/LeftDerived.lean#L394). References: SGA 4 XVII (1.2.2), “(ii)”.

> **Stacks 05SC**. Let `F : C ⥤ H` be an exact functor of pretriangulated categories and let
> `W` be a saturated multiplicative system in `C` (Stacks 05Q8) compatible with the triangulation.
> Let `T = (X, Y, Z, f, g, h)` be a distinguished triangle of `C`.
>
> If the right derived functor `RF` of `F` with respect to `W` is defined at two of `X`, `Y`, `Z`
> — that is, if for two of them the ind-object `(s : X ⟶ X') ↦ F(X')` over `X/W` is essentially
> constant — then it is defined at the third; moreover, for any values `RF(X)`, `RF(Y)`, `RF(Z)` at
> the three objects there are morphisms `RF(f)`, `RF(g)`, `RF(h)` between them, each characterised
> by compatibility with the coprojections as in Stacks 05SA, such that
> `(RF(X), RF(Y), RF(Z), RF(f), RF(g), RF(h))` is a distinguished triangle of `H`. That is the first
> conjunct.
>
> Similarly for the left derived functor `LF`, the second conjunct: if `LF` is defined at two of
> `X`, `Y`, `Z` — if for two of them the pro-object `(s : X' ⟶ X) ↦ F(X')` over `W/X` is essentially
> constant — then it is defined at the third, and for any values `LF(X)`, `LF(Y)`, `LF(Z)` there are
> morphisms `LF(f)`, `LF(g)`, `LF(h)`, each characterised by compatibility with the projections as
> in the dual of Stacks 05SA, such that `(LF(X), LF(Y), LF(Z), LF(f), LF(g), LF(h))` is a
> distinguished triangle of `H`.

```lean
public theorem exists_isRightDerivedValueAt_and_isLeftDerivedValueAt_and_triangle_distinguished
    (F : C ⥤ H) [F.CommShift ℤ] [F.IsTriangulated] (W : MorphismProperty C)
    (hW : W.IsSaturated) [W.IsCompatibleWithTriangulation]
    (T : Triangle C) (hT : T ∈ distTriang C) :
    (((∃ c, F.IsRightDerivedValueAt W T.obj₁ c) → (∃ c, F.IsRightDerivedValueAt W T.obj₂ c) →
          ∃ c, F.IsRightDerivedValueAt W T.obj₃ c) ∧
        ((∃ c, F.IsRightDerivedValueAt W T.obj₂ c) → (∃ c, F.IsRightDerivedValueAt W T.obj₃ c) →
          ∃ c, F.IsRightDerivedValueAt W T.obj₁ c) ∧
        ((∃ c, F.IsRightDerivedValueAt W T.obj₃ c) → (∃ c, F.IsRightDerivedValueAt W T.obj₁ c) →
          ∃ c, F.IsRightDerivedValueAt W T.obj₂ c) ∧
        ∀ (cX : Cocone (MorphismProperty.Under.forget W ⊤ T.obj₁ ⋙ Under.forget T.obj₁ ⋙ F))
          (_ : F.IsRightDerivedValueAt W T.obj₁ cX)
          (cY : Cocone (MorphismProperty.Under.forget W ⊤ T.obj₂ ⋙ Under.forget T.obj₂ ⋙ F))
          (_ : F.IsRightDerivedValueAt W T.obj₂ cY)
          (cZ : Cocone (MorphismProperty.Under.forget W ⊤ T.obj₃ ⋙ Under.forget T.obj₃ ⋙ F))
          (_ : F.IsRightDerivedValueAt W T.obj₃ cZ),
          ∃ (u : cX.pt ⟶ cY.pt) (v : cY.pt ⟶ cZ.pt) (w : cZ.pt ⟶ cX.pt⟦(1 : ℤ)⟧),
            Triangle.mk u v w ∈ distTriang H ∧
            (∀ (s : W.Under ⊤ T.obj₁) (t : W.Under ⊤ T.obj₂) (f' : s.right ⟶ t.right),
              T.mor₁ ≫ t.hom = s.hom ≫ f' → cX.ι.app s ≫ u = F.map f' ≫ cY.ι.app t) ∧
            (∀ (t : W.Under ⊤ T.obj₂) (r : W.Under ⊤ T.obj₃) (g' : t.right ⟶ r.right),
              T.mor₂ ≫ r.hom = t.hom ≫ g' → cY.ι.app t ≫ v = F.map g' ≫ cZ.ι.app r) ∧
            ∀ (r : W.Under ⊤ T.obj₃) (s : W.Under ⊤ T.obj₁) (h' : r.right ⟶ s.right⟦(1 : ℤ)⟧),
              T.mor₃ ≫ s.hom⟦(1 : ℤ)⟧' = r.hom ≫ h' →
                cZ.ι.app r ≫ w =
                  F.map h' ≫ (F.commShiftIso (1 : ℤ)).hom.app s.right ≫
                    (cX.ι.app s)⟦(1 : ℤ)⟧') ∧
      (((∃ c, F.IsLeftDerivedValueAt W T.obj₁ c) → (∃ c, F.IsLeftDerivedValueAt W T.obj₂ c) →
            ∃ c, F.IsLeftDerivedValueAt W T.obj₃ c) ∧
          ((∃ c, F.IsLeftDerivedValueAt W T.obj₂ c) → (∃ c, F.IsLeftDerivedValueAt W T.obj₃ c) →
            ∃ c, F.IsLeftDerivedValueAt W T.obj₁ c) ∧
          ((∃ c, F.IsLeftDerivedValueAt W T.obj₃ c) → (∃ c, F.IsLeftDerivedValueAt W T.obj₁ c) →
            ∃ c, F.IsLeftDerivedValueAt W T.obj₂ c) ∧
          ∀ (cX : Cone (MorphismProperty.Over.forget W ⊤ T.obj₁ ⋙ Over.forget T.obj₁ ⋙ F))
            (_ : F.IsLeftDerivedValueAt W T.obj₁ cX)
            (cY : Cone (MorphismProperty.Over.forget W ⊤ T.obj₂ ⋙ Over.forget T.obj₂ ⋙ F))
            (_ : F.IsLeftDerivedValueAt W T.obj₂ cY)
            (cZ : Cone (MorphismProperty.Over.forget W ⊤ T.obj₃ ⋙ Over.forget T.obj₃ ⋙ F))
            (_ : F.IsLeftDerivedValueAt W T.obj₃ cZ),
            ∃ (u : cX.pt ⟶ cY.pt) (v : cY.pt ⟶ cZ.pt) (w : cZ.pt ⟶ cX.pt⟦(1 : ℤ)⟧),
              Triangle.mk u v w ∈ distTriang H ∧
              (∀ (s : W.Over ⊤ T.obj₁) (t : W.Over ⊤ T.obj₂) (f' : s.left ⟶ t.left),
                s.hom ≫ T.mor₁ = f' ≫ t.hom → u ≫ cY.π.app t = cX.π.app s ≫ F.map f') ∧
              (∀ (t : W.Over ⊤ T.obj₂) (r : W.Over ⊤ T.obj₃) (g' : t.left ⟶ r.left),
                t.hom ≫ T.mor₂ = g' ≫ r.hom → v ≫ cZ.π.app r = cY.π.app t ≫ F.map g') ∧
              ∀ (r : W.Over ⊤ T.obj₃) (s : W.Over ⊤ T.obj₁) (h' : r.left ⟶ s.left⟦(1 : ℤ)⟧),
                r.hom ≫ T.mor₃ = h' ≫ s.hom⟦(1 : ℤ)⟧' →
                  w ≫ (cX.π.app s)⟦(1 : ℤ)⟧' =
                    cZ.π.app r ≫ F.map h' ≫ (F.commShiftIso (1 : ℤ)).hom.app s.left)
```

## Tag 05SD, a lemma

[Tag 05SD](https://stacks.math.columbia.edu/tag/05SD) in the Stacks Project.

**`CategoryTheory.Functor.exists_isDerivedValueAt_biprod_and_isIso_biprod_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Biprod.lean, line 895](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Biprod.lean#L895).

> **Stacks 05SD**. Let `F : C ⥤ H` be an exact functor of pretriangulated categories and let
> `W` be a saturated multiplicative system in `C` (Stacks 05Q8) compatible with the triangulation.
> Let `X` and `Y` be objects of `C` and write `X ⊞ Y` for their direct sum. Then, `RF` and `LF`
> being the right and left derived functors of `F` with respect to `W` and definedness and values
> being as in Stacks 05S9:
>
> 1. if `RF` is defined at `X` and at `Y`, then `RF` is defined at `X ⊞ Y`, and likewise for `LF`;
> 2. if `H` is Karoubian (`IsIdempotentComplete`) and `RF` is defined at `X ⊞ Y`, then `RF` is
>    defined at `X` and at `Y`, and likewise for `LF`;
>
> and in either case `RF(X ⊞ Y) = RF(X) ⊞ RF(Y)`: for values `cX`, `cY`, `cXY` of `RF` at `X`, `Y`
> and `X ⊞ Y` there are morphisms `p₁ : RF(X ⊞ Y) ⟶ RF(X)` and `p₂ : RF(X ⊞ Y) ⟶ RF(Y)`, namely
> the maps `RF(biprod.fst)` and `RF(biprod.snd)` of Stacks 05SA — each pinned by compatibility with
> the coprojections along every commutative square, which determines it uniquely — such that
> `biprod.lift p₁ p₂` is an isomorphism; and likewise for `LF`, with the projections of the
> cones.

```lean
public theorem exists_isDerivedValueAt_biprod_and_isIso_biprod_lift
    (F : C ⥤ H) [F.CommShift ℤ]
    [F.IsTriangulated] (W : MorphismProperty C) (hW : W.IsSaturated)
    [W.IsCompatibleWithTriangulation] (X Y : C) :
    -- (1) for `RF` and for `LF`
    ((∃ c, F.IsRightDerivedValueAt W X c) → (∃ c, F.IsRightDerivedValueAt W Y c) →
        ∃ c, F.IsRightDerivedValueAt W (X ⊞ Y) c) ∧
      ((∃ c, F.IsLeftDerivedValueAt W X c) → (∃ c, F.IsLeftDerivedValueAt W Y c) →
        ∃ c, F.IsLeftDerivedValueAt W (X ⊞ Y) c) ∧
      -- (2) for `RF` and for `LF`, over a Karoubian target
      (IsIdempotentComplete H → (∃ c, F.IsRightDerivedValueAt W (X ⊞ Y) c) →
        (∃ c, F.IsRightDerivedValueAt W X c) ∧ ∃ c, F.IsRightDerivedValueAt W Y c) ∧
      (IsIdempotentComplete H → (∃ c, F.IsLeftDerivedValueAt W (X ⊞ Y) c) →
        (∃ c, F.IsLeftDerivedValueAt W X c) ∧ ∃ c, F.IsLeftDerivedValueAt W Y c) ∧
      -- `RF(X ⊞ Y) = RF(X) ⊞ RF(Y)`
      (∀ (cX : Cocone (MorphismProperty.Under.forget W ⊤ X ⋙ Under.forget X ⋙ F))
        (_ : F.IsRightDerivedValueAt W X cX)
        (cY : Cocone (MorphismProperty.Under.forget W ⊤ Y ⋙ Under.forget Y ⋙ F))
        (_ : F.IsRightDerivedValueAt W Y cY)
        (cXY : Cocone (MorphismProperty.Under.forget W ⊤ (X ⊞ Y) ⋙ Under.forget (X ⊞ Y) ⋙ F))
        (_ : F.IsRightDerivedValueAt W (X ⊞ Y) cXY),
        ∃ (p₁ : cXY.pt ⟶ cX.pt) (p₂ : cXY.pt ⟶ cY.pt),
          (∀ (a : W.Under ⊤ (X ⊞ Y)) (b : W.Under ⊤ X) (g : a.right ⟶ b.right),
            biprod.fst ≫ b.hom = a.hom ≫ g → cXY.ι.app a ≫ p₁ = F.map g ≫ cX.ι.app b) ∧
          (∀ (a : W.Under ⊤ (X ⊞ Y)) (b : W.Under ⊤ Y) (g : a.right ⟶ b.right),
            biprod.snd ≫ b.hom = a.hom ≫ g → cXY.ι.app a ≫ p₂ = F.map g ≫ cY.ι.app b) ∧
          IsIso (biprod.lift p₁ p₂)) ∧
      -- `LF(X ⊞ Y) = LF(X) ⊞ LF(Y)`
      ∀ (cX : Cone (MorphismProperty.Over.forget W ⊤ X ⋙ Over.forget X ⋙ F))
        (_ : F.IsLeftDerivedValueAt W X cX)
        (cY : Cone (MorphismProperty.Over.forget W ⊤ Y ⋙ Over.forget Y ⋙ F))
        (_ : F.IsLeftDerivedValueAt W Y cY)
        (cXY : Cone (MorphismProperty.Over.forget W ⊤ (X ⊞ Y) ⋙ Over.forget (X ⊞ Y) ⋙ F))
        (_ : F.IsLeftDerivedValueAt W (X ⊞ Y) cXY),
        ∃ (p₁ : cXY.pt ⟶ cX.pt) (p₂ : cXY.pt ⟶ cY.pt),
          (∀ (a : W.Over ⊤ (X ⊞ Y)) (b : W.Over ⊤ X) (g : a.left ⟶ b.left),
            g ≫ b.hom = a.hom ≫ biprod.fst → p₁ ≫ cX.π.app b = cXY.π.app a ≫ F.map g) ∧
          (∀ (a : W.Over ⊤ (X ⊞ Y)) (b : W.Over ⊤ Y) (g : a.left ⟶ b.left),
            g ≫ b.hom = a.hom ≫ biprod.snd → p₂ ≫ cY.π.app b = cXY.π.app a ≫ F.map g) ∧
          IsIso (biprod.lift p₁ p₂)
```

## Tag 05SE, a proposition

[Tag 05SE](https://stacks.math.columbia.edu/tag/05SE) in the Stacks Project.

**`CategoryTheory.Functor.isTriangulated_and_exists_rightDerivedFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Subcategory.lean, line 1183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Subcategory.lean#L1183).

> **Stacks 05SE**. Let `F : C ⥤ H` be an exact functor of pre-triangulated categories, let `W`
> be a saturated multiplicative system in `C` (Stacks 05Q8) compatible with the triangulation, and
> let `E` be the full subcategory of `C` spanned by the objects at which the right derived functor
> `RF` is defined, i.e. at which the ind-object `(s : X ⟶ X') ↦ F(X')` on `X/W` has a value in the
> sense of Stacks 05S9. Let `L : C ⥤ D` be a localization functor for `W`, so that `D` is a model
> of `W⁻¹C`, pre-triangulated by Stacks 05R6. Then, writing `S_E = W.inverseImage E.ι` for the
> morphisms of `E` lying in `W`:
>
> 1. `E` is a strictly full triangulated subcategory of `C`;
> 2. `RF` is an exact functor `E ⥤ H`;
> 3. an element of `W` with source or target in `E` has both in `E`, hence is a morphism of `E`;
> 4. `RF` inverts every element of `S_E`;
> 5. `S_E` is a saturated multiplicative system in `E` compatible with the triangulation;
> 6. the induced functor `S_E⁻¹E ⥤ W⁻¹C` is fully faithful and exact;
> 7. `RF` factors through an exact functor `S_E⁻¹E ⥤ H`;
> 8. if `H` is Karoubian, `E` is a saturated (thick) triangulated subcategory of `C`.
>
> The functor `RF` is pinned by its values: `RF.obj X` is the vertex of a value cocone `ι X` of
> the ind-object at `X` (Stacks 05S9), and `RF.map f` is the unique map compatible with the
> coprojections along every commutative square with sides in `W` (Stacks 05SA). The functors of
> (6) and (7) are pinned as lifts through a localization functor `LE` of `E` at `S_E`. A similar
> result holds for `LF`, by this statement in the opposite categories.

```lean
public theorem isTriangulated_and_exists_rightDerivedFunctor
    (F : C ⥤ H) [F.CommShift ℤ] [F.IsTriangulated]
    (W : MorphismProperty C) (hW : W.IsSaturated) [W.IsCompatibleWithTriangulation]
    (E : ObjectProperty C) (hE : ∀ X, E X ↔ ∃ c, F.IsRightDerivedValueAt W X c)
    (L : C ⥤ D) [L.IsLocalization W] [L.CommShift ℤ] [L.Additive] :
    letI := hW.hasLeftCalculusOfFractions
    letI := Triangulated.Localization.pretriangulated L W
    -- (1) `E` is a strictly full triangulated subcategory of `C`
    ∃ (_ : E.IsClosedUnderIsomorphisms) (_ : E.IsTriangulated),
      -- (3) an element of `W` with source or target in `E` has both in `E`
      (∀ {X Y : C} (s : X ⟶ Y), W s → (E X ↔ E Y)) ∧
      -- (8) over a Karoubian target, `E` is saturated
      (IsIdempotentComplete H → E.IsSaturated) ∧
      -- (5) `S_E` is a saturated multiplicative system compatible with the triangulation
      ∃ (hSE : (W.inverseImage E.ι).IsSaturated)
        (_ : (W.inverseImage E.ι).IsCompatibleWithTriangulation)
        (RF : E.FullSubcategory ⥤ H) (_ : RF.CommShift ℤ)
        (ι : ∀ X : E.FullSubcategory, MorphismProperty.Under.forget W ⊤ X.obj ⋙
          Under.forget X.obj ⋙ F ⟶ (Functor.const (W.Under ⊤ X.obj)).obj (RF.obj X)),
        -- (2) `RF : E ⥤ H` is exact
        RF.IsTriangulated ∧
        -- its value at `X` is a value of `RF` at `X` (Stacks 05S9)
        (∀ X : E.FullSubcategory,
          F.IsRightDerivedValueAt W X.obj (Cocone.mk (RF.obj X) (ι X))) ∧
        -- and its action on morphisms is the map of Stacks 05SA
        (∀ {X Y : E.FullSubcategory} (f : X ⟶ Y) (a : W.Under ⊤ X.obj) (b : W.Under ⊤ Y.obj)
          (g : a.right ⟶ b.right), E.ι.map f ≫ b.hom = a.hom ≫ g →
            (ι X).app a ≫ RF.map f = F.map g ≫ (ι Y).app b) ∧
        -- (4) `RF` inverts `S_E`
        (W.inverseImage E.ι).IsInvertedBy RF ∧
        letI := hSE.hasLeftCalculusOfFractions
        ∀ (EL : Type u₄) [Category.{v₄} EL] [HasZeroObject EL] [HasShift EL ℤ] [Preadditive EL]
          [∀ n : ℤ, (shiftFunctor EL n).Additive] (LE : E.FullSubcategory ⥤ EL)
          [LE.IsLocalization (W.inverseImage E.ι)] [LE.CommShift ℤ] [LE.Additive],
          letI := Triangulated.Localization.pretriangulated LE (W.inverseImage E.ι)
          -- (6) `S_E⁻¹E ⥤ W⁻¹C` is fully faithful and exact
          (∀ (Φ : EL ⥤ D) [Lifting LE (W.inverseImage E.ι) (E.ι ⋙ L) Φ],
            Φ.Full ∧ Φ.Faithful ∧
              (letI := Functor.commShiftOfLocalization LE (W.inverseImage E.ι) ℤ (E.ι ⋙ L) Φ;
                Φ.IsTriangulated)) ∧
            -- (7) `RF` factors through an exact functor `S_E⁻¹E ⥤ H`
            ∀ (RF' : EL ⥤ H) [Lifting LE (W.inverseImage E.ι) RF RF'],
              letI := Functor.commShiftOfLocalization LE (W.inverseImage E.ι) ℤ RF RF';
              RF'.IsTriangulated
```

## Tag 05SV, a definition

[Tag 05SV](https://stacks.math.columbia.edu/tag/05SV) in the Stacks Project.

**`CategoryTheory.Functor.IsRightDerivable`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/DefinedAt.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/DefinedAt.lean#L285). References: SGA 4 XVII (1.2.1), “(iii)”.

> **Stacks 05SV(1)**. `F` is *right derivable* with respect to `W`, equivalently the right
> derived functor `RF` is *everywhere defined*: `RF` is defined at every object `X` of `𝒟`, i.e.
> every `X` carries a cocone on the ind-object `X/W ⟶ 𝒟'`, `(s : X ⟶ X') ↦ F(X')` exhibiting its
> vertex as a value `RF(X)` in the sense of `CategoryTheory.Functor.IsRightDerivedValueAt`.

```lean
public abbrev IsRightDerivable (F : D ⥤ D') (W : MorphismProperty D) : Prop
```

**`CategoryTheory.Functor.IsLeftDerivable`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/DefinedAt.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/DefinedAt.lean#L293).

> **Stacks 05SV(2)**. `F` is *left derivable* with respect to `W`, equivalently the left
> derived functor `LF` is *everywhere defined*: `LF` is defined at every object `X` of `𝒟`, i.e.
> every `X` carries a cone on the pro-object `W/X ⟶ 𝒟'`, `(s : X' ⟶ X) ↦ F(X')` exhibiting its
> vertex as a value `LF(X)` in the sense of `CategoryTheory.Functor.IsLeftDerivedValueAt`.

```lean
public abbrev IsLeftDerivable (F : D ⥤ D') (W : MorphismProperty D) : Prop
```

## Tag 05SW, an equation

[Tag 05SW](https://stacks.math.columbia.edu/tag/05SW) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.totalRightDerived`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.totalRightDerived#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch13.lean#L80) (StacksFrontier): “RF : S⁻¹D ⥤ D'”.
- [`CategoryTheory.Functor.totalLeftDerived`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.totalLeftDerived#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch13.lean#L81) (StacksFrontier): “LF : S⁻¹D ⥤ D'”.

## Tag 05SX, a definition

[Tag 05SX](https://stacks.math.columbia.edu/tag/05SX) in the Stacks Project.

**`CategoryTheory.Functor.ComputesRightDerived`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/DefinedAt.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/DefinedAt.lean#L402). References: SGA 4 XVII (1.2.1); SGA 4 XVII (5.5.5).

> **Stacks 05SX(1)**. The object `X` of `𝒟` *computes* the right derived functor `RF` of
> `F : 𝒟 ⥤ 𝒟'` relative to `W`: the right derived functor is defined at `X`, i.e. some cocone `c`
> on the ind-object `X/W ⟶ 𝒟'`, `(s : X ⟶ X') ↦ F(X')` exhibits its vertex as a value `RF(X)`, and
> the canonical map `F(X) ⟶ RF(X)` — the coprojection of `c` at the index `𝟙 X` — is an
> isomorphism.

```lean
public abbrev ComputesRightDerived (F : D ⥤ D') (W : MorphismProperty D)
    [W.ContainsIdentities] (X : D) : Prop
```

**`CategoryTheory.Functor.ComputesLeftDerived`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/DefinedAt.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/DefinedAt.lean#L413). References: SGA 4 XVII (5.5.5).

> **Stacks 05SX(2)**. The object `X` of `𝒟` *computes* the left derived functor `LF` of
> `F : 𝒟 ⥤ 𝒟'` relative to `W`: the left derived functor is defined at `X`, i.e. some cone `c` on
> the pro-object `W/X ⟶ 𝒟'`, `(s : X' ⟶ X) ↦ F(X')` exhibits its vertex as a value `LF(X)`, and
> the canonical map `LF(X) ⟶ F(X)` — the projection of `c` at the index `𝟙 X` — is an
> isomorphism.

```lean
public abbrev ComputesLeftDerived (F : D ⥤ D') (W : MorphismProperty D)
    [W.ContainsIdentities] (X : D) : Prop
```

## Tag 05SY, a lemma

[Tag 05SY](https://stacks.math.columbia.edu/tag/05SY) in the Stacks Project.

**`Stacks.DerivedFunctor.Shift.Situation.computesRightDerived_shift_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Shift/ComputesShift.lean, line 547](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Shift/ComputesShift.lean#L547). The attribute's comment: “(1)”.

> Stacks 13.14.11(1), Tag 05SY: `X` computes `RF` if and only if `X⟦n⟧` computes `RF`.
>
> The shift restricts to an equivalence `rightShiftEquiv` of the index categories, under which the
> ind-object at `X⟦n⟧` is the ind-object at `X` followed by `⟦n⟧` (`rightDiagramShiftIso`) and the
> index `𝟙 (X⟦n⟧)` corresponds to `𝟙 X`; essential constancy and invertibility of the canonical map
> are carried across. The converse applies this to `X⟦n⟧` and `-n` and uses
> `computesRightDerived_of_iso` along `X⟦n⟧⟦-n⟧ ≅ X`.

```lean
theorem computesRightDerived_shift_iff (X : sit.D) (n : ℤ) :
    sit.F.ComputesRightDerived sit.S X ↔ sit.F.ComputesRightDerived sit.S (X⟦n⟧)
```

**`Stacks.DerivedFunctor.Shift.Situation.computesLeftDerived_shift_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Shift/ComputesShift.lean, line 560](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Shift/ComputesShift.lean#L560). The attribute's comment: “(2)”.

> Stacks 13.14.11(2), Tag 05SY: `X` computes `LF` if and only if `X⟦n⟧` computes `LF`.
> Dual to `computesRightDerived_shift_iff`.

```lean
theorem computesLeftDerived_shift_iff (X : sit.D) (n : ℤ) :
    sit.F.ComputesLeftDerived sit.S X ↔ sit.F.ComputesLeftDerived sit.S (X⟦n⟧)
```

## Tag 05SZ, a lemma

[Tag 05SZ](https://stacks.math.columbia.edu/tag/05SZ) in the Stacks Project.

**`CategoryTheory.Functor.computesRightDerived_and_computesLeftDerived_of_distTriang`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Triangle/LeftDerived.lean, line 795](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Triangle/LeftDerived.lean#L795). References: SGA 4 XVII (1.2.2), “(i), special case”.

> **Stacks 05SZ**. Let `F : 𝒟 ⥤ 𝒟'` be an exact functor of pretriangulated categories and let
> `W` be a saturated multiplicative system in `𝒟` (Stacks 05Q8) compatible with the triangulation.
> Let `T = (X, Y, Z, f, g, h)` be a distinguished triangle of `𝒟`.
>
> If two of the three objects `X`, `Y`, `Z` compute the right derived functor `RF` — that is, `RF` is
> defined at each of them and the canonical map `F(-) ⟶ RF(-)` is an isomorphism there (Stacks 05SX)
> — then the third computes `RF` as well. Similarly for the left derived functor `LF`.
>
> The source states only the case where `X` and `Y` are assumed to compute; the other two positions
> are asserted as well because its applications use them (see the module docstring).

```lean
public theorem computesRightDerived_and_computesLeftDerived_of_distTriang (F : C ⥤ H)
    [F.CommShift ℤ] [F.IsTriangulated] (W : MorphismProperty C) [W.ContainsIdentities]
    (hW : W.IsSaturated) [W.IsCompatibleWithTriangulation]
    (T : Triangle C) (hT : T ∈ distTriang C) :
    (F.ComputesRightDerived W T.obj₁ → F.ComputesRightDerived W T.obj₂ →
        F.ComputesRightDerived W T.obj₃) ∧
      (F.ComputesRightDerived W T.obj₂ → F.ComputesRightDerived W T.obj₃ →
        F.ComputesRightDerived W T.obj₁) ∧
      (F.ComputesRightDerived W T.obj₃ → F.ComputesRightDerived W T.obj₁ →
        F.ComputesRightDerived W T.obj₂) ∧
      (F.ComputesLeftDerived W T.obj₁ → F.ComputesLeftDerived W T.obj₂ →
        F.ComputesLeftDerived W T.obj₃) ∧
      (F.ComputesLeftDerived W T.obj₂ → F.ComputesLeftDerived W T.obj₃ →
        F.ComputesLeftDerived W T.obj₁) ∧
      (F.ComputesLeftDerived W T.obj₃ → F.ComputesLeftDerived W T.obj₁ →
        F.ComputesLeftDerived W T.obj₂)
```

## Tag 05T0, a lemma

[Tag 05T0](https://stacks.math.columbia.edu/tag/05T0) in the Stacks Project.

**`CategoryTheory.Functor.computesRightDerived_and_computesLeftDerived_of_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Biprod.lean, line 1602](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Biprod.lean#L1602).

> **Stacks 05T0**. Let `F : 𝒟 ⥤ 𝒟'` be an additive functor of preadditive categories, `𝒟`
> having binary biproducts, and let `W` be a saturated multiplicative system in `𝒟` (Stacks 05Q8).
> Let `X` and `Y` be objects of `𝒟`. If the direct sum `X ⊞ Y` computes the right derived functor
> `RF` — that is, `RF` is defined at `X ⊞ Y` and the canonical map `F(X ⊞ Y) ⟶ RF(X ⊞ Y)` is an
> isomorphism (Stacks 05SX) — then `X` and `Y` compute `RF`. Similarly, if `X ⊞ Y` computes `LF`,
> then `X` and `Y` compute `LF`.
>
> Situation 05S8's triangulated hypotheses are not needed; see the module docstring.

```lean
public theorem computesRightDerived_and_computesLeftDerived_of_biprod (F : C ⥤ H) [F.Additive]
    (W : MorphismProperty C) [W.ContainsIdentities] (hW : W.IsSaturated) (X Y : C) :
    (F.ComputesRightDerived W (X ⊞ Y) →
        F.ComputesRightDerived W X ∧ F.ComputesRightDerived W Y) ∧
      (F.ComputesLeftDerived W (X ⊞ Y) →
        F.ComputesLeftDerived W X ∧ F.ComputesLeftDerived W Y)
```

## Tag 05T1, a lemma

[Tag 05T1](https://stacks.math.columbia.edu/tag/05T1) in the Stacks Project.

**`CategoryTheory.Functor.isRightDerivable_and_isLeftDerivable_of_forall_exists_isDerivedValueAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Morphisms.lean, line 1236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Morphisms.lean#L1236).

> **Stacks 05T1**. Let `F : 𝒟 ⥤ 𝒟'` be a functor and let `W` be a class of morphisms of `𝒟`.
>
> 1. If `W` has a left calculus of fractions and if for every object `X` of `𝒟` there is a
>    morphism `s : X ⟶ X'` in `W` such that the right derived functor `RF` is defined at `X'`,
>    then `RF` is everywhere defined, i.e. `F` is right derivable.
> 2. If `W` has a right calculus of fractions and if for every object `X` of `𝒟` there is a
>    morphism `s : X' ⟶ X` in `W` such that the left derived functor `LF` is defined at `X'`,
>    then `LF` is everywhere defined, i.e. `F` is left derivable.
>
> Definedness and values are those of Stacks 05S9, and everywhere-definedness that of Stacks 05SV.
> The source assumes the stronger hypothesis that `X'` *computes* `RF`, resp. `LF` (Stacks 05SX),
> and works in Situation 05S8; the canonical map `F(X') ⟶ RF(X')` plays no role and neither does
> the triangulated structure, only the relevant calculus of fractions on `W`.

```lean
public theorem isRightDerivable_and_isLeftDerivable_of_forall_exists_isDerivedValueAt
    (F : D ⥤ D') (W : MorphismProperty D) :
    (W.HasLeftCalculusOfFractions →
        (∀ X : D, ∃ (X' : D) (s : X ⟶ X'), W s ∧ ∃ c, F.IsRightDerivedValueAt W X' c) →
        F.IsRightDerivable W) ∧
      (W.HasRightCalculusOfFractions →
        (∀ X : D, ∃ (X' : D) (s : X' ⟶ X), W s ∧ ∃ c, F.IsLeftDerivedValueAt W X' c) →
        F.IsLeftDerivable W)
```

## Tag 06XN, a lemma

[Tag 06XN](https://stacks.math.columbia.edu/tag/06XN) in the Stacks Project.

**`Stacks.DerivedFunctor.Computing.rightDerived_everywhereDefined_and_computes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Computing.lean, line 778](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Computing.lean#L778). The attribute's comment: “(1)”.

> Let `S` be a saturated multiplicative system on `D` admitting a left calculus of fractions,
> and `F : D ⥤ D'` a functor. Suppose there is a subset `I ⊆ Ob(D)` such that:
> 1. for all `X` there is an arrow `s : X → X'` in `S` with `X' ∈ I`; and
> 2. for every arrow `s : X → X'` in `S` with `X, X' ∈ I`, `F.map s` is an isomorphism.
>
> Then `RF` is everywhere defined, and every `X ∈ I` computes `RF`.

```lean
theorem rightDerived_everywhereDefined_and_computes
    (F : D ⥤ D') (S : MorphismProperty D)
    [S.HasLeftCalculusOfFractions]
    (hSat : S.IsSaturatedMultiplicative)
    (I : Set D)
    (h1 : ∀ X : D, ∃ (X' : D) (s : X ⟶ X'), S s ∧ X' ∈ I)
    (h2 : ∀ ⦃X X' : D⦄ (s : X ⟶ X'), S s → X ∈ I → X' ∈ I → IsIso (F.map s)) :
    F.IsRightDerivable S ∧ ∀ X ∈ I, F.ComputesRightDerived S X
```

**`Stacks.DerivedFunctor.Computing.leftDerived_everywhereDefined_and_computes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Computing.lean, line 808](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Computing.lean#L808). The attribute's comment: “(2)”.

> Let `S` be a saturated multiplicative system on `D` admitting a right calculus of fractions,
> and `F : D ⥤ D'` a functor. Suppose there is a subset `P ⊆ Ob(D)` such that:
> 1. for all `X` there is an arrow `s : X' → X` in `S` with `X' ∈ P`; and
> 2. for every arrow `s : X → X'` in `S` with `X, X' ∈ P`, `F.map s` is an isomorphism.
>
> Then `LF` is everywhere defined, and every `X ∈ P` computes `LF`.

```lean
theorem leftDerived_everywhereDefined_and_computes
    (F : D ⥤ D') (S : MorphismProperty D)
    [S.HasRightCalculusOfFractions]
    (hSat : S.IsSaturatedMultiplicative)
    (P : Set D)
    (h1 : ∀ X : D, ∃ (X' : D) (s : X' ⟶ X), S s ∧ X' ∈ P)
    (h2 : ∀ ⦃X X' : D⦄ (s : X ⟶ X'), S s → X ∈ P → X' ∈ P → IsIso (F.map s)) :
    F.IsLeftDerivable S ∧ ∀ X ∈ P, F.ComputesLeftDerived S X
```

## Tag 05T2, a lemma

[Tag 05T2](https://stacks.math.columbia.edu/tag/05T2) in the Stacks Project.

**`DerivedFunctorComposition.exists_rightDerived_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Composition.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Composition.lean#L187). The attribute's comment: “(1)”.

> **Stacks Lemma 13.14.16, Statement 1 (Tag 05T2).**
> Assume the data of Definition 4 and that the right derived functors `RF'`, `RG`
> and `R(G∘F)` are everywhere defined.  Then there exists a natural transformation
> `t : R(G∘F) ⟶ RG ∘ RF'` of functors `S⁻¹A ⥤ C` which is characterized at each
> object `Q_A X` by the concrete composite of Tag 05T2: precomposing the component
> `t_{Q_A X}` with the structure map `αGF.app X : (G∘F)(X) ⟶ R(G∘F)(Q_A X)` yields
> the canonical map `G(F X) ⟶ RG(Q_B(F X))` followed by `RG` applied to the
> structure map `αFp.app X` of `RF'`.

```lean
theorem exists_rightDerived_comparison
    [RFp.IsRightDerivedFunctor αFp S] [RG.IsRightDerivedFunctor αG S']
    [RGF.IsRightDerivedFunctor αGF S] :
    ∃ t : RGF ⟶ RFp ⋙ RG,
      ∀ X : A, αGF.app X ≫ t.app (QA.obj X) = αG.app (F.obj X) ≫ RG.map (αFp.app X)
```

**`DerivedFunctorComposition.exists_leftDerived_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Functor/Derived/Composition.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Functor/Derived/Composition.lean#L249). The attribute's comment: “(2)”.

> **Stacks Lemma 13.14.16, Statement 2 (Tag 05T2).**
> Dually to Statement 1: assume the data of Definition 4 and that the left derived
> functors `LF'`, `LG` and `L(G∘F)` are everywhere defined.  Then there exists a
> natural transformation `t : LG ∘ LF' ⟶ L(G∘F)` of functors `S⁻¹A ⥤ C`,
> characterized at each object `Q_A X` by the concrete dual composite of Tag 05T2:
> postcomposing the component `t_{Q_A X}` with the structure map
> `βGF.app X : L(G∘F)(Q_A X) ⟶ (G∘F)(X)` yields `LG` applied to the structure map
> `βFp.app X` of `LF'` followed by the canonical map `LG(Q_B(F X)) ⟶ G(F X)`.

```lean
theorem exists_leftDerived_comparison
    [LFp.IsLeftDerivedFunctor βFp S] [LG.IsLeftDerivedFunctor βG S']
    [LGF.IsLeftDerivedFunctor βGF S] :
    ∃ t : LFp ⋙ LG ⟶ LGF,
      ∀ X : A, t.app (QA.obj X) ≫ βGF.app X = LG.map (βFp.app X) ≫ βG.app (F.obj X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.14, Tag 05S7](https://stacks.math.columbia.edu/tag/05S7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
