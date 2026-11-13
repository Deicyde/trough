---
declaration: section
origin: cited
lean: Crystalline.homotopic_tensor_id, Crystalline.homotopic_exteriorPower_map, Crystalline.homotopic_baseChange, Crystalline.homotopic_adicCompletionMap
statement: formalized
proof: formalized
---

# 60.16 Cosimplicial algebra

Section 60.16 of the Stacks Project, [Tag 07KP](https://stacks.math.columbia.edu/tag/07KP). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07KQ, a lemma

[Tag 07KQ](https://stacks.math.columbia.edu/tag/07KQ) in the Stacks Project.

**`Crystalline.homotopic_tensor_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Cosimplicial.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/Cosimplicial.lean#L155). The attribute's comment: “tensor”.

> **Stacks Lemma 07KQ (tensor).** Tensoring homotopic morphisms of cosimplicial modules
> with the identity morphism of another cosimplicial module preserves homotopy.

```lean
public theorem homotopic_tensor_id {φ ψ : K ⟶ M} (h : Homotopic φ ψ)
    (L : CosimplicialModule A) :
    Homotopic (φ ⊗ₘ 𝟙 L) (ψ ⊗ₘ 𝟙 L)
```

**`Crystalline.homotopic_exteriorPower_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Cosimplicial.lean, line 406](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/Cosimplicial.lean#L406). The attribute's comment: “exterior\_power”.

> **Stacks 07KQ, exterior power.** Homotopic homomorphisms of cosimplicial
> modules induce homotopic homomorphisms on every exterior power.

```lean
public theorem homotopic_exteriorPower_map
    {A : CosimplicialObject CommRingCat.{u}}
    {K M : CosimplicialModule A} {φ ψ : K ⟶ M} (i : ℕ)
    (h : Homotopic φ ψ) :
    Homotopic ((exteriorPowerFunctor A i).functor.map φ)
      ((exteriorPowerFunctor A i).functor.map ψ)
```

**`Crystalline.homotopic_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Cosimplicial.lean, line 746](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/Cosimplicial.lean#L746). The attribute's comment: “base change”.

> **Stacks 07KQ, base change.** If two homomorphisms of cosimplicial `A`-modules are
> homotopic and `f : A ⟶ B` is a homomorphism of cosimplicial rings, then the induced
> homomorphisms of cosimplicial `B`-modules between the base changes are homotopic.  The
> homotopy is `h ⊗ 1`, and in particular each of its components is `B_n`-linear, because
> `Homotopy` for cosimplicial `B`-modules demands exactly that.

```lean
public theorem homotopic_baseChange (f : A ⟶ B) {K M : CosimplicialModule A} {φ ψ : K ⟶ M}
    (h : Homotopic φ ψ) :
    Homotopic ((baseChange f).map φ) ((baseChange f).map ψ)
```

**`Crystalline.homotopic_adicCompletionMap`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Cosimplicial.lean, line 1122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/Cosimplicial.lean#L1122). The attribute's comment: “completion”.

> **Stacks 07KQ, completion.** Homotopic homomorphisms of modules over a cosimplicial ring
> induce homotopic homomorphisms on their completions with respect to a cosimplicial ideal.

```lean
public lemma homotopic_adicCompletionMap
    {A : CosimplicialObject CommRingCat.{u}} (I : CosimplicialIdeal A)
    {K M : SemilinearCosimplicialModule.{u, v} A} (φ ψ : SemilinearCosimplicialModule.Hom K M)
    (h : Relation.EqvGen (fun a b => Nonempty (SemilinearCosimplicialModule.Homotopy a b)) φ ψ)
    (Khat : SemilinearCosimplicialModule.Completion I K)
    (Mhat : SemilinearCosimplicialModule.Completion I M)
    (φhat ψhat : SemilinearCosimplicialModule.Completion.Hom Khat Mhat)
    (hφ : ∀ n x, Mhat.iso n (φhat.hom.app n x) =
      AdicCompletion.map (I.obj n) (φ.app n) (Khat.iso n x))
    (hψ : ∀ n x, Mhat.iso n (ψhat.hom.app n x) =
      AdicCompletion.map (I.obj n) (ψ.app n) (Khat.iso n x)) :
    Relation.EqvGen (fun a b =>
      Nonempty (SemilinearCosimplicialModule.Completion.Homotopy a b)) φhat ψhat
```

## Tag 07KT, an item

[Tag 07KT](https://stacks.math.columbia.edu/tag/07KT) in the Stacks Project.

**`Crystalline.homotopic_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Cosimplicial.lean, line 746](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/Cosimplicial.lean#L746). The attribute's comment: “homotopy is preserved by base change along a homomorphism of cosimplicial rings”.

> **Stacks 07KQ, base change.** If two homomorphisms of cosimplicial `A`-modules are
> homotopic and `f : A ⟶ B` is a homomorphism of cosimplicial rings, then the induced
> homomorphisms of cosimplicial `B`-modules between the base changes are homotopic.  The
> homotopy is `h ⊗ 1`, and in particular each of its components is `B_n`-linear, because
> `Homotopy` for cosimplicial `B`-modules demands exactly that.

```lean
public theorem homotopic_baseChange (f : A ⟶ B) {K M : CosimplicialModule A} {φ ψ : K ⟶ M}
    (h : Homotopic φ ψ) :
    Homotopic ((baseChange f).map φ) ((baseChange f).map ψ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.16, Tag 07KP](https://stacks.math.columbia.edu/tag/07KP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
