---
declaration: section
origin: cited
lean: CategoryTheory.CosimplicialObject.Homotopy, CategoryTheory.CosimplicialObject.exists_hom_power_iff, CategoryTheory.CosimplicialObject.exists_homotopy_iff, CategoryTheory.CosimplicialObject.exists_homotopy_iff_nonempty_homotopy_op, CategoryTheory.homotopic_whiskerRight, CategoryTheory.Arrow.homotopyEquiv_cechConerve_const_of_retraction, AlgebraicTopology.homotopic_normalizedCochainComplex_map, AlgebraicTopology.homotopic_alternatingCofaceMapComplex_map
statement: formalized
proof: formalized
---

# 14.28 Homotopies and cosimplicial objects

Section 14.28 of the Stacks Project, [Tag 019U](https://stacks.math.columbia.edu/tag/019U). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 019W, a definition

[Tag 019W](https://stacks.math.columbia.edu/tag/019W) in the Stacks Project.

**`CategoryTheory.CosimplicialObject.Homotopy`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Homotopy/Cosimplicial.lean, line 942](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Homotopy/Cosimplicial.lean#L942). The attribute's comment: “the finite products of the source are replaced by the products that name `Hom(Δ[1], V)`; the two conditions `a = e₀ ∘ h`, `b = e₁ ∘ h` are recorded degreewise, `e₀` and `e₁` being pinned there to the two projections; part (2), homotopic, is `Relation.EqvGen fun a b => Nonempty (Homotopy a b)`”. References: SGA 4 Vbis (3.0.2.2), “Dual form, special case”.

> **Stacks 019W**.
> A *homotopy from `a` to `b`*, for `a b : U ⟶ V` two morphisms of cosimplicial objects of `C`: a
> morphism `h : U ⟶ Hom(Δ[1], V)` into the cosimplicial object `Hom(Δ[1], V) = V.power Δ[1]` of
> [Stacks, Tag 019V] such that `a = e₀ ∘ h` and `b = e₁ ∘ h`, where `e₀, e₁ : Hom(Δ[1], V) ⟶ V` are
> induced by the two vertices of `Δ[1]`. The two conditions are recorded in each degree `n`, where
> `e₀` and `e₁` are the projections of `Hom(Δ[1], V)_n = ∏_{α ∈ Δ[1]_n} V_n` onto the factors indexed
> by the constant maps `[n] → [1]` with value `0`, resp. `1`; so the components
> `h_{n, α} : U_n ⟶ V_n` of `h` satisfy `a_n = h_{n, 0}` and `b_n = h_{n, 1}`, and the naturality of
> `h` is the compatibility of the `h_{n, α}` with the structure maps.

```lean
public structure Homotopy (a b : U ⟶ V) : Type v
```

## Tag 07KB, an equation

[Tag 07KB](https://stacks.math.columbia.edu/tag/07KB) in the Stacks Project.

**`CategoryTheory.CosimplicialObject.exists_hom_power_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Homotopy/Cosimplicial.lean, line 1050](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Homotopy/Cosimplicial.lean#L1050). The attribute's comment: “stated for an arbitrary simplicial set `K` in place of `Δ[1]`, and as the criterion characterising the families of morphisms that assemble into a morphism `U ⟶ Hom(K, V)`, which is what the source's paragraph asserts in both directions”.

> **Stacks 07KB**.
> A family of morphisms `h_{n, α} : U_n ⟶ V_n` of `C`, indexed by the simplices `α ∈ K_n` of a
> simplicial set `K`, is the family of components of a morphism `H : U ⟶ Hom(K, V)` of cosimplicial
> objects, with `H_n = ∏_{α ∈ K_n} h_{n, α}`, if and only if `h_{m, α} ∘ U(f) = V(f) ∘ h_{n, α ∘ f}`
> for every morphism `f : [n] → [m]` of `Δ` and every `α ∈ K_m`, where `α ∘ f = K(f)(α)`.

```lean
public theorem exists_hom_power_iff
    (h : ∀ n : SimplexCategory, K.obj (op n) → (U.obj n ⟶ V.obj n)) :
    (∃ H : U ⟶ V.power K, ∀ n, H.app n = Pi.lift (h n)) ↔
      ∀ ⦃n m : SimplexCategory⦄ (f : n ⟶ m) (α : K.obj (op m)),
        U.map f ≫ h m α = h n (K.map f.op α) ≫ V.map f
```

## Tag 0FKJ, a remark

[Tag 0FKJ](https://stacks.math.columbia.edu/tag/0FKJ) in the Stacks Project.

**`CategoryTheory.CosimplicialObject.exists_homotopy_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Homotopy/Cosimplicial.lean, line 1143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Homotopy/Cosimplicial.lean#L1143). The attribute's comment: “the remark's comparison of its notion with the one of 019W, `this new notion is the same as the old one in case finite products exist`, stated for a given family and with the correspondence pinned degreewise to `h_n = ∏_α h_{n, α}`; the finite products of 019W are weakened to the products naming `Hom(Δ[1], V)`, and the right hand side, which needs no products, is the remark's definition, in the form its dependents use. Part (2), homotopic, is `Relation.EqvGen` of the existence of such a family, as in 019W and 019S; the remark's functoriality assertions are 019Y (2)”.

> **Stacks 0FKJ**.
> A *homotopy from `a` to `b`*, for `a b : U ⟶ V` morphisms of cosimplicial objects of a category `C`
> with no assumptions whatsoever, is a family of morphisms `h_{n, α} : U_n ⟶ V_n` indexed by the
> objects `⦋n⦌` of `Δ` and the simplices `α ∈ Δ[1]_n`, satisfying
> `h_{m, α} ∘ U(f) = V(f) ∘ h_{n, α ∘ f}` for every morphism `f : ⦋n⦌ ⟶ ⦋m⦌` of `Δ`
> ([Stacks, Tag 07KB]) and having `a_n` and `b_n` as its components at the two constant maps
> `⦋n⦌ ⟶ ⦋1⦌`, with value `0` resp. `1`. This notion agrees with the one of [Stacks, Tag 019W], which
> needs the products `∏_{α ∈ Δ[1]_n} V_n` naming `Hom(Δ[1], V)`: whenever those exist, a family is a
> homotopy in the above sense if and only if it is the family of components of a homotopy
> `h : U ⟶ Hom(Δ[1], V)` from `a` to `b`, with `h_n = ∏_{α ∈ Δ[1]_n} h_{n, α}`.

```lean
public theorem exists_homotopy_iff (a b : U ⟶ V)
    (h : ∀ n : SimplexCategory, (Δ[1] : SSet.{0}).obj (op n) → (U.obj n ⟶ V.obj n)) :
    (∃ H : Homotopy a b, ∀ n, H.h.app n = Pi.lift (h n)) ↔
      (∀ ⦃n m : SimplexCategory⦄ (f : n ⟶ m) (α : (Δ[1] : SSet.{0}).obj (op m)),
          U.map f ≫ h m α = h n ((Δ[1] : SSet.{0}).map f.op α) ≫ V.map f) ∧
        (∀ n : SimplexCategory, h n (stdSimplex.const 1 0 (op n)) = a.app n) ∧
        (∀ n : SimplexCategory, h n (stdSimplex.const 1 1 (op n)) = b.app n)
```

## Tag 019X, a lemma

[Tag 019X](https://stacks.math.columbia.edu/tag/019X) in the Stacks Project.

**`CategoryTheory.CosimplicialObject.exists_homotopy_iff_nonempty_homotopy_op`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Homotopy/Cosimplicial.lean, line 414](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Homotopy/Cosimplicial.lean#L414). The attribute's comment: “the equivalence of (1) and (2); the primed objects are spelled `U.op` and `NatTrans.op a` rather than through `cosimplicialSimplicialEquiv`, a homotopy as in 0FKJ by its family of components as in 07KB, and a homotopy as in 019M by Mathlib's `SimplicialObject.Homotopy`, so that neither side needs (co)products and the statement holds over an arbitrary category. The final assertion, homotopic if and only if homotopic, is the equivalence of the `Relation.EqvGen` of the two sides and is formal from this one, by transport along the bijection `NatTrans.op : (U ⟶ V) ≃ (V.op ⟶ U.op)`; it is what 019Y (2) and (4) apply”.

> **Stacks 019X**.
> A homotopy of morphisms of cosimplicial objects is a simplicial homotopy in the opposite category.
> Let `C` be a category with no assumptions whatsoever, let `U`, `V` be cosimplicial objects of `C`
> and let `a, b : U ⟶ V`, so that `U`, `V` correspond to simplicial objects `U.op`, `V.op` of `Cᵒᵖ`
> and `a`, `b` to morphisms `aᵒᵖ, bᵒᵖ : V.op ⟶ U.op`. Then there exists a homotopy `{h_{n, α}}` from
> `a` to `b` in the sense of [Stacks, Tag 0FKJ] — a family of morphisms `h_{n, α} : U_n ⟶ V_n`,
> indexed by the simplices `α ∈ Δ[1]_n`, satisfying `h_{m, α} ∘ U(f) = V(f) ∘ h_{n, α ∘ f}` for every
> morphism `f : ⦋n⦌ ⟶ ⦋m⦌` of `Δ` and having `a_n`, `b_n` as its components at the two constant maps
> `⦋n⦌ ⟶ ⦋1⦌` — if and only if there exists a homotopy `{h_{n, i}}` from `aᵒᵖ` to `bᵒᵖ` in the sense
> of [Stacks, Tag 019M]. Hence `a` and `b` are homotopic if and only if `aᵒᵖ` and `bᵒᵖ` are, the two
> relations being the equivalence relations generated by these two existence statements.

```lean
public theorem exists_homotopy_iff_nonempty_homotopy_op {U V : CosimplicialObject C}
    (a b : U ⟶ V) :
    (∃ h : ∀ n : SimplexCategory, (Δ[1] : SSet.{0}).obj (op n) → (U.obj n ⟶ V.obj n),
        (∀ ⦃n m : SimplexCategory⦄ (f : n ⟶ m) (α : (Δ[1] : SSet.{0}).obj (op m)),
            U.map f ≫ h m α = h n ((Δ[1] : SSet.{0}).map f.op α) ≫ V.map f) ∧
          (∀ n : SimplexCategory, h n (stdSimplex.const 1 0 (op n)) = a.app n) ∧
          (∀ n : SimplexCategory, h n (stdSimplex.const 1 1 (op n)) = b.app n)) ↔
      Nonempty (SimplicialObject.Homotopy (NatTrans.op a) (NatTrans.op b))
```

## Tag 019Y, a lemma

[Tag 019Y](https://stacks.math.columbia.edu/tag/019Y) in the Stacks Project.

**`CategoryTheory.homotopic_whiskerRight`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Homotopy/Cosimplicial.lean, line 462](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Homotopy/Cosimplicial.lean#L462). The attribute's comment: “all four parts, at the chain level: `homotopic` is `Relation.EqvGen` of the existence of a homotopy, as in 019K, 019W and 0FKJ. Homotopy of simplicial objects over an arbitrary category is `SimplicialObject.Homotopy` (Mathlib), the notion of 019M through the composites of the source's footnote; homotopy of cosimplicial objects is the family of 0FKJ, repeated verbatim. The source's four categories occur as they do there, each part binding the two it names, so that each part applies on its own; the four are one conjunction because they are one assertion read in four dualities. The passage between variances is `Functor.rightOp`/`Functor.op` and `NatTrans.rightOp`/`NatTrans.op`, the anti-equivalences `simplicialCosimplicialEquiv` and `cosimplicialSimplicialEquiv`”.

> **Stacks 019Y**.
> Functors preserve homotopic morphisms of (co)simplicial objects. Let `C`, `C'`, `D`, `D'` be
> categories, with no assumptions whatsoever. (1) If `a, b : U ⟶ V` are homotopic morphisms of
> simplicial objects of `D` in the sense of [Stacks, Tag 019M] and `F : D ⥤ D'` is a functor, then
> `F(a)`, `F(b)` are homotopic morphisms `F(U) ⟶ F(V)` of simplicial objects of `D'`. (2) If
> `a, b : U ⟶ V` are homotopic morphisms of cosimplicial objects of `C` in the sense of
> [Stacks, Tag 0FKJ] — a family `h_{n, α} : Uₙ ⟶ Vₙ`, indexed by the simplices `α ∈ Δ[1]_n`,
> satisfying `h_{m, α} ∘ U(f) = V(f) ∘ h_{n, α ∘ f}` and having `aₙ`, `bₙ` as its components at the
> two constant maps `⦋n⦌ ⟶ ⦋1⦌`, and chains of such — and `F : C ⥤ C'` is a functor, then `F(a)`,
> `F(b)` are homotopic morphisms `F(U) ⟶ F(V)` of cosimplicial objects of `C'`. (3) For a
> contravariant functor, i.e. a functor `F : Dᵒᵖ ⥤ C`, homotopic morphisms `a, b : U ⟶ V` of
> simplicial objects of `D` have homotopic images `F(a)`, `F(b) : F(V) ⟶ F(U)`, morphisms of
> cosimplicial objects of `C`. (4) Likewise a functor `F : Cᵒᵖ ⥤ D` takes homotopic morphisms
> `a, b : U ⟶ V` of cosimplicial objects of `C` to homotopic morphisms `F(a)`, `F(b) : F(V) ⟶ F(U)`
> of simplicial objects of `D`. No (co)limit in any of the four categories is assumed to exist, and
> the functor is not asked to preserve anything.

```lean
public theorem homotopic_whiskerRight :
    (∀ {D : Type u₁} [Category.{v₁} D] {D' : Type u₂} [Category.{v₂} D']
        {U V : SimplicialObject D} {a b : U ⟶ V} (F : D ⥤ D'),
        Relation.EqvGen (fun x y : U ⟶ V => Nonempty (SimplicialObject.Homotopy x y)) a b →
          Relation.EqvGen
            (fun x y : U ⋙ F ⟶ V ⋙ F => Nonempty (SimplicialObject.Homotopy x y))
            (Functor.whiskerRight a F) (Functor.whiskerRight b F)) ∧
      (∀ {C : Type u₁} [Category.{v₁} C] {C' : Type u₂} [Category.{v₂} C']
          {U V : CosimplicialObject C} {a b : U ⟶ V} (F : C ⥤ C'),
          Relation.EqvGen (fun x y : U ⟶ V => ∃ h : ∀ n : SimplexCategory,
              (Δ[1] : SSet.{0}).obj (op n) → (U.obj n ⟶ V.obj n),
              (∀ ⦃n m : SimplexCategory⦄ (f : n ⟶ m) (α : (Δ[1] : SSet.{0}).obj (op m)),
                  U.map f ≫ h m α = h n ((Δ[1] : SSet.{0}).map f.op α) ≫ V.map f) ∧
                (∀ n : SimplexCategory, h n (stdSimplex.const 1 0 (op n)) = x.app n) ∧
                (∀ n : SimplexCategory, h n (stdSimplex.const 1 1 (op n)) = y.app n)) a b →
            Relation.EqvGen (fun x y : U ⋙ F ⟶ V ⋙ F => ∃ h : ∀ n : SimplexCategory,
                (Δ[1] : SSet.{0}).obj (op n) → ((U ⋙ F).obj n ⟶ (V ⋙ F).obj n),
                (∀ ⦃n m : SimplexCategory⦄ (f : n ⟶ m) (α : (Δ[1] : SSet.{0}).obj (op m)),
                    (U ⋙ F).map f ≫ h m α =
                      h n ((Δ[1] : SSet.{0}).map f.op α) ≫ (V ⋙ F).map f) ∧
                  (∀ n : SimplexCategory, h n (stdSimplex.const 1 0 (op n)) = x.app n) ∧
                  (∀ n : SimplexCategory, h n (stdSimplex.const 1 1 (op n)) = y.app n))
              (Functor.whiskerRight a F) (Functor.whiskerRight b F)) ∧
        (∀ {D : Type u₁} [Category.{v₁} D] {C : Type u₂} [Category.{v₂} C]
            {U V : SimplicialObject D} {a b : U ⟶ V} (F : Dᵒᵖ ⥤ C),
            Relation.EqvGen (fun x y : U ⟶ V => Nonempty (SimplicialObject.Homotopy x y)) a b →
              Relation.EqvGen (fun x y : V.rightOp ⋙ F ⟶ U.rightOp ⋙ F =>
                  ∃ h : ∀ n : SimplexCategory, (Δ[1] : SSet.{0}).obj (op n) →
                    ((V.rightOp ⋙ F).obj n ⟶ (U.rightOp ⋙ F).obj n),
                  (∀ ⦃n m : SimplexCategory⦄ (f : n ⟶ m) (α : (Δ[1] : SSet.{0}).obj (op m)),
                      (V.rightOp ⋙ F).map f ≫ h m α =
                        h n ((Δ[1] : SSet.{0}).map f.op α) ≫ (U.rightOp ⋙ F).map f) ∧
                    (∀ n : SimplexCategory, h n (stdSimplex.const 1 0 (op n)) = x.app n) ∧
                    (∀ n : SimplexCategory, h n (stdSimplex.const 1 1 (op n)) = y.app n))
                (Functor.whiskerRight (NatTrans.rightOp a) F)
                (Functor.whiskerRight (NatTrans.rightOp b) F)) ∧
          (∀ {C : Type u₁} [Category.{v₁} C] {D : Type u₂} [Category.{v₂} D]
              {U V : CosimplicialObject C} {a b : U ⟶ V} (F : Cᵒᵖ ⥤ D),
              Relation.EqvGen (fun x y : U ⟶ V => ∃ h : ∀ n : SimplexCategory,
                  (Δ[1] : SSet.{0}).obj (op n) → (U.obj n ⟶ V.obj n),
                  (∀ ⦃n m : SimplexCategory⦄ (f : n ⟶ m) (α : (Δ[1] : SSet.{0}).obj (op m)),
                      U.map f ≫ h m α = h n ((Δ[1] : SSet.{0}).map f.op α) ≫ V.map f) ∧
                    (∀ n : SimplexCategory, h n (stdSimplex.const 1 0 (op n)) = x.app n) ∧
                    (∀ n : SimplexCategory, h n (stdSimplex.const 1 1 (op n)) = y.app n)) a b →
                Relation.EqvGen (fun x y : V.op ⋙ F ⟶ U.op ⋙ F =>
                    Nonempty (SimplicialObject.Homotopy x y))
                  (Functor.whiskerRight (NatTrans.op a) F)
                  (Functor.whiskerRight (NatTrans.op b) F))
```

## Tag 019Z, a lemma

[Tag 019Z](https://stacks.math.columbia.edu/tag/019Z) in the Stacks Project.

**`CategoryTheory.Arrow.homotopyEquiv_cechConerve_const_of_retraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Homotopy/CechConerveRetraction.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Homotopy/CechConerveRetraction.lean#L71). The attribute's comment: “the existence of the iterated pushouts `Y ⨿_X ⋯ ⨿_X Y`, which is all Example 016N uses, replaces the source's pushouts in `C`. The self map is characterised by its composites with the factor inclusions `cechι n i`, it exists, and every such map admits a homotopy to the identity, which is stronger than being homotopic. A homotopy is its family of components as in 0FKJ and 07KB, which needs no products in `C`; homotopic is `Relation.EqvGen` of the existence of a homotopy, the spelling of 019Y and 0FKK; homotopy equivalent is the dual of 019N, spelled out”.

> **Stacks 019Z**.
> Let `f : X ⟶ Y` be a morphism of a category `C` whose iterated pushouts `Y ⨿_X ⋯ ⨿_X Y` exist and
> let `s : Y ⟶ X` satisfy `s ∘ f = id_X`. Let `U = f.cechConerve` be the cosimplicial object of
> [Stacks, Tag 016N] built from `f`, with `cechι n i : Y ⟶ Uₙ` the inclusion of the `i`-th factor.
> Then:
> 1. there is a morphism `φ : U ⟶ U` which in each degree is `f ∘ s` on each factor, i.e.
>   `φₙ ∘ cechι n i = cechι n i ∘ f ∘ s`, and every such `φ` admits a homotopy to `𝟙 U` in the sense
>   of [Stacks, Tag 0FKJ]: a family `h_{n, α} : Uₙ ⟶ Uₙ`, `α ∈ Δ[1]ₙ`, with
>   `h_{m, α} ∘ U(g) = U(g) ∘ h_{n, α ∘ g}` for every `g : ⦋n⦌ ⟶ ⦋m⦌`, whose components at the
>   constant maps with values `0` and `1` are `φₙ` and `id`; in particular `φ` and `𝟙 U` are
>   homotopic;
> 2. `U` is homotopy equivalent to the constant cosimplicial object `X` (the notion dual to
>   [Stacks, Tag 019N]): there are `a : U ⟶ X` and `b : X ⟶ U` such that `b ∘ a` is homotopic to
>   `𝟙 U` and `a ∘ b` is homotopic to `𝟙 X`, homotopic being the equivalence relation generated by
>   the existence of a homotopy.

```lean
public theorem homotopyEquiv_cechConerve_const_of_retraction (s : f.right ⟶ f.left)
    (hs : f.hom ≫ s = 𝟙 f.left) :
    ((∃ φ : f.cechConerve ⟶ f.cechConerve,
        ∀ (n : SimplexCategory) (i : Fin (n.len + 1)),
          cechι n i ≫ φ.app n = (s ≫ f.hom) ≫ cechι n i) ∧
      ∀ φ : f.cechConerve ⟶ f.cechConerve,
        (∀ (n : SimplexCategory) (i : Fin (n.len + 1)),
          cechι n i ≫ φ.app n = (s ≫ f.hom) ≫ cechι n i) →
        ∃ h : ∀ n : SimplexCategory, (Δ[1] : SSet.{0}).obj (op n) →
            (f.cechConerve.obj n ⟶ f.cechConerve.obj n),
          (∀ ⦃n m : SimplexCategory⦄ (g : n ⟶ m) (α : (Δ[1] : SSet.{0}).obj (op m)),
              f.cechConerve.map g ≫ h m α =
                h n ((Δ[1] : SSet.{0}).map g.op α) ≫ f.cechConerve.map g) ∧
            (∀ n : SimplexCategory, h n (stdSimplex.const 1 0 (op n)) = φ.app n) ∧
            (∀ n : SimplexCategory, h n (stdSimplex.const 1 1 (op n)) =
              𝟙 (f.cechConerve.obj n))) ∧
      ∃ (a : f.cechConerve ⟶ (CosimplicialObject.const C).obj f.left)
        (b : (CosimplicialObject.const C).obj f.left ⟶ f.cechConerve),
        Relation.EqvGen (fun x y : f.cechConerve ⟶ f.cechConerve =>
            ∃ h : ∀ n : SimplexCategory, (Δ[1] : SSet.{0}).obj (op n) →
              (f.cechConerve.obj n ⟶ f.cechConerve.obj n),
            (∀ ⦃n m : SimplexCategory⦄ (g : n ⟶ m) (α : (Δ[1] : SSet.{0}).obj (op m)),
                f.cechConerve.map g ≫ h m α =
                  h n ((Δ[1] : SSet.{0}).map g.op α) ≫ f.cechConerve.map g) ∧
              (∀ n : SimplexCategory, h n (stdSimplex.const 1 0 (op n)) = x.app n) ∧
              (∀ n : SimplexCategory, h n (stdSimplex.const 1 1 (op n)) = y.app n))
          (a ≫ b) (𝟙 f.cechConerve) ∧
        Relation.EqvGen (fun x y : (CosimplicialObject.const C).obj f.left ⟶
              (CosimplicialObject.const C).obj f.left =>
            ∃ h : ∀ n : SimplexCategory, (Δ[1] : SSet.{0}).obj (op n) →
              (((CosimplicialObject.const C).obj f.left).obj n ⟶
                ((CosimplicialObject.const C).obj f.left).obj n),
            (∀ ⦃n m : SimplexCategory⦄ (g : n ⟶ m) (α : (Δ[1] : SSet.{0}).obj (op m)),
                ((CosimplicialObject.const C).obj f.left).map g ≫ h m α =
                  h n ((Δ[1] : SSet.{0}).map g.op α) ≫
                    ((CosimplicialObject.const C).obj f.left).map g) ∧
              (∀ n : SimplexCategory, h n (stdSimplex.const 1 0 (op n)) = x.app n) ∧
              (∀ n : SimplexCategory, h n (stdSimplex.const 1 1 (op n)) = y.app n))
          (b ≫ a) (𝟙 _)
```

## Tag 01A0, a lemma

[Tag 01A0](https://stacks.math.columbia.edu/tag/01A0) in the Stacks Project.

**`AlgebraicTopology.homotopic_normalizedCochainComplex_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/DoldKan/CosimplicialHomotopy.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/DoldKan/CosimplicialHomotopy.lean#L98). The attribute's comment: “the second assertion, for the normalized cochain complex `Q`; the first, for the Moore cochain complex `s`, is `homotopic_alternatingCofaceMapComplex_map`. `Q` is any functor with a natural transformation `π : s ⟶ Q` which is an isomorphism in degree `0` and a cokernel of the cofaces `δⁿ⁺¹ᵢ`, `i ≤ n`, in degree `n + 1`, the characterization of `Q` and of `s(U) → Q(U)` given in 019I, which determines `Q` up to unique isomorphism under `s`. A homotopy is given by its family of components as in 0FKJ and 07KB, and being homotopic is spelled `Relation.EqvGen` of the existence of such a family, as in 019S”.

> **Stacks 01A0**, the assertion for the normalized cochain complex.
> Let `A` be an abelian category, and let `Q` be the normalized cochain complex functor of
> [Stacks, Tag 019I], given with its projection `π : s ⟶ Q` from the Moore cochain complex: `π` is
> an isomorphism in degree `0` and, in each degree `n + 1`, a cokernel of the cofaces
> `δⁿ⁺¹ᵢ : Uₙ ⟶ Uₙ₊₁`, `i ≤ n`. Let `a, b : U ⟶ V` be homotopic morphisms of cosimplicial objects
> of `A`: related by a chain of morphisms consecutive members of which admit a homotopy in one
> direction or the other, a homotopy from `a` to `b` being a family of morphisms
> `h_{n, α} : Uₙ ⟶ Vₙ` indexed by the simplices `α ∈ Δ[1]ₙ` with
> `h_{m, α} ∘ U(g) = V(g) ∘ h_{n, α ∘ g}` for every morphism `g : ⦋n⦌ ⟶ ⦋m⦌` of `Δ`, whose
> components at the constant maps `⦋n⦌ ⟶ ⦋1⦌` with values `0` and `1` are `a_n` and `b_n`
> ([Stacks, Tag 0FKJ]). Then `Q(a), Q(b) : Q(U) ⟶ Q(V)` are homotopic maps of cochain
> complexes.

```lean
public theorem homotopic_normalizedCochainComplex_map
    (Q : CosimplicialObject A ⥤ CochainComplex A ℕ) (π : alternatingCofaceMapComplex A ⟶ Q)
    (hπ₀ : ∀ U : CosimplicialObject A, IsIso ((π.app U).f 0))
    (hπ : ∀ (U : CosimplicialObject A) (n : ℕ),
      ∃ e : cokernel (Sigma.desc (f := fun _ : Fin (n + 1) => U.obj ⦋n⦌)
          fun i => U.δ i.castSucc) ≅ (Q.obj U).X (n + 1),
        cokernel.π _ ≫ e.hom = (π.app U).f (n + 1))
    {U V : CosimplicialObject A} {a b : U ⟶ V}
    (h : Relation.EqvGen
      (fun a b : U ⟶ V => ∃ h : ∀ n : SimplexCategory, (Δ[1] : SSet.{0}).obj (op n) →
          (U.obj n ⟶ V.obj n),
        (∀ ⦃n m : SimplexCategory⦄ (g : n ⟶ m) (α : (Δ[1] : SSet.{0}).obj (op m)),
            U.map g ≫ h m α = h n ((Δ[1] : SSet.{0}).map g.op α) ≫ V.map g) ∧
          (∀ n : SimplexCategory, h n (SSet.stdSimplex.const 1 0 (op n)) = a.app n) ∧
          (∀ n : SimplexCategory, h n (SSet.stdSimplex.const 1 1 (op n)) = b.app n)) a b) :
    homotopic A (ComplexShape.up ℕ) (Q.map a) (Q.map b)
```

**`AlgebraicTopology.homotopic_alternatingCofaceMapComplex_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Homotopy/Cosimplicial.lean, line 792](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Homotopy/Cosimplicial.lean#L792). The attribute's comment: “the first assertion, for the Moore cochain complex `s`, with the source's additive `A` weakened to preadditive, which is all `s` uses; the second, for the normalized cochain complex `Q` of 019I, is `homotopic_normalizedCochainComplex_map`. A homotopy is given by its family of components as in 0FKJ and 07KB, which needs no products in `A`, and being homotopic is spelled `Relation.EqvGen` of the existence of such a family, as in 019S”. References: SGA 4 XVII (5.5.3), “homotopy preservation”.

> **Stacks 01A0**.
> The Moore cochain complex functor carries homotopic morphisms to homotopic maps of cochain
> complexes. Let `a, b : U ⟶ V` be homotopic morphisms of cosimplicial objects of a preadditive
> category `A`: related by a chain of morphisms consecutive members of which admit a homotopy in one
> direction or the other, a homotopy from `a` to `b` being a family of morphisms `h_{n, α} : Uₙ ⟶ Vₙ`
> indexed by the simplices `α ∈ Δ[1]ₙ` with `h_{m, α} ∘ U(g) = V(g) ∘ h_{n, α ∘ g}` for every
> morphism `g : ⦋n⦌ ⟶ ⦋m⦌` of `Δ`, whose components at the constant maps `⦋n⦌ ⟶ ⦋1⦌` with values `0`
> and `1` are `a_n` and `b_n` ([Stacks, Tag 0FKJ]). Then the induced maps `s(a), s(b) : s(U) ⟶ s(V)`
> of Moore cochain complexes are chain homotopic.

```lean
public theorem homotopic_alternatingCofaceMapComplex_map
    (h : Relation.EqvGen
      (fun a b : U ⟶ V => ∃ h : ∀ n : SimplexCategory, (Δ[1] : SSet.{0}).obj (op n) →
          (U.obj n ⟶ V.obj n),
        (∀ ⦃n m : SimplexCategory⦄ (g : n ⟶ m) (α : (Δ[1] : SSet.{0}).obj (op m)),
            U.map g ≫ h m α = h n ((Δ[1] : SSet.{0}).map g.op α) ≫ V.map g) ∧
          (∀ n : SimplexCategory, h n (stdSimplex.const 1 0 (op n)) = a.app n) ∧
          (∀ n : SimplexCategory, h n (stdSimplex.const 1 1 (op n)) = b.app n)) a b) :
    homotopic A (ComplexShape.up ℕ) ((alternatingCofaceMapComplex A).map a)
      ((alternatingCofaceMapComplex A).map b)
```

## Tag 0FKK, a lemma

[Tag 0FKK](https://stacks.math.columbia.edu/tag/0FKK) in the Stacks Project.

**`AlgebraicTopology.homotopyEquivalences_moore_and_normalizedCochainComplex_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/DoldKan/CosimplicialHomotopyEquivalence.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/DoldKan/CosimplicialHomotopyEquivalence.lean#L118). The attribute's comment: “the source's additive `A` is generalized to preadditive in the assertion for `s`, which is all `s` uses. Being a homotopy equivalence of cochain complexes is `HomologicalComplex.homotopyEquivalences`, which pins the map. A homotopy equivalence of cosimplicial objects is spelled out (the source defines it by duality with 019N): a homotopy is its family of components as in 0FKJ and 07KB, which needs no products in `A`, and being homotopic is `Relation.EqvGen` of the existence of such a family, the spelling of 01A0. The normalized cochain complex `Q` is any functor with a projection `π : s ⟶ Q` that is an isomorphism in degree 0 and the cokernel of the cofaces `δ_i`, `i < n`, in degree `n`, the description of 019I, which provides one; the differential of `Q` is then the one induced by `(-1)^{n+1} δ_{n+1}`”.

> **Stacks 0FKK**.
> Homotopy equivalences of cosimplicial objects induce homotopy equivalences of cochain complexes.
> Let `a : U ⟶ V` be a homotopy equivalence of cosimplicial objects of `A`: there is `b : V ⟶ U`
> such that `a ≫ b` is homotopic to `𝟙 U` and `b ≫ a` is homotopic to `𝟙 V`, where two morphisms
> `f`, `g` of cosimplicial objects are *homotopic* when they are related by the equivalence relation
> generated by the existence of a homotopy from one to the other, a homotopy being a family of
> morphisms `h_{n, α}` indexed by the simplices `α ∈ Δ[1]ₙ` with
> `h_{m, α} ∘ U(u) = V(u) ∘ h_{n, α ∘ u}` for every morphism `u : ⦋n⦌ ⟶ ⦋m⦌` of `Δ`, whose
> components at the constant maps `⦋n⦌ ⟶ ⦋1⦌` with values `0` and `1` are `f_n` and `g_n`
> ([Stacks, Tag 0FKJ]).
> 1. If `A` is preadditive, then `s(a) : s(U) ⟶ s(V)` is a homotopy equivalence of Moore cochain
>   complexes.
> 2. If `A` is abelian, then `Q(a) : Q(U) ⟶ Q(V)` is a homotopy equivalence of normalized cochain
>   complexes, for any normalized cochain complex functor `Q` with projection `π : s ⟶ Q`, which is
>   an isomorphism in degree `0` and a cokernel of the cofaces `δ i : Uₙ ⟶ Uₙ₊₁`, `i ≤ n`, in degree
>   `n + 1` ([Stacks, Tag 019I]).

```lean
public theorem homotopyEquivalences_moore_and_normalizedCochainComplex_map :
    (∀ (A : Type u) [Category.{v} A] [Preadditive A] (U V : CosimplicialObject A) (a : U ⟶ V),
      (∃ b : V ⟶ U,
        Relation.EqvGen (fun f₁ f₂ : U ⟶ U => ∃ h : ∀ n : SimplexCategory,
            (Δ[1] : SSet.{0}).obj (op n) → (U.obj n ⟶ U.obj n),
          (∀ ⦃n m : SimplexCategory⦄ (u : n ⟶ m) (α : (Δ[1] : SSet.{0}).obj (op m)),
              U.map u ≫ h m α = h n ((Δ[1] : SSet.{0}).map u.op α) ≫ U.map u) ∧
            (∀ n : SimplexCategory, h n (stdSimplex.const 1 0 (op n)) = f₁.app n) ∧
            (∀ n : SimplexCategory, h n (stdSimplex.const 1 1 (op n)) = f₂.app n))
          (a ≫ b) (𝟙 U) ∧
        Relation.EqvGen (fun f₁ f₂ : V ⟶ V => ∃ h : ∀ n : SimplexCategory,
            (Δ[1] : SSet.{0}).obj (op n) → (V.obj n ⟶ V.obj n),
          (∀ ⦃n m : SimplexCategory⦄ (u : n ⟶ m) (α : (Δ[1] : SSet.{0}).obj (op m)),
              V.map u ≫ h m α = h n ((Δ[1] : SSet.{0}).map u.op α) ≫ V.map u) ∧
            (∀ n : SimplexCategory, h n (stdSimplex.const 1 0 (op n)) = f₁.app n) ∧
            (∀ n : SimplexCategory, h n (stdSimplex.const 1 1 (op n)) = f₂.app n))
          (b ≫ a) (𝟙 V)) →
      HomologicalComplex.homotopyEquivalences A (ComplexShape.up ℕ)
        ((alternatingCofaceMapComplex A).map a)) ∧
    (∀ (A : Type u) [Category.{v} A] [Abelian A]
      (Q : CosimplicialObject A ⥤ CochainComplex A ℕ) (π : alternatingCofaceMapComplex A ⟶ Q),
      (∀ U : CosimplicialObject A, IsIso ((π.app U).f 0)) →
      (∀ (U : CosimplicialObject A) (n : ℕ),
        ∃ e : cokernel (Sigma.desc (f := fun _ : Fin (n + 1) => U.obj ⦋n⦌)
            fun i => U.δ i.castSucc) ≅ (Q.obj U).X (n + 1),
          cokernel.π _ ≫ e.hom = (π.app U).f (n + 1)) →
      ∀ (U V : CosimplicialObject A) (a : U ⟶ V),
      (∃ b : V ⟶ U,
        Relation.EqvGen (fun f₁ f₂ : U ⟶ U => ∃ h : ∀ n : SimplexCategory,
            (Δ[1] : SSet.{0}).obj (op n) → (U.obj n ⟶ U.obj n),
          (∀ ⦃n m : SimplexCategory⦄ (u : n ⟶ m) (α : (Δ[1] : SSet.{0}).obj (op m)),
              U.map u ≫ h m α = h n ((Δ[1] : SSet.{0}).map u.op α) ≫ U.map u) ∧
            (∀ n : SimplexCategory, h n (stdSimplex.const 1 0 (op n)) = f₁.app n) ∧
            (∀ n : SimplexCategory, h n (stdSimplex.const 1 1 (op n)) = f₂.app n))
          (a ≫ b) (𝟙 U) ∧
        Relation.EqvGen (fun f₁ f₂ : V ⟶ V => ∃ h : ∀ n : SimplexCategory,
            (Δ[1] : SSet.{0}).obj (op n) → (V.obj n ⟶ V.obj n),
          (∀ ⦃n m : SimplexCategory⦄ (u : n ⟶ m) (α : (Δ[1] : SSet.{0}).obj (op m)),
              V.map u ≫ h m α = h n ((Δ[1] : SSet.{0}).map u.op α) ≫ V.map u) ∧
            (∀ n : SimplexCategory, h n (stdSimplex.const 1 0 (op n)) = f₁.app n) ∧
            (∀ n : SimplexCategory, h n (stdSimplex.const 1 1 (op n)) = f₂.app n))
          (b ≫ a) (𝟙 V)) →
      HomologicalComplex.homotopyEquivalences A (ComplexShape.up ℕ) (Q.map a))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.28, Tag 019U](https://stacks.math.columbia.edu/tag/019U)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
