---
declaration: section
origin: cited
lean: RingHom.QuotientDiagram.isTaut_iff_hasQuotientDiagram, TopologicalRing.isTaut_localizationPreserves, TopologicalRing.isTaut_faithfullyFlatDescent, TopologicalRing.isTaut_finiteProductPreserves, TopologicalRing.isTaut_isomorphismInvariant, TopologicalRing.isTaut_completedMap_of_isTaut, TopologicalRing.isTaut_map_of_isTaut_completedMap, TopologicalRing.isTaut_pi
statement: formalized
proof: formalized
---

# 87.22 Taut ring maps and representability by algebraic spaces

Section 87.22 of the Stacks Project, [Tag 0GBQ](https://stacks.math.columbia.edu/tag/0GBQ). 2 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ANJ, a lemma

[Tag 0ANJ](https://stacks.math.columbia.edu/tag/0ANJ) in the Stacks Project.

**`RingHom.QuotientDiagram.isTaut_iff_hasQuotientDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/QuotientDiagram.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/QuotientDiagram.lean#L303). The attribute's comment: “taut\_iff\_quotient\_diagram”.

> A continuous arrow of weakly admissible linearly topologized rings is taut if and only if
> its canonical quotients along any chosen decreasing fundamental sequence form the quotient
> diagram whose topological inverse limit is the target.

```lean
public theorem isTaut_iff_hasQuotientDiagram {A B : Type*}
    [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    (f : B →+* A) (hf : Continuous f)
    (hA : TopologicalRing.IsWeaklyAdmissible A) (hB : TopologicalRing.IsWeaklyAdmissible B)
    (J : ℕ → Ideal B) (hJ : IsFundamentalSequence J) :
    RingHom.IsTaut f ↔ HasQuotientDiagram f J hJ.2.1
```

**`TopologicalRing.isTaut_localizationPreserves`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/TautIsLocal.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/TautIsLocal.lean#L200). The attribute's comment: “taut\_is\_local\_property”.

> Tautness ascends along a completed étale localization diagram of countably indexed weakly
> admissible rings.

```lean
public theorem isTaut_localizationPreserves :
    LocalizationPreserves.{u} IsCountablyWeaklyAdmissible
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
        (f : B →+* A) ↦ RingHom.IsTaut f)
```

**`TopologicalRing.isTaut_faithfullyFlatDescent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/TautIsLocal.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/TautIsLocal.lean#L216). The attribute's comment: “taut\_is\_local\_property”.

> Tautness descends along a completed étale localization diagram whose upper horizontal ring
> map is faithfully flat.

```lean
public theorem isTaut_faithfullyFlatDescent :
    FaithfullyFlatDescent.{u} IsCountablyWeaklyAdmissible
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
        (f : B →+* A) ↦ RingHom.IsTaut f)
```

**`TopologicalRing.isTaut_finiteProductPreserves`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/TautIsLocal.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/TautIsLocal.lean#L251). The attribute's comment: “taut\_is\_local\_property”.

> Tautness is preserved by finite products of targets.

```lean
public theorem isTaut_finiteProductPreserves :
    FiniteProductPreserves.{u} IsCountablyWeaklyAdmissible
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
        (f : B →+* A) ↦ RingHom.IsTaut f)
```

**`TopologicalRing.isTaut_isomorphismInvariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/TautIsLocalRefined.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/TautIsLocalRefined.lean#L69). The attribute's comment: “taut\_is\_local\_property”.

> Tautness does not depend on the chosen presentations of the source and the target of a
> continuous homomorphism: pre- and post-composing with bicontinuous ring isomorphisms preserves
> and reflects tautness.

```lean
public theorem isTaut_isomorphismInvariant :
    IsomorphismInvariant.{u}
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
        (f : B →+* A) ↦ RingHom.IsTaut f)
      IsCountablyWeaklyAdmissible
```

**`TopologicalRing.isTaut_completedMap_of_isTaut`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/TautIsLocalUnconditional.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/TautIsLocalUnconditional.lean#L59). The attribute's comment: “axiom 0AND for tautness, the completed corners in WAdm^count by 0ANB”.

> **Stacks 0ANJ**, axiom 0AND for tautness, with the hypotheses of Situation 0CBA only.
> Given a diagram (0ANC) — `A`, `B` countably indexed weakly admissible, `A → A'` and `B → B'`
> étale, `φ : B → A` and `φ' : (B')^∧ → (A')^∧` continuous and commuting with the canonical
> maps — if `φ` is taut then so is `φ'`. The completed corners `(A')^∧` and `(B')^∧` are objects of
> `WAdm^{count}` by Stacks 0ANB (`isCountablyWeaklyAdmissible_completionOver`), which is how the
> source reads the axiom.

```lean
public theorem isTaut_completedMap_of_isTaut {A B A' B' : Type u}
    [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [CommRing A'] [CommRing B'] (D : LocalizationDiagram A B A' B')
    (h : RingHom.IsTaut D.map) : RingHom.IsTaut D.completedMap
```

**`TopologicalRing.isTaut_map_of_isTaut_completedMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/TautIsLocalUnconditional.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/TautIsLocalUnconditional.lean#L74). The attribute's comment: “axiom 0ANE for tautness, the completed corners in WAdm^count by 0ANB”.

> **Stacks 0ANJ**, axiom 0ANE for tautness, with the hypotheses of Situation 0CBA only.
> Given a diagram (0ANC) whose map `A → A'` is faithfully flat, if `φ' : (B')^∧ → (A')^∧` is taut
> then so is `φ : B → A`. The completed corners are objects of `WAdm^{count}` by Stacks 0ANB
> (`isCountablyWeaklyAdmissible_completionOver`).

```lean
public theorem isTaut_map_of_isTaut_completedMap {A B A' B' : Type u}
    [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [CommRing A'] [CommRing B'] (D : LocalizationDiagram A B A' B')
    (hff : D.toA'.FaithfullyFlat) (h : RingHom.IsTaut D.completedMap) :
    RingHom.IsTaut D.map
```

**`TopologicalRing.isTaut_pi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/TautIsLocalUnconditional.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/TautIsLocalUnconditional.lean#L89). The attribute's comment: “axiom 0ANF for tautness”.

> **Stacks 0ANJ**, axiom 0ANF for tautness, stated once: if `B → A_i` are taut arrows of
> `WAdm^{count}` for `i` in a finite index set, then `B → ∏ A_i` is taut.

```lean
public theorem isTaut_pi {B : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B] (hB : IsCountablyWeaklyAdmissible B)
    {ι : Type u} [Fintype ι] (A : ι → Type u)
    [∀ i, CommRing (A i)] [∀ i, TopologicalSpace (A i)]
    [∀ i, IsTopologicalRing (A i)] [∀ i, IsLinearTopology (A i) (A i)]
    (hA : ∀ i, IsCountablyWeaklyAdmissible (A i))
    (f : ∀ i, B →+* A i) (hf : ∀ i, Continuous (f i)) (h : ∀ i, RingHom.IsTaut (f i)) :
    RingHom.IsTaut (RingHom.pi f)
```

## Tag 0ANK, a lemma

[Tag 0ANK](https://stacks.math.columbia.edu/tag/0ANK) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isTaut_tfae_isRepresentableByAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TautMorphismRepresentability.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/TautMorphismRepresentability.lean#L220). The attribute's comment: “the equivalence, with the five inputs this library does not carry as named hypotheses: Stacks 0AJ3 as h0AJ3, the implication (2) implies (1) of Stacks 0AKX for the countably indexed property as h0AKX, the equivalence of conditions (1) and (3) of Stacks 0AN5 read on countably indexed affine charts as h0AN5, Stacks 0AQ0 as h0AQ0, and the implication (5) implies (1) of Stacks 0AN4 as h0AN4”.

> **Stacks 0ANK.** Let `f : X ⟶ Y` be a morphism of locally countably indexed formal
> algebraic spaces over `S`. The following are equivalent:
>
> 1. every commutative square with affine formal algebraic spaces `U`, `V` and representable
>    étale maps `U ⟶ X`, `V ⟶ Y` has `U ⟶ V` given by a taut continuous homomorphism of
>    countably indexed weakly admissible topological rings;
> 2. there is a covering `{Vⱼ ⟶ Y}` as in Definition 0AIM and for each `j` a covering
>    `{Uᵢ ⟶ Vⱼ ×_Y X}` as in Definition 0AIM with each `Uᵢ ⟶ Vⱼ` given by such a taut map;
> 3. there is a covering `{Uᵢ ⟶ X}` as in Definition 0AIM and for each `i` a factorization
>    `Uᵢ ⟶ Vᵢ ⟶ Y` through an affine formal algebraic space representable étale over `Y` with
>    `Uᵢ ⟶ Vᵢ` given by such a taut map;
> 4. `f` is representable by algebraic spaces.
>
> The cycle runs `(1) ⟹ (2) ⟹ (3) ⟹ (4) ⟹ (1)`: the first step is Stacks 0ANG, the second is
> proved here, and the last two pass between tautness and representability on charts through
> Stacks 0AN5 and between charts and `f` through Stacks 0AN4.

```lean
theorem isTaut_tfae_isRepresentableByAlgebraicSpaces {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyCountablyIndexed B S hS X) (hY : IsLocallyCountablyIndexed B S hS Y)
    (h0AJ3 : ∀ (V : FppfSheaf B S hS) (v : V ⟶ Y), IsAffineFormalAlgebraicSpace B S hS V →
      IsRepresentableEtale B S hS v → IsFormalAlgebraicSpace B S hS (pullback v f))
    (h0AKX : ∀ (Z : FppfSheaf B S hS), IsLocallyCountablyIndexed B S hS Z →
      ∀ (U : FppfSheaf B S hS) (a : U ⟶ Z), IsAffineFormalAlgebraicSpace B S hS U →
      IsRepresentableEtale B S hS a → IsCountablyIndexed B S hS U)
    (h0AN5 : ∀ {U V : FppfSheaf B S hS} (t : U ⟶ V),
      IsAffineFormalAlgebraicSpace B S hS U → IsAffineFormalAlgebraicSpace B S hS V →
      IsCountablyIndexed B S hS U → IsCountablyIndexed B S hS V →
      (Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS t.hom ↔
        HasPropertyOnAffineChartMap B S hS TopologicalRing.IsCountablyWeaklyAdmissible
          TautChartProperty t))
    (h0AQ0 : ∀ {A A' A'' : FppfSheaf B S hS} (s : A ⟶ A') (r : A' ⟶ A''),
      IsFormalAlgebraicSpace B S hS A → IsFormalAlgebraicSpace B S hS A' →
      IsFormalAlgebraicSpace B S hS A'' →
      Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (s ≫ r).hom →
      Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS s.hom)
    (h0AN4 : ∀ (I : Type (u + 1)) (U W : I → FppfSheaf B S hS) (a : ∀ i, U i ⟶ X)
      (b : ∀ i, W i ⟶ Y) (t : ∀ i, U i ⟶ W i), IsAffineEtaleCover B S hS U a →
      (∀ i, IsAffineFormalAlgebraicSpace B S hS (W i)) →
      (∀ i, Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (b i).hom) →
      (∀ i, Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (t i).hom) →
      (∀ i, a i ≫ f = t i ≫ b i) →
      Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom) :
    List.TFAE
      [ IsTautOnEveryAffineEtaleDiagram B S hS f,
        IsTautAfterTargetCover B S hS f,
        IsTautAfterSourceCover B S hS f,
        Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom ]
```

**`AlgebraicGeometry.FormalSpace.tfae_isTautOnEveryAffineEtaleDiagram_isRepresentableByAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TautMorphismRepresentabilityUnconditional.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/TautMorphismRepresentabilityUnconditional.lean#L92).

> **Stacks 0ANK.** Let `f : X ⟶ Y` be a morphism of locally countably indexed formal
> algebraic spaces over `S`. The following are equivalent:
>
> 1. every commutative square with affine formal algebraic spaces `U`, `V` and representable
>    étale maps `U ⟶ X`, `V ⟶ Y` has `U ⟶ V` given by a taut continuous homomorphism of
>    countably indexed weakly admissible topological rings;
> 2. there is a covering `{Vⱼ ⟶ Y}` as in Definition 0AIM and for each `j` a covering
>    `{Uᵢ ⟶ Vⱼ ×_Y X}` as in Definition 0AIM with each `Uᵢ ⟶ Vⱼ` given by such a taut map;
> 3. there is a covering `{Uᵢ ⟶ X}` as in Definition 0AIM and for each `i` a factorization
>    `Uᵢ ⟶ Vᵢ ⟶ Y` through an affine formal algebraic space representable étale over `Y` with
>    `Uᵢ ⟶ Vᵢ` given by such a taut map;
> 4. `f` is representable by algebraic spaces.

```lean
theorem tfae_isTautOnEveryAffineEtaleDiagram_isRepresentableByAlgebraicSpaces
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyCountablyIndexed B S hS X) (hY : IsLocallyCountablyIndexed B S hS Y) :
    List.TFAE
      [ IsTautOnEveryAffineEtaleDiagram B S hS f,
        IsTautAfterTargetCover B S hS f,
        IsTautAfterSourceCover B S hS f,
        Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom ]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.22, Tag 0GBQ](https://stacks.math.columbia.edu/tag/0GBQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
