---
declaration: section
origin: cited
lean: IsSeminormalRing, IsAbsolutelyWeaklyNormalRing, isSeminormalRing_propertyIsLocal, isAbsolutelyWeaklyNormalRing_propertyIsLocal, AlgebraicGeometry.IsSeminormal, AlgebraicGeometry.IsAbsolutelyWeaklyNormal, AlgebraicGeometry.isSeminormal_tfae, AlgebraicGeometry.isSeminormal_open
statement: formalized
proof: formalized
---

# 29.48 Absolute weak normalization and seminormalization

Section 29.48 of the Stacks Project, [Tag 0EUK](https://stacks.math.columbia.edu/tag/0EUK). 10 tags here are carried by 37 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EUL, a definition

[Tag 0EUL](https://stacks.math.columbia.edu/tag/0EUL) in the Stacks Project.

**`IsSeminormalRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Ring.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Ring.lean#L50). The attribute's comment: “part (1)”.

> A commutative ring is seminormal if every `x, y` with `x ^ 3 = y ^ 2` are uniquely the
> square and cube of a common element.
>
> Use `isSeminormalRing_iff` to rewrite this predicate and
> `IsSeminormalRing.existsUnique_of_cube_eq_square` to apply its defining condition.

```lean
def IsSeminormalRing (A : Type*) [CommRing A] : Prop
```

**`IsAbsolutelyWeaklyNormalRing`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Ring.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Ring.lean#L74). The attribute's comment: “part (2)”.

> A commutative ring is absolutely weakly normal if it is seminormal and, for every prime
> number `p`, every solution of `p ^ p * x = y ^ p` uniquely has the prescribed form
> `x = a ^ p`, `y = p * a`.
>
> Use `isAbsolutelyWeaklyNormalRing_iff` to rewrite this predicate,
> `IsAbsolutelyWeaklyNormalRing.isSeminormalRing` for its seminormal part, and
> `IsAbsolutelyWeaklyNormalRing.existsUnique_of_prime_pow_mul_eq_pow` for its prime-root
> condition.

```lean
abbrev IsAbsolutelyWeaklyNormalRing (A : Type*) [CommRing A] : Prop
```

## Tag 0EUM, a lemma

[Tag 0EUM](https://stacks.math.columbia.edu/tag/0EUM) in the Stacks Project.

**`isSeminormalRing_propertyIsLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Local.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Local.lean#L130). The attribute's comment: “seminormal_local_property”.

> Seminormality is a local property of commutative rings.

```lean
theorem isSeminormalRing_propertyIsLocal :
    CommRing.PropertyIsLocal
      (fun (R : Type u) [CommRing R] => IsSeminormalRing R)
```

**`isAbsolutelyWeaklyNormalRing_propertyIsLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Local.lean, line 445](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Local.lean#L445). The attribute's comment: “absolutely_weakly_normal_local_property”.

> Being an absolutely weakly normal commutative ring is a local property of rings.

```lean
theorem isAbsolutelyWeaklyNormalRing_propertyIsLocal :
    CommRing.PropertyIsLocal
      (fun (R : Type u) [CommRing R] => IsAbsolutelyWeaklyNormalRing R)
```

## Tag 0EUN, a definition

[Tag 0EUN](https://stacks.math.columbia.edu/tag/0EUN) in the Stacks Project.

**`AlgebraicGeometry.IsSeminormal`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Scheme.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Scheme.lean#L49). The attribute's comment: “part (1)”.

> A scheme is seminormal if every point has an affine open neighbourhood whose ring of
> sections is seminormal.

```lean
abbrev IsSeminormal (X : Scheme.{u}) : Prop
```

**`AlgebraicGeometry.IsAbsolutelyWeaklyNormal`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Scheme.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Scheme.lean#L55). The attribute's comment: “part (2)”.

> A scheme is absolutely weakly normal if every point has an affine open neighbourhood
> whose ring of sections is absolutely weakly normal.

```lean
abbrev IsAbsolutelyWeaklyNormal (X : Scheme.{u}) : Prop
```

## Tag 0EUP, a lemma

[Tag 0EUP](https://stacks.math.columbia.edu/tag/0EUP) in the Stacks Project.

**`AlgebraicGeometry.isSeminormal_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/SeminormalLocalCriteria.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/SeminormalLocalCriteria.lean#L50). The attribute's comment: “seminormal equivalent conditions”.

> A scheme is seminormal if and only if the section ring of every affine open is seminormal,
> if and only if this holds on an affine open covering, if and only if the scheme has an open
> covering by seminormal open subschemes.

```lean
public theorem isSeminormal_tfae (X : Scheme.{u}) :
    List.TFAE [
      IsSeminormal X,
      ∀ U : X.affineOpens, IsSeminormalRing Γ(X, U.val),
      ∃ (I : Type u) (U : I → X.affineOpens),
        (⨆ i, (U i).val) = ⊤ ∧ ∀ i, IsSeminormalRing Γ(X, (U i).val),
      ∃ (I : Type u) (U : I → X.Opens),
        (⨆ i, U i) = ⊤ ∧ ∀ i, IsSeminormal (U i).toScheme]
```

**`AlgebraicGeometry.isSeminormal_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/SeminormalLocalCriteria.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/SeminormalLocalCriteria.lean#L65). The attribute's comment: “seminormal open subschemes”.

> Every open subscheme of a seminormal scheme is seminormal.

```lean
public theorem isSeminormal_open {X : Scheme.{u}} (hX : IsSeminormal X)
    (U : X.Opens) : IsSeminormal U.toScheme
```

**`AlgebraicGeometry.isAbsolutelyWeaklyNormal_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/SeminormalLocalCriteria.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/SeminormalLocalCriteria.lean#L73). The attribute's comment: “absolutely weakly normal equivalent conditions”.

> A scheme is absolutely weakly normal if and only if the section ring of every affine open is
> absolutely weakly normal, if and only if this holds on an affine open covering, if and only if
> the scheme has an open covering by absolutely weakly normal open subschemes.

```lean
public theorem isAbsolutelyWeaklyNormal_tfae (X : Scheme.{u}) :
    List.TFAE [
      IsAbsolutelyWeaklyNormal X,
      ∀ U : X.affineOpens, IsAbsolutelyWeaklyNormalRing Γ(X, U.val),
      ∃ (I : Type u) (U : I → X.affineOpens),
        (⨆ i, (U i).val) = ⊤ ∧ ∀ i, IsAbsolutelyWeaklyNormalRing Γ(X, (U i).val),
      ∃ (I : Type u) (U : I → X.Opens),
        (⨆ i, U i) = ⊤ ∧ ∀ i, IsAbsolutelyWeaklyNormal (U i).toScheme]
```

**`AlgebraicGeometry.isAbsolutelyWeaklyNormal_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/SeminormalLocalCriteria.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/SeminormalLocalCriteria.lean#L90). The attribute's comment: “absolutely weakly normal open subschemes”.

> Every open subscheme of an absolutely weakly normal scheme is absolutely weakly normal.

```lean
public theorem isAbsolutelyWeaklyNormal_open {X : Scheme.{u}}
    (hX : IsAbsolutelyWeaklyNormal X) (U : X.Opens) :
    IsAbsolutelyWeaklyNormal U.toScheme
```

## Tag 0EUQ, a lemma

[Tag 0EUQ](https://stacks.math.columbia.edu/tag/0EUQ) in the Stacks Project.

**`seminormalRing_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Ring.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Ring.lean#L98). The attribute's comment: “seminormal rings”.

> **Stacks Project, Tag 0EUQ.** A seminormal commutative ring is reduced.

```lean
theorem seminormalRing_isReduced {A : Type*} [CommRing A]
    (hA : IsSeminormalRing A) : IsReduced A
```

**`absolutelyWeaklyNormalRing_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Ring.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Ring.lean#L106). The attribute's comment: “absolutely weakly normal rings”.

> **Stacks Project, Tag 0EUQ.** An absolutely weakly normal commutative ring is reduced.

```lean
theorem absolutelyWeaklyNormalRing_isReduced {A : Type*} [CommRing A]
    (hA : IsAbsolutelyWeaklyNormalRing A) : IsReduced A
```

**`AlgebraicGeometry.seminormal_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Scheme.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Scheme.lean#L60). The attribute's comment: “seminormal schemes”.

> **Stacks Project, Tag 0EUQ.** A seminormal scheme is reduced.

```lean
theorem seminormal_isReduced {X : Scheme.{u}} (hX : IsSeminormal X) :
    IsReduced X
```

**`AlgebraicGeometry.absolutelyWeaklyNormal_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Scheme.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Scheme.lean#L68). The attribute's comment: “absolutely weakly normal schemes”.

> **Stacks Project, Tag 0EUQ.** An absolutely weakly normal scheme is reduced.

```lean
theorem absolutelyWeaklyNormal_isReduced {X : Scheme.{u}}
    (hX : IsAbsolutelyWeaklyNormal X) : IsReduced X
```

## Tag 0EUR, a lemma

[Tag 0EUR](https://stacks.math.columbia.edu/tag/0EUR) in the Stacks Project.

**`AlgebraicGeometry.isIso_lift_to_absoluteWeakNormalization_iff_isAbsolutelyWeaklyNormalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AbsoluteWeakNormalizationCharacterization/Basic.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AbsoluteWeakNormalizationCharacterization/Basic.lean#L243). The attribute's comment: “awn_characterization”.

> A universally homeomorphic `A`-algebra is the absolute weak normalization of `A`
> precisely when its underlying ring is absolutely weakly normal.

```lean
public theorem isIso_lift_to_absoluteWeakNormalization_iff_isAbsolutelyWeaklyNormalRing
    (A B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    (huniv : UniversalHomeomorphism
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B)).op)) :
    IsIso ((absoluteWeakNormalizationCategoryObject_isTerminal A).from
      (⟨CommAlgCat.of A B, huniv⟩ :
        AbsoluteWeakNormalizationCategory A)) ↔
      IsAbsolutelyWeaklyNormalRing B
```

**`AlgebraicGeometry.existsUnique_absoluteWeakNormalizationMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AbsoluteWeakNormalizationFunctorial/Basic.lean, line 478](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AbsoluteWeakNormalizationFunctorial/Basic.lean#L478). The attribute's comment: “awn_functoriality”.

> A ring homomorphism induces a unique compatible homomorphism between absolute weak
> normalizations.

```lean
public theorem existsUnique_absoluteWeakNormalizationMap
    {A : Type u} {A' : Type v} [CommRing A] [CommRing A'] (φ : A →+* A') :
    ∃! φawn : AbsoluteWeakNormalization A →+* AbsoluteWeakNormalization A',
      φawn.comp (algebraMap A (AbsoluteWeakNormalization A)) =
        (algebraMap A' (AbsoluteWeakNormalization A')).comp φ
```

**`AlgebraicGeometry.absoluteWeakNormalizationCategoryObject_isTerminal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AbsoluteWeakNormalizationTerminal/Basic.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AbsoluteWeakNormalizationTerminal/Basic.lean#L270). The attribute's comment: “awn_final”.

> The absolute weak normalization of `A` is final among `A`-algebras which give universal
> homeomorphisms on spectra.

```lean
public noncomputable def absoluteWeakNormalizationCategoryObject_isTerminal
    (A : Type u) [CommRing A] :
    IsTerminal (absoluteWeakNormalizationCategoryObject A)
```

**`Algebra.seminormalization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RingColimit.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RingColimit.lean#L135). The attribute's comment: “seminormalization_of_a_ring”.

> The seminormalization `Aˢⁿ` is the colimit of the finitely presented `A`-algebras
> which induce a universal homeomorphism on spectra and isomorphisms on residue fields. Its
> `A`-algebra structure is the canonical map `A → Aˢⁿ`.

```lean
def seminormalization (A : Type u) [CommRing A] : CommAlgCat.{u} A
```

**`Algebra.AbsoluteWeakNormalizationIndex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RingColimit.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RingColimit.lean#L164). The attribute's comment: “absolute_weak_normalization_of_a_ring”.

> A small category of representatives of finitely presented `A`-algebras whose maps on
> spectra are universal homeomorphisms.

```lean
abbrev AbsoluteWeakNormalizationIndex (A : Type u) [CommRing A] : Type u
```

**`Algebra.AbsoluteWeakNormalization`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RingColimit.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RingColimit.lean#L195). The attribute's comment: “absolute_weak_normalization_of_a_ring”.

> The absolute weak normalization `Aᵃʷⁿ` is the colimit of all finitely presented
> `A`-algebras whose maps on spectra are universal homeomorphisms. Its inherited `A`-algebra
> structure supplies the canonical map `A → Aᵃʷⁿ`.

```lean
abbrev AbsoluteWeakNormalization (A : Type u) [CommRing A] : Type u
```

**`AlgebraicGeometry.seminormalizationAlgebraObject_isTerminal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SeminormalizationAffineInitial/Basic.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SeminormalizationAffineInitial/Basic.lean#L135). The attribute's comment: “sn_final”.

> **Stacks 0EUR.** The seminormalization of `A` is terminal among the `A`-algebras whose
> spectrum morphism is a universal homeomorphism inducing isomorphisms on all residue fields.

```lean
def seminormalizationAlgebraObject_isTerminal :
    IsTerminal (seminormalizationAlgebraObject A)
```

**`AlgebraicGeometry.existsUnique_seminormalizationMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SeminormalizationRingFunctorial/Basic.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SeminormalizationRingFunctorial/Basic.lean#L359). The attribute's comment: “sn_functoriality”.

> **Stacks 0EUR.** A ring homomorphism induces a unique compatible homomorphism between the
> seminormalizations of its source and target.

```lean
theorem existsUnique_seminormalizationMap
    {A : Type u} {A' : Type v} [CommRing A] [CommRing A'] (φ : A →+* A') :
    ∃! φsn : Algebra.seminormalization A →+* Algebra.seminormalization A',
      φsn.comp (algebraMap A (Algebra.seminormalization A)) =
        (algebraMap A' (Algebra.seminormalization A')).comp φ
```

**`AlgebraicGeometry.isIso_lift_to_seminormalization_iff_isSeminormalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SnCharacterization/Basic.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SnCharacterization/Basic.lean#L104). The attribute's comment: “sn_characterization”.

> **Stacks 0EUR.** A subintegral `A`-algebra is the seminormalization of `A` precisely when
> its underlying ring is seminormal.

```lean
public theorem isIso_lift_to_seminormalization_iff_isSeminormalRing
    (A B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    (huniv : UniversalHomeomorphism
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B)).op))
    (hres : Scheme.Hom.InducesResidueFieldIsomorphisms
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B)).op)) :
    IsIso ((seminormalizationAlgebraObject_isTerminal A).from
      (⟨CommAlgCat.of A B, huniv, hres⟩ : SeminormalizationAlgebraCategory A)) ↔
      IsSeminormalRing B
