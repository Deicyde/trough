---
declaration: module
origin: cited
lean: IdealGas.ideal_gas_law, IdealGas, IdealGas.partitionZ_eq, IdealGas.helmholtzA_eq, IdealGas.ZIntegrable
statement: formalized
proof: formalized
---

# Ideal gas as a Micro Canonical Ensemble

The module `Physlib.StatisticalMechanics.MicroCanonicalEnsemble.IdealGas`, [Physlib/StatisticalMechanics/MicroCanonicalEnsemble/IdealGas.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/IdealGas.lean): 5 declarations, 4 with a docstring, 1 listed as significant.

> In this module we give the

**`IdealGas`**, a def, [line 25](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/IdealGas.lean#L25).

> The Hamiltonian for an ideal gas: particles live in a cube of volume V^(1/3), and each
> contributes an energy p^2/2. The per-particle mass is normalized to 1.

```lean
def IdealGas : NVEHamiltonian
```

**`IdealGas.partitionZ_eq`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/IdealGas.lean#L56).

> The partition function Z for an ideal gas.

```lean
lemma partitionZ_eq (hV : 0 < V) (hβ : 0 < β) :
    IdealGas.partitionZ (n,V) β = V ^ n * (2 * Real.pi / β) ^ (3 * n / 2 : ℝ)
```

**`IdealGas.helmholtzA_eq`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/IdealGas.lean#L178).

> The Helmholtz Free Energy A for an ideal gas.

```lean
lemma helmholtzA_eq (hV : 0 < V) (hT : 0 < T) : IdealGas.helmholtzA (n,V) T =
    -n * T * (Real.log V + (3/2) * Real.log (2 * Real.pi * T))
```

**`IdealGas.ZIntegrable`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/IdealGas.lean#L185).

```lean
lemma ZIntegrable (hV : 0 < V) (hβ : 0 < β) : IdealGas.ZIntegrable (n,V) β
```

**`IdealGas.ideal_gas_law`**, a theorem, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/IdealGas.lean#L196). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The ideal gas law: PV = nRT. In our unitsless system, R = 1.

```lean
theorem ideal_gas_law (hV : 0 < V) (hT : 0 < T) :
    let P := IdealGas.pressure (n,V) T;
    let R := 1;
    P * V = n * R * T
```

## Depends on

- [The theormodynamical quantities of a microcanonical ensemble](thermoquantities.md)

## Sources

- [Physlib/StatisticalMechanics/MicroCanonicalEnsemble/IdealGas.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/MicroCanonicalEnsemble/IdealGas.lean)
