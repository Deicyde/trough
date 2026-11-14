---
declaration: module
origin: cited
lean: FTheory.SU5.Quanta, FTheory.SU5.Quanta.ext, FTheory.SU5.Quanta.toCharges, FTheory.SU5.Quanta.toCharges_qHd, FTheory.SU5.Quanta.toCharges_qHu, FTheory.SU5.Quanta.reduce, FTheory.SU5.Quanta.liftCharge, FTheory.SU5.Quanta.mem_liftCharge_iff
statement: formalized
proof: formalized
---

# Quanta of representations

The module `Physlib.StringTheory.FTheory.SU5.Quanta.Basic`, [Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean): 19 declarations (4 instances with no name), 8 with a docstring.

## i. Overview

> In SU(5) × U(1) F-theory theory, each 5-bar and 10d representation
> carries with it the quantum numbers of their U(1) charges and their fluxes.
>
> In this module we define the data structure for these quanta and
> properties thereof.

## ii. Key results

> - `Quanta` : The structure containing the quantum numbers of the 5-bar and 10d
>   representations, as well as the charges of the `Hd` and `Hu` particles.
> - `Quanta.liftCharge` : Lifting a `ChargeSpectrum` to a multiset of `Quanta`
>   which have no chiral exotics and no zero fluxes.
> - `Quanta.AnomalyCancellation` : The anomaly cancellation conditions on a `Quanta`.

## iv. References

> * Rational F-Theory GUTs without exotics (arXiv:1401.5084), Anomaly cancellation conditions,
>   equation 22. [ref: arxiv\_1401\_5084]

## A. The Quanta structure

**`FTheory.SU5.Quanta`**, a structure, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean#L71).

