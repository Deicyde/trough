---
declaration: module
origin: cited
lean: MicroHamiltonian.entropy_A_eq_entropy_Z, MicroHamiltonian.β_eq_deriv_S_U, MicroHamiltonian.partitionZ, MicroHamiltonian.PartitionZComplex, MicroHamiltonian.ZComplexConvergenceDomain, MicroHamiltonian.contDiffAt_partitionZ_of_mem_interior_convergenceDomain, MicroHamiltonian.partitionZT, MicroHamiltonian.internalU
statement: formalized
proof: formalized
---

# The theormodynamical quantities of a microcanonical ensemble

The module `Physlib.StatisticalMechanics.MicroCanonicalEnsemble.ThermoQuantities`, [Physlib/StatisticalMechanics/MicroCanonicalEnsemble/ThermoQuantities.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/ThermoQuantities.lean): 14 declarations, 13 with a docstring, 2 listed as significant; 1 private, not shown.

**`MicroHamiltonian.partitionZ`**, a def, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/ThermoQuantities.lean#L28).

> The partition function corresponding to a given MicroHamiltonian. This is a function taking a
> thermodynamic β, not a temperature. It also depends on the data D defining the system extrinsincs.
>
> * Ideally this would be an NNReal, but ∫ (NNReal) doesn't work right now, so it would just be a
>   separate proof anyway

```lean
def partitionZ (β : ℝ) : ℝ
```

**`MicroHamiltonian.PartitionZComplex`**, a def, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/ThermoQuantities.lean#L34).

> The complexified partition function, viewed as a Laplace transform.

```lean
def PartitionZComplex (z : ℂ) : ℂ
```

**`MicroHamiltonian.ZComplexConvergenceDomain`**, a def, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/ThermoQuantities.lean#L38).

> The complex convergence domain of the partition-function Laplace transform.

```lean
def ZComplexConvergenceDomain : Set ℂ
```

**`MicroHamiltonian.contDiffAt_partitionZ_of_mem_interior_convergenceDomain`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/ThermoQuantities.lean#L65).

```lean
lemma contDiffAt_partitionZ_of_mem_interior_convergenceDomain {β : ℝ}
    (hβ : (β : ℂ) ∈ interior (H.ZComplexConvergenceDomain d)) :
    ContDiffAt ℝ ⊤ (H.partitionZ d) β
```

**`MicroHamiltonian.partitionZT`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/ThermoQuantities.lean#L76).

> The partition function as a function of temperature T instead of β.

```lean
def partitionZT (T : ℝ) : ℝ
```

**`MicroHamiltonian.internalU`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/ThermoQuantities.lean#L80).

> The Internal Energy, U or E, defined as -∂(ln Z)/∂β. Parameterized here with β.

```lean
def internalU (β : ℝ) : ℝ
```

**`MicroHamiltonian.helmholtzA`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/ThermoQuantities.lean#L85).

> The Helmholtz Free Energy, -T * ln Z. Also denoted F. Parameterized here with temperature T, not
> β.

```lean
def helmholtzA (T : ℝ) : ℝ
```

**`MicroHamiltonian.entropyS`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/ThermoQuantities.lean#L89).

> The entropy, defined as the -∂A/∂T. Function of T.

```lean
def entropyS (T : ℝ) : ℝ
```

**`MicroHamiltonian.entropySβ`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/ThermoQuantities.lean#L93).

> The entropy, defined as ln Z + β*U. Function of β.

```lean
def entropySβ (β : ℝ) : ℝ
```

**`MicroHamiltonian.ZIntegrable`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/ThermoQuantities.lean#L100).

> To be able to compute or define anything from a Hamiltonian, we need its partition function to
> be a computable integral. A Hamiltonian is ZIntegrable at β if PartitionZ is Lesbegue integrable
> and nonzero.

```lean
def ZIntegrable (β : ℝ) : Prop
```

**`MicroHamiltonian.PositiveβIntegrable`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/ThermoQuantities.lean#L109).

> This Prop defines the most common case of ZIntegrable, that it is integrable at all finite
> temperatures (aka all positive β).

```lean
def PositiveβIntegrable : Prop
```

**`MicroHamiltonian.entropy_A_eq_entropy_Z`**, a theorem, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/ThermoQuantities.lean#L133). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The two definitions of entropy, in terms of `T` or `β = 1 / T`, are equivalent.

```lean
theorem entropy_A_eq_entropy_Z (T : ℝ) (hT : T ≠ 0)
    (hZne : H.partitionZ d (1 / T) ≠ 0)
    (hZint : ((1 / T : ℝ) : ℂ) ∈ interior (H.ZComplexConvergenceDomain d)) :
    entropyS H d T = entropySβ H d (1 / T)
```

**`MicroHamiltonian.β_eq_deriv_S_U`**, a theorem, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/ThermoQuantities.lean#L168). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The "definition of temperature from entropy":
> 1/T = (∂S/∂U), when the derivative is at constant extrinsic d (typically N/V).
> Here we use β instead of 1/T on the left, and express the right actually as (∂S/∂β)/(∂U/∂β),
> as all our things are ultimately parameterized by β.
>
> This identity requires the denominator `∂U/∂β` to be nonzero.

```lean
theorem β_eq_deriv_S_U {β : ℝ}
    (hZne : H.partitionZ d β ≠ 0)
    (hZint : (β : ℂ) ∈ interior (H.ZComplexConvergenceDomain d))
    (hU' : deriv (H.internalU d) β ≠ 0) :
    β = (deriv (H.entropySβ d) β) / deriv (H.internalU d) β
```

**`NVEHamiltonian.pressure`**, a def, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/ThermoQuantities.lean#L219).

> Pressure, as a function of T. Defined as the conjugate variable to volume.

```lean
def pressure (T : ℝ) : ℝ
```

## Depends on

- [The Microcanonical Ensemble](basic.md)
- [QuantumInfo.ForMathlib.ComplexLaplaceTransform](../../../quantuminfo/formathlib/complexlaplacetransform.md)

## Sources

- [Physlib/StatisticalMechanics/MicroCanonicalEnsemble/ThermoQuantities.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/ThermoQuantities.lean)
