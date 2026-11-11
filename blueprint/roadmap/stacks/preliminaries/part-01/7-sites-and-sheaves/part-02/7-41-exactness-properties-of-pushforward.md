---
declaration: section
origin: cited
lean: exactness_properties_bundled, preservesEpi, val_app_comp_eq_on_image_arrow
statement: formalized
proof: formalized
---

# 7.41 Exactness properties of pushforward

Section 7.41 of the Stacks Project, [Tag 04D5](https://stacks.math.columbia.edu/tag/04D5). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04D6, a lemma

[Tag 04D6](https://stacks.math.columbia.edu/tag/04D6) in the Stacks Project.

**`exactness_properties_bundled`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/ExactnessOfMorphism.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topos/ExactnessOfMorphism.lean#L88). References: SGA 4 I (5.6), “iv) <=> v)”; SGA 4 I (6.4), “epic counit ⇒ ψ faithful”.

> **Stacks Tag 04D6** (abstract bundled form for an adjunction `L ⊣ R`,
> playing the role of a morphism of topoi `f⁻¹ ⊣ f_*`). Five of the eight
> sub-implications of the Stacks lemma in their topos-free formulation:
>
> * (a) (2) ⇒ (1):       `R` fully faithful implies `R` faithful;
> * (b) (3) ⇒ (1):       each component of the counit `L∘R ⟶ id` being an
>                        epimorphism implies `R` is faithful;
> * (d) (9) ⇒ (3):       if `R` reflects epimorphisms, then each component of
>                        the counit is an epimorphism (since the counit-image
>                        under `R` is split epi, hence epi);
> * (g) (9) ⇒ (8), (10): a faithful functor reflects monomorphisms (8) and
>                        bijections (10) automatically; we record (8) here, and
>                        (10) follows by combining (8) with (9);
> * (h) (7) ⇒ (2):       counit pointwise iso implies `R` fully faithful;
> * (h) (2) ⇒ (7):       `R` fully faithful implies the counit is pointwise
>                        iso.
>
> All six are immediate consequences of existing Mathlib lemmas:
> `Adjunction.faithful_R_of_epi_counit_app`, `Adjunction.counit_epi_of_R_faithful`,
> `Adjunction.fullyFaithfulROfIsIsoCounit`,
> `Adjunction.counit_isIso_of_R_fully_faithful`,
> `Functor.reflectsMonomorphisms_of_faithful`.

```lean
theorem exactness_properties_bundled :
    (R.FullyFaithful → R.Faithful) ∧
    ((∀ X, Epi (h.counit.app X)) → R.Faithful) ∧
    (R.ReflectsEpimorphisms → ∀ X, Epi (h.counit.app X)) ∧
    ((∀ X, IsIso (h.counit.app X)) → Nonempty R.FullyFaithful) ∧
    (R.FullyFaithful → ∀ X, IsIso (h.counit.app X))
```

## Tag 04D7, a lemma

[Tag 04D7](https://stacks.math.columbia.edu/tag/04D7) in the Stacks Project.

**`preservesEpi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/PreservesEpi.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topos/PreservesEpi.lean#L67).

> **Stacks 04D7.**
>
> Let `u : C ⥤ D` be a continuous functor between sites `(C, J)` and
> `(D, K)`. Assume `u` satisfies the section-lifting hypothesis of Stacks
> 04D7 (`Hypothesis u J K`): for every `K`-locally surjective morphism of
> type-valued sheaves on `(D, K)` and every section on `u(U)`, sections lift
> locally on a `J`-cover of `U`. Then the pushforward functor
> `u.sheafPushforwardContinuous (Type max u₂ v₂) J K : Sheaf K _ ⥤ Sheaf J _`
> preserves epimorphisms, i.e. transforms surjective maps of sheaves into
> surjective maps of sheaves.

```lean
theorem preservesEpi
    {C : Type u₁} [Category.{v₁} C] {D : Type u₂} [Category.{v₂} D]
    (u : C ⥤ D) (J : GrothendieckTopology C) (K : GrothendieckTopology D)
    [u.IsContinuous J K]
    (hyp : Hypothesis u J K) :
    (u.sheafPushforwardContinuous (Type max u₂ v₂) J K).PreservesEpimorphisms
```

## Tag 04D9, a lemma

[Tag 04D9](https://stacks.math.columbia.edu/tag/04D9) in the Stacks Project.

**`val_app_comp_eq_on_image_arrow`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/PushforwardEquality.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topos/PushforwardEquality.lean#L38).

> If `u_*(f) = u_*(g)`, then `f` and `g` agree after restriction along any arrow
> `u.obj U ⟶ V`, by naturality applied to a `congrArg` on objects of the form `u.obj U`.

```lean
lemma val_app_comp_eq_on_image_arrow
    [u.IsContinuous J K] {X Y : Sheaf K A} (f g : X ⟶ Y)
    (h : (u.sheafPushforwardContinuous A J K).map f =
         (u.sheafPushforwardContinuous A J K).map g)
    {V : D} {U : C} (p : u.obj U ⟶ V) :
    f.hom.app (op V) ≫ Y.obj.map p.op = g.hom.app (op V) ≫ Y.obj.map p.op
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.41, Tag 04D5](https://stacks.math.columbia.edu/tag/04D5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
