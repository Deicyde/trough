---
declaration: module
origin: cited
lean: SuperSymmetry.SU5.ChargeSpectrum.AllowsTerm, SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_iff_zero_mem_ofPotentialTerm', SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_mono, SuperSymmetry.SU5.ChargeSpectrum.allowsTermForm, SuperSymmetry.SU5.ChargeSpectrum.allowsTermForm_allowsTerm, SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_of_eq_allowsTermForm, SuperSymmetry.SU5.ChargeSpectrum.allowsTermForm_eq_of_subset, SuperSymmetry.SU5.ChargeSpectrum.allowsTermForm_card_le_degree
statement: formalized
proof: formalized
---

# Charges allowing terms

The module `Physlib.Particles.SuperSymmetry.SU5.ChargeSpectrum.AllowsTerm`, [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean): 22 declarations (3 instances with no name), 5 with a docstring.

## i. Overview

> To each charge spectrum `x : ChargeSpectrum 𝓩` we say it
> allows the potential term `T : PotentialTerm`, if one of the charges associated with that
> potential term is zero.
>
> What this means, is that there is a choice of charges from the charge spectrum `x` that
> can be assigned to the fields in the potential term `T` such that the total charge is zero,
> and therefore that the term is present in the potential. The presence of
> absence of certain terms is of phenomenological importance.
>
> This concept is captured by the proposition `AllowsTerm`.
>
> In addition to this, for each potential term `T`, we define a function `allowsTermForm`
> which takes three elements of `𝓩`, `a`, `b`, and `c` and returns a charge spectrum
> which allows the term `T`. We will show in `allowsTerm_iff_subset_allowsTermForm`
> that any charge spectrum that allows a term `T` has a subset which can be expressed as
> `allowsTermForm a b c T` for some `a`, `b`, and `c`.
>
> We also define the propositions `AllowsTermQ5 x q5 T` and `AllowsTermQ10 x q10 T`
> which correspond to the condition that adding a charge `q5` to the `Q5` charges of
> the charge spectrum `x`, or adding a charge `q10` to the `Q10` charges of the
> charge spectrum `x`, leads to a zero charge in the charges of potential term `T`.

## ii. Key results

> - `AllowsTerm` : The proposition that a charge spectrum allows a potential term.
> - `allowsTermForm` : A function which for each potential term `T` and three charges
>   `a`, `b`, and `c` returns a charge spectrum which allows the term `T`,
>   and such that any charge spectrum allowing `T` has a subset of this form.
> - `AllowsTermQ5` : The proposition that adding a charge `q5` to the `Q5` charges
>   of a charge spectrum `x` allows the potential term `T` due to the addition of that charge.
> - `AllowsTermQ10` : The proposition that adding a charge `q10` to the `Q10` charges
>   of a charge spectrum `x` allows the potential term `T` due to the addition of that charge.

## iv. References

> * None.

## A. Charge spectrums allowing potential terms

> We first define the proposition `AllowsTerm`, which for a charge spectrum `x : ChargeSpectrum 𝓩`
> and a potential term `T : PotentialTerm`, is true if the zero charge is in the set of
> charges associated with that potential term.
>
> That is, if there is some choice of representations present in the theory which will allow that
> potential term via symmetry.

**`SuperSymmetry.SU5.ChargeSpectrum.AllowsTerm`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L101).

> The charge spectrum of representations `x : ChargeSpectrum 𝓩` allows a potential term
> `T : PotentialTerm`
> if the zero charge is in the set of charges associated with that potential term.

```lean
def AllowsTerm (x : ChargeSpectrum 𝓩) (T : PotentialTerm) : Prop
```

### A.1. Decidability of `AllowsTerm`

> We define the decidability of `AllowsTerm` through `ofPotentialTerm'` rather than
> `ofPotentialTerm` due to the speed of the former compared to the latter.

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_iff_zero_mem_ofPotentialTerm'`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L112).

```lean
lemma allowsTerm_iff_zero_mem_ofPotentialTerm' [DecidableEq 𝓩]
    {x : ChargeSpectrum 𝓩} {T : PotentialTerm} :
    x.AllowsTerm T ↔ 0 ∈ x.ofPotentialTerm' T
```

**An instance with no name**, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L117).

```lean
instance [DecidableEq 𝓩] (x : ChargeSpectrum 𝓩) (T : PotentialTerm) : Decidable (x.AllowsTerm T)
```

### A.2. Monotonicity of `AllowsTerm`

