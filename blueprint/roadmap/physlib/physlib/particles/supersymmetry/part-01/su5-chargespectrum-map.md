---
declaration: module
origin: cited
lean: SuperSymmetry.SU5.ChargeSpectrum.map, SuperSymmetry.SU5.ChargeSpectrum.map_empty, SuperSymmetry.SU5.ChargeSpectrum.map_map, SuperSymmetry.SU5.ChargeSpectrum.map_id, SuperSymmetry.SU5.ChargeSpectrum.map_ofFieldLabel, SuperSymmetry.SU5.ChargeSpectrum.map_subset, SuperSymmetry.SU5.ChargeSpectrum.map_ofPotentialTerm_toFinset, SuperSymmetry.SU5.ChargeSpectrum.mem_map_ofPotentialTerm_iff
statement: formalized
proof: formalized
---

# Mapping charge spectra values

The module `Physlib.Particles.SuperSymmetry.SU5.ChargeSpectrum.Map`, [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean): 26 declarations, 3 with a docstring.

## i. Overview

> In this module we define a function `map` which takes an additive monoid homomorphism
> `f : 𝓩 →+ 𝓩1` and a charge spectra `x : ChargeSpectrum 𝓩`, and returns the charge
> `x.map f : ChargeSpectrum 𝓩1` obtained by mapping the elements of `x` by `f`.
>
> There are various properties which are preserved under this mapping:
> - The presence of a specific term in the potential.
> - Being complete.
>
> There are some properties which are reflected under this mapping:
> - Not being pheno-constrained.
> - Not regenerating dangerous Yukawa terms at a given level.
>
> We define the preimage of this mapping within a subset `ofFinset S5 S10` of `Charges 𝓩` in
> a computationally efficient way.

## ii. Key results

> - `map` : The mapping of charge spectra under an additive monoid homomorphism.
> - `map_allowsTerm` : If a charge spectrum allows a potential term, then so does its mapping.
> - `map_isPhenoConstrained` : If a charge spectrum is pheno-constrained, then so is its mapping.
> - `map_isComplete_iff` : A charge spectrum is complete if and only if its mapping is complete.
> - `map_yukawaGeneratesDangerousAtLevel` : A charge spectrum regenerates dangerous Yukawa terms
>   at a given level then so does its mapping.
> - `preimageOfFinset` : The preimage of a charge spectrum in `ofFinset S5 S10`
>   under a mapping.
> - `preimageOfFinsetCard` : The cardinality of the preimage of a charge spectrum
>   in `ofFinset S5 S10` under a mapping.

## iv. References

> * None.

## A. The mapping of charge spectra

**`SuperSymmetry.SU5.ChargeSpectrum.map`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L89).

> Given an additive monoid homomorphisms `f : 𝓩 →+ 𝓩1`, for a charge spectrum
> `x : ChargeSpectrum 𝓩`, `x.map f` is the charge spectrum in `ChargeSpectrum 𝓩1` obtained by
> mapping the elements of `x` by `f`.

```lean
def map (f : 𝓩 →+ 𝓩1) (x : ChargeSpectrum 𝓩) : ChargeSpectrum 𝓩1
```

**`SuperSymmetry.SU5.ChargeSpectrum.map_empty`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L102).

```lean
lemma map_empty (f : 𝓩 →+ 𝓩1) : map f (∅ : ChargeSpectrum 𝓩) = ∅
```

### A.2. Mapping of charge spectra obeys composing maps

**`SuperSymmetry.SU5.ChargeSpectrum.map_map`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L113).

```lean
lemma map_map (f : 𝓩 →+ 𝓩1) (g : 𝓩1 →+ 𝓩2) (x : ChargeSpectrum 𝓩) :
    map g (map f x) = map (g.comp f) x
```

### A.3. Mapping of charge spectra obeys the identity

**`SuperSymmetry.SU5.ChargeSpectrum.map_id`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L124).

```lean
lemma map_id [DecidableEq 𝓩] (x : ChargeSpectrum 𝓩) : map (AddMonoidHom.id 𝓩) x = x
```

### A.4. The charges of a field label commute with mapping of charge spectra

**`SuperSymmetry.SU5.ChargeSpectrum.map_ofFieldLabel`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L133).

```lean
lemma map_ofFieldLabel (f : 𝓩 →+ 𝓩1) (x : ChargeSpectrum 𝓩) (F : FieldLabel) :
    ofFieldLabel (map f x) F = (ofFieldLabel x F).image f
```

### A.5. Mappings of charge spectra preserve the subset relation

**`SuperSymmetry.SU5.ChargeSpectrum.map_subset`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L165).

```lean
lemma map_subset {f : 𝓩 →+ 𝓩1} {x y : ChargeSpectrum 𝓩} (h : x ⊆ y) :
    map f x ⊆ map f y
```

