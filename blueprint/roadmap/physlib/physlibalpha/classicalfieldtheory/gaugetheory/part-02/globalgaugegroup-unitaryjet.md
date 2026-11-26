---
declaration: module
origin: cited
lean: GlobalGaugeGroup.star_eq_neg_of_mem_lieAlgebra, GlobalGaugeGroup.derivValueMatrix_star, GlobalGaugeGroup.star_eq_neg_of_mem_jetLieAlgebra, GlobalGaugeGroup.star_mul_self_gaugeJet, GlobalGaugeGroup.star_eq_inv_gaugeJet, GlobalGaugeGroup.SU.star_mul_self_val, GlobalGaugeGroup.SU.star_mul_self, GlobalGaugeGroup.SU.mul_star_self
statement: formalized
proof: formalized
---

# The gauge jets of unitary gauge groups

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.UnitaryJet`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/UnitaryJet.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/UnitaryJet.lean): 14 declarations, 14 with a docstring.

> The gauge jets of `SU(n)` and `U(1)` are unitary at every order.

## i. Overview

> When every element of a global gauge group is unitary, its generators are anti-hermitian, the
> derivative at `t = 0` of `exp (t X)† exp (t X) = 1`. The Maurer–Cartan form `ω_μ = (∂_μ U) U⁻¹`
> of a gauge jet is a Lie algebra jet, so each of its base-point derivatives is anti-hermitian,
> and so `ω_μ† = −ω_μ` as a matrix of jets. Then `U† U` has vanishing derivatives,
> `∂_μ (U† U) = (ω_μ U)† U + U† ω_μ U = 0`, so it is the constant `1` of its value. Thus
> every gauge jet of `SU(n)` or `U(1)` is a unitary matrix of jets, with `U⁻¹ = U†`.
>
> For `U(1)` this makes every gauge jet the scalar matrix of a unitary jet.

## ii. Key results

> - `GlobalGaugeGroup.star_eq_neg_of_mem_lieAlgebra` : the generators of a unitary global gauge
>   group are anti-hermitian.
> - `GlobalGaugeGroup.star_mul_self_gaugeJet` : a gauge jet of a unitary global gauge group is
>   unitary.
> - `GlobalGaugeGroup.SU.star_mul_self`, `GlobalGaugeGroup.SU.mul_star_self` : the gauge jets of
>   `SU(n)` are unitary matrices of jets.
> - `GlobalGaugeGroup.U1.unitaryJet` : the unitary jet of a gauge jet of `U(1)`.
> - `GlobalGaugeGroup.U1.gaugeJet_eq_scalar` : every gauge jet of `U(1)` is a scalar matrix.

## iv. References

> * None.

## A. Generators of unitary groups are anti-hermitian

**`GlobalGaugeGroup.star_eq_neg_of_mem_lieAlgebra`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/UnitaryJet.lean#L69).

> The generators of a global gauge group all of whose elements are unitary are
> anti-hermitian. The conjugate transpose of `exp (t X)` is `exp (t X†)` and is the inverse
> `exp (−t X)`, so the two one-parameter families have the same derivative at `t = 0`.

```lean
lemma star_eq_neg_of_mem_lieAlgebra (hG : ∀ g ∈ G.group, star (g : Matrix κ κ ℂ) * g = 1)
    {X : Matrix κ κ ℂ} (hX : X ∈ G.lieAlgebra) : star X = -X
```

## B. Lie algebra jets of unitary groups are anti-hermitian

**`GlobalGaugeGroup.derivValueMatrix_star`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/UnitaryJet.lean#L97).

> The base-point derivatives of the conjugate transpose of a matrix of jets are the
> conjugate transposes of its base-point derivatives.

```lean
lemma derivValueMatrix_star (s : Multiset (Fin 1 ⊕ Fin 3)) (M : Matrix κ κ SpaceTimeAlgebra) :
    derivValueMatrix s (star M) = star (derivValueMatrix s M)
```

**`GlobalGaugeGroup.star_eq_neg_of_mem_jetLieAlgebra`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/UnitaryJet.lean#L105).

> A Lie algebra jet of a global gauge group all of whose elements are unitary is
> anti-hermitian as a matrix of jets.

```lean
lemma star_eq_neg_of_mem_jetLieAlgebra (hG : ∀ g ∈ G.group, star (g : Matrix κ κ ℂ) * g = 1)
    {A : Matrix κ κ SpaceTimeAlgebra} (hA : A ∈ G.jetLieAlgebra) : star A = -A
```

## C. Gauge jets of unitary groups are unitary

**`GlobalGaugeGroup.star_mul_self_gaugeJet`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/UnitaryJet.lean#L120).

> A gauge jet of a global gauge group all of whose elements are unitary is a unitary
> matrix of jets, `U† U = 1`. The product `U† U` has vanishing derivatives, since the
> Maurer–Cartan form is anti-hermitian, so it is the constant of its value.

```lean
lemma star_mul_self_gaugeJet (hG : ∀ g ∈ G.group, star (g : Matrix κ κ ℂ) * g = 1)
    (U : G.gaugeJetGroup) :
    star (U.1 : Matrix κ κ SpaceTimeAlgebra) * (U.1 : Matrix κ κ SpaceTimeAlgebra) = 1
