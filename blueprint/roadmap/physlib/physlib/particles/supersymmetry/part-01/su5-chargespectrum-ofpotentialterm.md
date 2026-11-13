---
declaration: module
origin: cited
lean: SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm, SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm_mono, SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm_empty, SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm', SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm'_μ_finset, SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm'_β_finset, SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm'_W2_finset, SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm'_W3_finset
statement: formalized
proof: formalized
---

# Charges associated with a potential term

The module `Physlib.Particles.SuperSymmetry.SU5.ChargeSpectrum.OfPotentialTerm`, [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean): 17 declarations, 2 with a docstring.

## i. Overview

> In this module we give the multiset of charges associated with a given type of potential term,
> given a charge spectrum.
>
> We will define two versions of this, one based on the underlying fields on the
> potentials, and the charges that they carry, and one more explicit version which
> is faster to compute with. The former is `ofPotentialTerm`, and the latter is
> `ofPotentialTerm'`.
>
> We will show that these two multisets have the same elements.

## ii. Key results

> - `ofPotentialTerm` : The multiset of charges associated with a potential term,
>   defined in terms of the fields making up that potential term, given a charge spectrum.
> - `ofPotentialTerm'` : The multiset of charges associated with a potential term,
>   defined explicitly, given a charge spectrum.

## iv. References

> * None.

## A. Charges of a potential term from field labels

> We first define `ofPotentialTerm`, and prover properties of it.
> This is slow to compute in practice.

**`SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean#L74).

> Given a charge spectrum `x : ChargeSpectrum 𝓩` associated to the representations, and a
> potential term `T`, the charges associated with instances of that potential term.

```lean
def ofPotentialTerm (x : ChargeSpectrum 𝓩) (T : PotentialTerm) : Multiset 𝓩
```

### A.1. Monotonicity of `ofPotentialTerm`

> We show that `ofPotentialTerm` is monotone in its charge spectrum argument.
> That is if `x ⊆ y` then `ofPotentialTerm x T ⊆ ofPotentialTerm y T`.

**`SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm_mono`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean#L87).

```lean
lemma ofPotentialTerm_mono {x y : ChargeSpectrum 𝓩} (h : x ⊆ y) (T : PotentialTerm) :
    x.ofPotentialTerm T ⊆ y.ofPotentialTerm T
```

### A.2. Charges of potential terms for the empty charge spectrum

> For the empty charge spectrum, the charges associated with any potential term is empty.

**`SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm_empty`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean#L111).

```lean
lemma ofPotentialTerm_empty (T : PotentialTerm) :
    ofPotentialTerm (∅ : ChargeSpectrum 𝓩) T = ∅
```

## B. Explicit construction of charges of a potential term

> We now turn to a more explicit construction of the charges associated with a potential term.
> This is faster to compute with, but less obviously connected to the underlying
> fields.

**`SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm'`**, a def, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean#L133).

> Given a charges `x : ChargeSpectrum` associated to the representations, and a potential
> term `T`, the charges associated with instances of that potential term.
>
> This is a more explicit form of `PotentialTerm`, which has the benefit that
> it is quick with `decide`, but it is not defined based on more fundamental
> concepts, like `ofPotentialTerm` is.

```lean
def ofPotentialTerm' (y : ChargeSpectrum 𝓩) (T : PotentialTerm) : Multiset 𝓩
```

### B.1. Explicit multisets for `ofPotentialTerm'`

> For each potential term, we give an explicit form of the multiset `ofPotentialTerm'`.

**`SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm'_μ_finset`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean#L188).

```lean
lemma ofPotentialTerm'_μ_finset {x : ChargeSpectrum 𝓩} :
    x.ofPotentialTerm' μ =
    (x.qHd.toFinset.product <| x.qHu.toFinset).val.map (fun x => x.1 - x.2)
```

**`SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm'_β_finset`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean#L193).

```lean
lemma ofPotentialTerm'_β_finset {x : ChargeSpectrum 𝓩} :
    x.ofPotentialTerm' β =
    (x.qHu.toFinset.product <| x.Q5).val.map (fun x => - x.1 + x.2)
```

**`SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm'_W2_finset`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean#L198).

```lean
lemma ofPotentialTerm'_W2_finset {x : ChargeSpectrum 𝓩} :
    x.ofPotentialTerm' W2 = (x.qHd.toFinset.product <|
      x.Q10.product <| x.Q10.product <| x.Q10).val.map
    (fun x => x.1 + x.2.1 + x.2.2.1 + x.2.2.2)
```

**`SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm'_W3_finset`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean#L204).

```lean
lemma ofPotentialTerm'_W3_finset {x : ChargeSpectrum 𝓩} :
    x.ofPotentialTerm' W3 = (x.qHu.toFinset.product <| x.Q5.product <| x.Q5).val.map
    (fun x => -x.1 - x.1 + x.2.1 + x.2.2)
```

**`SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm'_W4_finset`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean#L209).