### A.6. Mappings of charge spectra and charges of potential terms

**`SuperSymmetry.SU5.ChargeSpectrum.map_ofPotentialTerm_toFinset`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L195).

```lean
lemma map_ofPotentialTerm_toFinset [DecidableEq 𝓩]
    (f : 𝓩 →+ 𝓩1) (x : ChargeSpectrum 𝓩) (T : PotentialTerm) :
    (ofPotentialTerm (map f x) T).toFinset = (ofPotentialTerm x T).toFinset.image f
```

**`SuperSymmetry.SU5.ChargeSpectrum.mem_map_ofPotentialTerm_iff`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L212).

```lean
lemma mem_map_ofPotentialTerm_iff [DecidableEq 𝓩]
    (f : 𝓩 →+ 𝓩1) (x : ChargeSpectrum 𝓩) (T : PotentialTerm) :
    i ∈ (ofPotentialTerm (map f x) T) ↔ i ∈ (ofPotentialTerm x T).map f
```

**`SuperSymmetry.SU5.ChargeSpectrum.mem_map_ofPotentialTerm'_iff`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L220).

```lean
lemma mem_map_ofPotentialTerm'_iff[DecidableEq 𝓩]
    (f : 𝓩 →+ 𝓩1) (x : ChargeSpectrum 𝓩) (T : PotentialTerm) :
    i ∈ (ofPotentialTerm' (map f x) T) ↔ i ∈ (ofPotentialTerm' x T).map f
```

**`SuperSymmetry.SU5.ChargeSpectrum.map_ofPotentialTerm'_toFinset`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L234).

```lean
lemma map_ofPotentialTerm'_toFinset [DecidableEq 𝓩]
    (f : 𝓩 →+ 𝓩1) (x : ChargeSpectrum 𝓩) (T : PotentialTerm) :
    (ofPotentialTerm' (map f x) T).toFinset = (ofPotentialTerm' x T).toFinset.image f
```

### A.7. Mapping charge spectra of `allowsTermForm

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTermForm_map`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L249).

```lean
lemma allowsTermForm_map {T} {f : 𝓩 →+ 𝓩1} {a b c : 𝓩} :
    (allowsTermForm a b c T).map f = allowsTermForm (f a) (f b) (f c) T
```

### A.8. Mapping preserves whether a charge spectrum allows a potential term

**`SuperSymmetry.SU5.ChargeSpectrum.map_allowsTerm`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L260).

```lean
lemma map_allowsTerm {f : 𝓩 →+ 𝓩1} {x : ChargeSpectrum 𝓩} {T : PotentialTerm}
    (h : x.AllowsTerm T) : (map f x).AllowsTerm T
```

### A.9. Mapping preserves if a charge spectrum is pheno-constrained

**`SuperSymmetry.SU5.ChargeSpectrum.map_isPhenoConstrained`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L274).

```lean
lemma map_isPhenoConstrained (f : 𝓩 →+ 𝓩1) {x : ChargeSpectrum 𝓩}
    (h : x.IsPhenoConstrained) : (map f x).IsPhenoConstrained
```

**`SuperSymmetry.SU5.ChargeSpectrum.not_isPhenoConstrained_of_map`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L287).

```lean
lemma not_isPhenoConstrained_of_map {f : 𝓩 →+ 𝓩1} {x : ChargeSpectrum 𝓩}
    (h : ¬ (map f x).IsPhenoConstrained) : ¬ x.IsPhenoConstrained
```

### A.10. Mapping preserves completeness of charge spectra

**`SuperSymmetry.SU5.ChargeSpectrum.map_isComplete_iff`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L298).

```lean
lemma map_isComplete_iff {f : 𝓩 →+ 𝓩1} {x : ChargeSpectrum 𝓩} :
    (map f x).IsComplete ↔ x.IsComplete
```

### A.11. Mapping commutes with charges of Yukawa terms

**`SuperSymmetry.SU5.ChargeSpectrum.map_ofYukawaTerms_toFinset`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L308).

```lean
lemma map_ofYukawaTerms_toFinset {f : 𝓩 →+ 𝓩1} {x : ChargeSpectrum 𝓩} :
    (map f x).ofYukawaTerms.toFinset = x.ofYukawaTerms.toFinset.image f
```

**`SuperSymmetry.SU5.ChargeSpectrum.mem_map_ofYukawaTerms_iff`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L317).

```lean
lemma mem_map_ofYukawaTerms_iff {f : 𝓩 →+ 𝓩1} {x : ChargeSpectrum 𝓩} {i} :
    i ∈ (map f x).ofYukawaTerms ↔ i ∈ x.ofYukawaTerms.map f
