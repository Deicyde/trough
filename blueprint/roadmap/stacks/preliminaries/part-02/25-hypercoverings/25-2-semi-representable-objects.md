---
declaration: section
origin: cited
lean: CategoryTheory.Limits.FormalCoproduct, CategoryTheory.Limits.FormalCoproduct.Hom, CategoryTheory.Limits.FormalCoproduct.category, CategoryTheory.Limits.FormalCoproduct.yoneda, CategoryTheory.Limits.FormalCoproduct.instHasBinaryProducts, CategoryTheory.Limits.FormalCoproduct.instHasEqualizers, CategoryTheory.Limits.FormalCoproduct.hasCoproducts_formalCoproduct, CategoryTheory.Limits.FormalCoproduct.preservesColimitsOfShape_yoneda
statement: formalized
proof: formalized
---

# 25.2 Semi-representable objects

Section 25.2 of the Stacks Project, [Tag 0DBB](https://stacks.math.columbia.edu/tag/0DBB). 3 tags here are carried by 12 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01G0, a definition

[Tag 01G0](https://stacks.math.columbia.edu/tag/01G0) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Limits.FormalCoproduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.FormalCoproduct#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch25.lean, line 13](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch25.lean#L13) (StacksFrontier): “the objects of `SR(C)`: families `{U_i}_{i ∈ I}` of objects of `C`”.
- [`CategoryTheory.Limits.FormalCoproduct.Hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.FormalCoproduct.Hom#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch25.lean, line 16](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch25.lean#L16) (StacksFrontier): “the morphisms of `SR(C)`: a map `α : I → J` and morphisms `U_i → V_{α(i)}`”.
- [`CategoryTheory.Limits.FormalCoproduct.category`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.FormalCoproduct.category#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch25.lean, line 19](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch25.lean#L19) (StacksFrontier): “the category structure on `SR(C)`: identities and composition of such pairs”.

## Tag 01G1, a definition

[Tag 01G1](https://stacks.math.columbia.edu/tag/01G1) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Limits.FormalCoproduct.yoneda`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.FormalCoproduct.yoneda#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch25.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch25.lean#L27) (StacksFrontier): “the functor `F : SR(C) → PSh(C)`, `{U_i}_{i ∈ I} ↦ ∐ h_{U_i}`”.

## Tag 01G2, a lemma

[Tag 01G2](https://stacks.math.columbia.edu/tag/01G2) in the Stacks Project.

**`CategoryTheory.Limits.FormalCoproduct.instHasBinaryProducts`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/FormalCoproductBinaryProducts.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Limits/FormalCoproductBinaryProducts.lean#L55). The attribute's comment: “products of pairs in SR(C)”.

> **Stacks Project, Tag 01G2**, products of pairs clause. If `C` has binary products, then so
> does its category of formal coproducts — equivalently, the category `SR(C)` of semi-representable
> objects of `C` has binary products.

```lean
instance instHasBinaryProducts : HasBinaryProducts (FormalCoproduct.{w} C)
```

**`CategoryTheory.Limits.FormalCoproduct.instHasEqualizers`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/FormalCoproductEqualizers.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Limits/FormalCoproductEqualizers.lean#L116). The attribute's comment: “equalizers”. References: SGA 4 V (7.3.0), “equalizers in SR(C)”.

> **Stacks Project, Tag 01G2**, equalizers clause. If `C` has equalizers, then so does its
> category of formal coproducts — equivalently, the category `SR(C)` of semi-representable
> objects of `C` has equalizers.

```lean
instance instHasEqualizers : HasEqualizers (FormalCoproduct.{w} C)
```

**`CategoryTheory.Limits.FormalCoproduct.hasCoproducts_formalCoproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/FormalCoproductLimits.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Limits/FormalCoproductLimits.lean#L81). The attribute's comment: “coproducts in SR(C)”.

> **Stacks Project, Tag 01G2**, coproducts clause, first half. The category of formal
> coproducts of `C` — equivalently, the category `SR(C)` of semi-representable objects of `C` — has
> arbitrary coproducts, indexed by types in the index universe `w`. The coproduct of a family of
> families of objects is obtained by concatenating the index types.

```lean
theorem hasCoproducts_formalCoproduct : HasCoproducts.{w} (FormalCoproduct.{w} C)
```

**`CategoryTheory.Limits.FormalCoproduct.preservesColimitsOfShape_yoneda`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/FormalCoproductLimits.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Limits/FormalCoproductLimits.lean#L88). The attribute's comment: “F commutes with coproducts”.

> **Stacks Project, Tag 01G2**, coproducts clause, second half. The functor
> `F : SR(C) ⥤ PSh(C)`, sending a family `{U_i}` of objects of `C` to the coproduct `∐ h_{U_i}` of
> the representable presheaves, commutes with coproducts.

```lean
theorem preservesColimitsOfShape_yoneda (J : Type v) :
    PreservesColimitsOfShape (Discrete J) (FormalCoproduct.yoneda (C := C))
```

**`CategoryTheory.Limits.FormalCoproduct.preservesLimitsOfSize_yoneda`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/FormalCoproductLimits.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Limits/FormalCoproductLimits.lean#L133). The attribute's comment: “F : SR(C) → PSh(C) commutes with limits”.

> **Stacks Project, Tag 01G2**, limits clause. The functor `F : SR(C) ⥤ PSh(C)`, sending a
> family `{U_i}` of objects of `C` to the coproduct `∐ h_{U_i}` of the representable presheaves,
> commutes with limits — of any shape, and for an arbitrary category `C`.
>
> Limits of presheaves are computed sectionwise, and each section functor of `F` is corepresentable
> by `yonedaCompEvaluationIso`.

```lean
noncomputable instance preservesLimitsOfSize_yoneda :
    PreservesLimitsOfSize.{w, w'} (FormalCoproduct.yoneda (C := C))
```

**`CategoryTheory.Limits.FormalCoproduct.hasPullbacks_formalCoproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/FormalCoproductLimits.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Limits/FormalCoproductLimits.lean#L149). The attribute's comment: “fibre products in SR(C)”.

> **Stacks Project, Tag 01G2**, fibre products clause. If `C` has fibre products, then so does
> its category of formal coproducts — equivalently, the category `SR(C)` of semi-representable
> objects of `C` has fibre products. They are computed componentwise, the index type of
> `{U_i} ×_{{V_j}} {W_k}` being the set of triples `(i, j, k)` with `j` the common image of `i` and
> of `k`.

```lean
theorem hasPullbacks_formalCoproduct [HasPullbacks C] :
    HasPullbacks (FormalCoproduct.{w} C)
```

**`CategoryTheory.Limits.FormalCoproduct.hasTerminal_formalCoproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/FormalCoproductLimits.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Limits/FormalCoproductLimits.lean#L162). The attribute's comment: “final object in SR(C)”.

> **Stacks Project, Tag 01G2**, final object clause. If `C` has a final object `X`, then the
> one-member family `{X}` is a final object of the category of formal coproducts of `C` —
> equivalently, of the category `SR(C)` of semi-representable objects of `C`.

```lean
theorem hasTerminal_formalCoproduct [HasTerminal C] :
    HasTerminal (FormalCoproduct.{w} C)
```

**`Stacks.CategoryTheory.Hypercovering.hasFiniteLimits_formalCoproductOver`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CoveringPermanence.lean, line 915](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CoveringPermanence.lean#L915). The attribute's comment: “SR(C, X) has finite limits”.

> **Stacks Project, Tag 01G2**, finite limits clause for `SR(C, X)`, first half. If `C` has
> fibre products then `SR(C, X)` has finite limits: it has a terminal object, namely `{X → X}`, and
> it has fibre products, computed componentwise.
>
> The second half of the clause, that `F : SR(C, X) ⥤ PSh(C)/h_X` commutes with those finite
> limits, is the instance `CategoryTheory.Limits.FormalCoproduct.preservesLimitsOfSize_yonedaOver`
> in `StacksFrontier.CategoryTheory.Sites.Localization.SemiRepresentableOver`, for limits of every
> shape.

```lean
instance hasFiniteLimits_formalCoproductOver {X : C} :
    HasFiniteLimits (FormalCoproduct.{w} (Over X))
```

**`CategoryTheory.Limits.FormalCoproduct.yonedaOverObjIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/SemiRepresentableOver.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/SemiRepresentableOver.lean#L207). The attribute's comment: “the value of F: F(\{U\_i → X}) is ∐ h\_\{U\_i} augmented to h\_X”.

> **The value of `F` on a family, Stacks Project, Tag 01G2.** `F({U_i → X})` is the coproduct
> `∐ h_{U_i}` of the representable presheaves of the `U_i`, equipped with the map to `h_X` whose
> component on `h_{U_i}` is `h` of the structure morphism `U_i → X`. This is the source's
> `F({U_i → X}) = (∐ h_{U_i} → h_X)`, and it is what makes the clauses below statements about the
> source's `F`.
>
> The proof is the source's description read backwards: `FormalCoproduct.yoneda` of `C/X` sends
> `{U_i → X}` to the coproduct of the presheaves on `C/X` represented by the `U_i → X`, the
> presheaf level `j_{X!}` preserves that coproduct because it is a left adjoint
> (`OverShriek.presheafAdjunction`), and it takes the presheaf represented by `U_i → X` to the
> presheaf represented by `U_i` over `h_X` (`OverShriek.presheafFunctorToOverYonedaIso`).

```lean
noncomputable def yonedaOverObjIso (A : FormalCoproduct.{v} (Over X)) :
    (yonedaOver X).obj A ≅
      Over.mk (Sigma.desc fun i : A.I ↦ CategoryTheory.yoneda.map (A.obj i).hom)
```

**`CategoryTheory.Limits.FormalCoproduct.hasCoproducts_formalCoproductOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/SemiRepresentableOver.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/SemiRepresentableOver.lean#L216). The attribute's comment: “coproducts in SR(C, X)”.

> **Stacks Project, Tag 01G2**, coproducts clause for `SR(C, X)`, first half. The category
> `SR(C, X)` of semi-representable objects over `X` has arbitrary coproducts, obtained by
> concatenating the index types of the families.

```lean
theorem hasCoproducts_formalCoproductOver :
    HasCoproducts.{w} (FormalCoproduct.{w} (Over X))
```

**`CategoryTheory.Limits.FormalCoproduct.preservesColimitsOfShape_yonedaOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/SemiRepresentableOver.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/SemiRepresentableOver.lean#L224). The attribute's comment: “F commutes with coproducts in SR(C, X)”.

> **Stacks Project, Tag 01G2**, coproducts clause for `SR(C, X)`, second half. The functor
> `F : SR(C, X) ⥤ PSh(C)/h_X` commutes with coproducts: the semi-representable Yoneda embedding of
> `C/X` does, and `j_{X!} : PSh(C/X) ⥤ PSh(C)/h_X` is an equivalence.

```lean
theorem preservesColimitsOfShape_yonedaOver (J : Type v) :
    PreservesColimitsOfShape (Discrete J) (yonedaOver X)
```

**`CategoryTheory.Limits.FormalCoproduct.preservesLimitsOfSize_yonedaOver`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/SemiRepresentableOver.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/SemiRepresentableOver.lean#L235). The attribute's comment: “F : SR(C, X) → PSh(C)/h\_X commutes with finite limits”.

> **Stacks Project, Tag 01G2**, finite limits clause for `SR(C, X)`, second half. The functor
> `F : SR(C, X) ⥤ PSh(C)/h_X` commutes with limits of every shape, with no hypothesis on `C`; this
> strengthens the finite limits of the source's clause. The first half, that `SR(C, X)` has finite
> limits as soon as `C` has fibre products, is
> `Stacks.CategoryTheory.Hypercovering.hasFiniteLimits_formalCoproductOver`.

```lean
noncomputable instance preservesLimitsOfSize_yonedaOver :
    PreservesLimitsOfSize.{w, w'} (yonedaOver X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 25.2, Tag 0DBB](https://stacks.math.columbia.edu/tag/0DBB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
