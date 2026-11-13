---
declaration: section
origin: cited
lean: StacksRepresentableCFG.IsRepresentable, StacksRepresentableCFG.representable_iff, StacksRepresentableCFG.representing_pair_unique, CategoryTheory.Functor.exists_oneMorphism_inducing_hom, CategoryTheory.Functor.twoIsoQuotientEquivHomOfRepresentableBy
statement: formalized
proof: formalized
---

# 4.40 Representable categories fibred in groupoids

Section 4.40 of the Stacks Project, [Tag 04SE](https://stacks.math.columbia.edu/tag/04SE). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0046, a definition

[Tag 0046](https://stacks.math.columbia.edu/tag/0046) in the Stacks Project.

**`StacksRepresentableCFG.IsRepresentable`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/Criterion.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/Criterion.lean#L254). The attribute's comment: “stated for any category over C; Stacks' case is p fibred in groupoids, where an equivalence over C is an equivalence in the 2-category of groupoids over C (02XS)”.

> **Stacks 0046.** `p : S ⥤ C` is *representable* if it is representable by some object `X` of
> `C`: there are an object `X` of `C` and an equivalence `j : S → C/X` over `C`
> (`StacksRepresentableCFG.RepresentableBy`), i.e. strict 1-morphisms over `C` in both directions
> with unit and counit 2-isomorphisms over `C`.
>
> The predicate is stated for an arbitrary category `p : S ⥤ C` over `C`; Stacks applies it to
> categories fibred in groupoids. For those it is exactly the source's notion: `C/X` is fibred in
> groupoids, and the 2-category of categories fibred in groupoids over `C` (Stacks 02XS) has as
> 1-morphisms the functors strictly over `C` and as 2-morphisms the transformations lying over
> identities, as in the 2-category of categories over `C` (Stacks 003Y), so an equivalence in it
> is exactly an equivalence over `C` between `S` and `C/X`.

```lean
def IsRepresentable (p : 𝒮 ⥤ 𝒞) : Prop
```

## Tag 02Y3, a lemma

[Tag 02Y3](https://stacks.math.columbia.edu/tag/02Y3) in the Stacks Project.

**`StacksRepresentableCFG.representable_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/Criterion.lean, line 843](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/Criterion.lean#L843). The attribute's comment: “(1)”. References: SGA 4 I (6.5), “(ii)⇔(iv), special case”.

> **Stacks 02Y3** (part 1). A category fibred in groupoids `p : S ⥤ C` is representable
> if and only if `S` is fibred in setoids and its presheaf of isomorphism classes
> `\overline{S}` is representable.

```lean
theorem representable_iff (p : 𝒮 ⥤ 𝒞) :
    IsRepresentable p ↔ (p.IsFiberedInSetoids ∧ IsoClassRepresentable p)
```

**`StacksRepresentableCFG.representing_pair_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/RepresentingPairUnique.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/RepresentingPairUnique.lean#L128). The attribute's comment: “(2); stated for any category over C, Stacks' case is p fibred in groupoids”.

> **Stacks 02Y3** (part 2). If a category `p : 𝒮 ⥤ 𝒞` is representable, the pair `(X, j)`,
> with `j : 𝒮 → 𝒞/X` an equivalence over `𝒞`, is uniquely determined up to isomorphism: for
> two such pairs `(X, j)` and `(X', j')` there is an isomorphism `φ : X' ≅ X` in `𝒞` and a
> 2-isomorphism `α : (𝒞/φ) ∘ j' ≅ j` over `𝒞`, where `𝒞/φ = Over.map φ.hom : 𝒞/X' ⥤ 𝒞/X`;
> "over `𝒞`" means that `α` whiskered with `Over.forget X` is the identity 2-cell.

```lean
theorem representing_pair_unique (p : 𝒮 ⥤ 𝒞) {X X' : 𝒞} (j : RepresentableBy p X)
    (j' : RepresentableBy p X') :
    ∃ φ : X' ≅ X, ∃ α : j'.hom.functor ⋙ Over.map φ.hom ≅ j.hom.functor,
      Functor.whiskerRight α.hom (Over.forget X) =
        eqToHom (by rw [Functor.assoc, Over.mapForget_eq, j'.hom.w, j.hom.w])
```

## Tag 04SF, a lemma

[Tag 04SF](https://stacks.math.columbia.edu/tag/04SF) in the Stacks Project.

**`CategoryTheory.Functor.exists_oneMorphism_inducing_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/RepresentableFibred.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/RepresentableFibred.lean#L195). The attribute's comment: “Given `φ : X ⟶ Y` there is a 1-morphism inducing it, unique up to unique 2-isomorphism.”.

> **Stacks 04SF**, the precise form: given `φ : X ⟶ Y` there is a 1-morphism `G : 𝒳 ⥤ 𝒴` over
> `𝒞` which induces `φ` on isomorphism classes of objects, and any 1-morphism inducing `φ` is
> related to it by a unique 2-isomorphism. Inducing `φ` is spelled out through the bijections
> `\overline{𝒳}(U) ≃ (U ⟶ X)` and `\overline{𝒴}(U) ≃ (U ⟶ Y)` that representability supplies.

```lean
theorem exists_oneMorphism_inducing_hom (φ : X ⟶ Y) :
    ∃ (G : 𝒳 ⥤ 𝒴) (hG : G ⋙ q = p),
      (∀ (U : 𝒞) (c : p.isoClassPresheaf.obj (op U)),
        hY.equiv U ((isoClassMapOfCompEq hG).app (op U) c) = hX.equiv U c ≫ φ) ∧
      ∀ (H : 𝒳 ⥤ 𝒴) (hH : H ⋙ q = p),
        (∀ (U : 𝒞) (c : p.isoClassPresheaf.obj (op U)),
          hY.equiv U ((isoClassMapOfCompEq hH).app (op U) c) = hX.equiv U c ≫ φ) →
        ∃! e : G ≅ H, ∀ x : 𝒳, q.IsHomLift (𝟙 (p.obj x)) (e.hom.app x)
```

**`CategoryTheory.Functor.twoIsoQuotientEquivHomOfRepresentableBy`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/RepresentableFibred.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/RepresentableFibred.lean#L225).

> **Stacks 04SF.** Let `𝒳`, `𝒴` be categories fibred in groupoids over `𝒞` representable by
> objects `X`, `Y` of `𝒞`. Then `Mor_{Cat/𝒞}(𝒳, 𝒴)` modulo 2-isomorphism is `Mor_𝒞(X, Y)`. The
> bijection is the composite of Stacks 04SC, which identifies the left-hand side with the maps
> `\overline{𝒳} ⟶ \overline{𝒴}` of presheaves of isomorphism classes, with the Yoneda step
> `CategoryTheory.Functor.isoClassPresheafHomEquiv`.

```lean
noncomputable def twoIsoQuotientEquivHomOfRepresentableBy :
    _root_.Quotient (twoIsoSetoid p q) ≃ (X ⟶ Y)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.40, Tag 04SE](https://stacks.math.columbia.edu/tag/04SE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