```lean
lemma ofPotentialTerm'_W4_finset {x : ChargeSpectrum 𝓩} :
    x.ofPotentialTerm' W4 = (x.qHd.toFinset.product <|
      x.qHu.toFinset.product <| x.Q5).val.map
    (fun x => x.1 - x.2.1 - x.2.1 + x.2.2)
```

**`SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm'_K2_finset`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean#L215).

```lean
lemma ofPotentialTerm'_K2_finset {x : ChargeSpectrum 𝓩} :
    x.ofPotentialTerm' K2 = (x.qHd.toFinset.product <|
      x.qHu.toFinset.product <| x.Q10).val.map
    (fun x => x.1 + x.2.1 + x.2.2)
```

**`SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm'_topYukawa_finset`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean#L221).

```lean
lemma ofPotentialTerm'_topYukawa_finset {x : ChargeSpectrum 𝓩} :
    x.ofPotentialTerm' topYukawa = (x.qHu.toFinset.product <|
      x.Q10.product <| x.Q10).val.map
    (fun x => -x.1 + x.2.1 + x.2.2)
```

**`SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm'_bottomYukawa_finset`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean#L227).

```lean
lemma ofPotentialTerm'_bottomYukawa_finset {x : ChargeSpectrum 𝓩} :
    x.ofPotentialTerm' bottomYukawa = (x.1.toFinset.product <|
      x.Q5.product <| x.Q10).val.map
    (fun x => x.1 + x.2.1 + x.2.2)
```

### B.2. `ofPotentialTerm'` on the empty charge spectrum

> We show that for the empty charge spectrum, the charges associated with any potential term is empty,
> as defined through `ofPotentialTerm'`.

**`SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm'_empty`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean#L243).

```lean
lemma ofPotentialTerm'_empty (T : PotentialTerm) :
    ofPotentialTerm' (∅ : ChargeSpectrum 𝓩) T = ∅
```

## C. Relation between two constructions of charges of potential terms

> We now give the relation between `ofPotentialTerm` and `ofPotentialTerm'`.
> We show that they have the same elements, by showing that they are subsets of each other.
>
> The prove of some of these results are rather long since they involve explicit
> case analysis for each potential term, due to the nature of the definition
> of `ofPotentialTerm'`.

### C.1. Showing that `ofPotentialTerm` is a subset of `ofPotentialTerm'`

> We first show that `ofPotentialTerm` is a subset of `ofPotentialTerm'`.

**`SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm_subset_ofPotentialTerm'`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean#L269).

```lean
lemma ofPotentialTerm_subset_ofPotentialTerm' {x : ChargeSpectrum 𝓩} (T : PotentialTerm) :
    x.ofPotentialTerm T ⊆ x.ofPotentialTerm' T
```

### C.2. Showing that `ofPotentialTerm'` is a subset of `ofPotentialTerm`

> We now show the other direction of the subset relation, that
> `ofPotentialTerm'` is a subset of `ofPotentialTerm`.

**`SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm'_subset_ofPotentialTerm`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean#L313).

```lean
lemma ofPotentialTerm'_subset_ofPotentialTerm [DecidableEq 𝓩]
    {x : ChargeSpectrum 𝓩} (T : PotentialTerm) :
    x.ofPotentialTerm' T ⊆ x.ofPotentialTerm T
```

### C.3. Equivalence of elements of `ofPotentialTerm` and `ofPotentialTerm'`

> We now show that a charge is in `ofPotentialTerm` if and only if it is in
> `ofPotentialTerm'`. I.e. their underlying finite sets are equal.
> We do not say anything about the multiplicity of elements within the multisets,
> which is not important for us.

**`SuperSymmetry.SU5.ChargeSpectrum.mem_ofPotentialTerm_iff_mem_ofPotentialTerm`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean#L381).

```lean
lemma mem_ofPotentialTerm_iff_mem_ofPotentialTerm [DecidableEq 𝓩]
    {T : PotentialTerm} {n : 𝓩} {y : ChargeSpectrum 𝓩} :
    n ∈ y.ofPotentialTerm T ↔ n ∈ y.ofPotentialTerm' T
```

### C.4. Induced monotonicity of `ofPotentialTerm'`

> Due to the equivalence of elements of `ofPotentialTerm` and `ofPotentialTerm'`,
> we can now also show that `ofPotentialTerm'` is monotone in its charge spectrum argument.

**`SuperSymmetry.SU5.ChargeSpectrum.ofPotentialTerm'_mono`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean#L397).

```lean
lemma ofPotentialTerm'_mono [DecidableEq 𝓩] {x y : ChargeSpectrum 𝓩}
    (h : x ⊆ y) (T : PotentialTerm) :
    x.ofPotentialTerm' T ⊆ y.ofPotentialTerm' T
```

## Depends on

- [Charges associated with a field label](su5-chargespectrum-offieldlabel.md)
- [Potential of the SU(5) + U(1) GUT](su5-potential.md)

## Sources

- [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/OfPotentialTerm.lean)
