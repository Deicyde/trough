---
declaration: module
origin: cited
lean: FTheory.SU5.CodimensionOneConfig, FTheory.SU5.CodimensionOneConfig.allowedBarFiveCharges, FTheory.SU5.CodimensionOneConfig.allowedTenCharges
statement: formalized
proof: formalized
---

# Allowed charges

The module `Physlib.StringTheory.FTheory.SU5.Charges.OfRationalSection`, [Physlib/StringTheory/FTheory/SU5/Charges/OfRationalSection.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/OfRationalSection.lean): 6 declarations (3 instances with no name), 3 with a docstring.

## i. Overview

> Within SU(5) F-theory with 10d and 5-bar matter fields there are constraints on the
> allowed U(1) charges the fields can have.
> These constraints are determined in arXiv:1504.05593 [ref: lawrie\_schafer\_nameki\_wong\_2015].
> They are related to the
> distinct configurations of the zero-section (`σ₀`) relativity to the
> additional rational section (`σ₁`s) in codimension one fiber.
> For our purposes here, we currently just state the constraints found
> in arXiv:1504.05593 [ref: lawrie\_schafer\_nameki\_wong\_2015], and leave the proof and derivation
> of these constraints to future work.

## ii. Key results

> - `CodimensionOneConfig` : The distinct configurations of the
>   zero-section (`σ₀`) relativity to the additional rational section (`σ₁`s) in
>   the codimension one fiber, `I₅`.
> - `CodimensionOneConfig.allowedBarFiveCharges` : The allowed
>   `U(1)`-charges of matter in the 5-bar representation of `SU(5)`
>   given a `CodimensionOneConfig`.
> - `CodimensionOneConfig.allowedTenCharges` : The allowed
>   `U(1)`-charges of matter in the 10d representation of `SU(5)`
>   given a `CodimensionOneConfig`.

## iv. References

> * The main reference for the material in this section: Lawrie, Schafer-Nameki and Wong, F-theory
>   and All Things Rational: Surveying U(1) Symmetries with Rational Sections, page 6.
>   [ref: lawrie\_schafer\_nameki\_wong\_2015]
> * See also footnote 4 of 1507.05961. [ref: arxiv\_1507\_05961]

## A. The distinct section configurations

**`FTheory.SU5.CodimensionOneConfig`**, an inductive, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/OfRationalSection.lean#L74).

> The distinct codimension one configurations of the
> zero-section (`σ₀`) relativity to the additional rational section (`σ₁`s).

```lean
inductive CodimensionOneConfig
  /-- `σ₀` and `σ₁` intersect the same `ℙ¹` of the `I₅` Kodaira fiber.
    This is sometimes denoted `I₅^{(01)}` -/
  | same : CodimensionOneConfig
  /-- `σ₀` and `σ₁` intersect the nearest neighbor `ℙ¹`s of the `I₅` Kodaira fiber.
    This is sometimes denoted `I₅^{(0|1)}` -/
  | nearestNeighbor : CodimensionOneConfig
  /-- `σ₀` and `σ₁` intersect the next to nearest neighbor `ℙ¹`s of the `I₅` Kodaira fiber.
    This is sometimes denoted `I₅^{(0||1)}` -/
  | nextToNearestNeighbor : CodimensionOneConfig
```

### A.1. The finiteness of the set of configurations

**An instance with no name**, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/OfRationalSection.lean#L94).

```lean
instance : Fintype CodimensionOneConfig
```

## B. The allowed charges given a configuration

### B.1. The allowed charges of the 5-bar matter

**`FTheory.SU5.CodimensionOneConfig.allowedBarFiveCharges`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/OfRationalSection.lean#L112).

> The allowed `U(1)`-charges of matter in the 5-bar representation of `SU(5)`
> given a `CodimensionOneConfig`.

```lean
def allowedBarFiveCharges : CodimensionOneConfig → Finset ℤ
```

### B.2. The allowed charges of the 10d matter

**`FTheory.SU5.CodimensionOneConfig.allowedTenCharges`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/OfRationalSection.lean#L125).

> The allowed `U(1)`-charges of matter in the 10d representation of `SU(5)`
> given a `CodimensionOneConfig`.

```lean
def allowedTenCharges : CodimensionOneConfig → Finset ℤ
```

### B.3. The finiteness of the allowed charges

**An instance with no name**, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/OfRationalSection.lean#L136).

```lean
instance : (I : CodimensionOneConfig) → Fintype I.allowedBarFiveCharges
```

**An instance with no name**, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/OfRationalSection.lean#L141).

```lean
instance : (I : CodimensionOneConfig) → Fintype I.allowedTenCharges
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/StringTheory/FTheory/SU5/Charges/OfRationalSection.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Charges/OfRationalSection.lean)
