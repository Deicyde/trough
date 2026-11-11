---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsEnvelope, AlgebraicGeometry.isEnvelope_comp, AlgebraicGeometry.isEnvelope_isStableUnderBaseChange, Stacks.Chow.envelope_chow_comp_eq_zero, Stacks.Chow.envelope_chow_exact, Stacks.Chow.envelope_chow_exactSequence
statement: formalized
proof: formalized
---

# 42.22 Chow groups and envelopes

Section 42.22 of the Stacks Project, [Tag 0GU4](https://stacks.math.columbia.edu/tag/0GU4). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GU5, a definition

[Tag 0GU5](https://stacks.math.columbia.edu/tag/0GU5) in the Stacks Project.

**`AlgebraicGeometry.IsEnvelope`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChowGroupsEnvelopes/Basic.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChowGroupsEnvelopes/Basic.lean#L43).

> An **envelope** is a proper, completely decomposed morphism of schemes.

```lean
abbrev IsEnvelope {X Y : Scheme.{u}} (f : Y ⟶ X) : Prop
```

## Tag 0GU6, a lemma

[Tag 0GU6](https://stacks.math.columbia.edu/tag/0GU6) in the Stacks Project.

**`AlgebraicGeometry.isEnvelope_comp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChowGroupsEnvelopes/Stability.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChowGroupsEnvelopes/Stability.lean#L34).

> The composite of two envelopes of schemes is an envelope.

```lean
lemma isEnvelope_comp {X Y Z : Scheme.{u}} (f : Y ⟶ X) (g : Z ⟶ Y)
    (hf : IsEnvelope f) (hg : IsEnvelope g) : IsEnvelope (g ≫ f)
```

## Tag 0GU7, a lemma

[Tag 0GU7](https://stacks.math.columbia.edu/tag/0GU7) in the Stacks Project.

**`AlgebraicGeometry.isEnvelope_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChowGroupsEnvelopes/Stability.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChowGroupsEnvelopes/Stability.lean#L51).

> Envelopes of schemes are stable under arbitrary base change.

```lean
instance isEnvelope_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (fun {X Y : Scheme.{u}} (f : X ⟶ Y) ↦ IsEnvelope f)
```

## Tag 0GU8, a lemma

[Tag 0GU8](https://stacks.math.columbia.edu/tag/0GU8) in the Stacks Project.

**`Stacks.Chow.envelope_chow_comp_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChowGroupsEnvelopes/ExactSequence.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChowGroupsEnvelopes/ExactSequence.lean#L254). The attribute's comment: “the composite of the two maps is zero”.

> Pushing a class on `Y ×_X Y` forward along the two projections, taking the difference and
> pushing forward along `f` gives zero.

```lean
theorem envelope_chow_comp_eq_zero (γ : chowGroup C (pullback.fst f f ≫ f ≫ sX) k) :
    properChowPushforward C (f ≫ sX) sX f rfl k
        (properPushforwardFactorsThroughRationalEquivalence C (f ≫ sX) sX f rfl k)
        (properChowPushforward C (pullback.fst f f ≫ f ≫ sX) (f ≫ sX) (pullback.fst f f) rfl k
            (properPushforwardFactorsThroughRationalEquivalence C
              (pullback.fst f f ≫ f ≫ sX) (f ≫ sX) (pullback.fst f f) rfl k) γ -
          properChowPushforward C (pullback.fst f f ≫ f ≫ sX) (f ≫ sX) (pullback.snd f f)
            (pullback_snd_comp_eq_pullback_fst_comp f sX) k
            (properPushforwardFactorsThroughRationalEquivalence C
              (pullback.fst f f ≫ f ≫ sX) (f ≫ sX) (pullback.snd f f)
              (pullback_snd_comp_eq_pullback_fst_comp f sX) k) γ) = 0
```

**`Stacks.Chow.envelope_chow_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChowGroupsEnvelopes/ExactSequence.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChowGroupsEnvelopes/ExactSequence.lean#L273). The attribute's comment: “exactness at the middle term”.

> For an envelope `f : Y ⟶ X` a class in
> `A_k(Y)` pushes forward to zero in `A_k(X)` exactly when it is the difference of the pushforwards
> of a single class in `A_k(Y ×_X Y)` along the two projections.

```lean
theorem envelope_chow_exact (hcd : IsCompletelyDecomposed f) (β : chowGroup C (f ≫ sX) k) :
    properChowPushforward C (f ≫ sX) sX f rfl k
        (properPushforwardFactorsThroughRationalEquivalence C (f ≫ sX) sX f rfl k) β = 0 ↔
      ∃ γ : chowGroup C (pullback.fst f f ≫ f ≫ sX) k,
        β = properChowPushforward C (pullback.fst f f ≫ f ≫ sX) (f ≫ sX) (pullback.fst f f) rfl k
              (properPushforwardFactorsThroughRationalEquivalence C
                (pullback.fst f f ≫ f ≫ sX) (f ≫ sX) (pullback.fst f f) rfl k) γ -
            properChowPushforward C (pullback.fst f f ≫ f ≫ sX) (f ≫ sX) (pullback.snd f f)
              (pullback_snd_comp_eq_pullback_fst_comp f sX) k
              (properPushforwardFactorsThroughRationalEquivalence C
                (pullback.fst f f ≫ f ≫ sX) (f ≫ sX) (pullback.snd f f)
                (pullback_snd_comp_eq_pullback_fst_comp f sX) k) γ
```

**`Stacks.Chow.envelope_chow_exactSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChowGroupsEnvelopes/ExactSequence.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChowGroupsEnvelopes/ExactSequence.lean#L314). The attribute's comment: “the exact sequence of Chow groups of an envelope”.

> For an envelope `f : Y ⟶ X` with the two projections `p, q : Y ×_X Y ⟶ Y` of its fibre
> square, the sequence
>
>   `A_k(Y ×_X Y) --(p_* - q_*)--> A_k(Y) --f_*--> A_k(X) ⟶ 0`
>
> is exact for every `k ∈ ℤ`: the composite of the two maps is zero, a class killed by `f_*` is a
> difference `p_* γ - q_* γ`, and `f_*` is surjective.

```lean
theorem envelope_chow_exactSequence (hcd : IsCompletelyDecomposed f) :
    (∀ γ : chowGroup C (pullback.fst f f ≫ f ≫ sX) k,
        properChowPushforward C (f ≫ sX) sX f rfl k
          (properPushforwardFactorsThroughRationalEquivalence C (f ≫ sX) sX f rfl k)
          (properChowPushforward C (pullback.fst f f ≫ f ≫ sX) (f ≫ sX) (pullback.fst f f) rfl k
              (properPushforwardFactorsThroughRationalEquivalence C
                (pullback.fst f f ≫ f ≫ sX) (f ≫ sX) (pullback.fst f f) rfl k) γ -
            properChowPushforward C (pullback.fst f f ≫ f ≫ sX) (f ≫ sX) (pullback.snd f f)
              (pullback_snd_comp_eq_pullback_fst_comp f sX) k
              (properPushforwardFactorsThroughRationalEquivalence C
                (pullback.fst f f ≫ f ≫ sX) (f ≫ sX) (pullback.snd f f)
                (pullback_snd_comp_eq_pullback_fst_comp f sX) k) γ) = 0) ∧
      (∀ β : chowGroup C (f ≫ sX) k,
        properChowPushforward C (f ≫ sX) sX f rfl k
            (properPushforwardFactorsThroughRationalEquivalence C (f ≫ sX) sX f rfl k) β = 0 ↔
          ∃ γ : chowGroup C (pullback.fst f f ≫ f ≫ sX) k,
            β = properChowPushforward C (pullback.fst f f ≫ f ≫ sX) (f ≫ sX)
                  (pullback.fst f f) rfl k
                  (properPushforwardFactorsThroughRationalEquivalence C
                    (pullback.fst f f ≫ f ≫ sX) (f ≫ sX) (pullback.fst f f) rfl k) γ -
                properChowPushforward C (pullback.fst f f ≫ f ≫ sX) (f ≫ sX)
                  (pullback.snd f f) (pullback_snd_comp_eq_pullback_fst_comp f sX) k
                  (properPushforwardFactorsThroughRationalEquivalence C
                    (pullback.fst f f ≫ f ≫ sX) (f ≫ sX) (pullback.snd f f)
                    (pullback_snd_comp_eq_pullback_fst_comp f sX) k) γ) ∧
      Function.Surjective (properChowPushforward C (f ≫ sX) sX f rfl k
        (properPushforwardFactorsThroughRationalEquivalence C (f ≫ sX) sX f rfl k))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.22, Tag 0GU4](https://stacks.math.columbia.edu/tag/0GU4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
