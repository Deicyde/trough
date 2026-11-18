---
declaration: module
origin: cited
lean: FTheory.SU5.ChargeSpectrum.IsAnomalyFree, FTheory.SU5.ChargeSpectrum.isAnomalyFree_map, FTheory.SU5.ChargeSpectrum.viable_anomalyFree
statement: formalized
proof: formalized
---

# Anomaly cancellation

The module `Physlib.StringTheory.FTheory.SU5.Charges.AnomalyFree`, [Physlib/StringTheory/FTheory/SU5/Charges/AnomalyFree.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/AnomalyFree.lean): 4 declarations (1 instance with no name), 2 with a docstring.

## i. Overview

> In this module we do two things. The first is to define a proposition `IsAnomalyFree`
> on a `ChargeSpectrum` which states that the charge spectrum can be lifted
> to an anomaly-free `Quanta` with fluxes which do not have exotics.
>
> We then find all the viable charges given a configuration of the sections in codimension one
> fiber `CodimensionOneConfig` that can be lifted to an anomaly-free `Quanta` with fluxes
> which do not have exotics.

## ii. Key results

> - `IsAnomalyFree` : The proposition on a `ChargeSpectrum` that it can be lifted to an
>   anomaly-free `Quanta` with fluxes which do not have exotics.
> - `viable_anomalyFree` : The viable charges given a configuration of the sections
>   in codimension one fiber `CodimensionOneConfig` which can be lifted to an anomaly-free
>   `Quanta` with fluxes which do not have exotics.

## iv. References

> * None.

## A. Charge spectrum which lift to anomaly free quanta

**`FTheory.SU5.ChargeSpectrum.IsAnomalyFree`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/AnomalyFree.lean#L66).

> The condition on a collection of charges `c` that it extends to an anomaly free `Quanta`.
> That anomaly free `Quanta` is not tracked by this proposition.

```lean
def IsAnomalyFree [DecidableEq 𝓩] [CommRing 𝓩] (c : ChargeSpectrum 𝓩) : Prop
```

### A.1. Decidability of the proposition

**An instance with no name**, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/AnomalyFree.lean#L75).

```lean
instance [DecidableEq 𝓩] [CommRing 𝓩] {c : ChargeSpectrum 𝓩} : Decidable (IsAnomalyFree c)
```

### A.2. The proposition is preserved under mappings of charge spectra

**`FTheory.SU5.ChargeSpectrum.isAnomalyFree_map`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/AnomalyFree.lean#L88).

```lean
lemma isAnomalyFree_map (f : 𝓩 →+* 𝓩1) {c : ChargeSpectrum 𝓩}
    (h : IsAnomalyFree c) : IsAnomalyFree (c.map (f.toAddMonoidHom))
```

## B. The viable charges which lift to anomaly free quanta

**`FTheory.SU5.ChargeSpectrum.viable_anomalyFree`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/AnomalyFree.lean#L112).

> The viable charges which are anomaly free.

```lean
lemma viable_anomalyFree (I : CodimensionOneConfig) :
    (viableCharges I).filter IsAnomalyFree =
    (match I with
    | .same => {⟨some 2, some (-2), {-3, -1}, {-1}⟩,
      ⟨some 2, some (-2), {-1, 1}, {-1}⟩,
      ⟨some (-2), some 2, {-1, 1}, {1}⟩,
      ⟨some (-2), some 2, {1, 3}, {1}⟩}
    | .nearestNeighbor => {⟨some (-4), some (-14), {6, 11}, {-7}⟩,
      ⟨some 6, some (-14), {-9, 1}, {-7}⟩,
      ⟨some 6, some (-14), {1, 11}, {-7}⟩,
      ⟨some (-14), some 6, {1, 11}, {3}⟩}
    | .nextToNearestNeighbor => {⟨some 2, some 12, {-13, -8}, {6}⟩})
```

## Depends on

- [Mapping charge spectra values](../../particles/supersymmetry/part-01/su5-chargespectrum-map.md)
- [Charges which are not pheno-constrained and do not regenerate dangerous couplings with Yukawas](su5-charges-viable.md)
- [Quanta of representations](su5-quanta-basic.md)

## Sources

- [Physlib/StringTheory/FTheory/SU5/Charges/AnomalyFree.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/AnomalyFree.lean)