> The proposition `AllowsTerm` is monotone in its charge spectrum argument.
> That is if a charge spectrum `y` is a subset of a charge spectrum `x`,
> and `y` allows a potential term `T`, then `x` also allows that potential term `T`.

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_mono`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L130).

```lean
lemma allowsTerm_mono {T : PotentialTerm} {y x : ChargeSpectrum 𝓩}
    (h : y ⊆ x) (hy : y.AllowsTerm T) : x.AllowsTerm T
```

## B. Forms of charges which allow potential terms

> We now define the function `allowsTermForm` which for each potential term `T`
> and three charges `a`, `b`, and `c` returns a charge spectrum which allows the term `T`.
>
> These charges are in a minimal form, in the sense that any charge spectrum allowing `T`
> has a subset of this form.

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTermForm`**, a def, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L151).

> A element of `Charges` from three integers `a b c : ℤ` for a given potential term `T`.
> Defined such that `allowsTermForm a b c T` always allows the potential term `T`,
> and if any over charge `x` allows `T` then it is due to a subset of the form
> `allowsTermForm a b c T`.

```lean
def allowsTermForm (a b c : 𝓩) : (T : PotentialTerm) → ChargeSpectrum 𝓩
```

### B.1. `allowsTermForm` allows the potential term

> Any charge spectrum of the form `allowsTermForm a b c T` allows the potential term `T`.

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTermForm_allowsTerm`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L173).

> The charge spectrum `allowsTermForm a b c T` allows the potential term `T`.

```lean
lemma allowsTermForm_allowsTerm {a b c : 𝓩} {T : PotentialTerm} :
    (allowsTermForm a b c T).AllowsTerm T
```

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_of_eq_allowsTermForm`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L191).

```lean
lemma allowsTerm_of_eq_allowsTermForm {T : PotentialTerm}
    (x : ChargeSpectrum 𝓩) (h : ∃ a b c, x = allowsTermForm a b c T) :
    x.AllowsTerm T
```

### B.2. Subset relations for `allowsTermForm`

> For any potential term `T` except for `W¹ᵢⱼₖₗ 10ⁱ 10ʲ 10ᵏ 5̄Mˡ` or `W²ᵢⱼₖ 10ⁱ 10ʲ 10ᵏ 5̄Hd`,
> a charge spectrum `allowsTermForm a b c T` is a subset of another charge spectrum
> `allowsTermForm a' b' c' T` if they are equal.
>
> The reason this does not work for `W1` an `W2` is due to the presence of three
> charges in the 10d representation.

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTermForm_eq_of_subset`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L211).

```lean
lemma allowsTermForm_eq_of_subset {a b c a' b' c' : 𝓩} {T : PotentialTerm}
    (h : allowsTermForm a b c T ⊆ allowsTermForm a' b' c' T) (hT : T ≠ W1 ∧ T ≠ W2) :
    allowsTermForm a b c T = allowsTermForm a' b' c' T
```

### B.3. Card of `allowsTermForm`

> The cardinality of the charge spectrum `allowsTermForm a b c T` is always
> less than or equal to the degree of the potential term `T`.

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTermForm_card_le_degree`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L245).

```lean
lemma allowsTermForm_card_le_degree {a b c : 𝓩} {T : PotentialTerm} :
    (allowsTermForm a b c T).card ≤ T.degree
```

### B.4. If `AllowsTerm` then subset equal to `allowsTermForm a b c T`

> We now show one of the more important properties of `allowsTermForm`.
> Namely that if a charge spectrum `x`
> allows a potential term `T`, then there exists charges `a`, `b`, and `c` such that
> `allowsTermForm a b c T ⊆ x`.
>
> The proof of this result is rather long, relying on case-by-case analysis of each
> of the potential terms of interest.

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTermForm_subset_allowsTerm_of_allowsTerm`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L277).

```lean
lemma allowsTermForm_subset_allowsTerm_of_allowsTerm {T : PotentialTerm} {x : ChargeSpectrum 𝓩}
    (h : x.AllowsTerm T) :
    ∃ a b c, allowsTermForm a b c T ⊆ x ∧ (allowsTermForm a b c T).AllowsTerm T
```

### B.5. `AllowsTerm` if and only if subset equal to `allowsTermForm a b c T`

> We now lift the previous result to show that a charge spectrum `x`
> allows a potential term `T` if and only if there exists charges `a`, `b`, and `c` such that
> `allowsTermForm a b c T ⊆ x`.
>
> Given what has already been shown, this result is now trivial.

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_iff_subset_allowsTermForm`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L381).

```lean
lemma allowsTerm_iff_subset_allowsTermForm {T : PotentialTerm} {x : ChargeSpectrum 𝓩} :
    x.AllowsTerm T ↔ ∃ a b c, allowsTermForm a b c T ⊆ x
```

### B.6. Cardinality of subset allowing potential term

