---
declaration: module
origin: cited
lean: SuperSymmetry.SU5.ChargeSpectrum.MinimallyAllowsTerm, SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_of_minimallyAllowsTerm, SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_of_has_minimallyAllowsTerm_subset, SuperSymmetry.SU5.ChargeSpectrum.minimallyAllowsTerm_iff_powerset_filter_eq, SuperSymmetry.SU5.ChargeSpectrum.minimallyAllowsTerm_iff_powerset_countP_eq_one, SuperSymmetry.SU5.ChargeSpectrum.subset_minimallyAllowsTerm_of_allowsTerm, SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_iff_subset_minimallyAllowsTerm, SuperSymmetry.SU5.ChargeSpectrum.card_le_degree_of_minimallyAllowsTerm
statement: formalized
proof: formalized
---

# Charge spectrum which minimally allows terms

The module `Physlib.Particles.SuperSymmetry.SU5.ChargeSpectrum.MinimallyAllowsTerm.Basic`, [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/Basic.lean): 11 declarations (1 instance with no name), 1 with a docstring.

## i. Overview

> We can say that a charge spectrum `x : ChargeSpectrum 𝓩` minimally allows a potential term
> `T : PotentialTerm` if it allows the term `T` and no strict subset of `x` allows `T`.
>
> That is to say, you need all of the charges in `x` to allow the term `T`.
>
> We show that any charge spectrum which allows `T` has a subset which minimally allows `T`.
>
> We show that every charge spectrum which minimally allows `T` is of the form
> `allowsTermForm a b c T` for some `a b c : 𝓩`, and the reverse is true for
> `T` not equal to `W1` or `W2`.

## ii. Key results

> - `MinimallyAllowsTerm` : Predicate on charge spectra which is true if the charge spectrum
>   minimally allows a potential term.
> - `allowsTerm_iff_subset_minimallyAllowsTerm` : A charge spectrum which allows a term
>   has a subset which minimally allows the term, and vice versa.
> - `eq_allowsTermForm_of_minimallyAllowsTerm` : Any charge spectrum which minimally allows a term
>   is of the form `allowsTermForm a b c T` for some `a b c : 𝓩`.

## iv. References

> * None.

## A. Charge spectra which minimally allow potential terms

> We define the predicate `MinimallyAllowsTerm` on charge spectra
> which is true if the charge spectrum allows a given potential term and no strict subset of
> it allows the term.
>
> We prove properties of charge spectra which minimally allow potential terms.

**`SuperSymmetry.SU5.ChargeSpectrum.MinimallyAllowsTerm`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/Basic.lean#L78).

> A charge spectrum `x : ChargeSpectrum 𝓩` is said to minimally allow
> the potential term `T` if it allows `T` and no strict subset of it allows `T`.

```lean
def MinimallyAllowsTerm (x : ChargeSpectrum 𝓩) (T : PotentialTerm) : Prop
```

### A.1. Decidability of `MinimallyAllowsTerm`

> We show that `MinimallyAllowsTerm` is decidable.

**An instance with no name**, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/Basic.lean#L88).

```lean
instance (x : ChargeSpectrum 𝓩) (T : PotentialTerm) : Decidable (x.MinimallyAllowsTerm T)
```

### A.2. A charge spectrum which minimally allows a term allows the term

> Somewhat trivially a charge spectrum which minimally allows the term does indeed allow the term.

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_of_minimallyAllowsTerm`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/Basic.lean#L101).

```lean
lemma allowsTerm_of_minimallyAllowsTerm (h : x.MinimallyAllowsTerm T) : x.AllowsTerm T
```

### A.3. Spectrum with a subset which minimally allows a term, allows the term

> If a charge spectrum `x` has a subset which minimally allows a term `T`, then `x` allows `T`.

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_of_has_minimallyAllowsTerm_subset`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/Basic.lean#L113).

```lean
lemma allowsTerm_of_has_minimallyAllowsTerm_subset
    (hx : ∃ y ∈ powerset x, y.MinimallyAllowsTerm T) : x.AllowsTerm T
```

### A.4. Minimally allows term iff only member of powerset allowing term

