---
declaration: module
origin: cited
lean: ProbabilisticTheory.JordanAlgebra.SpinFactor, ProbabilisticTheory.JordanAlgebra.SpinFactor.ext, ProbabilisticTheory.JordanAlgebra.SpinFactor.add_fst, ProbabilisticTheory.JordanAlgebra.SpinFactor.add_snd, ProbabilisticTheory.JordanAlgebra.SpinFactor.zero_fst, ProbabilisticTheory.JordanAlgebra.SpinFactor.zero_snd, ProbabilisticTheory.JordanAlgebra.SpinFactor.neg_fst, ProbabilisticTheory.JordanAlgebra.SpinFactor.neg_snd
statement: formalized
proof: formalized
---

# Spin factors

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.Examples.SpinFactor`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean): 30 declarations (7 instances with no name), 6 with a docstring.

> Spin factors `V × R` of a symmetric bilinear form, the basic non-associative Jordan algebras.

## i. Overview

> A spin factor is `V × ℝ` with the Jordan product `(x, a) ∘ (y, b) = (a y + b x, B x y + a b)` for a
> symmetric bilinear form `B`. It is the basic non-associative Jordan algebra; for a positive definite
> form it carries the Lorentz cone. Only the algebraic structure is built here.

## ii. Key results

> - `JordanAlgebra.SpinFactor` : the spin factor of a bilinear form.
> - `JordanAlgebra.SpinFactor.isCommJordan` : it is a Jordan algebra.
> - `JordanAlgebra.SpinFactor.mul_self_sub_two_smul_snd_mul_add_determinant_smul_one` : every element
>   satisfies a quadratic equation.
> - `JordanAlgebra.SpinFactor.determinant` : the determinant quadratic form `a² - B x x`.

## iv. References

> - Adapted from Cobord, `Jordan/SpinFactor.lean`.

## A. The underlying module

**`ProbabilisticTheory.JordanAlgebra.SpinFactor`**, an abbrev, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L59).

> The spin factor determined by a bilinear form.  The synonym keeps products belonging to
> different forms from becoming definitionally interchangeable.

```lean
abbrev SpinFactor (_B : LinearMap.BilinForm R V) : Type _
```

**An instance with no name**, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L66).

```lean
instance : AddCommGroup (SpinFactor R V B)
```

**An instance with no name**, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L67).

```lean
instance : Module R (SpinFactor R V B)
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.ext`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L69).

```lean
lemma ext {z w : SpinFactor R V B} (hV : z.1 = w.1) (hR : z.2 = w.2) : z = w
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.add_fst`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L72).

```lean
lemma add_fst (z w : SpinFactor R V B) : (z + w).1 = z.1 + w.1
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.add_snd`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L73).

```lean
lemma add_snd (z w : SpinFactor R V B) : (z + w).2 = z.2 + w.2
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.zero_fst`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L74).

```lean
lemma zero_fst : (0 : SpinFactor R V B).1 = 0
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.zero_snd`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L75).

```lean
lemma zero_snd : (0 : SpinFactor R V B).2 = 0
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.neg_fst`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L76).

```lean
lemma neg_fst (z : SpinFactor R V B) : (-z).1 = -z.1
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.neg_snd`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L77).

```lean
lemma neg_snd (z : SpinFactor R V B) : (-z).2 = -z.2
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.smul_fst`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L78).

```lean
lemma smul_fst (r : R) (z : SpinFactor R V B) : (r • z).1 = r • z.1
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.smul_snd`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L79).

```lean
lemma smul_snd (r : R) (z : SpinFactor R V B) : (r • z).2 = r • z.2
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.mk`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L82).

> Constructor exposing the vector and scalar components.

```lean
def mk (x : V) (a : R) : SpinFactor R V B
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.mk_fst`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L84).

```lean
lemma mk_fst (x : V) (a : R) : (mk B x a).1 = x
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.mk_snd`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L85).

```lean
lemma mk_snd (x : V) (a : R) : (mk B x a).2 = a
```

## B. The Jordan product

**An instance with no name**, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L93).

```lean
instance : Mul (SpinFactor R V B)
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.mul_fst`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L96).

```lean
lemma mul_fst (z w : SpinFactor R V B) :
    (z * w).1 = z.2 • w.1 + w.2 • z.1
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.mul_snd`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L99).

```lean
lemma mul_snd (z w : SpinFactor R V B) :
    (z * w).2 = B z.1 w.1 + z.2 * w.2
```

**An instance with no name**, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L102).

```lean
instance : One (SpinFactor R V B)
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.one_fst`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L104).

```lean
lemma one_fst : (1 : SpinFactor R V B).1 = 0
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.one_snd`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L105).

```lean
lemma one_snd : (1 : SpinFactor R V B).2 = 1
```

**An instance with no name**, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L107).

```lean
instance : NonAssocRing (SpinFactor R V B)
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.mul_comm`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L115).

```lean
lemma mul_comm (hB : B.IsSymm) (z w : SpinFactor R V B) : z * w = w * z
```

**An instance with no name**, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L125).

```lean
instance : IsScalarTower R (SpinFactor R V B) (SpinFactor R V B)
```

**An instance with no name**, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L129).

```lean
instance : SMulCommClass R (SpinFactor R V B) (SpinFactor R V B)
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.nonAssocCommRing`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L135).

> A symmetric form gives the commutative Jordan algebra structure on the spin factor.

```lean
noncomputable def nonAssocCommRing (hB : B.IsSymm) : NonAssocCommRing (SpinFactor R V B)
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.isCommJordan`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L140).

> The Jordan identity for the spin-factor product.

```lean
lemma isCommJordan (hB : B.IsSymm) :
    let _ : NonAssocCommRing (SpinFactor R V B) := nonAssocCommRing B hB
    IsCommJordan (SpinFactor R V B)
```

## C. The determinant and the quadratic equation

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.determinant`**, a def, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L158).

> The rank-two determinant/norm form of a spin factor.

```lean
def determinant : QuadraticMap R (SpinFactor R V B) R
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.determinant_apply`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L168).

```lean
lemma determinant_apply (z : SpinFactor R V B) :
    determinant B z = z.2 * z.2 - B z.1 z.1
```

**`ProbabilisticTheory.JordanAlgebra.SpinFactor.mul_self_sub_two_smul_snd_mul_add_determinant_smul_one`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean#L173).

> The quadratic Cayley--Hamilton identity characteristic of rank-two spin factors.

```lean
lemma mul_self_sub_two_smul_snd_mul_add_determinant_smul_one
    (z : SpinFactor R V B) :
    z * z - (2 * z.2) • z + determinant B z • (1 : SpinFactor R V B) = 0
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Examples/SpinFactor.lean)
