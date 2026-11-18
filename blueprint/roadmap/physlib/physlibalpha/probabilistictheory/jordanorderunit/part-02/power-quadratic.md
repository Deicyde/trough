---
declaration: module
origin: cited
lean: ProbabilisticTheory.JordanAlgebra.quadRep_jpow_jpow, ProbabilisticTheory.JordanAlgebra.quadRep_jpow, ProbabilisticTheory.JordanAlgebra.quadRep_jpow_one, ProbabilisticTheory.JordanAlgebra.quadRep_jpow_comp_jpow
statement: formalized
proof: formalized
---

# Quadratic representations of powers

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.Power.Quadratic`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Power/Quadratic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Power/Quadratic.lean): 4 declarations, 4 with a docstring.

> The quadratic representation on powers: `U_{aᵐ} aⁿ = a²ᵐ⁺ⁿ`.

## i. Overview

> On powers the quadratic representation acts by `U_{aᵐ} aⁿ = a²ᵐ⁺ⁿ`.

## ii. Key results

> - `JordanAlgebra.quadRep_jpow_jpow` : `U_{aᵐ} aⁿ = a²ᵐ⁺ⁿ`.

## iv. References

> * None.

## A. Quadratic action on powers

**`ProbabilisticTheory.JordanAlgebra.quadRep_jpow_jpow`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Power/Quadratic.lean#L48).

> `U_{aᵐ} aⁿ = a²ᵐ⁺ⁿ`.

```lean
lemma quadRep_jpow_jpow (a : E) (m n : ℕ) :
    U (a ^[m]) (a ^[n]) = a ^[2 * m + n]
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_jpow`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Power/Quadratic.lean#L62).

> A single outer factor raises the degree of a power by two.

```lean
lemma quadRep_jpow (a : E) (n : ℕ) : U a (a ^[n]) = a ^[n + 2]
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_jpow_one`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Power/Quadratic.lean#L66).

> The quadratic representation of a power at the order unit is its even power.

```lean
lemma quadRep_jpow_one (a : E) (m : ℕ) : U (a ^[m]) (1 : E) = a ^[2 * m]
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_jpow_comp_jpow`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Power/Quadratic.lean#L70).

> Quadratic representations compose additively on powers of a common element.

```lean
lemma quadRep_jpow_comp_jpow (a : E) (m n k : ℕ) :
    U (a ^[m]) (U (a ^[n]) (a ^[k])) = a ^[2 * m + 2 * n + k]
```

## Depends on

- [Powers, multiplication operators and the quadratic representation](../part-01/operator.md)

## Proof depends on

- [Power-associativity](power-associative.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Power/Quadratic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Power/Quadratic.lean)