```

**`GlobalGaugeGroup.star_eq_inv_gaugeJet`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/UnitaryJet.lean#L143).

> The inverse of a gauge jet of a global gauge group all of whose elements are unitary is
> its conjugate transpose.

```lean
lemma star_eq_inv_gaugeJet (hG : ∀ g ∈ G.group, star (g : Matrix κ κ ℂ) * g = 1)
    (U : G.gaugeJetGroup) :
    star (U.1 : Matrix κ κ SpaceTimeAlgebra) = (↑U.1⁻¹ : Matrix κ κ SpaceTimeAlgebra)
```

## D. The gauge jets of SU(n)

**`GlobalGaugeGroup.SU.star_mul_self_val`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/UnitaryJet.lean#L160).

> The elements of `SU(n)` are unitary, `g† g = 1`.

```lean
lemma SU.star_mul_self_val {n : ℕ} {g : GeneralLinearGroup (Fin n) ℂ}
    (hg : g ∈ (SU n).group) : star (g : Matrix (Fin n) (Fin n) ℂ) * g = 1
```

**`GlobalGaugeGroup.SU.star_mul_self`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/UnitaryJet.lean#L165).

> A gauge jet of `SU(n)` is a unitary matrix of jets, `U† U = 1`.

```lean
lemma SU.star_mul_self {n : ℕ} (U : (SU n).gaugeJetGroup) :
    star (U.1 : Matrix (Fin n) (Fin n) SpaceTimeAlgebra) * U.1 = 1
```

**`GlobalGaugeGroup.SU.mul_star_self`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/UnitaryJet.lean#L170).

> A gauge jet of `SU(n)` is a unitary matrix of jets, `U U† = 1`.

```lean
lemma SU.mul_star_self {n : ℕ} (U : (SU n).gaugeJetGroup) :
    (U.1 : Matrix (Fin n) (Fin n) SpaceTimeAlgebra) * star U.1 = 1
```

**`GlobalGaugeGroup.SU.star_eq_inv`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/UnitaryJet.lean#L175).

> The inverse of a gauge jet of `SU(n)` is its conjugate transpose.

```lean
lemma SU.star_eq_inv {n : ℕ} (U : (SU n).gaugeJetGroup) :
    star (U.1 : Matrix (Fin n) (Fin n) SpaceTimeAlgebra) =
      (↑U.1⁻¹ : Matrix (Fin n) (Fin n) SpaceTimeAlgebra)
```

## E. The gauge jets of U(1)

**`GlobalGaugeGroup.U1.star_mul_self_val`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/UnitaryJet.lean#L187).

> The elements of `U(1)` are unitary, `g† g = 1`.

```lean
lemma U1.star_mul_self_val {g : GeneralLinearGroup (Fin 1) ℂ} (hg : g ∈ U1.group) :
    star (g : Matrix (Fin 1) (Fin 1) ℂ) * g = 1
```

**`GlobalGaugeGroup.U1.star_mul_self`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/UnitaryJet.lean#L192).

> A gauge jet of `U(1)` is a unitary matrix of jets, `U† U = 1`.

```lean
lemma U1.star_mul_self (U : U1.gaugeJetGroup) :
    star (U.1 : Matrix (Fin 1) (Fin 1) SpaceTimeAlgebra) * U.1 = 1
```

**`GlobalGaugeGroup.U1.star_eq_inv`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/UnitaryJet.lean#L197).

> The inverse of a gauge jet of `U(1)` is its conjugate transpose.

```lean
lemma U1.star_eq_inv (U : U1.gaugeJetGroup) :
    star (U.1 : Matrix (Fin 1) (Fin 1) SpaceTimeAlgebra) =
      (↑U.1⁻¹ : Matrix (Fin 1) (Fin 1) SpaceTimeAlgebra)
```

**`GlobalGaugeGroup.U1.unitaryJet`**, a def, [line 203](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/UnitaryJet.lean#L203).

> The unitary jet of a gauge jet of `U(1)`, its only matrix entry.

```lean
def U1.unitaryJet (U : U1.gaugeJetGroup) : unitary SpaceTimeAlgebra
```

**`GlobalGaugeGroup.U1.gaugeJet_eq_scalar`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/UnitaryJet.lean#L210).

> Every gauge jet of `U(1)` is the scalar matrix of its unitary jet.

```lean
lemma U1.gaugeJet_eq_scalar (U : U1.gaugeJetGroup) :
    (U.1 : Matrix (Fin 1) (Fin 1) SpaceTimeAlgebra) =
      Matrix.scalar (Fin 1) (U1.unitaryJet U : SpaceTimeAlgebra)
```

## Depends on

- [The jet gauge group of a global gauge group](globalgaugegroup-gaugejetgroup.md)
- [The global gauge group SU(n)](globalgaugegroup-su.md)
- [The global gauge group U(1)](globalgaugegroup-u1.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/UnitaryJet.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/UnitaryJet.lean)
