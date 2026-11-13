---
declaration: section
origin: cited
lean: AlgebraicGeometry.varietyEquivalenceFinitelyGeneratedFieldExtensionOpposite, AlgebraicGeometry.Variety.nonempty_iso_tfae
statement: formalized
proof: formalized
---

# 33.4 Varieties and rational maps

Section 33.4 of the Stacks Project, [Tag 0BXM](https://stacks.math.columbia.edu/tag/0BXM). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BXN, a theorem

[Tag 0BXN](https://stacks.math.columbia.edu/tag/0BXN) in the Stacks Project.

**`AlgebraicGeometry.varietyEquivalenceFinitelyGeneratedFieldExtensionOpposite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Varieties/FunctionFieldEquivalence/Equivalence.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Varieties/FunctionFieldEquivalence/Equivalence.lean#L85).

> **Stacks Project, Tag 0BXN.** Varieties and dominant rational maps over a field are
> contravariantly equivalent to finitely generated field extensions of that field.

```lean
noncomputable def varietyEquivalenceFinitelyGeneratedFieldExtensionOpposite
    (k : Type u) [Field k] :
    Variety k ≌ (FinitelyGeneratedFieldExtension k)ᵒᵖ
```

## Tag 0BXP, a lemma

[Tag 0BXP](https://stacks.math.columbia.edu/tag/0BXP) in the Stacks Project.

**`AlgebraicGeometry.Variety.nonempty_iso_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/RationalMap/BirationalVariety.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/RationalMap/BirationalVariety.lean#L140). The attribute's comment: “Item (1), birationality of varieties, which the source defines as Spec(k)-birationality in the sense of Tag 0A20, is isomorphism in `AlgebraicGeometry.Variety k`, the category of varieties over `k` and dominant rational maps of Tag 0BXN. The function field in item (2) is the stalk at the generic point with its `k`-algebra structure from Tag 0BXN. The opens in items (3) and (4) are nonempty, as varieties are, and the isomorphism and the morphism commute with the structure morphisms to `Spec k`.”.

> **Stacks Project, Tag 0BXP.** Let `X` and `Y` be varieties over a field `k`. The following
> are equivalent:
> 1. `X` and `Y` are birational varieties, that is, isomorphic in the category of varieties over
>    `k` and dominant rational maps;
> 2. the function fields `k(X)` and `k(Y)` are isomorphic as extensions of `k`;
> 3. there exist nonempty opens of `X` and `Y` which are isomorphic as varieties over `k`;
> 4. there exist an open `U ⊆ X` and a birational morphism `U → Y` of varieties over `k`.

```lean
theorem Variety.nonempty_iso_tfae (X Y : Variety k) :
    List.TFAE [
      Nonempty (X ≅ Y),
      Nonempty (X.toScheme.functionField ≃ₐ[k] Y.toScheme.functionField),
      ∃ (U : X.toScheme.Opens) (V : Y.toScheme.Opens),
        (U : Set X.toScheme).Nonempty ∧ (V : Set Y.toScheme).Nonempty ∧
          ∃ e : U.toScheme ≅ V.toScheme,
            e.hom ≫ V.ι ≫ Y.structureMap = U.ι ≫ X.structureMap,
      ∃ (U : X.toScheme.Opens), (U : Set X.toScheme).Nonempty ∧
        ∃ f : U.toScheme ⟶ Y.toScheme,
          IsBirational f ∧ f ≫ Y.structureMap = U.ι ≫ X.structureMap]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.4, Tag 0BXM](https://stacks.math.columbia.edu/tag/0BXM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
