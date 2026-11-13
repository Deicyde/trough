---
declaration: section
origin: cited
lean: CategoryTheory.NatTrans.Equifibered, Stacks.Simplicial.Descent.cartesianObjectsOverEquivalenceDescentData, AlgebraicGeometry.simplicialScheme, AlgebraicGeometry.SimplicialScheme.toDescentDatum, AlgebraicGeometry.SimplicialScheme.isPullback_cartesianLeft, AlgebraicGeometry.SimplicialScheme.isPullback_cartesianRight, AlgebraicGeometry.SimplicialScheme.cartesian_actMap, AlgebraicGeometry.SimplicialScheme.cartesianDescentDatum
statement: formalized
proof: formalized
---

# 85.27 Descent in terms of simplicial schemes

Section 85.27 of the Stacks Project, [Tag 0248](https://stacks.math.columbia.edu/tag/0248). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0249, a definition

[Tag 0249](https://stacks.math.columbia.edu/tag/0249) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.NatTrans.Equifibered`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.NatTrans.Equifibered#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch85.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch85.lean#L19) (StacksFrontier): “more general: an equifibered natural transformation of functors J ⥤ C; here J = SimplexCategoryᵒᵖ and C = Scheme, so a morphism of simplicial schemes”. References: EGA I (10.12.2), “more general”.

## Tag 07TC, a lemma

[Tag 07TC](https://stacks.math.columbia.edu/tag/07TC) in the Stacks Project.

**`Stacks.Simplicial.Descent.cartesianObjectsOverEquivalenceDescentData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/CartesianDescentData.lean, line 1179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/CartesianDescentData.lean#L1179).

> Cartesian simplicial objects over `X` are equivalent to descent data consisting of an
> object over `X₀` and a normalized transition isomorphism satisfying the cocycle condition.

```lean
noncomputable def cartesianObjectsOverEquivalenceDescentData (X : SimplicialObject C) :
    ObjectProperty.FullSubcategory (fun Y : Over X ↦ Y.hom.Equifibered) ≌
      DescentDatum X
```

## Tag 024A, a definition

[Tag 024A](https://stacks.math.columbia.edu/tag/024A) in the Stacks Project.

**`AlgebraicGeometry.simplicialScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/DescentViaSimplicialSchemes.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/DescentViaSimplicialSchemes.lean#L72).

> The simplicial scheme `(X/S)_•` associated to `f : X ⟶ S`: its degree-`n` part is the
> `(n + 1)`-fold fibre product of `X` over `S`, i.e. it is the Čech nerve of `f`.

```lean
def simplicialScheme : SimplicialObject Scheme.{u}
```

## Tag 024B, a lemma

[Tag 024B](https://stacks.math.columbia.edu/tag/024B) in the Stacks Project.

**`AlgebraicGeometry.SimplicialScheme.toDescentDatum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/DescentViaSimplicialSchemes.lean, line 555](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/DescentViaSimplicialSchemes.lean#L555). The attribute's comment: “the descent datum (V, φ) attached to a descent datum on (X/S)\_•”.

> **The descent datum `(V, φ)` relative to `f : X ⟶ S`** attached to a descent datum on
> `(X/S)_•`.

```lean
def toDescentDatum (D : Stacks.Simplicial.Descent.DescentDatum (simplicialScheme f)) :
    AlgebraicGeometry.DescentDatum f
```

**`AlgebraicGeometry.SimplicialScheme.isPullback_cartesianLeft`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/DescentViaSimplicialSchemes.lean, line 623](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/DescentViaSimplicialSchemes.lean#L623). The attribute's comment: “the isomorphism V ×\_S X ← Y\_1 given by (d¹\_1, pr\_1 ∘ π\_1)”.

> **`(d¹₁, pr₁ ∘ π₁) : Y₁ ⟶ V ×_S X` is an isomorphism.**

```lean
lemma isPullback_cartesianLeft (Y : Stacks.Simplicial.Descent.Cartesian (simplicialScheme f)) :
    IsPullback (Y.1.left.δ (1 : Fin 2)) (Y.1.hom.app (op ⦋1⦌) ≫ proj f 1 1)
      ((descentObj (cartesianDatum Y)).hom ≫ f) f
```

**`AlgebraicGeometry.SimplicialScheme.isPullback_cartesianRight`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/DescentViaSimplicialSchemes.lean, line 632](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/DescentViaSimplicialSchemes.lean#L632). The attribute's comment: “the isomorphism Y\_1 → X ×\_S V given by (pr\_0 ∘ π\_1, d¹\_0)”.

> **`(pr₀ ∘ π₁, d¹₀) : Y₁ ⟶ X ×_S V` is an isomorphism.**

```lean
lemma isPullback_cartesianRight (Y : Stacks.Simplicial.Descent.Cartesian (simplicialScheme f)) :
    IsPullback (Y.1.hom.app (op ⦋1⦌) ≫ proj f 1 0) (Y.1.left.δ (0 : Fin 2)) f
      ((descentObj (cartesianDatum Y)).hom ≫ f)
```

**`AlgebraicGeometry.SimplicialScheme.cartesian_actMap`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/DescentViaSimplicialSchemes.lean, line 642](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/DescentViaSimplicialSchemes.lean#L642). The attribute's comment: “φ is the isomorphism resulting from d¹\_0 and π\_1”.

> `φ` is the isomorphism induced by `d¹₀` and `π₁`: a point of `V ×_S X` lifted to a point
> `y` of `Y₁` is sent to the zeroth face of `y`.

```lean
lemma cartesian_actMap (Y : Stacks.Simplicial.Descent.Cartesian (simplicialScheme f)) {W : Over S}
    (q : W ⟶ (Over.map f).obj (descentObj (cartesianDatum Y)) ⨯ Over.mk f)
    (y : W.left ⟶ Y.1.left.obj (op ⦋1⦌))
    (h₁ : y ≫ Y.1.left.δ (1 : Fin 2) = (q ≫ prod.fst).left)
    (h₂ : y ≫ Y.1.hom.app (op ⦋1⦌) ≫ proj f 1 1 = (q ≫ prod.snd).left) :
    (q ≫ actMap (cartesianDatum Y)).left = y ≫ Y.1.left.δ (0 : Fin 2)
```

**`AlgebraicGeometry.SimplicialScheme.cartesianDescentDatum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/DescentViaSimplicialSchemes.lean, line 681](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/DescentViaSimplicialSchemes.lean#L681). The attribute's comment: “(V, φ) is a descent datum relative to X ⟶ S, for cartesian Y over (X/S)\_•”.

> **`(V, φ)` is a descent datum relative to `X ⟶ S`**, for `V = Y₀` over `X` and `φ` the
> isomorphism `V ×_S X ≅ X ×_S V` induced by `d¹₀`, `d¹₁` and `π₁` on a cartesian simplicial
> scheme `Y` over `(X/S)_•`.

```lean
def cartesianDescentDatum (Y : Stacks.Simplicial.Descent.Cartesian (simplicialScheme f)) :
    AlgebraicGeometry.DescentDatum f
```

## Tag 024C, a lemma

[Tag 024C](https://stacks.math.columbia.edu/tag/024C) in the Stacks Project.

**`AlgebraicGeometry.SimplicialScheme.cartesianDescentDatumFunctor_isEquivalence`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/CartesianSchemesDescentEquivalence.lean, line 748](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/CartesianSchemesDescentEquivalence.lean#L748).

> **The construction of Lemma 024B, from cartesian schemes over `(X/S)_•` to descent data
> relative to `X/S`, is an equivalence of categories.**

```lean
instance cartesianDescentDatumFunctor_isEquivalence (f : X ⟶ S) :
    (cartesianDescentDatumFunctor f).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.27, Tag 0248](https://stacks.math.columbia.edu/tag/0248)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