> We show that if a charge spectrum `x` allows a potential term `T`,
> then there exists a subset of `x` which allows `T` and whose cardinality is less than or equal
> to the degree of `T`.
>
> This follows from the fact that `allowsTermForm a b c T` always has cardinality
> less than or equal to the degree of `T`.

**`SuperSymmetry.SU5.ChargeSpectrum.subset_card_le_degree_allowsTerm_of_allowsTerm`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L400).

```lean
lemma subset_card_le_degree_allowsTerm_of_allowsTerm {T : PotentialTerm} {x : ChargeSpectrum 𝓩}
    (h : x.AllowsTerm T) : ∃ y ∈ x.powerset, y.card ≤ T.degree ∧ y.AllowsTerm T
```

## C. Allowing a potential term by insertion of a `Q5` charge

> We now study what happens when we add a charge `q5` to the `Q5` charges of a charge spectrum `x`.
> We define the proposition `AllowsTermQ5 x q5 T` which is true if adding the charge `q5`
> to the `Q5` charges of `x` allows the potential term `T` due to the addition of that charge.
>
> We prove a number of properties of this proposition, including its relation
> to `AllowsTerm` and its decidability.

**`SuperSymmetry.SU5.ChargeSpectrum.AllowsTermQ5`**, a def, [line 420](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L420).

> The proposition for which says, given a charge `x` adding a charge `q5` permits the
> existence of a potential term `T` due to the addition of that charge.

```lean
def AllowsTermQ5 (x : ChargeSpectrum 𝓩) (q5 : 𝓩) (T : PotentialTerm) : Prop
```

### C.1. Decidability of `AllowsTermQ5`

> We show that if the type `𝓩` has decidable equality, then the proposition
> `AllowsTermQ5 x q5 T` is decidable for any charge spectrum `x`, charge `q5`, and
> potential term `T`.

**An instance with no name**, [line 457](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L457).

```lean
instance (x : ChargeSpectrum 𝓩) (q5 : 𝓩) (T : PotentialTerm) :
    Decidable (AllowsTermQ5 x q5 T)
```

### C.2. AllowsTermQ5 or AllowsTerm from AllowsTerm with inserted of `Q5` charge

> We show that if a charge spectrum `x` with an inserted charge `q5`
> allows a potential term `T`, then either the charge spectrum `x`
> allows that potential term `T` *due to* the addition of that charge,
> or the charge spectrum `x` already allows that potential term `T`.

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTermQ5_or_allowsTerm_of_allowsTerm_insertQ5`**, a lemma, [line 506](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L506).

```lean
lemma allowsTermQ5_or_allowsTerm_of_allowsTerm_insertQ5 {qHd qHu : Option 𝓩}
    {Q5 Q10: Finset 𝓩} {q5 : 𝓩} (T : PotentialTerm)
    (h : AllowsTerm ⟨qHd, qHu, insert q5 Q5, Q10⟩ T) :
    AllowsTermQ5 ⟨qHd, qHu, Q5, Q10⟩ q5 T ∨
    AllowsTerm ⟨qHd, qHu, Q5, Q10⟩ T
```

### C.3. AllowsTerm with inserted of `Q5` charge from AllowsTermQ5

> We show that if a charge spectrum `x` allows a potential term `T`
> *due to* the addition of a charge `q5`, then the charge spectrum `x` with that charge inserted
> allows that potential term `T`.

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_insertQ5_of_allowsTermQ5`**, a lemma, [line 613](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L613).

```lean
lemma allowsTerm_insertQ5_of_allowsTermQ5 {qHd qHu : Option 𝓩}
    {Q5 Q10: Finset 𝓩} {q5 : 𝓩} (T : PotentialTerm)
    (h : AllowsTermQ5 ⟨qHd, qHu, Q5, Q10⟩ q5 T) :
    AllowsTerm ⟨qHd, qHu, insert q5 Q5, Q10⟩ T
```

### C.4. AllowsTerm with inserted of `Q5` charge iff AllowsTermQ5 or AllowsTerm

> We show that the charge spectrum `x` with that charge inserted
> allows that potential term `T` if and only if either the charge spectrum `x`
> allows that potential term `T` *due to* the addition of that charge,
> or the charge spectrum `x` already allows that potential term `T`.

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_insertQ5_iff_allowsTermQ5`**, a lemma, [line 685](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L685).

```lean
lemma allowsTerm_insertQ5_iff_allowsTermQ5 {qHd qHu : Option 𝓩}
    {Q5 Q10: Finset 𝓩} {q5 : 𝓩} (T : PotentialTerm) :
    AllowsTerm ⟨qHd, qHu, insert q5 Q5, Q10⟩ T ↔
    AllowsTermQ5 ⟨qHd, qHu, Q5, Q10⟩ q5 T ∨
    AllowsTerm ⟨qHd, qHu, Q5, Q10⟩ T
