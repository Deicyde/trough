---
declaration: module
origin: cited
lean: FTheory.SU5.ChargeSpectrum.viableCompletions, FTheory.SU5.ChargeSpectrum.viableCompletions_card, FTheory.SU5.ChargeSpectrum.viableCompletions_nodup, FTheory.SU5.ChargeSpectrum.viableCompletions_isPhenoConstrained, FTheory.SU5.ChargeSpectrum.viableCompletions_yukawaGeneratesDangerousAtLevel_one, FTheory.SU5.ChargeSpectrum.containsPhenoCompletionsOfMinimallyAllows_viableCompletions, FTheory.SU5.ChargeSpectrum.viableChargesAdditional, FTheory.SU5.ChargeSpectrum.viableChargesAdditional_nodup
statement: formalized
proof: formalized
---

# Charges which are not pheno-constrained and do not regenerate dangerous couplings with Yukawas

The module `Physlib.StringTheory.FTheory.SU5.Charges.Viable`, [Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean): 26 declarations, 5 with a docstring.

## i. Overview

> WARNING: This file can take a long time to compute.
>
> In this module, given a configuration of the sections in codimension one
> fiber `CodimensionOneConfig`, we find the multiset of all
> `ℤ`-valued charges which have values allowed by the configuration,
> permit a top Yukawa coupling, are not phenomenologically constrained,
> and do not regenerate dangerous couplings with one insertion of a Yukawa coupling.
>
> The multiset of charge spectrum is called `viableCharges`.
> The main proof that `viableCharges` contains all such charges is
> using `completeness_of_isPhenoClosedQ5_isPhenoClosedQ10`.
> Note this proof relies on us stating `viableCharges` and then verifying
> that it has the required properties.
>
> To make our lives easier, we first construct a multiset of charge spectrum called
> `viableCompletions` which contains all completions of charges which minimally allow the top Yukawa,
> which are not phenomenologically constrained, and do not regenerate dangerous couplings.
> Again the proof that `viableCompletions` has these properties is done by
> first stating `viableCompletions` and then verifying that it has the required properties,
> primarily using `ContainsPhenoCompletionsOfMinimallyAllows`.
>
> We also define `viableChargesAdditional` which are the multiset of charge spectrum
> which are in `viableCharges` but not in `viableCompletions`. This helps split some of the
> proofs.
>
> Note that this file is slow to run, any improvements to the speed of this file
> will be very welcome. In particular working out a way to restrict by anomaly cancellation.

## ii. Key results

> - `viableCharges` contains all charges, for a given `CodimensionOneConfig`, `I`,
>   which permit a top Yukawa coupling, are not phenomenologically constrained,
>   and do not regenerate dangerous couplings with one insertion of a Yukawa coupling.
> - The lemma `mem_viableCharges_iff` expresses membership of `viableCharges I`, i.e.
>   that it contains all charges which permit a top Yukawa coupling,
>   are not phenomenologically constrained, and do not regenerate dangerous couplings.
> - The lemma `mem_viableCharges_iff` follows directly from
>   `completeness_of_isPhenoClosedQ5_isPhenoClosedQ10`
>   and a number of conditions on `viableCharges` which can be proved using the `decide`
>   tactic.
> - `viableCharges` itself is constructed via `viableCompletions` which
>   contains all completions of charges which minimally allow the top Yukawa,
>   which are not phenomenologically constrained, and do not regenerate dangerous couplings.

## iv. References

> * None.

## A. Viable completions of charges permitting a top Yukawa coupling

### A.1. Stating the multiset `viableCompletions`

**`FTheory.SU5.ChargeSpectrum.viableCompletions`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L128).

> The multiset of charges which are completions of charges which minimally allow the top Yukawa,
>   which are not phenomenologically constrained, and do not regenerate dangerous couplings.
>
> This can be constructed via
>
> `#eval completeMinSubset same.allowedBarFiveCharges same.allowedTenCharges`

```lean
def viableCompletions (I : CodimensionOneConfig) : Multiset (ChargeSpectrum ℤ)
```

