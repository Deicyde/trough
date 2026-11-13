---
declaration: section
origin: cited
lean: RingHom.IsUnramifiedLocalHom, RingHom.isUnramifiedLocalHom_algebraMap_iff, RingHom.isUnramifiedLocalHom_iff, Algebra.exists_unramified_away_iff_isUnramifiedLocalHom_algebraMap, RingHom.moduleFinite_adicCompletion_of_formallyUnramified, RingHom.surjective_adicCompletionMap_of_bijective_residueFieldMap, RingHom.surjective_adicCompletionMap_of_isSepClosed, RingHom.unramified_iff_uniformizer_and_residueField
statement: formalized
proof: formalized
---

# 41.3 Unramified morphisms

Section 41.3 of the Stacks Project, [Tag 024L](https://stacks.math.columbia.edu/tag/024L). 6 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 024M, a definition

[Tag 024M](https://stacks.math.columbia.edu/tag/024M) in the Stacks Project.

**`RingHom.IsUnramifiedLocalHom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/LocalHom.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/LocalHom.lean#L58).

> A local homomorphism `f : A → B` of local rings is an *unramified homomorphism of local
> rings* if `𝔪_A B = 𝔪_B`, the residue field `κ(𝔪_B)` is a finite separable extension of
> `κ(𝔪_A)`, and `B` is essentially of finite type over `A`.

```lean
structure IsUnramifiedLocalHom (f : A →+* B) [IsLocalHom f] : Prop
```

**`RingHom.isUnramifiedLocalHom_algebraMap_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/LocalHom.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/LocalHom.lean#L98). The attribute's comment: “Equivalently, `A → B` is formally unramified and essentially of finite type.”.

> The structure map of a local algebra `B` over `A` is an unramified homomorphism of local rings
> if and only if `B` is formally unramified and essentially of finite type over `A`.

```lean
theorem isUnramifiedLocalHom_algebraMap_iff :
    (algebraMap A B).IsUnramifiedLocalHom ↔
      Algebra.FormallyUnramified A B ∧ Algebra.EssFiniteType A B
```

**`RingHom.isUnramifiedLocalHom_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/LocalHom.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/LocalHom.lean#L114). The attribute's comment: “Equivalently, `f` is formally unramified and essentially of finite type.”.

> A local homomorphism of local rings is an unramified homomorphism of local rings if and only
> if it is formally unramified and essentially of finite type.

```lean
theorem isUnramifiedLocalHom_iff (f : A →+* B) [IsLocalHom f] :
    f.IsUnramifiedLocalHom ↔ f.FormallyUnramified ∧ f.EssFiniteType
```

## Tag 039G, a lemma

[Tag 039G](https://stacks.math.columbia.edu/tag/039G) in the Stacks Project.

**`Algebra.exists_unramified_away_iff_isUnramifiedLocalHom_algebraMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/LocalHomAtPrime.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/LocalHomAtPrime.lean#L68). The attribute's comment: “Without the Noetherian hypothesis on `A`, which is used in the source only to make Definition 024M applicable to `A_p → B_q`; `RingHom.IsUnramifiedLocalHom` is defined for all local rings. See the module docstring.”.

> **Stacks 039G.** Let `A → B` be of finite type and let `q` be a prime of `B` lying over the
> prime `p` of `A`. Then `A → B` is unramified at `q` (there is `g ∉ q` with `A → B_g` unramified)
> if and only if `A_p → B_q` is an unramified homomorphism of local rings. The source assumes `A`
> Noetherian, which is not needed.

```lean
theorem exists_unramified_away_iff_isUnramifiedLocalHom_algebraMap {A B : Type*} [CommRing A]
    [CommRing B] [Algebra A B] [Algebra.FiniteType A B] (p : Ideal A) [p.IsPrime] (q : Ideal B)
    [q.IsPrime] [q.LiesOver p] [Algebra (Localization.AtPrime p) (Localization.AtPrime q)]
    [IsScalarTower A (Localization.AtPrime p) (Localization.AtPrime q)] :
    (∃ g ∉ q, Algebra.Unramified A (Localization.Away g)) ↔
      (algebraMap (Localization.AtPrime p) (Localization.AtPrime q)).IsUnramifiedLocalHom
```

## Tag 039H, a lemma

[Tag 039H](https://stacks.math.columbia.edu/tag/039H) in the Stacks Project.

**`RingHom.moduleFinite_adicCompletion_of_formallyUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/UnramifiedCompletion.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/UnramifiedCompletion.lean#L65). The attribute's comment: “part (1)”. References: EGA IV (17.4.4), “f) finiteness of B̂/Â”.

> **Stacks Project, Tag 039H**, part (1). The completion of the target of an unramified local
> homomorphism of Noetherian local rings is a finite module over the completion of the source.

```lean
theorem moduleFinite_adicCompletion_of_formallyUnramified
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B] (f : A →+* B) [IsLocalHom f]
    (hfu : f.FormallyUnramified) (hft : f.EssFiniteType) :
    letI := (adicCompletionMap f (maximalIdeal A) (maximalIdeal B)
      (map_maximalIdeal_le f)).toAlgebra
    Module.Finite (AdicCompletion (maximalIdeal A) A)
      (AdicCompletion (maximalIdeal B) B)
```

**`RingHom.surjective_adicCompletionMap_of_bijective_residueFieldMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/UnramifiedCompletion.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/UnramifiedCompletion.lean#L130). The attribute's comment: “part (2)”. References: EGA IV (17.4.4), “f'') when k(x)=k(y)”; SGA 1 I (3.7), “unram ⇒ surj, κ(A)=κ(B)”; SGA 3 XI (1.3), “(ii) completion surj.”.

> **Stacks Project, Tag 039H**, part (2). An unramified local homomorphism inducing a
> bijection on residue fields induces a surjection on completions.

```lean
theorem surjective_adicCompletionMap_of_bijective_residueFieldMap
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B] (f : A →+* B) [IsLocalHom f]
    (hfu : f.FormallyUnramified) (hft : f.EssFiniteType)
    (hκ : Function.Bijective (ResidueField.map f)) :
    Function.Surjective
      (adicCompletionMap f (maximalIdeal A) (maximalIdeal B) (map_maximalIdeal_le f))
```

**`RingHom.surjective_adicCompletionMap_of_isSepClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/UnramifiedCompletion.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/UnramifiedCompletion.lean#L192). The attribute's comment: “part (3)”. References: EGA IV (17.4.4), “f'') k sep closed”; EGA IV (17.6.3), “partial”; SGA 1 I (3.7), “unram ⇒ surj, κ sep cl”.

> **Stacks Project, Tag 039H**, part (3). An unramified local homomorphism whose source has
> separably closed residue field induces a surjection on completions.

```lean
theorem surjective_adicCompletionMap_of_isSepClosed
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B] (f : A →+* B) [IsLocalHom f]
    (hfu : f.FormallyUnramified) (hft : f.EssFiniteType)
    [IsSepClosed (ResidueField A)] :
    Function.Surjective
      (adicCompletionMap f (maximalIdeal A) (maximalIdeal B) (map_maximalIdeal_le f))
```

**`RingHom.unramified_iff_uniformizer_and_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/UnramifiedCompletion.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/UnramifiedCompletion.lean#L210). The attribute's comment: “part (4)”.

> **Stacks Project, Tag 039H**, part (4). A local homomorphism of complete discrete valuation
> rings is unramified exactly when it carries a uniformizer to a uniformizer, its residue field
> extension is finite and separable, and it is essentially of finite type.

```lean
theorem unramified_iff_uniformizer_and_residueField
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsDomain A] [IsDomain B]
    [IsDiscreteValuationRing A] [IsDiscreteValuationRing B]
    [IsAdicComplete (maximalIdeal A) A] [IsAdicComplete (maximalIdeal B) B]
    (f : A →+* B) [IsLocalHom f] (ϖ : A) (hϖ : Irreducible ϖ) :
    letI := f.toAlgebra
    (Algebra.FormallyUnramified A B ∧ Algebra.EssFiniteType A B) ↔
      (Irreducible (f ϖ) ∧ Module.Finite (ResidueField A) (ResidueField B) ∧
        Algebra.IsSeparable (ResidueField A) (ResidueField B) ∧ Algebra.EssFiniteType A B)
```

## Tag 039I, a lemma

[Tag 039I](https://stacks.math.columbia.edu/tag/039I) in the Stacks Project.

**`RingHom.formallyUnramified_iff_formallyUnramified_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/CompletionCriteria.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/CompletionCriteria.lean#L235). The attribute's comment: “parts (1) and (2)”. References: EGA IV (17.4.4), “f')”.

> **Stacks Project, Tag 039I**, parts (1) and (2). An essentially finite type local
> homomorphism of Noetherian local rings is formally unramified if and only if the induced
> homomorphism of completions is.

```lean
theorem formallyUnramified_iff_formallyUnramified_adicCompletion
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B] (f : A →+* B) [IsLocalHom f] (hft : f.EssFiniteType) :
    letI := f.toAlgebra
    Algebra.FormallyUnramified A B ↔
      (letI := (adicCompletionMap f (maximalIdeal A) (maximalIdeal B)
        (map_maximalIdeal_le f)).toAlgebra
       Algebra.FormallyUnramified
         (AdicCompletion (maximalIdeal A) A) (AdicCompletion (maximalIdeal B) B))
```

**`RingHom.formallyUnramified_adicCompletion_iff_unramified_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/CompletionCriteria.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/CompletionCriteria.lean#L293). The attribute's comment: “parts (2) and (3)”.

> **Stacks Project, Tag 039I**, parts (2) and (3). For the completion of an essentially finite
> type local homomorphism of Noetherian local rings, formal unramifiedness and unramifiedness
> agree.

```lean
theorem formallyUnramified_adicCompletion_iff_unramified_adicCompletion
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B] (f : A →+* B) [IsLocalHom f] (hft : f.EssFiniteType) :
    letI := (adicCompletionMap f (maximalIdeal A) (maximalIdeal B)
      (map_maximalIdeal_le f)).toAlgebra
    Algebra.FormallyUnramified
        (AdicCompletion (maximalIdeal A) A) (AdicCompletion (maximalIdeal B) B) ↔
      Algebra.Unramified
        (AdicCompletion (maximalIdeal A) A) (AdicCompletion (maximalIdeal B) B)
```

## Tag 024N, a definition

[Tag 024N](https://stacks.math.columbia.edu/tag/024N) in the Stacks Project.

**`AlgebraicGeometry.StalkwiseUnramifiedAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Unramified.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Unramified.lean#L45). The attribute's comment: “part (1)”.

> A locally finite type morphism to a locally Noetherian scheme is unramified at `x` if its
> map on local rings at `x` is unramified.

```lean
abbrev StalkwiseUnramifiedAt {X Y : Scheme.{u}} (f : X ⟶ Y) [IsLocallyNoetherian Y]
    [LocallyOfFiniteType f] (x : X) : Prop
```

**`AlgebraicGeometry.StalkwiseUnramified`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Unramified.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Unramified.lean#L53). The attribute's comment: “part (2)”.

> A locally finite type morphism to a locally Noetherian scheme is unramified if it is
> unramified at every point of its source.

```lean
class StalkwiseUnramified {X Y : Scheme.{u}} (f : X ⟶ Y) [IsLocallyNoetherian Y]
    [LocallyOfFiniteType f] : Prop
```

## Tag 039J, a lemma

[Tag 039J](https://stacks.math.columbia.edu/tag/039J) in the Stacks Project.

**`AlgebraicGeometry.unramifiedAt_iff_morphisms_unramifiedAt`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Unramified.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Unramified.lean#L85).

> For a locally finite type morphism to a locally Noetherian scheme, the stalk-theoretic
> definition of unramifiedness at a point agrees with the affine-neighbourhood definition.

```lean
lemma unramifiedAt_iff_morphisms_unramifiedAt
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsLocallyNoetherian Y]
    [LocallyOfFiniteType f] (x : X) :
    StalkwiseUnramifiedAt f x ↔ UnramifiedAt f x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 41.3, Tag 024L](https://stacks.math.columbia.edu/tag/024L)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
