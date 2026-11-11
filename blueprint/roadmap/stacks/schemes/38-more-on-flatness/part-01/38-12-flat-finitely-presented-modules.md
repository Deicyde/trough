---
declaration: section
origin: cited
lean: Module.exists_freeMap_bijective_residueField, Module.universallyInjective_localizedMap_of_flat_localizedModule, Module.exists_universallyInjective_localizedModule_away_of_flat_localizedModule, Module.flat_localizedModule_coker_of_flat_localizedModule, Module.exists_universallyInjective_and_flat_coker_of_flat_localizedModule, Module.universallyInjective_localizedMap_and_flat_coker_of_exists_away, Module.injective_localizedMap_of_universallyInjective_localizedMap, Module.bijective_localizedMap_map_of_injective_localizedMap
statement: formalized
proof: formalized
---

# 38.12 Flat finitely presented modules

Section 38.12 of the Stacks Project, [Tag 05I9](https://stacks.math.columbia.edu/tag/05I9). 10 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05IA, a lemma

[Tag 05IA](https://stacks.math.columbia.edu/tag/05IA) in the Stacks Project.

**`Module.exists_freeMap_bijective_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapAtGenericFibre.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapAtGenericFibre.lean#L136). The attribute's comment: “existence”.

> **Stacks Project, Tag 05IA, the existence assertion.** Let `R → S` be flat with a
> geometrically integral fibre over the prime `r`, and let `N` be a finite `S`-module. Then the
> extension `𝔭 = rS` is prime and some map from a finite free `S`-module to `N` becomes an
> isomorphism after base change to the residue field `κ(𝔭)`.

```lean
public theorem Module.exists_freeMap_bijective_residueField {R S N : Type u} [CommRing R]
    [CommRing S] [Algebra R S] [Module.Flat R S] {r : Ideal R} [r.IsPrime] [AddCommGroup N]
    [Module S N] [Module.Finite S N]
    (hgeom : Algebra.IsGeometricallyIntegral r.ResidueField (r.Fiber S)) :
    ∃ (n : ℕ) (a : (Fin n → S) →ₗ[S] N),
      ∃ hp : (r.map (algebraMap R S)).IsPrime,
        Function.Bijective
          (a.rTensor (@Ideal.ResidueField S _ (r.map (algebraMap R S)) hp))
```

**`Module.universallyInjective_localizedMap_of_flat_localizedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapSpreadingOut.lean, line 656](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapSpreadingOut.lean#L656). The attribute's comment: “the implication (1) ⟹ (3), the universal injectivity of `α_𝔯` over `R_𝔯`”.

> Let `R → S` be a flat ring map of finite presentation with geometrically integral fibres,
> let `q ⊆ S` be a prime lying over `r = q ∩ R`, write `p = rS` for the generic point of the fibre
> over `r`, let `N` be a finite `S`-module and let `alpha : S^{⊕ n} → N` become injective over
> `κ(p)`. If `N_q` is flat over `R` then `alpha_r : S_r^{⊕ n} → N_r` is universally injective as a
> map of `R`-modules.

```lean
public theorem Module.universallyInjective_localizedMap_of_flat_localizedModule
    (R S : Type u) [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.FinitePresentation R S] [Module.Flat R S]
    [GeometricallyIntegral (Spec.map (ofHom (algebraMap R S)))]
    (q : Ideal S) [q.IsPrime]
    (N : Type w) [AddCommGroup N] [Module S N] [Module R N] [IsScalarTower R S N]
    [Module.Finite S N] (n : ℕ) (alpha : (Fin n → S) →ₗ[S] N)
    (halpha : letI := Ideal.isPrime_map_of_geometricallyIntegral R S (q.under R)
      Function.Injective (alpha.rTensor
        (Ideal.map (algebraMap R S) (q.under R)).ResidueField))
    (hflat : Module.Flat R (LocalizedModule q.primeCompl N))
    (Q : Type (max u w)) [AddCommGroup Q] [Module R Q] :
    Function.Injective (((LocalizedModule.map (q.under R).primeCompl
      (alpha.restrictScalars R)).restrictScalars R).rTensor Q)
```

**`Module.exists_universallyInjective_localizedModule_away_of_flat_localizedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapSpreadingOut.lean, line 757](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapSpreadingOut.lean#L757). The attribute's comment: “the first half of the implication (1) ⟹ (2), the universal injectivity of `α_f`”.

> In the situation of `Module.universallyInjective_localizedMap_of_flat_localizedModule`, with
> `N` finitely presented and `alpha` an isomorphism over `κ(p)`, there is an `f ∈ R`, `f ∉ r`, such
> that `alpha_f : S_f^{⊕ n} → N_f` is universally injective as a map of `R`-modules.

```lean
public theorem Module.exists_universallyInjective_localizedModule_away_of_flat_localizedModule
    (R S : Type u) [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.FinitePresentation R S] [Module.Flat R S]
    [GeometricallyIntegral (Spec.map (ofHom (algebraMap R S)))]
    (r : Ideal R) [r.IsPrime] (q : Ideal S) [q.IsPrime] (hq : q.under R = r)
    (N : Type u) [AddCommGroup N] [Module S N] [Module R N] [IsScalarTower R S N]
    [Module.FinitePresentation S N] (n : ℕ) (alpha : (Fin n → S) →ₗ[S] N)
    (halpha : letI := Ideal.isPrime_map_of_geometricallyIntegral R S r
      Function.Bijective (alpha.rTensor (Ideal.map (algebraMap R S) r).ResidueField))
    (hflat : Module.Flat R (LocalizedModule q.primeCompl N)) :
    ∃ f ∈ r.primeCompl, ∀ (Q : Type u) [AddCommGroup Q] [Module R Q],
        Function.Injective (((LocalizedModule.map (Submonoid.powers f)
          (alpha.restrictScalars R)).restrictScalars R).rTensor Q)
```

**`Module.flat_localizedModule_coker_of_flat_localizedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapSpreadingOut.lean, line 869](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapSpreadingOut.lean#L869). The attribute's comment: “the flatness of `Coker(α)_𝔮`, the second half of conditions (3) to (6)”.

> In the situation of `Module.universallyInjective_localizedMap_of_flat_localizedModule` the
> localization of `Coker(alpha)` at `q` is flat over `R`.

```lean
public theorem Module.flat_localizedModule_coker_of_flat_localizedModule
    (R S : Type u) [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.FinitePresentation R S] [Module.Flat R S]
    [GeometricallyIntegral (Spec.map (ofHom (algebraMap R S)))]
    (q : Ideal S) [q.IsPrime]
    (N : Type u) [AddCommGroup N] [Module S N] [Module R N] [IsScalarTower R S N]
    [Module.Finite S N] (n : ℕ) (alpha : (Fin n → S) →ₗ[S] N)
    (halpha : letI := Ideal.isPrime_map_of_geometricallyIntegral R S (q.under R)
      Function.Injective (alpha.rTensor
        (Ideal.map (algebraMap R S) (q.under R)).ResidueField))
    (hflat : Module.Flat R (LocalizedModule q.primeCompl N)) :
    Module.Flat R (LocalizedModule q.primeCompl (N ⧸ LinearMap.range alpha))
```

**`Module.exists_universallyInjective_and_flat_coker_of_flat_localizedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapSpreadingOut.lean, line 931](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapSpreadingOut.lean#L931). The attribute's comment: “the implication (1) ⟹ (2)”.

> Let `R → S` be a flat ring map of finite presentation with geometrically integral fibres,
> let `q ⊆ S` be a prime lying over `r = q ∩ R`, write `p = rS`, let `N` be a finitely presented
> `S`-module and let `alpha : S^{⊕ n} → N` be an isomorphism over `κ(p)`. If `N_q` is flat over `R`
> then there are an `f ∈ R`, `f ∉ r`, such that `alpha_f` is universally injective as a map of
> `R`-modules, and a `g ∈ S`, `g ∉ q`, such that `Coker(alpha)_g` is flat over `R`.

```lean
public theorem Module.exists_universallyInjective_and_flat_coker_of_flat_localizedModule
    (R S : Type u) [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.FinitePresentation R S] [Module.Flat R S]
    [GeometricallyIntegral (Spec.map (ofHom (algebraMap R S)))]
    (q : Ideal S) [q.IsPrime]
    (N : Type u) [AddCommGroup N] [Module S N] [Module R N] [IsScalarTower R S N]
    [Module.FinitePresentation S N] (n : ℕ) (alpha : (Fin n → S) →ₗ[S] N)
    (halpha : letI := Ideal.isPrime_map_of_geometricallyIntegral R S (q.under R)
      Function.Bijective (alpha.rTensor
        (Ideal.map (algebraMap R S) (q.under R)).ResidueField))
    (hflat : Module.Flat R (LocalizedModule q.primeCompl N)) :
    (∃ f ∈ (q.under R).primeCompl, ∀ (Q : Type u) [AddCommGroup Q] [Module R Q],
        Function.Injective (((LocalizedModule.map (Submonoid.powers f)
          (alpha.restrictScalars R)).restrictScalars R).rTensor Q)) ∧
      ∃ g ∈ q.primeCompl, Module.Flat R (LocalizedModule.Away g (N ⧸ LinearMap.range alpha))
```

**`Module.universallyInjective_localizedMap_and_flat_coker_of_exists_away`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapSpreadingOut.lean, line 1139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapSpreadingOut.lean#L1139). The attribute's comment: “the implication (2) ⟹ (3)”.

> If `alpha_f` is universally injective as a map of `R`-modules for some `f ∈ R`, `f ∉ r`, and
> `Coker(alpha)_g` is `R`-flat for some `g ∈ S`, `g ∉ q`, then `alpha_r` is universally injective
> as a map of `R`-modules and `Coker(alpha)_q` is `R`-flat. The prime `q` need not lie over `r`.

```lean
public theorem Module.universallyInjective_localizedMap_and_flat_coker_of_exists_away
    (R S : Type u) [CommRing R] [CommRing S] [Algebra R S] (r : Ideal R) [r.IsPrime]
    (q : Ideal S) [q.IsPrime]
    (N : Type w) [AddCommGroup N] [Module S N] [Module R N] [IsScalarTower R S N] (n : ℕ)
    (alpha : (Fin n → S) →ₗ[S] N)
    (h : (∃ f ∈ r.primeCompl, UniversallyInjective.{max u w} (A := R)
            ((LocalizedModule.map (Submonoid.powers f)
              (alpha.restrictScalars R)).restrictScalars R)) ∧
      ∃ g ∈ q.primeCompl,
        Module.Flat R (LocalizedModule.Away g (N ⧸ LinearMap.range alpha))) :
    UniversallyInjective.{max u w} (A := R)
        ((LocalizedModule.map r.primeCompl (alpha.restrictScalars R)).restrictScalars R) ∧
      Module.Flat R (LocalizedModule q.primeCompl (N ⧸ LinearMap.range alpha))
```

**`Module.injective_localizedMap_of_universallyInjective_localizedMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapSpreadingOut.lean, line 1168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapSpreadingOut.lean#L1168). The attribute's comment: “the implication (3) ⟹ (4), the injectivity of `α_𝔯`”.

> If `alpha_r` is universally injective as a map of `R`-modules then it is injective.

```lean
public theorem Module.injective_localizedMap_of_universallyInjective_localizedMap
    (R S : Type u) [CommRing R] [CommRing S] [Algebra R S] (r : Ideal R) [r.IsPrime]
    (N : Type w) [AddCommGroup N] [Module S N] [Module R N] [IsScalarTower R S N] (n : ℕ)
    (alpha : (Fin n → S) →ₗ[S] N)
    (h : UniversallyInjective.{max u w} (A := R)
      ((LocalizedModule.map r.primeCompl (alpha.restrictScalars R)).restrictScalars R)) :
    Function.Injective (LocalizedModule.map r.primeCompl (alpha.restrictScalars R))
```

**`Module.bijective_localizedMap_map_of_injective_localizedMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapSpreadingOut.lean, line 1181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapSpreadingOut.lean#L1181). The attribute's comment: “the implication (4) ⟹ (5), the isomorphism `α_𝔭`”.

> If `alpha` is surjective over `κ(p)` and `alpha_r` is injective, then `alpha_p` is an
> isomorphism at the generic point `p = rS` of the fibre over `r`.

```lean
public theorem Module.bijective_localizedMap_map_of_injective_localizedMap (R S : Type u)
    [CommRing R] [CommRing S] [Algebra R S] [Algebra.FinitePresentation R S] [Module.Flat R S]
    [GeometricallyIntegral (Spec.map (ofHom (algebraMap R S)))] (r : Ideal R) [r.IsPrime]
    (N : Type w) [AddCommGroup N] [Module S N] [Module R N] [IsScalarTower R S N]
    [Module.Finite S N] (n : ℕ) (alpha : (Fin n → S) →ₗ[S] N)
    (halpha : letI := Ideal.isPrime_map_of_geometricallyIntegral R S r
      Function.Surjective (alpha.rTensor (Ideal.map (algebraMap R S) r).ResidueField))
    (hinj : Function.Injective (LocalizedModule.map r.primeCompl (alpha.restrictScalars R))) :
    letI := Ideal.isPrime_map_of_geometricallyIntegral R S r
    Function.Bijective
      (LocalizedModule.map (Ideal.map (algebraMap R S) r).primeCompl alpha)
```

**`Module.injective_localizedMap_atPrime_of_bijective_localizedMap_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapSpreadingOut.lean, line 1201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapSpreadingOut.lean#L1201). The attribute's comment: “the implication (5) ⟹ (6), the injectivity of `α_𝔮`”.

> If `alpha_p` is an isomorphism at the generic point `p = rS` of the fibre over `r` then
> `alpha_q` is injective at every prime `q` of `S` lying over `r`.

```lean
public theorem Module.injective_localizedMap_atPrime_of_bijective_localizedMap_map (R S : Type u)
    [CommRing R] [CommRing S] [Algebra R S] [Algebra.FinitePresentation R S] [Module.Flat R S]
    [GeometricallyIntegral (Spec.map (ofHom (algebraMap R S)))] (r : Ideal R) [r.IsPrime]
    (q : Ideal S) [q.IsPrime] (hq : q.under R = r)
    (N : Type w) [AddCommGroup N] [Module S N] (n : ℕ) (alpha : (Fin n → S) →ₗ[S] N)
    (hbij : letI := Ideal.isPrime_map_of_geometricallyIntegral R S r
      Function.Bijective (LocalizedModule.map (Ideal.map (algebraMap R S) r).primeCompl alpha)) :
    Function.Injective (LocalizedModule.map q.primeCompl alpha)
```

**`Module.flat_localizedModule_of_injective_localizedMap_of_flat_coker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapSpreadingOut.lean, line 1220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapSpreadingOut.lean#L1220). The attribute's comment: “the implication (6) ⟹ (1)”.

> For `S` flat over `R`, if `alpha_q` is injective and `Coker(alpha)_q` is `R`-flat then `N_q`
> is `R`-flat.

```lean
public theorem Module.flat_localizedModule_of_injective_localizedMap_of_flat_coker (R S : Type u)
    [CommRing R] [CommRing S] [Algebra R S] [Module.Flat R S] (q : Ideal S) [q.IsPrime]
    (N : Type w) [AddCommGroup N] [Module S N] [Module R N] [IsScalarTower R S N] (n : ℕ)
    (alpha : (Fin n → S) →ₗ[S] N)
    (hinj : Function.Injective (LocalizedModule.map q.primeCompl alpha))
    (hC : Module.Flat R (LocalizedModule q.primeCompl (N ⧸ LinearMap.range alpha))) :
    Module.Flat R (LocalizedModule q.primeCompl N)
```

**`Module.flat_localizedModule_freeMap_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapSpreadingOut.lean, line 1249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FinitelyPresented/FreeMapSpreadingOut.lean#L1249). The attribute's comment: “the equivalence of the six conditions”.

> Let `R → S` be a finitely presented flat ring map with geometrically integral fibres, let
> `q ⊆ S` be a prime lying over `r ⊆ R`, write `p = rS` for the generic point of the fibre over `r`,
> let `N` be a finitely presented `S`-module and let `alpha : S^{⊕ n} → N` become an isomorphism
> over `κ(p)`. Then the following six conditions are equivalent:
>
> 1. `N_q` is `R`-flat;
> 2. there are an `f ∈ R`, `f ∉ r`, with `alpha_f` universally injective over `R`, and a `g ∈ S`,
>    `g ∉ q`, with `Coker(alpha)_g` `R`-flat;
> 3. `alpha_r` is universally injective over `R` and `Coker(alpha)_q` is `R`-flat;
> 4. `alpha_r` is injective and `Coker(alpha)_q` is `R`-flat;
> 5. `alpha_p` is an isomorphism and `Coker(alpha)_q` is `R`-flat;
> 6. `alpha_q` is injective and `Coker(alpha)_q` is `R`-flat.

```lean
public theorem Module.flat_localizedModule_freeMap_tfae (R S : Type u) [CommRing R] [CommRing S]
    [Algebra R S] [Algebra.FinitePresentation R S] [Module.Flat R S]
    [GeometricallyIntegral (Spec.map (ofHom (algebraMap R S)))] (r : Ideal R) [r.IsPrime]
    (q : Ideal S) [q.IsPrime] (hq : q.under R = r)
    (N : Type u) [AddCommGroup N] [Module S N] [Module R N] [IsScalarTower R S N]
    [Module.FinitePresentation S N] (n : ℕ) (alpha : (Fin n → S) →ₗ[S] N)
    (halpha : letI := Ideal.isPrime_map_of_geometricallyIntegral R S r
      Function.Bijective (alpha.rTensor (Ideal.map (algebraMap R S) r).ResidueField)) :
    letI := Ideal.isPrime_map_of_geometricallyIntegral R S r
    List.TFAE [
      Module.Flat R (LocalizedModule q.primeCompl N),
      (∃ f ∈ r.primeCompl, UniversallyInjective.{u} (A := R)
            ((LocalizedModule.map (Submonoid.powers f)
              (alpha.restrictScalars R)).restrictScalars R)) ∧
        ∃ g ∈ q.primeCompl,
          Module.Flat R (LocalizedModule.Away g (N ⧸ LinearMap.range alpha)),
      UniversallyInjective.{u} (A := R)
          ((LocalizedModule.map r.primeCompl (alpha.restrictScalars R)).restrictScalars R) ∧
        Module.Flat R (LocalizedModule q.primeCompl (N ⧸ LinearMap.range alpha)),
      Function.Injective (LocalizedModule.map r.primeCompl (alpha.restrictScalars R)) ∧
        Module.Flat R (LocalizedModule q.primeCompl (N ⧸ LinearMap.range alpha)),
      Function.Bijective (LocalizedModule.map (Ideal.map (algebraMap R S) r).primeCompl alpha) ∧
        Module.Flat R (LocalizedModule q.primeCompl (N ⧸ LinearMap.range alpha)),
      Function.Injective (LocalizedModule.map q.primeCompl alpha) ∧
        Module.Flat R (LocalizedModule q.primeCompl (N ⧸ LinearMap.range alpha))]
```

## Tag 05IB, a lemma

[Tag 05IB](https://stacks.math.columbia.edu/tag/05IB) in the Stacks Project.

**`Module.CompleteDevissage.exists_away_decomposition_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/DevissageAwayGeneralBase.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/DevissageAwayGeneralBase.lean#L239). The attribute's comment: “the decomposition and projectivity, over a general base”.

> **Stacks Project, Tag 05IB.** Let `N` be a finitely presented module over a finitely
> presented `R`-algebra `S` which is flat over `R`, and let `N/S/R` admit a complete dévissage over
> a prime `r` of `R`. Then there is an `a ∈ R` outside `r` such that, over `R_a`, the stage algebras
> of the dévissage stay smooth with geometrically irreducible fibres, the module `N_a` is the direct
> sum of the finite free modules `(Bᵢ)_a^{⊕ rᵢ}` over them, and `N_a` is projective.
>
> One and the same `a` does all of this: it is the element of
> `Module.CompleteDevissage.exists_away_injective_alpha`, after inverting which the away-localized
> dévissage (`Module.CompleteDevissage.localizeAwayCanonical`) has injective stage maps, so that
> `Module.CompleteDevissage.nonempty_linearEquiv_directSum` gives the decomposition and
> `Module.CompleteDevissage.projective_of_injective_alpha` the projectivity, the lower algebras
> being projective over the new base by Stacks 05FT
> (`Module.CompleteDevissage.projective_lowerAlgebra`). The smoothness and the fibres are the fields
> of the away-localized dévissage.

```lean
public theorem exists_away_decomposition_projective (D : CompleteDevissage R S N r) :
    ∃ a ∈ r.primeCompl,
      (∀ i, Algebra.Smooth (Localization.Away a) (D.locAwayB a i)) ∧
      (∀ i, GeometricallyIrreducible
        (Spec.map (ofHom (algebraMap (Localization.Away a) (D.locAwayB a i))))) ∧
      Nonempty (LocalizedModule (Submonoid.powers a) N ≃ₗ[Localization.Away a]
        ⨁ i : Fin (D.stepCount + 1), (Fin (D.multiplicity i) →₀ D.locAwayB a i)) ∧
      Module.Projective (Localization.Away a) (LocalizedModule (Submonoid.powers a) N)
```

**`Module.CompleteDevissage.nonempty_linearEquiv_directSum_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/EtaleNeighborhoodProjectiveSections.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/EtaleNeighborhoodProjectiveSections.lean#L223). The attribute's comment: “the decomposition, over a local base”.

> **The decomposition over a local base.** Let `R` be a local ring, let `N` be a finite
> `S`-module flat over `R` and let `N/S/R` have a complete dévissage over the maximal ideal of `R`.
> Then `N` is, as an `R`-module, the direct sum of the finite free modules `Bᵢ^{⊕ rᵢ}` over the
> smooth stage algebras of the dévissage.

```lean
public theorem nonempty_linearEquiv_directSum_of_flat [IsLocalRing R] [Module.Flat R N]
    (D : CompleteDevissage R S N r) (hr : r = IsLocalRing.maximalIdeal R) :
    Nonempty (N ≃ₗ[R] ⨁ i : Fin (D.stepCount + 1), (Fin (D.multiplicity i) →₀ D.B i))
```

**`Module.CompleteDevissage.projective_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/EtaleNeighborhoodProjectiveSections.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/EtaleNeighborhoodProjectiveSections.lean#L233). The attribute's comment: “projectivity over a local base”.

> **Projectivity over a local base.** In the situation of
> `Module.CompleteDevissage.nonempty_linearEquiv_directSum_of_flat` the module `N` is projective
> over `R`.

```lean
public theorem projective_of_flat [IsLocalRing R] [Module.Flat R N]
    (D : CompleteDevissage R S N r) (hr : r = IsLocalRing.maximalIdeal R) :
    Module.Projective R N
```

## Tag 05ID, a proposition

[Tag 05ID](https://stacks.math.columbia.edu/tag/05ID) in the Stacks Project.

**`AlgebraicGeometry.exists_elementaryEtaleNeighborhood_projective_sections_of_isFlatOverAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/ProjectiveSectionsFlatAtPoint.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/ProjectiveSectionsFlatAtPoint.lean#L244).

> **Stacks Project, Tag 05ID.** A finitely presented quasi-coherent module which is flat over
> the base at a point has projective global sections after compatible affine elementary étale
> localization of the source and of the base.
>
> Openness of the flat locus (Tag 0399) replaces `X` by the open subscheme on which `F` is flat over
> `S`; Proposition 05HR and Remark 05I0 then produce an affine elementary étale square carrying a
> complete dévissage of the global sections at the prime of the distinguished point, and Lemma 05IB
> over a general base makes those sections projective after inverting a global function on the new
> base which does not vanish at the distinguished point. Shrinking the square to the basic opens of
> that function and of its pullback gives the square of the conclusion.

```lean
theorem exists_elementaryEtaleNeighborhood_projective_sections_of_isFlatOverAt
    {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) (x : X)
    [LocallyOfFinitePresentation f] [F.IsQuasicoherent] [F.IsFinitePresentation]
    (hflat : IsFlatOverAt f.toLRSHom.toShHom F x) :
    ∃ (V : EtaleNeighborhood S (f x))
      (U : EtaleNeighborhood X x) (h : U.scheme ⟶ V.scheme),
      V.IsElementary ∧ U.IsElementary ∧
        (h ≫ V.toBase = U.toBase ≫ f) ∧ (h U.point = V.point) ∧
        IsAffine U.scheme ∧ IsAffine V.scheme ∧
        (let M := (Scheme.Modules.pullback U.toBase).obj F
         letI : Module Γ(V.scheme, ⊤) Γ(M, ⊤) :=
           Module.compHom Γ(M, ⊤) h.appTop.hom
         Module.Projective Γ(V.scheme, ⊤) Γ(M, ⊤))
```

## Tag 05KW, a lemma

[Tag 05KW](https://stacks.math.columbia.edu/tag/05KW) in the Stacks Project.

**`AlgebraicGeometry.exists_elementaryEtaleNeighborhood_projective_sections_along_fibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/ProjectiveSectionsAlongFibre.lean, line 619](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/ProjectiveSectionsAlongFibre.lean#L619).

> **Stacks Project, Tag 05KW.** Let `f : X ⟶ S` be of finite presentation, let `F` be a
> quasi-coherent `𝒪_X`-module of finite presentation and let `s ∈ S` be such that `F` is flat over
> `S` at every point of the fibre `X_s`. Then there is an elementary étale neighbourhood
> `(S', s') ⟶ (S, s)` and a commutative square whose upper arrow `g : X' ⟶ X` is étale, with `X'`
> and `S'` affine, with `X_s ⊆ g(X')`, and with `Γ(X', g^*F)` a projective
> `Γ(S', 𝒪_{S'})`-module.
>
> Tag 05ID enters as
> `AlgebraicGeometry.exists_elementaryEtaleNeighborhood_projective_sections_of_isFlatOverAt`.

```lean
theorem exists_elementaryEtaleNeighborhood_projective_sections_along_fibre
    {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) (s : S)
    (hf : FinitePresentation f)
    [F.IsQuasicoherent] [F.IsFinitePresentation]
    (hflat : ∀ x : f.fiber s,
      IsFlatOverAt f.toLRSHom.toShHom F (f.fiberι s x)) :
    ∃ (U : EtaleNeighborhood S s) (X' : Scheme.{u})
      (h : X' ⟶ U.scheme) (g : X' ⟶ X),
      U.IsElementary ∧ IsAffine U.scheme ∧ IsAffine X' ∧ Etale g ∧
      g ≫ f = h ≫ U.toBase ∧
      f ⁻¹' {s} ⊆ Set.range g ∧
      (let N := Γ((Scheme.Modules.pullback g).obj F, ⊤)
       letI : Module Γ(U.scheme, ⊤) N := Module.compHom N h.appTop.hom
       Module.Projective Γ(U.scheme, ⊤) N)
```

## Tag 05IE, a lemma

[Tag 05IE](https://stacks.math.columbia.edu/tag/05IE) in the Stacks Project.

**`AlgebraicGeometry.exists_elementaryEtaleNeighborhood_projective_structureSheafSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/StructureSheafProjectiveSections.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/StructureSheafProjectiveSections.lean#L196). The attribute's comment: “the full conclusion; assumes only `hdev` of Tag 05ID at the structure sheaf”.

> **Stacks Project, Tag 05IE.** Let `f : X ⟶ S` be locally of finite presentation and let
> `x : X`. If `f` is flat at `x` over `S`, then there is a commutative square of pointed schemes
> ```
>   (X, x) ←ᵍ (X', x')
>     ↓          ↓
>   (S, s) ← (S', s')
> ```
> whose horizontal arrows are elementary étale neighbourhoods, with `X'` and `S'` affine, such that
> `Γ(X', 𝒪_{X'})` is a projective `Γ(S', 𝒪_{S'})`-module.
>
> This is the case `ℱ = 𝒪_X` of Tag 05ID, as in the source. The flatness hypothesis is converted
> from the morphism to the structure sheaf by
> `AlgebraicGeometry.isFlatOverAt_unit_iff_isFlatAt`, and the conclusion is converted back from
> `Γ(X', g^*𝒪_X)` to `Γ(X', 𝒪_{X'})` by
> `AlgebraicGeometry.Scheme.Modules.pullbackUnitSectionsLinearEquiv`; the finite presentation of
> `𝒪_X` as a module, which Tag 05ID requires of `ℱ`, is
> `AlgebraicGeometry.Scheme.unitModule_isFinitePresentation`.
>
> The hypothesis `hdev` is the hypothesis of this library's Tag 05ID,
> `AlgebraicGeometry.exists_elementaryEtaleNeighborhood_projective_sections`, instantiated at
> the structure sheaf: Proposition 05HR composed with Remark 05I0, carrying the injectivity of the
> maps `α i` of Lemma 05IA. Nothing is assumed beyond it — in particular no Noetherian hypothesis,
> which Tag 05IE does not have. The form without `hdev` is
> `exists_elementaryEtaleNeighborhood_projective_structureSheafSections_of_isFlatAt`.

```lean
theorem exists_elementaryEtaleNeighborhood_projective_structureSheafSections
    {X S : Scheme.{u}} (f : X ⟶ S) (x : X) [LocallyOfFinitePresentation f]
    (hflat : IsFlatAt (LocallyRingedSpace.forgetToSheafedSpace.map f.toLRSHom) x)
    (hdev : IsFlatOverAt (LocallyRingedSpace.forgetToSheafedSpace.map f.toLRSHom)
        (Scheme.unitModule X) x →
      ∃ (V : EtaleNeighborhood S (f x)) (U : EtaleNeighborhood X x) (h : U.scheme ⟶ V.scheme)
        (_ : V.IsElementary) (_ : U.IsElementary)
        (hover : h ≫ V.toBase = U.toBase ≫ f) (_ : h U.point = V.point)
        (_ : IsAffine U.scheme) (_ : IsAffine V.scheme)
        (r : Ideal Γ(V.scheme, ⊤)) (_ : r.IsPrime),
        letI : (Scheme.unitModule X).IsFiniteType :=
          SheafOfModules.instIsFiniteTypeOfIsFinitePresentation (Scheme.unitModule X)
        letI : Algebra Γ(V.scheme, ⊤) Γ(U.scheme, ⊤) := h.appTop.hom.toAlgebra
        letI : Algebra.FinitePresentation Γ(V.scheme, ⊤) Γ(U.scheme, ⊤) :=
          EtaleNeighborhood.algebraFinitePresentation_globalSections f V U h hover
        letI : Module Γ(V.scheme, ⊤)
            Γ((Scheme.Modules.pullback U.toBase).obj (Scheme.unitModule X), ⊤) :=
          Module.compHom _ h.appTop.hom
        letI : Module.Finite Γ(U.scheme, ⊤)
            Γ((Scheme.Modules.pullback U.toBase).obj (Scheme.unitModule X), ⊤) :=
          EtaleNeighborhood.moduleFinite_pullback_globalSections (Scheme.unitModule X) U
        letI : IsScalarTower Γ(V.scheme, ⊤) Γ(U.scheme, ⊤)
            Γ((Scheme.Modules.pullback U.toBase).obj (Scheme.unitModule X), ⊤) :=
          IsScalarTower.of_algebraMap_smul fun _ _ => rfl
        ∃ D : Module.CompleteDevissage Γ(V.scheme, ⊤) Γ(U.scheme, ⊤)
            Γ((Scheme.Modules.pullback U.toBase).obj (Scheme.unitModule X), ⊤) r,
          ∀ i, letI : Module (D.B i) (D.M i) :=
              Module.compHom (D.M i) (D.toLeft i).toRingHom
            Function.Injective (D.alpha i)) :
    ∃ (V : EtaleNeighborhood S (f x)) (U : EtaleNeighborhood X x) (h : U.scheme ⟶ V.scheme),
      V.IsElementary ∧ U.IsElementary ∧
        (h ≫ V.toBase = U.toBase ≫ f) ∧ (h U.point = V.point) ∧
        IsAffine U.scheme ∧ IsAffine V.scheme ∧
        (letI : Module Γ(V.scheme, ⊤) Γ(U.scheme, ⊤) :=
           Module.compHom Γ(U.scheme, ⊤) h.appTop.hom
         Module.Projective Γ(V.scheme, ⊤) Γ(U.scheme, ⊤))
```

**`AlgebraicGeometry.exists_elementaryEtaleNeighborhood_projective_structureSheafSections_of_isFlatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/StructureSheafProjectiveSections.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/StructureSheafProjectiveSections.lean#L266).

> **Stacks Project, Tag 05IE.** Let `f : X ⟶ S` be locally of finite presentation and let
> `x : X`. If `f` is flat at `x` over `S`, then there is a commutative square of pointed schemes
> ```
>   (X, x) ←ᵍ (X', x')
>     ↓          ↓
>   (S, s) ← (S', s')
> ```
> whose horizontal arrows are elementary étale neighbourhoods, with `X'` and `S'` affine, such that
> `Γ(X', 𝒪_{X'})` is a projective `Γ(S', 𝒪_{S'})`-module.
>
> This is the case `ℱ = 𝒪_X` of Tag 05ID, as in the source, whose proof of Tag 05IE is the single
> sentence "This is a special case of Proposition 05ID". The specialisation needs the three
> identifications of the module docstring: `AlgebraicGeometry.Scheme.unitModule X` is quasi-coherent
> and, by `AlgebraicGeometry.Scheme.unitModule_isFinitePresentation`, of finite presentation, so Tag
> 05ID applies to it; `AlgebraicGeometry.isFlatOverAt_unit_iff_isFlatAt` turns flatness of the
> morphism at `x` into flatness of the structure sheaf over the base at `x`; and
> `AlgebraicGeometry.Scheme.Modules.pullbackUnitSectionsLinearEquiv` identifies `Γ(X', g^*𝒪_X)` with
> `Γ(X', 𝒪_{X'})`, compatibly with the restriction of scalars along
> `Γ(S', 𝒪_{S'}) ⟶ Γ(X', 𝒪_{X'})` that both sides carry.
>
> Unlike
> `AlgebraicGeometry.exists_elementaryEtaleNeighborhood_projective_structureSheafSections`, this
> carries no hypothesis beyond the source's: the unconditional form of Tag 05ID,
> `AlgebraicGeometry.exists_elementaryEtaleNeighborhood_projective_sections_of_isFlatOverAt`, is
> used in place of the conditional
> `AlgebraicGeometry.exists_elementaryEtaleNeighborhood_projective_sections`, so there is nothing
> left to assume.

```lean
theorem exists_elementaryEtaleNeighborhood_projective_structureSheafSections_of_isFlatAt
    {X S : Scheme.{u}} (f : X ⟶ S) (x : X) [LocallyOfFinitePresentation f]
    (hflat : IsFlatAt f.toLRSHom.toShHom x) :
    ∃ (V : EtaleNeighborhood S (f x)) (U : EtaleNeighborhood X x) (h : U.scheme ⟶ V.scheme),
      V.IsElementary ∧ U.IsElementary ∧
        (h ≫ V.toBase = U.toBase ≫ f) ∧ (h U.point = V.point) ∧
        IsAffine U.scheme ∧ IsAffine V.scheme ∧
        (letI : Module Γ(V.scheme, ⊤) Γ(U.scheme, ⊤) :=
           Module.compHom Γ(U.scheme, ⊤) h.appTop.hom
         Module.Projective Γ(V.scheme, ⊤) Γ(U.scheme, ⊤))
```

## Tag 05KX, a lemma

[Tag 05KX](https://stacks.math.columbia.edu/tag/05KX) in the Stacks Project.

**`AlgebraicGeometry.exists_elementaryEtaleNeighborhood_projective_structureSheafSections_along_fibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/StructureSheafProjectiveSectionsAlongFibre.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/StructureSheafProjectiveSectionsAlongFibre.lean#L102).

> **Stacks Project, Tag 05KX.** Let `f : X ⟶ S` be of finite presentation and let `s : S` be a
> point at which `X` is flat over `S` at every point of the fibre `X_s`. Then there are an
> elementary étale neighbourhood `(S', s') ⟶ (S, s)` and a commutative square
> ```
>   X  ←ᵍ  X'
>   ↓      ↓
>   S  ←   S'
> ```
> with `g` étale, `X_s ⊆ g(X')`, with `X'` and `S'` affine, and with `Γ(X', 𝒪_{X'})` a projective
> `Γ(S', 𝒪_{S'})`-module.
>
> This is the case `ℱ = 𝒪_X` of Tag 05KW, as in the source. The flatness hypothesis is converted
> from the morphism to the structure sheaf by
> `AlgebraicGeometry.isFlatOverAt_unit_iff_isFlatAt`, and the conclusion is converted back from
> `Γ(X', g^*𝒪_X)` to `Γ(X', 𝒪_{X'})` by
> `AlgebraicGeometry.Scheme.Modules.pullbackUnitSectionsLinearEquiv`; the finite presentation of
> `𝒪_X` as a module, which Tag 05KW requires of `ℱ`, is
> `AlgebraicGeometry.Scheme.unitModule_isFinitePresentation`. Tag 05KW enters as
> `AlgebraicGeometry.exists_elementaryEtaleNeighborhood_projective_sections_along_fibre`, which is
> unconditional, so nothing is assumed here beyond the source's hypotheses.

```lean
theorem exists_elementaryEtaleNeighborhood_projective_structureSheafSections_along_fibre
    {X S : Scheme.{u}} (f : X ⟶ S) (s : S) (hf : FinitePresentation f)
    (hflat : ∀ x : f.fiber s, IsFlatAt f.toLRSHom.toShHom (f.fiberι s x)) :
    ∃ (U : EtaleNeighborhood S s) (X' : Scheme.{u})
      (h : X' ⟶ U.scheme) (g : X' ⟶ X),
      U.IsElementary ∧ IsAffine U.scheme ∧ IsAffine X' ∧ Etale g ∧
      g ≫ f = h ≫ U.toBase ∧
      f ⁻¹' {s} ⊆ Set.range g ∧
      (letI : Module Γ(U.scheme, ⊤) Γ(X', ⊤) := Module.compHom Γ(X', ⊤) h.appTop.hom
       Module.Projective Γ(U.scheme, ⊤) Γ(X', ⊤))
```

## Tag 05KY, a lemma

[Tag 05KY](https://stacks.math.columbia.edu/tag/05KY) in the Stacks Project.

**`AlgebraicGeometry.exists_etale_neighborhood_with_free_globalSections_of_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/FreeSectionsFromFiniteTypeFlatness.lean, line 652](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/FreeSectionsFromFiniteTypeFlatness.lean#L652).

> **Stacks Project, Tag 05KY.** Let `f : X ⟶ S` be locally of finite presentation, let `F` be a
> quasi-coherent `𝒪_X`-module of finite type and let `x ∈ X` be a point at which `F` is flat over
> `S`. Then there is an elementary étale neighbourhood `(S', s') ⟶ (S, s)` of the image `s` of `x`
> and a commutative diagram of pointed schemes
> ```
>   (X, x) ← (X', x')
>     ↓         ↓
>   (S, s) ← Spec 𝒪_{S', s'}
> ```
> such that `X' ⟶ X ×_S Spec 𝒪_{S', s'}` is étale, `κ(x) = κ(x')`, `X'` is affine and of finite
> presentation over `𝒪_{S', s'}`, `g^*F` is of finite presentation, and `Γ(X', g^*F)` is a free
> `𝒪_{S', s'}`-module.
>
> The two inputs are Tag 05ID,
> `AlgebraicGeometry.exists_elementaryEtaleNeighborhood_projective_sections_of_isFlatOverAt`, and
> Tag 05I5, `AlgebraicGeometry.existsElementaryEtaleNeighborhoodFinitePresentationFlatOver`.

```lean
theorem exists_etale_neighborhood_with_free_globalSections_of_isFiniteType
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFinitePresentation f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (x : X) (hflat : IsFlatOverAt f.toLRSHom.toShHom F x) :
    ∃ (U : EtaleNeighborhood S (f x)) (_ : U.IsElementary)
      (X' : Scheme.{u}) (x' : X')
      (g : X' ⟶ X)
      (q : X' ⟶ Spec (.of (U.scheme.presheaf.stalk U.point)))
      (_ : g x' = x)
      (_ : q x' = IsLocalRing.closedPoint (U.scheme.presheaf.stalk U.point))
      (hcomm : g ≫ f = q ≫ U.scheme.fromSpecStalk U.point ≫ U.toBase)
      (_ : Etale (pullback.lift g q hcomm))
      (_ : IsIso (g.residueFieldMap x'))
      (_ : IsAffine X')
      (_ : FinitePresentation q)
      (_ : ((Scheme.Modules.pullback g).obj F).IsFinitePresentation),
      letI : Module (U.scheme.presheaf.stalk U.point)
          Γ((Scheme.Modules.pullback g).obj F, ⊤) :=
        Module.compHom _
          ((Scheme.ΓSpecIso (.of (U.scheme.presheaf.stalk U.point))).inv ≫ q.appTop).hom
      Module.Free (U.scheme.presheaf.stalk U.point)
        Γ((Scheme.Modules.pullback g).obj F, ⊤)
```

## Tag 05KZ, a lemma

[Tag 05KZ](https://stacks.math.columbia.edu/tag/05KZ) in the Stacks Project.

**`AlgebraicGeometry.exists_etale_neighborhood_with_free_globalSections_of_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/FreeSectionsFiniteType.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/FreeSectionsFiniteType.lean#L217).

> **Stacks Project, Tag 05KZ.** Let `f : X ⟶ S` be locally of finite type, let `F` be a
> quasi-coherent `𝒪_X`-module of finite type and let `x : X` be a point at which `F` is flat over
> `S`. Then there is an elementary étale neighbourhood `(S', s') ⟶ (S, s)` of the image `s` of `x`
> and a commutative diagram of pointed schemes
> ```
>   (X, x) ← (X', x')
>     ↓         ↓
>   (S, s) ← Spec 𝒪_{S', s'}
> ```
> such that `X' ⟶ X ×_S Spec 𝒪_{S', s'}` is étale, `κ(x) = κ(x')`, `X'` is affine, and
> `Γ(X', g^*F)` is a free `𝒪_{S', s'}`-module.
>
> This is Tag 05KY with the finite-presentation hypothesis on `f` weakened to finite type, by the
> source's embedding into affine space: an affine neighbourhood `V` of `x` is a closed subscheme
> `i : V ⟶ A` of an affine space `A` over an affine open of `S`, with `A ⟶ S` locally of finite
> presentation, and Tag 05KY applies to `A ⟶ S`, to the direct image `i_*(F|_V)` and to the point
> `i x`. The chart `Y ⟶ A` it returns is pulled back to `X' = V ×_A Y`. The embedding is
> `AlgebraicGeometry.exists_closedImmersion_affineSpace_of_locallyOfFiniteType`, the flatness
> transfer across `i` is `AlgebraicGeometry.isFlatOverAt_pushforward_finite_iff`, and the
> comparison of sections is `AlgebraicGeometry.affinePushforwardBaseChangeIso`.

```lean
theorem exists_etale_neighborhood_with_free_globalSections_of_locallyOfFiniteType
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (x : X) (hflat : IsFlatOverAt f.toLRSHom.toShHom F x) :
    ∃ (U : EtaleNeighborhood S (f x)) (_ : U.IsElementary)
      (X' : Scheme.{u}) (x' : X')
      (g : X' ⟶ X)
      (q : X' ⟶ Spec (.of (U.scheme.presheaf.stalk U.point)))
      (_ : g x' = x)
      (_ : q x' = IsLocalRing.closedPoint (U.scheme.presheaf.stalk U.point))
      (hcomm : g ≫ f = q ≫ U.scheme.fromSpecStalk U.point ≫ U.toBase)
      (_ : Etale (pullback.lift g q hcomm))
      (_ : IsIso (g.residueFieldMap x'))
      (_ : IsAffine X'),
      letI : Module (U.scheme.presheaf.stalk U.point)
          Γ((Scheme.Modules.pullback g).obj F, ⊤) :=
        Module.compHom _
          ((Scheme.ΓSpecIso (.of (U.scheme.presheaf.stalk U.point))).inv ≫ q.appTop).hom
      Module.Free (U.scheme.presheaf.stalk U.point)
        Γ((Scheme.Modules.pullback g).obj F, ⊤)
```

## Tag 05L0, a lemma

[Tag 05L0](https://stacks.math.columbia.edu/tag/05L0) in the Stacks Project.

**`AlgebraicGeometry.exists_elementaryEtaleNeighborhood_free_sections_along_fibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/FreeSectionsAlongFibre.lean, line 902](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/FreeSectionsAlongFibre.lean#L902).

> **Stacks Project, Tag 05L0.** Let `f : X ⟶ S` be of finite presentation, let `F` be a
> quasi-coherent `𝒪_X`-module of finite type and let `s : S` be such that `F` is flat over `S` at
> every point of the fibre `X_s`. Then there are an elementary étale neighbourhood
> `(S', s') ⟶ (S, s)` and a commutative diagram
> ```
>   X  ←ᵍ  X'
>   ↓      ↓
>   S  ←  Spec 𝒪_{S', s'}
> ```
> such that `X' ⟶ X ×_S Spec 𝒪_{S', s'}` is étale, `X_s = g((X')_{s'})`, `X'` is affine and of
> finite presentation over `𝒪_{S', s'}`, `g^*F` is of finite presentation, and `Γ(X', g^*F)` is a
> free `𝒪_{S', s'}`-module.
>
> The inputs are Tag 05KY,
> `AlgebraicGeometry.exists_etale_neighborhood_with_free_globalSections_of_isFiniteType`, applied at
> every point of the fibre, and Tag 057B, which makes the elementary étale neighbourhoods of
> `(S, s)` cofiltered so that the finitely many neighbourhoods surviving the quasi-compactness of
> the fibre are dominated by one of them.

```lean
theorem exists_elementaryEtaleNeighborhood_free_sections_along_fibre
    {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) (hfp : FinitePresentation f)
    [F.IsQuasicoherent] [F.IsFiniteType] (s : S)
    (hflat : ∀ x : f.fiber s, IsFlatOverAt f.toLRSHom.toShHom F (f.fiberι s x)) :
    ∃ (U : EtaleNeighborhood S s) (_ : U.IsElementary)
      (X' : Scheme.{u})
      (q : X' ⟶ Spec (.of (U.scheme.presheaf.stalk U.point)))
      (g : X' ⟶ X)
      (hcomm : g ≫ f = q ≫ U.scheme.fromSpecStalk U.point ≫ U.toBase)
      (_ : Etale (pullback.lift g q hcomm))
      (_ : f ⁻¹' {s} = g '' (q ⁻¹' {IsLocalRing.closedPoint _}))
      (_ : IsAffine X')
      (_ : FinitePresentation q)
      (_ : ((Scheme.Modules.pullback g).obj F).IsFinitePresentation),
      letI : Module (U.scheme.presheaf.stalk U.point)
          Γ((Scheme.Modules.pullback g).obj F, ⊤) :=
        Module.compHom _
          ((Scheme.ΓSpecIso (.of (U.scheme.presheaf.stalk U.point))).inv ≫ q.appTop).hom
      Module.Free (U.scheme.presheaf.stalk U.point)
        Γ((Scheme.Modules.pullback g).obj F, ⊤)
```

## Tag 05L1, a lemma

[Tag 05L1](https://stacks.math.columbia.edu/tag/05L1) in the Stacks Project.

**`AlgebraicGeometry.exists_elementaryEtaleNeighborhood_free_sections_along_fibre_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/FreeSectionsAlongFibre.lean, line 1031](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/FreeSectionsAlongFibre.lean#L1031).

> **Stacks Project, Tag 05L1.** Let `f : X ⟶ S` be of finite type, let `F` be a quasi-coherent
> `𝒪_X`-module of finite type and let `s : S` be such that `F` is flat over `S` at every point of
> the fibre `X_s`. Then there are an elementary étale neighbourhood `(S', s') ⟶ (S, s)` and a
> commutative diagram
> ```
>   X  ←ᵍ  X'
>   ↓      ↓
>   S  ←  Spec 𝒪_{S', s'}
> ```
> such that `X' ⟶ X ×_S Spec 𝒪_{S', s'}` is étale, `X_s = g((X')_{s'})`, `X'` is affine, and
> `Γ(X', g^*F)` is a free `𝒪_{S', s'}`-module.
>
> This differs from Tag 05L0 only in assuming `f` of finite type rather than of finite
> presentation, the input at each point of the fibre being Tag 05KZ,
> `AlgebraicGeometry.exists_etale_neighborhood_with_free_globalSections_of_locallyOfFiniteType`,
> in place of Tag 05KY; correspondingly the two finite-presentation clauses are dropped from the
> conclusion.

```lean
theorem exists_elementaryEtaleNeighborhood_free_sections_along_fibre_of_finiteType
    {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules)
    [LocallyOfFiniteType f] [QuasiCompact f]
    [F.IsQuasicoherent] [F.IsFiniteType] (s : S)
    (hflat : ∀ x : f.fiber s, IsFlatOverAt f.toLRSHom.toShHom F (f.fiberι s x)) :
    ∃ (U : EtaleNeighborhood S s) (_ : U.IsElementary)
      (X' : Scheme.{u})
      (q : X' ⟶ Spec (.of (U.scheme.presheaf.stalk U.point)))
      (g : X' ⟶ X)
      (hcomm : g ≫ f = q ≫ U.scheme.fromSpecStalk U.point ≫ U.toBase)
      (_ : Etale (pullback.lift g q hcomm))
      (_ : f ⁻¹' {s} = g '' (q ⁻¹' {IsLocalRing.closedPoint _}))
      (_ : IsAffine X'),
      letI : Module (U.scheme.presheaf.stalk U.point)
          Γ((Scheme.Modules.pullback g).obj F, ⊤) :=
        Module.compHom _
          ((Scheme.ΓSpecIso (.of (U.scheme.presheaf.stalk U.point))).inv ≫ q.appTop).hom
      Module.Free (U.scheme.presheaf.stalk U.point)
        Γ((Scheme.Modules.pullback g).obj F, ⊤)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.12, Tag 05I9](https://stacks.math.columbia.edu/tag/05I9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
