---
declaration: section
origin: cited
lean: ProetaleWContractible.IsWContractible, AlgebraicGeometry.ProEtale.nonempty_algHom_of_ind_etale_of_isWContractible, AlgebraicGeometry.ProEtale.strictlyHenselian_atPrime_of_ind_etale_retraction, AlgebraicGeometry.ProEtale.localizationAtPrime_strictlyHenselian_of_isWContractible, AlgebraicGeometry.ProEtale.wContractible_tfae, AlgebraicGeometry.ProEtale.exists_faithfullyFlat_ind_etale_wContractible, AlgebraicGeometry.ProEtale.exists_small_faithfullyFlat_ind_etale_wContractible, AlgebraicGeometry.ProEtale.extremallyDisconnected_primeSpectrum_of_quasiFinite
statement: formalized
proof: formalized
---

# 61.11 Constructing w-contractible covers

Section 61.11 of the Stacks Project, [Tag 0980](https://stacks.math.columbia.edu/tag/0980). 7 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0981, a definition

[Tag 0981](https://stacks.math.columbia.edu/tag/0981) in the Stacks Project.

**`ProetaleWContractible.IsWContractible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/WeaklyContractible/WContractibleRings.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/WeaklyContractible/WContractibleRings.lean#L70).

> **Definition 4 (w-contractible ring; Stacks Tag `0981`).**
> A ring `A` is *w-contractible* if every faithfully flat weakly etale ring map `A → B` has a
> retraction.  We quantify over all `A`-algebra structures on all rings `B`; the universe of
> `B` is the implicit universe parameter `w` of this definition, so the condition is not
> restricted to a fixed universe.

```lean
def IsWContractible.{w} (A : Type u) [CommRing A] : Prop
```

## Tag 0982, a lemma

[Tag 0982](https://stacks.math.columbia.edu/tag/0982) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.nonempty_algHom_of_ind_etale_of_isWContractible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WContractibleCharacterization.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WContractibleCharacterization.lean#L57). The attribute's comment: “(1) ⇒ (2)”.

> **Lemma 0982, (1) ⇒ (2).** A w-contractible ring retracts every faithfully flat ind-étale
> algebra over it, ind-étaleness being taken in the categorical form
> `(CommAlgCat.etale A).ind (CommAlgCat.of A B)`.

```lean
theorem nonempty_algHom_of_ind_etale_of_isWContractible (A : Type u) [CommRing A]
    (h : ProetaleWContractible.IsWContractible.{u, u} A) (B : Type u) [CommRing B]
    [Algebra A B] (hff : Module.FaithfullyFlat A B)
    (hind : ObjectProperty.ind.{u} (fun C : CommAlgCat A ↦ Algebra.Etale A C)
      (CommAlgCat.of A B)) :
    Nonempty (B →ₐ[A] A)
```

**`AlgebraicGeometry.ProEtale.strictlyHenselian_atPrime_of_ind_etale_retraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WContractibleCharacterization.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WContractibleCharacterization.lean#L69). The attribute's comment: “(2) ⇒ (3)(c)”.

> **Lemma 0982, the (3)(c) component of (2) ⇒ (3).** If every faithfully flat ind-étale
> algebra over `A` has a retraction, then `A` localized at any maximal ideal is strictly
> henselian. An étale algebra is ind-étale, so this is Lemma 097V.

```lean
theorem strictlyHenselian_atPrime_of_ind_etale_retraction (A : Type u) [CommRing A]
    (h : ∀ (B : Type u) [CommRing B] [Algebra A B], Module.FaithfullyFlat A B →
      ObjectProperty.ind.{u} (fun C : CommAlgCat A ↦ Algebra.Etale A C) (CommAlgCat.of A B) →
      Nonempty (B →ₐ[A] A))
    (m : Ideal A) [m.IsMaximal] :
    StrictlyHenselianLocalRing (Localization.AtPrime m)
```

**`AlgebraicGeometry.ProEtale.localizationAtPrime_strictlyHenselian_of_isWContractible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/WContractibleCharacterization.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/WContractibleCharacterization.lean#L116). The attribute's comment: “(1) ⇒ (3)(c)”.

> The localization of a w-contractible ring at a maximal ideal is strictly henselian.

```lean
theorem localizationAtPrime_strictlyHenselian_of_isWContractible (A : Type u) [CommRing A]
    (h : ProetaleWContractible.IsWContractible.{u, u} A) (m : Ideal A) [m.IsMaximal] :
    StrictlyHenselianLocalRing (Localization.AtPrime m)
```

**`AlgebraicGeometry.ProEtale.wContractible_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/WContractibleTFAE.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/WContractibleTFAE.lean#L233).

> **Stacks 0982.** For a commutative ring `A` the following are equivalent: `A` is
> w-contractible; every faithfully flat ind-étale `A`-algebra admits a retraction; `Spec A` is
> w-local, `π₀(Spec A)` is extremally disconnected and the localization of `A` at every maximal
> ideal is strictly henselian.

```lean
theorem wContractible_tfae (A : Type u) [CommRing A] :
    List.TFAE
      [ProetaleWContractible.IsWContractible.{u, u} A,
        ∀ (B : Type u) [CommRing B] [Algebra A B], Module.FaithfullyFlat A B →
          StacksDraft.IndEtale A B → Nonempty (B →ₐ[A] A),
        WLocalSpace (PrimeSpectrum A) ∧
          ExtremallyDisconnected (ConnectedComponents (PrimeSpectrum A)) ∧
            ∀ (m : Ideal A) [m.IsMaximal],
              StrictlyHenselianLocalRing (Localization.AtPrime m)]
```

## Tag 0983, a proposition

[Tag 0983](https://stacks.math.columbia.edu/tag/0983) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exists_faithfullyFlat_ind_etale_wContractible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/WContractibleCover.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/WContractibleCover.lean#L201).

> **Stacks 0983.** Every commutative ring has a faithfully flat ind-étale map to a
> w-contractible ring.

```lean
theorem exists_faithfullyFlat_ind_etale_wContractible (A : Type u) [CommRing A] :
    ∃ (D : Type u) (_ : CommRing D) (f : A →+* D),
      f.FaithfullyFlat ∧
        (ObjectProperty.ind.{u}
          (fun C : Under (CommRingCat.of A) ↦ C.hom.hom.Etale)
          (Under.mk (CommRingCat.ofHom f)) ∧
        ProetaleWContractible.IsWContractible.{u, u} D)
```

## Tag 0984, a remark

[Tag 0984](https://stacks.math.columbia.edu/tag/0984) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exists_small_faithfullyFlat_ind_etale_wContractible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/WContractibleCoverCardinality.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/WContractibleCoverCardinality.lean#L278).

> **Stacks 0984.** A ring of cardinality at most an infinite cardinal `κ` has a faithfully flat
> ind-étale w-contractible extension of cardinality at most `κ ^ (2 ^ (2 ^ (2 ^ κ)))`.

```lean
theorem exists_small_faithfullyFlat_ind_etale_wContractible (A : Type u) [CommRing A]
    (κ : Cardinal.{u}) (hκ : ℵ₀ ≤ κ) (hA : Cardinal.mk A ≤ κ) :
    ∃ (D : Type u) (_ : CommRing D) (f : A →+* D),
      f.FaithfullyFlat ∧
        ObjectProperty.ind.{u}
          (fun C : Under (CommRingCat.of A) ↦ C.hom.hom.Etale)
          (Under.mk (CommRingCat.ofHom f)) ∧
        ProetaleWContractible.IsWContractible.{u, u} D ∧
        Cardinal.mk D ≤
          κ ^ ((2 : Cardinal.{u}) ^ ((2 : Cardinal.{u}) ^ ((2 : Cardinal.{u}) ^ κ)))
```

## Tag 0985, a lemma

[Tag 0985](https://stacks.math.columbia.edu/tag/0985) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.extremallyDisconnected_primeSpectrum_of_quasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ExtremallyDisconnectedSpectrum.lean, line 532](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ExtremallyDisconnectedSpectrum.lean#L532).

> The spectrum of a quasi-finite, finitely presented algebra over a ring with separably closed
> residue fields and Hausdorff extremally disconnected spectrum is extremally disconnected.

```lean
theorem extremallyDisconnected_primeSpectrum_of_quasiFinite
    (A : Type u) (B : Type v) [CommRing A] [CommRing B] [Algebra A B]
    [Algebra.QuasiFinite A B] [Algebra.FinitePresentation A B]
    (hres : ∀ p : PrimeSpectrum A, IsSepClosed p.asIdeal.ResidueField)
    (hT2 : T2Space (PrimeSpectrum A))
    (hA : ExtremallyDisconnected (PrimeSpectrum A)) :
    ExtremallyDisconnected (PrimeSpectrum B)
```

## Tag 0986, a lemma

[Tag 0986](https://stacks.math.columbia.edu/tag/0986) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.isWContractible_of_finite_of_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/WContractibleFinite.lean, line 431](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/WContractibleFinite.lean#L431).

> A finite, finitely presented algebra over a w-contractible ring is w-contractible.

```lean
public theorem isWContractible_of_finite_of_finitePresentation
    (A : Type u) (B : Type v) [CommRing A] [CommRing B] [Algebra A B]
    [Module.Finite A B] [Algebra.FinitePresentation A B]
    (hA : ProetaleWContractible.IsWContractible.{u, max u v} A) :
    ProetaleWContractible.IsWContractible.{v, max u v} B
```

## Tag 0987, a lemma

[Tag 0987](https://stacks.math.columbia.edu/tag/0987) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.isWContractible_localizationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/WContractibleLocalization.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/WContractibleLocalization.lean#L61).

> The canonical localization along a finitely generated closed subset of the spectrum of
> a w-contractible ring is w-contractible.

```lean
theorem isWContractible_localizationRing
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
    (hA : ProetaleWContractible.IsWContractible.{u, max u v} A) :
    ProetaleWContractible.IsWContractible.{u, max u v}
      (localizationRing I (1 : A))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.11, Tag 0980](https://stacks.math.columbia.edu/tag/0980)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
