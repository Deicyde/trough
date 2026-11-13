---
declaration: section
origin: cited
lean: CategoryTheory.ObjectProperty.prop_obj₂_of_exact, CategoryTheory.ObjectProperty.IsSerreClass, CategoryTheory.ObjectProperty.isSerreClass_iff_prop_X₂_of_exact, CategoryTheory.ObjectProperty.abelian_of_isSerreClass, CategoryTheory.ObjectProperty.preservesFiniteLimits_ι, CategoryTheory.ObjectProperty.preservesFiniteLimits_ι_and_preservesFiniteColimits_ι, CategoryTheory.ObjectProperty.isSerreClass_iff_and_abelian_and_exact, CategoryTheory.ObjectProperty.IsWeakSerreClass
statement: formalized
proof: formalized
---

# 12.10 Serre subcategories

Section 12.10 of the Stacks Project, [Tag 02MN](https://stacks.math.columbia.edu/tag/02MN). 7 tags here are carried by 18 declarations of the repository (10 in StacksCore and 8 in StacksFrontier) and 8 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02MO, a definition

[Tag 02MO](https://stacks.math.columbia.edu/tag/02MO) in the Stacks Project.

**`CategoryTheory.ObjectProperty.prop_obj₂_of_exact`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean#L77). The attribute's comment: “part 2”.

> **Stacks 02MO (2).** A weak Serre subcategory in the sense of 0754 contains the middle term of
> every five term exact sequence whose other four terms belong to it.
>
> The middle term is an extension of `ker (A₃ ⟶ A₄)` by `coker (A₀ ⟶ A₁)`: exactness at `A₁` makes
> `coker (A₀ ⟶ A₁) ⟶ A₂` a monomorphism, exactness at `A₃` makes `A₂ ⟶ ker (A₃ ⟶ A₄)` an
> epimorphism, and the resulting short complex is exact because it differs from `A₁ ⟶ A₂ ⟶ A₃` by
> an epimorphism on the left and a monomorphism on the right.

```lean
theorem prop_obj₂_of_exact [P.IsWeakSerreClass] (S : ComposableArrows C 4) (hS : S.Exact)
    (h₀ : P (S.obj' 0)) (h₁ : P (S.obj' 1)) (h₃ : P (S.obj' 3)) (h₄ : P (S.obj' 4)) :
    P (S.obj' 2)
```

Declarations registered for the tag:

- [`CategoryTheory.ObjectProperty.IsSerreClass`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ObjectProperty.IsSerreClass#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/SerreClass/Basic.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/SerreClass/Basic.lean#L38) (StacksCore): “part 1, packaged as closure under subobjects, quotients and extensions; `isSerreClass_iff_prop_X₂_of_exact` identifies this with the definition in the Stacks project.”.

## Tag 02MP, a lemma

[Tag 02MP](https://stacks.math.columbia.edu/tag/02MP) in the Stacks Project.

**`CategoryTheory.ObjectProperty.isSerreClass_iff_prop_X₂_of_exact`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Basic.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/SerreClass/Basic.lean#L92). The attribute's comment: “the equivalence part”.

> **Stacks 02MP.** Mathlib's `ObjectProperty.IsSerreClass` — zero, subobjects, quotients,
> extensions — is the Stacks project's Serre subcategory: nonempty, and containing the middle term
> of every exact sequence whose outer terms belong to it.
>
> Condition (2), strict fullness, is not a hypothesis here: an `ObjectProperty` is a predicate on
> objects, and a Serre class is closed under isomorphism, so it holds by construction.

```lean
theorem isSerreClass_iff_prop_X₂_of_exact :
    P.IsSerreClass ↔ (∃ X, P X) ∧
      ∀ S : ShortComplex C, S.Exact → P S.X₁ → P S.X₃ → P S.X₂
```

**`CategoryTheory.ObjectProperty.abelian_of_isSerreClass`**, a private lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Basic.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/SerreClass/Basic.lean#L118). The attribute's comment: “Serre Subcategory is abelian”.

```lean
private lemma abelian_of_isSerreClass [P.IsSerreClass] :
    Nonempty (Abelian P.FullSubcategory)
```

**`CategoryTheory.ObjectProperty.preservesFiniteLimits_ι`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Basic.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/SerreClass/Basic.lean#L122). The attribute's comment: “inclusion functor is exact”.

```lean
lemma preservesFiniteLimits_ι [P.IsSerreClass] : PreservesFiniteLimits P.ι
```

**`CategoryTheory.ObjectProperty.preservesFiniteLimits_ι_and_preservesFiniteColimits_ι`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/SerreClass/Exact.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/SerreClass/Exact.lean#L43). The attribute's comment: “inclusion functor is exact (left and right exact)”.

> **Stacks 02MP**, "moreover": the inclusion of a Serre subcategory is exact, that is, it
> preserves finite limits (it preserves kernels) and finite colimits (it preserves cokernels).

```lean
lemma preservesFiniteLimits_ι_and_preservesFiniteColimits_ι [P.IsSerreClass] :
    PreservesFiniteLimits P.ι ∧ PreservesFiniteColimits P.ι
```

**`CategoryTheory.ObjectProperty.isSerreClass_iff_and_abelian_and_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/SerreClass/Exact.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/SerreClass/Exact.lean#L57). The attribute's comment: “the equivalence, and moreover: abelian with exact inclusion functor”.

> **Stacks 02MP**, in full. A full subcategory of an abelian category closed under isomorphisms
> is a Serre subcategory (Mathlib's `IsSerreClass`: zero, subobjects, quotients, extensions) exactly
> when it is nonempty and contains the middle term of every exact sequence whose outer terms belong
> to it; and a Serre subcategory is abelian, with inclusion functor preserving finite limits and
> finite colimits, that is, exact.
>
> Strict fullness is not a hypothesis: an `ObjectProperty` is a predicate on objects, and a Serre
> class is closed under isomorphism, so it holds by construction.

```lean
theorem isSerreClass_iff_and_abelian_and_exact :
    (P.IsSerreClass ↔ (∃ X, P X) ∧
        ∀ S : ShortComplex C, S.Exact → P S.X₁ → P S.X₃ → P S.X₂) ∧
      (P.IsSerreClass → Nonempty (Abelian P.FullSubcategory) ∧
        PreservesFiniteLimits P.ι ∧ PreservesFiniteColimits P.ι)
```

## Tag 0754, a lemma

[Tag 0754](https://stacks.math.columbia.edu/tag/0754) in the Stacks Project.

**`CategoryTheory.ObjectProperty.IsWeakSerreClass`**, a class in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean, line 36](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean#L36). The attribute's comment: “conditions (1)-(4), as the definition”. References: SGA 6 IV (1.6).

> **Stacks 0754**, conditions (1)–(4): a *weak Serre subcategory* is a strictly full subcategory
> which contains `0` and is closed under kernels, cokernels and extensions.
>
> `prop_obj₂_of_exact` shows this satisfies the definition in 02MO (2).

```lean
class IsWeakSerreClass : Prop extends P.ContainsZero, P.IsClosedUnderIsomorphisms,
    P.IsClosedUnderKernels, P.IsClosedUnderCokernels, P.IsClosedUnderExtensions
```

**`CategoryTheory.ObjectProperty.abelian_of_isWeakSerreClass`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean#L53). The attribute's comment: “moreover: a weak Serre subcategory is abelian”.

> **Stacks 0754**, "moreover": a weak Serre subcategory is an abelian category.

```lean
lemma abelian_of_isWeakSerreClass : Nonempty (Abelian P.FullSubcategory)
```

**`CategoryTheory.ObjectProperty.preservesFiniteLimits_ι_of_isWeakSerreClass`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean#L57). The attribute's comment: “moreover: the inclusion functor preserves finite limits”.

> **Stacks 0754**, "moreover": the inclusion functor is exact, here its left exactness.

```lean
lemma preservesFiniteLimits_ι_of_isWeakSerreClass : PreservesFiniteLimits P.ι
```

**`CategoryTheory.ObjectProperty.preservesFiniteColimits_ι_of_isWeakSerreClass`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean#L63). The attribute's comment: “moreover: the inclusion functor preserves finite colimits”.

> **Stacks 0754**, "moreover": the inclusion functor is exact, here its right exactness.

```lean
lemma preservesFiniteColimits_ι_of_isWeakSerreClass : PreservesFiniteColimits P.ι
```

**`CategoryTheory.ObjectProperty.isWeakSerreClass_iff_prop_obj₂_of_exact`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean#L198).

> **Stacks 0754.** The closure conditions defining `IsWeakSerreClass` are equivalent to the
> definition of a weak Serre subcategory in 02MO (2): being nonempty and containing the middle term
> of every five term exact sequence whose other four terms belong to it.

```lean
theorem isWeakSerreClass_iff_prop_obj₂_of_exact :
    P.IsWeakSerreClass ↔ (∃ X, P X) ∧
      ∀ S : ComposableArrows C 4, S.Exact → P (S.obj' 0) → P (S.obj' 1) →
        P (S.obj' 3) → P (S.obj' 4) → P (S.obj' 2)
```

## Tag 02MQ, a lemma

[Tag 02MQ](https://stacks.math.columbia.edu/tag/02MQ) in the Stacks Project.

Declarations registered for the tag:

- [`instIsSerreClassInverseImageOfPreservesFiniteLimitsOfPreservesFiniteColimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=instIsSerreClassInverseImageOfPreservesFiniteLimitsOfPreservesFiniteColimits#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/SerreClass/Basic.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/SerreClass/Basic.lean#L42) (StacksCore): “the objects killed by an exact functor are `Functor.kernel F`, which is by definition the inverse image along `F` of the Serre class of zero objects. So the tag is the composition of this instance with `instIsSerreClassIsZero`, and needs no proof of its own: `inferInstance` closes it. As for 02MO, `isSerreClass_iff_prop_X₂_of_exact` is what makes `IsSerreClass` the Stacks notion here.”.

## Tag 02MR, a definition

[Tag 02MR](https://stacks.math.columbia.edu/tag/02MR) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.kernel`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.kernel#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/ObjectProperty/ContainsZero.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/ObjectProperty/ContainsZero.lean#L8) (StacksCore): “`Ker F`, the full subcategory of objects killed by `F`. Reducibly `ObjectProperty.inverseImage IsZero F`, hence the very object property that 02MQ is stated for in `StacksCore.CategoryTheory.Abelian.SerreClass.Basic`: one definition seen twice, with `F.kernel X ↔ IsZero (F.obj X)` by `rfl`.”. References: SGA 4½ Etat 0 (2.2).

## Tag 02MS, a lemma

[Tag 02MS](https://stacks.math.columbia.edu/tag/02MS) in the Stacks Project.

**`CategoryTheory.ObjectProperty.SerreClassLocalization.exists_abelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean#L67). The attribute's comment: “`A/C` is abelian, with its given preadditive structure”.

> **Stacks 02MS**, `A/C` is abelian: there is an abelian structure on `D` whose preadditive
> structure is the given one.

```lean
theorem exists_abelian : ∃ h : Abelian D, h.toPreadditive = ‹Preadditive D›
```

**`CategoryTheory.ObjectProperty.SerreClassLocalization.essSurj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean#L74). The attribute's comment: “`F` is essentially surjective”.

> **Stacks 02MS**, the quotient functor `F : A ⥤ A/C` is essentially surjective.

```lean
theorem essSurj : L.EssSurj
```

**`CategoryTheory.ObjectProperty.SerreClassLocalization.kernel_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean#L79). The attribute's comment: “`Ker F = C`”.

> **Stacks 02MS**, the kernel of the quotient functor `F : A ⥤ A/C` is exactly `C`.

```lean
theorem kernel_eq : L.kernel = P
```

**`CategoryTheory.ObjectProperty.SerreClassLocalization.exists_exact_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean#L88). The attribute's comment: “universal property, existence of the exact factorization `G ≅ F ⋙ H`”.

> **Stacks 02MS**, the universal property, existence: an exact `G : A ⥤ B` whose kernel contains
> `C` factors as `G ≅ F ⋙ H` through an exact `H : A/C ⥤ B`.

```lean
theorem exists_exact_lift (G : C ⥤ B) [PreservesFiniteLimits G] [PreservesFiniteColimits G]
    (hG : P ≤ G.kernel) :
    ∃ H : D ⥤ B, PreservesFiniteLimits H ∧ PreservesFiniteColimits H ∧ Nonempty (L ⋙ H ≅ G)
```

**`CategoryTheory.ObjectProperty.SerreClassLocalization.existsUnique_iso_of_comp_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean#L105). The attribute's comment: “universal property, uniqueness of `H` up to a unique compatible isomorphism”.

> **Stacks 02MS**, the universal property, uniqueness: two factorizations `e₁ : F ⋙ H₁ ≅ G` and
> `e₂ : F ⋙ H₂ ≅ G` are related by a unique isomorphism `φ : H₁ ≅ H₂` with `F ⋙ φ` followed by `e₂`
> equal to `e₁`.

```lean
theorem existsUnique_iso_of_comp_iso {G : C ⥤ B} (H₁ H₂ : D ⥤ B) (e₁ : L ⋙ H₁ ≅ G)
    (e₂ : L ⋙ H₂ ≅ G) : ∃! φ : H₁ ≅ H₂, Functor.isoWhiskerLeft L φ ≪≫ e₂ = e₁
```

**`CategoryTheory.ObjectProperty.SerreClassLocalization.exists_abelian_and_universal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean#L125).

> **Stacks 02MS.** For a Serre subcategory `C` of an abelian category `A`, the quotient
> `F : A ⥤ A/C` (any localization functor for `P.isoModSerre`) has: `A/C` abelian, `F` exact,
> `F` essentially surjective, `Ker F = C`, and every exact `G : A ⥤ B` to an abelian category with
> `C ⊂ Ker G` factors as `G ≅ F ⋙ H` through an exact `H`, unique up to a unique isomorphism
> compatible with the factorizations.

```lean
theorem exists_abelian_and_universal :
    (∃ h : Abelian D, h.toPreadditive = ‹Preadditive D›) ∧
      (PreservesFiniteLimits L ∧ PreservesFiniteColimits L) ∧ L.EssSurj ∧ L.kernel = P ∧
      ∀ {B : Type u₃} [Category.{v₃} B] [Abelian B] (G : C ⥤ B) [PreservesFiniteLimits G]
        [PreservesFiniteColimits G], P ≤ G.kernel →
        (∃ H : D ⥤ B, PreservesFiniteLimits H ∧ PreservesFiniteColimits H ∧
          Nonempty (L ⋙ H ≅ G)) ∧
        ∀ (H₁ H₂ : D ⥤ B) (e₁ : L ⋙ H₁ ≅ G) (e₂ : L ⋙ H₂ ≅ G),
          ∃! φ : H₁ ≅ H₂, Functor.isoWhiskerLeft L φ ≪≫ e₂ = e₁
```

Declarations registered for the tag:

- [`CategoryTheory.ObjectProperty.SerreClassLocalization.preservesFiniteLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ObjectProperty.SerreClassLocalization.preservesFiniteLimits#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean#L51) (StacksFrontier): “`F` is exact: it preserves finite limits”. References: SGA 4 VI (6.5), “Clause e), special case”.
- [`CategoryTheory.ObjectProperty.SerreClassLocalization.preservesFiniteColimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ObjectProperty.SerreClassLocalization.preservesFiniteColimits#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean#L53) (StacksFrontier): “`F` is exact: it preserves finite colimits”. References: SGA 5 V (2.3.4), “special case”.
- [`CategoryTheory.ObjectProperty.SerreClassLocalization.isZero_obj_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ObjectProperty.SerreClassLocalization.isZero_obj_iff#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean#L55) (StacksFrontier): “`Ker F = C`, objectwise: `F X = 0` iff `X ∈ C`”. References: SGA 5 V (2.3.5), “special case”.
- [`CategoryTheory.ObjectProperty.SerreClassLocalization.fullyFaithfulWhiskeringLeft`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ObjectProperty.SerreClassLocalization.fullyFaithfulWhiskeringLeft#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean#L57) (StacksFrontier): “universal property: precomposing with `F` is fully faithful on exact functors”.
- [`CategoryTheory.ObjectProperty.SerreClassLocalization.essImage_whiskeringLeft`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ObjectProperty.SerreClassLocalization.essImage_whiskeringLeft#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/SerreClass/Quotient.lean#L59) (StacksFrontier): “universal property: an exact functor factors through `F` iff it inverts `isoModSerre`”.

## Tag 06XK, a lemma

[Tag 06XK](https://stacks.math.columbia.edu/tag/06XK) in the Stacks Project.

**`CategoryTheory.ObjectProperty.SerreClassLocalization.faithful_liftOfLeKernel_iff`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Localization.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/SerreClass/Localization.lean#L126).

> **Stacks 06XK.** For an exact `F : A ⥤ B` and a Serre subcategory `C ⊂ A` contained in `Ker F`,
> the induced functor `F̄ : A/C ⥤ B` is faithful exactly when `C` is all of `Ker F`.

```lean
theorem faithful_liftOfLeKernel_iff (hP : P ≤ F.kernel) :
    (liftOfLeKernel L P F hP).Faithful ↔ P = F.kernel
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.10, Tag 02MN](https://stacks.math.columbia.edu/tag/02MN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