> The quanta associated with the representations in a `SU(5) x U(1)` F-theory.
> This contains the value of the charges and the flux integers `(M, N)` for the
> 5-bar matter content and the 10d matter content, and the charges of the `Hd` and
> `Hu` particles (there values of `(M,N)` are not included as they are
> forced to be `(0, 1)` and `(0, -1)` respectively.

```lean
structure Quanta (𝓩 : Type := ℤ) where
  /-- The charge of the Hd matter field. -/
  qHd : Option 𝓩
  /-- The negative charge of the Hu matter field.
    In other words the charge of the Hu considered as a 5-bar field. -/
  qHu : Option 𝓩
  /-- The quanta carried by the 5-bar matter fields. -/
  F : FiveQuanta 𝓩
  /-- The quanta carried by the 10d matter fields. -/
  T : TenQuanta 𝓩
```

### A.1. Repr instance on `Quanta`

**An instance with no name**, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean#L94).

```lean
unsafe instance [Repr 𝓩] : Repr (Quanta 𝓩)
```

### A.2. Extensionality lemma

**`FTheory.SU5.Quanta.ext`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean#L109).

```lean
lemma ext {𝓩 : Type} {x y : Quanta 𝓩} (h1 : x.qHd = y.qHd) (h2 : x.qHu = y.qHu)
    (h3 : x.F = y.F) (h4 : x.T = y.T) : x = y
```

### A.3. Decidable equality instance

**An instance with no name**, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean#L120).

```lean
instance [DecidableEq 𝓩] : DecidableEq (Quanta 𝓩)
```

### A.4. Map to the underlying `ChargeSpectrum`

**`FTheory.SU5.Quanta.toCharges`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean#L129).

> The underlying `ChargeSpectrum` of a `Quanta`.

```lean
def toCharges [DecidableEq 𝓩] (x : Quanta 𝓩) : ChargeSpectrum 𝓩
```

**`FTheory.SU5.Quanta.toCharges_qHd`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean#L135).

```lean
lemma toCharges_qHd [DecidableEq 𝓩] (x : Quanta 𝓩) : (toCharges x).qHd = x.qHd
```

**`FTheory.SU5.Quanta.toCharges_qHu`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean#L137).

```lean
lemma toCharges_qHu [DecidableEq 𝓩] (x : Quanta 𝓩) : (toCharges x).qHu = x.qHu
```

## B. The reduction of a `Quanta`

**`FTheory.SU5.Quanta.reduce`**, a def, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean#L147).

> The reduce of `Quanta` is a new `Quanta` with all the fluxes corresponding to the same
> charge (i.e. representation) added together.

```lean
def reduce [DecidableEq 𝓩] (x : Quanta 𝓩) : Quanta 𝓩
```

## C. Lifting a charge spectrum to quanta with no exotics or zero fluxes

**`FTheory.SU5.Quanta.liftCharge`**, a def, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean#L161).

> Lifting a charge spectrum to quanta which do not have exotics and
> which have no zero flux.

```lean
def liftCharge [DecidableEq 𝓩] (c : ChargeSpectrum 𝓩) : Multiset (Quanta 𝓩)
```

### C.1. Simplification of membership in the liftCharge multiset

**`FTheory.SU5.Quanta.mem_liftCharge_iff`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean#L173).

```lean
lemma mem_liftCharge_iff [DecidableEq 𝓩] {c : ChargeSpectrum 𝓩}
    {x : Quanta 𝓩} :
    x ∈ liftCharge c ↔ x.qHd = c.qHd ∧ x.qHu = c.qHu ∧
    x.F ∈ FiveQuanta.liftCharge c.Q5 ∧ x.T ∈ TenQuanta.liftCharge c.Q10
```

### C.2. Charge spectrum of a lifted quanta

**`FTheory.SU5.Quanta.toCharges_of_mem_liftCharge`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean#L190).

```lean
lemma toCharges_of_mem_liftCharge [DecidableEq 𝓩] {c : ChargeSpectrum 𝓩}
    {x : Quanta 𝓩} (h : x ∈ liftCharge c) :
    x.toCharges = c
```

## D. Anomaly cancellation conditions

> There are two anomaly cancellation conditions in the SU(5)×U(1) model which involve the
> `U(1)` charges. These are
>
> - `∑ᵢ qᵢ Nᵢ + ∑ₐ qₐ Nₐ = 0` where the first sum is over all 5-bar representations and the second
>   is over all 10d representations.
> - `∑ᵢ qᵢ² Nᵢ + 3 * ∑ₐ qₐ² Nₐ = 0` where the first sum is over all 5-bar representations and the
>   second is over all 10d representations.
>
> According to arXiv:1401.5084 [ref: arxiv\_1401\_5084] it is unclear whether this second condition
> should necessarily be imposed.

### D.1. The anomaly coefficient of Hd

**`FTheory.SU5.Quanta.HdAnomalyCoefficient`**, a def, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean#L223).

> The pair of anomaly cancellation coefficients associated with the `Hd` particle.

```lean
def HdAnomalyCoefficient [CommRing 𝓩] (qHd : Option 𝓩) : 𝓩 × 𝓩
```

**`FTheory.SU5.Quanta.HdAnomalyCoefficient_map`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean#L229).

```lean
lemma HdAnomalyCoefficient_map {𝓩 𝓩1 : Type} [CommRing 𝓩] [CommRing 𝓩1]
    (f : 𝓩 →+* 𝓩1) (qHd : Option 𝓩) :
    HdAnomalyCoefficient (qHd.map f) = (f.prodMap f) (HdAnomalyCoefficient qHd)
```

### D.2. The anomaly coefficient of Hu

**`FTheory.SU5.Quanta.HuAnomalyCoefficient`**, a def, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean#L241).

> The pair of anomaly cancellation coefficients associated with the `Hu` particle.

```lean
def HuAnomalyCoefficient [CommRing 𝓩] (qHu : Option 𝓩) : 𝓩 × 𝓩
```

**`FTheory.SU5.Quanta.HuAnomalyCoefficient_map`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean#L247).

```lean
lemma HuAnomalyCoefficient_map {𝓩 𝓩1 : Type} [CommRing 𝓩] [CommRing 𝓩1]
    (f : 𝓩 →+* 𝓩1) (qHu : Option 𝓩) :
    HuAnomalyCoefficient (qHu.map f) = (f.prodMap f) (HuAnomalyCoefficient qHu)
```

### D.3. The anomaly cancellation condition propositions

**`FTheory.SU5.Quanta.LinearAnomalyCancellation`**, a def, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean#L261).

> The linear anomaly cancellation condition, corresponding to
> `∑ᵢ qᵢ Nᵢ + ∑ₐ qₐ Nₐ = 0` where the first sum is over all 5-bar representations and the second
>   is over all 10d representations.

```lean
def LinearAnomalyCancellation [CommRing 𝓩] (Q : Quanta 𝓩) : Prop
```

**`FTheory.SU5.Quanta.QuarticAnomalyCancellation`**, a def, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean#L269).

> The quartic anomaly cancellation condition, corresponding to
> `∑ᵢ qᵢ² Nᵢ + 3 * ∑ₐ qₐ² Nₐ = 0` where the first sum is over all 5-bar representations and the
>   second is over all 10d representations.

```lean
def QuarticAnomalyCancellation [CommRing 𝓩] (Q : Quanta 𝓩) :
    Prop
```

#### D.3.1. The propositions are decidable

**An instance with no name**, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean#L280).

```lean
instance [CommRing 𝓩] [DecidableEq 𝓩] (Q : Quanta 𝓩) : Decidable Q.LinearAnomalyCancellation
```

**An instance with no name**, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean#L284).

```lean
instance [CommRing 𝓩] [DecidableEq 𝓩] (Q : Quanta 𝓩) : Decidable Q.QuarticAnomalyCancellation
```

## Depends on

- [Quanta of 5-d representations](su5-quanta-fivequanta.md)
- [Quanta of 10d representations](su5-quanta-tenquanta.md)

## Sources

- [Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/Basic.lean)
