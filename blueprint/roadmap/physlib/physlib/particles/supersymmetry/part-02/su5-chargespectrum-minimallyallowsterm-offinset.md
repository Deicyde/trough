---
declaration: module
origin: cited
lean: SuperSymmetry.SU5.ChargeSpectrum.toMultisetsOne, SuperSymmetry.SU5.ChargeSpectrum.mem_toMultisetsOne_iff, SuperSymmetry.SU5.ChargeSpectrum.toMultisetsTwo, SuperSymmetry.SU5.ChargeSpectrum.mem_toMultisetsTwo_iff, SuperSymmetry.SU5.ChargeSpectrum.toMultisetsThree, SuperSymmetry.SU5.ChargeSpectrum.mem_toMultisetsThree_iff, SuperSymmetry.SU5.ChargeSpectrum.minimallyAllowsTermsOfFinset, SuperSymmetry.SU5.ChargeSpectrum.mem_ofFinset_of_mem_minimallyAllowsTermOfFinset
statement: formalized
proof: formalized
---

# The set of charges which minimally allows a potential term

The module `Physlib.Particles.SuperSymmetry.SU5.ChargeSpectrum.MinimallyAllowsTerm.OfFinset`, [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/OfFinset.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/OfFinset.lean): 16 declarations, 4 with a docstring.

## i. Overview

> In this module given finite sets for the `5`-bar and `10`d charges `S5` and `S10`
> we find the sets of charge spectra which minimally allowed a potential term `T`.
> The set we will actually define will be a multiset, for computational
> efficiency (using multisets saves Lean having to manually check for duplicates,
> which can be very costly)
>
> To do this we define some auxiliary results which create multisets of a given cardinality
> from a finset.

## ii. Key results

> - `minimallyAllowsTermsOfFinset S5 S10 T` : the multiset of all charge spectra
>   with charges in `S5` and `S10` which minimally allow the potential term `T`.
> - `minimallyAllowsTerm_iff_mem_minimallyAllowsTermOfFinset` : the
>   statement that `minimallyAllowsTermsOfFinset S5 S10 T` contains exactly the charge spectra
>   with charges in `S5` and `S10` which minimally allow the potential term `T`.

## iv. References

> * None.

## A. Construction of set of charges which minimally allow a potential term

> We start with the construction of the set of charges which minimally allow a potential term,
> and then later prover properties about this set.
> The set we will define is `minimallyAllowsTermsOfFinset`, the construction of
> which relies on some preliminary results.

### A.1. Preliminary: Multisets from finite sets

> We construct the multisets of cardinality `1`, `2` and `3` which
> contain elements of finite set `s`.

#### A.1.1. Multisets of cardinality `1`

**`SuperSymmetry.SU5.ChargeSpectrum.toMultisetsOne`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/OfFinset.lean#L93).

> The multisets of cardinality `1` containing elements from a finite set `s`.

```lean
def toMultisetsOne (s : Finset 𝓩) : Multiset (Multiset 𝓩)
```

**`SuperSymmetry.SU5.ChargeSpectrum.mem_toMultisetsOne_iff`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/OfFinset.lean#L98).

```lean
lemma mem_toMultisetsOne_iff [DecidableEq 𝓩] {s : Finset 𝓩} (X : Multiset 𝓩) :
    X ∈ toMultisetsOne s ↔ X.toFinset ⊆ s ∧ X.card = 1
```

#### A.1.2. Multisets of cardinality `2`

**`SuperSymmetry.SU5.ChargeSpectrum.toMultisetsTwo`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/OfFinset.lean#L109).

> The multisets of cardinality `2` containing elements from a finite set `s`.

```lean
def toMultisetsTwo (s : Finset 𝓩) : Multiset (Multiset 𝓩)
```

**`SuperSymmetry.SU5.ChargeSpectrum.mem_toMultisetsTwo_iff`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/OfFinset.lean#L115).

```lean
lemma mem_toMultisetsTwo_iff [DecidableEq 𝓩] {s : Finset 𝓩} (X : Multiset 𝓩) :
    X ∈ toMultisetsTwo s ↔ X.toFinset ⊆ s ∧ X.card = 2
```

#### A.1.3. Multisets of cardinality `3`

**`SuperSymmetry.SU5.ChargeSpectrum.toMultisetsThree`**, a def, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/OfFinset.lean#L145).

> The multisets of cardinality `3` containing elements from a finite set `s`.

