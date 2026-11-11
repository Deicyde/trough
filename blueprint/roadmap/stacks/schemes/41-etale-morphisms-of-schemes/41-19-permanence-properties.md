---
declaration: section
origin: cited
lean: RingHom.depth_eq_of_isEtaleLocalHom, RingHom.isReduced_iff_of_isEtaleLocalHom, RingHom.isCohenMacaulayLocalRing_iff_of_isEtaleLocalHom, RingHom.ringKrullDim_eq_of_isEtaleLocalHom, RingHom.isRegularLocalRing_iff_of_isEtaleLocalHom, RingHom.isNormalDomain_iff_of_isEtaleLocalHom
statement: formalized
proof: formalized
---

# 41.19 Permanence properties

Section 41.19 of the Stacks Project, [Tag 025L](https://stacks.math.columbia.edu/tag/025L). 7 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 025L, the section

[Tag 025L](https://stacks.math.columbia.edu/tag/025L) in the Stacks Project.

**`RingHom.depth_eq_of_isEtaleLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean#L72). The tag is given by the `attribute` command at [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean#L90). The attribute's comment: “Proposition 039T of the section: for an étale homomorphism `A → B` of Noetherian local rings, `depth(A) = depth(B)`.”.

> An étale local homomorphism between Noetherian local rings
> preserves depth.

```lean
theorem depth_eq_of_isEtaleLocalHom
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B]
    (f : A →+* B) [IsLocalHom f]
    (hf : IsEtaleLocalHom f) :
    Module.depth A (IsLocalRing.maximalIdeal A) A =
      Module.depth B (IsLocalRing.maximalIdeal B) B
```

**`RingHom.isReduced_iff_of_isEtaleLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean#L97). The tag is given by the `attribute` command at [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean#L115). The attribute's comment: “Proposition 025O of the section: for an étale homomorphism `A → B` of Noetherian local rings, `A` is reduced if and only if `B` is reduced.”. References: SGA 1 I (9.3), “Noetherian case”.

> An étale local homomorphism between Noetherian local rings
> preserves and reflects reducedness.

```lean
theorem isReduced_iff_of_isEtaleLocalHom
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B]
    (f : A →+* B) [IsLocalHom f]
    (hf : IsEtaleLocalHom f) :
    IsReduced A ↔ IsReduced B
```

**`RingHom.isCohenMacaulayLocalRing_iff_of_isEtaleLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean#L153). The tag is given by the `attribute` command at [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean#L168). The attribute's comment: “Proposition 025Q of the section: for an étale homomorphism `A → B` of Noetherian local rings, `A` is Cohen-Macaulay if and only if `B` is Cohen-Macaulay.”.

> Cohen-Macaulayness is preserved and reflected by an étale
> local homomorphism of Noetherian local rings.

```lean
theorem isCohenMacaulayLocalRing_iff_of_isEtaleLocalHom
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B]
    (f : A →+* B) [IsLocalHom f]
    (hf : IsEtaleLocalHom f) :
    IsCohenMacaulayLocalRing A ↔ IsCohenMacaulayLocalRing B
```

**`RingHom.ringKrullDim_eq_of_isEtaleLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean#L175). The tag is given by the `attribute` command at [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean#L184). The attribute's comment: “Lemma 039S of the section: for an étale homomorphism `A → B` of Noetherian local rings, `dim(A) = dim(B)`.”. References: EGA IV (6.1.3), “special case”.

> An étale homomorphism of Noetherian local rings preserves the
> Krull dimension: the dimension of the source equals the dimension of the target.

```lean
theorem ringKrullDim_eq_of_isEtaleLocalHom
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B]
    (f : A →+* B) [IsLocalHom f]
    (hf : IsEtaleLocalHom f) :
    ringKrullDim A = ringKrullDim B
```

**`RingHom.isRegularLocalRing_iff_of_isEtaleLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/Permanence.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/Permanence.lean#L56). The tag is given by the `attribute` command at [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/Permanence.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/Permanence.lean#L73). The attribute's comment: “Proposition 025N of the section: for an étale homomorphism `A → B` of Noetherian local rings, `A` is regular if and only if `B` is regular.”. References: SGA 1 I (9.1).

> **Stacks Project, Tag 025N.** An étale local homomorphism between Noetherian local rings
> preserves and reflects regularity.

```lean
theorem isRegularLocalRing_iff_of_isEtaleLocalHom
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B]
    (f : A →+* B) [IsLocalHom f]
    (hf : IsEtaleLocalHom f) :
    IsRegularLocalRing A ↔ IsRegularLocalRing B
