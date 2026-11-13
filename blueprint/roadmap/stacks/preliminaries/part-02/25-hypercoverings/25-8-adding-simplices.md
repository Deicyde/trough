---
declaration: section
origin: cited
lean: Stacks.CategoryTheory.Hypercovering.isCoveringOver_homFromSSetMap_app_zero_of_oneMoreSimplex, Stacks.CategoryTheory.Hypercovering.isCoveringOver_homFromSSetRestriction_app_zero, Stacks.CategoryTheory.Hypercovering.isCoveringOver_delta, Stacks.CategoryTheory.Hypercovering.isCoveringOver_terminalFrom, CategoryTheory.MorphismProperty.IsHypercovering, CategoryTheory.MorphismProperty.IsHypercovering.face_mem, CategoryTheory.MorphismProperty.IsHypercovering.hom_app
statement: formalized
proof: formalized
---

# 25.8 Adding simplices

Section 25.8 of the Stacks Project, [Tag 01GL](https://stacks.math.columbia.edu/tag/01GL). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01GM, a lemma

[Tag 01GM](https://stacks.math.columbia.edu/tag/01GM) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.isCoveringOver_homFromSSetMap_app_zero_of_oneMoreSimplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CoveringPermanence.lean, line 845](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CoveringPermanence.lean#L845).

> **Stacks Project, Tag 01GM.** Let `K` be a hypercovering of `X`. If the finite simplicial
> set `V` is obtained from a subcomplex `U` by adjoining a single `n`-simplex `x`, with every
> simplex of `V` outside `U` in degree above `n` degenerate, then the restriction morphism
> `Hom(V, K)₀ ⟶ Hom(U, K)₀` is a covering in `SR(C, X)`.

```lean
theorem isCoveringOver_homFromSSetMap_app_zero_of_oneMoreSimplex (J : Pretopology C)
    [Precoverage.IsStableUnderComposition J.toPrecoverage] {X : C}
    (K : SimplicialObject (FormalCoproduct.{w} (Over X)))
    (hK : IsHypercovering J K)
    (V : SSet.{max w v}) (U : V.Subcomplex)
    [SSet.Finite (U : SSet.{max w v})]
    (_hUnonempty : ∀ m : ℕ, Nonempty (U.obj (op ⦋m⦌)))
    (_hVfinite : ∀ m : ℕ, Finite (V.obj (op ⦋m⦌)))
    (_hVnonempty : ∀ m : ℕ, Nonempty (V.obj (op ⦋m⦌)))
    (n : ℕ) (x : V.obj (op ⦋n⦌))
    (hx : x ∉ Set.range (U.ι.app (op ⦋n⦌)))
    (hbelow : ∀ m < n, Function.Bijective (U.ι.app (op ⦋m⦌)))
    (hat : ∀ y : V.obj (op ⦋n⦌), y ∈ Set.range (U.ι.app (op ⦋n⦌)) ∨ y = x)
    (habove : ∀ m, n < m → ∀ y : V.obj (op ⦋m⦌),
      y ∉ Set.range (U.ι.app (op ⦋m⦌)) → y ∈ V.degenerate m)
    (HV HU : SimplicialObject (FormalCoproduct.{w} (Over X)))
    (hV : SimplicialObject.IsHomFromSSet V K HV)
    (hU : SimplicialObject.IsHomFromSSet U K HU) :
    IsCoveringOver J ((homFromSSetMap hV hU U.ι).app (op ⦋0⦌))
```

## Tag 01GN, a lemma

[Tag 01GN](https://stacks.math.columbia.edu/tag/01GN) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.isCoveringOver_homFromSSetRestriction_app_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CoveringPermanence.lean, line 1282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CoveringPermanence.lean#L1282).

> **Stacks Project, Tag 01GN.** Let `K` be a hypercovering of `X` and let `U ⊆ V` be finite
> nonempty simplicial sets. Then restriction `Hom(V, K)₀ ⟶ Hom(U, K)₀` is a covering morphism in
> `SR(C, X)`.

```lean
theorem isCoveringOver_homFromSSetRestriction_app_zero (J : Pretopology C)
    [Precoverage.IsStableUnderComposition J.toPrecoverage] (X : C)
    (K : SimplicialObject (FormalCoproduct.{w} (Over X))) (hK : IsHypercovering J K)
    (V : SSet.{max w v}) [V.Finite] [V.Nonempty]
    (U : V.Subcomplex) [SSet.Finite (U : SSet)] [SSet.Nonempty (U : SSet)] :
    IsCoveringOver J ((homFromSSetRestriction U.ι K).app (op ⦋0⦌))
```

## Tag 0DEQ, a lemma

[Tag 0DEQ](https://stacks.math.columbia.edu/tag/0DEQ) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.isCoveringOver_delta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/HypercoverDescent.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/HypercoverDescent.lean#L186). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 0DEQ, part (2).** Every face map of a hypercovering of `X` is a
> covering morphism in `SR(C, X)`.

```lean
theorem isCoveringOver_delta (hK : IsHypercovering J K) (n : ℕ) (i : Fin (n + 2)) :
    IsCoveringOver J (K.δ i)
```

**`Stacks.CategoryTheory.Hypercovering.isCoveringOver_terminalFrom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/HypercoverDescent.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/HypercoverDescent.lean#L236). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 0DEQ, part (1).** Every level of a hypercovering of `X` is a
> covering of `X`.

```lean
theorem isCoveringOver_terminalFrom (hK : IsHypercovering J K) (n : ℕ) :
    IsCoveringOver J (terminal.from (K.obj (op ⦋n⦌)))
```

## Tag 0DER, a remark

[Tag 0DER](https://stacks.math.columbia.edu/tag/0DER) in the Stacks Project.

**`CategoryTheory.MorphismProperty.IsHypercovering`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/MorphismProperty.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/MorphismProperty.lean#L140). The attribute's comment: “p\_hypercovering”.

> **Stacks Project, Tag 0DER.** An augmented simplicial object is a `P`-hypercovering when its
> degree-zero augmentation, its canonical degree-one morphism to `U₀ ×_X U₀`, and all of its higher
> matching morphisms belong to `P`.

```lean
structure MorphismProperty.IsHypercovering {C : Type u} [Category.{v} C] [HasPullbacks C]
    (P : MorphismProperty C) (A : SimplicialObject.Augmented C) : Prop
```

**`CategoryTheory.MorphismProperty.IsHypercovering.face_mem`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/MorphismPropertyCovering.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/MorphismPropertyCovering.lean#L104). The attribute's comment: “faces\_in\_p”.

> Every face map in positive degree of a `P`-hypercovering belongs to `P`.

```lean
lemma face_mem (P : MorphismProperty C) [P.IsStableUnderBaseChange] [P.IsMultiplicative]
    {A : SimplicialObject.Augmented C}
    (hA : MorphismProperty.IsHypercovering P A) (n : ℕ) (i : Fin (n + 2)) :
    P (A.left.δ i)
```

**`CategoryTheory.MorphismProperty.IsHypercovering.hom_app`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/MorphismPropertyCovering.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/MorphismPropertyCovering.lean#L124). The attribute's comment: “levels\_in\_p”.

> Every level of a `P`-hypercovering maps to its augmentation point by a morphism in `P`.
>
> This is the `levels_in_p` assertion of **Stacks Project, Tag 0DER**.

```lean
lemma hom_app [P.IsMultiplicative] [P.IsStableUnderBaseChange]
    (hA : MorphismProperty.IsHypercovering P A) (n : ℕ) :
    P (A.hom.app (Opposite.op (SimplexCategory.mk n)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 25.8, Tag 01GL](https://stacks.math.columbia.edu/tag/01GL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
