---
declaration: section
origin: cited
lean: IsRepresentable, StacksRepresentableCFG.representable_iff, StacksRepresentableCFG.representing_object_unique, CategoryTheory.Functor.exists_oneMorphism_inducing_hom, CategoryTheory.Functor.twoIsoQuotientEquivHomOfRepresentableBy
statement: formalized
proof: formalized
---

# 4.40 Representable categories fibred in groupoids

Section 4.40 of the Stacks Project, [Tag 04SE](https://stacks.math.columbia.edu/tag/04SE). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0046, a definition

[Tag 0046](https://stacks.math.columbia.edu/tag/0046) in the Stacks Project.

**`IsRepresentable`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/Defs.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/Defs.lean#L51).

> A category fibred in groupoids `p : 𝒮 ⥤ 𝒞` is *representable* if there exists
> an object `X` of `𝒞` and an equivalence `j : 𝒮 ≌ Over X` over `𝒞`.

```lean
structure IsRepresentable {𝒞 : Type*} [Category 𝒞] {𝒮 : Type*} [Category 𝒮]
    (p : 𝒮 ⥤ 𝒞) [IsFibered p] : Prop
```

## Tag 02Y3, a lemma

[Tag 02Y3](https://stacks.math.columbia.edu/tag/02Y3) in the Stacks Project.

**`StacksRepresentableCFG.representable_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/Criterion.lean, line 829](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/Criterion.lean#L829). The attribute's comment: “(1)”. References: SGA 4 I (6.5), “(ii)⇔(iv), special case”.

> **Stacks 02Y3** (part 1). A category fibred in groupoids `p : S ⥤ C` is representable
> if and only if `S` is fibred in setoids and its presheaf of isomorphism classes
> `\overline{S}` is representable.

```lean
theorem representable_iff (p : 𝒮 ⥤ 𝒞) :
    IsRepresentable p ↔ (p.IsFiberedInSetoids ∧ IsoClassRepresentable p)
```

**`StacksRepresentableCFG.representing_object_unique`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/Criterion.lean, line 841](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/Representability/Criterion.lean#L841). The attribute's comment: “(2)”.

> **Stacks 02Y3** (part 2). If `p : S ⥤ C` is representable by both `X` (via `j`) and `X'`
> (via `j'`), then the representing objects are **canonically isomorphic** in `C`: this is
> the isomorphism `X' ≅ X` induced by the composite equivalence over `C`, obtained by
> transporting the terminal object `(X', 𝟙 X')` of `Over X'` to the terminal object
> `(X, 𝟙 X)` of `Over X`.

```lean
noncomputable def representing_object_unique (p : 𝒮 ⥤ 𝒞)
    {X X' : 𝒞} (j : RepresentableBy p X) (j' : RepresentableBy p X') :
    X' ≅ X
```

## Tag 04SF, a lemma

[Tag 04SF](https://stacks.math.columbia.edu/tag/04SF) in the Stacks Project.

**`CategoryTheory.Functor.exists_oneMorphism_inducing_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/RepresentableFibred.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/RepresentableFibred.lean#L195). The attribute's comment: “Given `φ : X ⟶ Y` there is a 1-morphism inducing it, unique up to unique 2-isomorphism.”.

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

**`CategoryTheory.Functor.twoIsoQuotientEquivHomOfRepresentableBy`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/RepresentableFibred.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/RepresentableFibred.lean#L225).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
