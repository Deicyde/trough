---
declaration: section
origin: cited
lean: Deformation.CompleteLocalAlgCat, Deformation.CompleteLocalAlgCat.Hom, Deformation.CompleteLocalAlgCat.instCategory, Deformation.surjective_iff_surjective_cotangentSpaceMap, Deformation.surjective_iff_surjective_relativeCotangentSpaceMap, Deformation.CompleteLocalAlgCat.hasPushouts, Deformation.instHasBinaryCoproducts, Deformation.derivation_module_finite
statement: formalized
proof: formalized
---

# 90.4 The completed base category

Section 90.4 of the Stacks Project, [Tag 06GV](https://stacks.math.columbia.edu/tag/06GV). 9 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06GW, a definition

[Tag 06GW](https://stacks.math.columbia.edu/tag/06GW) in the Stacks Project.

**`Deformation.CompleteLocalAlgCat`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Completed/Basic.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Completed/Basic.lean#L104). The attribute's comment: “objects”. References: SGA 7 VI (1.15), “objects, K a field”.

> A Noetherian complete local `Λ`-algebra together with a specified `Λ`-algebra
> isomorphism from its residue field to `k`. These are the objects of
> `\widehat{\mathcal C}_Λ` in Stacks Project, Tag 06GW.

```lean
structure CompleteLocalAlgCat (Λ : Type u) (k : Type w) [CommRing Λ] [Field k]
    [Algebra Λ k]
```

**`Deformation.CompleteLocalAlgCat.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Completed/Basic.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Completed/Basic.lean#L142). The attribute's comment: “morphisms”. References: SGA 7 VI (1.15), “morphisms, K a field”.

> A morphism of Noetherian complete local `Λ`-algebras with fixed residue field is a
> local `Λ`-algebra homomorphism whose induced map on residue fields respects the specified
> identifications with `k`.

```lean
structure Hom (A B : CompleteLocalAlgCat.{u, v, w} Λ k)
```

**`Deformation.CompleteLocalAlgCat.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Completed/Basic.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Completed/Basic.lean#L171). The attribute's comment: “category structure”.

> The category structure on Noetherian complete local `Λ`-algebras with fixed residue
> field. Composition is composition of the underlying local algebra homomorphisms.

```lean
instance instCategory : Category (CompleteLocalAlgCat.{u, v, w} Λ k)
```

## Tag 06GZ, a lemma

[Tag 06GZ](https://stacks.math.columbia.edu/tag/06GZ) in the Stacks Project.

**`Deformation.surjective_iff_surjective_cotangentSpaceMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Completed/Basic.lean, line 519](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Completed/Basic.lean#L519). The attribute's comment: “conditions (1) and (2)”.

> A morphism of Noetherian complete local algebras is surjective if and only if its
> canonical map `m_R / m_R² → m_S / m_S²` is surjective.

```lean
theorem surjective_iff_surjective_cotangentSpaceMap
    {R S : CompleteLocalAlgCat.{u, v, w} Λ k} (f : R ⟶ S) :
    Function.Surjective f.hom ↔
      Function.Surjective
        (Ideal.mapCotangent (maximalIdeal R) (maximalIdeal S) f.hom
          (by
            let _ : IsLocalHom f.hom.toRingHom := f.isLocal
            intro x hx
            change x ∈ (maximalIdeal S).comap f.hom.toRingHom
            simpa only [maximalIdeal_comap] using hx))
```

**`Deformation.surjective_iff_surjective_relativeCotangentSpaceMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Completed/Basic.lean, line 541](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Completed/Basic.lean#L541). The attribute's comment: “conditions (1) and (3)”.

> A morphism of Noetherian complete local algebras is surjective if and only if its map
> `m_R / (m_Λ R + m_R²) → m_S / (m_Λ S + m_S²)` is surjective.

```lean
theorem surjective_iff_surjective_relativeCotangentSpaceMap
    {R S : CompleteLocalAlgCat.{u, v, w} Λ k} (f : R ⟶ S) :
    Function.Surjective f.hom ↔ Function.Surjective (relativeCotangentSpaceMap f)
```

## Tag 06SB, a lemma

[Tag 06SB](https://stacks.math.columbia.edu/tag/06SB) in the Stacks Project.

**`Deformation.CompleteLocalAlgCat.hasPushouts`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Completed/Pushout.lean, line 972](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Completed/Pushout.lean#L972).

> The category of Noetherian complete local `Λ`-algebras with residue field identified
> with `k` admits pushouts.

```lean
public instance hasPushouts :
    HasPushouts (CompleteLocalAlgCat.{u, v, w} Λ k)
```

## Tag 06H1, a lemma

[Tag 06H1](https://stacks.math.columbia.edu/tag/06H1) in the Stacks Project.

**`Deformation.instHasBinaryCoproducts`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Completed/Coproduct.lean, line 558](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Completed/Coproduct.lean#L558).

> The category of Noetherian complete local `Λ`-algebras with residue field `k`
> admits coproducts of pairs of objects.

```lean
instance instHasBinaryCoproducts {Λ : Type u} {k : Type w}
    [CommRing Λ] [Field k] [Algebra Λ k] [Algebra.FiniteType Λ k] :
    HasBinaryCoproducts (CompleteLocalAlgCat.{u, v, w} Λ k)
```

## Tag 06SC, a lemma

[Tag 06SC](https://stacks.math.columbia.edu/tag/06SC) in the Stacks Project.

**`Deformation.derivation_module_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Completed/Basic.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Completed/Basic.lean#L222).

> **Stacks Project, Tag 06SC.** The `k`-vector space of `Λ`-derivations from a
> Noetherian local `Λ`-algebra with residue field `k` to `k` is finite-dimensional.

```lean
theorem derivation_module_finite
    {Λ : Type u} {S : Type v} {k : Type w} [CommRing Λ] [CommRing S]
    [IsLocalRing S] [IsNoetherianRing S] [Field k] [Algebra Λ S] [Algebra Λ k]
    [Module.Finite Λ k] (e : ResidueField S ≃ₐ[Λ] k) :
    letI : Algebra S k :=
      (e.toAlgHom.comp (IsScalarTower.toAlgHom Λ S (ResidueField S))).toRingHom.toAlgebra
    Module.Finite k (Derivation Λ S k)
```

## Tag 06SD, a lemma

[Tag 06SD](https://stacks.math.columbia.edu/tag/06SD) in the Stacks Project.

**`Deformation.surjective_of_residueDerivation_comap_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Completed/Basic.lean, line 650](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Completed/Basic.lean#L650).

> A morphism of Noetherian complete local algebras with fixed residue field is
> surjective if restriction of residue-field-valued derivations along it is injective.

```lean
public theorem surjective_of_residueDerivation_comap_injective
    {R S : CompleteLocalAlgCat.{u, v, w} Λ k} (f : R ⟶ S)
    (h : Function.Injective (ResidueDerivation.comap f)) :
    Function.Surjective f.hom
```

## Tag 06SE, a lemma

[Tag 06SE](https://stacks.math.columbia.edu/tag/06SE) in the Stacks Project.

**`Deformation.quotient_filtration_isAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Completed/InverseLimit.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Completed/InverseLimit.lean#L191).

> Let `A` be a Noetherian complete local algebra and let `J n` be a decreasing sequence of
> ideals containing the `n`-th power of the maximal ideal.  In the quotient by `⋂ n, J n`, the
> images of the `J n` form an adic filtration for the image of the maximal ideal.

```lean
theorem quotient_filtration_isAdic
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (A : CompleteLocalAlgCat.{u, v, w} Λ k) (J : ℕ → Ideal A)
    (hJ : Antitone J) (hpow : ∀ n, maximalIdeal A ^ n ≤ J n) :
    Ideal.IsAdicFiltration
      (Ideal.map (Ideal.Quotient.mk (⨅ n, J n)) (maximalIdeal A))
      (fun n ↦ Ideal.map (Ideal.Quotient.mk (⨅ n, J n)) (J n))
```

## Tag 06SF, a lemma

[Tag 06SF](https://stacks.math.columbia.edu/tag/06SF) in the Stacks Project.

**`Deformation.inverseLimit_isObjectOfCompleteLocalAlgCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Completed/InverseLimit.lean, line 1068](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Completed/InverseLimit.lean#L1068). The attribute's comment: “complete local inverse limit”.

> **Stacks Project, Tag 06SF (first assertion).** If the transition maps in a tower of
> Artinian local `Λ`-algebras are surjective and the dimensions of the cotangent spaces are
> bounded, then its inverse limit is a Noetherian complete local algebra whose residue field is
> the specified field `k`.

```lean
theorem inverseLimit_isObjectOfCompleteLocalAlgCat
    (A : ℕ → ArtinianLocalAlgCat.{u, v, w} Λ k)
    (f : ∀ n, A (n + 1) ⟶ A n)
    (hsurj : ∀ n, Function.Surjective (f n).hom)
    (hbounded : ∃ d : ℕ,
      ∀ n, Module.finrank (ResidueField (A n)) (CotangentSpace (A n)) ≤ d) :
    ∃ h : IsNoetherianCompleteLocalRing (inverseLimit A f),
      letI : IsLocalRing (inverseLimit A f) := h.isLocal
      Nonempty (ResidueField (inverseLimit A f) ≃ₐ[Λ] k)
```

**`Deformation.kernel_projections_define_maximalIdeal_adicTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Completed/InverseLimit.lean, line 1095](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Completed/InverseLimit.lean#L1095). The attribute's comment: “projection kernels define the adic topology”.

> **Stacks Project, Tag 06SF (second assertion).** Under the same hypotheses, the kernels of
> the projections from the inverse limit are cofinal with the powers of its maximal ideal, and
> hence define its maximal-ideal-adic topology.

```lean
theorem kernel_projections_define_maximalIdeal_adicTopology
    (A : ℕ → ArtinianLocalAlgCat.{u, v, w} Λ k)
    (f : ∀ n, A (n + 1) ⟶ A n)
    (hsurj : ∀ n, Function.Surjective (f n).hom)
    (h : IsNoetherianCompleteLocalRing (inverseLimit A f)) :
    letI : IsLocalRing (inverseLimit A f) := h.isLocal
    Ideal.IsAdicFiltration (maximalIdeal (inverseLimit A f))
      (fun n ↦ RingHom.ker (inverseLimitProj A f n))
```

## Tag 06SG, a lemma

[Tag 06SG](https://stacks.math.columbia.edu/tag/06SG) in the Stacks Project.

**`Deformation.mvPowerSeries_bijective_of_eventually_quotient_retract`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Completed/PowerSeries.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Completed/PowerSeries.lean#L249).

> Suppose `R` is the additive direct sum of the image of `R'` and an ideal `I`, and
> `x : Fin r → I` is a basis of `I / 𝔪_R I`.  The power-series map which sends `X i` to
> `x i` is bijective if, in all sufficiently high degrees, its maps modulo powers of the
> maximal ideals have local `Λ`-algebra retractions.

```lean
public theorem mvPowerSeries_bijective_of_eventually_quotient_retract
    {R' R : CompleteLocalAlgCat.{u, v, w} Λ k} (f : R' ⟶ R) (I : Ideal R)
    (hdecomp : ∀ z : R, ∃! p : R' × I, z = f.hom p.1 + p.2.1)
    {r : ℕ} (x : Fin r → I)
    (hspan : ∀ y : I, ∃ a : Fin r → R,
      y.1 - ∑ i, a i * (x i).1 ∈ maximalIdeal R * I)
    (hindep : ∀ a : Fin r → R,
      (∑ i, a i * (x i).1 ∈ maximalIdeal R * I) →
        ∀ i, a i ∈ maximalIdeal R)
    (F : MvPowerSeries (Fin r) R' →+* R)
    (hF_C : ∀ a : R', F (MvPowerSeries.C a) = f.hom a)
    (hF_X : ∀ i, F (MvPowerSeries.X i) = (x i).1)
    (hretract : ∃ N : ℕ, ∀ n : ℕ, N ≤ n →
      Ideal.map F (maximalIdeal (MvPowerSeries (Fin r) R') ^ n) ≤
          maximalIdeal R ^ n ∧
        ∃ h : (R ⧸ maximalIdeal R ^ n) →+*
            (MvPowerSeries (Fin r) R' ⧸ maximalIdeal (MvPowerSeries (Fin r) R') ^ n),
          IsLocalHom h ∧
          (∀ s : MvPowerSeries (Fin r) R',
            h (Ideal.Quotient.mk (maximalIdeal R ^ n) (F s)) =
              Ideal.Quotient.mk (maximalIdeal (MvPowerSeries (Fin r) R') ^ n) s) ∧
      (∀ a : Λ,
            h (Ideal.Quotient.mk (maximalIdeal R ^ n) (algebraMap Λ R a)) =
              Ideal.Quotient.mk (maximalIdeal (MvPowerSeries (Fin r) R') ^ n)
                (MvPowerSeries.C (algebraMap Λ R' a)))) :
    Function.Bijective F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.4, Tag 06GV](https://stacks.math.columbia.edu/tag/06GV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
