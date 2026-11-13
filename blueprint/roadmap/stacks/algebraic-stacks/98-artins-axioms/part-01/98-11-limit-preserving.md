---
declaration: section
origin: cited
lean: Deformation.Artin.IsLimitPreserving, AlgebraicGeometry.Stack.isLimitPreserving_twoFibreProduct, AlgebraicGeometry.Stack.isLimitPreservingOnObjects_toTerminalCFG_twoFibreProduct, AlgebraicGeometry.Stack.isStackInSetoids_and_isLimitPreservingOnObjects_of_isRepresentableBySpaceLocallyOfFinPres, AlgebraicGeometry.Stack.isStackInSetoids_isLimitPreserving_tfae, AlgebraicGeometry.Stack.isStackInSetoids_and_isLimitPreservingOnObjects_of_isLimitPreserving, AlgebraicGeometry.Stack.isLocallyOfFiniteType_diagonal
statement: formalized
proof: formalized
---

# 98.11 Limit preserving

Section 98.11 of the Stacks Project, [Tag 07XK](https://stacks.math.columbia.edu/tag/07XK). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07XL, a definition

[Tag 07XL](https://stacks.math.columbia.edu/tag/07XL) in the Stacks Project.

**`Deformation.Artin.IsLimitPreserving`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/LimitPreserving.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/LimitPreserving.lean#L144).

> A category fibred in groupoids is limit preserving if for every directed inverse
> limit of affine schemes the canonical comparison `colim 𝒳_{Tᵢ} ⥤ 𝒳_T` is an equivalence
> of categories.

```lean
public abbrev IsLimitPreserving
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : CatFiberedInGroupoids.{u, vX, u + 1, uX}
      (BigFppfOver B S hS)) : Prop
```

## Tag 07XM, a lemma

[Tag 07XM](https://stacks.math.columbia.edu/tag/07XM) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLimitPreserving_twoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingTwoFibreProduct.lean, line 715](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingTwoFibreProduct.lean#L715). The attribute's comment: “part (2)”.

> **Stacks 07XM, part (2).** If `𝒳`, `𝒴` and `𝒵` are limit preserving categories fibred in
> groupoids over `(Sch/S)_{fppf}`, then so is the 2-fibre product `𝒳 ×_𝒴 𝒵`: for every directed
> inverse system of affine schemes with limit `T`, the canonical comparison from the colimit of the
> fibre categories over the stages to the fibre category over `T` is an equivalence.

```lean
theorem isLimitPreserving_twoFibreProduct
    (h𝒳 : Deformation.Artin.IsLimitPreserving.{u, v, w, u + 1, u} B S hS 𝒳)
    (h𝒴 : Deformation.Artin.IsLimitPreserving.{u, v, w, u + 1, u} B S hS 𝒴)
    (h𝒵 : Deformation.Artin.IsLimitPreserving.{u, v, w, u + 1, u} B S hS 𝒵) :
    Deformation.Artin.IsLimitPreserving.{u, v, w, u + 1, u} B S hS
      (BigFppfOver.twoFibreProduct.{u, u, u + 1} B S hS 𝒳 𝒴 𝒵 pf qf)
```

**`AlgebraicGeometry.Stack.isLimitPreservingOnObjects_toTerminalCFG_twoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingTwoFibreProductObjects.lean, line 435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingTwoFibreProductObjects.lean#L435). The attribute's comment: “part (1)”.

> **Stacks 07XM, part (1).** If the structure morphisms of `𝒳` and of `𝒵` to `(Sch/S)_{fppf}`
> are limit preserving on objects and `𝒴` is limit preserving, then the structure morphism of the
> 2-fibre product `𝒳 ×_𝒴 𝒵` to `(Sch/S)_{fppf}` is limit preserving on objects.
>
> Part (2) of Stacks 07XM, that `𝒳 ×_𝒴 𝒵` is limit preserving when `𝒳`, `𝒴` and `𝒵` are, is
> `AlgebraicGeometry.Stack.isLimitPreserving_twoFibreProduct`.

```lean
theorem isLimitPreservingOnObjects_toTerminalCFG_twoFibreProduct
    (h𝒳 : BigFppfOver.IsLimitPreservingOnObjects.{u, v, w, u, u + 1} B S hS 𝒳
      (terminalCFG B S hS) (Bicategory.InducedBicategory.mkHom (toTerminalCFG B S hS 𝒳)))
    (h𝒵 : BigFppfOver.IsLimitPreservingOnObjects.{u, v, w, u, u + 1} B S hS 𝒵
      (terminalCFG B S hS) (Bicategory.InducedBicategory.mkHom (toTerminalCFG B S hS 𝒵)))
    (h𝒴 : Deformation.Artin.IsLimitPreserving.{u, v, w, u + 1, u} B S hS 𝒴) :
    BigFppfOver.IsLimitPreservingOnObjects.{u, v, w, u, u + 1} B S hS
      (BigFppfOver.twoFibreProduct.{u, u, u + 1} B S hS 𝒳 𝒴 𝒵 pf qf) (terminalCFG B S hS)
      (Bicategory.InducedBicategory.mkHom (toTerminalCFG B S hS
        (BigFppfOver.twoFibreProduct.{u, u, u + 1} B S hS 𝒳 𝒴 𝒵 pf qf)))
```

## Tag 07XN, a lemma

[Tag 07XN](https://stacks.math.columbia.edu/tag/07XN) in the Stacks Project.

**`AlgebraicGeometry.Stack.isStackInSetoids_and_isLimitPreservingOnObjects_of_isRepresentableBySpaceLocallyOfFinPres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingSetoidRepresentable.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingSetoidRepresentable.lean#L207). The attribute's comment: “the implication (3) ⟹ (1), with condition (3) read as `IsRepresentableBySpaceLocallyOfFinitePresentation` and limit preservation on objects for cofiltered index categories in the universe of the schemes, which is the scope of the library's form of Tag 06CX that the proof uses”.

> **Stacks 07XN, the implication (3) ⟹ (1).** A category fibred in groupoids over the big fppf
> site of `S` which is representable by an algebraic space locally of finite presentation over `S`
> is a stack in setoids whose structure morphism to `(Sch/S)_{fppf}` is limit preserving on
> objects.
>
> The setoid clause is the implication (3) ⟹ (1) of Stacks 04SZ, and the limit-preservation clause
> is Stacks 06CX read at the structure morphism. Neither algebraicity nor any cited hypothesis is
> used.

```lean
theorem isStackInSetoids_and_isLimitPreservingOnObjects_of_isRepresentableBySpaceLocallyOfFinPres
    (h : IsRepresentableBySpaceLocallyOfFinitePresentation B S hS 𝒳) :
    𝒳.val.p.IsStackInSetoids (BigFppfOver.topology B S hS) ∧
      BigFppfOver.IsLimitPreservingOnObjects.{u, u, u, u, u + 1} B S hS 𝒳
        (terminalCFG B S hS)
        (Bicategory.InducedBicategory.mkHom (toTerminalCFG B S hS 𝒳))
```

**`AlgebraicGeometry.Stack.isStackInSetoids_isLimitPreserving_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingStackInSetoids.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingStackInSetoids.lean#L303).

> **Stacks 07XN.** For an algebraic stack `𝒳` over the big fppf site of a scheme `S` the
> following are equivalent:
>
> 1. `𝒳` is a stack in setoids and its structure morphism `𝒳 ⟶ (Sch/S)_{fppf}` is limit preserving
>    on objects in the sense of Stacks 06CU;
> 2. `𝒳` is a stack in setoids and is limit preserving in the sense of Stacks 07XL;
> 3. `𝒳` is representable by an algebraic space over `S` which is locally of finite presentation
>    over `S`, i.e. `AlgebraicGeometry.Stack.IsRepresentableBySpaceLocallyOfFinitePresentation`.
>
> The three implications proved are the cycle (1) ⟹ (3) ⟹ (2) ⟹ (1). Inverse systems are indexed
> by categories in the universe `u` of the schemes, which is the size the source's directed inverse
> systems have and the size at which the inputs of the two nontrivial implications are available.

```lean
theorem isStackInSetoids_isLimitPreserving_tfae
    (halg : IsAlgebraicStack.{u, t} B S hS 𝒳.val) :
    List.TFAE
      [𝒳.val.p.IsStackInSetoids (BigFppfOver.topology B S hS) ∧
          BigFppfOver.IsLimitPreservingOnObjects.{u, u, u, u, u + 1} B S hS 𝒳
            (terminalCFG B S hS) (Bicategory.InducedBicategory.mkHom (toTerminalCFG B S hS 𝒳)),
        𝒳.val.p.IsStackInSetoids (BigFppfOver.topology B S hS) ∧
          Deformation.Artin.IsLimitPreserving.{u, u, u, u + 1, u} B S hS 𝒳,
        IsRepresentableBySpaceLocallyOfFinitePresentation B S hS 𝒳]
```

**`AlgebraicGeometry.Stack.isStackInSetoids_and_isLimitPreservingOnObjects_of_isLimitPreserving`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingStructureMorphism.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingStructureMorphism.lean#L216). The attribute's comment: “the implication (2) ⟹ (1)”.

> **Stacks 07XN, the implication (2) ⟹ (1).** A category fibred in groupoids over the big fppf
> site of `S` which is a stack in setoids and is limit preserving is a stack in setoids whose
> structure morphism to `(Sch/S)_{fppf}` is limit preserving on objects.
>
> The stack-in-setoids clause is common to the two conditions, and the limit-preservation clause
> weakens from an equivalence of categories to essential surjectivity. The remaining implications of
> Stacks 07XN are not proved here; see the implementation notes of this module.

```lean
theorem isStackInSetoids_and_isLimitPreservingOnObjects_of_isLimitPreserving
    (h : 𝒳.val.p.IsStackInSetoids (BigFppfOver.topology B S hS) ∧
      Deformation.Artin.IsLimitPreserving.{u, v, w, u + 1, u} B S hS 𝒳) :
    𝒳.val.p.IsStackInSetoids (BigFppfOver.topology B S hS) ∧
      BigFppfOver.IsLimitPreservingOnObjects.{u, v, w, u, u + 1} B S hS 𝒳
        (terminalCFG B S hS)
        (Bicategory.InducedBicategory.mkHom (toTerminalCFG B S hS 𝒳))
```

## Tag 0CXI, a lemma

[Tag 0CXI](https://stacks.math.columbia.edu/tag/0CXI) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLocallyOfFiniteType_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DiagonalLocallyOfFiniteType.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DiagonalLocallyOfFiniteType.lean#L239).

> **Stacks 0CXI.** Let `𝒳` be a category fibred in groupoids over the big fppf site of a scheme
> `S` whose diagonal `Δ : 𝒳 ⟶ 𝒳 × 𝒳` is representable by algebraic spaces. If `𝒳` is limit
> preserving then `Δ` is locally of finite type.
>
> The base change of `Δ` along a scheme-valued point of `𝒳 × 𝒳` over `U` is the presheaf of
> vertical morphisms between the two components of that point, so a section of the representing
> algebraic space over an affine inverse limit is a vertical morphism there, and limit preservation
> of `𝒳` makes it the restriction of one at a finite stage. The surjectivity criterion of Stacks
> 0CM6 turns that into local finite presentation of the representing space over `U`, and Stacks
> 0464 into local finite type.

```lean
theorem isLocallyOfFiniteType_diagonal
    (hΔ : IsRepresentableByAlgebraicSpaces B S hS (diagonal.{u, u, u + 1} B S hS 𝒳).hom)
    (h𝒳 : Deformation.Artin.IsLimitPreserving.{u, u, u, u + 1, u} B S hS 𝒳) :
    HasRelativeProperty.{u, u, u + 1, u} B S hS (Space.locallyOfFiniteTypeProperty B S hS)
      (diagonal.{u, u, u + 1} B S hS 𝒳) hΔ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.11, Tag 07XK](https://stacks.math.columbia.edu/tag/07XK)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