```

### A.12. Mapping of charge spectra and regenerating dangerous Yukawa terms

**`SuperSymmetry.SU5.ChargeSpectrum.map_ofYukawaTermsNSum_toFinset`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L330).

```lean
lemma map_ofYukawaTermsNSum_toFinset {f : 𝓩 →+ 𝓩1} {x : ChargeSpectrum 𝓩} {n : ℕ}:
    ((map f x).ofYukawaTermsNSum n).toFinset = (x.ofYukawaTermsNSum n).toFinset.image f
```

**`SuperSymmetry.SU5.ChargeSpectrum.mem_map_ofYukawaTermsNSum_iff`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L365).

```lean
lemma mem_map_ofYukawaTermsNSum_iff {f : 𝓩 →+ 𝓩1} {x : ChargeSpectrum 𝓩} {n i} :
    i ∈ (map f x).ofYukawaTermsNSum n ↔ i ∈ (x.ofYukawaTermsNSum n).map f
```

**`SuperSymmetry.SU5.ChargeSpectrum.map_phenoConstrainingChargesSP_toFinset`**, a lemma, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L372).

```lean
lemma map_phenoConstrainingChargesSP_toFinset {f : 𝓩 →+ 𝓩1} {x : ChargeSpectrum 𝓩} :
    (map f x).phenoConstrainingChargesSP.toFinset =
    x.phenoConstrainingChargesSP.toFinset.image f
```

**`SuperSymmetry.SU5.ChargeSpectrum.map_yukawaGeneratesDangerousAtLevel`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L377).

```lean
lemma map_yukawaGeneratesDangerousAtLevel (f : 𝓩 →+ 𝓩1) {x : ChargeSpectrum 𝓩} (n : ℕ)
    (h : x.YukawaGeneratesDangerousAtLevel n) : (map f x).YukawaGeneratesDangerousAtLevel n
```

**`SuperSymmetry.SU5.ChargeSpectrum.not_yukawaGeneratesDangerousAtLevel_of_map`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L386).

```lean
lemma not_yukawaGeneratesDangerousAtLevel_of_map {f : 𝓩 →+ 𝓩1} {x : ChargeSpectrum 𝓩}
    (n : ℕ) (h : ¬ (map f x).YukawaGeneratesDangerousAtLevel n) :
    ¬ x.YukawaGeneratesDangerousAtLevel n
```

## B. Preimage of a charge spectrum under a mapping

> We give a computationally efficient way of calculating the preimage of a charge
> `s : Charges 𝓩1` in a subset `ofFinset S5 S10`, and then show it is
> equal to the actual preimage.

**`SuperSymmetry.SU5.ChargeSpectrum.preimageOfFinset`**, a def, [line 403](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L403).

> The preimage of a charge `Charges 𝓩1` in `ofFinset S5 S10 ⊆ Charges 𝓩` under
> mapping charges through `f : 𝓩 →+ 𝓩1`.

```lean
def preimageOfFinset (S5 S10 : Finset 𝓩) (f : 𝓩 →+ 𝓩1)
    (x : ChargeSpectrum 𝓩1) : Finset (ChargeSpectrum 𝓩)
```

### B.1. `preimageOfFinset` gives the actual preimage

**`SuperSymmetry.SU5.ChargeSpectrum.preimageOfFinset_eq`**, a lemma, [line 420](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L420).

```lean
lemma preimageOfFinset_eq (S5 S10 : Finset 𝓩) (f : 𝓩 →+ 𝓩1) (x : ChargeSpectrum 𝓩1) :
    preimageOfFinset S5 S10 f x = {y : ChargeSpectrum 𝓩 | y.map f = x ∧ y ∈ ofFinset S5 S10}
```

### B.2. Efficient definition for the cardinality of the preimage

**`SuperSymmetry.SU5.ChargeSpectrum.preimageOfFinsetCard`**, a def, [line 475](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L475).

> The cardinality of the
> preimage of a charge `Charges 𝓩1` in `ofFinset S5 S10 ⊆ Charges 𝓩` under
> mapping charges through `f : 𝓩 →+ 𝓩1`.

```lean
def preimageOfFinsetCard (S5 S10 : Finset 𝓩) (f : 𝓩 →+ 𝓩1) (x : ChargeSpectrum 𝓩1) : ℕ
```

### B.3. Definition for the cardinality equals cardinality of the preimage

**`SuperSymmetry.SU5.ChargeSpectrum.preimageOfFinset_card_eq`**, a lemma, [line 492](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean#L492).

```lean
lemma preimageOfFinset_card_eq (S5 S10 : Finset 𝓩) (f : 𝓩 →+ 𝓩1) (x : ChargeSpectrum 𝓩1) :
    preimageOfFinsetCard S5 S10 f x =
    (preimageOfFinset S5 S10 f x).card
```

## Depends on

- [Completions of charges](su5-chargespectrum-completions.md)
- [Yukawa charges](../part-02/su5-chargespectrum-yukawa.md)

## Sources

- [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Map.lean)
