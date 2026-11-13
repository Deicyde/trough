---
declaration: section
origin: cited
lean: preservesInjectiveObjects_of_exact_of_adjunction, exact_iff_preservesInjectiveObjects_of_adjunction, ModuleCat.flat_iff_restrictScalars_preservesInjectiveObjects, ModuleCat.extendScalars_adj_restrictScalars_exactness, ModuleCat.not_restrictScalars_preservesInjectiveObjects_intCast_zmod, ModuleCat.restrictScalars_extendScalars_injective_flat, CategoryTheory.EnoughInjectives.of_adjunction, hasFunctorialInjectiveEmbeddings_of_adjunction
statement: formalized
proof: formalized
---

# 12.29 Injectives and adjoint functors

Section 12.29 of the Stacks Project, [Tag 015Y](https://stacks.math.columbia.edu/tag/015Y). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 015Z, a lemma

[Tag 015Z](https://stacks.math.columbia.edu/tag/015Z) in the Stacks Project.

**`preservesInjectiveObjects_of_exact_of_adjunction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Injective/Adjunction.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/Injective/Adjunction.lean#L76). The attribute's comment: “first part”. References: SGA 4 V (0.2), “1) (i) ⇒ (ii)”.

> Conjunction of (a) ⇔ (b) and (b) ⇒ (c).

```lean
theorem preservesInjectiveObjects_of_exact_of_adjunction
    (u : A ⥤ B) (v : B ⥤ A) [u.Additive] [v.Additive] (adj : v ⊣ u) :
    (v.PreservesMonomorphisms ↔ (PreservesFiniteLimits v ∧ PreservesFiniteColimits v)) ∧
      ((PreservesFiniteLimits v ∧ PreservesFiniteColimits v) → u.PreservesInjectiveObjects)
```

**`exact_iff_preservesInjectiveObjects_of_adjunction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Injective/Adjunction.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/Injective/Adjunction.lean#L86). The attribute's comment: “full statement”. References: SGA 4 V (0.2), “1) (i)⇔(ii)”.

> Assuming `A` has enough injectives, the three conditions are equivalent.

```lean
theorem exact_iff_preservesInjectiveObjects_of_adjunction
    [EnoughInjectives A]
    (u : A ⥤ B) (v : B ⥤ A) [u.Additive] [v.Additive] (adj : v ⊣ u) :
    (v.PreservesMonomorphisms ↔ (PreservesFiniteLimits v ∧ PreservesFiniteColimits v)) ∧
      ((PreservesFiniteLimits v ∧ PreservesFiniteColimits v) ↔ u.PreservesInjectiveObjects)
```

## Tag 03B8, a remark

[Tag 03B8](https://stacks.math.columbia.edu/tag/03B8) in the Stacks Project.

**`ModuleCat.flat_iff_restrictScalars_preservesInjectiveObjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Injective/ChangeOfRings.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/Injective/ChangeOfRings.lean#L32). The attribute's comment: “flatness criterion”.

> **Stacks Project, Tag 03B8.**  Every injective `S`-module remains injective after
> restriction of scalars along `f : R →+* S` if and only if `f` is flat.
>
> The forward implication uses that extension of scalars along a flat map is exact.  Conversely,
> if restriction of scalars preserves injectives, its left adjoint preserves monomorphisms; since
> extension of scalars already preserves colimits, it is exact, and hence `S` is flat over `R`.

```lean
theorem ModuleCat.flat_iff_restrictScalars_preservesInjectiveObjects
    {R S : Type u} [CommRing R] [CommRing S] (f : R →+* S) :
    f.Flat ↔ (ModuleCat.restrictScalars.{u} f).PreservesInjectiveObjects
```

**`ModuleCat.extendScalars_adj_restrictScalars_exactness`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Injective/RestrictScalarsExactness.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/Injective/RestrictScalarsExactness.lean#L50). The attribute's comment: “adjunction and exactness”.

> **Stacks Project, Tag 03B8.**  Let `f : R →+* S` be a ring map, `u` restriction of scalars
> and `v = - ⊗_R S` extension of scalars. Then `u` is right adjoint to `v` (Mathlib's
> `ModuleCat.extendRestrictScalarsAdj`), `u` is exact and `v` is right exact.

```lean
theorem ModuleCat.extendScalars_adj_restrictScalars_exactness
    {R S : Type u} [CommRing R] [CommRing S] (f : R →+* S) :
    Nonempty (ModuleCat.extendScalars.{u, u, u} f ⊣ ModuleCat.restrictScalars.{u, u, u} f) ∧
      (PreservesFiniteLimits (ModuleCat.restrictScalars.{u, u, u} f) ∧
        PreservesFiniteColimits (ModuleCat.restrictScalars.{u, u, u} f)) ∧
      PreservesFiniteColimits (ModuleCat.extendScalars.{u, u, u} f)
```

**`ModuleCat.not_restrictScalars_preservesInjectiveObjects_intCast_zmod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Injective/RestrictScalarsExactness.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/Injective/RestrictScalarsExactness.lean#L70). The attribute's comment: “the counterexample ℤ → ℤ/pℤ”.

> **Stacks Project, Tag 03B8.**  For a prime `p` and `f : ℤ → ℤ/pℤ`, the injective
> `ℤ/pℤ`-module `ℤ/pℤ` is not an injective `ℤ`-module, so for this ring map none of the
> conditions of Stacks, Tag 015Z holds: extension of scalars does not preserve monomorphisms,
> is not exact, and restriction of scalars does not preserve injective objects.

```lean
theorem ModuleCat.not_restrictScalars_preservesInjectiveObjects_intCast_zmod
    (p : ℕ) [hp : Fact p.Prime] :
    Injective (ModuleCat.of (ZMod p) (ZMod p)) ∧
      ¬ Injective ((ModuleCat.restrictScalars.{0, 0, 0} (Int.castRingHom (ZMod p))).obj
        (ModuleCat.of (ZMod p) (ZMod p))) ∧
      ¬ (ModuleCat.extendScalars.{0, 0, 0} (Int.castRingHom (ZMod p))).PreservesMonomorphisms ∧
      ¬ (PreservesFiniteLimits (ModuleCat.extendScalars.{0, 0, 0} (Int.castRingHom (ZMod p))) ∧
        PreservesFiniteColimits (ModuleCat.extendScalars.{0, 0, 0} (Int.castRingHom (ZMod p)))) ∧
      ¬ (ModuleCat.restrictScalars.{0, 0, 0}
        (Int.castRingHom (ZMod p))).PreservesInjectiveObjects
```

**`ModuleCat.restrictScalars_extendScalars_injective_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Injective/RestrictScalarsExactness.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/Injective/RestrictScalarsExactness.lean#L104).

> **Stacks Project, Tag 03B8**, all of it.  For every ring map `f : R →+* S`, extension of
> scalars `v` is left adjoint to restriction of scalars `u`, `u` is exact, `v` is right exact, and
> `u` takes all injective `S`-modules to injective `R`-modules if and only if `f` is flat; the
> conditions of Stacks, Tag 015Z fail for `ℤ → ℤ/pℤ` with `p` prime, where `ℤ/pℤ` is an
> injective `ℤ/pℤ`-module but not an injective `ℤ`-module.

```lean
theorem ModuleCat.restrictScalars_extendScalars_injective_flat
    {R S : Type u} [CommRing R] [CommRing S] (f : R →+* S) :
    (Nonempty (ModuleCat.extendScalars.{u, u, u} f ⊣ ModuleCat.restrictScalars.{u, u, u} f) ∧
      (PreservesFiniteLimits (ModuleCat.restrictScalars.{u, u, u} f) ∧
        PreservesFiniteColimits (ModuleCat.restrictScalars.{u, u, u} f)) ∧
      PreservesFiniteColimits (ModuleCat.extendScalars.{u, u, u} f)) ∧
    (∀ (p : ℕ) [Fact p.Prime],
      Injective (ModuleCat.of (ZMod p) (ZMod p)) ∧
      ¬ Injective ((ModuleCat.restrictScalars.{0, 0, 0} (Int.castRingHom (ZMod p))).obj
        (ModuleCat.of (ZMod p) (ZMod p))) ∧
      ¬ (ModuleCat.extendScalars.{0, 0, 0} (Int.castRingHom (ZMod p))).PreservesMonomorphisms ∧
      ¬ (PreservesFiniteLimits (ModuleCat.extendScalars.{0, 0, 0} (Int.castRingHom (ZMod p))) ∧
        PreservesFiniteColimits (ModuleCat.extendScalars.{0, 0, 0} (Int.castRingHom (ZMod p)))) ∧
      ¬ (ModuleCat.restrictScalars.{0, 0, 0}
        (Int.castRingHom (ZMod p))).PreservesInjectiveObjects) ∧
    (f.Flat ↔ (ModuleCat.restrictScalars.{u, u, u} f).PreservesInjectiveObjects)
```

## Tag 0160, a lemma

[Tag 0160](https://stacks.math.columbia.edu/tag/0160) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.EnoughInjectives.of_adjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.EnoughInjectives.of_adjunction#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Preadditive/Injective/Adjunction.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/Injective/Adjunction.lean#L99) (StacksFrontier): “under v.ReflectsMonomorphisms”. References: SGA 4 V (0.2), “2)”.

## Tag 0161, a lemma

[Tag 0161](https://stacks.math.columbia.edu/tag/0161) in the Stacks Project.

**`hasFunctorialInjectiveEmbeddings_of_adjunction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Injective/Adjunction.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/Injective/Adjunction.lean#L168).

> Let `A` and `B` be abelian categories, `u : A ⥤ B` and `v : B ⥤ A` additive functors.
> Assume `u` is right adjoint to `v`, `v` transforms injective maps into injective maps, `A` has
> enough injectives, `v B = 0` implies `B = 0`, and `A` has functorial injective embeddings. Then
> `B` has functorial injective embeddings.

```lean
theorem hasFunctorialInjectiveEmbeddings_of_adjunction
    (A : Type*) [Category A] [Abelian A]
    (B : Type*) [Category B] [Abelian B]
    (u : A ⥤ B) (v : B ⥤ A)
    [u.Additive] [v.Additive]
    (adj : v ⊣ u)
    (hv_mono : ∀ {X Y : B} (f : X ⟶ Y) [Mono f], Mono (v.map f))
    [EnoughInjectives A]
    (h_reflectZero : ∀ (X : B), IsZero (v.obj X) → IsZero X)
    (hA : HasFunctorialInjectiveEmbeddings A) :
    HasFunctorialInjectiveEmbeddings B
```

## Tag 0793, a lemma

[Tag 0793](https://stacks.math.columbia.edu/tag/0793) in the Stacks Project.

**`isRightAdjoint_of_partialAdjointData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Injective/Adjunction.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/Injective/Adjunction.lean#L293).

> Let `𝒜` and `𝓑` be abelian categories, `u : 𝒜 ⥤ 𝓑` a functor, and suppose
> there is `S ⊆ Ob(𝓑)` such that every object of `𝓑` is a quotient of some
> object of `S` and, for every `P ∈ S`, the functor `A ↦ Hom_𝓑(P, u A)` is
> corepresentable. Then `u` admits a left adjoint.

```lean
theorem isRightAdjoint_of_partialAdjointData
    {A B : Type*} [Category A] [Category B] [Abelian A] [Abelian B]
    (u : A ⥤ B) (S : Set B)
    (h1 : QuotientOfFamily S)
    (h2 : PartialAdjointData u S) :
    u.IsRightAdjoint
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.29, Tag 015Y](https://stacks.math.columbia.edu/tag/015Y)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