### A.2. Cardinality of `viableCompletions`

**`FTheory.SU5.ChargeSpectrum.viableCompletions_card`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L236).

```lean
lemma viableCompletions_card (I : CodimensionOneConfig) :
    (viableCompletions I).card = if I = same then 70 else
      if I = nearestNeighbor then 48 else 37
```

### A.3. No duplicates of `viableCompletions`

**`FTheory.SU5.ChargeSpectrum.viableCompletions_nodup`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L247).

```lean
lemma viableCompletions_nodup (I : CodimensionOneConfig) :
    (viableCompletions I).Nodup
```

### A.4. Elements of `viableCompletions` are not pheno-constrained

**`FTheory.SU5.ChargeSpectrum.viableCompletions_isPhenoConstrained`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L257).

```lean
lemma viableCompletions_isPhenoConstrained (I : CodimensionOneConfig) :
    ∀ x ∈ viableCompletions I, ¬ IsPhenoConstrained x
```

### A.5. Elements of `viableCompletions` do not regenerate dangerous couplings

**`FTheory.SU5.ChargeSpectrum.viableCompletions_yukawaGeneratesDangerousAtLevel_one`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L267).

```lean
lemma viableCompletions_yukawaGeneratesDangerousAtLevel_one (I : CodimensionOneConfig) :
    ∀ x ∈ viableCompletions I, ¬ YukawaGeneratesDangerousAtLevel x 1
```

### A.6. `viableCompletions` contain all pheno-viable completions of top-yukawa permitting

**`FTheory.SU5.ChargeSpectrum.containsPhenoCompletionsOfMinimallyAllows_viableCompletions`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L277).

```lean
lemma containsPhenoCompletionsOfMinimallyAllows_viableCompletions :
    (I : CodimensionOneConfig) →
    ContainsPhenoCompletionsOfMinimallyAllows I.allowedBarFiveCharges
      I.allowedTenCharges (viableCompletions I)
```

## B. The multiset of additional viable charges

### B.1. Stating the multiset `viableChargesAdditional`

**`FTheory.SU5.ChargeSpectrum.viableChargesAdditional`**, a def, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L304).

> The charges in addition to `viableCompletions` which which permit a top Yukawa coupling,
> are not phenomenologically constrained,
> and do not regenerate dangerous couplings with one insertion of a Yukawa coupling.
>
> These can be found with e.g.
> - #eval (viableChargesMultiset same.allowedBarFiveCharges same.allowedTenCharges).toFinset \
>   (completeMinSubset same.allowedBarFiveCharges
>     same.allowedTenCharges).toFinset

```lean
def viableChargesAdditional : CodimensionOneConfig → Multiset (ChargeSpectrum ℤ)
```

### B.2. `viableChargesAdditional` has no duplicates

**`FTheory.SU5.ChargeSpectrum.viableChargesAdditional_nodup`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L350).

```lean
lemma viableChargesAdditional_nodup (I : CodimensionOneConfig) :
    (viableChargesAdditional I).Nodup
```

### B.3. Elements of `viableChargesAdditional` are not pheno-constrained

**`FTheory.SU5.ChargeSpectrum.not_isPhenoConstrained_of_mem_viableChargesAdditional`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L360).

```lean
lemma not_isPhenoConstrained_of_mem_viableChargesAdditional (I : CodimensionOneConfig) :
    ∀ x ∈ (viableChargesAdditional I), ¬ IsPhenoConstrained x
```

### B.4. Elements of `viableChargesAdditional` do not regenerate dangerous couplings

**`FTheory.SU5.ChargeSpectrum.yukawaGeneratesDangerousAtLevel_one_of_mem_viableChargesAdditional`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L370).

```lean
lemma yukawaGeneratesDangerousAtLevel_one_of_mem_viableChargesAdditional
    (I : CodimensionOneConfig) :
    ∀ x ∈ (viableChargesAdditional I), ¬ YukawaGeneratesDangerousAtLevel x 1
```

