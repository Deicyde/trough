---
declaration: module
origin: cited
lean: FTheory.SU5.Quanta.IsViable, FTheory.SU5.Quanta.isViable_iff_def, FTheory.SU5.Quanta.isViable_iff_charges_mem_viableCharges, FTheory.SU5.Quanta.isViable_iff_charges_mem_viableCharges_mem_liftCharges, FTheory.SU5.Quanta.isViable_iff_filter, FTheory.SU5.Quanta.viableElems, FTheory.SU5.Quanta.isViable_of_mem_viableElems, FTheory.SU5.Quanta.isViable_iff_mem_viableElems
statement: formalized
proof: formalized
---

# Viable Quanta with Yukawa

The module `Physlib.StringTheory.FTheory.SU5.Quanta.IsViable`, [Physlib/StringTheory/FTheory/SU5/Quanta/IsViable.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/IsViable.lean): 11 declarations, 3 with a docstring.

## i. Overview

> We say a term of a type `Quanta` is viable
>   if it satisfies the following properties:
> - It has a `Hd`, `Hu` and at least one matter particle in the 5 and 10 representation.
> - It has no exotic chiral particles.
> - It leads to a top Yukawa coupling.
> - It does not lead to a pheno constraining terms.
> - It does not lead to a dangerous Yukawa coupling at one insertion of the Yukawa singlets.
> - It satisfies linear anomaly cancellation.
> - The charges are allowed by an `I` configuration.
>
> We also write down the explicit set of viable quanta, and prove that this set is complete.
>
> One can view the dependencies of this module with:
>
> ```
> lake exe graph --from
>   Physlib.StringTheory.FTheory.SU5.Fluxes.Basic,Physlib.Particles.SuperSymmetry.SU5.FieldLabels
>   my_graph.pdf
> ```

## ii. Key results

> - `Quanta.IsViable` : The proposition on a `Quanta` that it is viable.
> - `Quanta.viableElems` : The multiset of viable quanta.
> - `Quanta.isViable_iff_mem_viableElems` : A quanta is viable if and only if it is in the
>   `Quanta.viableElems`.

## iv. References

> * Froggatt-Nielsen meets Mordell-Weil: A Phenomenological Survey of Global F-theory GUTs
>   with U(1)s (arxiv:1507.05961). [ref: arxiv\_1507\_05961]

## A. The condition for a `Quanta` to be viable

**`FTheory.SU5.Quanta.IsViable`**, a structure, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/IsViable.lean#L81).

> For a given `I : CodimensionOneConfig` the condition on a `Quanta` for it to be
> phenomenologically viable.

```lean
structure IsViable (x : Quanta) : Prop where
  /-- There is a `Hd`, `Hu`, 5-bar matter and 10d matter. -/
  has_all_charges : x.toCharges.IsComplete
  /-- The charges do not lead to any phenomenologically constraining terms. -/
  not_pheno_constrained : ¬ x.toCharges.IsPhenoConstrained
  /-- The charges are such that dangerous couplings in the super potential are not
    regenerated with the Yukawa terms. -/
  not_regenerate_dangerous_couplings : ¬ x.toCharges.YukawaGeneratesDangerousAtLevel 1
  /-- The charges are such that they are allowed by a configuration of sections on the
    co-dimension 1 fiber. -/
  charges_allowed_by_section_config :
    (∃ I : CodimensionOneConfig, x.toCharges ∈ ofFinset I.allowedBarFiveCharges I.allowedTenCharges)
  /-- Within the 5-bar matter, there is at most one entry for each charge. -/
  no_duplicate_five_bar_charges : x.F.toCharges.Nodup
  /-- Within the 10d matter, there is at most one entry for each charge. -/
  no_duplicate_ten_charges : x.T.toCharges.Nodup
  /-- The charges permit at least one Top-Yukawa coupling. -/
  allows_top_yukawa : AllowsTerm x.toCharges topYukawa
  /-- The fluxes of the 5-bar matter fields do not lead to any exotic chiral particles. -/
  no_exotics_from_five_bar : x.F.toFluxesFive.NoExotics
  /-- There are 5-bar matter fields where both fluxes are zero (these are not
    being counted here). -/
  no_five_bar_zero_fluxes : x.F.toFluxesFive.HasNoZero
  /-- The fluxes of the 10d matter fields do not lead to any exotic chiral particles. -/
  no_exotics_from_ten : x.T.toFluxesTen.NoExotics
  /-- There are 10d matter fields where both fluxes are zero (these are not
    being counted here). -/
  no_ten_zero_fluxes : x.T.toFluxesTen.HasNoZero
  /-- The quanta satisfy the linear anomaly cancellation conditions. -/
  linear_anomalies : x.LinearAnomalyCancellation
```

