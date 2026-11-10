---
declaration: section
origin: cited
lean: CategoryTheory.Functor.Monoidal, CategoryTheory.MonoidalCategory.invertible_tfae, CategoryTheory.MonoidalCategory.HasInverse, CategoryTheory.MonoidalCategory.IsInvertible, CategoryTheory.ExactPairing, CategoryTheory.tensorRightHomEquiv_whiskerRight_comp_comp, CategoryTheory.tensorLeftHomEquiv_whiskerLeft_comp_comp, CategoryTheory.tensorRightAdjunction
statement: formalized
proof: formalized
---

# 4.43 Monoidal categories

Section 4.43 of the Stacks Project, [Tag 0FFJ](https://stacks.math.columbia.edu/tag/0FFJ). 10 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 8 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FFL, a definition

[Tag 0FFL](https://stacks.math.columbia.edu/tag/0FFL) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.Monoidal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.Monoidal#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L56) (StacksFrontier).

## Tag 0FFM, a lemma

[Tag 0FFM](https://stacks.math.columbia.edu/tag/0FFM) in the Stacks Project.

**`CategoryTheory.MonoidalCategory.invertible_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/InvertibleObject.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Monoidal/InvertibleObject.lean#L116).

> For an object `X` of a monoidal category, the following are equivalent:
> 1. `tensorLeft X` is an equivalence;
> 2. `tensorRight X` is an equivalence;
> 3. `X` is invertible, i.e. it has a two-sided tensor inverse.

```lean
theorem invertible_tfae (X : C) :
    [ (tensorLeft X).IsEquivalence,
      (tensorRight X).IsEquivalence,
      IsInvertible X ].TFAE
```

## Tag 0FFN, a definition

[Tag 0FFN](https://stacks.math.columbia.edu/tag/0FFN) in the Stacks Project.

**`CategoryTheory.MonoidalCategory.HasInverse`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/InvertibleObject.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Monoidal/InvertibleObject.lean#L38).

> A two-sided tensor inverse for an object `X` of a monoidal category: an object `inv`
> together with isomorphisms `X ⊗ inv ≅ 𝟙_ C` and `inv ⊗ X ≅ 𝟙_ C`.

```lean
structure HasInverse (X : C)
```

**`CategoryTheory.MonoidalCategory.IsInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/InvertibleObject.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Monoidal/InvertibleObject.lean#L49).

> An object `X` of a monoidal category is *invertible* if it admits a two-sided tensor
> inverse, i.e. an object `X'` with `X ⊗ X' ≅ 𝟙_ C` and `X' ⊗ X ≅ 𝟙_ C`.

```lean
def IsInvertible (X : C) : Prop
```

## Tag 0FFP, a definition

[Tag 0FFP](https://stacks.math.columbia.edu/tag/0FFP) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.ExactPairing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ExactPairing#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L58) (StacksFrontier).

## Tag 0FFQ, a lemma

[Tag 0FFQ](https://stacks.math.columbia.edu/tag/0FFQ) in the Stacks Project.

**`CategoryTheory.tensorRightHomEquiv_whiskerRight_comp_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/DualHomBijections.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Monoidal/DualHomBijections.lean#L59). The attribute's comment: “first bijection, natural in Z and Z'”.

> **Stacks Project, Tag 0FFQ**, first bijection. If `Y` is a left dual of `X` (in Mathlib,
> `[ExactPairing X Y]`), then `tensorRightHomEquiv Z' X Y Z : Mor(Z' ⊗ X, Z) ≃ Mor(Z', Z ⊗ Y)` is
> natural in `Z` and `Z'`: for `a : Z₂' ⟶ Z₁'` and `b : Z₁ ⟶ Z₂` it carries
> `(a ⊗ 1_X) ≫ f ≫ b` to `a ≫ e(f) ≫ (b ⊗ 1_Y)`.

```lean
theorem tensorRightHomEquiv_whiskerRight_comp_comp (X Y : C) [ExactPairing X Y] {Z₁' Z₂' Z₁ Z₂ : C}
    (a : Z₂' ⟶ Z₁') (f : Z₁' ⊗ X ⟶ Z₁) (b : Z₁ ⟶ Z₂) :
    tensorRightHomEquiv Z₂' X Y Z₂ (a ▷ X ≫ f ≫ b) =
      a ≫ tensorRightHomEquiv Z₁' X Y Z₁ f ≫ b ▷ Y
```

**`CategoryTheory.tensorLeftHomEquiv_whiskerLeft_comp_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/DualHomBijections.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Monoidal/DualHomBijections.lean#L71). The attribute's comment: “second bijection, natural in Z and Z'”.

> **Stacks Project, Tag 0FFQ**, second bijection. If `Y` is a left dual of `X` (in Mathlib,
> `[ExactPairing X Y]`), then `tensorLeftHomEquiv Z' X Y Z : Mor(Y ⊗ Z', Z) ≃ Mor(Z', X ⊗ Z)` is
> natural in `Z` and `Z'`: for `a : Z₂' ⟶ Z₁'` and `b : Z₁ ⟶ Z₂` it carries
> `(1_Y ⊗ a) ≫ f ≫ b` to `a ≫ e(f) ≫ (1_X ⊗ b)`.

```lean
theorem tensorLeftHomEquiv_whiskerLeft_comp_comp (X Y : C) [ExactPairing X Y] {Z₁' Z₂' Z₁ Z₂ : C}
    (a : Z₂' ⟶ Z₁') (f : Y ⊗ Z₁' ⟶ Z₁) (b : Z₁ ⟶ Z₂) :
    tensorLeftHomEquiv Z₂' X Y Z₂ (Y ◁ a ≫ f ≫ b) =
      a ≫ tensorLeftHomEquiv Z₁' X Y Z₁ f ≫ X ◁ b
```

Declarations registered for the tag:

- [`CategoryTheory.tensorRightAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.tensorRightAdjunction#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Monoidal/DualHomBijections.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Monoidal/DualHomBijections.lean#L82) (StacksFrontier): “first bijection as the adjunction tensorRight X ⊣ tensorRight Y”.
- [`CategoryTheory.tensorLeftAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.tensorLeftAdjunction#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Monoidal/DualHomBijections.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Monoidal/DualHomBijections.lean#L84) (StacksFrontier): “second bijection as the adjunction tensorLeft Y ⊣ tensorLeft X”.

## Tag 0FFR, a remark

[Tag 0FFR](https://stacks.math.columbia.edu/tag/0FFR) in the Stacks Project.

**`CategoryTheory.Adjunction.IsTensorCompatible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean#L93).

> An adjunction `adj : tensorRight X ⊣ tensorRight Y`, i.e. a bijection
> `Mor(Z' ⊗ X, Z) ≃ Mor(Z', Z ⊗ Y)` functorial in `Z` and `Z'`, is *compatible with the tensor
> structure* if for all `W`, `Z`, `Z'` the square
>
> ```
>   Mor(Z' ⊗ X, Z)         →  Mor(Z', Z ⊗ Y)
>    | id_W ⊗ -                | id_W ⊗ -
>    v                         v
>   Mor(W ⊗ Z' ⊗ X, W ⊗ Z) →  Mor(W ⊗ Z', W ⊗ Z ⊗ Y)
> ```
>
> commutes, the two vertical maps being `f ↦ 𝟙 W ⊗ f` read through the associators.

```lean
def IsTensorCompatible (adj : tensorRight X ⊣ tensorRight Y) : Prop
```

**`CategoryTheory.Adjunction.unit_app_comp_tensorEvaluation_whiskerRight`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean#L150).

> The first identity that an adjunction `tensorRight X ⊣ tensorRight Y` supplies for free,
> with no compatibility with the tensor structure assumed: `(ε ⊗ 1_Y) ∘ η_Y = 1_Y`, where `η_Y` is
> the component of the unit at `Y`.

```lean
theorem unit_app_comp_tensorEvaluation_whiskerRight :
    adj.unit.app Y ≫ adj.tensorEvaluation ▷ Y = (λ_ Y).inv
```

**`CategoryTheory.Adjunction.tensorCoevaluation_whiskerRight_comp_counit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean#L163).

> The second identity that an adjunction `tensorRight X ⊣ tensorRight Y` supplies for free,
> with no compatibility with the tensor structure assumed: `ε_X ∘ (η ⊗ 1_X) = 1_X`, where `ε_X` is
> the component of the counit at `X`.

```lean
theorem tensorCoevaluation_whiskerRight_comp_counit_app :
    adj.tensorCoevaluation ▷ X ≫ adj.counit.app X = (λ_ X).hom
```

**`CategoryTheory.ExactPairing.isTensorCompatible_tensorRightAdjunction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean#L177).

> The adjunction `tensorRight X ⊣ tensorRight Y` attached to an exact pairing is compatible
> with the tensor structure.

```lean
theorem ExactPairing.isTensorCompatible_tensorRightAdjunction (X Y : C) [ExactPairing X Y] :
    (tensorRightAdjunction X Y).IsTensorCompatible
```

**`CategoryTheory.Adjunction.IsTensorCompatible.exactPairing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean#L272).

> **The converse direction of Stacks 0FFR.** A tensor-compatible adjunction
> `tensorRight X ⊣ tensorRight Y` exhibits `Y` as a left dual of `X`: its candidate coevaluation
> and evaluation satisfy both triangle identities of an exact pairing.

```lean
def exactPairing (h : adj.IsTensorCompatible) : ExactPairing X Y
```

Declarations registered for the tag:

- [`CategoryTheory.leftDualIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.leftDualIso#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean#L287) (StacksFrontier).

## Tag 0FFS, a lemma

[Tag 0FFS](https://stacks.math.columbia.edu/tag/0FFS) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.ExactPairing.tensor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ExactPairing.tensor#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Monoidal/Rigid.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Monoidal/Rigid.lean#L193) (StacksFrontier).

## Tag 0FN8, a lemma

[Tag 0FN8](https://stacks.math.columbia.edu/tag/0FN8) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.BraidedCategory.exactPairing_swap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.BraidedCategory.exactPairing_swap#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L62) (StacksFrontier).

## Tag 0FFY, a definition

[Tag 0FFY](https://stacks.math.columbia.edu/tag/0FFY) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.Braided`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.Braided#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L60) (StacksFrontier).

## Tag 0GWJ, a remark

[Tag 0GWJ](https://stacks.math.columbia.edu/tag/0GWJ) in the Stacks Project.

**`InternalHom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean#L42). References: SGA 4 IV (10.2).

> **Definition 1 (Internal hom).**
> An internal hom on a monoidal category `C` consists of a bifunctor
> `hom : Cᵒᵖ ⥤ C ⥤ C` (contravariant in the first variable, covariant in the second)
> together with, for all objects `X, Y, Z`, a bijection
> `Φ X Y Z : Mor(X, hom(Y, Z)) ≃ Mor(X ⊗ Y, Z)` that is natural in `X`, in `Y`, and
> in `Z`.
>
> This is the opening clause of Stacks 0GWJ: `C` *has an internal hom* if for every pair `X, Y`
> there is an object `hom(X, Y)` with `Mor(X, hom(Y, Z)) = Mor(X ⊗ Y, Z)` functorially in
> `X, Y, Z`.

```lean
structure InternalHom (C : Type u) [Category.{v} C] [MonoidalCategory C]
```

**`InternalHom.ev`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean#L76). The attribute's comment: “(1)”. References: SGA 7 VIII (1.6), “more general”.

> **Construction of (1) Evaluation.**
> `ev_{X,Y} := Φ (id_{hom(X,Y)})`, the image of the identity under `Φ`.

```lean
def ev (X Y : C) : ih.homObj X Y ⊗ X ⟶ Y
```

**`InternalHom.comp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean#L84). The attribute's comment: “(2)”.

> **Construction of (2) Composition.**
> `c_{X,Y,Z}` is the image under `Φ⁻¹` (using `X` as the tensoring object) of the
> composite `hom(Y,Z) ⊗ hom(X,Y) ⊗ X → hom(Y,Z) ⊗ Y → Z` given by
> `(id ⊗ ev_{X,Y})` followed by `ev_{Y,Z}`.

```lean
def comp (X Y Z : C) : ih.homObj Y Z ⊗ ih.homObj X Y ⟶ ih.homObj X Z
```

**`InternalHom.tensorLeftMor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean#L92). The attribute's comment: “(3)”.

> **Construction of (3) Tensor on the left.**
> `t_{X,Y,Z}` is the image under `Φ⁻¹` of `id_Z ⊗ ev_{X,Y} : Z ⊗ hom(X,Y) ⊗ X → Z ⊗ Y`.

```lean
def tensorLeftMor (X Y Z : C) : Z ⊗ ih.homObj X Y ⟶ ih.homObj X (Z ⊗ Y)
```

**`InternalHom.coev`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean#L103). The attribute's comment: “(4)”.

> **Construction of (4) Unit / coevaluation.**
> `η_{X,Y} := ρ_Y⁻¹ ≫ (id_Y ⊗ u_X) ≫ t_{X,X,Y}`.

```lean
def coev (X Y : C) : Y ⟶ ih.homObj X (Y ⊗ X)
```

**`InternalHom.internalCurryMor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean#L111). The attribute's comment: “(5)”.

> **Construction of (5) Internalized currying (symmetric case).**
> `d_{X,Y,Z}` is the image under `Φ⁻¹` (using `hom(X,Y)` as the tensoring object) of the
> composite `hom(Y,Z) ⊗ X ⊗ hom(X,Y) → hom(Y,Z) ⊗ hom(X,Y) ⊗ X → hom(Y,Z) ⊗ Y → Z`,
> where the first arrow uses the braiding `σ_{X, hom(X,Y)}`.

```lean
def internalCurryMor [BraidedCategory C] (X Y Z : C) :
    ih.homObj Y Z ⊗ X ⟶ ih.homObj (ih.homObj X Y) Z
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.43, Tag 0FFJ](https://stacks.math.columbia.edu/tag/0FFJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
