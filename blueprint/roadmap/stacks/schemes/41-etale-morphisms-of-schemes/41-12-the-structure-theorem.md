---
declaration: section
origin: cited
lean: Algebra.exists_standardEtalePair_localization, Algebra.exists_standardEtalePair_localization_surjection, AlgebraicGeometry.exists_isOpenImmersion_specMap_derivativePair_of_etaleAt
statement: formalized
proof: formalized
---

# 41.12 The structure theorem

Section 41.12 of the Stacks Project, [Tag 025A](https://stacks.math.columbia.edu/tag/025A). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 025B, a theorem

[Tag 025B](https://stacks.math.columbia.edu/tag/025B) in the Stacks Project.

**`Algebra.exists_standardEtalePair_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/StructureTheorem.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/StructureTheorem.lean#L42).

> If `A → B` is an étale local homomorphism of Noetherian local rings, then `B` is isomorphic as
> an `A`-algebra to the localization of a standard étale `A`-algebra at a prime.

```lean
theorem exists_standardEtalePair_localization
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B] [Algebra A B]
    [IsLocalHom (algebraMap A B)]
    (h : RingHom.IsEtaleLocalHom (algebraMap A B)) :
    ∃ (P : StandardEtalePair A) (q : Ideal P.Ring) (hq : q.IsPrime),
      letI := hq
      Nonempty (B ≃ₐ[A] Localization.AtPrime q)
```

## Tag 039O, a theorem

[Tag 039O](https://stacks.math.columbia.edu/tag/039O) in the Stacks Project.

**`Algebra.exists_standardEtalePair_localization_surjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/UnramifiedStructure.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/UnramifiedStructure.lean#L33). References: SGA 1 I (7.7), “unramified ⇒ quotient”.

> An unramified local algebra over a local ring is a quotient of the localization at a prime of
> a standard étale algebra.

```lean
theorem exists_standardEtalePair_localization_surjection
    {A B : Type*} [CommRing A] [CommRing B] [Algebra A B]
    [IsLocalRing A] [IsLocalRing B] [IsLocalHom (algebraMap A B)]
    [Algebra.EssFiniteType A B] [Algebra.FormallyUnramified A B] :
    ∃ (P : StandardEtalePair A) (q : Ideal P.Ring) (hq : q.IsPrime),
      letI := hq
      ∃ φ : Localization.AtPrime q →ₐ[A] B, Function.Surjective φ
```

## Tag 025C, a theorem

[Tag 025C](https://stacks.math.columbia.edu/tag/025C) in the Stacks Project.

**`AlgebraicGeometry.exists_isOpenImmersion_specMap_derivativePair_of_etaleAt`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/LocalStructure.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/LocalStructure.lean#L383). The attribute's comment: “the étale local structure theorem”.

> **Stacks Project, Tag 0CBJ, étale case.** At a point where the morphism is étale, the
> immersion of `AlgebraicGeometry.exists_isImmersion_specMap_derivativePair_of_unramifiedAt` may
> be chosen to be an open immersion.

```lean
public lemma exists_isOpenImmersion_specMap_derivativePair_of_etaleAt
    {X S : Scheme.{u}} (f : X ⟶ S) (x : X) (V : S.Opens)
    (hV : IsAffineOpen V) (hxV : f x ∈ V) (hf : EtaleAt f x) :
    ∃ (U : X.Opens) (_ : IsAffineOpen U) (_ : x ∈ U)
      (hUV : U ≤ f ⁻¹ᵁ V) (P : StandardEtalePair Γ(S, V)),
      P.g = P.f.derivative ∧
        ∃ (j : U.toScheme ⟶ Spec (CommRingCat.of P.Ring)),
          IsOpenImmersion j ∧
            j ≫ Spec.map (CommRingCat.ofHom (aeval P.X).toRingHom) ≫
                Spec.map (CommRingCat.ofHom (Polynomial.C : Γ(S, V) →+* Γ(S, V)[X])) =
              f.resLE V U hUV ≫ hV.isoSpec.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 41.12, Tag 025A](https://stacks.math.columbia.edu/tag/025A)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
