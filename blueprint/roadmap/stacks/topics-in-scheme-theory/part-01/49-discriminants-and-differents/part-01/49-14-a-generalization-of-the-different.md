---
declaration: section
origin: cited
lean: Stacks.Discriminant.mapsNonZeroDivisors_of_fractionBaseChangeFlat, Stacks.Discriminant.flatAtAssociatedPrimes_of_flatAtPrimesOverAssociatedPrimes, Stacks.Discriminant.flatAtPrimesOverAssociatedPrimes_of_fractionBaseChangeFlat, Stacks.Discriminant.mapsNonZeroDivisors_of_flatAtAssociatedPrimes, Stacks.Discriminant.fractionBaseChangeFlat_iff_flatAtPrimesOverAssociatedPrimes, Stacks.Discriminant.associatedPoints_subset_of_preimage_subset, Stacks.Discriminant.GeneralizedTraceSection.sect_eq, Stacks.Discriminant.generalizedDifferent
statement: formalized
proof: formalized
---

# 49.14 A generalization of the different

Section 49.14 of the Stacks Project, [Tag 0BWK](https://stacks.math.columbia.edu/tag/0BWK). 4 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BWL, a lemma

[Tag 0BWL](https://stacks.math.columbia.edu/tag/0BWL) in the Stacks Project.

**`Stacks.Discriminant.mapsNonZeroDivisors_of_fractionBaseChangeFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/Basic.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/Basic.lean#L149). The attribute's comment: “(2) implies (1)”.

> Condition (2) implies condition (1).

```lean
theorem mapsNonZeroDivisors_of_fractionBaseChangeFlat
    (h : FractionBaseChangeFlat A B) : MapsNonZeroDivisors A B
```

**`Stacks.Discriminant.flatAtAssociatedPrimes_of_flatAtPrimesOverAssociatedPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/Basic.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/Basic.lean#L154). The attribute's comment: “(4) implies (3)”.

> Condition (4) implies condition (3).

```lean
theorem flatAtAssociatedPrimes_of_flatAtPrimesOverAssociatedPrimes
    (h : FlatAtPrimesOverAssociatedPrimes A B) : FlatAtAssociatedPrimes A B
```

**`Stacks.Discriminant.flatAtPrimesOverAssociatedPrimes_of_fractionBaseChangeFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/Basic.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/Basic.lean#L159). The attribute's comment: “(2) implies (4)”.

> Condition (2) implies condition (4).

```lean
theorem flatAtPrimesOverAssociatedPrimes_of_fractionBaseChangeFlat
    (h : FractionBaseChangeFlat A B) : FlatAtPrimesOverAssociatedPrimes A B
```

**`Stacks.Discriminant.mapsNonZeroDivisors_of_flatAtAssociatedPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/Basic.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/Basic.lean#L170). The attribute's comment: “(3) implies (1)”.

> Condition (3) implies condition (1) for Noetherian rings.

```lean
theorem mapsNonZeroDivisors_of_flatAtAssociatedPrimes
    [IsNoetherianRing A] [IsNoetherianRing B]
    (h : FlatAtAssociatedPrimes A B) : MapsNonZeroDivisors A B
```

**`Stacks.Discriminant.fractionBaseChangeFlat_iff_flatAtPrimesOverAssociatedPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/Basic.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/Basic.lean#L218). The attribute's comment: “equivalence under going up”.

> If `A → B` satisfies going up, conditions (2) and (4) are equivalent.

```lean
theorem fractionBaseChangeFlat_iff_flatAtPrimesOverAssociatedPrimes
    [IsNoetherianRing A] [IsNoetherianRing B] [Algebra.HasGoingUp A B] :
    FractionBaseChangeFlat A B ↔ FlatAtPrimesOverAssociatedPrimes A B
```

## Tag 0BWM, a remark

[Tag 0BWM](https://stacks.math.columbia.edu/tag/0BWM) in the Stacks Project.

**`Stacks.Discriminant.associatedPoints_subset_of_preimage_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/TheDifferent.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/TheDifferent.lean#L123). The attribute's comment: “the associated points of the relative dualizing module lie in the flat locus”.

> **[Stacks, Tag 0BWM], condition (1).** An open of the source containing the inverse image of
> the associated points of the base contains the associated points of the relative dualizing
> module.

```lean
theorem associatedPoints_subset_of_preimage_subset (ω : RelativeDualizingModuleData f)
    (V : Y.Opens)
    (hV : f.base ⁻¹' Stacks.Divisors.schemeAssociatedPoints X ⊆ (V : Set Y)) :
    Stacks.Divisors.associatedPoints ω.sheaf ⊆ (V : Set Y)
```

**`Stacks.Discriminant.GeneralizedTraceSection.sect_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/TheDifferent.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/TheDifferent.lean#L239). The attribute's comment: “uniqueness of the extension of the trace element”.

> **[Stacks, Tag 0BWM], uniqueness of the extension.** In the situation of Tag 0BWM a global
> section of the relative dualizing module extending the trace element `τ_{V/X}` is unique.

```lean
theorem sect_eq (S : GeneralizedDifferentSituation f) (ω : RelativeDualizingModuleData f)
    (τ₁ τ₂ : GeneralizedTraceSection ω) : τ₁.sect = τ₂.sect
```

**`Stacks.Discriminant.generalizedDifferent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/TheDifferent.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/TheDifferent.lean#L265). The attribute's comment: “the generalized different”.

> **[Stacks, Tag 0BWM].** The *generalized different* `𝔇_f` of a quasi-finite morphism of
> locally Noetherian schemes which is flat near the associated points: the annihilator of the
> cokernel of the map `𝒪_Y → ω_{Y/X}` given by the extension `τ` of the trace element
> `τ_{V/X}`.

```lean
def generalizedDifferent (ω : RelativeDualizingModuleData f) (τ : GeneralizedTraceSection ω) :
    (SheafOfModules.unit (structureSheafRing Y.toRingedSpace)).Submodule
```

## Tag 0BWN, a lemma

[Tag 0BWN](https://stacks.math.columbia.edu/tag/0BWN) in the Stacks Project.

**`Stacks.Discriminant.generalizedDifferent_spec_eq_tilde_dedekindDifferent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/DedekindGeneralization.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/DedekindGeneralization.lean#L113). The attribute's comment: “the generalized different of `Spec B → Spec A` is defined iff `1 ∈ L_{B/A}` (e.g. for normal `A`), and then `𝔇_{B/A}` is an ideal of `B` and `𝔇_f = (𝔇_{B/A})~`”.

> **[Stacks, Tag 0BWN].** Assume the Dedekind different is defined for `A → B`, and set
> `X = Spec(A)`, `Y = Spec(B)` and `f : Y → X`.  Then, for the relative dualizing module `ω` of
> `f`, the generalization of the different (Remark 0BWM) applies to `f` — an open of `Y` over which
> `f` is flat contains `Ass(𝒪_Y)` and `f⁻¹(Ass(𝒪_X))`, and the trace element of the flat locus
> comes from a global section of `ω_{Y/X}` — if and only if `1 ∈ L_{B/A}`; this is the case for
> instance if `A` is normal.  In this case the Dedekind different `𝔇_{B/A}` is an ideal of `B`,
> and the generalized different `𝔇_f` is the coherent sheaf of ideals `(𝔇_{B/A})~` on `Y`.

```lean
theorem generalizedDifferent_spec_eq_tilde_dedekindDifferent {A B : Type u} [CommRing A]
    [CommRing B] [Algebra A B] (setup : DedekindDifferentSetup A B) :
    letI : IsNoetherianRing A := setup.isNoetherianRing
    letI : Module.Finite A B := setup.finite
    letI : IsNoetherianRing B := IsNoetherianRing.of_finite A B
    letI := locallyQuasiFinite_spec_map (A := A) (B := B)
    ∀ ω : RelativeDualizingModuleData (Spec.map (CommRingCat.ofHom (algebraMap A B))),
      ((Nonempty (GeneralizedDifferentSituation (Spec.map (CommRingCat.ofHom (algebraMap A B)))) ∧
          Nonempty (GeneralizedTraceSection ω)) ↔
        (1 : B ⊗[A] FractionRing A) ∈ setup.complementaryModule) ∧
      (IsNormalRing A → (1 : B ⊗[A] FractionRing A) ∈ setup.complementaryModule) ∧
      ((1 : B ⊗[A] FractionRing A) ∈ setup.complementaryModule →
        setup.dedekindDifferent =
            Submodule.map (Algebra.linearMap B (B ⊗[A] FractionRing A))
              (dedekindDifferentIdeal setup : Submodule B B) ∧
          ∀ τ : GeneralizedTraceSection ω,
            Stacks.SheafOfModules.IsCoherent (generalizedDifferent ω τ).toSheafOfModules ∧
            generalizedDifferent ω τ =
              (Scheme.IdealSheafData.ofIdealTop ((dedekindDifferentIdeal setup).map
                (Scheme.ΓSpecIso (CommRingCat.of B)).inv.hom)).unitSubmodule)
```

## Tag 0BWP, an example

[Tag 0BWP](https://stacks.math.columbia.edu/tag/0BWP) in the Stacks Project.

**`Stacks.Discriminant.NodeExample.one_mem_complementaryModule_iff_natCast_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/ComplementaryModule.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/ComplementaryModule.lean#L179). The attribute's comment: “complementary module criterion”.

> One belongs to the complementary module exactly when the two branch degrees have the same
> image in `k`.  The source states this as `n = m`; what the trace of one, `(nx+my)/(x+y)`, lies
> in `A` for is `(n : k) = (m : k)`.

```lean
theorem one_mem_complementaryModule_iff_natCast_eq
    (n m : ℕ) (hn : IsUnit (n : k)) (hm : IsUnit (m : k))
    (f : nodeRing k →+* targetNodeRing k)
    (hx : f (x k) = u k ^ n) (hy : f (y k) = v k ^ m)
    (hk : ∀ a : k, f (algebraMap k (nodeRing k) a) = algebraMap k (targetNodeRing k) a) :
    letI : Algebra (nodeRing k) (targetNodeRing k) := f.toAlgebra
    ∀ setup : DedekindDifferentSetup (nodeRing k) (targetNodeRing k),
      letI : DedekindDifferentSetup (nodeRing k) (targetNodeRing k) := setup
      ((1 : (targetNodeRing k) ⊗[nodeRing k] FractionRing (nodeRing k)) ∈
        setup.complementaryModule ↔ (n : k) = (m : k))
```

**`Stacks.Discriminant.NodeExample.complementaryModule_eq_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/ComplementaryModule.lean, line 451](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/ComplementaryModule.lean#L451). The attribute's comment: “complementary module equals B”.

> When the branch degrees agree, the complementary module is precisely `B`.

```lean
theorem complementaryModule_eq_range
    (n m : ℕ) (hn : IsUnit (n : k)) (hm : IsUnit (m : k))
    (f : nodeRing k →+* targetNodeRing k)
    (hx : f (x k) = u k ^ n) (hy : f (y k) = v k ^ m)
    (hk : ∀ a : k, f (algebraMap k (nodeRing k) a) = algebraMap k (targetNodeRing k) a)
    (heq : (n : k) = (m : k)) :
    letI : Algebra (nodeRing k) (targetNodeRing k) := f.toAlgebra
    ∀ setup : DedekindDifferentSetup (nodeRing k) (targetNodeRing k),
      letI : DedekindDifferentSetup (nodeRing k) (targetNodeRing k) := setup
      ∀ z, z ∈ setup.complementaryModule ↔
        z ∈ Set.range (algebraMap (targetNodeRing k)
          ((targetNodeRing k) ⊗[nodeRing k] FractionRing (nodeRing k)))
```

**`Stacks.Discriminant.NodeExample.dedekindDifferent_eq_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/ComplementaryModule.lean, line 550](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/ComplementaryModule.lean#L550). The attribute's comment: “unit Dedekind different”.

> In that case the Dedekind different is the unit ideal of `B`.

```lean
theorem dedekindDifferent_eq_range
    (n m : ℕ) (hn : IsUnit (n : k)) (hm : IsUnit (m : k))
    (f : nodeRing k →+* targetNodeRing k)
    (hx : f (x k) = u k ^ n) (hy : f (y k) = v k ^ m)
    (hk : ∀ a : k, f (algebraMap k (nodeRing k) a) = algebraMap k (targetNodeRing k) a)
    (heq : (n : k) = (m : k)) :
    letI : Algebra (nodeRing k) (targetNodeRing k) := f.toAlgebra
    ∀ setup : DedekindDifferentSetup (nodeRing k) (targetNodeRing k),
      letI : DedekindDifferentSetup (nodeRing k) (targetNodeRing k) := setup
      ∀ z, z ∈ setup.dedekindDifferent ↔
        z ∈ Set.range (algebraMap (targetNodeRing k)
          ((targetNodeRing k) ⊗[nodeRing k] FractionRing (nodeRing k)))
```

**`Stacks.Discriminant.NodeExample.exists_dual_trace_iff_natCast_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/ComplementaryModule.lean, line 586](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/ComplementaryModule.lean#L586). The attribute's comment: “definedness of the different, on the chart”.

> **The chartwise form of the definedness of the different of [Stacks, Tag 0BWM].** The trace
> element of the generic fibre comes from a section of the relative dualizing module
> `ω_{B/A} = Hom_A(B, A)` exactly when the two branch degrees have the same image in `k`.

```lean
theorem exists_dual_trace_iff_natCast_eq
    (n m : ℕ) (hn : IsUnit (n : k)) (hm : IsUnit (m : k))
    (f : nodeRing k →+* targetNodeRing k)
    (hx : f (x k) = u k ^ n) (hy : f (y k) = v k ^ m)
    (hk : ∀ a : k, f (algebraMap k (nodeRing k) a) = algebraMap k (targetNodeRing k) a) :
    letI : Algebra (nodeRing k) (targetNodeRing k) := f.toAlgebra
    ∀ setup : DedekindDifferentSetup (nodeRing k) (targetNodeRing k),
      letI : Algebra (FractionRing (nodeRing k))
          ((targetNodeRing k) ⊗[nodeRing k] FractionRing (nodeRing k)) :=
        Algebra.TensorProduct.rightAlgebra
      ((∃ φ : Module.Dual (nodeRing k) (targetNodeRing k), ∀ b : targetNodeRing k,
            algebraMap (nodeRing k) (FractionRing (nodeRing k)) (φ b) =
              setup.trace (algebraMap (targetNodeRing k)
                ((targetNodeRing k) ⊗[nodeRing k] FractionRing (nodeRing k)) b)) ↔
        (n : k) = (m : k))
```

**`Stacks.Discriminant.NodeExample.dedekindDifferentIdeal_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/ComplementaryModule.lean, line 610](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/ComplementaryModule.lean#L610). The attribute's comment: “the different is the unit ideal, on the chart”.

> **The chartwise form of the different of [Stacks, Tag 0BWM] being the unit ideal.** When the
> two branch degrees have the same image in `k`, the Dedekind different ideal of `B` is the unit
> ideal.

```lean
theorem dedekindDifferentIdeal_eq_top
    (n m : ℕ) (hn : IsUnit (n : k)) (hm : IsUnit (m : k))
    (f : nodeRing k →+* targetNodeRing k)
    (hx : f (x k) = u k ^ n) (hy : f (y k) = v k ^ m)
    (hk : ∀ a : k, f (algebraMap k (nodeRing k) a) = algebraMap k (targetNodeRing k) a)
    (heq : (n : k) = (m : k)) :
    letI : Algebra (nodeRing k) (targetNodeRing k) := f.toAlgebra
    ∀ setup : DedekindDifferentSetup (nodeRing k) (targetNodeRing k),
      dedekindDifferentIdeal setup = ⊤
```

**`Stacks.Discriminant.NodeExample.exists_powerMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/FiniteEtale.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/FiniteEtale.lean#L272). The attribute's comment: “power map”.

> The branchwise power map, specified on the two coordinates.

```lean
theorem exists_powerMap (n m : ℕ) (hn : 0 < n) (hm : 0 < m) :
    ∃ f : nodeRing k →+* targetNodeRing k,
      f (x k) = u k ^ n ∧ f (y k) = v k ^ m ∧
        ∀ a : k, f (algebraMap k (nodeRing k) a) = algebraMap k (targetNodeRing k) a
```

**`Stacks.Discriminant.NodeExample.finite_away_node`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/FiniteEtale.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/FiniteEtale.lean#L293). The attribute's comment: “finite localization”.

> The localized branchwise power map is finite.

```lean
theorem finite_away_node
    (n m : ℕ) (hn : IsUnit (n : k)) (hm : IsUnit (m : k))
    (f : nodeRing k →+* targetNodeRing k)
    (hx : f (x k) = u k ^ n) (hy : f (y k) = v k ^ m)
    (hk : ∀ a : k, f (algebraMap k (nodeRing k) a) = algebraMap k (targetNodeRing k) a) :
    letI : Algebra (Localization.Away (x k + y k))
        (Localization.Away (f (x k + y k))) :=
      (IsLocalization.Away.map (Localization.Away (x k + y k))
        (Localization.Away (f (x k + y k))) f (x k + y k)).toAlgebra
    Module.Finite (Localization.Away (x k + y k))
      (Localization.Away (f (x k + y k)))
```

**`Stacks.Discriminant.NodeExample.etale_away_node`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/FiniteEtale.lean, line 535](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/FiniteEtale.lean#L535). The attribute's comment: “étale localization”.

> The localized branchwise power map is étale.

```lean
theorem etale_away_node
    (n m : ℕ) (hn : IsUnit (n : k)) (hm : IsUnit (m : k))
    (f : nodeRing k →+* targetNodeRing k)
    (hx : f (x k) = u k ^ n) (hy : f (y k) = v k ^ m)
    (hk : ∀ a : k, f (algebraMap k (nodeRing k) a) = algebraMap k (targetNodeRing k) a) :
    letI : Algebra (Localization.Away (x k + y k))
        (Localization.Away (f (x k + y k))) :=
      (IsLocalization.Away.map (Localization.Away (x k + y k))
        (Localization.Away (f (x k + y k))) f (x k + y k)).toAlgebra
    Algebra.Etale (Localization.Away (x k + y k))
      (Localization.Away (f (x k + y k)))
```

**`Stacks.Discriminant.NodeExample.exists_dedekindDifferentSetup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/FiniteEtale.lean, line 640](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/FiniteEtale.lean#L640). The attribute's comment: “Dedekind setup”.

> This finite map satisfies the standing hypotheses for its Dedekind different.

```lean
theorem exists_dedekindDifferentSetup
    (n m : ℕ) (hn : IsUnit (n : k)) (hm : IsUnit (m : k))
    (f : nodeRing k →+* targetNodeRing k)
    (hx : f (x k) = u k ^ n) (hy : f (y k) = v k ^ m)
    (hk : ∀ a : k, f (algebraMap k (nodeRing k) a) = algebraMap k (targetNodeRing k) a) :
    letI : Algebra (nodeRing k) (targetNodeRing k) := f.toAlgebra
    Nonempty (DedekindDifferentSetup (nodeRing k) (targetNodeRing k))
```

**`Stacks.Discriminant.NodeExample.powerMap_two_not_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/NotFlatNotUnramified.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/NotFlatNotUnramified.lean#L71). The attribute's comment: “nonflat example”.

> Even with equal branch degrees and unit different, the power map is not flat.

```lean
theorem powerMap_two_not_flat
    (f : nodeRing ℚ →+* targetNodeRing ℚ)
    (hx : f (x ℚ) = u ℚ ^ 2) (hy : f (y ℚ) = v ℚ ^ 2)
    (hk : ∀ a : ℚ, f (algebraMap ℚ (nodeRing ℚ) a) =
      algebraMap ℚ (targetNodeRing ℚ) a) :
    letI : Algebra (nodeRing ℚ) (targetNodeRing ℚ) := f.toAlgebra
    ¬ Module.Flat (nodeRing ℚ) (targetNodeRing ℚ)
```

**`Stacks.Discriminant.NodeExample.powerMap_two_not_formallyUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/NotFlatNotUnramified.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/NotFlatNotUnramified.lean#L135). The attribute's comment: “not unramified example”.

> The same map is not unramified, despite its unit different.

```lean
theorem powerMap_two_not_formallyUnramified
    (f : nodeRing ℚ →+* targetNodeRing ℚ)
    (hx : f (x ℚ) = u ℚ ^ 2) (hy : f (y ℚ) = v ℚ ^ 2)
    (hk : ∀ a : ℚ, f (algebraMap ℚ (nodeRing ℚ) a) =
      algebraMap ℚ (targetNodeRing ℚ) a) :
    ¬ RingHom.FormallyUnramified f
```

**`Stacks.Discriminant.NodeExample.trace_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/TraceValues.lean, line 551](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/TraceValues.lean#L551). The attribute's comment: “trace of one”.

> The trace of one on the generic fibre is `(nx+my)/(x+y)`.

```lean
theorem trace_one
    (n m : ℕ) (hn : IsUnit (n : k)) (hm : IsUnit (m : k))
    (f : nodeRing k →+* targetNodeRing k)
    (hx : f (x k) = u k ^ n) (hy : f (y k) = v k ^ m)
    (hk : ∀ a : k, f (algebraMap k (nodeRing k) a) = algebraMap k (targetNodeRing k) a) :
    letI : Algebra (nodeRing k) (targetNodeRing k) := f.toAlgebra
    ∀ setup : DedekindDifferentSetup (nodeRing k) (targetNodeRing k),
      setup.trace 1 *
        algebraMap (nodeRing k) (FractionRing (nodeRing k)) (x k + y k) =
        algebraMap (nodeRing k) (FractionRing (nodeRing k))
          ((algebraMap k (nodeRing k) (n : k)) * x k +
            (algebraMap k (nodeRing k) (m : k)) * y k)
```

**`Stacks.Discriminant.NodeExample.trace_u_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/TraceValues.lean, line 592](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/TraceValues.lean#L592). The attribute's comment: “trace of u powers”.

> The trace vanishes on proper powers of the first branch coordinate.

```lean
theorem trace_u_pow
    (n m : ℕ) (hn : IsUnit (n : k)) (hm : IsUnit (m : k))
    (f : nodeRing k →+* targetNodeRing k)
    (hx : f (x k) = u k ^ n) (hy : f (y k) = v k ^ m)
    (hk : ∀ a : k, f (algebraMap k (nodeRing k) a) = algebraMap k (targetNodeRing k) a) :
    letI : Algebra (nodeRing k) (targetNodeRing k) := f.toAlgebra
    ∀ (setup : DedekindDifferentSetup (nodeRing k) (targetNodeRing k))
      (i : ℕ), 1 ≤ i → i < n →
        setup.trace (TensorProduct.tmul (nodeRing k) (u k ^ i) 1) = 0
```

**`Stacks.Discriminant.NodeExample.trace_v_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/TraceValues.lean, line 607](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/GeneralizationDifferent/NodeExample/TraceValues.lean#L607). The attribute's comment: “trace of v powers”.

> The trace vanishes on proper powers of the second branch coordinate.

```lean
theorem trace_v_pow
    (n m : ℕ) (hn : IsUnit (n : k)) (hm : IsUnit (m : k))
    (f : nodeRing k →+* targetNodeRing k)
    (hx : f (x k) = u k ^ n) (hy : f (y k) = v k ^ m)
    (hk : ∀ a : k, f (algebraMap k (nodeRing k) a) = algebraMap k (targetNodeRing k) a) :
    letI : Algebra (nodeRing k) (targetNodeRing k) := f.toAlgebra
    ∀ (setup : DedekindDifferentSetup (nodeRing k) (targetNodeRing k))
      (j : ℕ), 1 ≤ j → j < m →
        setup.trace (TensorProduct.tmul (nodeRing k) (v k ^ j) 1) = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 49.14, Tag 0BWK](https://stacks.math.columbia.edu/tag/0BWK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
