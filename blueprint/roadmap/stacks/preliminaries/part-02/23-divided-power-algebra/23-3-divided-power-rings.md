---
declaration: section
origin: cited
lean: DividedPowerRing, DividedPowers.DPMorphism, DividedPowerRing.hasLimits, DividedPowerRing.forgetPreservesLimits, DividedPowerRing.isCorepresentable_of_cardinal_solutionSet, DividedPowerRing.instHasColimits, DividedPowerRing.tensorProductQuotientEquivPushoutQuotient, DividedPowerRing.tensorProductToPushout_surjective
statement: formalized
proof: formalized
---

# 23.3 Divided power rings

Section 23.3 of the Stacks Project, [Tag 07GT](https://stacks.math.columbia.edu/tag/07GT). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07GU, a definition

[Tag 07GU](https://stacks.math.columbia.edu/tag/07GU) in the Stacks Project.

**`DividedPowerRing`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Ring/Basic.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Ring/Basic.lean#L61). The attribute's comment: “divided power rings”.

> A divided power ring is a commutative ring equipped with an ideal and a divided power
> structure on that ideal.

```lean
public structure DividedPowerRing
```

Declarations registered for the tag:

- [`DividedPowers.DPMorphism`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DividedPowers.DPMorphism#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/DividedPowers/Ring/Basic.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Ring/Basic.lean#L75) (StacksFrontier): “homomorphisms of divided power rings”.

## Tag 07GV, a lemma

[Tag 07GV](https://stacks.math.columbia.edu/tag/07GV) in the Stacks Project.

**`DividedPowerRing.hasLimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Ring/Basic.lean, line 365](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Ring/Basic.lean#L365). The attribute's comment: “existence of limits”.

> The category of divided power rings has all small limits.

```lean
public instance hasLimits : HasLimits DividedPowerRing.{u}
```

**`DividedPowerRing.forgetPreservesLimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Ring/Basic.lean, line 371](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Ring/Basic.lean#L371). The attribute's comment: “agreement with limits of rings”.

> Limits of divided power rings are computed on their underlying commutative rings.

```lean
public noncomputable instance forgetPreservesLimits :
    PreservesLimits DividedPowerRing.forget.{u}
```

## Tag 07GW, a lemma

[Tag 07GW](https://stacks.math.columbia.edu/tag/07GW) in the Stacks Project.

**`DividedPowerRing.isCorepresentable_of_cardinal_solutionSet`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Ring/Basic.lean, line 433](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Ring/Basic.lean#L433).

> A limit-preserving functor on divided power rings is corepresentable when every one of its
> elements is obtained from an element over a divided power ring whose underlying type has
> uniformly bounded cardinality.

```lean
public theorem isCorepresentable_of_cardinal_solutionSet
    (F : DividedPowerRing.{u} ⥤ Type u)
    [PreservesLimitsOfSize.{u, u} F]
    (hF : ∃ κ : Cardinal.{u}, ∀ (A : DividedPowerRing.{u}) (f : F.obj A),
      ∃ (A' : DividedPowerRing.{u}) (f' : F.obj A') (g : A' ⟶ A),
        F.map g f' = f ∧ Cardinal.mk A' ≤ κ) :
    F.IsCorepresentable
```

## Tag 07GX, a lemma

[Tag 07GX](https://stacks.math.columbia.edu/tag/07GX) in the Stacks Project.

**`DividedPowerRing.instHasColimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Ring/Colimits.lean, line 513](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Ring/Colimits.lean#L513).

> The category of divided power rings has all colimits.

```lean
public instance instHasColimits : HasColimits (DividedPowerRing.{u})
```

## Tag 0H86, a remark

[Tag 0H86](https://stacks.math.columbia.edu/tag/0H86) in the Stacks Project.

**`DividedPowerRing.tensorProductQuotientEquivPushoutQuotient`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Ring/PushoutQuotient.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Ring/PushoutQuotient.lean#L154). The attribute's comment: “quotient\_of\_pushout”.

> For a pushout of divided power rings, the tensor product of the quotients of the two
> factors over the quotient of the base is canonically isomorphic to the quotient of the
> pushout.

```lean
public noncomputable def tensorProductQuotientEquivPushoutQuotient
    {A B B' B'' : DividedPowerRing.{u}} (f : A ⟶ B) (f' : A ⟶ B')
    (g : B ⟶ B'') (g' : B' ⟶ B'') (h : IsPushout f f' g g') :
    letI : Algebra (A ⧸ A.ideal) (B ⧸ B.ideal) := (quotientRingHom f).toAlgebra
    letI : Algebra (A ⧸ A.ideal) (B' ⧸ B'.ideal) := (quotientRingHom f').toAlgebra
    {e : (B ⧸ B.ideal) ⊗[A ⧸ A.ideal] (B' ⧸ B'.ideal) ≃+* (B'' ⧸ B''.ideal) //
      ∀ (b : B) (b' : B'),
        e (Ideal.Quotient.mk B.ideal b ⊗ₜ[A ⧸ A.ideal] Ideal.Quotient.mk B'.ideal b') =
          Ideal.Quotient.mk B''.ideal (g b * g' b')}
```

**`DividedPowerRing.tensorProductToPushout_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Ring/PushoutTensor.lean, line 436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Ring/PushoutTensor.lean#L436). The attribute's comment: “tensor\_map\_surjective”.

> In a pushout of divided power rings, the canonical map from the tensor product of the
> underlying rings to the underlying ring of the pushout is surjective.

```lean
public theorem tensorProductToPushout_surjective
    {A B B' B'' : DividedPowerRing.{u}} (f : A ⟶ B) (f' : A ⟶ B')
    (g : B ⟶ B'') (g' : B' ⟶ B'') (h : IsPushout f f' g g') :
    Function.Surjective (tensorProductToPushout f f' g g' h.w)
```

**`DividedPowerRing.dividedPowerIdeal_surjective_of_isPushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Ring/PushoutTensor.lean, line 490](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Ring/PushoutTensor.lean#L490). The attribute's comment: “ideal\_map\_surjective”.

> In a pushout of divided power rings, the canonical map from the sum of the two extended
> divided power ideals onto the distinguished ideal of the pushout is surjective.

```lean
public theorem dividedPowerIdeal_surjective_of_isPushout
    {A B B' B'' : DividedPowerRing.{u}}
    (f : A ⟶ B) (g : A ⟶ B') (h : B ⟶ B'') (h' : B' ⟶ B'')
    (H : IsPushout f g h h') :
    letI : Algebra A B := f.toRingHom.toAlgebra
    letI : Algebra A B' := g.toRingHom.toAlgebra
    ∀ y : B''.ideal,
      ∃ x : (Ideal.map Algebra.TensorProduct.includeLeftRingHom B.ideal +
          Ideal.map Algebra.TensorProduct.includeRight.toRingHom B'.ideal :
            Ideal (B ⊗[A] B')),
        canonicalTensorProductHom f g h h' H.w x.1 = y.1
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 23.3, Tag 07GT](https://stacks.math.columbia.edu/tag/07GT)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