```

## D. Allowing a potential term by insertion of a `Q10` charge

> We now replicate the previous section, but for the insertion of a `Q10` charge, rather
> than a `Q5` charge.
>
> We study what happens when we add a charge `q10` to the `Q10` charges of a charge spectrum `x`.
> We define the proposition `AllowsTermQ10 x q10 T` which is true if adding the charge `q10`
> to the `Q10` charges of `x` allows the potential term `T` due to the addition of that charge.
>
> We prove a number of properties of this proposition, including its relation
> to `AllowsTerm` and its decidability.

**`SuperSymmetry.SU5.ChargeSpectrum.AllowsTermQ10`**, a def, [line 713](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L713).

> The proposition for which says, given a charge `x` adding a charge `q5` permits the
> existence of a potential term `T` due to the addition of that charge.

```lean
def AllowsTermQ10 (x : ChargeSpectrum 𝓩) (q10 : 𝓩) (T : PotentialTerm) : Prop
```

### D.1. Decidability of `AllowsTermQ5`

> We show that if the type `𝓩` has decidable equality, then the proposition
> `AllowsTermQ10 x q10 T` is decidable for any charge spectrum `x`, charge `q10`, and
> potential term `T`.

**An instance with no name**, [line 752](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L752).

```lean
instance (x : ChargeSpectrum 𝓩) (q10 : 𝓩) (T : PotentialTerm) :
    Decidable (AllowsTermQ10 x q10 T)
```

### D.2. AllowsTermQ10 or AllowsTerm from AllowsTerm with inserted of `Q10` charge

> We show that if a charge spectrum `x` with an inserted charge `q10`
> allows a potential term `T`, then either the charge spectrum `x`
> allows that potential term `T` *due to* the addition of that charge,
> or the charge spectrum `x` already allows that potential term `T`.

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTermQ10_or_allowsTerm_of_allowsTerm_insertQ10`**, a lemma, [line 804](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L804).

```lean
lemma allowsTermQ10_or_allowsTerm_of_allowsTerm_insertQ10 {qHd qHu : Option 𝓩}
    {Q5 Q10: Finset 𝓩} {q10 : 𝓩} (T : PotentialTerm)
    (h : AllowsTerm ⟨qHd, qHu, Q5, insert q10 Q10⟩ T) :
    AllowsTermQ10 ⟨qHd, qHu, Q5, Q10⟩ q10 T ∨
    AllowsTerm ⟨qHd, qHu, Q5, Q10⟩ T
```

### D.3. AllowsTerm with inserted of `Q10` charge from AllowsTermQ5

> We show that if a charge spectrum `x` allows a potential term `T`
> *due to* the addition of a charge `q10`, then the charge spectrum `x` with that charge inserted
> allows that potential term `T`.

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_insertQ10_of_allowsTermQ10`**, a lemma, [line 946](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L946).

```lean
lemma allowsTerm_insertQ10_of_allowsTermQ10 {qHd qHu : Option 𝓩}
    {Q5 Q10: Finset 𝓩} {q10 : 𝓩} (T : PotentialTerm)
    (h : AllowsTermQ10 ⟨qHd, qHu, Q5, Q10⟩ q10 T) :
    AllowsTerm ⟨qHd, qHu, Q5, insert q10 Q10⟩ T
```

### D.4. AllowsTerm with inserted of `Q10` charge iff AllowsTermQ10 or AllowsTerm

> We show that the charge spectrum `x` with that charge inserted
> allows that potential term `T` if and only if either the charge spectrum `x`
> allows that potential term `T` *due to* the addition of that charge,
> or the charge spectrum `x` already allows that potential term `T`.

**`SuperSymmetry.SU5.ChargeSpectrum.allowsTerm_insertQ10_iff_allowsTermQ10`**, a lemma, [line 1009](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean#L1009).

```lean
lemma allowsTerm_insertQ10_iff_allowsTermQ10 {qHd qHu : Option 𝓩}
    {Q5 Q10: Finset 𝓩} {q10 : 𝓩} (T : PotentialTerm) :
    AllowsTerm ⟨qHd, qHu, Q5, insert q10 Q10⟩ T ↔
    AllowsTermQ10 ⟨qHd, qHu, Q5, Q10⟩ q10 T ∨
    AllowsTerm ⟨qHd, qHu, Q5, Q10⟩ T
```

## Depends on

- [Charges associated with a potential term](su5-chargespectrum-ofpotentialterm.md)

## Sources

- [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/AllowsTerm.lean)