### B.5. `viableChargesAdditional` is disjoint from `viableCompletions`

**`FTheory.SU5.ChargeSpectrum.viableCompletions_disjiont_viableChargesAdditional`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L381).

```lean
lemma viableCompletions_disjiont_viableChargesAdditional (I : CodimensionOneConfig) :
    Disjoint (viableCompletions I) (viableChargesAdditional I)
```

## C. The multiset of all viable charges given a configuration of sections

### C.1. Stating the multiset `viableCharges`

**`FTheory.SU5.ChargeSpectrum.viableCharges`**, a def, [line 405](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L405).

> All charges, for a given `CodimensionOneConfig`, `I`,
> which permit a top Yukawa coupling, are not phenomenologically constrained,
> and do not regenerate dangerous couplings with one insertion of a Yukawa coupling.
>
> These trees can be found with e.g.
> `#eval viableChargesExt nextToNearestNeighbor`.

```lean
def viableCharges (I : CodimensionOneConfig) : Multiset (ChargeSpectrum ℤ)
```

### C.2. `viableCharges` has no duplicates

**`FTheory.SU5.ChargeSpectrum.viableCharges_nodup`**, a lemma, [line 414](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L414).

```lean
lemma viableCharges_nodup (I : CodimensionOneConfig) :
    (viableCharges I).Nodup
```

### C.3. Cardinality of `viableCharges`

**`FTheory.SU5.ChargeSpectrum.viableCharges_card`**, a lemma, [line 424](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L424).

```lean
lemma viableCharges_card (I : CodimensionOneConfig) :
    (viableCharges I).card =
    if I = .same then 102 else
    if I = .nearestNeighbor then 71 else 51
```

### C.4. Elements of `viableCharges` have charges allowed by configuration

**`FTheory.SU5.ChargeSpectrum.viableCharges_mem_ofFinset`**, a lemma, [line 436](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L436).

```lean
lemma viableCharges_mem_ofFinset (I : CodimensionOneConfig) :
    ∀ x ∈ (viableCharges I), x ∈ ofFinset I.allowedBarFiveCharges I.allowedTenCharges
```

### C.5. Elements of `viableCharges` are complete

**`FTheory.SU5.ChargeSpectrum.isComplete_of_mem_viableCharges`**, a lemma, [line 447](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L447).

```lean
lemma isComplete_of_mem_viableCharges (I : CodimensionOneConfig) :
    ∀ x ∈ (viableCharges I), IsComplete x
```

### C.6. Elements of `viableCharges` permit a top Yukawa coupling

**`FTheory.SU5.ChargeSpectrum.allowsTerm_topYukawa_of_mem_viableCharges`**, a lemma, [line 457](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L457).

```lean
lemma allowsTerm_topYukawa_of_mem_viableCharges (I : CodimensionOneConfig) :
    ∀ x ∈ (viableCharges I), x.AllowsTerm topYukawa
```

### C.7. Elements of `viableCharges` are not pheno-constrained

**`FTheory.SU5.ChargeSpectrum.not_isPhenoConstrained_of_mem_viableCharges`**, a lemma, [line 467](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L467).

```lean
lemma not_isPhenoConstrained_of_mem_viableCharges (I : CodimensionOneConfig) :
    ∀ x ∈ (viableCharges I), ¬ IsPhenoConstrained x
```

### C.8. Elements of `viableCharges` do not regenerate dangerous couplings

**`FTheory.SU5.ChargeSpectrum.not_yukawaGeneratesDangerousAtLevel_one_of_mem_viableCharges`**, a lemma, [line 480](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L480).

```lean
lemma not_yukawaGeneratesDangerousAtLevel_one_of_mem_viableCharges
    (I : CodimensionOneConfig) :
    ∀ x ∈ (viableCharges I), ¬ YukawaGeneratesDangerousAtLevel x 1
```

### C.9. Elements of `viableCharges` have at most two 5-bar reps