```

**`Algebra.isIso_toAbsoluteWeakNormalization_iff_isAbsolutelyWeaklyNormalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/RingCharacterization.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/RingCharacterization.lean#L185). The attribute's comment: “awn_characterization”.

> **Stacks 0EUR.** For an `A`-algebra `B` whose spectrum morphism to `Spec A` is a universal
> homeomorphism, the canonical map `B ⟶ Aᵃʷⁿ` is an isomorphism exactly when `B` is absolutely
> weakly normal.

```lean
theorem isIso_toAbsoluteWeakNormalization_iff_isAbsolutelyWeaklyNormalRing
    (A B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    (huniv : UniversalHomeomorphism (Spec.map (CommRingCat.ofHom (algebraMap A B)))) :
    IsIso ((absoluteWeakNormalizationCandidate_isTerminal A).from
        (⟨CommAlgCat.of A B, huniv⟩ : AbsoluteWeakNormalizationCategory A)) ↔
      IsAbsolutelyWeaklyNormalRing B
```

**`Algebra.absoluteWeakNormalizationCandidate_isTerminal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/RingUniversalProperty.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/WeakNormalization/RingUniversalProperty.lean#L246). The attribute's comment: “awn_final”.

> **Stacks 0EUR.** The absolute weak normalization of `A` is terminal among the `A`-algebras
> whose spectrum morphism to `Spec A` is a universal homeomorphism.

```lean
def absoluteWeakNormalizationCandidate_isTerminal :
    IsTerminal (absoluteWeakNormalizationCandidate A)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.seminormalization_universalHomeomorphism`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Seminormalization/Colimit.lean#L88), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/SeminormalizationAffineInitial/Basic.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SeminormalizationAffineInitial/Basic.lean#L216) (StacksFrontier): “sn_final”.
- [`AlgebraicGeometry.seminormalization_inducesResidueFieldIsomorphisms`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Seminormalization/Colimit.lean#L96), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/SeminormalizationAffineInitial/Basic.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SeminormalizationAffineInitial/Basic.lean#L218) (StacksFrontier): “sn_final”.

## Tag 0EUS, a lemma

[Tag 0EUS](https://stacks.math.columbia.edu/tag/0EUS) in the Stacks Project.

**`AlgebraicGeometry.hasInitialUniversalHomeomorphismOver`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AbsoluteWeakNormalizationInitial/Basic.lean, line 763](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AbsoluteWeakNormalizationInitial/Basic.lean#L763). The attribute's comment: “absolute_weak_normalization_initial”.

> The category of universal homeomorphisms to a scheme `X` has an initial object, the absolute
> weak normalization of `X`, which remains initial over every open subscheme.

```lean
public instance hasInitialUniversalHomeomorphismOver (X : Scheme.{u}) :
    HasLocallyInitialUniversalHomeomorphismOver X