**`FTheory.SU5.Quanta.isViable_iff_def`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/IsViable.lean#L112).

```lean
lemma isViable_iff_def (x : Quanta) : IsViable x ↔
    x.toCharges.IsComplete ∧
    ¬ x.toCharges.IsPhenoConstrained ∧
    ¬ x.toCharges.YukawaGeneratesDangerousAtLevel 1 ∧
    (∃ I : CodimensionOneConfig, x.toCharges ∈
      ofFinset I.allowedBarFiveCharges I.allowedTenCharges) ∧
    x.F.toCharges.Nodup ∧
    x.T.toCharges.Nodup ∧
    x.toCharges.AllowsTerm topYukawa ∧
    x.F.toFluxesFive.NoExotics ∧
    x.F.toFluxesFive.HasNoZero ∧
    x.T.toFluxesTen.NoExotics ∧
    x.T.toFluxesTen.HasNoZero ∧
    x.LinearAnomalyCancellation
```

### A.1. Simplification of the prop to use the set of viable charges `viableCharges I`

**`FTheory.SU5.Quanta.isViable_iff_charges_mem_viableCharges`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/IsViable.lean#L135).

```lean
lemma isViable_iff_charges_mem_viableCharges (x : Quanta) :
    IsViable x ↔
        /- 1. Conditions just on the charges. -/
        (∃ I, x.toCharges ∈ viableCharges I) ∧
        x.F.toCharges.Nodup ∧
        x.T.toCharges.Nodup ∧
        /- 2. Conditions just on the fluxes -/
        x.F.toFluxesFive.NoExotics ∧
        x.F.toFluxesFive.HasNoZero ∧
        x.T.toFluxesTen.NoExotics ∧
        x.T.toFluxesTen.HasNoZero ∧
        /- 3. Conditions on the fluxes and the charges. -/
        x.LinearAnomalyCancellation
```

### A.2. Further simplification of the prop to use the set of viable charges `Quanta.liftCharge`

**`FTheory.SU5.Quanta.isViable_iff_charges_mem_viableCharges_mem_liftCharges`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/IsViable.lean#L157).

```lean
lemma isViable_iff_charges_mem_viableCharges_mem_liftCharges (x : Quanta) :
    IsViable x ↔ (∃ I, x.toCharges ∈ viableCharges I) ∧
      x ∈ Quanta.liftCharge x.toCharges ∧
      x.LinearAnomalyCancellation
```

### A.3. Further simplification of the prop to use the anomaly free set of viable charges

**`FTheory.SU5.Quanta.isViable_iff_filter`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/IsViable.lean#L173).

```lean
lemma isViable_iff_filter (x : Quanta) :
    IsViable x ↔ (∃ I, x.toCharges ∈ (viableCharges I).filter IsAnomalyFree) ∧
      x ∈ Quanta.liftCharge x.toCharges
      ∧ x.LinearAnomalyCancellation
```

## B. The multiset of viable quanta

