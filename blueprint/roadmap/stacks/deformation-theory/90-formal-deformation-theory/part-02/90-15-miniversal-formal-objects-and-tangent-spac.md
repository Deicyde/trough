---
declaration: section
origin: cited
lean: Deformation.HasBijectiveDifferential, Deformation.HasBijectiveDifferentialOnDerivationOrbits, Deformation.hasBijectiveDifferentialOnDerivationOrbits_of_hasBijectiveDifferential, Deformation.minimalVersal_hasBijectiveDifferentialOnDerivationOrbits, Deformation.isMinimalVersal_of_hasBijectiveDifferentialOnDerivationOrbits, Deformation.isomorphic_of_hasBijectiveDifferentialOnDerivationOrbits, Deformation.schlessingerConditionS1_of_versal_bijectiveDifferential, Deformation.schlessingerConditionS2_of_versal_bijectiveDifferential
statement: formalized
proof: formalized
---

# 90.15 Miniversal formal objects and tangent spaces

Section 90.15 of the Stacks Project, [Tag 06IL](https://stacks.math.columbia.edu/tag/06IL). 10 tags here are carried by 31 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06IM, an equation

[Tag 06IM](https://stacks.math.columbia.edu/tag/06IM) in the Stacks Project.

**`Deformation.HasBijectiveDifferential`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/BijectiveDifferential.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/BijectiveDifferential.lean#L98).

> **Stacks Project, Tag 06IM.** The differential of the morphism associated
> to a formal object is bijective from `Λ`-derivations to its tangent space.

```lean
public def HasBijectiveDifferential
    (hp : Deformation.IsCofiberedInGroupoids p)
    (ξ : Deformation.FormalObject p) : Prop
```

## Tag 06T6, an equation

[Tag 06T6](https://stacks.math.columbia.edu/tag/06T6) in the Stacks Project.

**`Deformation.HasBijectiveDifferentialOnDerivationOrbits`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/DerivationOrbits.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/FormalObject/DerivationOrbits.lean#L101). The attribute's comment: “the condition, as a predicate on formal objects”.

> **Stacks Project, Tag 06T6,** the condition itself. The differential of a formal object is a
> well-defined, equivariant map from derivations of its underlying algebra to the tangent space,
> surjective on tangent vectors, and bijective after passing to `Der_Λ(k, k)`-orbits on both
> sides. That this holds for a minimal versal formal object is Stacks 06T8,
> `Deformation.minimalVersal_hasBijectiveDifferentialOnDerivationOrbits`.

```lean
public noncomputable def HasBijectiveDifferentialOnDerivationOrbits
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : IsPredeformationCategory p) (ξ : FormalObject p) : Prop
```

**`Deformation.hasBijectiveDifferentialOnDerivationOrbits_of_hasBijectiveDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/DerivationOrbitsOfBijective.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/FormalObject/DerivationOrbitsOfBijective.lean#L61). The attribute's comment: “the condition holds for a formal object with bijective differential”.

> **Stacks Project, Tag 06T6.** The condition holds for a formal object whose differential is
> bijective: the differential of such an object is a well-defined, equivariant and surjective map
> from derivations of its underlying complete local algebra to the tangent space, and it is
> bijective on `Der_Λ(k, k)`-orbits.

```lean
public theorem hasBijectiveDifferentialOnDerivationOrbits_of_hasBijectiveDifferential
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : IsPredeformationCategory p) (ξ : FormalObject p)
    (hbij : HasBijectiveDifferential hp.cofibered ξ) :
    HasBijectiveDifferentialOnDerivationOrbits.{u, v, w} p hp ξ
```

**`Deformation.minimalVersal_hasBijectiveDifferentialOnDerivationOrbits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/VersalObject/MinimalVersalOrbitBijection.lean, line 703](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/VersalObject/MinimalVersalOrbitBijection.lean#L703). The attribute's comment: “the condition holds for a minimal versal formal object”.

> The differential of a minimal versal formal object of a predeformation category satisfying
> Schlessinger's condition (S2) is well defined, surjective and equivariant, and induces a
> bijection on `Der_Λ(k, k)`-orbits.

```lean
public theorem minimalVersal_hasBijectiveDifferentialOnDerivationOrbits
    [IsNoetherianRing Λ] [Module.Finite Λ k]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : IsPredeformationCategory p)
    (hS2 : SchlessingerConditionS2 p)
    (ξ : FormalObject p)
    (hξ : IsMinimalVersal hp.cofibered ξ) :
    HasBijectiveDifferentialOnDerivationOrbits.{u, v, w} p hp ξ
```

## Tag 06IR, a lemma

[Tag 06IR](https://stacks.math.columbia.edu/tag/06IR) in the Stacks Project.

**`Deformation.isMinimalVersal_of_hasBijectiveDifferentialOnDerivationOrbits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/VersalObject/DerivationOrbitCriterion.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Formal/VersalObject/DerivationOrbitCriterion.lean#L146). The attribute's comment: “minimality”.

> A versal formal object of a predeformation category whose
> differential is bijective on derivation orbits is a minimal versal formal object.

```lean
public theorem isMinimalVersal_of_hasBijectiveDifferentialOnDerivationOrbits
    (hp : IsPredeformationCategory p) (ξ : FormalObject p) (hξ : IsVersal hp.cofibered ξ)
    (hd : HasBijectiveDifferentialOnDerivationOrbits.{u, v, w} p hp ξ) :
    IsMinimalVersal hp.cofibered ξ
```

**`Deformation.isomorphic_of_hasBijectiveDifferentialOnDerivationOrbits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/VersalObject/DerivationOrbitCriterion.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Formal/VersalObject/DerivationOrbitCriterion.lean#L212). The attribute's comment: “uniqueness”. References: SGA 7 VI (1.20), “uniqueness”.

> Any two versal formal objects whose differentials are bijective on derivation orbits are
> isomorphic.

```lean
public theorem isomorphic_of_hasBijectiveDifferentialOnDerivationOrbits
    (hp : IsPredeformationCategory p) (ξ η : FormalObject p)
    (hξ : IsVersal hp.cofibered ξ) (hη : IsVersal hp.cofibered η)
    (hdξ : HasBijectiveDifferentialOnDerivationOrbits.{u, v, w} p hp ξ)
    (hdη : HasBijectiveDifferentialOnDerivationOrbits.{u, v, w} p hp η) :
    Nonempty (ξ ≅ η)
```

## Tag 06IV, a lemma

[Tag 06IV](https://stacks.math.columbia.edu/tag/06IV) in the Stacks Project.

**`Deformation.schlessingerConditionS1_of_versal_bijectiveDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/VersalBijectiveDifferential.lean, line 410](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Schlessinger/VersalBijectiveDifferential.lean#L410). The attribute's comment: “part (1): condition (S1)”.

> A versal formal object with bijective differential forces Schlessinger's
> condition (S1). The bijectivity of the differential is not used.

```lean
public theorem schlessingerConditionS1_of_versal_bijectiveDifferential
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type uF} [Category.{vF} F]
    (p : F ⥤ Deformation.ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : Deformation.IsPredeformationCategory p)
    (ξ : Deformation.FormalObject p)
    (hversal : Deformation.IsVersal hp.cofibered ξ)
    (_hbij : Deformation.HasBijectiveDifferential hp.cofibered ξ) :
    Deformation.SchlessingerConditionS1 p
```

**`Deformation.schlessingerConditionS2_of_versal_bijectiveDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/VersalBijectiveDifferential.lean, line 424](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Schlessinger/VersalBijectiveDifferential.lean#L424). The attribute's comment: “part (2): condition (S2)”.

> A versal formal object with bijective differential forces Schlessinger's
> condition (S2).

```lean
public theorem schlessingerConditionS2_of_versal_bijectiveDifferential
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type uF} [Category.{vF} F]
    (p : F ⥤ Deformation.ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : Deformation.IsPredeformationCategory p)
    (ξ : Deformation.FormalObject p)
    (hversal : Deformation.IsVersal hp.cofibered ξ)
    (hbij : Deformation.HasBijectiveDifferential hp.cofibered ξ) :
    Deformation.SchlessingerConditionS2 p
```

**`Deformation.finiteDimensional_tangentSpace_of_versal_bijectiveDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/VersalBijectiveDifferential.lean, line 729](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Schlessinger/VersalBijectiveDifferential.lean#L729). The attribute's comment: “part (3): finite-dimensional tangent space”.

> A versal formal object with bijective differential has a
> finite-dimensional tangent space.

```lean
public theorem finiteDimensional_tangentSpace_of_versal_bijectiveDifferential
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    [Module.Finite Λ k]
    (𝓕 : BasedCategory.{vF, uF} (Deformation.ArtinianLocalAlgCat.{u, max v w, w} Λ k))
    (hp : Deformation.IsPredeformationCategory 𝓕.p)
    (ξ : Deformation.FormalObject 𝓕.p)
    (hversal : Deformation.IsVersal hp.cofibered ξ)
    (hbij : Deformation.HasBijectiveDifferential hp.cofibered ξ) :
    let hS2 := schlessingerConditionS2_of_versal_bijectiveDifferential
      𝓕.p hp ξ hversal hbij
    let hAssocS2 :=
      Deformation.schlessingerConditionS2_of_isIsomorphismClasses
        𝓕 hp.cofibered hS2 (Or.inl hp)
    letI : Fact (Deformation.IsPredeformationCategory 𝓕.p) := ⟨hp⟩
    letI : Fact (Deformation.SchlessingerConditionS2
      (Functor.Elements.π (Deformation.isomorphismClasses 𝓕 hp.cofibered))) :=
      ⟨hAssocS2⟩
    FiniteDimensional k
      (Deformation.tangentSpaceArtinian Λ k
        (Deformation.isomorphismClasses 𝓕 hp.cofibered))
```

Declarations registered for the tag:

- [`Deformation.schlessingerConditionS1_of_versal`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Schlessinger/Basic.lean#L788), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/Schlessinger/VersalBijectiveDifferential.lean, line 405](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Schlessinger/VersalBijectiveDifferential.lean#L405) (StacksFrontier): “part (1): condition (S1)”.

## Tag 06T7, an example

[Tag 06T7](https://stacks.math.columbia.edu/tag/06T7) in the Stacks Project.

**`Deformation.exists_versal_orbitBijective_not_schlessingerConditionS2`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/OrbitBijectivityWarning.lean, line 772](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/FormalObject/OrbitBijectivityWarning.lean#L772).

> There is a predeformation category carrying a versal formal object whose differential is
> bijective on `Der_Λ(k, k)`-orbits and which does not satisfy Schlessinger's condition (S2).

```lean
theorem exists_versal_orbitBijective_not_schlessingerConditionS2 :
    ∃ (B : BasedCategory.{0, 1} (ArtinianLocalAlgCat.{0, 0, 0} Lam Kay))
      (hp : IsPredeformationCategory.{0, 0, 0} B.p) (ksi : FormalObject B.p),
      IsVersal hp.cofibered ksi ∧
        HasBijectiveDifferentialOnDerivationOrbits.{0, 0, 0} B.p hp ksi ∧
          ¬ SchlessingerConditionS2 B.p
```

## Tag 06T8, a lemma

[Tag 06T8](https://stacks.math.columbia.edu/tag/06T8) in the Stacks Project.

**`Deformation.minimalVersal_hasBijectiveDifferentialOnDerivationOrbits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/VersalObject/MinimalVersalOrbitBijection.lean, line 703](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/VersalObject/MinimalVersalOrbitBijection.lean#L703).

> The differential of a minimal versal formal object of a predeformation category satisfying
> Schlessinger's condition (S2) is well defined, surjective and equivariant, and induces a
> bijection on `Der_Λ(k, k)`-orbits.

```lean
public theorem minimalVersal_hasBijectiveDifferentialOnDerivationOrbits
    [IsNoetherianRing Λ] [Module.Finite Λ k]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : IsPredeformationCategory p)
    (hS2 : SchlessingerConditionS2 p)
    (ξ : FormalObject p)
    (hξ : IsMinimalVersal hp.cofibered ξ) :
    HasBijectiveDifferentialOnDerivationOrbits.{u, v, w} p hp ξ
```

## Tag 06IX, a theorem

[Tag 06IX](https://stacks.math.columbia.edu/tag/06IX) in the Stacks Project.

**`Deformation.schlessingerConditionS1_of_minimalVersal_hasBijectiveDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/DerivationOrbits.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/FormalObject/DerivationOrbits.lean#L123). The attribute's comment: “(1) implies (3a)”.

> **Stacks Project, Tag 06IX,** the implication (1) ⟹ (3a). Condition (1) of that theorem is
> that the predeformation category have a minimal versal formal object whose differential is
> bijective, Stacks 06IM; condition (3a) is Schlessinger's condition (S1). Neither the minimality
> nor the bijectivity of the differential is used: versality alone gives (S1), by Stacks 06SY.

```lean
public theorem schlessingerConditionS1_of_minimalVersal_hasBijectiveDifferential
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : IsPredeformationCategory p)
    (hξ : ∃ ξ : FormalObject p,
      IsMinimalVersal hp.cofibered ξ ∧ HasBijectiveDifferential hp.cofibered ξ) :
    SchlessingerConditionS1 p
```

**`Deformation.exists_minimalVersal_hasBijectiveDifferentialOnDerivationOrbits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/MiniversalExistence.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Schlessinger/MiniversalExistence.lean#L44). The attribute's comment: “(3) implies (2)”. References: SGA 7 VI (1.11), “(i)”; SGA 7 VI (1.20), “special case”.

> A predeformation category satisfying Schlessinger's conditions (S1) and (S2) whose tangent
> space is finite dimensional has a minimal versal formal object whose differential is bijective
> on `Der_Λ(k, k)`-orbits.

```lean
public theorem exists_minimalVersal_hasBijectiveDifferentialOnDerivationOrbits
    (Λ : Type u) (k : Type w) [CommRing Λ] [IsNoetherianRing Λ] [Field k] [Algebra Λ k]
    [Module.Finite Λ k]
    (𝓕 : BasedCategory.{vF, uF} (ArtinianLocalAlgCat.{u, max v w, w} Λ k))
    (hpre : IsPredeformationCategory.{u, v, w} 𝓕.p)
    (hS1 : SchlessingerConditionS1 𝓕.p)
    (hS2 : SchlessingerConditionS2 𝓕.p)
    (hfin :
      letI : Fact (IsPredeformationCategory.{u, v, w} 𝓕.p) := ⟨hpre⟩
      letI : Fact (SchlessingerConditionS2
          (Functor.Elements.π (isomorphismClasses 𝓕 hpre.cofibered))) :=
        ⟨schlessingerConditionS2_of_isIsomorphismClasses 𝓕 hpre.cofibered hS2 (Or.inl hpre)⟩
      FiniteDimensional k (tangentSpaceArtinian.{u, w, v} Λ k
        (isomorphismClasses 𝓕 hpre.cofibered))) :
    ∃ ξ : FormalObject 𝓕.p,
      IsMinimalVersal hpre.cofibered ξ ∧
        HasBijectiveDifferentialOnDerivationOrbits.{u, v, w} 𝓕.p hpre ξ
```

**`Deformation.schlessingerConditionS2_of_minimalVersal_hasBijectiveDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/MiniversalSeparable.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Schlessinger/MiniversalSeparable.lean#L149). The attribute's comment: “(1) implies (3b)”.

> **Stacks Project, Tag 06IX,** the implication (1) implies (3b). A predeformation category
> with a minimal versal formal object whose differential is bijective — that is, one satisfying
> the condition of Stacks 06IM — satisfies Schlessinger's condition (S2).
>
> This is part (2) of Stacks 06IV, which asks only for versality, restated under the hypothesis
> (1) of Stacks 06IX.

```lean
public theorem schlessingerConditionS2_of_minimalVersal_hasBijectiveDifferential
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (𝓕 : BasedCategory.{vF, uF} (Deformation.ArtinianLocalAlgCat.{u, max v w, w} Λ k))
    (hpre : Deformation.IsPredeformationCategory 𝓕.p)
    (hξ : ∃ ξ : Deformation.FormalObject 𝓕.p,
      Deformation.IsMinimalVersal hpre.cofibered ξ ∧
        Deformation.HasBijectiveDifferential hpre.cofibered ξ) :
    Deformation.SchlessingerConditionS2 𝓕.p
```

**`Deformation.finiteDimensional_tangentSpace_of_minimalVersal_hasBijectiveDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/MiniversalSeparable.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Schlessinger/MiniversalSeparable.lean#L172). The attribute's comment: “(1) implies (3c)”. References: SGA 7 VI (1.11), “(ii)”.

> **Stacks Project, Tag 06IX,** the implication (1) implies (3c). The tangent space of a
> predeformation category with a minimal versal formal object whose differential is bijective —
> that is, one satisfying the condition of Stacks 06IM — is finite dimensional.
>
> This is part (3) of Stacks 06IV, which asks only for versality, restated under the hypothesis
> (1) of Stacks 06IX. The canonical `k`-vector-space structure of Stacks 06IH on the tangent
> space needs the predeformation property of `𝓕` and condition (S2) for its functor of
> isomorphism classes; the first is `hpre` and the second comes from
> `Deformation.schlessingerConditionS2_of_minimalVersal_hasBijectiveDifferential`, the
> implication (1) implies (3b), so both are installed by the `letI` prefix of the conclusion and
> neither is assumed.

```lean
public theorem finiteDimensional_tangentSpace_of_minimalVersal_hasBijectiveDifferential
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k] [Module.Finite Λ k]
    (𝓕 : BasedCategory.{vF, uF} (Deformation.ArtinianLocalAlgCat.{u, max v w, w} Λ k))
    (hpre : Deformation.IsPredeformationCategory 𝓕.p)
    (hξ : ∃ ξ : Deformation.FormalObject 𝓕.p,
      Deformation.IsMinimalVersal hpre.cofibered ξ ∧
        Deformation.HasBijectiveDifferential hpre.cofibered ξ) :
    letI : Fact (Deformation.IsPredeformationCategory 𝓕.p) := ⟨hpre⟩
    letI : Fact (Deformation.SchlessingerConditionS2 (Functor.Elements.π
        (Deformation.isomorphismClasses 𝓕 hpre.cofibered))) :=
      ⟨Deformation.schlessingerConditionS2_of_isIsomorphismClasses 𝓕 hpre.cofibered
        (schlessingerConditionS2_of_minimalVersal_hasBijectiveDifferential 𝓕 hpre hξ)
        (Or.inl hpre)⟩
    FiniteDimensional k
      (Deformation.tangentSpaceArtinian Λ k
        (Deformation.isomorphismClasses 𝓕 hpre.cofibered))
```

**`Deformation.exists_minimalVersal_hasBijectiveDifferential_of_separable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/MiniversalSeparable.lean, line 379](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Schlessinger/MiniversalSeparable.lean#L379). The attribute's comment: “(2) implies (1) under separability”.

> If `k` is separable over the image field of `Λ`, orbitwise bijectivity
> of a minimal versal formal object's differential is ordinary bijectivity.

```lean
public theorem exists_minimalVersal_hasBijectiveDifferential_of_separable
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    [Algebra.IsSeparable (Deformation.residueImageField Λ k) k]
    (𝓕 : BasedCategory.{vF, uF} (Deformation.ArtinianLocalAlgCat.{u, max v w, w} Λ k))
    (hpre : Deformation.IsPredeformationCategory 𝓕.p)
    (hξ : ∃ ξ : Deformation.FormalObject 𝓕.p,
      Deformation.IsMinimalVersal hpre.cofibered ξ ∧
        Deformation.HasBijectiveDifferentialOnDerivationOrbits 𝓕.p hpre ξ) :
    ∃ ξ : Deformation.FormalObject 𝓕.p,
      Deformation.IsMinimalVersal hpre.cofibered ξ ∧
        Deformation.HasBijectiveDifferential hpre.cofibered ξ
```

Declarations registered for the tag:

- [`Deformation.schlessingerConditionS1_of_versal`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Schlessinger/Basic.lean#L788), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/FormalObject/DerivationOrbits.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/FormalObject/DerivationOrbits.lean#L137) (StacksFrontier): “(1) implies (3a)”.
- [`Deformation.schlessingerConditionS2_of_versal_bijectiveDifferential`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Schlessinger/VersalBijectiveDifferential.lean#L424), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/Schlessinger/MiniversalSeparable.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Schlessinger/MiniversalSeparable.lean#L192) (StacksFrontier): “(1) implies (3b)”.
- [`Deformation.finiteDimensional_tangentSpace_of_versal_bijectiveDifferential`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Schlessinger/VersalBijectiveDifferential.lean#L729), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/Schlessinger/MiniversalSeparable.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Schlessinger/MiniversalSeparable.lean#L194) (StacksFrontier): “(1) implies (3c)”.

## Tag 06IY, a remark

[Tag 06IY](https://stacks.math.columbia.edu/tag/06IY) in the Stacks Project.

**`Deformation.IsHull`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/VersalObject/IsomorphismClassesHull.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Formal/VersalObject/IsomorphismClassesHull.lean#L43). The attribute's comment: “hull”.

> A *hull* of a category cofibered in groupoids over `𝒞_Λ` is a versal formal object whose
> differential `dξ : T\underline{R}|_{𝒞_Λ} → T𝓕` is an isomorphism.

```lean
public abbrev IsHull {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type uF} [Category.{vF} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k}
    (hp : IsCofiberedInGroupoids p) (ξ : FormalObject p) : Prop
```

**`Deformation.exists_hull_of_schlessingerConditions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/SetValuedExistence.lean, line 359](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Schlessinger/SetValuedExistence.lean#L359). The attribute's comment: “(H1) + (H2) + (H3) implies a hull exists”. References: SGA 7 VI (1.20), “set-valued functor”.

> **Stacks Project, Tag 06IY.** A set-valued predeformation functor on `𝒞_Λ` satisfying
> Schlessinger's conditions (H1), (H2) and (H3) has a hull, provided `k` is separable over the
> image field of `Λ`: a versal formal object whose differential is an isomorphism.
>
> This is Schlessinger's theorem on the existence of hulls. It is Stacks 06IX read through the
> identifications of Stacks 06GT and 06HY, exactly as
> `Deformation.exists_versalFormalObject_of_schlessingerConditions` is Stacks 06IW, and (H3) is
> stated and discharged in the same way: about `TF = F(k[ε])` itself, transported inside the
> proof by `Deformation.finiteDimensional_tangentSpace_isomorphismClasses_of_setValued`.

```lean
public theorem exists_hull_of_schlessingerConditions
    (Λ : Type u) (k : Type w) [CommRing Λ] [IsNoetherianRing Λ] [Field k] [Algebra Λ k]
    [Module.Finite Λ k] [Algebra.IsSeparable (residueImageField Λ k) k]
    (F : ArtinianLocalAlgCat.{u, max v w, w} Λ k ⥤ Type t)
    (hpre : IsPredeformationFunctor.{u, v, w, t} F)
    (hH1 : ∀ ⦃A₁ A₂ A A₁₂ : ArtinianLocalAlgCat.{u, max v w, w} Λ k⦄
      (f₁ : A₁ ⟶ A) (f₂ : A₂ ⟶ A), Function.Surjective f₂.hom →
        ∀ (g₁ : A₁₂ ⟶ A₁) (g₂ : A₁₂ ⟶ A₂) (hPB : IsPullback g₂ g₁ f₂ f₁),
          Function.Surjective (fibreProductComparison F g₁ g₂ f₁ f₂ hPB.w))
    (hH2 : ∀ ⦃A A₀ Aε B : ArtinianLocalAlgCat.{u, max v w, w} Λ k⦄
      (d : A ⟶ A₀) (e : Aε ⟶ A₀), IsDualNumberProjection e →
        ∀ (g : B ⟶ A) (gε : B ⟶ Aε) (hPB : IsPullback gε g e d),
          Function.Bijective (fibreProductComparison F g gε d e hPB.w))
    (hH3 :
      letI : Fact (IsPredeformationCategory.{u, v, w}
          (BasedCategory.ofFunctor (Elements.π F)).p) :=
        ⟨(isPredeformationCategory_iff F).2 hpre⟩
      letI : Fact (SchlessingerConditionS2 (Elements.π
          (isomorphismClasses (BasedCategory.ofFunctor (Elements.π F))
            ((isPredeformationCategory_iff F).2 hpre).cofibered))) :=
        ⟨schlessingerConditionS2_of_isIsomorphismClasses
          (BasedCategory.ofFunctor (Elements.π F))
          ((isPredeformationCategory_iff F).2 hpre).cofibered
          ((schlessingerConditionS2_elements_iff F).2 hH2)
          (Or.inl ((isPredeformationCategory_iff F).2 hpre))⟩
      letI := setValuedTangentSpaceAddCommGroup.{u, v, w, t} F
        ((isPredeformationCategory_iff F).2 hpre)
      letI := setValuedTangentSpaceModule.{u, v, w, t} F
        ((isPredeformationCategory_iff F).2 hpre)
      FiniteDimensional k (tangentSpaceArtinian.{u, w, v} Λ k F)) :
    ∃ ξ : FormalObject (Elements.π F),
      IsHull ((isPredeformationCategory_iff F).2 hpre).cofibered ξ
```

**`Deformation.exists_hull_of_schlessingerConditions_isClassical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/SetValuedExistence.lean, line 415](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Schlessinger/SetValuedExistence.lean#L415). The attribute's comment: “(H1) + (H2) + (H3) implies a hull exists, classical case”. References: SGA 7 VI (1.20), “special case”.

> **Stacks Project, Tag 06IY.** In the classical case — `Λ` a Noetherian complete local ring
> whose residue field is identified with `k` — a set-valued predeformation functor satisfying
> Schlessinger's conditions (H1), (H2) and (H3) has a hull.
>
> A classical base satisfies the three standing hypotheses of
> `Deformation.exists_hull_of_schlessingerConditions`: it is Noetherian, `k` is a finite
> `Λ`-module, and `k` is separable over the image field of `Λ` because that image field is all
> of `k`.

```lean
public theorem exists_hull_of_schlessingerConditions_isClassical
    (Λ : Type u) (k : Type w) [CommRing Λ] [Field k] [Algebra Λ k] (hΛ : IsClassical Λ k)
    (F : ArtinianLocalAlgCat.{u, max v w, w} Λ k ⥤ Type t)
    (hpre : IsPredeformationFunctor.{u, v, w, t} F)
    (hH1 : ∀ ⦃A₁ A₂ A A₁₂ : ArtinianLocalAlgCat.{u, max v w, w} Λ k⦄
      (f₁ : A₁ ⟶ A) (f₂ : A₂ ⟶ A), Function.Surjective f₂.hom →
        ∀ (g₁ : A₁₂ ⟶ A₁) (g₂ : A₁₂ ⟶ A₂) (hPB : IsPullback g₂ g₁ f₂ f₁),
          Function.Surjective (fibreProductComparison F g₁ g₂ f₁ f₂ hPB.w))
    (hH2 : ∀ ⦃A A₀ Aε B : ArtinianLocalAlgCat.{u, max v w, w} Λ k⦄
      (d : A ⟶ A₀) (e : Aε ⟶ A₀), IsDualNumberProjection e →
        ∀ (g : B ⟶ A) (gε : B ⟶ Aε) (hPB : IsPullback gε g e d),
          Function.Bijective (fibreProductComparison F g gε d e hPB.w))
    (hH3 :
      letI : Fact (IsPredeformationCategory.{u, v, w}
          (BasedCategory.ofFunctor (Elements.π F)).p) :=
        ⟨(isPredeformationCategory_iff F).2 hpre⟩
      letI : Fact (SchlessingerConditionS2 (Elements.π
          (isomorphismClasses (BasedCategory.ofFunctor (Elements.π F))
            ((isPredeformationCategory_iff F).2 hpre).cofibered))) :=
        ⟨schlessingerConditionS2_of_isIsomorphismClasses
          (BasedCategory.ofFunctor (Elements.π F))
          ((isPredeformationCategory_iff F).2 hpre).cofibered
          ((schlessingerConditionS2_elements_iff F).2 hH2)
          (Or.inl ((isPredeformationCategory_iff F).2 hpre))⟩
      letI := setValuedTangentSpaceAddCommGroup.{u, v, w, t} F
        ((isPredeformationCategory_iff F).2 hpre)
      letI := setValuedTangentSpaceModule.{u, v, w, t} F
        ((isPredeformationCategory_iff F).2 hpre)
      FiniteDimensional k (tangentSpaceArtinian.{u, w, v} Λ k F)) :
    ∃ ξ : FormalObject (Elements.π F),
      IsHull ((isPredeformationCategory_iff F).2 hpre).cofibered ξ
```

## Tag 06IZ, a remark

[Tag 06IZ](https://stacks.math.columbia.edu/tag/06IZ) in the Stacks Project.

**`Deformation.mapIsomorphismClasses_bijective_of_isIsomorphismClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/VersalObject/IsomorphismClasses.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Formal/VersalObject/IsomorphismClasses.lean#L98). The attribute's comment: “bijective on isomorphism classes”.

> A based functor realizing the functor of isomorphism classes is bijective on isomorphism
> classes over every object of the base: injective because its fibres are skeletal and identify
> exactly the isomorphism classes upstairs, surjective because it is essentially surjective on
> each fibre.

```lean
public theorem mapIsomorphismClasses_bijective_of_isIsomorphismClasses
    {𝓐 : BasedCategory.{v₁, u₁} C} {𝓑 : BasedCategory.{v₂, u₂} C}
    (h𝓐 : IsCofiberedInGroupoids 𝓐.p) (h𝓑 : IsCofiberedInGroupoids 𝓑.p)
    (φ : BasedFunctor 𝓐 𝓑) (hφ : IsIsomorphismClasses φ) (A : C) :
    Function.Bijective (mapIsomorphismClasses h𝓐 h𝓑 φ A)
```

**`Deformation.isSmooth_associatedMorphism_toIsomorphismClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/VersalObject/IsomorphismClasses.lean, line 321](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Formal/VersalObject/IsomorphismClasses.lean#L321). The attribute's comment: “smooth composite”.

> **Stacks Project, Tag 06IZ.** The composite of the morphism associated to a versal formal
> object with the canonical morphism to the functor of isomorphism classes is smooth.

```lean
public theorem isSmooth_associatedMorphism_toIsomorphismClasses
    (ξ : FormalObject 𝓕.p) (hξ : IsVersal hpre.cofibered ξ)
    (pushforwards : ChosenPushforwards 𝓕.p) :
    IsSmooth (BasedFunctor.comp
      (associatedMorphism hpre.cofibered ξ pushforwards).toBasedFunctor
      (toIsomorphismClasses 𝓕 hpre.cofibered))
```

**`Deformation.isVersal_imageInIsomorphismClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/VersalObject/IsomorphismClasses.lean, line 336](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Formal/VersalObject/IsomorphismClasses.lean#L336). The attribute's comment: “versal image”.

> **Stacks Project, Tag 06IZ.** The image of a versal formal object in the functor of
> isomorphism classes is versal.

```lean
public theorem isVersal_imageInIsomorphismClasses
    (ξ : FormalObject 𝓕.p) (hξ : IsVersal hpre.cofibered ξ) :
    IsVersal
      (categoryOfElements_projection_isCofibered (isomorphismClasses 𝓕 hpre.cofibered))
      (imageInIsomorphismClasses 𝓕 hpre ξ)
```

**`Deformation.hasBijectiveDifferential_imageInIsomorphismClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/VersalObject/IsomorphismClasses.lean, line 357](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Formal/VersalObject/IsomorphismClasses.lean#L357). The attribute's comment: “tangent isomorphism”. References: SGA 7 VI (1.13), “tangent iso for [A]”.

> **Stacks Project, Tag 06IZ.** The image in the functor of isomorphism classes of a formal
> object with bijective differential has bijective differential: the canonical morphism
> identifies the two tangent spaces.

```lean
public theorem hasBijectiveDifferential_imageInIsomorphismClasses
    (ξ : FormalObject 𝓕.p) (hξ : HasBijectiveDifferential hpre.cofibered ξ) :
    HasBijectiveDifferential
      (categoryOfElements_projection_isCofibered (isomorphismClasses 𝓕 hpre.cofibered))
      (imageInIsomorphismClasses 𝓕 hpre ξ)
```

**`Deformation.differential_toIsomorphismClasses_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/VersalObject/IsomorphismClasses.lean, line 404](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Formal/VersalObject/IsomorphismClasses.lean#L404). The attribute's comment: “tangent spaces of the canonical morphism”.

> **Stacks Project, Tag 06IZ.** The canonical morphism from a predeformation category to its
> functor of isomorphism classes identifies tangent spaces.

```lean
public theorem differential_toIsomorphismClasses_bijective :
    Function.Bijective
      (differential hpre.cofibered
        (categoryOfElements_projection_isCofibered (isomorphismClasses 𝓕 hpre.cofibered))
        (toIsomorphismClasses 𝓕 hpre.cofibered))
```

**`Deformation.exists_hull_isomorphismClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/VersalObject/IsomorphismClassesHull.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Formal/VersalObject/IsomorphismClassesHull.lean#L54). The attribute's comment: “existence of a hull”. References: SGA 7 VI (1.20), “existence”.

> A predeformation category satisfying Schlessinger's conditions (S1) and (S2), with
> finite-dimensional tangent space and separable residue field extension, has a versal formal
> object with bijective differential whose image in the associated functor of isomorphism classes
> is again versal with bijective differential, hence a hull of that functor.

```lean
public theorem exists_hull_isomorphismClasses
    (Λ : Type u) (k : Type w) [CommRing Λ] [IsNoetherianRing Λ] [Field k] [Algebra Λ k]
    [Module.Finite Λ k] [Algebra.IsSeparable (residueImageField Λ k) k]
    (𝓕 : BasedCategory.{vF, uF} (ArtinianLocalAlgCat.{u, max v w, w} Λ k))
    (hpre : IsPredeformationCategory.{u, v, w} 𝓕.p)
    (hS1 : SchlessingerConditionS1 𝓕.p)
    (hS2 : SchlessingerConditionS2 𝓕.p)
    (hfin :
      letI : Fact (IsPredeformationCategory.{u, v, w} 𝓕.p) := ⟨hpre⟩
      letI : Fact (SchlessingerConditionS2
          (Functor.Elements.π (isomorphismClasses 𝓕 hpre.cofibered))) :=
        ⟨schlessingerConditionS2_of_isIsomorphismClasses 𝓕 hpre.cofibered hS2 (Or.inl hpre)⟩
      FiniteDimensional k (tangentSpaceArtinian.{u, w, v} Λ k
        (isomorphismClasses 𝓕 hpre.cofibered))) :
    ∃ ξ : FormalObject 𝓕.p,
      IsHull hpre.cofibered ξ ∧
      IsHull
        (categoryOfElements_projection_isCofibered (isomorphismClasses 𝓕 hpre.cofibered))
        (imageInIsomorphismClasses 𝓕 hpre ξ)
```

## Tag 06T9, an example

[Tag 06T9](https://stacks.math.columbia.edu/tag/06T9) in the Stacks Project.

**`Deformation.isPredeformationCategory_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/BaseCategoryOverItself.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/BaseCategoryOverItself.lean#L121). The attribute's comment: “predeformation category”.

> The base category `𝒞_Λ`, regarded through the identity functor as a category cofibered in
> groupoids over itself, is a predeformation category.

```lean
public theorem isPredeformationCategory_id :
    IsPredeformationCategory.{u, v, w} (𝟭 (ArtinianLocalAlgCat.{u, max v w, w} Λ k))
```

**`Deformation.schlessingerConditionS1_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/BaseCategoryOverItself.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/BaseCategoryOverItself.lean#L129). The attribute's comment: “condition (S1)”.

> `𝒞_Λ` over itself satisfies Schlessinger's condition (S1).

```lean
public theorem schlessingerConditionS1_id :
    SchlessingerConditionS1 (𝟭 (ArtinianLocalAlgCat.{u, max v w, w} Λ k))
```

**`Deformation.schlessingerConditionS2_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/BaseCategoryOverItself.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/BaseCategoryOverItself.lean#L140). The attribute's comment: “condition (S2)”.

> `𝒞_Λ` over itself satisfies Schlessinger's condition (S2).

```lean
public theorem schlessingerConditionS2_id :
    SchlessingerConditionS2 (𝟭 (ArtinianLocalAlgCat.{u, max v w, w} Λ k))
```

**`Deformation.unique_predeformationTangentSpace_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/BaseCategoryOverItself.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/BaseCategoryOverItself.lean#L200). The attribute's comment: “vanishing of the tangent space”.

> The tangent space of `𝒞_Λ` over itself vanishes: it has exactly one element.

```lean
public theorem unique_predeformationTangentSpace_id :
    Nonempty (Unique (predeformationTangentSpace.{u, v, w}
      (𝟭 (ArtinianLocalAlgCat.{u, max v w, w} Λ k)) (isPredeformationCategory_id Λ k)))
```

**`Deformation.isMinimalVersal_selfFormalObject_smoothModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/BaseCategoryOverItself.lean, line 454](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/BaseCategoryOverItself.lean#L454). The attribute's comment: “the smooth model of Stacks 06SM carries a minimal versal formal object”.

> The object `R` constructed in Stacks 06SM carries a minimal versal formal object of `𝒞_Λ`
> regarded as cofibered in groupoids over itself.

```lean
public theorem isMinimalVersal_selfFormalObject_smoothModel :
    IsMinimalVersal isCofiberedInGroupoids_id
      (selfFormalObject.{u, u, w} (smoothModel.{u, w} (Λ := Λ) (k := k)))
```

**`Deformation.isMinimalVersal_id_base_properties`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/BaseCategoryOverItself.lean, line 465](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/BaseCategoryOverItself.lean#L465). The attribute's comment: “the cotangent identifications and the comparison with Stacks 06SM”.

> The complete local algebra `S` underlying any minimal versal formal object of `𝒞_Λ` over
> itself is formally smooth over `Λ` in the `𝔪_S`-adic topology, its module of differentials
> satisfies `Ω_{S/Λ} ⊗_S k = Ω_{k/Λ}`, its conormal module satisfies `H₁(L_{k/Λ}) = 𝔪_S/𝔪_S²`, and
> it is isomorphic to the object constructed in Stacks 06SM.

```lean
public theorem isMinimalVersal_id_base_properties
    (ξ : FormalObject (𝟭 (ArtinianLocalAlgCat.{u, max u w, w} Λ k)))
    (hξ : IsMinimalVersal isCofiberedInGroupoids_id ξ) :
    letI : Algebra ξ.base k := (residueHom ξ.base).toRingHom.toAlgebra
    letI : IsScalarTower Λ ξ.base k :=
      IsScalarTower.of_algebraMap_eq' (residueHom ξ.base).comp_algebraMap.symm
    RingHom.FormallySmoothNAdic.{max u w} (algebraMap Λ ξ.base) (maximalIdeal ξ.base) ∧
      Function.Bijective (KaehlerDifferential.mapBaseChange Λ ξ.base k) ∧
        Function.Bijective (Algebra.H1Cotangent.map Λ ξ.base k k) ∧
          Nonempty (ξ.base ≅ smoothModel.{u, w} (Λ := Λ) (k := k))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.15, Tag 06IL](https://stacks.math.columbia.edu/tag/06IL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