```

**`AlgebraicGeometry.isIso_initialMap_iff_isAbsolutelyWeaklyNormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AbsoluteWeakNormalizationIsoIff/Basic.lean, line 531](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AbsoluteWeakNormalizationIsoIff/Basic.lean#L531). The attribute's comment: “absolute_weak_normalization_iso_iff”.

> **Stacks Project, Tag 0EUS.** The canonical map from the absolute weak
> normalization of `X` to a universal homeomorphism `Y ⟶ X` is an isomorphism
> if and only if `Y` is absolutely weakly normal.

```lean
public theorem isIso_initialMap_iff_isAbsolutelyWeaklyNormal
    {X Y : Scheme.{u}} [HasLocallyInitialUniversalHomeomorphismOver X]
    (f : Y ⟶ X) (hf : UniversalHomeomorphism f) :
    IsIso ((initial.to (⟨Over.mk f, hf⟩ : UniversalHomeomorphismOver X)).hom.left) ↔
      IsAbsolutelyWeaklyNormal Y
```

**`AlgebraicGeometry.isIso_initialTo_iff_isAbsolutelyWeaklyNormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/AbsoluteWeakNormalCriterion.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/AbsoluteWeakNormalCriterion.lean#L127). The attribute's comment: “absolute_weak_normalization_iso_iff”.

> **Stacks Project, Tag 0EUS.** The canonical morphism from the absolute weak normalization of
> `X` to a universal homeomorphism `Y ⟶ X` is an isomorphism if and only if `Y` is absolutely
> weakly normal.

```lean
theorem isIso_initialTo_iff_isAbsolutelyWeaklyNormal (X : Scheme.{u})
    [HasLocallyInitialUniversalHomeomorphismOver X] (Y : UniversalHomeomorphismOver X) :
    IsIso ((initial.to Y).hom.left) ↔ IsAbsolutelyWeaklyNormal Y.obj.left
```

**`AlgebraicGeometry.existsUnique_absoluteWeakNormalization_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Functorial.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Functorial.lean#L55). The attribute's comment: “absolute_weak_normalization_functorial”.

> Every morphism of schemes has a unique compatible lift to the absolute weak normalizations.

```lean
theorem existsUnique_absoluteWeakNormalization_lift {X' X : Scheme.{u}} (h : X' ⟶ X) :
    ∃! hawn : X'.absoluteWeakNormalization ⟶ X.absoluteWeakNormalization,
      hawn ≫ X.absoluteWeakNormalizationHom =
        X'.absoluteWeakNormalizationHom ≫ h
```

**`AlgebraicGeometry.existsUnique_seminormalization_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/SeminormalizationFunctorial.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/SeminormalizationFunctorial.lean#L45). The attribute's comment: “seminormalization_functorial”.

> **Stacks Project, Tag 0EUS.** A morphism of schemes has a unique compatible
> lift to their seminormalizations.

```lean
theorem existsUnique_seminormalization_lift {X' X : Scheme.{u}}
    [HasInitial (SeminormalizationCategory X')]
    [HasInitial (SeminormalizationCategory X)]
    (h : X' ⟶ X) :
    ∃! hsn : X'.seminormalization ⟶ X.seminormalization,
      hsn ≫ X.seminormalizationHom =
        X'.seminormalizationHom ≫ h
```

**`AlgebraicGeometry.hasInitial_seminormalizationCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SeminormalizationGluing/Basic.lean, line 691](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SeminormalizationGluing/Basic.lean#L691). The attribute's comment: “seminormalization_initial”.

> **Stacks Project, Tag 0EUS.** The category of universal homeomorphisms to a scheme which
> induce isomorphisms on all residue fields has an initial object, the seminormalization of that
> scheme.

```lean
noncomputable instance hasInitial_seminormalizationCategory (X : Scheme.{u}) :
    HasInitial (SeminormalizationCategory X)
```

**`AlgebraicGeometry.isIso_initialTo_iff_isSeminormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SeminormalizationGluing/Basic.lean, line 716](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SeminormalizationGluing/Basic.lean#L716). The attribute's comment: “seminormalization_iso_iff”.

> **Stacks Project, Tag 0EUS.** The canonical morphism from the seminormalization of `X` to a
> universal homeomorphism `Y ⟶ X` inducing isomorphisms on all residue fields is an isomorphism
> precisely when `Y` is seminormal.

```lean
theorem isIso_initialTo_iff_isSeminormal (X : Scheme.{u})
    (Y : SeminormalizationCategory X) :
    IsIso (initial.to Y).hom.left ↔ IsSeminormal Y.obj.left
```

## Tag 0EUT, a definition

[Tag 0EUT](https://stacks.math.columbia.edu/tag/0EUT) in the Stacks Project.

**`AlgebraicGeometry.Scheme.seminormalizationHom`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Functorial.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Functorial.lean#L85). The attribute's comment: “part (1): the seminormalization morphism of an arbitrary scheme, no hypotheses”.

> The canonical morphism from the seminormalization of `X` to `X`.

```lean
abbrev Scheme.seminormalizationHom (X : Scheme.{u}) : X.seminormalization ⟶ X
```

Declarations registered for the tag:

- [`Scheme.absoluteWeakNormalizationHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Scheme.absoluteWeakNormalizationHom#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Functorial.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Functorial.lean#L88) (StacksFrontier): “part (2): the absolute weak normalization morphism of an arbitrary scheme, no hypotheses”.

## Tag 0H3G, a lemma

[Tag 0H3G](https://stacks.math.columbia.edu/tag/0H3G) in the Stacks Project.

**`AlgebraicGeometry.isSeminormal_iff_isIso_seminormalizationHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Characterization.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Characterization.lean#L100). The attribute's comment: “conditions (1) and (2)”.

> **Stacks Project, Tag 0H3G.** A scheme is seminormal if and only if its canonical
> seminormalization morphism is an isomorphism, i.e. if and only if it equals its own
> seminormalization.

```lean
theorem isSeminormal_iff_isIso_seminormalizationHom (X : Scheme.{u}) :
    IsSeminormal X ↔ IsIso X.seminormalizationHom
```

**`AlgebraicGeometry.isSeminormal_iff_isIso_of_universalHomeomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Characterization.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Characterization.lean#L114). The attribute's comment: “conditions (1) and (3)”.

> **Stacks Project, Tag 0H3G.** A scheme is seminormal if and only if every universal
> homeomorphism to it from a reduced scheme inducing isomorphisms on all residue fields is an
> isomorphism.

```lean
theorem isSeminormal_iff_isIso_of_universalHomeomorphism (X : Scheme.{u}) :
    IsSeminormal X ↔
      ∀ (Y : Scheme.{u}) (π : Y ⟶ X), UniversalHomeomorphism π →
        (∀ y : Y, IsIso (π.residueFieldMap y)) → IsReduced Y → IsIso π
```

## Tag 0H3H, a lemma

[Tag 0H3H](https://stacks.math.columbia.edu/tag/0H3H) in the Stacks Project.

**`AlgebraicGeometry.isAbsolutelyWeaklyNormal_iff_isIso_absoluteWeakNormalizationHom'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Characterization.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Characterization.lean#L154). The attribute's comment: “conditions (1) and (2)”.

> **Stacks Project, Tag 0H3H.** A scheme is absolutely weakly normal if and only if its
> canonical absolute weak normalization morphism is an isomorphism, i.e. if and only if it equals
> its own absolute weak normalization.

```lean
theorem isAbsolutelyWeaklyNormal_iff_isIso_absoluteWeakNormalizationHom' (X : Scheme.{u}) :
    IsAbsolutelyWeaklyNormal X ↔ IsIso X.absoluteWeakNormalizationHom
```

**`AlgebraicGeometry.isAbsolutelyWeaklyNormal_iff_isIso_of_universalHomeomorphism'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Characterization.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Characterization.lean#L187). The attribute's comment: “conditions (1) and (3)”.

> **Stacks Project, Tag 0H3H.** A scheme is absolutely weakly normal if and only if every
> universal homeomorphism to it from a reduced scheme is an isomorphism.

```lean
theorem isAbsolutelyWeaklyNormal_iff_isIso_of_universalHomeomorphism' (X : Scheme.{u}) :
    IsAbsolutelyWeaklyNormal X ↔
      ∀ (Y : Scheme.{u}) (π : Y ⟶ X), UniversalHomeomorphism π → IsReduced Y → IsIso π
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.48, Tag 0EUK](https://stacks.math.columbia.edu/tag/0EUK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
