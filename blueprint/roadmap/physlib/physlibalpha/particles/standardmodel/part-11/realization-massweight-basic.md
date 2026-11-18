---
declaration: module
origin: cited
lean: StandardModel.AlgebraRealization.massWeight_H, StandardModel.AlgebraRealization.massWeight_barH, StandardModel.AlgebraRealization.massWeight_A, StandardModel.AlgebraRealization.massWeight_d, StandardModel.AlgebraRealization.massWeight_bard, StandardModel.AlgebraRealization.massWeight_u, StandardModel.AlgebraRealization.massWeight_baru, StandardModel.AlgebraRealization.massWeight_Q
statement: formalized
proof: formalized
---

# The mass weights of the fields of an algebra realization

The module `PhyslibAlpha.Particles.StandardModel.Realization.MassWeight.Basic`, [PhyslibAlpha/Particles/StandardModel/Realization/MassWeight/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/MassWeight/Basic.lean): 13 declarations, 13 with a docstring; 1 private, not shown.

## i. Overview

> Every derivative symbol of an algebra realization is an eigenvector of `massWeightPoly`, of
> pure monomial weight equal to twice its mass dimension.  The bosons have mass dimension
> `1 + |s|` and the fermions `3/2 + |s|`, where `|s|` counts the derivatives.  Each law is the
> corresponding law of the jet algebra, pushed along the defining algebra map.

## ii. Key results

> - `map_massWeight_monomial` : a monomial mass-weight eigenvalue transports along the defining map:
>   the map carries the mass-weight polynomial to the mass-weight polynomial, and a monomial to a
>   monomial
> - `massWeight_H` : the law `massWeight_H` of a Standard Model, obtained from the corresponding law
>   of the jet algebra by pushing it along the defining algebra map
> - `massWeight_barH` : the law `massWeight_barH` of a Standard Model, obtained from the corresponding
>   law of the jet algebra by pushing it along the defining algebra map
> - `massWeight_A` : the law `massWeight_A` of a Standard Model, obtained from the corresponding law
>   of the jet algebra by pushing it along the defining algebra map

## iv. References

> * None.

## A. The mass weights of the fields

> Every derivative symbol is a `massWeightPoly`-eigenvector of pure monomial weight — twice
> its mass dimension. The bosons have mass dimension `1 + |s|`, the fermions `3/2 + |s|`.

**`StandardModel.AlgebraRealization.massWeight_H`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/MassWeight/Basic.lean#L80).

> The law `massWeight_H` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma massWeight_H : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) φ,
    massWeightPoly (h.H s φ) = Polynomial.monomial (2 * (1 + Multiset.card s)) (h.H s φ)
```

**`StandardModel.AlgebraRealization.massWeight_barH`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/MassWeight/Basic.lean#L86).

> The law `massWeight_barH` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma massWeight_barH : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) φ,
    massWeightPoly (h.barH s φ) = Polynomial.monomial (2 * (1 + Multiset.card s)) (h.barH s φ)
```

**`StandardModel.AlgebraRealization.massWeight_A`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/MassWeight/Basic.lean#L92).

> The law `massWeight_A` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma massWeight_A : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) μ φ,
    massWeightPoly (h.A s μ φ) = Polynomial.monomial (2 * (1 + Multiset.card s)) (h.A s μ φ)
```

**`StandardModel.AlgebraRealization.massWeight_d`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/MassWeight/Basic.lean#L98).

> The law `massWeight_d` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma massWeight_d : ∀ i (s : Multiset (Fin 1 ⊕ Fin 3)) φ,
    massWeightPoly (h.d i s φ) = Polynomial.monomial (3 + 2 * Multiset.card s) (h.d i s φ)
```

**`StandardModel.AlgebraRealization.massWeight_bard`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/MassWeight/Basic.lean#L104).

> The law `massWeight_bard` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma massWeight_bard : ∀ i (s : Multiset (Fin 1 ⊕ Fin 3)) φ,
    massWeightPoly (h.bard i s φ) = Polynomial.monomial (3 + 2 * Multiset.card s) (h.bard i s φ)
```

**`StandardModel.AlgebraRealization.massWeight_u`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/MassWeight/Basic.lean#L110).

> The law `massWeight_u` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma massWeight_u : ∀ i (s : Multiset (Fin 1 ⊕ Fin 3)) φ,
    massWeightPoly (h.u i s φ) = Polynomial.monomial (3 + 2 * Multiset.card s) (h.u i s φ)
```

**`StandardModel.AlgebraRealization.massWeight_baru`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/MassWeight/Basic.lean#L116).

> The law `massWeight_baru` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma massWeight_baru : ∀ i (s : Multiset (Fin 1 ⊕ Fin 3)) φ,
    massWeightPoly (h.baru i s φ) = Polynomial.monomial (3 + 2 * Multiset.card s) (h.baru i s φ)
```

**`StandardModel.AlgebraRealization.massWeight_Q`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/MassWeight/Basic.lean#L122).

> The law `massWeight_Q` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma massWeight_Q : ∀ i (s : Multiset (Fin 1 ⊕ Fin 3)) φ,
    massWeightPoly (h.Q i s φ) = Polynomial.monomial (3 + 2 * Multiset.card s) (h.Q i s φ)
```

**`StandardModel.AlgebraRealization.massWeight_barQ`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/MassWeight/Basic.lean#L128).

> The law `massWeight_barQ` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma massWeight_barQ : ∀ i (s : Multiset (Fin 1 ⊕ Fin 3)) φ,
    massWeightPoly (h.barQ i s φ) = Polynomial.monomial (3 + 2 * Multiset.card s) (h.barQ i s φ)
```

**`StandardModel.AlgebraRealization.massWeight_L`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/MassWeight/Basic.lean#L134).

> The law `massWeight_L` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma massWeight_L : ∀ i (s : Multiset (Fin 1 ⊕ Fin 3)) φ,
    massWeightPoly (h.L i s φ) = Polynomial.monomial (3 + 2 * Multiset.card s) (h.L i s φ)
```

**`StandardModel.AlgebraRealization.massWeight_barL`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/MassWeight/Basic.lean#L140).

> The law `massWeight_barL` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma massWeight_barL : ∀ i (s : Multiset (Fin 1 ⊕ Fin 3)) φ,
    massWeightPoly (h.barL i s φ) = Polynomial.monomial (3 + 2 * Multiset.card s) (h.barL i s φ)
```

**`StandardModel.AlgebraRealization.massWeight_e`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/MassWeight/Basic.lean#L146).

> The law `massWeight_e` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma massWeight_e : ∀ i (s : Multiset (Fin 1 ⊕ Fin 3)) φ,
    massWeightPoly (h.e i s φ) = Polynomial.monomial (3 + 2 * Multiset.card s) (h.e i s φ)
```

**`StandardModel.AlgebraRealization.massWeight_bare`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/MassWeight/Basic.lean#L152).

> The law `massWeight_bare` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma massWeight_bare : ∀ i (s : Multiset (Fin 1 ⊕ Fin 3)) φ,
    massWeightPoly (h.bare i s φ) = Polynomial.monomial (3 + 2 * Multiset.card s) (h.bare i s φ)
```

## Depends on

- [The algebra valued Standard model](../part-09/realization-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Realization/MassWeight/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/MassWeight/Basic.lean)