> We find all the viable quanta. This can be evaluated with
>
> ```
>   ((((viableCharges .same ∪ viableCharges .nearestNeighbor ∪
>   viableCharges .nextToNearestNeighbor).filter IsAnomalyFree).bind
>     Quanta.liftCharge).filter LinearAnomalyCancellation)
> ```

**`FTheory.SU5.Quanta.viableElems`**, a def, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/IsViable.lean#L195).

> Given a `CodimensionOneConfig` the `Quanta` which satisfy the condition `IsViable`.

```lean
def viableElems : Multiset Quanta
```

### B.1. Every element of the multiset is viable

**`FTheory.SU5.Quanta.isViable_of_mem_viableElems`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/IsViable.lean#L239).

```lean
lemma isViable_of_mem_viableElems (x : Quanta) (h : x ∈ viableElems) :
    IsViable x
```

### B.2. A quanta is viable if and only if it is in the multiset

**`FTheory.SU5.Quanta.isViable_iff_mem_viableElems`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/IsViable.lean#L251).

```lean
lemma isViable_iff_mem_viableElems (x : Quanta) :
    x.IsViable ↔ x ∈ viableElems
```

### B.3. Every element of the multiset regenerates Yukawa at two insertions of the Yukawa singlets

**`FTheory.SU5.Quanta.yukawaSingletsRegenerateDangerousInsertion_two_of_isViable`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/IsViable.lean#L274).

> Every viable Quanta regenerates a dangerous coupling at two insertions of the Yukawa
> singlets.

```lean
lemma yukawaSingletsRegenerateDangerousInsertion_two_of_isViable
    (x : Quanta) (h : IsViable x) :
    (toCharges x).YukawaGeneratesDangerousAtLevel 2
```

### B.4. Those quanta which satisfy the quartic anomaly cancellation condition

**`FTheory.SU5.Quanta.quarticAnomalyCancellation_iff_mem_of_isViable`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/IsViable.lean#L287).

```lean
lemma quarticAnomalyCancellation_iff_mem_of_isViable (x : Quanta) (h : IsViable x) :
    x.QuarticAnomalyCancellation ↔ x ∈
    ({⟨some 2, some (-2), {(-1, ⟨1, 2⟩), (1, ⟨2, -2⟩)}, {(-1, ⟨3, 0⟩)}⟩,
    ⟨some 2, some (-2), {(-1, ⟨0, 2⟩), (1, ⟨3, -2⟩)}, {(-1, ⟨3, 0⟩)}⟩,
    ⟨some (-2), some 2, {(-1, ⟨2, -2⟩), (1, ⟨1, 2⟩)}, {(1, ⟨3, 0⟩)}⟩,
    ⟨some (-2), some 2, {(-1, ⟨3, -2⟩), (1, ⟨0, 2⟩)}, {(1, ⟨3, 0⟩)}⟩,
    ⟨some 6, some (-14), {(-9, ⟨1, 2⟩), (1, ⟨2, -2⟩)}, {(-7, ⟨3, 0⟩)}⟩,
    ⟨some 6, some (-14), {(-9, ⟨0, 2⟩), (1, ⟨3, -2⟩)}, {(-7, ⟨3, 0⟩)}⟩} : Finset Quanta)
```

### B.5. Map down to Z2

**`FTheory.SU5.Quanta.map_to_Z2_of_isViable`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/IsViable.lean#L305).

```lean
lemma map_to_Z2_of_isViable (x : Quanta ℤ) (h : IsViable x) :
    x.toCharges.map (Int.castAddHom (ZMod 2)) ∈
    ({⟨some 0, some 0, {1}, {1}⟩, ⟨some 0, some 0, {0,1}, {1}⟩, ⟨some 0, some 0, {0,1}, {0}⟩} :
    Finset (ChargeSpectrum (ZMod 2)))
```

## Depends on

- [Anomaly cancellation](su5-charges-anomalyfree.md)

## Sources

- [Physlib/StringTheory/FTheory/SU5/Quanta/IsViable.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/IsViable.lean)
