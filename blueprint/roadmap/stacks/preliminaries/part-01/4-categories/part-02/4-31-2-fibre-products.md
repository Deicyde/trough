---
declaration: section
origin: cited
lean: CategoryTheory.Bicategory.TwoCommSq, CategoryTheory.Bicategory.TwoCommSq.PreHom, CategoryTheory.Bicategory.TwoCommSq.category, CategoryTheory.Bicategory.IsBiterminal, CategoryTheory.Bicategory.IsTwoFibreProduct, CategoryTheory.Limits.CategoricalPullback, CategoryTheory.Limits.CategoricalPullback.instCategory, CategoryTheory.Limits.CategoricalPullback.catCommSq
statement: formalized
proof: formalized
---

# 4.31 2-fibre products

Section 4.31 of the Stacks Project, [Tag 003O](https://stacks.math.columbia.edu/tag/003O). 15 tags here are carried by 28 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 003O, the section

[Tag 003O](https://stacks.math.columbia.edu/tag/003O) in the Stacks Project.

**`CategoryTheory.Bicategory.TwoCommSq`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/Defs.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/Defs.lean#L96).

> A **2-commutative cone** over the cospan `(f, g)`: an object `pt` together with
> 1-morphisms `fst : pt ⟶ x`, `snd : pt ⟶ y` and an invertible 2-morphism
> `iso : fst ≫ f ≅ snd ≫ g` filling the square.
>
> **Stacks 003O.** These are the objects of the category of 2-commutative diagrams over
> the cospan `(f, g)`.

```lean
structure TwoCommSq (f : x ⟶ z) (g : y ⟶ z)
```

**`CategoryTheory.Bicategory.TwoCommSq.PreHom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/Defs.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/Defs.lean#L117).

> A **pre-morphism of cones** `T ⟶ S`: a 1-morphism `hom : T.pt ⟶ S.pt` together with
> invertible comparison 2-cells `isoFst : T.fst ≅ hom ≫ S.fst`, `isoSnd : T.snd ≅ hom ≫ S.snd`
> subject to the Stacks 003O compatibility square.
>
> **Stacks 003O.** These are the morphisms of the category of 2-commutative diagrams, before
> passing to classes modulo the 2-cell equivalence `TwoCommSq.PreHom.Rel`.

```lean
structure TwoCommSq.PreHom (T S : TwoCommSq f g)
```

**`CategoryTheory.Bicategory.TwoCommSq.category`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/Defs.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/Defs.lean#L247).

> **Stacks 003O.** The category of 2-commutative diagrams over the cospan `(f, g)`:
> objects are the 2-commutative squares, and morphisms are pre-morphisms modulo the 2-cell
> equivalence, which is what makes composition strictly associative and unital.

```lean
instance TwoCommSq.category : Category (TwoCommSq f g)
```

## Tag 003P, a definition

[Tag 003P](https://stacks.math.columbia.edu/tag/003P) in the Stacks Project.

**`CategoryTheory.Bicategory.IsBiterminal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Bicategory/TwoOneCategory.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Bicategory/TwoOneCategory.lean#L67).

> A *final object* of a `(2,1)`-category `B`, defined as an object `T` such that every
> hom-category `X ⟶ T` has a terminal object. In a locally groupoidal `B` this says that every
> object admits a `1`-morphism to `T`, and any two such are isomorphic by a unique `2`-morphism
> (`CategoryTheory.Bicategory.isBiterminal_iff`).

```lean
def IsBiterminal (T : B) : Prop
```

## Tag 003Q, a definition

[Tag 003Q](https://stacks.math.columbia.edu/tag/003Q) in the Stacks Project.

**`CategoryTheory.Bicategory.IsTwoFibreProduct`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/Defs.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/Defs.lean#L270).

> **Stacks 003Q.** A 2-commutative square `P` over `(f, g)` is a **2-fibre product** of
> `f` and `g` when it is a terminal (final) object of the category `TwoCommSq f g` of
> 2-commutative diagrams. Its `fst`, `snd` and `iso` fields are the projections `p`, `q` and
> the invertible `ψ : f ∘ p ⟶ g ∘ q` of the source.

```lean
abbrev IsTwoFibreProduct (P : TwoCommSq f g) : Type _
```

## Tag 003R, an example

[Tag 003R](https://stacks.math.columbia.edu/tag/003R) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Limits.CategoricalPullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.CategoricalPullback#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L64) (StacksFrontier): “objects: triples (A, B, f)”.
- [`CategoryTheory.Limits.CategoricalPullback.instCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.CategoricalPullback.instCategory#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L65) (StacksFrontier): “morphisms: compatible pairs (a, b)”.
- [`CategoryTheory.Limits.CategoricalPullback.catCommSq`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.CategoricalPullback.catCommSq#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L67) (StacksFrontier): “projections and the transformation ψ”.

## Tag 02X9, a lemma

[Tag 02X9](https://stacks.math.columbia.edu/tag/02X9) in the Stacks Project.

**`CategoryTheory.Cat.isTwoFibreProduct_categoricalPullbackSq`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/CatCategoricalPullback.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/CatCategoricalPullback.lean#L214). The attribute's comment: “the explicit construction is a 2-fibre product in the sense of Stacks 003Q”.

> The explicit 2-fibre product of two functors is a 2-fibre product of them in the bicategory of
> categories: it is a terminal object of the category of 2-commutative squares over the cospan.

```lean
def isTwoFibreProduct_categoricalPullbackSq (F : A ⟶ C) (G : B ⟶ C) :
    IsTwoFibreProduct (categoricalPullbackSq F G)
```

## Tag 06RL, a remark

[Tag 06RL](https://stacks.math.columbia.edu/tag/06RL) in the Stacks Project.

**`CategoryTheory.Limits.CategoricalPullback.Quintuple`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/SymmetricModel.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/SymmetricModel.lean#L39).

> **Stacks 06RL.** The symmetric model of the 2-fibre product `𝒜 ×_𝒞 ℬ`: an object is a
> quintuple `(A, B, C, a, b)` with `A : 𝒜`, `B : ℬ`, `C : 𝒞` and isomorphisms `a : F A ≅ C`,
> `b : G B ≅ C`.

```lean
structure Quintuple
```

**`CategoryTheory.Limits.CategoricalPullback.Quintuple.toCategoricalPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/SymmetricModel.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/SymmetricModel.lean#L90).

> **Stacks 06RL.** The comparison functor from the symmetric model to the standard 2-fibre
> product: on objects it sends `(A, B, C, a, b)` to `(A, B, a ≪≫ b.symm)`, whose structural
> morphism is `b⁻¹ ∘ a`, and on morphisms it sends `(f, g, h)` to `(f, g)`.

```lean
def toCategoricalPullback : Quintuple F G ⥤ CategoricalPullback F G
```

**`CategoryTheory.Limits.CategoricalPullback.Quintuple.isEquivalence_toCategoricalPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/SymmetricModel.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/SymmetricModel.lean#L165).

> **Stacks 06RL.** The comparison functor from the symmetric quintuple model of the 2-fibre
> product to the standard model `CategoricalPullback F G` is an equivalence of categories.

```lean
theorem isEquivalence_toCategoricalPullback :
    (toCategoricalPullback (F := F) (G := G)).IsEquivalence
```

## Tag 02XA, a lemma

[Tag 02XA](https://stacks.math.columbia.edu/tag/02XA) in the Stacks Project.

**`CategoryTheory.Limits.CategoricalPullback.map`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/Functoriality.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/Functoriality.lean#L43).

> The functor `𝒳 ×_𝒵 𝒴 ⥤ 𝒜 ×_𝒞 ℬ` induced by a 2-commutative diagram between the two cospans: on
> objects it sends `(x, y, φ)` to `(L x, K y, α_y⁻¹ ∘ M(φ) ∘ β_x⁻¹)`, and on morphisms it applies `L`
> and `K` componentwise.

```lean
def CategoricalPullback.map (H : 𝒳 ⥤ 𝒵) (I : 𝒴 ⥤ 𝒵)
    (L : 𝒳 ⥤ 𝒜) (K : 𝒴 ⥤ ℬ) (M : 𝒵 ⥤ 𝒞) (F : 𝒜 ⥤ 𝒞) (G : ℬ ⥤ 𝒞)
    (α : K ⋙ G ≅ I ⋙ M) (β : H ⋙ M ≅ L ⋙ F) :
    CategoricalPullback H I ⥤ CategoricalPullback F G
```

## Tag 02XB, a lemma

[Tag 02XB](https://stacks.math.columbia.edu/tag/02XB) in the Stacks Project.

**`CategoryTheory.induced_faithful_of_faithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/InducedFunctor.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/InducedFunctor.lean#L174). The attribute's comment: “(1)”.

> **Stacks 02XB (1)** — If `K` and `L` are faithful, then the induced functor
> `𝒳 ×_𝒵 𝒴 ⥤ 𝒜 ×_𝒞 ℬ` is faithful.

```lean
theorem induced_faithful_of_faithful [K.Faithful] [L.Faithful] :
    (CategoricalPullback.map H I L K M F G α β).Faithful
```

**`CategoryTheory.induced_fullyFaithful_of_fullyFaithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/InducedFunctor.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/InducedFunctor.lean#L183). The attribute's comment: “(2)”. References: SGA 1 VI (4.1).

> **Stacks 02XB (2)** — If `K` and `L` are fully faithful and `M` is faithful,
> then the induced functor `𝒳 ×_𝒵 𝒴 ⥤ 𝒜 ×_𝒞 ℬ` is fully faithful.

```lean
theorem induced_fullyFaithful_of_fullyFaithful
    [K.Faithful] [K.Full] [L.Faithful] [L.Full] [M.Faithful] :
    (CategoricalPullback.map H I L K M F G α β).Faithful ∧
      (CategoricalPullback.map H I L K M F G α β).Full
```

**`CategoryTheory.induced_isEquivalence_of_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/InducedFunctor.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/InducedFunctor.lean#L201). The attribute's comment: “(3)”.

> **Stacks 02XB (3)** — If `K` and `L` are equivalences and `M` is fully
> faithful, then the induced functor `𝒳 ×_𝒵 𝒴 ⥤ 𝒜 ×_𝒞 ℬ` is an equivalence
> of categories.

```lean
theorem induced_isEquivalence_of_isEquivalence
    [K.IsEquivalence] [L.IsEquivalence] [M.Faithful] [M.Full] :
    (CategoricalPullback.map H I L K M F G α β).IsEquivalence
```

## Tag 02XC, a lemma

[Tag 02XC](https://stacks.math.columbia.edu/tag/02XC) in the Stacks Project.

**`CategoryTheory.Limits.CategoricalPullback.assocFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/Associativity.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/Associativity.lean#L33).

> **Stacks 02XC.** The canonical comparison functor
> `(𝒜 ×_ℬ 𝒞) ×_𝒟 ℰ ⥤ 𝒜 ×_ℬ (𝒞 ×_𝒟 ℰ)`, rebracketing `((A, C, φ), E, ψ) ↦ (A, (C, E, ψ), φ)`.

```lean
def CategoricalPullback.assocFunctor
    (H : 𝒜 ⥤ ℬ) (K : 𝒞 ⥤ ℬ) (L : 𝒞 ⥤ 𝒟) (M : ℰ ⥤ 𝒟) :
    CategoricalPullback (CategoricalPullback.π₂ H K ⋙ L) M ⥤
      CategoricalPullback H (CategoricalPullback.π₁ L M ⋙ K)
```

**`CategoryTheory.Limits.CategoricalPullback.assoc`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/Associativity.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/Associativity.lean#L58).

> **Stacks 02XC.** Associativity of 2-fibre products of categories: for
> `H : 𝒜 ⥤ ℬ`, `K : 𝒞 ⥤ ℬ`, `L : 𝒞 ⥤ 𝒟` and `M : ℰ ⥤ 𝒟` the two iterated 2-fibre products
> are canonically equivalent, `(𝒜 ×_ℬ 𝒞) ×_𝒟 ℰ ≌ 𝒜 ×_ℬ (𝒞 ×_𝒟 ℰ)`, via
> `CategoricalPullback.assocFunctor`.

```lean
def CategoricalPullback.assoc
    (H : 𝒜 ⥤ ℬ) (K : 𝒞 ⥤ ℬ) (L : 𝒞 ⥤ 𝒟) (M : ℰ ⥤ 𝒟) :
    CategoricalPullback (CategoricalPullback.π₂ H K ⋙ L) M ≌
      CategoricalPullback H (CategoricalPullback.π₁ L M ⋙ K)
```

## Tag 04S7, a lemma

[Tag 04S7](https://stacks.math.columbia.edu/tag/04S7) in the Stacks Project.

**`CategoryTheory.Limits.CategoricalPullback.pr₀₂`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/TripleProjection.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/TripleProjection.lean#L91).

> **Stacks 04S7.** For a commuting inner square `G ⋙ P = H ⋙ Q` under the diagram
> `𝒜 → ℬ ← 𝒞 → 𝒟 ← ℰ`, the canonical functor `(𝒜 ×_ℬ 𝒞) ×_𝒟 ℰ ⥤ 𝒜 ×_ℱ ℰ` which forgets the
> middle factor and transports the two structural isomorphisms into `ℱ`.

```lean
def CategoricalPullback.pr₀₂ (h : G ⋙ P = H ⋙ Q) :
    CategoricalPullback (CategoricalPullback.π₂ F G ⋙ H) I ⥤
      CategoricalPullback (F ⋙ P) (I ⋙ Q)
```

## Tag 02XD, a lemma

[Tag 02XD](https://stacks.math.columbia.edu/tag/02XD) in the Stacks Project.

**`CategoryTheory.Limits.CategoricalPullback.assocComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/Cancellation.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/Cancellation.lean#L107).

> **Stacks 02XD.** The canonical equivalence of categories `(A ×_B C) ×_C D ≌ A ×_B D`
> for `A --F--> B <--G-- C <--H-- D`, i.e.
> `CategoricalPullback (π₂ F G) H ≌ CategoricalPullback F (H ⋙ G)`, given by
> `assocCompFunctor`.

```lean
def assocComp :
    CategoricalPullback (π₂ F G) H ≌ CategoricalPullback F (H ⋙ G)
```

## Tag 02XE, a lemma

[Tag 02XE](https://stacks.math.columbia.edu/tag/02XE) in the Stacks Project.

**`CategoryTheory.Limits.CategoricalPullback.prodDiagFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/Diagonal.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/Diagonal.lean#L58).

> **Stacks 02XE.** The canonical comparison functor
> `CategoricalPullback (G₁.prod G₂) (Functor.diag S) ⥤ CategoricalPullback G₁ G₂`. On objects it
> sends `((X₁, X₂), Y, φ)` to `(X₁, X₂, φ₁ ≪≫ φ₂⁻¹)`, where `φ = (φ₁, φ₂)`; on morphisms it acts as
> the identity on the underlying pair of component morphisms.

```lean
def prodDiagFunctor (G₁ : C₁ ⥤ S) (G₂ : C₂ ⥤ S) :
    CategoricalPullback (G₁.prod G₂) (Functor.diag S) ⥤ CategoricalPullback G₁ G₂
```

**`CategoryTheory.Limits.CategoricalPullback.isEquivalence_prodDiagFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/Diagonal.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/Diagonal.lean#L165).

> **Stacks 02XE.** The canonical comparison functor `prodDiagFunctor` is an equivalence of
> categories: the 2-fibre product of `G₁ × G₂ : C₁ × C₂ ⥤ S × S` and the diagonal `Δ : S ⥤ S × S`
> is canonically equivalent to `C₁ ×_S C₂`.

```lean
theorem isEquivalence_prodDiagFunctor (G₁ : C₁ ⥤ S) (G₂ : C₂ ⥤ S) :
    (prodDiagFunctor G₁ G₂).IsEquivalence
```

**`CategoryTheory.Limits.CategoricalPullback.prodDiagEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/Diagonal.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/Diagonal.lean#L174).

> **Stacks 02XE.** The canonical equivalence of categories
> `CategoricalPullback (G₁.prod G₂) (Functor.diag S) ≌ CategoricalPullback G₁ G₂`, induced by
> `prodDiagFunctor`.

```lean
noncomputable def prodDiagEquiv (G₁ : C₁ ⥤ S) (G₂ : C₂ ⥤ S) :
    CategoricalPullback (G₁.prod G₂) (Functor.diag S) ≌ CategoricalPullback G₁ G₂
```

## Tag 02XF, a lemma

[Tag 02XF](https://stacks.math.columbia.edu/tag/02XF) in the Stacks Project.

**`CategoryTheory.Limits.CategoricalPullback.diagComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/IteratedDiagonal.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/IteratedDiagonal.lean#L98).

> **Stacks 02XF.** The comparison functor `(𝒞 ×_𝒮 𝒞) ×_{𝒞 × 𝒞} 𝒞 ⥤ 𝒞 ×_{𝒮 × 𝒮} 𝒮`. On objects
> it sends `((c₁, c₂, φ), c₃, ψ)` to `(c₃, G₁ c₁, (G₁ ψ₁⁻¹, φ⁻¹ ∘ G₂ ψ₂⁻¹))`, and on morphisms
> `((α₁, α₂), α₃)` to `(α₃, G₁ α₁)`.

```lean
def diagComparison : diagComparisonSource G₁ G₂ ⥤ diagComparisonTarget G₁ G₂
```

**`CategoryTheory.Limits.CategoricalPullback.isEquivalence_diagComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/IteratedDiagonal.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/IteratedDiagonal.lean#L234).

> **Stacks 02XF.** The comparison functor `(𝒞 ×_𝒮 𝒞) ×_{𝒞 × 𝒞} 𝒞 ⥤ 𝒞 ×_{𝒮 × 𝒮} 𝒮` is an
> equivalence of categories. (The source asserts an isomorphism of categories; that is corrected to
> an equivalence per the Stacks comments #5394 and #5627, since the functor is in general not
> bijective on objects.)

```lean
theorem isEquivalence_diagComparison : (diagComparison G₁ G₂).IsEquivalence
```

## Tag 04Z1, a lemma

[Tag 04Z1](https://stacks.math.columbia.edu/tag/04Z1) in the Stacks Project.

**`CategoryTheory.Limits.CategoricalPullback.relativeDiagonalSquareIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/AsPullback.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/AsPullback.lean#L89).

> **Stacks 04Z1.** The natural isomorphism `σ : Θ ⋙ ρ ≅ π ⋙ Δ_{C/D}` witnessing that the
> square 2-commutes; its component at `(a, b, f)` is `(𝟙_{F a}, f⁻¹)`.

```lean
def relativeDiagonalSquareIso :
    (mapBase F G H ⋙ toRelativeDiagonalTarget F G H) ≅ (toBase F G ⋙ relativeDiagonal H)
```

**`CategoryTheory.Limits.CategoricalPullback.toRelativeDiagonalPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/AsPullback.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/AsPullback.lean#L108).

> **Stacks 04Z1.** The functor `A ×_C B ⥤ (A ×_D B) ×_{C ×_D C} C` induced by
> `(Θ, π, σ)` into the explicit 2-fibre product of the cospan
> `A ×_D B --ρ--> C ×_D C <--Δ_{C/D}-- C`. On objects it sends `(a, b, f)` to
> `((a, b, H f), F a, (𝟙_{F a}, f⁻¹))`, and a morphism `(x, y)` to `((x, y), F x)`.

```lean
def toRelativeDiagonalPullback :
    CategoricalPullback F G ⥤
      CategoricalPullback (toRelativeDiagonalTarget F G H) (relativeDiagonal H)
```

**`CategoryTheory.Limits.CategoricalPullback.isEquivalence_toRelativeDiagonalPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/AsPullback.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/AsPullback.lean#L179).

> **Stacks 04Z1.** The square above is a 2-fibre product diagram: the induced functor
> `A ×_C B ⥤ (A ×_D B) ×_{C ×_D C} C` is an equivalence of categories.

```lean
theorem isEquivalence_toRelativeDiagonalPullback :
    (toRelativeDiagonalPullback F G H).IsEquivalence
```

## Tag 04YR, a lemma

[Tag 04YR](https://stacks.math.columbia.edu/tag/04YR) in the Stacks Project.

**`CategoryTheory.Limits.CategoricalPullback.baseChangeDiagonalSquareIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/DiagonalBaseChange.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/DiagonalBaseChange.lean#L104).

> **Stacks 04YR.** The structural 2-cell `r ⋙ Δ_{X/Y} ≅ Δ_{U/V} ⋙ (r × r)` of the base-change
> square for the diagonal. Both composites have both projections equal to `r = π₁ h s`, so the
> 2-cell is the canonical one with identity projections.

```lean
def baseChangeDiagonalSquareIso :
    (π₁ h s ⋙ relativeDiagonal h) ≅ (relativeDiagonal (π₂ h s) ⋙ mapDiag h s)
```

**`CategoryTheory.Limits.CategoricalPullback.baseChangeDiagonalSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/DiagonalBaseChange.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/DiagonalBaseChange.lean#L126).

> **Stacks 04YR.** The base-change square for the diagonal, over `U = h ⊡ s`: its legs are
> `r = π₁ h s : U ⥤ X` and `Δ_{U/V} = relativeDiagonal (π₂ h s) : U ⥤ U ×_V U`, its cospan is
> `Δ_{X/Y} = relativeDiagonal h : X ⥤ X ×_Y X` and `r × r = mapDiag h s`, and its structural
> 2-cell is `baseChangeDiagonalSquareIso`.

```lean
def baseChangeDiagonalSquare :
    CatCommSqOver (relativeDiagonal h) (mapDiag h s) (h ⊡ s)
```

**`CategoryTheory.Limits.CategoricalPullback.isEquivalence_baseChangeDiagonalComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/DiagonalBaseChange.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/DiagonalBaseChange.lean#L402).

> **Stacks 04YR.** The diagonal is stable under base change: for `h : X ⥤ Y` and `s : V ⥤ Y`,
> with `U = X ×_Y V`, `r = π₁ h s` and `g = π₂ h s`, the square
> `Δ_{U/V} : U ⥤ U ×_V U`, `r : U ⥤ X` over `Δ_{X/Y} : X ⥤ X ×_Y X`, `r × r : U ×_V U ⥤ X ×_Y X`
> is 2-cartesian, i.e. its comparison functor `U ⥤ Δ_{X/Y} ⊡ (r × r)` is an equivalence of
> categories. The quasi-inverse is `baseChangeDiagonalInverse`, the unit is an identity by
> `baseChangeDiagonalComparison_comp_inverse`, and the counit is
> `baseChangeDiagonalCounitIso`.

```lean
theorem isEquivalence_baseChangeDiagonalComparison :
    Functor.IsEquivalence (comparison (relativeDiagonal h) (mapDiag h s)
      (baseChangeDiagonalSquare h s))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.31, Tag 003O](https://stacks.math.columbia.edu/tag/003O)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