```lean
def toMultisetsThree [DecidableEq 𝓩] (s : Finset 𝓩) : Multiset (Multiset 𝓩)
```

**`SuperSymmetry.SU5.ChargeSpectrum.mem_toMultisetsThree_iff`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/OfFinset.lean#L152).

```lean
lemma mem_toMultisetsThree_iff [DecidableEq 𝓩] {s : Finset 𝓩} (X : Multiset 𝓩) :
    X ∈ toMultisetsThree s ↔ X.toFinset ⊆ s ∧ X.card = 3
```

### A.2. `minimallyAllowsTermsOfFinset`: the set of charges which minimally allow a potential term

> Given the construction of the multisets above we can now define the set of charges
> which minimally allow a potential term.
>
> We will prove it has the desired properties later in this module.

**`SuperSymmetry.SU5.ChargeSpectrum.minimallyAllowsTermsOfFinset`**, a def, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/OfFinset.lean#L213).

> The multiset of all charges within `ofFinset S5 S10` which minimally allow the
> potential term `T`.

```lean
def minimallyAllowsTermsOfFinset (S5 S10 : Finset 𝓩) :
    (T : PotentialTerm) → Multiset (ChargeSpectrum 𝓩)
```

### A.3. Showing `minimallyAllowsTermsOfFinset` has charges in given sets

> We show that every element of `minimallyAllowsTermsOfFinset S5 S10 T` is in `ofFinset S5 S10`.
> That is every element of `minimallyAllowsTermsOfFinset S5 S10 T` has charges
> in the sets `S5` and `S10`.

**`SuperSymmetry.SU5.ChargeSpectrum.mem_ofFinset_of_mem_minimallyAllowsTermOfFinset`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/OfFinset.lean#L296).

```lean
lemma mem_ofFinset_of_mem_minimallyAllowsTermOfFinset {S5 S10 : Finset 𝓩} {T : PotentialTerm}
    {x : ChargeSpectrum 𝓩} (hx : x ∈ minimallyAllowsTermsOfFinset S5 S10 T) :
    x ∈ ofFinset S5 S10
```

**`SuperSymmetry.SU5.ChargeSpectrum.minimallyAllowsTermOfFinset_subset_ofFinset`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/OfFinset.lean#L338).

```lean
lemma minimallyAllowsTermOfFinset_subset_ofFinset {S5 S10 : Finset 𝓩} {T : PotentialTerm} :
    minimallyAllowsTermsOfFinset S5 S10 T ⊆ (ofFinset S5 S10).val
```

## B. Proving the `minimallyAllowsTermsOfFinset` is set of charges which minimally allow a term

> We now prove that `minimallyAllowsTermsOfFinset` has the property
> that all charges spectra with charges in the sets `S5` and `S10`
> which minimally allow the potential term `T` are in
> `minimallyAllowsTermsOfFinset S5 S10 T`, and vice versa.

### B.1. An element of `minimallyAllowsTermsOfFinset` is of the form `allowsTermForm`

> We show that every element of `minimallyAllowsTermsOfFinset S5 S10 T` is of the form
> `allowsTermForm a b c T` for some `a`, `b` and `c`.

**`SuperSymmetry.SU5.ChargeSpectrum.eq_allowsTermForm_of_mem_minimallyAllowsTermOfFinset`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/OfFinset.lean#L361).

```lean
lemma eq_allowsTermForm_of_mem_minimallyAllowsTermOfFinset {S5 S10 : Finset 𝓩} {T : PotentialTerm}
    {x : ChargeSpectrum 𝓩} (hx : x ∈ minimallyAllowsTermsOfFinset S5 S10 T) :
    ∃ a b c, x = allowsTermForm a b c T
```

### B.2. Every element of `minimallyAllowsTermsOfFinset` allows the term

> We show that every element of `minimallyAllowsTermsOfFinset S5 S10 T` allows the term `T`.

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_of_mem_minimallyAllowsTermOfFinset`**, a lemma, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/OfFinset.lean#L434).

```lean
lemma allowsTerm_of_mem_minimallyAllowsTermOfFinset {S5 S10 : Finset 𝓩} {T : PotentialTerm}
    {x : ChargeSpectrum 𝓩} (hx : x ∈ minimallyAllowsTermsOfFinset S5 S10 T) :
    x.AllowsTerm T
