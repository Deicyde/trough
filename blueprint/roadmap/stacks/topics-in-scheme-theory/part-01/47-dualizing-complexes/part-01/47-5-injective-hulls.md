---
declaration: section
origin: cited
lean: Module.IsInjectiveHull, Module.exists_isInjectiveHull, Module.mono_of_isEssentialMono_of_comp_eq, Module.isIso_of_isInjectiveHull_of_isEssentialMono, Module.isIso_of_isInjectiveHull_of_extends_iso, Module.exists_iso_of_isInjectiveHull, Module.exists_iso_biprod_of_isInjectiveHull, CategoryTheory.Injective.factorThru
statement: formalized
proof: formalized
---

# 47.5 Injective hulls

Section 47.5 of the Stacks Project, [Tag 08Y1](https://stacks.math.columbia.edu/tag/08Y1). 9 tags here are carried by 20 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08Y2, a definition

[Tag 08Y2](https://stacks.math.columbia.edu/tag/08Y2) in the Stacks Project.

**`Module.IsInjectiveHull`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean#L80).

> An injective hull is an essential monomorphism into an injective object.

```lean
abbrev IsInjectiveHull {𝒜 : Type u} [Category.{v} 𝒜]
    [Limits.HasZeroObject 𝒜] [Limits.HasPullbacks 𝒜] {M I : 𝒜} (i : M ⟶ I) [Mono i] : Prop
```

## Tag 08Y3, a lemma

[Tag 08Y3](https://stacks.math.columbia.edu/tag/08Y3) in the Stacks Project.

**`Module.exists_isInjectiveHull`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean, line 693](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean#L693).

> Every module over a ring has an injective hull.

```lean
theorem exists_isInjectiveHull (R : Type u) [Ring R]
    (M : ModuleCat.{max v u} R) :
    ∃ (I : ModuleCat.{max v u} R) (i : M ⟶ I) (h : Mono i),
      let _ : Mono i := h
      IsInjectiveHull i
```

## Tag 08Y4, a lemma

[Tag 08Y4](https://stacks.math.columbia.edu/tag/08Y4) in the Stacks Project.

**`Module.mono_of_isEssentialMono_of_comp_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean#L165). The attribute's comment: “injective_extension”.

> A morphism which is monic on an essential subobject is a monomorphism.

```lean
theorem mono_of_isEssentialMono_of_comp_eq {C : Type u} [Category.{v} C] [Abelian C]
    {M E N J : C} (i : M ⟶ E) [Mono i] (hi : IsEssentialMono i) (φ : M ⟶ N) [Mono φ]
    (j : N ⟶ J) [Mono j] (ψ : E ⟶ J) (hψ : i ≫ ψ = φ ≫ j) : Mono ψ
```

**`Module.isIso_of_isInjectiveHull_of_isEssentialMono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean#L173). The attribute's comment: “essential_extension_iso”.

> A morphism between injective hulls which extends an essential monomorphism is an isomorphism.

```lean
theorem isIso_of_isInjectiveHull_of_isEssentialMono
    {C : Type u} [Category.{v} C] [Abelian C]
    {M E N E' : C} (i : M ⟶ E) (j : N ⟶ E')
    [Mono i] [Mono j]
    (hi : IsInjectiveHull i)
    (hj : IsInjectiveHull j)
    (phi : M ⟶ N) [Mono phi]
    (hphi : IsEssentialMono phi)
    (psi : E ⟶ E') (hpsi : i ≫ psi = phi ≫ j) :
    IsIso psi
```

**`Module.isIso_of_isInjectiveHull_of_extends_iso`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean#L197). The attribute's comment: “iso_extension”.

> A morphism between injective hulls which extends an isomorphism of the embedded modules is an
> isomorphism.

```lean
lemma isIso_of_isInjectiveHull_of_extends_iso
    {C : Type u} [Category.{v} C] [Abelian C] {M N E E' : C}
    (i : M ⟶ E) (j : N ⟶ E') [Mono i] [Mono j]
    (hi : IsInjectiveHull i)
    (hj : IsInjectiveHull j)
    (e : M ≅ N) (f : E ⟶ E')
    (comm : i ≫ f = e.hom ≫ j) :
    IsIso f
```

**`Module.exists_iso_of_isInjectiveHull`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean#L210). The attribute's comment: “unique_up_to_iso”.

> Any two injective hulls of an object are isomorphic compatibly with their embeddings of that
> object.

```lean
lemma exists_iso_of_isInjectiveHull {𝒜 : Type u} [Category.{v} 𝒜]
    [Abelian 𝒜]
    {M I J : 𝒜} (i : M ⟶ I) (j : M ⟶ J) [Mono i] [Mono j]
    (hi : IsInjectiveHull i) (hj : IsInjectiveHull j) :
    ∃ e : I ≅ J, i ≫ e.hom = j
```

**`Module.exists_iso_biprod_of_isInjectiveHull`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean#L223). The attribute's comment: “splits_in_injective”.

> An injective hull is a direct summand of any injective module containing the original module,
> compatibly with the two embeddings.

```lean
lemma exists_iso_biprod_of_isInjectiveHull
    {R : Type u} [Ring R] {M E I : ModuleCat.{v} R}
    (i : M ⟶ E) [Mono i] (hi : IsInjectiveHull i)
    (j : M ⟶ I) [Mono j] [CategoryTheory.Injective I] :
    ∃ I' : ModuleCat.{v} R, ∃ e : I ≅ E ⊞ I',
      j ≫ e.hom = i ≫ Limits.biprod.inl
```

Declarations registered for the tag:

- [`CategoryTheory.Injective.factorThru`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Injective.factorThru#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean#L158) (StacksFrontier): “extend_map”.
- [`CategoryTheory.Injective.comp_factorThru`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Injective.comp_factorThru#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean#L159) (StacksFrontier): “extend_map”.

## Tag 08Y5, an example

[Tag 08Y5](https://stacks.math.columbia.edu/tag/08Y5) in the Stacks Project.

**`Module.isInjectiveHull_fractionRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean#L247).

> The canonical inclusion of a domain into its fraction field is an injective hull.

```lean
theorem isInjectiveHull_fractionRing
    (R : Type u) [CommRing R] [IsDomain R]
    (K : Type v) [Field K] [Algebra R K] [IsFractionRing R K] :
    let M : Submodule R K := (Algebra.linearMap R K).range
    let i : ModuleCat.of R M ⟶ ModuleCat.of R K :=
      ModuleCat.ofHom M.subtype
    letI : Mono i :=
      (ModuleCat.mono_iff_injective i).2 M.injective_subtype
    IsInjectiveHull i
```

## Tag 08Y6, a definition

[Tag 08Y6](https://stacks.math.columbia.edu/tag/08Y6) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Indecomposable`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Indecomposable#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch47.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch47.lean#L22) (StacksFrontier): “for any category with zero morphisms and binary biproducts, e.g. an additive category”.

## Tag 08Y7, a lemma

[Tag 08Y7](https://stacks.math.columbia.edu/tag/08Y7) in the Stacks Project.

**`Module.Subobject.isInjectiveHull_arrow_of_indecomposable`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/IndecomposableInjective.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/IndecomposableInjective.lean#L78). The attribute's comment: “injective_hull”.

> The inclusion of any nonzero submodule of an indecomposable injective module exhibits the
> ambient module as its injective hull.

```lean
lemma Subobject.isInjectiveHull_arrow_of_indecomposable
    (R : Type u) [Ring R] (E : ModuleCat.{v} R) [CategoryTheory.Injective E]
    (hE : Indecomposable E) (M : Subobject E) (hM : M ≠ ⊥) :
    IsInjectiveHull M.arrow
```

**`Module.Subobject.inf_ne_bot_of_indecomposable_injective`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/IndecomposableInjective.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/IndecomposableInjective.lean#L124). The attribute's comment: “nonzero_intersection”.

> Two nonzero submodules of an indecomposable injective module have nonzero intersection.

```lean
lemma Subobject.inf_ne_bot_of_indecomposable_injective (R : Type u) [Ring R]
    (E : ModuleCat.{v} R) [CategoryTheory.Injective E] (hE : Indecomposable E)
    (A B : Subobject E) (hA : A ≠ ⊥) (hB : B ≠ ⊥) : A ⊓ B ≠ ⊥
```

**`Module.endomorphismRing_isLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/IndecomposableInjective.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/IndecomposableInjective.lean#L220). The attribute's comment: “endomorphism_ring_local”.

> The endomorphism ring of an indecomposable injective module is a (possibly
> noncommutative) local ring.

```lean
theorem endomorphismRing_isLocalRing
    {R : Type u} {E : Type v} [CommRing R] [AddCommGroup E] [Module R E]
    [Module.Injective R E]
    (hE : Indecomposable (ModuleCat.of R E)) :
    IsLocalRing (Module.End R E)
```

**`Module.exists_maximalIdeal_endomorphismRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/IndecomposableInjective.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/IndecomposableInjective.lean#L247). The attribute's comment: “endomorphism_ring_local”.

> The maximal two-sided ideal of the endomorphism ring consists exactly of the
> endomorphisms with nonzero kernel, and every endomorphism outside it is invertible.

```lean
theorem exists_maximalIdeal_endomorphismRing
    {R : Type u} {E : Type v} [CommRing R] [AddCommGroup E] [Module R E]
    [Module.Injective R E]
    (hE : Indecomposable (ModuleCat.of R E)) :
    ∃ I : Ideal (Module.End R E), I.IsTwoSided ∧ I.IsMaximal ∧
      (∀ φ : Module.End R E, φ ∈ I ↔ LinearMap.ker φ ≠ ⊥) ∧
      (∀ φ : Module.End R E, φ ∉ I → IsUnit φ)
```

**`Module.exists_prime_eq_zeroDivisorsOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/IndecomposableInjective.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/IndecomposableInjective.lean#L311). The attribute's comment: “zero_divisors_prime”.

> The set of zerodivisors on an indecomposable injective module is the underlying set of a prime
> ideal.

```lean
theorem exists_prime_eq_zeroDivisorsOn {R : Type u} [CommRing R]
    (E : ModuleCat.{v} R) [CategoryTheory.Injective E] (hE : Indecomposable E) :
    ∃ p : Ideal R, p.IsPrime ∧ (p : Set R) = {r : R | ∃ m : E, m ≠ 0 ∧ r • m = 0}
```

**`Module.exists_injective_localizationAtPrime_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/IndecomposableInjective.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/IndecomposableInjective.lean#L331). The attribute's comment: “injective_over_localization”.

> An indecomposable injective module is an injective module over the localization at its prime
> ideal of zerodivisors.

```lean
theorem exists_injective_localizationAtPrime_module
    {R : Type u} [CommRing R] (E : ModuleCat.{v} R) [CategoryTheory.Injective E]
    (hE : Indecomposable E) (p : Ideal R) (hp : p.IsPrime)
    (hpE : (p : Set R) = {r : R | ∃ m : E, m ≠ 0 ∧ r • m = 0}) :
    ∃ moduleStructure : Module (Localization.AtPrime p) E,
      letI := moduleStructure
      (∀ (r : R) (x : E), algebraMap R (Localization.AtPrime p) r • x = r • x) ∧
        CategoryTheory.Injective (ModuleCat.of (Localization.AtPrime p) E)
```

## Tag 08Y8, a lemma

[Tag 08Y8](https://stacks.math.columbia.edu/tag/08Y8) in the Stacks Project.

**`Module.exists_isInjectiveHull_residueField_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/DirectSumDecomposition.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/DirectSumDecomposition.lean#L300). The attribute's comment: “localized_hull”.

> The injective hull of `R ⧸ p` is naturally an injective hull of the residue field at `p` over
> `Rₚ`.

```lean
theorem exists_isInjectiveHull_residueField_localization
    {R : Type u} [CommRing R] (p : Ideal R) [p.IsPrime]
    (E : ModuleCat.{u} R) (i : ModuleCat.of R (R ⧸ p) ⟶ E) [Mono i]
    (hi : IsInjectiveHull i) :
    ∃ moduleStructure : Module (Localization.AtPrime p) E,
      letI := moduleStructure
      ∃ tower : IsScalarTower R (Localization.AtPrime p) E,
        letI := tower
        ∃ j : ModuleCat.of (Localization.AtPrime p) p.ResidueField ⟶
            ModuleCat.of (Localization.AtPrime p) E,
          ∃ monoJ : Mono j,
            letI := monoJ
            ModuleCat.ofHom
                ((LinearMap.restrictScalars R j.hom).comp
                  (LinearMap.restrictScalars R
                    (Algebra.linearMap (R ⧸ p) p.ResidueField))) = i ∧
              IsInjectiveHull j
```

**`Module.exists_isInjectiveHull_residueField_of_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean#L296). The attribute's comment: “hull_of_residue_field”.

> An injective hull of the quotient by a prime ideal is also an injective hull of the prime's
> residue field.

```lean
theorem exists_isInjectiveHull_residueField_of_quotient
    (R : Type u) [CommRing R] (p : Ideal R) [p.IsPrime]
    (E : ModuleCat.{max u v} R)
    (i : ModuleCat.of R (ULift.{v} (R ⧸ p)) ⟶ E) [Mono i]
    (hi : IsInjectiveHull i) :
    ∃ (j : ModuleCat.of R (ULift.{v} p.ResidueField) ⟶ E) (_ : Mono j),
      IsInjectiveHull j
```

**`Module.indecomposable_of_isInjectiveHull_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/IndecomposableInjective.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/IndecomposableInjective.lean#L406). The attribute's comment: “indecomposable”.

> The injective hull of the quotient by a prime ideal is indecomposable.

```lean
theorem indecomposable_of_isInjectiveHull_quotient
    {R : Type u} [CommRing R] (p : Ideal R) [p.IsPrime]
    {E : ModuleCat.{max v u} R}
    (i : ModuleCat.of R (ULift.{v} (R ⧸ p)) ⟶ E) [Mono i]
    (hi : IsInjectiveHull i) : Indecomposable E
```

## Tag 08Y9, a lemma

[Tag 08Y9](https://stacks.math.columbia.edu/tag/08Y9) in the Stacks Project.

**`Module.exists_isInjectiveHull_residueField_of_indecomposable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/IndecomposableInjective.lean, line 502](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/IndecomposableInjective.lean#L502).

> An indecomposable injective module over a Noetherian ring is an injective hull of the residue
> field at some prime ideal.

```lean
theorem exists_isInjectiveHull_residueField_of_indecomposable
    (R : Type u) [CommRing R] [IsNoetherianRing R]
    (E : ModuleCat.{v} R) [CategoryTheory.Injective E] (hE : Indecomposable E) :
    ∃ (p : PrimeSpectrum R) (K : ModuleCat.{v} R),
      Nonempty (K ≃ₗ[R] p.asIdeal.ResidueField) ∧
        ∃ (i : K ⟶ E) (_ : Mono i), IsInjectiveHull i
```

## Tag 08YA, a proposition

[Tag 08YA](https://stacks.math.columbia.edu/tag/08YA) in the Stacks Project.

**`Module.exists_iso_directSum_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/DirectSumDecomposition.lean, line 646](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/DirectSumDecomposition.lean#L646). The attribute's comment: “direct sum decomposition”.

> An injective module over a Noetherian ring is isomorphic to a direct sum of indecomposable
> injective modules.

```lean
theorem exists_iso_directSum_of_injective
    (R : Type u) [CommRing R] [IsNoetherianRing R]
    (I : ModuleCat.{v} R) [CategoryTheory.Injective I] :
    ∃ (ι : Type v) (E : ι → ModuleCat.{v} R)
      (_ : I ≅ ModuleCat.of R (⨁ i, E i)),
      (∀ i, CategoryTheory.Injective (E i)) ∧ (∀ i, Indecomposable (E i))
```

**`Module.exists_residueField_injectiveHull`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/DirectSumDecomposition.lean, line 744](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/InjectiveHull/Basic/DirectSumDecomposition.lean#L744). The attribute's comment: “indecomposable injective modules”.

> An indecomposable injective module over a Noetherian ring is an injective hull of the residue
> field at a prime ideal.

```lean
theorem exists_residueField_injectiveHull
    (R : Type u) [CommRing R] [IsNoetherianRing R]
    (E : ModuleCat.{v} R) [CategoryTheory.Injective E] (hE : Indecomposable E) :
    ∃ (p : Ideal R) (hp : p.IsPrime),
      letI := hp
      ∃ (K : ModuleCat.{v} R) (_ : K ≃ₗ[R] p.ResidueField)
        (i : K ⟶ E) (hi : Mono i),
        letI := hi
        IsInjectiveHull i
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.5, Tag 08Y1](https://stacks.math.columbia.edu/tag/08Y1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
