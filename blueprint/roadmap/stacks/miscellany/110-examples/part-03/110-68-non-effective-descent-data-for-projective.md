---
declaration: section
origin: cited
lean: Stacks.Examples.NonEffectiveProjectiveDescent.exists_etale_descentData_projective_not_isEffective
statement: formalized
proof: formalized
---

# 110.68 Non-effective descent data for projective schemes

Section 110.68 of the Stacks Project, [Tag 08KE](https://stacks.math.columbia.edu/tag/08KE). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08KF, a lemma

[Tag 08KF](https://stacks.math.columbia.edu/tag/08KF) in the Stacks Project.

**`Stacks.Examples.NonEffectiveProjectiveDescent.exists_etale_descentData_projective_not_isEffective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Examples/HironakaInvolution/NonEffectiveDescent.lean, line 922](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Examples/HironakaInvolution/NonEffectiveDescent.lean#L922). The attribute's comment: “The source's construction over ℚ: the involution [x:y:z:w] ↦ [y:x:w:z] of ℙ³ acts freely on Y = ℙ³ minus two lines, Y → S = Y/G is an étale double cover, Hironaka's threefold over ℙ³ carries the lifted involution, and its restriction gives the descent datum. Two choices differ from the text: the étale covering is the single open Y − \{Q} → S (a member of the source's covering (Y − P) ⊔ (Y − Q), already surjective onto S), and non-effectivity is derived from χ(H|L₀) + χ(H|g(L₀)) = 2 for invertible H (the Euler-characteristic form of L₀ + g(L₀) ∼ 0) applied to the divisor of a function on the would-be quotient, instead of degrees of 1-cycles”.

> **There is a non-effective projective descent datum along an étale covering.** There are an
> étale covering of a scheme consisting of a single morphism `f : X ⟶ S` and a descent datum
> relative to `f` whose scheme over `X` is projective over `X` and which is not effective in the
> category of schemes. This is [Stacks, Tag 08KF] with no hypothesis; the witness is built over
> `ULift ℚ` by
> `HironakaInvolution.exists_etale_descentData_projective_not_isEffective_of_two_ne_zero`.

```lean
theorem exists_etale_descentData_projective_not_isEffective :
    ∃ (S X : Scheme.{u}) (f : X ⟶ S)
      (D : DescentData (S := S) (X := fun _ : Unit ↦ X) (fun _ ↦ f)),
      Presieve.singleton f ∈ Scheme.etalePrecoverage S ∧
        IsProjective (D.obj ()).hom ∧ ¬ D.IsEffective
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.68, Tag 08KE](https://stacks.math.columbia.edu/tag/08KE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
