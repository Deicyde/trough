---
declaration: section
origin: cited
lean: StatMech.Ising.Z, StatMech.Ising.Zpow, StatMech.Ising.logZSeq, StatMech.Ising.pressure, StatMech.Ising.psv_Bdry
statement: formalized
proof: formalized
---

# Pressure of the Ising model

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/pressure-of-the-ising-model/index.html).

## Partition function of a finite system

The partition function `Z(β) = ∑_s e^{-βE(s)}` of a finite system.

Formalized by `StatMech.Ising.Z`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Pressure.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Pressure.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/pressure-of-the-ising-model/index.html#z).

## Partition function of independent copies

The partition function of `n` independent copies of the system.

Formalized by `StatMech.Ising.Zpow`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Pressure.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Pressure.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/pressure-of-the-ising-model/index.html#zpow).

## Log-partition sequence of independent copies

The sequence `log Z_n` for `n` independent copies.

Formalized by `StatMech.Ising.logZSeq`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Pressure.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Pressure.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/pressure-of-the-ising-model/index.html#log-zseq).

## Pressure from independent copies

The pressure: the limit of `log Z_n / n` for independent copies, obtained from subadditivity.

Formalized by `StatMech.Ising.pressure`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Pressure.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Pressure.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/pressure-of-the-ising-model/index.html#pressure).

## Outer vertex boundary of a box

The outer vertex boundary `Λ_{n+1} ∖ Λ_n` of the box.

Formalized by `StatMech.Ising.psv_Bdry`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PressureSurfaceVolume.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PressureSurfaceVolume.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/pressure-of-the-ising-model/index.html#psv-bdry).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pressure of the Ising model](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/pressure-of-the-ising-model/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/spin-models/pressure-of-the-ising-model)
