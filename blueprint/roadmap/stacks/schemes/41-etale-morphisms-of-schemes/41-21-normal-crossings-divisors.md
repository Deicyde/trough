---
declaration: section
origin: cited
lean: Stacks.Divisors.IsStrictNormalCrossingsDivisor, Stacks.Divisors.isStrictNormalCrossingsDivisor_iff, Stacks.Divisors.isStrictNormalCrossingsDivisor_comap, Stacks.Divisors.IsNormalCrossingsDivisor, Stacks.Divisors.isNormalCrossingsDivisor_comap, Stacks.Divisors.isClopen_normalizationDistinctLocus, Stacks.Divisors.unramified_normalizationDistinctToAmbient, Stacks.Divisors.formallyUnramified_normalizationDistinctToAmbient
statement: formalized
proof: formalized
---

# 41.21 Normal crossings divisors

Section 41.21 of the Stacks Project, [Tag 0CBN](https://stacks.math.columbia.edu/tag/0CBN). 7 tags here are carried by 25 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BI9, a definition

[Tag 0BI9](https://stacks.math.columbia.edu/tag/0BI9) in the Stacks Project.

**`Stacks.Divisors.IsStrictNormalCrossingsDivisor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/NormalCrossings/Defs.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/NormalCrossings/Defs.lean#L58). References: SGA 5 I (3.1.5), “a) strict n.c.”.

> An effective Cartier divisor locally cut out by a product of a nonempty initial segment of a
> regular system of parameters.

```lean
public abbrev IsStrictNormalCrossingsDivisor {X : Scheme.{u}}
    [IsLocallyNoetherian X] (D : X.IdealSheafData) : Prop
```

## Tag 0BIA, a lemma

[Tag 0BIA](https://stacks.math.columbia.edu/tag/0BIA) in the Stacks Project.

**`Stacks.Divisors.isStrictNormalCrossingsDivisor_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/Components.lean, line 1139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/Components.lean#L1139).

> A locally Noetherian effective Cartier divisor has strict normal crossings
> if and only if it is reduced and all finite nonempty intersections of its
> irreducible components are regular of the expected codimension.

```lean
public theorem isStrictNormalCrossingsDivisor_iff {X : Scheme.{u}}
    [IsLocallyNoetherian X] (D : X.IdealSheafData)
    (hD : IsEffectiveCartierDivisor D) :
    IsStrictNormalCrossingsDivisor D ↔
      (IsReduced D.subscheme ∧
        (∀ C : irreducibleComponents D.subscheme,
          IsEffectiveCartierDivisor
            (componentIdeal D C)) ∧
        (∀ J : Finset (irreducibleComponents D.subscheme), J.Nonempty →
          AlgebraicGeometry.IsRegular (componentIntersection D J).subscheme ∧
            ∀ C : irreducibleComponents (componentIntersection D J).subscheme,
              codimension (IrreducibleCloseds.closureSingleton
                ((componentIntersection D J).subschemeι C.2.1.genericPoint)) =
                  (J.card : ℕ∞)))
```

## Tag 0CBP, a lemma

[Tag 0CBP](https://stacks.math.columbia.edu/tag/0CBP) in the Stacks Project.

**`Stacks.Divisors.isStrictNormalCrossingsDivisor_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/SmoothPullback.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/SmoothPullback.lean#L295).

> **Stacks Project, Tag 0CBP.** The pullback of a strict normal crossings divisor along a
> smooth morphism is a strict normal crossings divisor.

```lean
theorem isStrictNormalCrossingsDivisor_comap {X Y : Scheme.{u}} [IsLocallyNoetherian X]
    (f : Y ⟶ X) [Smooth f] (D : X.IdealSheafData)
    (hD : IsStrictNormalCrossingsDivisor D) :
    @IsStrictNormalCrossingsDivisor Y (LocallyOfFiniteType.isLocallyNoetherian f)
      (D.comap f)
```

## Tag 0BSF, a definition

[Tag 0BSF](https://stacks.math.columbia.edu/tag/0BSF) in the Stacks Project.

**`Stacks.Divisors.IsNormalCrossingsDivisor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/NormalCrossings/Defs.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/NormalCrossings/Defs.lean#L70). References: SGA 1 XIII (2.1.0), “absolute case”; SGA 5 I (3.1.5), “a) normal crossings”.

> An effective Cartier divisor which acquires strict normal crossings étale-locally at every
> point of its support.

```lean
public abbrev IsNormalCrossingsDivisor {X : Scheme.{u}}
    [IsLocallyNoetherian X] (D : X.IdealSheafData) : Prop
```

## Tag 0CBQ, a lemma

[Tag 0CBQ](https://stacks.math.columbia.edu/tag/0CBQ) in the Stacks Project.

**`Stacks.Divisors.isNormalCrossingsDivisor_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/SmoothPullback.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/SmoothPullback.lean#L319).

> **Stacks Project, Tag 0CBQ.** The pullback of a normal crossings divisor along a smooth
> morphism is a normal crossings divisor.

```lean
theorem isNormalCrossingsDivisor_comap {X Y : Scheme.{u}} [IsLocallyNoetherian X]
    (f : Y ⟶ X) [Smooth f] (D : X.IdealSheafData)
    (hD : IsNormalCrossingsDivisor D) :
    @IsNormalCrossingsDivisor Y (LocallyOfFiniteType.isLocallyNoetherian f) (D.comap f)
```

## Tag 0CBR, a lemma

[Tag 0CBR](https://stacks.math.columbia.edu/tag/0CBR) in the Stacks Project.

**`Stacks.Divisors.isClopen_normalizationDistinctLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationCriterion.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationCriterion.lean#L275). The attribute's comment: “first paragraph of the proof: `Z_n` is an open and closed subscheme of the fibre power of the normalization. Neither implication of the equivalence is asserted.”.

> `Z_n` is open and closed in the fibre power of the normalization, once the latter is
> unramified.

```lean
public theorem isClopen_normalizationDistinctLocus [Unramified (divisorNormalization D)]
    (n : ℕ) : IsClopen (fibrePowerDistinctLocus (divisorNormalization D) n)
```

**`Stacks.Divisors.unramified_normalizationDistinctToAmbient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationCriterion.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationCriterion.lean#L283). The attribute's comment: “first paragraph of the proof: `Z_n ⟶ X` is unramified. Neither implication of the equivalence is asserted.”.

> Once the normalization of `D` is unramified, `Z_n ⟶ X` is unramified: it is the composition
> of an open immersion, an iterated base change of the normalization, and a closed immersion.

```lean
public theorem unramified_normalizationDistinctToAmbient
    [Unramified (divisorNormalization D)] (n : ℕ) :
    Unramified (normalizationDistinctToAmbient D n)
```

**`Stacks.Divisors.formallyUnramified_normalizationDistinctToAmbient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationCriterion.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationCriterion.lean#L294). The attribute's comment: “first paragraph of the proof: `Z_n ⟶ X` is formally unramified, so the conormal sheaf `𝒞_n` exists. Neither implication of the equivalence is asserted.”.

> Once the normalization of `D` is unramified, `Z_n ⟶ X` is formally unramified, so that it
> has a conormal sheaf.

```lean
public theorem formallyUnramified_normalizationDistinctToAmbient
    [Unramified (divisorNormalization D)] (n : ℕ) :
    FormallyUnramified (normalizationDistinctToAmbient D n)
```

**`Stacks.Divisors.IsNormalizationCrossingsDivisor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationCriterion.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationCriterion.lean#L306). The attribute's comment: “condition (2). Its equivalence with condition (1), `Stacks.Divisors.IsNormalCrossingsDivisor`, is not asserted.”.

> Condition (2) of Tag 0CBR: the closed subscheme cut out by `D` is reduced, its normalization
> is unramified, and every `Z_n` with `n ≥ 1` is regular and maps to the ambient scheme by a local
> complete intersection morphism whose conormal sheaf is locally free of rank `n`.

```lean
public def IsNormalizationCrossingsDivisor : Prop
```

**`Stacks.Divisors.isReduced_of_isNormalCrossingsDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationCriterion.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationCriterion.lean#L323). The attribute's comment: “the implication (1) to (2), restricted to its reducedness clause. The remaining clauses of (2) under hypothesis (1), and the converse implication, are not asserted.”.

> A normal crossings divisor is reduced, which is the first clause of condition (2) of
> Tag 0CBR. Étale-locally the divisor has strict normal crossings, hence is reduced by Tag 0BIA,
> and reducedness descends along the faithfully flat maps that an étale chart induces on stalks of
> the divisor.

```lean
public theorem isReduced_of_isNormalCrossingsDivisor (h : IsNormalCrossingsDivisor D) :
    IsReduced D.subscheme
```

**`Stacks.Divisors.isNormal_reducedComponent_of_isStrictNormalCrossingsDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationCriterion.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationCriterion.lean#L420). The attribute's comment: “an input to the implication (1) to (2) in the strict case: an irreducible component of a strict normal crossings divisor, with its reduced induced closed subscheme structure, is normal. Neither implication of the equivalence is asserted.”.

> An irreducible component of a strict normal crossings divisor, with its reduced induced
> closed subscheme structure, is a normal scheme: it is regular by Tag 0BIA, and a regular scheme
> is normal.

```lean
public theorem isNormal_reducedComponent_of_isStrictNormalCrossingsDivisor
    (h : IsStrictNormalCrossingsDivisor D) (C : irreducibleComponents D.subscheme) :
    IsNormal (D.subscheme.reducedComponent C)
```

**`Stacks.Divisors.unramified_divisorNormalization_of_isStrictNormalCrossingsDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationCriterion.lean, line 438](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationCriterion.lean#L438). The attribute's comment: “the implication (1) to (2) for a strict normal crossings divisor, restricted to the clause that the normalization of the divisor is unramified. The general normal crossings case, the remaining clauses of (2), and the converse implication are not asserted.”.

> The normalization of a strict normal crossings divisor is unramified, which is the
> unramifiedness clause of condition (2) of Tag 0CBR in the strict case. The normalization is the
> disjoint union of the normalizations of the irreducible components of the divisor, each component
> is normal, so each of those normalization morphisms is an isomorphism, and what remains is a
> disjoint union of closed immersions.

```lean
public theorem unramified_divisorNormalization_of_isStrictNormalCrossingsDivisor
    (h : IsStrictNormalCrossingsDivisor D) : Unramified (divisorNormalization D)
```

**`Stacks.Divisors.isNormalCrossingsDivisor_iff_reduced_unramified_normalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationEquivalence.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationEquivalence.lean#L78).

> Let `X` be a locally Noetherian scheme and let `D ⊂ X` be a
> closed subscheme. The following are equivalent:
>
> 1. `D` is a normal crossings divisor in `X`;
> 2. `D` is reduced, the normalization `ν : D^ν ⟶ D` is unramified, and for every `n ≥ 1` the
>    scheme `Z_n`, obtained from the `n`-fold fibre power of `ν` over `D` by deleting the fat
>    diagonal, is regular and the morphism `Z_n ⟶ X` is a local complete intersection morphism
>    whose conormal sheaf is locally free of rank `n`.

```lean
theorem isNormalCrossingsDivisor_iff_reduced_unramified_normalization {X : Scheme.{u}}
    [IsLocallyNoetherian X] (D : X.IdealSheafData) :
    IsNormalCrossingsDivisor D ↔
      (IsReduced D.subscheme ∧
        ∃ hν : Unramified (divisorNormalization D), ∀ n : ℕ, 1 ≤ n →
          AlgebraicGeometry.IsRegular (normalizationDistinct D n) ∧
            IsLocalCompleteIntersectionMorphism (normalizationDistinctToAmbient D n) ∧
              (letI : Unramified (divisorNormalization D) := hν
               haveI := formallyUnramified_normalizationDistinctToAmbient D n
               SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
                 (Stacks.Thickenings.universalConormalSheaf
                   (normalizationDistinctToAmbient D n)) n))
```

**`Stacks.Divisors.isIntegralHom_divisorNormalization`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationFiniteness.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationFiniteness.lean#L102). The attribute's comment: “the proof of (2) to (1), first step: the normalization `ν : D^ν ⟶ D` is integral. Neither implication of the equivalence is asserted.”.

> The normalization of the closed subscheme cut out by a divisor on a locally Noetherian scheme
> is an integral morphism.

```lean
public instance isIntegralHom_divisorNormalization : IsIntegralHom (divisorNormalization D)
```

**`Stacks.Divisors.isFinite_divisorNormalization`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationFiniteness.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationFiniteness.lean#L116). The attribute's comment: “the proof of (2) to (1), first step: an unramified `ν` is finite, being integral and locally of finite type (Tag 01WJ). Neither implication of the equivalence is asserted.”.

> An unramified normalization of the closed subscheme cut out by a divisor on a locally
> Noetherian scheme is finite: it is integral and, being unramified, locally of finite type.

```lean
public instance isFinite_divisorNormalization [Unramified (divisorNormalization D)] :
    IsFinite (divisorNormalization D)
```

**`Stacks.Divisors.isFinite_divisorNormalizationToAmbient`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationFiniteness.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationFiniteness.lean#L130). The attribute's comment: “the proof of (2) to (1), second step: `D^ν ⟶ X` is finite. Neither implication of the equivalence is asserted.”.

> The morphism `D^ν ⟶ X` is finite when the normalization of `D` is unramified: it is the
> composition of the finite normalization with a closed immersion.

```lean
public instance isFinite_divisorNormalizationToAmbient
    [Unramified (divisorNormalization D)] : IsFinite (divisorNormalizationToAmbient D)
```

**`Stacks.Divisors.unramified_divisorNormalizationToAmbient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationFiniteness.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationFiniteness.lean#L138). The attribute's comment: “the proof of (2) to (1), second step: `D^ν ⟶ X` is unramified. Neither implication of the equivalence is asserted.”.

> The morphism `D^ν ⟶ X` is unramified when the normalization of `D` is: it is the composition
> of the unramified normalization with a closed immersion.

```lean
public theorem unramified_divisorNormalizationToAmbient
    [Unramified (divisorNormalization D)] : Unramified (divisorNormalizationToAmbient D)
```

**`Stacks.Divisors.exists_etaleNeighborhood_disjoint_closed_decomposition_divisorNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationFiniteness.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationFiniteness.lean#L149). The attribute's comment: “the proof of (2) to (1), third step: étale-locally on `X` the normalization is a finite disjoint union of closed subschemes of the étale neighbourhood (Tag 04HJ). The further shrinking making the chosen point lie on every `D_i` is not asserted, nor is either implication of the equivalence.”.

> Around any point of the ambient scheme the normalization of `D` becomes, after an étale base
> change, a finite disjoint union of closed subschemes of the étale neighbourhood: the morphism
> `D^ν ⟶ X` is finite and unramified, so Tag 04HJ applies to it.

```lean
public theorem exists_etaleNeighborhood_disjoint_closed_decomposition_divisorNormalization
    [Unramified (divisorNormalization D)] (p : X) :
    ∃ (U : EtaleNeighborhood X p) (n : ℕ)
      (V : Fin n → (pullback (divisorNormalizationToAmbient D) U.toBase).Opens),
      sSup (Set.range V) = ⊤ ∧ Pairwise (Disjoint on V) ∧
        ∀ j, IsClosedImmersion
          ((V j).ι ≫ pullback.snd (divisorNormalizationToAmbient D) U.toBase)
```

**`Stacks.Divisors.normalizationDistinctOneIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationFiniteness.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationFiniteness.lean#L164). The attribute's comment: “the identification `Z_1 = D^ν` used in the proof of (2) to (1). Neither implication of the equivalence is asserted.”.

> The scheme `Z_1` is the normalization of `D` itself: a one-fold fibre power has empty fat
> diagonal and is the normalization.

```lean
public noncomputable def normalizationDistinctOneIso :
    normalizationDistinct D 1 ≅ divisorNormalizationScheme D
```

**`Stacks.Divisors.isRegular_divisorNormalizationScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationFiniteness.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationFiniteness.lean#L194). The attribute's comment: “the proof of (2) to (1), fourth step, partially: the hypothesis on `Z_1` makes `D^ν` regular. The conclusion that each `D_i` is an effective Cartier divisor is not asserted.”.

> Condition (2) of Tag 0CBR makes the normalization of `D` a regular scheme: it is the scheme
> `Z_1` of that condition.

```lean
public theorem isRegular_divisorNormalizationScheme (h : IsNormalizationCrossingsDivisor D) :
    IsRegular (divisorNormalizationScheme D)
```

**`Stacks.Divisors.isLocalCompleteIntersectionMorphism_divisorNormalizationToAmbient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationFiniteness.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/NormalizationFiniteness.lean#L210). The attribute's comment: “the proof of (2) to (1), fourth step, partially: the hypothesis on `Z_1` makes `D^ν ⟶ X` a local complete intersection morphism. The conclusion that each `D_i` is an effective Cartier divisor is not asserted.”.

> Condition (2) of Tag 0CBR makes `D^ν ⟶ X` a local complete intersection morphism: it is the
> morphism `Z_1 ⟶ X` of that condition, up to the identification of `Z_1` with the
> normalization.

```lean
public theorem isLocalCompleteIntersectionMorphism_divisorNormalizationToAmbient
    (h : IsNormalizationCrossingsDivisor D) :
    IsLocalCompleteIntersectionMorphism (divisorNormalizationToAmbient D)
```

## Tag 0CBS, a lemma

[Tag 0CBS](https://stacks.math.columbia.edu/tag/0CBS) in the Stacks Project.

**`Stacks.Divisors.isStrictNormalCrossingsDivisor_comap_fromSpecStalk_of_isNormalCrossingsDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/StrictHenselization.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/StrictHenselization.lean#L68). The attribute's comment: “(1) ⇒ (2)”.

> **The strict henselization of a normal crossings divisor has strict normal crossings.** For `D`
> a normal crossings divisor on a locally Noetherian scheme `X` and `x` a point of `D`, the pullback
> of `D` to the spectrum of a strict henselization of `𝒪_{X, x}` is a strict normal crossings
> divisor.

```lean
theorem isStrictNormalCrossingsDivisor_comap_fromSpecStalk_of_isNormalCrossingsDivisor
    {X : Scheme.{u}} [IsLocallyNoetherian X] (D : X.IdealSheafData)
    (hD : IsNormalCrossingsDivisor D) (x : X) (hx : ∃ y : D.subscheme, D.subschemeι y = x)
    (L : Type u) [Field L]
    [Algebra (IsLocalRing.ResidueField (X.presheaf.stalk x)) L]
    [IsSepClosure (IsLocalRing.ResidueField (X.presheaf.stalk x)) L]
    (Ash : Type u) [CommRing Ash] [IsLocalRing Ash]
    [Algebra (X.presheaf.stalk x) Ash]
    [IsLocalRing.IsHenselization (X.presheaf.stalk x) L Ash] :
    haveI : IsNoetherianRing Ash :=
      IsLocalRing.isNoetherianRing_of_isHenselization (A := X.presheaf.stalk x) L
    IsStrictNormalCrossingsDivisor (D.comap
      (Spec.map (CommRingCat.ofHom (algebraMap (X.presheaf.stalk x) Ash)) ≫
        X.fromSpecStalk x))
```

**`Stacks.Divisors.isStrictNormalCrossingsDivisor_of_exists_regular_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/StrictHenselizationCriterion.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/StrictHenselizationCriterion.lean#L75). The attribute's comment: “(2) ⇒ (1), the step that upgrades condition (2) to strict normal crossings once each local equation factors into regular factors. The construction of an étale chart on which it does, which is where the J-2 or Nagata hypothesis of the lemma enters, is not asserted.”.

> Let `D` be a closed subscheme of a locally Noetherian scheme `X` which has strict normal
> crossings at the strict henselizations, and suppose that at every point `p` of `D` the stalk ideal
> is generated by a product `f₁ ⋯ f_k` of at least one element with each quotient
> `𝒪_{X, p} / (fⱼ)` a regular local ring. Then `D` is a strict normal crossings divisor.
>
> In Tag 0CBS the factorization hypothesis is what the J-2 or Nagata assumption produces, by
> realizing a regular system of parameters of `𝒪^{sh}_{X, p}` on an étale neighbourhood and
> shrinking it so that each of the resulting divisors is regular.

```lean
theorem isStrictNormalCrossingsDivisor_of_exists_regular_factorization {X : Scheme.{u}}
    [IsLocallyNoetherian X] (D : X.IdealSheafData)
    (hD : IsStrictNormalCrossingsAtStrictHenselizations D)
    (hfac : ∀ x : X, x ∈ D.support → ∃ fs : List (X.presheaf.stalk x),
      (∀ f ∈ fs, IsRegularLocalRing ((X.presheaf.stalk x : Type u) ⧸ Ideal.span {f})) ∧
        1 ≤ fs.length ∧
        AlgebraicGeometry.IdealSheafData.stalk D x = Ideal.span {fs.prod}) :
    IsStrictNormalCrossingsDivisor D
```

**`Stacks.Divisors.isNormalCrossingsDivisor_iff_isStrictNormalCrossingsAtStrictHenselizations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/StrictHenselizationEquivalence.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/StrictHenselizationEquivalence.lean#L122).

> Let `X` be a locally Noetherian scheme and `D ⊂ X` a closed
> subscheme. If `X` is J-2 or Nagata, then `D` is a normal crossings divisor in `X` if and only if
> for every point `p` of `D` the pullback of `D` to the spectrum of the strict henselization
> `𝒪^{sh}_{X, p}` is a strict normal crossings divisor.

```lean
public theorem isNormalCrossingsDivisor_iff_isStrictNormalCrossingsAtStrictHenselizations
    {X : Scheme.{u}} [IsLocallyNoetherian X] (D : X.IdealSheafData)
    (hX : AlgebraicGeometry.Scheme.IsJ2 X ∨ IsNagataScheme X) :
    IsNormalCrossingsDivisor D ↔ IsStrictNormalCrossingsAtStrictHenselizations D
```

**`Stacks.Divisors.isEffectiveCartierDivisor_of_isStrictNormalCrossingsAtStrictHenselizations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/StrictHenselizationStalkIdeal.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/NormalCrossings/StrictHenselizationStalkIdeal.lean#L246). The attribute's comment: “(2) ⇒ (1), the effective Cartier divisor conjunct of condition (1). The étale-local strict normal crossings clause of (1) is not asserted, and no J-2 or Nagata hypothesis is used for this conjunct.”.

> **Stacks Project, Tag 0CBS, the effective Cartier divisor conjunct of (2) ⇒ (1).** A closed
> subscheme of a locally Noetherian scheme whose inverse image to the spectrum of a strict
> henselization of the local ring at each of its points is a strict normal crossings divisor is an
> effective Cartier divisor. No J-2 or Nagata hypothesis is needed for this conjunct: the local
> equation is recovered one point at a time by descent along the henselization.

```lean
theorem isEffectiveCartierDivisor_of_isStrictNormalCrossingsAtStrictHenselizations
    {X : Scheme.{u}} [IsLocallyNoetherian X] (D : X.IdealSheafData)
    (hD : IsStrictNormalCrossingsAtStrictHenselizations D) :
    IsEffectiveCartierDivisor D
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 41.21, Tag 0CBN](https://stacks.math.columbia.edu/tag/0CBN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
