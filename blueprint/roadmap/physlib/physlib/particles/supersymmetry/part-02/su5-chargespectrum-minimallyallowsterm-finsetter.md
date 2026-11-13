---
declaration: module
origin: cited
lean: SuperSymmetry.SU5.ChargeSpectrum.MinimallyAllowsFinsetTerms, SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_of_minimallyAllowsFinsetTerms, SuperSymmetry.SU5.ChargeSpectrum.minimallyAllowsFinsetTerms_singleton, SuperSymmetry.SU5.ChargeSpectrum.minTopBottom, SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_topYukawa_of_mem_minTopBottom, SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_bottomYukawa_of_mem_minTopBottom, SuperSymmetry.SU5.ChargeSpectrum.mem_minTopBottom_of_minimallyAllowsFinsetTerms
statement: formalized
proof: formalized
---

# Minimally allows a set of terms

The module `Physlib.Particles.SuperSymmetry.SU5.ChargeSpectrum.MinimallyAllowsTerm.FinsetTerms`, [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/FinsetTerms.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/FinsetTerms.lean): 8 declarations (1 instance with no name), 2 with a docstring.

## i. Overview

> In this module we consider those charge spectra which minimally allow a
> finite set of potential terms.
> That is, they those charge spectra which allow each term in the set, but no proper subset of the
> charge spectra allows each term in that set.
>
> We have special focus on those charge spectra which minimally allow a top and bottom Yukawa term.

## ii. Key results

> - `MinimallyAllowsFinsetTerms`: the proposition that a charge spectrum
>   minimally allows a given finite set of potential terms.
> - `minTopBottom`: a finite set of charge spectra which contains every
>   charge spectrum which minimally allows a top and bottom Yukawa term, given
>   finite sets of possible `5`-bar and `10` charges.

## iv. References

> * None.

## A. Charge spectra which minimally allow a finite set of potential terms

> We start by defining the proposition that a charge spectrum minimally allows a
> finite set of potential terms, and prove some basic properties there of.

### A.1. `MinimallyAllowsFinsetTerms`: Prop of minimally allowing a finset of potential terms

**`SuperSymmetry.SU5.ChargeSpectrum.MinimallyAllowsFinsetTerms`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/FinsetTerms.lean#L76).

> A collection of charge spectra is said to minimally allow
> a finite set of potential terms `Ts` if it allows
> all terms in `Ts` and no strict subset of it allows all terms in `Ts`.

```lean
def MinimallyAllowsFinsetTerms (x : ChargeSpectrum 𝓩) (Ts : Finset PotentialTerm) : Prop
```

### A.2. The prop `MinimallyAllowsFinsetTerms` is decidable

**An instance with no name**, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/FinsetTerms.lean#L85).

```lean
instance (x : ChargeSpectrum 𝓩) (Ts : Finset PotentialTerm) :
    Decidable (x.MinimallyAllowsFinsetTerms Ts)
```

### A.3. Every element of `MinimallyAllowsFinsetTerms` allows each term in the finset

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_of_minimallyAllowsFinsetTerms`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/FinsetTerms.lean#L97).

```lean
lemma allowsTerm_of_minimallyAllowsFinsetTerms {T : PotentialTerm}
    (h : x.MinimallyAllowsFinsetTerms Ts) (hT : T ∈ Ts) : x.AllowsTerm T
```

### A.4. `MinimallyAllowsFinsetTerms` for the singleton set is equivalent to `MinimallyAllowsTerm`

**`SuperSymmetry.SU5.ChargeSpectrum.minimallyAllowsFinsetTerms_singleton`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/FinsetTerms.lean#L108).

```lean
lemma minimallyAllowsFinsetTerms_singleton {T : PotentialTerm} :
    x.MinimallyAllowsFinsetTerms {T} ↔ x.MinimallyAllowsTerm T
```

## B. Minimally allowing the top and bottom Yukawa

> We now consider the special case of those charge spectra which minimally allow
> a top and bottom Yukawa term.
>
> We construct a finite set of such charge spectra given finite sets of
> possible `5`-bar and `10` charges which contains every charge
> spectrum which minimally allows a top and bottom Yukawa term.

### B.1. Finset of charge spectra containing those which minimally allow top and bottom Yukawa

> Here we define `minTopBottom` in a way which is computationally efficient.

**`SuperSymmetry.SU5.ChargeSpectrum.minTopBottom`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/FinsetTerms.lean#L135).

> The set of charges of the form `(qHd, qHu, {q5}, {-qHd-q5, q10, qHu - q10})`
> This includes every charge which minimally allows for the top and bottom Yukawas.

```lean
def minTopBottom (S5 S10 : Finset 𝓩) : Multiset (ChargeSpectrum 𝓩)
```

### B.2. Every element of `minTopBottom` allows a top Yukawa

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_topYukawa_of_mem_minTopBottom`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/FinsetTerms.lean#L145).

```lean
lemma allowsTerm_topYukawa_of_mem_minTopBottom {S5 S10 : Finset 𝓩}
    {x : ChargeSpectrum 𝓩} (h : x ∈ minTopBottom S5 S10) :
    x.AllowsTerm topYukawa
```

### B.3. Every element of `minTopBottom` allows a bottom Yukawa

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_bottomYukawa_of_mem_minTopBottom`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/FinsetTerms.lean#L159).

```lean
lemma allowsTerm_bottomYukawa_of_mem_minTopBottom {S5 S10 : Finset 𝓩}
    {x : ChargeSpectrum 𝓩} (h : x ∈ minTopBottom S5 S10) :
    x.AllowsTerm bottomYukawa
```

### B.4. Every charge spectrum minimally allowing a top and bottom Yukawa in `minTopBottom`

**`SuperSymmetry.SU5.ChargeSpectrum.mem_minTopBottom_of_minimallyAllowsFinsetTerms`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/FinsetTerms.lean#L172).

```lean
lemma mem_minTopBottom_of_minimallyAllowsFinsetTerms
    {x : ChargeSpectrum 𝓩} {S5 S10 : Finset 𝓩}
    (h : x.MinimallyAllowsFinsetTerms {topYukawa, bottomYukawa})
    (hx : x ∈ ofFinset S5 S10) :
    x ∈ minTopBottom S5 S10
```

## Depends on

- [Charge spectrum which minimally allows terms](su5-chargespectrum-minimallyallowsterm-basic.md)

## Sources

- [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/FinsetTerms.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/FinsetTerms.lean)
