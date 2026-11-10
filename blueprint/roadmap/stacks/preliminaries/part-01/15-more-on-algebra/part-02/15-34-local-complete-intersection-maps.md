---
declaration: section
origin: cited
lean: RingHom.isKoszulRegularIdeal_ker_of_surjective_mvPolynomial, RingHom.IsLocalCompleteIntersection, RingHom.isLocalCompleteIntersection_of_localization_away, RingHom.isKoszulRegular_relation_of_isRelativeGlobalCompleteIntersection, RingHom.syntomic_iff_flat_and_isLocalCompleteIntersection, RingHom.cotangentMap_toComp_injective_of_isLocalCompleteIntersection, RingHom.cotangentMap_toComp_injective_of_isFilteredColimit_isLocalCompleteIntersection, Algebra.naiveCotangentComplex_quasiIso_henselization_and_strictHenselization
statement: formalized
proof: formalized
---

# 15.34 Local complete intersection maps

Section 15.34 of the Stacks Project, [Tag 07CY](https://stacks.math.columbia.edu/tag/07CY). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07CZ, a lemma

[Tag 07CZ](https://stacks.math.columbia.edu/tag/07CZ) in the Stacks Project.

**`RingHom.isKoszulRegularIdeal_ker_of_surjective_mvPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/RingMap/Defs.lean, line 688](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/RingMap/Defs.lean#L688).

> The kernel of every finite polynomial presentation is a Koszul-regular ideal if the kernel
> of one such presentation is Koszul-regular.

```lean
public theorem isKoszulRegularIdeal_ker_of_surjective_mvPolynomial
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    {ι : Type w} [_root_.Finite ι] {κ : Type x} [_root_.Finite κ]
    (α : MvPolynomial ι A →ₐ[A] B) (hα : Function.Surjective α)
    (hI : Ideal.IsKoszulRegular (RingHom.ker α.toRingHom))
    (β : MvPolynomial κ A →ₐ[A] B) (hβ : Function.Surjective β) :
    Ideal.IsKoszulRegular (RingHom.ker β.toRingHom)
```

## Tag 07D0, a definition

[Tag 07D0](https://stacks.math.columbia.edu/tag/07D0) in the Stacks Project.

**`RingHom.IsLocalCompleteIntersection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/RingMap/Defs.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/RingMap/Defs.lean#L94).

> A ring homomorphism is a local complete intersection if it is of finite type and some finite
> polynomial presentation has Koszul-regular kernel.

```lean
public def IsLocalCompleteIntersection {A : Type u} {B : Type v}
    [CommRing A] [CommRing B] (f : A →+* B) : Prop
```

## Tag 07D1, a lemma

[Tag 07D1](https://stacks.math.columbia.edu/tag/07D1) in the Stacks Project.

**`RingHom.isLocalCompleteIntersection_of_localization_away`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/RingMap/Criteria.lean, line 692](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/RingMap/Criteria.lean#L692).

> **Stacks 07D1.** If finitely many elements `g j` generate the unit ideal of `S` and every
> composite from `R` to the localization `S_{g j}` is a local complete intersection, then the
> original ring homomorphism `R → S` is a local complete intersection.

```lean
public theorem isLocalCompleteIntersection_of_localization_away
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] (f : R →+* S)
    {m : ℕ} (g : Fin m → S) (hspan : Ideal.span (Set.range g) = ⊤)
    (hlocal : ∀ j, RingHom.IsLocalCompleteIntersection
      ((algebraMap S (Localization.Away (g j))).comp f)) :
    RingHom.IsLocalCompleteIntersection f
```

## Tag 07D2, a lemma

[Tag 07D2](https://stacks.math.columbia.edu/tag/07D2) in the Stacks Project.

**`RingHom.isKoszulRegular_relation_of_isRelativeGlobalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/RingMap/Criteria.lean, line 1298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/RingMap/Criteria.lean#L1298).

> The relations in a polynomial presentation of a relative global complete intersection form a
> Koszul-regular sequence in the polynomial ring.

```lean
public theorem isKoszulRegular_relation_of_isRelativeGlobalCompleteIntersection
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S]
    {ι : Type w} [_root_.Finite ι] {c : ℕ} (P : Algebra.Presentation R S ι (Fin c))
    (hP : P.IsRelativeGlobalCompleteIntersection) :
    Koszul.IsKoszulRegular P.relation
```

## Tag 07D3, a lemma

[Tag 07D3](https://stacks.math.columbia.edu/tag/07D3) in the Stacks Project.

**`RingHom.syntomic_iff_flat_and_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/RingMap/Criteria.lean, line 1693](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/RingMap/Criteria.lean#L1693).

> **Stacks 07D3.** A ring homomorphism is syntomic if and only if it is flat and a local
> complete intersection.

```lean
public theorem syntomic_iff_flat_and_isLocalCompleteIntersection
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] (f : R →+* S) :
    letI := f.toAlgebra
    Algebra.Syntomic R S ↔ f.Flat ∧ RingHom.IsLocalCompleteIntersection f
```

## Tag 07D4, a lemma

[Tag 07D4](https://stacks.math.columbia.edu/tag/07D4) in the Stacks Project.

**`RingHom.cotangentMap_toComp_injective_of_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/RingMap/JacobiZariski.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/RingMap/JacobiZariski.lean#L249).

> Let `A → B → C` be ring maps, let `α : A[x_s] → B` and
> `β : B[y₁, ..., yₘ] → C` be presentations, and write `K` for the kernel of the induced
> presentation `β.comp α : A[x_s, y_t] → C`. If `B → C` is a local complete intersection, then
> the canonical map `C ⊗_B (I / I²) → K / K²` is injective. Together with the canonical exact
> conormal/differential diagram and the Jacobi--Zariski exactness lemmas, this gives the exact
> sequence
> `0 → H₁(NL\_\{B/A} ⊗\_B C) → H₁(L\_\{C/A}) → H₁(L\_\{C/B}) →
> C ⊗\_B Ω[B⁄A] → Ω[C⁄A] → Ω[C⁄B] → 0`.

```lean
public theorem cotangentMap_toComp_injective_of_isLocalCompleteIntersection
    {A : Type u₁} {B : Type u₂} [CommRing A] [CommRing B] [Algebra A B]
    {C : Type u₃} [CommRing C] [Algebra A C] [Algebra B C] [IsScalarTower A B C]
    {S : Type w} {m : ℕ} (α : Generators A B S) (β : Generators B C (Fin m))
    (h : RingHom.IsLocalCompleteIntersection (algebraMap B C)) :
    Function.Injective
      ((Extension.Cotangent.map (β.toComp α).toExtensionHom).liftBaseChange C)
```

## Tag 07D5, a lemma

[Tag 07D5](https://stacks.math.columbia.edu/tag/07D5) in the Stacks Project.

**`RingHom.cotangentMap_toComp_injective_of_isFilteredColimit_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/RingMap/JacobiZariski.lean, line 792](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/RingMap/JacobiZariski.lean#L792).

> Let `A → B → C` be ring maps and suppose that `B → C` is exhibited as a filtered
> colimit of local complete intersection homomorphisms, with `eB`, `eC`, and `hcomm` identifying
> the directed system's colimit map with `B → C`. For presentations `α : A[x_s] → B`
> and `β : B[y_t] → C`, the canonical map
> `C ⊗_B (I / I²) → K / K²` from the conormal module of `α` to that of the induced
> presentation `β.comp α` is injective.

```lean
public theorem cotangentMap_toComp_injective_of_isFilteredColimit_isLocalCompleteIntersection
    {A : Type u₁} {B : Type u₂} [CommRing A] [CommRing B] [Algebra A B]
    {C : Type u₃} [CommRing C] [Algebra A C] [Algebra B C] [IsScalarTower A B C]
    {S : Type w} {T : Type w'} (α : Generators A B S) (β : Generators B C T)
    {J : Type u₄} [Preorder J] [IsDirectedOrder J] [Nonempty J]
    (sys : RingMapSystemUnbundled.{u₅} J)
    (eB : sys.Rinf ≃+* B) (eC : sys.Sinf ≃+* C)
    (hcomm : eC.toRingHom.comp sys.gInf = (algebraMap B C).comp eB.toRingHom)
    (h : ∀ i : J, RingHom.IsLocalCompleteIntersection (sys.g i)) :
    Function.Injective
      ((Extension.Cotangent.map (β.toComp α).toExtensionHom).liftBaseChange C)
```

## Tag 0D08, a lemma

[Tag 0D08](https://stacks.math.columbia.edu/tag/0D08) in the Stacks Project.

**`Algebra.naiveCotangentComplex_quasiIso_henselization_and_strictHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Henselization.lean, line 602](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/NaiveCotangent/Henselization.lean#L602).

> Let `A → B` be a local homomorphism of local rings. For the induced local map between
> henselizations and the induced local map between strict henselizations associated to a compatible
> map of residue fields, the canonical maps
> `NL_{B/A} ⊗_B Bʰ ⟶ NL_{Bʰ/Aʰ}` and `NL_{B/A} ⊗_B Bˢʰ ⟶ NL_{Bˢʰ/Aˢʰ}` induce
> isomorphisms on all homology groups.

```lean
public theorem
    naiveCotangentComplex_quasiIso_henselization_and_strictHenselization
    (A Ah Ash : Type u) (B Bh Bsh : Type v) (kAsep : Type u) (kBsep : Type v)
    [CommRing A] [IsLocalRing A] [CommRing B] [IsLocalRing B]
    [Algebra A B] [IsLocalHom (algebraMap A B)]
    [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah]
    [IsLocalRing.IsHenselization A (IsLocalRing.ResidueField A) Ah]
    [CommRing Bh] [IsLocalRing Bh] [Algebra B Bh]
    [IsLocalRing.IsHenselization B (IsLocalRing.ResidueField B) Bh]
    [Algebra A Bh] [IsScalarTower A B Bh] [Algebra Ah Bh] [IsScalarTower A Ah Bh]
    [IsLocalHom (algebraMap Ah Bh)]
    [Field kAsep] [Algebra (IsLocalRing.ResidueField A) kAsep]
    [IsSepClosure (IsLocalRing.ResidueField A) kAsep]
    [CommRing Ash] [IsLocalRing Ash] [Algebra A Ash]
    [IsLocalRing.IsHenselization A kAsep Ash]
    [Field kBsep] [Algebra (IsLocalRing.ResidueField B) kBsep]
    [IsSepClosure (IsLocalRing.ResidueField B) kBsep]
    [CommRing Bsh] [IsLocalRing Bsh] [Algebra B Bsh]
    [IsLocalRing.IsHenselization B kBsep Bsh]
    [Algebra A Bsh] [IsScalarTower A B Bsh] [Algebra Ash Bsh] [IsScalarTower A Ash Bsh]
    [IsLocalHom (algebraMap Ash Bsh)]
    (phi : IsLocalRing.ResidueField Ash →+* IsLocalRing.ResidueField Bsh)
    (_hphi : phi.comp ((IsLocalRing.residue Ash).comp (algebraMap A Ash)) =
      (IsLocalRing.residue Bsh).comp (algebraMap A Bsh))
    (_hinduced : (IsLocalRing.residue Bsh).comp (algebraMap Ash Bsh) =
      phi.comp (IsLocalRing.residue Ash)) :
    QuasiIso (Algebra.naiveCotangentComplexBaseChangeComparison A Ah B Bh) ∧
      QuasiIso (Algebra.naiveCotangentComplexBaseChangeComparison A Ash B Bsh)
```

**`Algebra.naiveCotangentComplex_quasiIso_henselizationPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Henselization.lean, line 672](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/NaiveCotangent/Henselization.lean#L672). The attribute's comment: “the henselization-of-pairs case, which Stacks 0DZC's proof cites 0D08 for although 0D08's own statement is about the local and strict henselizations of a local ring: the input to the source's proof is that both vertical maps are filtered colimits of étale maps, which `ind_henselization` supplies for the henselization of a pair”.

> **Stacks 0D08 for the henselization of a pair.** Let `P` be an algebra over a commutative
> ring `k`, let `J ⊆ P` be an ideal and let `(Pʰ, Jʰ)` be the henselization of the pair `(P, J)`,
> described by the henselian-pair condition on `Pʰ` together with its universal property. Then the
> canonical comparison map
>
> `NL_{P/k} ⊗_P Pʰ ⟶ NL_{Pʰ/k}`
>
> induces isomorphisms on all homology groups.
>
> The source states Stacks 0D08 for the henselization and the strict henselization of a local
> ring, which is
> `naiveCotangentComplex_quasiIso_henselization_and_strictHenselization`. Its proof uses of those
> two only that they are filtered colimits of étale algebras over their bases, and the
> henselization of a pair is such a colimit by `ind_henselization`; this is the instance Stacks
> 0DZC's proof appeals to 0D08 for.

```lean
public theorem naiveCotangentComplex_quasiIso_henselizationPair
    (k : Type u) [CommRing k] (P : Type v) [CommRing P] [Algebra k P] (J : Ideal P)
    (Ph : Type v) [CommRing Ph] [Algebra P Ph] [Algebra k Ph] [IsScalarTower k P Ph]
    (hhens : HenselianPair Ph (J.map (algebraMap P Ph)))
    (huniv : ∀ (C : Type v) (_ : CommRing C) (JC : Ideal C), HenselianPair C JC →
      ∀ f : P →+* C, J ≤ JC.comap f →
        ∃! g : Ph →+* C, g.comp (algebraMap P Ph) = f ∧
          J.map (algebraMap P Ph) ≤ JC.comap g) :
    QuasiIso (naiveCotangentComplexBaseChangeComparison k k P Ph)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.34, Tag 07CY](https://stacks.math.columbia.edu/tag/07CY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