```

### B.3. Every element of `minimallyAllowsTermsOfFinset` minimally allows the term

> We make the above condition stronger, showing that every element of
> `minimallyAllowsTermsOfFinset S5 S10 T` minimally allows the term `T`.

**`SuperSymmetry.SU5.ChargeSpectrum.minimallyAllowsTerm_of_mem_minimallyAllowsTermOfFinset`**, a lemma, [line 449](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/OfFinset.lean#L449).

```lean
lemma minimallyAllowsTerm_of_mem_minimallyAllowsTermOfFinset {S5 S10 : Finset 𝓩}
    {T : PotentialTerm} {x : ChargeSpectrum 𝓩}
    (hx : x ∈ minimallyAllowsTermsOfFinset S5 S10 T) :
    x.MinimallyAllowsTerm T
```

### B.4. Every charge spectra which minimally allows term is in `minimallyAllowsTermsOfFinset`

> We show that every charge spectra which minimally allows term `T` and has charges
> in the sets `S5` and `S10` is in `minimallyAllowsTermsOfFinset S5 S10 T`.

**`SuperSymmetry.SU5.ChargeSpectrum.mem_minimallyAllowsTermOfFinset_of_minimallyAllowsTerm`**, a lemma, [line 469](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/OfFinset.lean#L469).

```lean
lemma mem_minimallyAllowsTermOfFinset_of_minimallyAllowsTerm {S5 S10 : Finset 𝓩}
    {T : PotentialTerm} (x : ChargeSpectrum 𝓩) (h : x.MinimallyAllowsTerm T)
    (hx : x ∈ ofFinset S5 S10) :
    x ∈ minimallyAllowsTermsOfFinset S5 S10 T
```

### B.5. In `minimallyAllowsTermsOfFinset` iff minimally allowing term

> We now show the key result of this section, that a charge spectrum `x`
> is in `minimallyAllowsTermsOfFinset S5 S10 T` if and only if
> it minimally allows the term `T`, provided it is in `ofFinset S5 S10`.

**`SuperSymmetry.SU5.ChargeSpectrum.minimallyAllowsTerm_iff_mem_minimallyAllowsTermOfFinset`**, a lemma, [line 517](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/OfFinset.lean#L517).

```lean
lemma minimallyAllowsTerm_iff_mem_minimallyAllowsTermOfFinset
    {S5 S10 : Finset 𝓩} {T : PotentialTerm}
    {x : ChargeSpectrum 𝓩} (hx : x ∈ ofFinset S5 S10) :
    x.MinimallyAllowsTerm T ↔ x ∈ minimallyAllowsTermsOfFinset S5 S10 T
```

## C. Other properties of `minimallyAllowsTermsOfFinset`

> We show two other properties of `minimallyAllowsTermsOfFinset`.

### C.1. Monotonicity of `minimallyAllowsTermsOfFinset` in allowed sets of charges

**`SuperSymmetry.SU5.ChargeSpectrum.minimallyAllowsTermOfFinset_subset_of_subset`**, a lemma, [line 538](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/OfFinset.lean#L538).

```lean
lemma minimallyAllowsTermOfFinset_subset_of_subset {S5 S5' S10 S10' : Finset 𝓩} {T : PotentialTerm}
    (h5 : S5' ⊆ S5) (h10 : S10' ⊆ S10) :
    minimallyAllowsTermsOfFinset S5' S10' T ⊆ minimallyAllowsTermsOfFinset S5 S10 T
```

### C.2. Not phenomenologically constrained if in `minimallyAllowsTermsOfFinset` for topYukawa

> We show that every term which is in `minimallyAllowsTermsOfFinset S5 S10 topYukawa` is not
> phenomenologically constrained.

**`SuperSymmetry.SU5.ChargeSpectrum.not_isPhenoConstrained_of_minimallyAllowsTermsOfFinset_topYukawa`**, a lemma, [line 556](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/OfFinset.lean#L556).

```lean
lemma not_isPhenoConstrained_of_minimallyAllowsTermsOfFinset_topYukawa
    {S5 S10 : Finset 𝓩} {x : ChargeSpectrum 𝓩}
    (hx : x ∈ minimallyAllowsTermsOfFinset S5 S10 topYukawa) :
    ¬ x.IsPhenoConstrained
```

## Depends on

- [Charge spectrum which minimally allows terms](su5-chargespectrum-minimallyallowsterm-basic.md)
- [Pheno constrained charge spectra](su5-chargespectrum-phenoconstrained.md)

## Sources

- [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/OfFinset.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/OfFinset.lean)