**`FTheory.SU5.ChargeSpectrum.card_five_bar_le_of_mem_viableCharges`**, a lemma, [line 494](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L494).

```lean
lemma card_five_bar_le_of_mem_viableCharges (I : CodimensionOneConfig) :
    ∀ x ∈ (viableCharges I), x.Q5.card ≤ 2
```

### C.10. Elements of `viableCharges` have at most two 10d reps

**`FTheory.SU5.ChargeSpectrum.card_ten_le_of_mem_viableCharges`**, a lemma, [line 504](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L504).

```lean
lemma card_ten_le_of_mem_viableCharges (I : CodimensionOneConfig) :
    ∀ x ∈ (viableCharges I), x.Q10.card ≤ 2
```

### C.11. `viableCharges` is phenomenologically closed under adding 5-bar charges

> We now show that adding a Q5 or a Q10 charge to an element of `viableCharges I` leads to a
> charge which is either not phenomenologically constrained, or does not regenerate dangerous
> couplings, or is already in `viableCharges I`.

**`FTheory.SU5.ChargeSpectrum.isPhenoClosedQ5_viableCharges`**, a lemma, [line 522](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L522).

> Inserting a `q5` charge into an element of `viableCharges I` either
> 1. produces another element of `viableCharges I`, or
> 2. produce a charge which is phenomenologically constrained or regenerates dangerous couplings
>   with the Yukawas.

```lean
lemma isPhenoClosedQ5_viableCharges : (I : CodimensionOneConfig) →
    IsPhenoClosedQ5 I.allowedBarFiveCharges (viableCharges I)
```

### C.12. `viableCharges` is phenomenologically closed under adding 10d charges

**`FTheory.SU5.ChargeSpectrum.isPhenoClosedQ10_viableCharges`**, a lemma, [line 538](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L538).

> Inserting a `q10` charge into an element of `viableCharges I` either
> 1. produces another element of `viableCharges I`, or
> 2. produce a charge which is phenomenologically constrained or regenerates dangerous couplings
>   with the Yukawas.

```lean
lemma isPhenoClosedQ10_viableCharges : (I : CodimensionOneConfig) →
    IsPhenoClosedQ10 I.allowedTenCharges (viableCharges I)
```

### C.13. `viableCompletions` is a subset of `viableCharges`

**`FTheory.SU5.ChargeSpectrum.viableCompletions_subset_viableCharges`**, a lemma, [line 550](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L550).

```lean
lemma viableCompletions_subset_viableCharges (I : CodimensionOneConfig) :
    ∀ x ∈ (viableCompletions I), x ∈ viableCharges I
```

### C.14. `viableCharges` contains all pheno-viable charges given a section configuration

**`FTheory.SU5.ChargeSpectrum.mem_viableCharges_iff`**, a lemma, [line 562](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L562).

```lean
lemma mem_viableCharges_iff {I} {x : ChargeSpectrum}
    (hsub : x ∈ ofFinset I.allowedBarFiveCharges I.allowedTenCharges) :
    x ∈ viableCharges I ↔ AllowsTerm x topYukawa ∧
    ¬ IsPhenoConstrained x ∧ ¬ YukawaGeneratesDangerousAtLevel x 1 ∧ IsComplete x
```

**`FTheory.SU5.ChargeSpectrum.mem_viableCharges_iff'`**, a lemma, [line 578](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean#L578).

```lean
lemma mem_viableCharges_iff' {I} {x : ChargeSpectrum} :
    x ∈ viableCharges I ↔
    x ∈ ofFinset I.allowedBarFiveCharges I.allowedTenCharges ∧
    AllowsTerm x topYukawa ∧
    ¬ IsPhenoConstrained x ∧ ¬ YukawaGeneratesDangerousAtLevel x 1 ∧ IsComplete x
```

## Depends on

- [Phenomenologically closed sets of charge spectra](../../particles/supersymmetry/part-02/su5-chargespectrum-phenoclosed.md)
- [Allowed charges](su5-charges-ofrationalsection.md)

## Sources

- [Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/Viable.lean)
