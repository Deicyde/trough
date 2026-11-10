---
declaration: section
origin: cited
lean: AlgebraicGeometry.varietyEquivalenceFinitelyGeneratedFieldExtensionOpposite, AlgebraicGeometry.birationalOver_tfae_functionField
statement: formalized
proof: formalized
---

# 33.4 Varieties and rational maps

Section 33.4 of the Stacks Project, [Tag 0BXM](https://stacks.math.columbia.edu/tag/0BXM). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BXN, a theorem

[Tag 0BXN](https://stacks.math.columbia.edu/tag/0BXN) in the Stacks Project.

**`AlgebraicGeometry.varietyEquivalenceFinitelyGeneratedFieldExtensionOpposite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Varieties/FunctionFieldEquivalence/Equivalence.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Varieties/FunctionFieldEquivalence/Equivalence.lean#L85).

> **Stacks Project, Tag 0BXN.** Varieties and dominant rational maps over a field are
> contravariantly equivalent to finitely generated field extensions of that field.

```lean
noncomputable def varietyEquivalenceFinitelyGeneratedFieldExtensionOpposite
    (k : Type u) [Field k] :
    Variety k ≌ (FinitelyGeneratedFieldExtension k)ᵒᵖ
```

## Tag 0BXP, a lemma

[Tag 0BXP](https://stacks.math.columbia.edu/tag/0BXP) in the Stacks Project.

**`AlgebraicGeometry.birationalOver_tfae_functionField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/RationalMap/FunctionField.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/RationalMap/FunctionField.lean#L254).

> **Stacks Project, Tag 0BXP.** The four characterizations of birationality for varieties over
> a field: birationality over `k`, isomorphy of the function fields as extensions of `k`, isomorphy
> of nonempty open subvarieties, and the existence of a birational morphism from an open
> subvariety.

```lean
public theorem birationalOver_tfae_functionField
    (k : Type u) [Field k] {X Y : Scheme.{u}}
    (sX : X ⟶ Spec (.of k)) (sY : Y ⟶ Spec (.of k))
    [IsVariety k sX] [IsVariety k sY] :
    letI : Algebra k (Stacks.Chow.rationalFunctions X) :=
      ((Stacks.Chow.ofSectionRingHom X ⟨⊤, dense_univ⟩).comp
        ((Scheme.ΓSpecIso (.of k)).inv ≫ sX.appTop).hom).toAlgebra
    letI : Algebra k (Stacks.Chow.rationalFunctions Y) :=
      ((Stacks.Chow.ofSectionRingHom Y ⟨⊤, dense_univ⟩).comp
        ((Scheme.ΓSpecIso (.of k)).inv ≫ sY.appTop).hom).toAlgebra
    List.TFAE [
      Scheme.BirationalOver sX sY,
      Nonempty (Stacks.Chow.rationalFunctions X ≃ₐ[k]
        Stacks.Chow.rationalFunctions Y),
      ∃ (U : X.Opens) (V : Y.Opens),
        (U : Set X).Nonempty ∧ (V : Set Y).Nonempty ∧
          ∃ e : U.toScheme ≅ V.toScheme,
            e.hom ≫ V.ι ≫ sY = U.ι ≫ sX,
      ∃ (U : X.Opens), (U : Set X).Nonempty ∧
        ∃ f : U.toScheme ⟶ Y,
          IsBirational f ∧ f ≫ sY = U.ι ≫ sX]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.4, Tag 0BXM](https://stacks.math.columbia.edu/tag/0BXM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
