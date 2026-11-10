---
declaration: section
origin: cited
lean: Stacks.DeRhamChern.existsUnique_deRhamTotalChernClass, Stacks.DeRhamChern.exists_injective_pull_hasInvertibleFiltration, Stacks.DeRhamChern.IsDeRhamTotalChernClass.apply_classOf_tensorObj_invertible, Stacks.DeRhamChern.existsUnique_deRhamChernCharacter
statement: formalized
proof: formalized
---

# 50.21 Chern classes

Section 50.21 of the Stacks Project, [Tag 0FW8](https://stacks.math.columbia.edu/tag/0FW8). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FW9, a lemma

[Tag 0FW9](https://stacks.math.columbia.edu/tag/0FW9) in the Stacks Project.

**`Stacks.DeRhamChern.existsUnique_deRhamTotalChernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/WeilCohomology/DeRhamTotalChernClass.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/WeilCohomology/DeRhamTotalChernClass.lean#L110). The attribute's comment: “there is a unique rule assigning to every quasi-compact and quasi-separated scheme X a total Chern class c^dR : K\_0(Vect(X)) -> prod\_\{i >= 0} H^\{2i}\_dR(X/Z) with (1) c^dR(alpha + beta) = c^dR(alpha) c^dR(beta), (2) c^dR(f^*alpha) = f^*c^dR(alpha) for every morphism f : X -> X' of quasi-compact and quasi-separated schemes, (3) c^dR([L]) = 1 + c\_1^dR(L) for L in Pic(X)”.

> There is a unique rule which assigns to every quasi-compact and quasi-separated scheme `X` a
> total Chern class `c^{dR} : K₀(Vect(X)) ⟶ ∏_{i ≥ 0} H^{2i}_{dR}(X/𝐙)`, read by components
> `c X α i ∈ H^{2i}_{dR}(X/𝐙)` in the even-degree ring, such that `c(α + β) = c(α) c(β)` (and
> `c(0) = 1`), `c(f^*α) = f^*c(α)` and `c([ℒ]) = 1 + c₁^{dR}(ℒ)`
> (`Stacks.DeRhamChern.IsDeRhamTotalChernClass`).

```lean
theorem existsUnique_deRhamTotalChernClass :
    ∃! c : ∀ X : (QCQSScheme (Spec (CommRingCat.of ℤ))).FullSubcategory,
        VectorBundleKZero ((QCQSScheme (Spec (CommRingCat.of ℤ))).ι.obj X).left → ℕ →
          evenDeRhamRing ((QCQSScheme (Spec (CommRingCat.of ℤ))).ι.obj X).hom,
      IsDeRhamTotalChernClass (QCQSScheme (Spec (CommRingCat.of ℤ))).ι c
```

## Tag 0FWA, a remark

[Tag 0FWA](https://stacks.math.columbia.edu/tag/0FWA) in the Stacks Project.

**`Stacks.DeRhamChern.exists_injective_pull_hasInvertibleFiltration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/WeilCohomology/DeRhamSplittingTwist.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/WeilCohomology/DeRhamSplittingTwist.lean#L61). The attribute's comment: “the analogue of Weil Cohomology Theories, Lemma 0FI7 (splitting principle) holds for de Rham Chern classes on quasi-compact and quasi-separated schemes: for a finite collection of locally free O\_X-modules E\_i of ranks r\_i there is p : P -> X with p^* injective on (+)\_i H^\{2i}\_dR(-/Z) and each p^*E\_i filtered with invertible successive quotients”.

> **Stacks Project, Tag 0FWA: the splitting principle for de Rham cohomology.** Let `X` be a
> quasi-compact and quasi-separated scheme and let `ℰ_i` be a finite collection of locally free
> `𝒪_X`-modules of ranks `r_i`. There is a morphism `p : P ⟶ X` of quasi-compact and
> quasi-separated schemes such that
>
> 1. `p^* : ⨁_i H^{2i}_{dR}(X/𝐙) ⟶ ⨁_i H^{2i}_{dR}(P/𝐙)` is injective,
> 2. each `p^*ℰ_i` has a filtration whose successive quotients `ℒ_{i,1}, …, ℒ_{i,r_i}` are
>    invertible `𝒪_P`-modules.
>
> The projection is moreover flat. This is Tag 0FI7 in the de Rham situation of the proof of
> Tag 0FW9.

```lean
theorem exists_injective_pull_hasInvertibleFiltration
    (X : (QCQSScheme (Spec (CommRingCat.of ℤ))).FullSubcategory) (I : Type*) [Finite I]
    (E : I → ((QCQSScheme.toScheme (Spec (CommRingCat.of ℤ))).obj X).Modules) (r : I → ℕ)
    (hE : ∀ i, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{0, 0, 0} (E i) (r i)) :
    ∃ (P : (QCQSScheme (Spec (CommRingCat.of ℤ))).FullSubcategory) (p : P ⟶ X),
      Flat ((QCQSScheme.toScheme (Spec (CommRingCat.of ℤ))).map p) ∧
      Function.Injective (pull (QCQSScheme (Spec (CommRingCat.of ℤ))).ι p) ∧
      ∀ i, HasInvertibleFiltration ((QCQSScheme.toScheme (Spec (CommRingCat.of ℤ))).obj P)
        ((Scheme.Modules.pullback ((QCQSScheme.toScheme (Spec (CommRingCat.of ℤ))).map p)).obj
          (E i)) (r i)
```

**`Stacks.DeRhamChern.IsDeRhamTotalChernClass.apply_classOf_tensorObj_invertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/WeilCohomology/DeRhamSplittingTwist.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/WeilCohomology/DeRhamSplittingTwist.lean#L86). The attribute's comment: “the analogue of Weil Cohomology Theories, Lemma 0FI8 (chern classes of tensor products) holds for de Rham Chern classes on quasi-compact and quasi-separated schemes: for the de Rham total Chern class c^dR of Tag 0FW9, E finite locally free of constant rank r, L invertible and i <= r, c^dR\_i(E (x) L) = sum\_\{j=0}^i binom(r-i+j, j) c^dR\_\{i-j}(E) cup c\_1^dR(L)^j”.

> **Stacks Project, Tag 0FWA: the Chern classes of a twist for de Rham Chern classes.** Let
> `c^{dR}` be the de Rham total Chern class of Tag 0FW9 (by that lemma there is exactly one rule with
> its three properties), let `X` be a quasi-compact and quasi-separated scheme, `ℰ` a finite locally
> free `𝒪_X`-module of constant rank `r` and `ℒ` an invertible `𝒪_X`-module. Then for `i ≤ r`
>
> `c^{dR}_i(ℰ ⊗ ℒ) = ∑_{j=0}^{i} binom(r - i + j, j) c^{dR}_{i-j}(ℰ) ∪ c₁^{dR}(ℒ)^j`
>
> in `H^{2i}_{dR}(X/𝐙)`. This is Tag 0FI8 in the de Rham situation of the proof of Tag 0FW9.

```lean
theorem IsDeRhamTotalChernClass.apply_classOf_tensorObj_invertible
    {c : ∀ X : (QCQSScheme (Spec (CommRingCat.of ℤ))).FullSubcategory,
      VectorBundleKZero ((QCQSScheme (Spec (CommRingCat.of ℤ))).ι.obj X).left → ℕ →
        evenDeRhamRing ((QCQSScheme (Spec (CommRingCat.of ℤ))).ι.obj X).hom}
    (hc : IsDeRhamTotalChernClass (QCQSScheme (Spec (CommRingCat.of ℤ))).ι c)
    (X : (QCQSScheme (Spec (CommRingCat.of ℤ))).FullSubcategory)
    (E L : ((QCQSScheme (Spec (CommRingCat.of ℤ))).ι.obj X).left.Modules) (r : ℕ)
    (hE : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{0, 0, 0} E r)
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible
      ((QCQSScheme (Spec (CommRingCat.of ℤ))).ι.obj X).left.presheaf
      ((QCQSScheme (Spec (CommRingCat.of ℤ))).ι.obj X).left.ringCatSheaf.2 L)
    (i : ℕ) (hi : i ≤ r) :
    c X (VectorBundleKZero.classOf _
        (Scheme.Modules.tensorObjRingedSpace
          ((QCQSScheme (Spec (CommRingCat.of ℤ))).ι.obj X).left E L)) i =
      ∑ j ∈ Finset.range (i + 1), (r - i + j).choose j •
        (c X (VectorBundleKZero.classOf _ E) (i - j) *
          c₁ (QCQSScheme (Spec (CommRingCat.of ℤ))).ι X
            (picardClassOf ((QCQSScheme (Spec (CommRingCat.of ℤ))).ι.obj X).left L hL) ^ j)
```

## Tag 0FWB, a lemma

[Tag 0FWB](https://stacks.math.columbia.edu/tag/0FWB) in the Stacks Project.

**`Stacks.DeRhamChern.existsUnique_deRhamChernCharacter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/WeilCohomology/DeRhamChernCharacter.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/WeilCohomology/DeRhamChernCharacter.lean#L74). The attribute's comment: “the unique rule ch^dR : K\_0(Vect(X)) -> prod\_i H^\{2i}\_dR(X/Q) on quasi-compact quasi-separated schemes X over Q, with (1) ch^dR a ring map, (2) f^* ch^dR = ch^dR f^* on all of K\_0 for every morphism f : X' -> X of quasi-compact quasi-separated schemes over Q, (3) ch^dR([L]) = exp(c\_1^dR(L)) for L in Pic(X); prod H^\{2i} read as sequences of components in ⨁ H^\{2j} with the i-th in H^\{2i}. Proved from Tag 0FI9 at the standing situation sourceChernSetupRat, whose axioms are all proved: (1) Tag 0FM3, (2) the clopen splitting, (3) Tag 0FMD, (4) Proposition 0FMT, (5) Lemmas 0FMX and 0FMY, clauses (1)-(3)(c) of the category”.

> **Stacks Project, Tag 0FWB.** There is a unique rule which assigns to every quasi-compact and
> quasi-separated scheme `X` over `𝐐` a Chern character
> `ch^{dR} : K₀(Vect(X)) ⟶ ∏_{i ≥ 0} H^{2i}_{dR}(X/𝐐)` such that (1) `ch^{dR}` is a ring map,
> (2) `f^* ∘ ch^{dR} = ch^{dR} ∘ f^*` for every morphism `f : X' ⟶ X` of quasi-compact and
> quasi-separated schemes over `𝐐`, and (3) `ch^{dR}([ℒ]) = exp(c₁^{dR}(ℒ))` for `ℒ ∈ Pic(X)`.
>
> An element of `∏_{i ≥ 0} H^{2i}_{dR}(X/𝐐)` is the sequence of its components, the `i`-th read in
> `⨁_j H^{2j}_{dR}(X/𝐐)` and lying in `H^{2i}_{dR}(X/𝐐)`; the properties are
> `Stacks.DeRhamChern.IsDeRhamChernCharacter`. The proof is the source's: the category of
> quasi-compact and quasi-separated schemes over `𝐐` with `A(X) = ⨁_i H^{2i}_{dR}(X/𝐐)` satisfies
> the axioms of Section 45.12, and `A(X)` is a `𝐐`-algebra, so Proposition 0FI9 applies.

```lean
theorem existsUnique_deRhamChernCharacter :
    ∃! ch : ∀ X : (QCQSScheme specRat).FullSubcategory,
        VectorBundleKZero X.obj.left → ℕ → evenDeRhamRing X.obj.hom,
      IsDeRhamChernCharacter (QCQSScheme specRat).ι ch
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.21, Tag 0FW8](https://stacks.math.columbia.edu/tag/0FW8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
