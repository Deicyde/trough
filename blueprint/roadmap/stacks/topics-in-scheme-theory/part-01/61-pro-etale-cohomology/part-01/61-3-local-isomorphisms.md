---
declaration: section
origin: cited
lean: Algebra.IdentifiesLocalRings, AlgebraicGeometry.ProEtale.identifiesLocalRings_tensorProduct, Algebra.IsLocalIso.instTensorProduct, Algebra.IdentifiesLocalRings.trans, Algebra.IsLocalIso.trans, AlgebraicGeometry.ProEtale.isLocalIso_of_left_of_comp, AlgebraicGeometry.ProEtale.identifiesLocalRings_of_left_of_comp, Algebra.IdentifiesLocalRings.of_isLocalIso
statement: formalized
proof: formalized
---

# 61.3 Local isomorphisms

Section 61.3 of the Stacks Project, [Tag 096D](https://stacks.math.columbia.edu/tag/096D). 8 tags here are carried by 10 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 096E, a definition

[Tag 096E](https://stacks.math.columbia.edu/tag/096E) in the Stacks Project.

**`Algebra.IdentifiesLocalRings`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalIso/IdentifiesLocalRings.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalIso/IdentifiesLocalRings.lean#L58). The attribute's comment: “part (2): identifies local rings”.

> An algebra *identifies local rings* if for every prime `q` of the target the canonical map
> from the localization of the source at the preimage of `q` to the localization of the target at
> `q` is an isomorphism.

```lean
abbrev IdentifiesLocalRings (R S : Type*) [CommSemiring R] [CommSemiring S] [Algebra R S] :
    Prop
```

## Tag 096F, a lemma

[Tag 096F](https://stacks.math.columbia.edu/tag/096F) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.identifiesLocalRings_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/LocalIso/BaseChange.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/LocalIso/BaseChange.lean#L124). The attribute's comment: “identifies_local_rings_base_change”.

> **Stacks Project, Tag 096F.** Base change preserves the property of identifying local
> rings.

```lean
theorem identifiesLocalRings_tensorProduct
    (A B A' : Type*) [CommRing A] [CommRing B] [CommRing A']
    [Algebra A B] [Algebra A A']
    (h : Algebra.IdentifiesLocalRings A B) :
    Algebra.IdentifiesLocalRings A' (A' ⊗[A] B)
```

Declarations registered for the tag:

- [`Algebra.IsLocalIso.instTensorProduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.IsLocalIso.instTensorProduct#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/LocalIso/BaseChange.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/LocalIso/BaseChange.lean#L133) (StacksFrontier): “local_isomorphism_base_change”. References: EGA I (4.5.5), “(iii), special case”.

## Tag 096G, a lemma

[Tag 096G](https://stacks.math.columbia.edu/tag/096G) in the Stacks Project.

**`Algebra.IdentifiesLocalRings.trans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WContractibleBasis/IdentifiesLocalRings.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WContractibleBasis/IdentifiesLocalRings.lean#L147). The attribute's comment: “(2)”.

> If `R → S` and `S → T` identify local rings, then so does `R → T`.

```lean
public theorem trans (hRS : Algebra.IdentifiesLocalRings R S)
    (hST : Algebra.IdentifiesLocalRings S T) :
    Algebra.IdentifiesLocalRings R T
```

Declarations registered for the tag:

- [`Algebra.IsLocalIso.trans`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.IsLocalIso.trans#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/LocalIso/Permanence.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/LocalIso/Permanence.lean#L237) (StacksFrontier): “(1)”. References: EGA I (4.5.5), “(i), special case”.

## Tag 096H, a lemma

[Tag 096H](https://stacks.math.columbia.edu/tag/096H) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.isLocalIso_of_left_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/LocalIso/Permanence.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/LocalIso/Permanence.lean#L71). The attribute's comment: “local_isomorphism_permanence”.

> **Stacks Project, Tag 096H.** If the base-to-middle and base-to-top maps of an algebra
> tower are local isomorphisms, then so is the middle-to-top map.

```lean
theorem isLocalIso_of_left_of_comp
    (A B C : Type*) [CommSemiring A] [CommSemiring B] [CommSemiring C]
    [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
    [Algebra.IsLocalIso A B] [Algebra.IsLocalIso A C] :
    Algebra.IsLocalIso B C
```

**`AlgebraicGeometry.ProEtale.identifiesLocalRings_of_left_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/LocalIso/Permanence.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/LocalIso/Permanence.lean#L197). The attribute's comment: “identifies_local_rings_permanence”.

> **Stacks Project, Tag 096H.** In an algebra tower, if the base-to-middle and base-to-top
> maps identify local rings, then so does the middle-to-top map.

```lean
theorem identifiesLocalRings_of_left_of_comp
    (A B C : Type*) [CommSemiring A] [CommSemiring B] [CommSemiring C]
    [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
    (hAB : Algebra.IdentifiesLocalRings A B)
    (hAC : Algebra.IdentifiesLocalRings A C) :
    Algebra.IdentifiesLocalRings B C
```

## Tag 096I, a lemma

[Tag 096I](https://stacks.math.columbia.edu/tag/096I) in the Stacks Project.

**`Algebra.IdentifiesLocalRings.of_isLocalIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WContractibleBasis/IdentifiesLocalRings.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WContractibleBasis/IdentifiesLocalRings.lean#L117). The attribute's comment: “(2)”.

> A local isomorphism identifies local rings.

```lean
public theorem of_isLocalIso [Algebra.IsLocalIso R S] : Algebra.IdentifiesLocalRings R S
```

**`Algebra.IsLocalIso.quasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WContractibleBasis/LocalIso.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WContractibleBasis/LocalIso.lean#L68). The attribute's comment: “(3)”.

> **A local isomorphism is quasi-finite**: it is of finite type, every fibre ring
> `κ(p) ⊗[A] B` is a finite `κ(p)`-module, and it is quasi-finite at every prime of `B`. All three
> come from `Algebra.IsLocalIso.etale`, an étale algebra being of finite presentation and formally
> unramified.

```lean
public theorem quasiFinite [Algebra.IsLocalIso A B] :
    Algebra.FiniteType A B ∧ Algebra.QuasiFinite A B ∧
      ∀ (q : Ideal B) [q.IsPrime], Algebra.QuasiFiniteAt A q
```

Declarations registered for the tag:

- [`Algebra.IsLocalIso.etale`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski.lean#L170), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/WContractibleBasis/LocalIso.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WContractibleBasis/LocalIso.lean#L51) (StacksFrontier): “(1)”.

## Tag 096J, a lemma

[Tag 096J](https://stacks.math.columbia.edu/tag/096J) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exists_fin_localization_away`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/LocalIsomorphism.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/LocalIsomorphism.lean#L55).

> A local isomorphism admits a finite cover by principal localizations that
> are principal localizations of the source.

```lean
theorem exists_fin_localization_away
    (A : Type u) (B : Type v) [CommSemiring A] [CommSemiring B]
    [Algebra A B] [Algebra.IsLocalIso A B] :
    ∃ (n : ℕ) (g : Fin n → B) (f : Fin n → A),
      Ideal.span (Set.range g) = ⊤ ∧
        ∀ i, IsLocalization.Away (f i) (Localization.Away (g i))
```

## Tag 096K, a lemma

[Tag 096K](https://stacks.math.columbia.edu/tag/096K) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.bijective_forgetToTop_morphism_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/InverseImageStructureSheaf.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/InverseImageStructureSheaf.lean#L241).

> If the structure sheaf of `Y` is the inverse image of that of `X`, then
> forgetting the sheaf map bijects morphisms `Z ⟶ Y` over `X` with continuous
> maps between the underlying spaces over `X`.

```lean
theorem bijective_forgetToTop_morphism_over
    {X Y Z : LocallyRingedSpace.{u}}
    (p : Y ⟶ X) (q : Z ⟶ X)
    [IsIso (inverseImageStructureMap p)] :
    Function.Bijective
      (fun f : {f : Z ⟶ Y // f ≫ p = q} ↦
        (⟨f.1.base, congrArg (fun k : Z ⟶ X ↦ k.base) f.2⟩ :
          {g : Z.toTopCat ⟶ Y.toTopCat // g ≫ p.base = q.base}))
```

## Tag 096L, a lemma

[Tag 096L](https://stacks.math.columbia.edu/tag/096L) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.existsUnique_algHom_of_specTopMap_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/LocalIso/SpectrumFullyFaithful.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/LocalIso/SpectrumFullyFaithful.lean#L136).

> **Stacks Project, Tag 096L.** A continuous map of affine spectra over `Spec A` is uniquely
> induced by an `A`-algebra homomorphism when the structural map of its target identifies local
> rings.

```lean
theorem existsUnique_algHom_of_specTopMap_over
    (A B C : Type u) [CommRing A] [CommRing B] [CommRing C]
    [Algebra A B] [Algebra A C]
    (hB : Algebra.IdentifiesLocalRings A B)
    (g : Spec.topObj (CommRingCat.of C) ⟶ Spec.topObj (CommRingCat.of B))
    (hg : g ≫ Spec.topMap (CommRingCat.ofHom (algebraMap A B)) =
      Spec.topMap (CommRingCat.ofHom (algebraMap A C))) :
    ∃! f : B →ₐ[A] C, Spec.topMap (CommRingCat.ofHom f.toRingHom) = g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.3, Tag 096D](https://stacks.math.columbia.edu/tag/096D)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