```

**`RingHom.isNormalDomain_iff_of_isEtaleLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/Permanence.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/Permanence.lean#L97). The tag is given by the `attribute` command at [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/Permanence.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/Permanence.lean#L123). The attribute's comment: “Proposition 025P of the section: for an étale homomorphism `A → B` of Noetherian local rings, `A` is a normal domain if and only if `B` is a normal domain.”. References: SGA 1 I (9.5), “(i), Noetherian”.

> **Stacks Project, Tag 025P.** An étale local homomorphism between Noetherian local rings
> preserves and reflects the property of being a normal domain.

```lean
theorem isNormalDomain_iff_of_isEtaleLocalHom
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B]
    (f : A →+* B) [IsLocalHom f]
    (hf : IsEtaleLocalHom f) :
    IsNormalDomain A ↔ IsNormalDomain B
```

## Tag 039S, a lemma

[Tag 039S](https://stacks.math.columbia.edu/tag/039S) in the Stacks Project.

**`RingHom.ringKrullDim_eq_of_isEtaleLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean#L175). References: EGA IV (6.1.3), “special case”.

> An étale homomorphism of Noetherian local rings preserves the
> Krull dimension: the dimension of the source equals the dimension of the target.

```lean
theorem ringKrullDim_eq_of_isEtaleLocalHom
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B]
    (f : A →+* B) [IsLocalHom f]
    (hf : IsEtaleLocalHom f) :
    ringKrullDim A = ringKrullDim B
```

## Tag 039T, a proposition

[Tag 039T](https://stacks.math.columbia.edu/tag/039T) in the Stacks Project.

**`RingHom.depth_eq_of_isEtaleLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean#L72).

> An étale local homomorphism between Noetherian local rings
> preserves depth.

```lean
theorem depth_eq_of_isEtaleLocalHom
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B]
    (f : A →+* B) [IsLocalHom f]
    (hf : IsEtaleLocalHom f) :
    Module.depth A (IsLocalRing.maximalIdeal A) A =
      Module.depth B (IsLocalRing.maximalIdeal B) B
```

## Tag 025Q, a proposition

[Tag 025Q](https://stacks.math.columbia.edu/tag/025Q) in the Stacks Project.

**`RingHom.isCohenMacaulayLocalRing_iff_of_isEtaleLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean#L153).

> Cohen-Macaulayness is preserved and reflected by an étale
> local homomorphism of Noetherian local rings.

```lean
theorem isCohenMacaulayLocalRing_iff_of_isEtaleLocalHom
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B]
    (f : A →+* B) [IsLocalHom f]
    (hf : IsEtaleLocalHom f) :
    IsCohenMacaulayLocalRing A ↔ IsCohenMacaulayLocalRing B
```

## Tag 025N, a proposition

[Tag 025N](https://stacks.math.columbia.edu/tag/025N) in the Stacks Project.

**`RingHom.isRegularLocalRing_iff_of_isEtaleLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/Permanence.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/Permanence.lean#L56). References: SGA 1 I (9.1).

> **Stacks Project, Tag 025N.** An étale local homomorphism between Noetherian local rings
> preserves and reflects regularity.

```lean
theorem isRegularLocalRing_iff_of_isEtaleLocalHom
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B]
    (f : A →+* B) [IsLocalHom f]
    (hf : IsEtaleLocalHom f) :
    IsRegularLocalRing A ↔ IsRegularLocalRing B
```

## Tag 025O, a proposition

[Tag 025O](https://stacks.math.columbia.edu/tag/025O) in the Stacks Project.

**`RingHom.isReduced_iff_of_isEtaleLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Permanence.lean#L97). References: SGA 1 I (9.3), “Noetherian case”.

> An étale local homomorphism between Noetherian local rings
> preserves and reflects reducedness.

```lean
theorem isReduced_iff_of_isEtaleLocalHom
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B]
    (f : A →+* B) [IsLocalHom f]
    (hf : IsEtaleLocalHom f) :
    IsReduced A ↔ IsReduced B
```

## Tag 025P, a proposition

[Tag 025P](https://stacks.math.columbia.edu/tag/025P) in the Stacks Project.

**`RingHom.isNormalDomain_iff_of_isEtaleLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/Permanence.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/Permanence.lean#L97). References: SGA 1 I (9.5), “(i), Noetherian”.

> **Stacks Project, Tag 025P.** An étale local homomorphism between Noetherian local rings
> preserves and reflects the property of being a normal domain.

```lean
theorem isNormalDomain_iff_of_isEtaleLocalHom
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B]
    (f : A →+* B) [IsLocalHom f]
    (hf : IsEtaleLocalHom f) :
    IsNormalDomain A ↔ IsNormalDomain B
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 41.19, Tag 025L](https://stacks.math.columbia.edu/tag/025L)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
