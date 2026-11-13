---
declaration: section
origin: cited
lean: RingHom.isKoszulRegularIdeal_ker_of_surjective_mvPolynomial, RingHom.IsLocalCompleteIntersection, RingHom.isLocalCompleteIntersection_of_localization_away, RingHom.isKoszulRegular_relation_of_isRelativeGlobalCompleteIntersection, RingHom.syntomic_iff_flat_and_isLocalCompleteIntersection, RingHom.cotangentMap_toComp_injective_of_isLocalCompleteIntersection, NaiveCotangent.jacobiZariski_exact_of_isLocalCompleteIntersection, NaiveCotangent.injective_onH₁_nlExtensionBaseChangeMap_of_isLocalCompleteIntersection
statement: formalized
proof: formalized
---

# 15.34 Local complete intersection maps

Section 15.34 of the Stacks Project, [Tag 07CY](https://stacks.math.columbia.edu/tag/07CY). 8 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07CZ, a lemma

[Tag 07CZ](https://stacks.math.columbia.edu/tag/07CZ) in the Stacks Project.

**`RingHom.isKoszulRegularIdeal_ker_of_surjective_mvPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/RingMap/Defs.lean, line 687](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteIntersection/RingMap/Defs.lean#L687).

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

**`RingHom.IsLocalCompleteIntersection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/RingMap/Defs.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteIntersection/RingMap/Defs.lean#L94).

> A ring homomorphism is a local complete intersection if it is of finite type and some finite
> polynomial presentation has Koszul-regular kernel.

```lean
public def IsLocalCompleteIntersection {A : Type u} {B : Type v}
    [CommRing A] [CommRing B] (f : A →+* B) : Prop
```

## Tag 07D1, a lemma

[Tag 07D1](https://stacks.math.columbia.edu/tag/07D1) in the Stacks Project.

**`RingHom.isLocalCompleteIntersection_of_localization_away`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/RingMap/Criteria.lean, line 692](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteIntersection/RingMap/Criteria.lean#L692).

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

**`RingHom.isKoszulRegular_relation_of_isRelativeGlobalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/RingMap/Criteria.lean, line 1298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteIntersection/RingMap/Criteria.lean#L1298).

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

**`RingHom.syntomic_iff_flat_and_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/RingMap/Criteria.lean, line 1692](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteIntersection/RingMap/Criteria.lean#L1692).

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

**`RingHom.cotangentMap_toComp_injective_of_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/RingMap/JacobiZariski.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteIntersection/RingMap/JacobiZariski.lean#L248). The attribute's comment: “the injectivity of C ⊗\_B I/I² → K/K²”.

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

**`NaiveCotangent.jacobiZariski_exact_of_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/RingMap/JacobiZariskiExact.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteIntersection/RingMap/JacobiZariskiExact.lean#L77).

> **Stacks 07D4.** Let `A → B → C` be ring maps with `B → C` a local complete intersection,
> let `α : A[x_s] → B` be a presentation with kernel `I`, let `β : B[y₁, …, yₘ] → C` be a
> presentation with kernel `J`, and let `γ = β.comp α : A[x_s, y_t] → C` be the induced
> presentation, with kernel `K`. Then the canonical diagram, whose vertical maps are the
> differentials of `NL(α) ⊗_B C`, `NL(γ)` and `NL(β)`, commutes, and both of its rows
> ```
> 0 ⟶ C ⊗_B Ω_{A[x]/A} ⟶ Ω_{A[x,y]/A} ⊗ C ⟶ Ω_{B[y]/B} ⊗ C ⟶ 0
> 0 ⟶   C ⊗_B I/I²     ⟶       K/K²        ⟶      J/J²      ⟶ 0
> ```
> are exact. In particular the six-term sequence of Stacks 00S2 can be completed with a zero on
> the left: the sequence
> ```
> 0 → H₁(NL(α) ⊗_B C) → H₁(NL(γ)) → H₁(NL(β)) --δ--> H₀(NL(α) ⊗_B C) → H₀(NL(γ)) → H₀(NL(β)) → 0
> ```
> is exact, that is
> `0 → H₁(NL_{B/A} ⊗_B C) → H₁(L_{C/A}) → H₁(L_{C/B}) → Ω_{B/A} ⊗_B C → Ω_{C/A} → Ω_{C/B} → 0`,
> with `δ` the connecting map `NaiveCotangent.jacobiZariskiConnecting`.

```lean
theorem jacobiZariski_exact_of_isLocalCompleteIntersection {S : Type w} {m : ℕ}
    (α : Generators A B S) (β : Generators B C (Fin m))
    (h : RingHom.IsLocalCompleteIntersection (algebraMap B C)) :
    -- the two squares of the canonical diagram commute
    ((NL (β.comp α)).d ∘ₗ (nlToComp β α).f₁ = (nlToComp β α).f₀ ∘ₗ (nlBaseChange C α).d ∧
      (NL β).d ∘ₗ (nlOfComp β α).f₁ = (nlOfComp β α).f₀ ∘ₗ (NL (β.comp α)).d) ∧
    -- the row of Kähler differentials is exact
    (Injective (nlToComp β α).f₀ ∧ Exact (nlToComp β α).f₀ (nlOfComp β α).f₀ ∧
      Surjective (nlOfComp β α).f₀) ∧
    -- the row of conormal modules is exact
    (Injective (nlToComp β α).f₁ ∧ Exact (nlToComp β α).f₁ (nlOfComp β α).f₁ ∧
      Surjective (nlOfComp β α).f₁) ∧
    -- the six-term sequence of Stacks 00S2, completed with a zero on the left, is exact
    (Injective (nlToComp β α).onH₁ ∧
      Exact (nlToComp β α).onH₁ (nlOfComp β α).onH₁ ∧
      Exact (nlOfComp β α).onH₁ (jacobiZariskiConnecting β α) ∧
      Exact (jacobiZariskiConnecting β α) (nlToComp β α).onH₀ ∧
      Exact (nlToComp β α).onH₀ (nlOfComp β α).onH₀ ∧
      Surjective (nlOfComp β α).onH₀)
```

**`NaiveCotangent.injective_onH₁_nlExtensionBaseChangeMap_of_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/LciLocalizedInjective.lean, line 326](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/LciLocalizedInjective.lean#L326). The attribute's comment: “the zero on the left of the 00S2 sequence, over the canonical presentations”.

> **Stacks 07D4, read on `H₁` over the canonical presentations.**  For ring maps `A → B → C`
> with `B → C` a local complete intersection homomorphism, the canonical map
>
> `NL_{B/A} ⊗_B C ⟶ NL_{C/A}`
>
> of two-term complexes of `C`-modules is injective on `H₁`.  Together with the six-term exact
> sequence of Stacks 00S2 this puts a zero at the left of that sequence.
>
> The statement holds for every morphism of extensions inducing the comparison, any two being
> homotopic.  Stacks 07D4 gives injectivity of the whole degree-`1` component for the presentation
> `β.comp α` induced by the canonical presentation `α` of `B` over `A` and a finite presentation
> `β` of `C` over `B`; the comparison of that presentation with the canonical presentation of `C`
> over `A` is a quasi-isomorphism by Stacks 00S1 (4), and injectivity on `H₁` is inherited.

```lean
theorem injective_onH₁_nlExtensionBaseChangeMap_of_isLocalCompleteIntersection
    (h : RingHom.IsLocalCompleteIntersection (algebraMap B C))
    (hom : (Generators.self A B).toExtension.Hom (Generators.self A C).toExtension) :
    Function.Injective (nlExtensionBaseChangeMap (T := C) hom).onH₁
```

## Tag 07D5, a lemma

[Tag 07D5](https://stacks.math.columbia.edu/tag/07D5) in the Stacks Project.

**`RingHom.cotangentMap_toComp_injective_of_isFilteredColimit_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/RingMap/JacobiZariski.lean, line 793](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteIntersection/RingMap/JacobiZariski.lean#L793). The attribute's comment: “The conormal form: injectivity of `C ⊗_B I/I² → K/K²`, the one assertion of the source beyond Stacks 00S2. The complete statement, both exact rows and the seven-term sequence, is `RingHom.jacobiZariski_exact_of_isFilteredColimit_isLocalCompleteIntersection`.”.

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

**`RingHom.jacobiZariski_exact_of_isFilteredColimit_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/RingMap/JacobiZariskiColimit.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteIntersection/RingMap/JacobiZariskiColimit.lean#L74). The attribute's comment: “The complete conclusion of 07D4 for a filtered colimit of lci maps: both exact rows of the conormal/differential diagram and the seven-term Jacobi-Zariski sequence with a zero on the left, for the naive cotangent complexes of the three presentations.”.

> **Stacks 07D5.** Let `A → B → C` be ring maps and suppose that `B → C` is a filtered
> colimit of local complete intersection homomorphisms, exhibited by a directed system `sys` of
> ring maps each of which is a local complete intersection, together with `eB`, `eC` and `hcomm`
> identifying the system's colimit map with `B → C`. Let `α : A[x_s] → B` and `β : B[y_t] → C` be
> presentations and `γ = β.comp α` the induced presentation of `C` over `A`. Then the conclusion
> of Stacks 07D4 holds:
>
> * the degree-`0` row `0 → C ⊗_B Ω_{A[x]/A} → Ω_{A[x,y]/A} ⊗ C → Ω_{B[y]/B} ⊗ C → 0` and the
>   degree-`1` row `0 → C ⊗_B I/I² → K/K² → J/J² → 0` of the canonical diagram are exact;
> * the sequence
>   `0 → H₁(NL(α) ⊗_B C) → H₁(NL(γ)) → H₁(NL(β)) → H₀(NL(α) ⊗_B C) → H₀(NL(γ)) → H₀(NL(β)) → 0`
>   is exact, its connecting map being `NaiveCotangent.jacobiZariskiConnecting β α`.

```lean
public theorem jacobiZariski_exact_of_isFilteredColimit_isLocalCompleteIntersection
    {A : Type u₁} {B : Type u₂} [CommRing A] [CommRing B] [Algebra A B]
    {C : Type u₃} [CommRing C] [Algebra A C] [Algebra B C] [IsScalarTower A B C]
    {S : Type w} {T : Type w'} (α : Generators A B S) (β : Generators B C T)
    {J : Type u₄} [Preorder J] [IsDirectedOrder J] [Nonempty J]
    (sys : RingMapSystemUnbundled.{u₅} J)
    (eB : sys.Rinf ≃+* B) (eC : sys.Sinf ≃+* C)
    (hcomm : eC.toRingHom.comp sys.gInf = (algebraMap B C).comp eB.toRingHom)
    (h : ∀ i : J, RingHom.IsLocalCompleteIntersection (sys.g i)) :
    (Injective (nlToComp β α).f₀ ∧ Exact (nlToComp β α).f₀ (nlOfComp β α).f₀ ∧
        Surjective (nlOfComp β α).f₀) ∧
      (Injective (nlToComp β α).f₁ ∧ Exact (nlToComp β α).f₁ (nlOfComp β α).f₁ ∧
        Surjective (nlOfComp β α).f₁) ∧
      Injective (nlToComp β α).onH₁ ∧
      Exact (nlToComp β α).onH₁ (nlOfComp β α).onH₁ ∧
      Exact (nlOfComp β α).onH₁ (jacobiZariskiConnecting β α) ∧
      Exact (jacobiZariskiConnecting β α) (nlToComp β α).onH₀ ∧
      Exact (nlToComp β α).onH₀ (nlOfComp β α).onH₀ ∧
      Surjective (nlOfComp β α).onH₀
```

## Tag 0D08, a lemma

[Tag 0D08](https://stacks.math.columbia.edu/tag/0D08) in the Stacks Project.

**`Algebra.naiveCotangentComplex_quasiIso_henselization_and_strictHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Henselization.lean, line 602](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Henselization.lean#L602).

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

**`Algebra.naiveCotangentComplex_quasiIso_henselizationPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Henselization.lean, line 672](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Henselization.lean#L672). The attribute's comment: “the henselization-of-pairs case, which Stacks 0DZC's proof cites 0D08 for although 0D08's own statement is about the local and strict henselizations of a local ring: the input to the source's proof is that both vertical maps are filtered colimits of étale maps, which `ind_henselization` supplies for the henselization of a pair”.

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
