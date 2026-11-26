---
declaration: module
origin: cited
lean: GlobalGaugeGroup.U1, GlobalGaugeGroup.mem_U1_iff_mem_unitaryGroup, GlobalGaugeGroup.mem_U1_iff, GlobalGaugeGroup.U1.groupEquiv, GlobalGaugeGroup.U1.groupEquiv_val, GlobalGaugeGroup.mem_lieAlgebra_U1, GlobalGaugeGroup.exists_eq_I_smul_scalar_of_mem_lieAlgebra_U1
statement: formalized
proof: formalized
---

# The global gauge group U(1)

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.U1`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1.lean): 7 declarations, 5 with a docstring.

> The group of phases, as a global gauge group.

## i. Overview

> The gauge group of electromagnetism, and of weak hypercharge in the Standard Model, is
> `U(1)`. It is the group of complex numbers of modulus one, the phases `e^{iθ}`, acting on a
> charged field by multiplication. As a global gauge group it is the group of unitary `1 × 1`
> complex matrices, and an invertible `1 × 1` matrix lies in it exactly when its entry has
> modulus one.
>
> Its generators are the anti-hermitian `1 × 1` matrices, the imaginary numbers `i θ`, whose
> exponentials `e^{i t θ}` are phases. The hermitian generator of physics is the real charge
> `θ`.

## ii. Key results

> - `GlobalGaugeGroup.U1` : the global gauge group `U(1)`.
> - `GlobalGaugeGroup.mem_U1_iff` : an invertible `1 × 1` matrix lies in `U(1)` exactly when
>   its entry has modulus one.
> - `GlobalGaugeGroup.mem_lieAlgebra_U1` : anti-hermitian `1 × 1` matrices are generators of
>   `U(1)`.
> - `GlobalGaugeGroup.exists_eq_I_smul_scalar_of_mem_lieAlgebra_U1` : generators of `U(1)` are
>   imaginary scalars.

## iv. References

> * None.

## A. The group U(1)

**`GlobalGaugeGroup.U1`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1.lean#L63).

> The global gauge group `U(1)`, the unitary `1 × 1` complex matrices.

```lean
def U1 : GlobalGaugeGroup (Fin 1)
```

**`GlobalGaugeGroup.mem_U1_iff_mem_unitaryGroup`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1.lean#L66).

```lean
lemma mem_U1_iff_mem_unitaryGroup {g : GeneralLinearGroup (Fin 1) ℂ} :
    g ∈ U1.group ↔ (g : Matrix (Fin 1) (Fin 1) ℂ) ∈ unitaryGroup (Fin 1) ℂ
```

## B. Elements as phases

**`GlobalGaugeGroup.mem_U1_iff`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1.lean#L78).

> An invertible `1 × 1` matrix lies in `U(1)` exactly when its entry is a phase, of
> modulus one.

```lean
lemma mem_U1_iff {g : GeneralLinearGroup (Fin 1) ℂ} :
    g ∈ U1.group ↔ ‖(g : Matrix (Fin 1) (Fin 1) ℂ) 0 0‖ = 1
```

**`GlobalGaugeGroup.U1.groupEquiv`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1.lean#L95).

> The phases are the elements of the global gauge group `U(1)`, as scalar `1 × 1`
> matrices.

```lean
noncomputable def U1.groupEquiv : unitary ℂ ≃* U1.group
```

**`GlobalGaugeGroup.U1.groupEquiv_val`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1.lean#L113).

```lean
lemma U1.groupEquiv_val (u : unitary ℂ) :
    (((U1.groupEquiv u : U1.group) : GeneralLinearGroup (Fin 1) ℂ) : Matrix (Fin 1) (Fin 1) ℂ) =
      scalar (Fin 1) (u : ℂ)
```

## C. The Lie algebra of U(1)

**`GlobalGaugeGroup.mem_lieAlgebra_U1`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1.lean#L125).

> An anti-hermitian `1 × 1` matrix is a generator of `U(1)`. Its exponential is unitary,
> with conjugate transpose the exponential of `−X`.

```lean
lemma mem_lieAlgebra_U1 {X : Matrix (Fin 1) (Fin 1) ℂ} (hX : star X = -X) :
    X ∈ U1.lieAlgebra
```

**`GlobalGaugeGroup.exists_eq_I_smul_scalar_of_mem_lieAlgebra_U1`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1.lean#L138).

> A generator of `U(1)` is an imaginary scalar `i a` with `a` real. The entry of `exp (X)` is
> `exp (x)` and has modulus one, so `x` has vanishing real part.

```lean
lemma exists_eq_I_smul_scalar_of_mem_lieAlgebra_U1 {X : Matrix (Fin 1) (Fin 1) ℂ}
    (hX : X ∈ U1.lieAlgebra) : ∃ a : ℝ, X = Complex.I • scalar (Fin 1) (a : ℂ)
```

## Depends on

- [The Lie algebra of a global gauge group](globalgaugegroup-liealgebra-basic.md)

## Proof depends on

- [Lie's Trace Formula](../../../../physlib/mathematics/formathlib/part-01/datastructures-matrix-lietrace.md)
- [Scalar matrices](../../../mathematics/part-02/formathlib/datastructures-matrix-scalar.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1.lean)
