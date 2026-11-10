---
declaration: section
origin: cited
lean: ModuleCat.subsingleton_ext_of_lt_ideal_depth, Module.subsingleton_ext_of_lt_depth, Stacks.LocalCohomology.depth_eq_sInf_nontrivial_localCohomologyWithSupportIn, Stacks.LocalCohomology.depth_eq_sInf_nontrivial_ext_and_localCohomology_and_subsingleton_ext, Module.depth_eq_sInf_nontrivial_ext, Module.min_depth_le_depth_of_exact, Module.depth_quotSMulTop_succ_eq_depth_and_exists_isRegular_append, Dualizing.supportDim_quotient_add_depth_eq_supportDim
statement: formalized
proof: formalized
---

# 47.11 Depth

Section 47.11 of the Stacks Project, [Tag 0AVY](https://stacks.math.columbia.edu/tag/0AVY). 6 tags here are carried by 15 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AVZ, a lemma

[Tag 0AVZ](https://stacks.math.columbia.edu/tag/0AVZ) in the Stacks Project.

**`ModuleCat.subsingleton_ext_of_lt_ideal_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DepthLemmas/Ext.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DepthLemmas/Ext.lean#L131). The attribute's comment: “Ext vanishing below depth for modules annihilated by an ideal power”. References: EGA 0 (16.4.4), “Ext^i(k”; SGA 2 III (2.2), “Clause (a), special case”; SGA 2 III (2.4), “(4)⇒(2)”; SGA 2 III (2.8), “Ext^i(k”; SGA 2 IV (5.3), “Ext^i_A(k, special case”.

> `Ext^i_R(N, M)` vanishes below the `I`-depth of `M` for **every** finite module `N`
> annihilated by a power of `I`, not just for `N = R ⧸ I`: a power of `I` annihilating `N` forces
> the support of `N` into `V(I)`, and Rees' theorem turns the vanishing of `Ext^j_R(R/I, M)` below
> the depth into an `M`-regular sequence in `I` long enough to kill `Ext^i_R(N, M)`.

```lean
theorem ModuleCat.subsingleton_ext_of_lt_ideal_depth [IsNoetherianRing R] [Small.{v} R]
    (I : Ideal R) (M N : ModuleCat.{v} R) [Module.Finite R M] [Module.Finite R N]
    (hIM : I • (⊤ : Submodule R M) ≠ ⊤) {k : ℕ} (hk : I ^ k ≤ Module.annihilator R N) {i : ℕ}
    (hi : (i : ℕ∞) < Module.depth R I M) :
    Subsingleton (Ext N M i)
```

**`Module.subsingleton_ext_of_lt_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/DepthVanishing/DepthEqLocalCohomology.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/DepthVanishing/DepthEqLocalCohomology.lean#L79). The attribute's comment: “Ext vanishing below depth for modules annihilated by an ideal power”. References: SGA 2 III (2.2), “(a), Noetherian f.g.”; SGA 2 IV (5.3), “Ext^i(M,A)=0 for i&lt;n”; SGA 2 III (3.3), “affine (iv)⇒(v)”.

> Ext from a finite module annihilated by a power of `I` vanishes below the `I`-depth.

```lean
theorem subsingleton_ext_of_lt_depth
    (R : Type u) [CommRing R] [IsNoetherianRing R] [Small.{v} R]
    (I : Ideal R) (M N : ModuleCat.{v} R)
    [Module.Finite R M] [Module.Finite R N]
    (hIM : I • (⊤ : Submodule R M) ≠ ⊤)
    (hN : ∃ n : ℕ, I ^ n ≤ Module.annihilator R N)
    (i : ℕ) (hi : (i : ℕ∞) < Module.depth R I M) :
    Subsingleton (Ext N M i)
```

**`Stacks.LocalCohomology.depth_eq_sInf_nontrivial_localCohomologyWithSupportIn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/DepthVanishing/DepthEqLocalCohomology.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/DepthVanishing/DepthEqLocalCohomology.lean#L417). The attribute's comment: “equality of depth and the first nonzero local-cohomology degree”.

> Depth is the first degree with nonzero local cohomology supported on `V(I)`.

```lean
theorem depth_eq_sInf_nontrivial_localCohomologyWithSupportIn
    (R : Type u) [CommRing R] [IsNoetherianRing R]
    (I : Ideal R) (M : ModuleCat.{max u v} R) [Module.Finite R M]
    (hIM : I • (⊤ : Submodule R M) ≠ ⊤) :
    Module.depth R I M =
      sInf {n : ℕ∞ | ∃ i : ℕ, n = (i : ℕ∞) ∧
      Nontrivial
          (localCohomologyWithSupportIn
            R (PrimeSpectrum.zeroLocus (I : Set R))
              ((DerivedCategory.singleFunctor (ModuleCat.{max u v} R) 0).obj M)
              (i : ℤ))}
```

**`Stacks.LocalCohomology.depth_eq_sInf_nontrivial_ext_and_localCohomology_and_subsingleton_ext`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/DepthVanishing/DepthEqLocalCohomology.lean, line 576](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/DepthVanishing/DepthEqLocalCohomology.lean#L576). The attribute's comment: “the three-way equality and the moreover clause conjoined, with the local cohomology of the third quantity in the RΓ_{V(I)} model”. References: SGA 2 III (2.3), “special case”; SGA 2 III (2.4), “(2)⇔(4)”; SGA 2 IV (5.3), “Ext^i_A(k, special case”; SGA 2 VII (1.2), “(i) ⇔ (iii)”.

> Let `R` be a Noetherian ring, `I ⊆ R` an ideal and `M` a finite
> `R`-module with `IM ≠ M`. Then the three integers of the source are equal — `depth_I(M)`, the
> least `i` with `Ext^i_R(R/I, M) ≠ 0`, and the least `i` with `H^i_{V(I)}(M) ≠ 0`, each of the
> last two read as an infimum in `ℕ∞` — and moreover `Ext^i_R(N, M) = 0` for every `i` below
> `depth_I(M)` and every finite `R`-module `N` annihilated by a power of `I`.
>
> The source's `H^i_I(M)`, the cohomology of derived `I`-power torsion, is `H^i_{V(I)}(M)` here:
> the two agree because `R` is Noetherian, by
> `Stacks.LocalCohomology.isIso_compareSectionsWithSupportLocalCohomology_app`
> ([Stacks, Tag 0955]).

```lean
theorem depth_eq_sInf_nontrivial_ext_and_localCohomology_and_subsingleton_ext
    (R : Type u) [CommRing R] [IsNoetherianRing R]
    (I : Ideal R) (M : ModuleCat.{u} R) [Module.Finite R M]
    (hIM : I • (⊤ : Submodule R M) ≠ ⊤) :
    Module.depth R I M =
        sInf {n : ℕ∞ | ∃ i : ℕ, n = (i : ℕ∞) ∧
          Nontrivial (Abelian.Ext (ModuleCat.of R (Shrink.{u} (R ⧸ I))) M i)} ∧
      Module.depth R I M =
        sInf {n : ℕ∞ | ∃ i : ℕ, n = (i : ℕ∞) ∧
          Nontrivial (localCohomologyWithSupportIn R (PrimeSpectrum.zeroLocus (I : Set R))
            ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj M) (i : ℤ))} ∧
      ∀ (N : ModuleCat.{u} R) [Module.Finite R N], (∃ k : ℕ, I ^ k ≤ Module.annihilator R N) →
        ∀ i : ℕ, (i : ℕ∞) < Module.depth R I M → Subsingleton (Abelian.Ext N M i)
```

Declarations registered for the tag:

- [`Module.depth_eq_sInf_nontrivial_ext`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DepthLemmas/Ext.lean#L152), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/Dualizing/LocalCohomologyNoetherian/Depth.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomologyNoetherian/Depth.lean#L197) (StacksFrontier): “equality of depth and the first nonzero Ext degree”.

## Tag 0BUV, a lemma

[Tag 0BUV](https://stacks.math.columbia.edu/tag/0BUV) in the Stacks Project.

Declarations registered for the tag:

- [`Module.min_depth_le_depth_of_exact`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Depth/ShortExact.lean#L279), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/Dualizing/Depth.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Depth.lean#L313) (StacksFrontier): “middle_depth_bound, quotient_depth_bound and submodule_depth_bound: the three conjuncts of this inequality”.

## Tag 0BUW, a lemma

[Tag 0BUW](https://stacks.math.columbia.edu/tag/0BUW) in the Stacks Project.

Declarations registered for the tag:

- [`Module.depth_quotSMulTop_succ_eq_depth_and_exists_isRegular_append`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Depth/Criteria.lean#L612), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/Dualizing/Depth.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Depth.lean#L318) (StacksFrontier).

## Tag 0BUX, a lemma

[Tag 0BUX](https://stacks.math.columbia.edu/tag/0BUX) in the Stacks Project.

**`Dualizing.supportDim_quotient_add_depth_eq_supportDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Depth.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Depth.lean#L187). References: EGA 0 (16.5.9), “r = depth_p(M)”.

> **Stacks Project, Tag 0BUX.** The depth of a finite Cohen--Macaulay module
> along a proper ideal is the drop in the dimension of its support on passing to
> the quotient by that ideal.

```lean
theorem supportDim_quotient_add_depth_eq_supportDim
    {R M : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M] [Module.Finite R M]
    (I : Ideal R) (hI : I ≠ ⊤) (hM : Module.IsCohenMacaulayAtMaximalIdeal R M) :
    Module.supportDim R (M ⧸ I • (⊤ : Submodule R M)) +
        (Module.depth R I M : WithBot ℕ∞) =
      Module.supportDim R M
```

## Tag 0BUY, a lemma

[Tag 0BUY](https://stacks.math.columbia.edu/tag/0BUY) in the Stacks Project.

**`Dualizing.ringKrullDim_fiber_le_depth_add_ringKrullDim_quotient_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Depth.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Depth.lean#L282).

> Let `R → S` be a flat local homomorphism with Noetherian local target. If its closed
> fibre is Cohen--Macaulay, then the depth of `S` along an ideal `I` is at least the difference
> between the dimension of the closed fibre and that of its quotient by `I`.

```lean
theorem ringKrullDim_fiber_le_depth_add_ringKrullDim_quotient_of_flat
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
    [IsNoetherianRing S] [IsLocalRing R] [IsLocalRing S]
    [Module.Flat R S] [IsLocalHom (algebraMap R S)] (I : Ideal S)
    (hCM : Module.IsCohenMacaulayAtMaximalIdeal S
      (S ⧸ Ideal.map (algebraMap R S) (maximalIdeal R))) :
    I = ⊤ ∨
      ringKrullDim (S ⧸ Ideal.map (algebraMap R S) (maximalIdeal R)) ≤
        (Module.depth S I S : WithBot ℕ∞) +
        ringKrullDim
            (S ⧸ (Ideal.map (algebraMap R S) (maximalIdeal R) ⊔ I))
```

## Tag 0AW0, a lemma

[Tag 0AW0](https://stacks.math.columbia.edu/tag/0AW0) in the Stacks Project.

**`Stacks.Duality.supportLocalCohomology_torsion_higher`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DivideByTorsion.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DivideByTorsion.lean#L155). The attribute's comment: “part (2), higher cohomology of the torsion submodule”.

> **Stacks 0AW0, part (2).** Higher local cohomology with support in `V(I)` of torsion
> vanishes: `H^p_Z(M[I^∞]) = 0` for `p > 0`.

```lean
theorem supportLocalCohomology_torsion_higher
    (A : Type u) [CommRing A]
    (I : Ideal A) (hI : I.FG) (M : ModuleCat.{max u v} A)
    (p : ℤ) (hp : 0 < p) :
    IsZero ((supportLocalCohomology.{u, v} A I hI p).obj
      (ModuleCat.of A (Ideal.primaryComponent M I)))
```

**`Stacks.Duality.supportLocalCohomology_quotient_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DivideByTorsion.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DivideByTorsion.lean#L325). The attribute's comment: “part (2), degree zero”.

> **Stacks 0AW0, part (2).** Quotienting by `I`-power torsion kills zeroth local cohomology
> with support in `V(I)`: `H^0_Z(M/M[I^∞]) = 0`.

```lean
theorem supportLocalCohomology_quotient_zero
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
    (M : ModuleCat.{max u v} A) :
    IsZero ((supportLocalCohomology.{u, v} A I hI 0).obj
      (ModuleCat.of A (M ⧸ Ideal.primaryComponent M I)))
```

**`Stacks.Duality.idealLocalCohomology_zero_iso_torsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TorsionQuotient.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/TorsionQuotient.lean#L298). The attribute's comment: “H^0_I is the torsion submodule”.

> **Stacks 0AW0.** The zeroth local cohomology `H^0_I(M)` of `M` for the `I`-power torsion
> theory is the `I`-power-torsion submodule `M[I^∞]` of `M`, by an isomorphism compatible with
> the canonical map of `H^0_I(M)` into `M`.

```lean
theorem idealLocalCohomology_zero_iso_torsion
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
    (M : ModuleCat.{max u v} A) :
    ∃ e : (idealLocalCohomology.{u, v} A I hI 0).obj M ≅
        ModuleCat.of A (Ideal.primaryComponent M I),
      e.hom ≫ ModuleCat.ofHom (Submodule.subtype (Ideal.primaryComponent M I)) =
        idealLocalCohomologyToModule.{u, v} A I hI M
```

**`Stacks.Duality.idealLocalCohomology_quotient_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TorsionQuotient.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/TorsionQuotient.lean#L325). The attribute's comment: “part (1), degree zero”.

> **Stacks 0AW0, part (1).** Quotienting by the `I`-power-torsion submodule kills the zeroth
> local cohomology for the `I`-power torsion theory: `H^0_I(M/M[I^∞]) = 0`.

```lean
theorem idealLocalCohomology_quotient_zero
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
    (M : ModuleCat.{max u v} A) :
    IsZero ((idealLocalCohomology.{u, v} A I hI 0).obj
      (ModuleCat.of A (M ⧸ Ideal.primaryComponent M I)))
```

**`Stacks.Duality.idealLocalCohomology_torsion_higher`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TorsionQuotient.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/TorsionQuotient.lean#L344). The attribute's comment: “part (1), higher cohomology of the torsion submodule”.

> **Stacks 0AW0, part (1).** Over a Noetherian ring the higher local cohomology of the
> `I`-power-torsion submodule vanishes for the `I`-power torsion theory:
> `H^p_I(M[I^∞]) = 0` for `p > 0`.
>
> The source states this for an arbitrary ring. The Noetherian hypothesis added here cannot be
> removed: for a finitely generated ideal of a non-Noetherian ring the assertion is false, by
> part (3) of [Stacks, Tag 0A6P]. See the module docstring.

```lean
theorem idealLocalCohomology_torsion_higher
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (I : Ideal A) (hI : I.FG) (M : ModuleCat.{max u v} A)
    (p : ℤ) (hp : 0 < p) :
    IsZero ((idealLocalCohomology.{u, v} A I hI p).obj
      (ModuleCat.of A (Ideal.primaryComponent M I)))
```

**`Stacks.Duality.idealLocalCohomology_quotient_map_higher`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TorsionQuotient.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/TorsionQuotient.lean#L373). The attribute's comment: “part (1), higher cohomology of the quotient”.

> **Stacks 0AW0, part (1).** Over a Noetherian ring the quotient map `M ⟶ M/M[I^∞]` induces
> an isomorphism `H^p_I(M) ≅ H^p_I(M/M[I^∞])` in every positive degree.
>
> The source states this for an arbitrary ring. The Noetherian hypothesis added here cannot be
> removed: taking an `I`-power-torsion `M`, so that `M/M[I^∞] = 0`, turns the assertion into the
> vanishing of `Stacks.Duality.idealLocalCohomology_torsion_higher`, which part (3) of
> [Stacks, Tag 0A6P] refutes over a non-Noetherian ring. See the module docstring.

```lean
theorem idealLocalCohomology_quotient_map_higher
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (I : Ideal A) (hI : I.FG) (M : ModuleCat.{max u v} A)
    (p : ℤ) (hp : 0 < p) :
    IsIso ((idealLocalCohomology.{u, v} A I hI p).map
      (ModuleCat.ofHom (Ideal.primaryComponent M I).mkQ))
```

**`Stacks.Duality.supportLocalCohomology_quotient_map_higher`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TorsionQuotient.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/TorsionQuotient.lean#L420). The attribute's comment: “part (2), higher cohomology of the quotient”.

> **Stacks 0AW0, part (2).** The quotient map `M ⟶ M/M[I^∞]` induces an isomorphism
> `H^p_Z(M) ≅ H^p_Z(M/M[I^∞])` in every positive degree.

```lean
theorem supportLocalCohomology_quotient_map_higher
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
    (M : ModuleCat.{max u v} A) (p : ℤ) (hp : 0 < p) :
    IsIso ((supportLocalCohomology.{u, v} A I hI p).map
      (ModuleCat.ofHom (Ideal.primaryComponent M I).mkQ))
```

**`Stacks.Duality.idealLocalCohomology_zero_iso_supportLocalCohomology_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TorsionQuotient.lean, line 439](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/TorsionQuotient.lean#L439). The attribute's comment: “H^0_I = H^0_Z”.

> **Stacks 0AW0.** For a finitely generated ideal `I` and `Z = V(I)` the two zeroth local
> cohomology modules agree, `H^0_I(M) = H^0_Z(M)`, compatibly with their canonical maps down
> to `M`; the common value is the `I`-power-torsion submodule `M[I^∞]`.

```lean
theorem idealLocalCohomology_zero_iso_supportLocalCohomology_zero
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
    (M : ModuleCat.{max u v} A) :
    ∃ e : (idealLocalCohomology.{u, v} A I hI 0).obj M ≅
        (supportLocalCohomology.{u, v} A I hI 0).obj M,
      e.hom ≫ supportLocalCohomologyToModule.{u, v} A I hI M =
        idealLocalCohomologyToModule.{u, v} A I hI M
```

**`Stacks.Duality.localCohomology_divide_by_torsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TorsionQuotient.lean, line 472](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/TorsionQuotient.lean#L472). The attribute's comment: “the preamble and both parts conjoined, with the Noetherian hypothesis that the two higher-degree clauses of part (1) require and the source lacks”.

> **Stacks 0AW0, the preamble and both parts.** Let `A` be a ring, let `I ⊆ A` be a finitely
> generated ideal, let `M` be an `A`-module and let `Z = V(I)`. Then `H^0_I(M) = H^0_Z(M)`; the
> common value `N` is the `I`-power-torsion submodule `M[I^∞]`, both identifications being
> compatible with the canonical maps down to `M`; and, writing `M' = M/N`,
>
> 1. `H^0_I(M') = 0`, `H^p_I(M) = H^p_I(M')` and `H^p_I(N) = 0` for all `p > 0`;
> 2. `H^0_Z(M') = 0`, `H^p_Z(M) = H^p_Z(M')` and `H^p_Z(N) = 0` for all `p > 0`.
>
> The two higher-degree clauses of part (1) carry the hypothesis that `A` is Noetherian, which
> the source does not have, so this conjunction carries it too. That hypothesis cannot be dropped:
> part (3) of [Stacks, Tag 0A6P] refutes those two clauses for a finitely generated ideal of a
> non-Noetherian ring, by the argument in the module docstring. Everything else here — the
> preamble and the whole of part (2) — holds over an arbitrary ring, and is stated that way by the
> eight declarations this conjoins, each of which carries the tag for its own clause; they are
> listed in the module docstring and in that of
> `StacksFrontier.AlgebraicGeometry.Duality.DivideByTorsion`.

```lean
theorem localCohomology_divide_by_torsion
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A) (hI : I.FG)
    (M : ModuleCat.{max u v} A) :
    (∃ e : (idealLocalCohomology.{u, v} A I hI 0).obj M ≅
        (supportLocalCohomology.{u, v} A I hI 0).obj M,
      e.hom ≫ supportLocalCohomologyToModule.{u, v} A I hI M =
        idealLocalCohomologyToModule.{u, v} A I hI M) ∧
    (∃ e : (idealLocalCohomology.{u, v} A I hI 0).obj M ≅
        ModuleCat.of A (Ideal.primaryComponent M I),
      e.hom ≫ ModuleCat.ofHom (Submodule.subtype (Ideal.primaryComponent M I)) =
        idealLocalCohomologyToModule.{u, v} A I hI M) ∧
    (IsZero ((idealLocalCohomology.{u, v} A I hI 0).obj
          (ModuleCat.of A (M ⧸ Ideal.primaryComponent M I))) ∧
        (∀ p : ℤ, 0 < p → IsIso ((idealLocalCohomology.{u, v} A I hI p).map
          (ModuleCat.ofHom (Ideal.primaryComponent M I).mkQ))) ∧
        ∀ p : ℤ, 0 < p → IsZero ((idealLocalCohomology.{u, v} A I hI p).obj
          (ModuleCat.of A (Ideal.primaryComponent M I)))) ∧
      (IsZero ((supportLocalCohomology.{u, v} A I hI 0).obj
          (ModuleCat.of A (M ⧸ Ideal.primaryComponent M I))) ∧
        (∀ p : ℤ, 0 < p → IsIso ((supportLocalCohomology.{u, v} A I hI p).map
          (ModuleCat.ofHom (Ideal.primaryComponent M I).mkQ))) ∧
        ∀ p : ℤ, 0 < p → IsZero ((supportLocalCohomology.{u, v} A I hI p).obj
          (ModuleCat.of A (Ideal.primaryComponent M I))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.11, Tag 0AVY](https://stacks.math.columbia.edu/tag/0AVY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