> A charge spectrum `x` minimally allows a term `T` if and only if the only member of its
> own powerset which allows `T` is itself.

**`SuperSymmetry.SU5.ChargeSpectrum.minimallyAllowsTerm_iff_powerset_filter_eq`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/Basic.lean#L129).

```lean
lemma minimallyAllowsTerm_iff_powerset_filter_eq :
    x.MinimallyAllowsTerm T ↔ x.powerset.filter (fun y => y.AllowsTerm T) = {x}
```

### A.5. Minimally allows term iff powerset allowing term has cardinal one

> A charge spectrum `x` minimally allows a term `T` if and only the
> the number of members of its powerset which allow `T` is one.

**`SuperSymmetry.SU5.ChargeSpectrum.minimallyAllowsTerm_iff_powerset_countP_eq_one`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/Basic.lean#L165).

```lean
lemma minimallyAllowsTerm_iff_powerset_countP_eq_one :
    x.MinimallyAllowsTerm T ↔ x.powerset.val.countP (fun y => y.AllowsTerm T) = 1
```

### A.6. A charge spectrum which allows a term has a subset which minimally allows the term

> If a charge spectrum `x` allows a term `T`, then it has a subset which minimally allows `T`.

**`SuperSymmetry.SU5.ChargeSpectrum.subset_minimallyAllowsTerm_of_allowsTerm`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/Basic.lean#L199).

```lean
lemma subset_minimallyAllowsTerm_of_allowsTerm
    (hx : x.AllowsTerm T) : ∃ y ∈ powerset x, y.MinimallyAllowsTerm T
```

### A.7. A charge spectrum allows a term iff it has a subset which minimally allows the term

> We combine results above to show that a charge spectrum allows a term if and only if it has a subset
> which minimally allows the term.

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_iff_subset_minimallyAllowsTerm`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/Basic.lean#L226).

```lean
lemma allowsTerm_iff_subset_minimallyAllowsTerm :
    x.AllowsTerm T ↔ ∃ y ∈ powerset x, y.MinimallyAllowsTerm T
```

### A.8. Cardinality of spectrum which minimally allows term is at most degree of term

> We show that the cardinality of a charge spectrum which minimally allows a term `T` is at most the
> degree of `T`.

**`SuperSymmetry.SU5.ChargeSpectrum.card_le_degree_of_minimallyAllowsTerm`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/Basic.lean#L240).

```lean
lemma card_le_degree_of_minimallyAllowsTerm (h : x.MinimallyAllowsTerm T) :
    x.card ≤ T.degree
```

## B. Relation between `MinimallyAllowsTerm` and `allowsTermForm`

> We now relate the predicate `MinimallyAllowsTerm` to charge spectra of the form
> `allowsTermForm a b c T`.

### B.1. A charge spectrum which minimally allows a term is of the form `allowsTermForm a b c T`

> We show that any charge spectrum which minimally allows a term `T` is of the form
> `allowsTermForm a b c T` for some `a b c : 𝓩`.

**`SuperSymmetry.SU5.ChargeSpectrum.eq_allowsTermForm_of_minimallyAllowsTerm`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/Basic.lean#L270).

```lean
lemma eq_allowsTermForm_of_minimallyAllowsTerm (h1 : x.MinimallyAllowsTerm T) :
    ∃ a b c, x = allowsTermForm a b c T
```

### B.2. `allowsTermForm a b c T` minimally allows `T` if `T` is not `W1` or `W2`

> We show that charge spectra of the form `allowsTermForm a b c T` minimally allow `T` provided that
> `T` is not one of `W1` or `W2`.

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTermForm_minimallyAllowsTerm`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/Basic.lean#L291).

```lean
lemma allowsTermForm_minimallyAllowsTerm {a b c : 𝓩} {T : PotentialTerm}
    (hT : T ≠ W1 ∧ T ≠ W2) :
    MinimallyAllowsTerm (allowsTermForm a b c T) T
```

## Depends on

- [Charges allowing terms](../part-01/su5-chargespectrum-allowsterm.md)

## Sources

- [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/MinimallyAllowsTerm/Basic.lean)
