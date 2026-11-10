---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.tfae_isQuasiCompactSpace_unconditional, AlgebraicGeometry.FormalSpace.IsQuasiCompactSpace.hasFiniteFormalAtlas', AlgebraicGeometry.FormalSpace.HasFiniteFormalAtlas.isQuasiCompactSpace', AlgebraicGeometry.FormalSpace.IsQuasiCompactSpace.hasFiniteFormalAtlas, AlgebraicGeometry.FormalSpace.IsQuasiCompactSpace.isQuasiCompactSpaceULift_reduction, AlgebraicGeometry.FormalSpace.tfae_isQuasiCompactSpace, AlgebraicGeometry.FormalSpace.IsQuasiCompactSpace.isQuasiCompactSpaceULift_of_isReduction, AlgebraicGeometry.FormalSpace.hasFiniteFormalAtlas_of_isQuasiCompactSpaceULift_reduction
statement: formalized
proof: formalized
---

# 87.17 Quasi-compact formal algebraic spaces

Section 87.17 of the Stacks Project, [Tag 0AJ8](https://stacks.math.columbia.edu/tag/0AJ8). 5 tags here are carried by 27 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AJ9, a lemma

[Tag 0AJ9](https://stacks.math.columbia.edu/tag/0AJ9) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.tfae_isQuasiCompactSpace_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CoproductRepresentableEtaleConsequences.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CoproductRepresentableEtaleConsequences.lean#L80). The attribute's comment: “the equivalence of the three conditions, for every reduction i : Xred ⟶ X of X, a reduction existing by Stacks 0AIN (exists_isReduction_of_isFormalAlgebraicSpace); nothing is assumed beyond the source's hypotheses, the input hCoproductEtale of AlgebraicGeometry.FormalSpace.tfae_isQuasiCompactSpace_of_isReduction being the theorem AlgebraicGeometry.FormalSpace.coproductsRepresentableEtale”.

> Let `X` be a formal algebraic space over `S` and let `i : Xred ⟶ X` be a reduction of `X`.
> Then quasi-compactness of `Xred`, the existence of an atlas as in Definition 0AIM indexed by a
> finite type, and the existence of a morphism from an affine formal algebraic space which is
> representable by algebraic spaces, étale and a surjection of sheaves are equivalent.
>
> A reduction of `X` exists by
> `AlgebraicGeometry.FormalSpace.exists_isReduction_of_isFormalAlgebraicSpace`.

```lean
theorem tfae_isQuasiCompactSpace_unconditional
    {X Xred : FppfSheaf B S hS} {i : Xred ⟶ X}
    (hX : IsFormalAlgebraicSpace B S hS X) (hi : IsReduction B S hS X Xred i) :
    [Space.IsQuasiCompactSpaceULift.{u + 1} B S hS Xred.obj,
      HasFiniteFormalAtlas B S hS X,
      IsQuasiCompactSpace B S hS X].TFAE
```

**`AlgebraicGeometry.FormalSpace.IsQuasiCompactSpace.hasFiniteFormalAtlas'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteFormalAtlas.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteFormalAtlas.lean#L184). The attribute's comment: “the implication (3) ⇒ (2)”.

> **Stacks 0AJ9, the implication (3) ⇒ (2).** A quasi-compact formal algebraic space over
> `S` has a finite formal atlas: the one affine formal algebraic space surjecting onto it is an
> atlas as in Definition 0AIM indexed by a one-point type, the induced map from the coproduct
> over that type being the given map up to the coproduct inclusion, which is a split
> epimorphism.

```lean
theorem IsQuasiCompactSpace.hasFiniteFormalAtlas' {X : FppfSheaf B S hS}
    (h : IsQuasiCompactSpace B S hS X) : HasFiniteFormalAtlas' B S hS X
```

**`AlgebraicGeometry.FormalSpace.HasFiniteFormalAtlas.isQuasiCompactSpace'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteFormalAtlas.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteFormalAtlas.lean#L204). The attribute's comment: “the implication (2) ⇒ (3)”.

> **Stacks 0AJ9, the implication (2) ⇒ (3).** A sheaf with a finite formal atlas is a
> quasi-compact formal algebraic space over `S`: the coproduct of the finitely many members of
> the atlas is an affine formal algebraic space, and the induced morphism from it is
> representable by algebraic spaces, étale and a surjection of sheaves.

```lean
theorem HasFiniteFormalAtlas.isQuasiCompactSpace'
    {X : FppfSheaf B S hS} (h : HasFiniteFormalAtlas' B S hS X) :
    IsQuasiCompactSpace B S hS X
```

**`AlgebraicGeometry.FormalSpace.IsQuasiCompactSpace.hasFiniteFormalAtlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactSpaceCriteria.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactSpaceCriteria.lean#L221). The attribute's comment: “the implication (3) ⇒ (2)”.

> **Stacks 0AJ9, the implication (3) ⇒ (2).** A quasi-compact formal algebraic space over
> `S` has a finite formal atlas: the one affine formal algebraic space surjecting onto it is an
> atlas as in Definition 0AIM indexed by a one-point type, the induced map from the coproduct
> over that type being the given map up to the coproduct inclusion, which is a split
> epimorphism.

```lean
theorem IsQuasiCompactSpace.hasFiniteFormalAtlas {X : FppfSheaf B S hS}
    (h : IsQuasiCompactSpace B S hS X) : HasFiniteFormalAtlas B S hS X
```

**`AlgebraicGeometry.FormalSpace.IsQuasiCompactSpace.isQuasiCompactSpaceULift_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactSpaceCriteria.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactSpaceCriteria.lean#L262). The attribute's comment: “the implication (3) ⇒ (1), with a reduction of X supplied as a hypothesis in place of Stacks 0AIN, on the hypotheses hAffineReduction that a reduction of an affine formal algebraic space is quasi-compact and hReductionEtaleSurjective that the morphism of reductions induced by a representable, étale and surjective morphism is surjective and étale”.

> **Stacks 0AJ9, the implication (3) ⇒ (1).** Let `X` be a quasi-compact formal algebraic
> space over `S` and let `i : Xred ⟶ X` be a reduction of `X`. Then `Xred` is a quasi-compact
> algebraic space. Indeed, the affine formal algebraic space `Y` surjecting onto `X` has a
> reduction `iY : Yred ⟶ Y`, the composite `Yred ⟶ Y ⟶ X` factors through `i` because `Yred` is
> a reduced algebraic space, and the resulting morphism `Yred ⟶ Xred` is surjective and étale;
> composing a quasi-compact surjective étale chart of `Yred` with it gives one of `Xred`.

```lean
theorem IsQuasiCompactSpace.isQuasiCompactSpaceULift_reduction
    (hAffineReduction : AffineReductionsQuasiCompact B S hS)
    (hReductionEtaleSurjective : ReductionsOfEtaleSurjectionsEtaleSurjective B S hS)
    {X Xred : FppfSheaf B S hS} {i : Xred ⟶ X} (hi : IsReduction B S hS X Xred i)
    (h : IsQuasiCompactSpace B S hS X) :
    Space.IsQuasiCompactSpaceULift.{u + 1} B S hS Xred.obj
```

**`AlgebraicGeometry.FormalSpace.tfae_isQuasiCompactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactSpaceCriteria.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactSpaceCriteria.lean#L291). The attribute's comment: “the equivalence of the three conditions, with a reduction of X supplied as a hypothesis in place of Stacks 0AIN, and on the hypotheses hFiniteRefinement for the implication (1) ⇒ (2), hCoproductEtale for the implication (2) ⇒ (3), and hAffineReduction and hReductionEtaleSurjective for the implication (3) ⇒ (1)”.

> **Stacks 0AJ9.** Let `X` be a formal algebraic space over `S` and let `i : Xred ⟶ X` be a
> reduction of `X`. The following are equivalent:
>
> 1. `Xred` is a quasi-compact algebraic space,
> 2. `X` admits an atlas as in Definition 0AIM indexed by a finite type,
> 3. `X` receives a morphism from an affine formal algebraic space which is representable by
>    algebraic spaces, étale and a surjection of sheaves.

```lean
theorem tfae_isQuasiCompactSpace
    (hAffineReduction : AffineReductionsQuasiCompact B S hS)
    (hReductionEtaleSurjective : ReductionsOfEtaleSurjectionsEtaleSurjective B S hS)
    (hCoproductEtale : CoproductsRepresentableEtale B S hS)
    {X Xred : FppfSheaf B S hS} {i : Xred ⟶ X}
    (_hX : IsFormalAlgebraicSpace B S hS X) (hi : IsReduction B S hS X Xred i)
    (hFiniteRefinement : Space.IsQuasiCompactSpaceULift.{u + 1} B S hS Xred.obj →
      HasFiniteFormalAtlas B S hS X) :
    [Space.IsQuasiCompactSpaceULift.{u + 1} B S hS Xred.obj,
      HasFiniteFormalAtlas B S hS X,
      IsQuasiCompactSpace B S hS X].TFAE
```

**`AlgebraicGeometry.FormalSpace.IsQuasiCompactSpace.isQuasiCompactSpaceULift_of_isReduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactSpaceCriteriaReduction.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactSpaceCriteriaReduction.lean#L184). The attribute's comment: “the implication (3) ⇒ (1), for every reduction i : Xred ⟶ X of X, a reduction existing by Stacks 0AIN (exists_isReduction_of_isFormalAlgebraicSpace); nothing is assumed beyond the source's hypotheses”.

> **Stacks 0AJ9, the implication (3) ⇒ (1).** Let `X` be a quasi-compact formal algebraic
> space over `S` and let `i : Xred ⟶ X` be a reduction of `X`. Then `Xred` is a quasi-compact
> algebraic space.
>
> Let `c : Y ⟶ X` be the morphism of condition (3), with `Y` an affine formal algebraic space.
> The fibre product `P = Y ×_X Xred` is a reduction of `Y` by **Stacks 0GB7**, an étale morphism
> being smooth, so `P` is the sheaf of an affine object `T` of the site by the affine case of
> Stacks 0AIN. The second projection `P ⟶ Xred` is a base change of `c`, hence representable by
> algebraic spaces and étale, and it is surjective on points because `c` is; so `T ⟶ Xred` is a
> quasi-compact surjective étale chart of `Xred`.

```lean
theorem IsQuasiCompactSpace.isQuasiCompactSpaceULift_of_isReduction
    {X Xred : FppfSheaf B S hS} {i : Xred ⟶ X} (hi : IsReduction B S hS X Xred i)
    (h : IsQuasiCompactSpace B S hS X) :
    Space.IsQuasiCompactSpaceULift.{u + 1} B S hS Xred.obj
```

**`AlgebraicGeometry.FormalSpace.hasFiniteFormalAtlas_of_isQuasiCompactSpaceULift_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactSpaceCriteriaRefined.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactSpaceCriteriaRefined.lean#L155). The attribute's comment: “the implication (1) ⇒ (2), for an arbitrary reduction of X”.

> **Stacks 0AJ9, the implication (1) ⇒ (2).** Let `X` be a formal algebraic space over `S`,
> let `i : Xred ⟶ X` be a reduction of `X` and suppose that `Xred` is a quasi-compact algebraic
> space. Then `X` has a finite formal atlas: an atlas as in Definition 0AIM indexed by a finite
> type.

```lean
theorem hasFiniteFormalAtlas_of_isQuasiCompactSpaceULift_reduction
    {X Xred : FppfSheaf B S hS} {i : Xred ⟶ X}
    (hX : IsFormalAlgebraicSpace B S hS X) (hi : IsReduction B S hS X Xred i)
    (hQC : Space.IsQuasiCompactSpaceULift.{u + 1} B S hS Xred.obj) :
    HasFiniteFormalAtlas B S hS X
```

**`AlgebraicGeometry.FormalSpace.hasFiniteFormalAtlas_of_isQuasiCompactSpaceULift_of_isReduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactSpaceCriteriaSupplement.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactSpaceCriteriaSupplement.lean#L75). The attribute's comment: “the implication (1) ⇒ (2)”.

> Let `X` be a formal algebraic space over `S` and let `i : Xred ⟶ X` be a reduction of `X`
> whose source is a quasi-compact algebraic space. Then `X` has a finite formal atlas.
>
> Finitely many members of the atlas as in Definition 0AIM which `X` carries are already jointly
> surjective on points, by
> `AlgebraicGeometry.FormalSpace.exists_finite_jointly_surjective_of_isQuasiCompactSpaceULift`;
> what remains is that such a finite subfamily is itself an atlas as in Definition 0AIM, that is
> that its induced morphism out of the coproduct is a surjection of sheaves. That morphism is
> representable by algebraic spaces and étale by
> `AlgebraicGeometry.FormalSpace.coproductsRepresentableEtale'`, hence flat and locally of finite
> presentation; joint surjectivity on points is surjectivity on points of it, which for a morphism
> representable by algebraic spaces is surjectivity in the sense of Stacks 03XZ by
> `AlgebraicGeometry.FormalSpace.hasPropertyULift_isSurjectiveULift_iff`; and Stacks 05VM turns a
> representable surjective flat cover into a surjection of sheaves.

```lean
theorem hasFiniteFormalAtlas_of_isQuasiCompactSpaceULift_of_isReduction
    {X Xred : FppfSheaf B S hS} {i : Xred ⟶ X} (hX : IsFormalAlgebraicSpace B S hS X)
    (hi : IsReduction B S hS X Xred i)
    (h : Space.IsQuasiCompactSpaceULift.{u + 1} B S hS Xred.obj) :
    HasFiniteFormalAtlas' B S hS X
```

**`AlgebraicGeometry.FormalSpace.IsQuasiCompactSpace.isQuasiCompactSpaceULift_reduction_space`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactSpaceCriteriaSupplement.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactSpaceCriteriaSupplement.lean#L119). The attribute's comment: “the implication (3) ⇒ (1)”.

> The reduction `reduction` of a quasi-compact formal algebraic space over `S` is a
> quasi-compact algebraic space.
>
> This is `AlgebraicGeometry.FormalSpace.IsQuasiCompactSpace.isQuasiCompactSpaceULift_of_isReduction`
> read at the reduction `AlgebraicGeometry.FormalSpace.reduction` that Stacks 0AIN produces, the
> formal algebraic space being the source's own hypothesis on `X` and being implied by condition
> (3). Condition (1) of the source names the reduction of `X`, so the statement mentions it; any
> other reduction is canonically isomorphic to this one by
> `AlgebraicGeometry.FormalSpace.Reduction.iso`, and the general statement applies to it directly,
> so nothing depends on the choice.

```lean
theorem IsQuasiCompactSpace.isQuasiCompactSpaceULift_reduction_space {X : FppfSheaf B S hS}
    (h : IsQuasiCompactSpace B S hS X) :
    Space.IsQuasiCompactSpaceULift.{u + 1} B S hS
      (liftSheaf B S hS
        (reduction B S hS X (IsQuasiCompactSpace.isFormalAlgebraicSpace B S hS h)).space).obj
```

**`AlgebraicGeometry.FormalSpace.tfae_isQuasiCompactSpace_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactSpaceCriteriaSupplement.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactSpaceCriteriaSupplement.lean#L159). The attribute's comment: “the equivalence of the three conditions”.

> Let `X` be a formal algebraic space over `S`. The following are equivalent:
>
> 1. the reduction `reduction` of `X` is a quasi-compact algebraic space,
> 2. `X` admits an atlas as in Definition 0AIM indexed by a finite type,
> 3. `X` receives a morphism from an affine formal algebraic space which is representable by
>    algebraic spaces, étale and a surjection of sheaves.
>
> Condition (1) is read at the reduction `AlgebraicGeometry.FormalSpace.reduction` that
> Stacks 0AIN produces; by `AlgebraicGeometry.FormalSpace.Reduction.iso` any two reductions of
> `X` are canonically isomorphic, so the condition does not depend on the choice, and
> `AlgebraicGeometry.FormalSpace.tfae_isQuasiCompactSpace_of_isReduction_unconditional` is the same
> equivalence at an arbitrary reduction.

```lean
theorem tfae_isQuasiCompactSpace_of_isFormalAlgebraicSpace
    {X : FppfSheaf B S hS} (hX : IsFormalAlgebraicSpace B S hS X) :
    [Space.IsQuasiCompactSpaceULift.{u + 1} B S hS
        (liftSheaf B S hS (reduction B S hS X hX).space).obj,
      HasFiniteFormalAtlas' B S hS X,
      IsQuasiCompactSpace B S hS X].TFAE
```

## Tag 0AJA, a definition

[Tag 0AJA](https://stacks.math.columbia.edu/tag/0AJA) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.FormalSpace.IsQuasiCompactSpace`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphism.lean#L147), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactSpaceCriteria.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactSpaceCriteria.lean#L316) (StacksFrontier): “the definition, realized by condition (3) of Stacks 0AJ9, `AlgebraicGeometry.FormalSpace.IsQuasiCompactSpace`; the equivalence with conditions (1) and (2) that makes the choice of condition immaterial is `tfae_isQuasiCompactSpace`, which carries the two hypotheses standing for the steps of the omitted proof of Stacks 0AJ9”.
- [`AlgebraicGeometry.FormalSpace.IsQuasiCompactSpace`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphism.lean#L147), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactSpaceCriteriaSupplement.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactSpaceCriteriaSupplement.lean#L249) (StacksFrontier): “the definition, realized by condition (3) of Stacks 0AJ9, `AlgebraicGeometry.FormalSpace.IsQuasiCompactSpace`; the equivalence with conditions (1) and (2) that makes the choice of condition immaterial is `tfae_isQuasiCompactSpace`, which is unconditional”.

## Tag 0AJB, a lemma

[Tag 0AJB](https://stacks.math.columbia.edu/tag/0AJB) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsQuasiCompactOnSchemeBaseChanges.isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphism.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphism.lean#L228). The attribute's comment: “condition (2) implies condition (3); no other implication among the four conditions is proved here”.

> **Stacks 0AJB, condition (2) implies condition (3).** The fibre product condition over the
> quasi-compact schemes over `S` in the site restricts to the affine ones, an affine scheme
> being quasi-compact.

```lean
theorem IsQuasiCompactOnSchemeBaseChanges.isQuasiCompact {X Y : FppfSheaf B S hS} {f : X ⟶ Y}
    (h : IsQuasiCompactOnSchemeBaseChanges B S hS f) : IsQuasiCompact B S hS f
```

**`AlgebraicGeometry.FormalSpace.isQuasiCompactOnReductions_iff_isQuasiCompactULift_chosenReductionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismChosenReduction.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismChosenReduction.lean#L126). The attribute's comment: “condition (1), in the source's own form — quasi-compactness of the morphism f_red of the chosen reductions — identified with the phrasing of the condition that quantifies over the reductions”.

> **Stacks 0AJB, condition (1).** Let `f : X ⟶ Y` be a morphism of formal algebraic spaces over
> `S`. The morphism `f_red : X_red ⟶ Y_red` of the chosen reductions is a quasi-compact morphism of
> algebraic spaces if and only if every morphism between reductions of `X` and of `Y` compatible
> with `f` is one. The second condition is
> `AlgebraicGeometry.FormalSpace.IsQuasiCompactOnReductions`, the phrasing of condition (1) which
> quantifies over the reductions instead of choosing them.
>
> Given reductions `iX : Xred ⟶ X` and `iY : Yred ⟶ Y` and a compatible `fred`, the universal
> properties of the chosen reductions supply comparison morphisms `a : Xred ⟶ X_red` and
> `b : Yred ⟶ Y_red` over `X` and over `Y`, and these are isomorphisms because two reductions of
> one sheaf are isomorphic over it. The inclusion of the reduction of `Y` is a monomorphism, so
> `a ≫ f_red = fred ≫ b`, and `fred` is `f_red` conjugated by the two isomorphisms.

```lean
theorem isQuasiCompactOnReductions_iff_isQuasiCompactULift_chosenReductionMap
    {X Y : FppfSheaf B S hS} (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    IsQuasiCompactOnReductions B S hS f ↔
      Space.IsQuasiCompactULift.{u + 1} B S hS (chosenReductionMap B S hS hX hY f).hom
```

**`AlgebraicGeometry.FormalSpace.IsQuasiCompact.isQuasiCompactULift_chosenReductionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismChosenReduction.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismChosenReduction.lean#L169). The attribute's comment: “condition (3) implies condition (1), for the morphism f_red of the chosen reductions”.

> **Stacks 0AJB, condition (3) implies condition (1).** Let `f : X ⟶ Y` be a morphism of formal
> algebraic spaces over `S` such that every fibre product of `f` with an affine scheme over `S` in
> the site mapping to `Y` is a quasi-compact formal algebraic space — that is, let `f` be
> quasi-compact in the sense of Stacks 0AJC. Then the morphism `f_red : X_red ⟶ Y_red` of the
> chosen reductions is a quasi-compact morphism of algebraic spaces.

```lean
theorem IsQuasiCompact.isQuasiCompactULift_chosenReductionMap {X Y : FppfSheaf B S hS}
    (hX : IsFormalAlgebraicSpace B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (h : IsQuasiCompact B S hS f) :
    Space.IsQuasiCompactULift.{u + 1} B S hS (chosenReductionMap B S hS hX hY f).hom
```

**`AlgebraicGeometry.FormalSpace.IsQuasiCompactOnSchemeBaseChanges.isQuasiCompactULift_chosenReductionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismChosenReduction.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismChosenReduction.lean#L181). The attribute's comment: “condition (2) implies condition (1), for the morphism f_red of the chosen reductions”.

> **Stacks 0AJB, condition (2) implies condition (1).** The fibre product condition over the
> quasi-compact schemes over `S` in the site restricts to the affine ones, which already makes the
> morphism `f_red` of the chosen reductions a quasi-compact morphism of algebraic spaces.

```lean
theorem IsQuasiCompactOnSchemeBaseChanges.isQuasiCompactULift_chosenReductionMap
    {X Y : FppfSheaf B S hS} (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (h : IsQuasiCompactOnSchemeBaseChanges B S hS f) :
    Space.IsQuasiCompactULift.{u + 1} B S hS (chosenReductionMap B S hS hX hY f).hom
```

**`AlgebraicGeometry.FormalSpace.IsQuasiCompact.isQuasiCompactOnSchemeBaseChanges`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismDecomposition.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismDecomposition.lean#L202). The attribute's comment: “condition (3) implies condition (2)”.

> **Stacks 0AJB, condition (3) implies condition (2).** Let `f : X ⟶ Y` be a morphism of fppf
> sheaves on the big fppf site of `S` every one of whose fibre products with an affine scheme over
> `S` in the site mapping to `Y` is a quasi-compact formal algebraic space over `S`. Then the same
> holds over every *quasi-compact* scheme over `S` in the site.
>
> Let `T` be such a scheme and let `W` be a fibre product of `f` with a point `T ⟶ Y`. A finite
> affine open covering `{U_i ⟶ T}` of `T` inside the site exists because `T` is quasi-compact
> (`AlgebraicGeometry.BigFppfOver.exists_finite_affine_open_cover`). Each `W ×_T U_i` is, by
> pasting the two cartesian squares, a fibre product of `f` with the affine point `U_i ⟶ Y`, hence
> a quasi-compact formal algebraic space by the hypothesis; each projection `W ×_T U_i ⟶ W` is a
> base change of `U_i ⟶ T`, hence representable étale, an open immersion being étale; and the
> family of projections is jointly surjective because `{U_i ⟶ T}` generates a covering sieve and
> coproducts of sheaves of types are stable under base change. So
> `AlgebraicGeometry.FormalSpace.isQuasiCompactSpace_of_finite_isRepresentableEtale_cover`
> applies.

```lean
theorem IsQuasiCompact.isQuasiCompactOnSchemeBaseChanges {X Y : FppfSheaf B S hS} {f : X ⟶ Y}
    (h : IsQuasiCompact B S hS f) : IsQuasiCompactOnSchemeBaseChanges B S hS f
```

**`AlgebraicGeometry.FormalSpace.isQuasiCompact_iff_isQuasiCompactOnSchemeBaseChanges`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismDecomposition.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismDecomposition.lean#L265). The attribute's comment: “the equivalence of conditions (2) and (3)”.

> **Stacks 0AJB, the equivalence of conditions (2) and (3).** For a morphism of fppf sheaves
> on the big fppf site of `S`, the fibre product condition over the quasi-compact schemes over `S`
> in the site and the fibre product condition over the affine ones are equivalent.
>
> One implication restricts the quantifier, an affine scheme being quasi-compact, and is
> `AlgebraicGeometry.FormalSpace.IsQuasiCompactOnSchemeBaseChanges.isQuasiCompact`; the other is
> `AlgebraicGeometry.FormalSpace.IsQuasiCompact.isQuasiCompactOnSchemeBaseChanges`. This is the
> first cycle closed among the four conditions of Stacks 0AJB.

```lean
theorem isQuasiCompact_iff_isQuasiCompactOnSchemeBaseChanges {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) :
    IsQuasiCompact B S hS f ↔ IsQuasiCompactOnSchemeBaseChanges B S hS f
```

**`AlgebraicGeometry.FormalSpace.IsQuasiCompactOnReductions.hasQuasiCompactFormalAtlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismFormalAtlas.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismFormalAtlas.lean#L269). The attribute's comment: “condition (1) implies condition (4), with the reductions quantified over in place of Stacks 0AIN and with the source's own hypothesis that X and Y be formal algebraic spaces, which is what supplies the covering of Y that condition (4) asks for”.

> **Stacks 0AJB, condition (1) implies condition (4).** Let `f : X ⟶ Y` be a morphism of
> formal algebraic spaces over `S` such that every morphism between reductions of `X` and of `Y`
> compatible with `f` is a quasi-compact morphism of algebraic spaces. Then there is a covering
> `{Yⱼ ⟶ Y}` as in Definition 0AIM all of whose fibre products with `f` are quasi-compact formal
> algebraic spaces over `S`.
>
> The covering is the atlas of `Y` that the hypothesis `IsFormalAlgebraicSpace B S hS Y` supplies,
> which is the covering Definition 0AIM provides and the one the source's hypothesis on `Y` names.
> Its members are affine formal algebraic spaces, hence quasi-compact formal algebraic spaces, and
> representable by algebraic spaces and étale, so
> `IsQuasiCompactOnReductions.isQuasiCompactSpace_of_isRepresentableEtale` applies to each fibre
> product.

```lean
theorem IsQuasiCompactOnReductions.hasQuasiCompactFormalAtlas {X Y : FppfSheaf B S hS}
    {f : X ⟶ Y} (h : IsQuasiCompactOnReductions B S hS f)
    (hX : IsFormalAlgebraicSpace B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y) :
    HasQuasiCompactFormalAtlas B S hS f
```

**`AlgebraicGeometry.FormalSpace.IsQuasiCompact.hasQuasiCompactFormalAtlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismFormalAtlas.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismFormalAtlas.lean#L292). The attribute's comment: “condition (3) implies condition (4), with the source's own hypothesis that X and Y be formal algebraic spaces”.

> **Stacks 0AJB, condition (3) implies condition (4).** A morphism of formal algebraic spaces
> over `S` which is quasi-compact in the sense of Stacks 0AJC — every fibre product of it with an
> affine scheme over `S` in the site mapping to its target is a quasi-compact formal algebraic
> space — admits a covering of its target as in Definition 0AIM all of whose fibre products with
> it are quasi-compact formal algebraic spaces.
>
> Condition (3) implies condition (1) by
> `AlgebraicGeometry.FormalSpace.IsQuasiCompact.isQuasiCompactOnReductions`, and condition (1)
> implies condition (4).

```lean
theorem IsQuasiCompact.hasQuasiCompactFormalAtlas {X Y : FppfSheaf B S hS} {f : X ⟶ Y}
    (h : IsQuasiCompact B S hS f) (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) : HasQuasiCompactFormalAtlas B S hS f
```

**`AlgebraicGeometry.FormalSpace.IsQuasiCompactOnSchemeBaseChanges.hasQuasiCompactFormalAtlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismFormalAtlas.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismFormalAtlas.lean#L305). The attribute's comment: “condition (2) implies condition (4), with the source's own hypothesis that X and Y be formal algebraic spaces”.

> **Stacks 0AJB, condition (2) implies condition (4).** A morphism of formal algebraic spaces
> over `S` every one of whose fibre products with a quasi-compact scheme over `S` in the site
> mapping to its target is a quasi-compact formal algebraic space admits a covering of its target
> as in Definition 0AIM all of whose fibre products with it are quasi-compact formal algebraic
> spaces: condition (2) restricts to the affine schemes, which is condition (3).

```lean
theorem IsQuasiCompactOnSchemeBaseChanges.hasQuasiCompactFormalAtlas {X Y : FppfSheaf B S hS}
    {f : X ⟶ Y} (h : IsQuasiCompactOnSchemeBaseChanges B S hS f)
    (hX : IsFormalAlgebraicSpace B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y) :
    HasQuasiCompactFormalAtlas B S hS f
```

**`AlgebraicGeometry.FormalSpace.IsQuasiCompact.isQuasiCompactOnReductions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismReductions.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismReductions.lean#L183). The attribute's comment: “condition (3) implies condition (1), with the reductions quantified over in place of Stacks 0AIN”.

> **Stacks 0AJB, condition (3) implies condition (1).** Let `f : X ⟶ Y` be a morphism of
> fppf sheaves on the big fppf site of `S` such that every fibre product of `f` with an affine
> scheme over `S` in the site mapping to `Y` is a quasi-compact formal algebraic space — that is,
> let `f` be quasi-compact in the sense of Stacks 0AJC. Then every morphism between reductions of
> `X` and of `Y` compatible with `f` is a quasi-compact morphism of algebraic spaces.
>
> Quasi-compactness of the morphism of reductions is tested against the quasi-compact algebraic
> spaces mapping to the reduction of `Y`; such a space has, by Stacks 03H6, a surjective étale
> chart by an *affine* scheme of the site, along which the test descends, so it suffices to treat
> an affine scheme of the site, which is `isQuasiCompactSpaceULift_pullback_of_affine`.

```lean
theorem IsQuasiCompact.isQuasiCompactOnReductions (hf : IsQuasiCompact B S hS f) :
    IsQuasiCompactOnReductions B S hS f
```

**`AlgebraicGeometry.FormalSpace.IsQuasiCompactOnSchemeBaseChanges.isQuasiCompactOnReductions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismReductions.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismReductions.lean#L197). The attribute's comment: “condition (2) implies condition (1), with the reductions quantified over in place of Stacks 0AIN”.

> **Stacks 0AJB, condition (2) implies condition (1).** The fibre product condition over the
> quasi-compact schemes over `S` in the site restricts to the affine ones, which already implies
> quasi-compactness of every induced morphism of reductions.

```lean
theorem IsQuasiCompactOnSchemeBaseChanges.isQuasiCompactOnReductions
    (hf : IsQuasiCompactOnSchemeBaseChanges B S hS f) :
    IsQuasiCompactOnReductions B S hS f
```

**`AlgebraicGeometry.FormalSpace.HasQuasiCompactFormalAtlas.isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismTFAE.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismTFAE.lean#L172). The attribute's comment: “condition (4) implies condition (3)”.

> **Stacks 0AJB, condition (4) implies condition (3).** Let `f : X ⟶ Y` be a morphism of fppf
> sheaves on the big fppf site of `S` admitting a covering `{cⱼ : Yⱼ ⟶ Y}` as in Definition 0AIM
> all of whose fibre products with `f` are quasi-compact formal algebraic spaces. Then every fibre
> product of `f` with an affine scheme over `S` in the site mapping to `Y` is a quasi-compact formal
> algebraic space; that is, `f` is quasi-compact in the sense of Stacks 0AJC.
>
> Let `g : T ⟶ Y` with `T` affine. The base changes `Yⱼ ×_Y T` are objects `Vⱼ` of the site étale
> over `T` (Stacks 0AIG); an affine open of some `Vⱼ` through each point of `T`, and
> quasi-compactness of `T`, give finitely many affine objects `Uₖ` étale over `T`, covering it, each
> mapping to a member `Yⱼ` compatibly with `g`. The fibre product `W = X ×_Y T` is covered along
> representable étale morphisms by the finitely many `W ×_T Uₖ = X ×_Y Uₖ`, each of which is
> quasi-compact by
> `AlgebraicGeometry.FormalSpace.isQuasiCompactSpace_of_isPullback_comp`, so `W` is quasi-compact
> by `AlgebraicGeometry.FormalSpace.isQuasiCompactSpace_of_finite_isRepresentableEtale_cover`.

```lean
theorem HasQuasiCompactFormalAtlas.isQuasiCompact {X Y : FppfSheaf B S hS} {f : X ⟶ Y}
    (h : HasQuasiCompactFormalAtlas B S hS f) : IsQuasiCompact B S hS f
```

**`AlgebraicGeometry.FormalSpace.tfae_isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismTFAE.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismTFAE.lean#L297). The attribute's comment: “the equivalence of the four conditions”.

> **Stacks 0AJB.** Let `f : X ⟶ Y` be a morphism of formal algebraic spaces over `S`. The
> following are equivalent:
>
> 1. the morphism `f_red : X_red ⟶ Y_red` induced between the reductions (Stacks 0AIN) is a
>    quasi-compact morphism of algebraic spaces;
> 2. for every quasi-compact scheme `T` over `S` in the site and morphism `T ⟶ Y`, the fibre product
>    `X ×_Y T` is a quasi-compact formal algebraic space;
> 3. the same for every affine scheme `T` over `S` in the site;
> 4. there is a covering `{Yⱼ ⟶ Y}` as in Definition 0AIM such that every `X ×_Y Yⱼ` is a
>    quasi-compact formal algebraic space.
>
> The reductions in condition (1) are the chosen ones,
> `AlgebraicGeometry.FormalSpace.reduction`, and `f_red` is
> `AlgebraicGeometry.FormalSpace.chosenReductionMap`. The cycle of implications is
> (1) ⇒ (4) (`IsQuasiCompactOnReductions.hasQuasiCompactFormalAtlas`),
> (4) ⇒ (3) (`HasQuasiCompactFormalAtlas.isQuasiCompact`),
> (3) ⇒ (2) (`IsQuasiCompact.isQuasiCompactOnSchemeBaseChanges`)
> and (2) ⇒ (1) (`IsQuasiCompactOnSchemeBaseChanges.isQuasiCompactULift_chosenReductionMap`).

```lean
theorem tfae_isQuasiCompact {X Y : FppfSheaf B S hS} (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    List.TFAE
      [Space.IsQuasiCompactULift.{u + 1} B S hS (chosenReductionMap B S hS hX hY f).hom,
        IsQuasiCompactOnSchemeBaseChanges B S hS f,
        IsQuasiCompact B S hS f,
        HasQuasiCompactFormalAtlas B S hS f]
```

## Tag 0AJC, a definition

[Tag 0AJC](https://stacks.math.columbia.edu/tag/0AJC) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsQuasiCompact`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphism.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphism.lean#L199). The attribute's comment: “condition (3) of Stacks 0AJB taken as the definition”.

> **Stacks 0AJC**, in the form of **Stacks 0AJB, condition (3)**. A morphism of formal
> algebraic spaces over `S` is *quasi-compact* when every fibre product of it with an affine
> scheme over `S` in the site mapping to its target is a quasi-compact formal algebraic space
> over `S`. The condition makes sense, and is stated, for an arbitrary morphism of fppf sheaves
> on the big fppf site of `S`.

```lean
abbrev IsQuasiCompact {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

## Tag 0AM2, a lemma

[Tag 0AM2](https://stacks.math.columbia.edu/tag/0AM2) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isQuasiCompact_iff_hasPropertyULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphism.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphism.lean#L394). The attribute's comment: “both directions, for an arbitrary morphism of fppf sheaves representable by algebraic spaces, with two named hypotheses: `QuasiCompactSpaceAgreesOnAlgebraicSpaces`, the agreement of the quasi-compactness notions of Stacks 0AJ9 and Stacks 03E3 on an algebraic space, and the implication (3) ⇒ (2) of Stacks 0AJB for the morphism”.

> **Stacks 0AM2.** Let `f : X ⟶ Y` be a morphism of formal algebraic spaces over `S` which
> is representable by algebraic spaces. Then `f` is quasi-compact in the sense of Stacks 0AJC —
> every fibre product of it with an affine scheme over `S` in the site is a quasi-compact formal
> algebraic space — exactly when it is quasi-compact in the sense of Bootstrap, Definition
> 03XZ: every fibre product of it with a scheme over `S` in the site is quasi-compact over that
> scheme as a morphism of algebraic spaces.
>
> Both directions pass through the agreement of the two notions of quasi-compactness of a space
> on an algebraic space, which is the hypothesis
> `AlgebraicGeometry.FormalSpace.QuasiCompactSpaceAgreesOnAlgebraicSpaces`. For the remaining
> direction the bootstrap condition must be tested against the quasi-compact, not only the
> affine, schemes over `S` in the site, which is the implication (3) ⇒ (2) of Stacks 0AJB and is
> the second hypothesis. The witnesses that the source and the target are formal algebraic
> spaces are not used, so the statement is for an arbitrary morphism of fppf sheaves.

```lean
theorem isQuasiCompact_iff_hasPropertyULift {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (hagree : QuasiCompactSpaceAgreesOnAlgebraicSpaces B S hS)
    (hbase : IsQuasiCompact B S hS f → IsQuasiCompactOnSchemeBaseChanges B S hS f) :
    IsQuasiCompact B S hS f ↔
      Space.HasPropertyULift.{u + 1} B S hS
        (Space.quasiCompactPropertyULift.{u + 1} B S hS) f.hom hf
```

**`AlgebraicGeometry.FormalSpace.isQuasiCompact_iff_hasPropertyULift'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismComparison.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactMorphismComparison.lean#L120). The attribute's comment: “both directions, for an arbitrary morphism of fppf sheaves representable by algebraic spaces”.

> **Stacks 0AM2.** Let `f : X ⟶ Y` be a morphism of formal algebraic spaces over `S` which
> is representable by algebraic spaces. Then `f` is quasi-compact in the sense of Stacks 0AJC —
> every fibre product of it with an affine scheme over `S` in the site is a quasi-compact formal
> algebraic space — exactly when it is quasi-compact in the sense of Bootstrap, Definition
> 03XZ: every fibre product of it with a scheme over `S` in the site is quasi-compact over that
> scheme as a morphism of algebraic spaces.
>
> Both directions pass through the agreement of the two notions of quasi-compactness of a space
> on an algebraic space, which is
> `AlgebraicGeometry.FormalSpace.quasiCompactSpaceAgreesOnAlgebraicSpaces`. For the remaining
> direction the bootstrap condition must be tested against the quasi-compact, not only the
> affine, schemes over `S` in the site, which is the implication (3) ⇒ (2) of Stacks 0AJB,
> `AlgebraicGeometry.FormalSpace.IsQuasiCompact.isQuasiCompactOnSchemeBaseChanges`. The witnesses
> that the source and the target are formal algebraic spaces are not used, so the statement is
> for an arbitrary morphism of fppf sheaves.

```lean
theorem isQuasiCompact_iff_hasPropertyULift' {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom) :
    IsQuasiCompact B S hS f ↔
      Space.HasPropertyULift.{u + 1} B S hS
        (Space.quasiCompactPropertyULift.{u + 1} B S hS) f.hom hf
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.17, Tag 0AJ8](https://stacks.math.columbia.edu/tag/0AJ8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
