---
declaration: theorem
origin: cited
lean: IsDedekindDomain.HeightOneSpectrum.adicCompletion.instIsModuleTopologyPi
statement: formalized
proof: formalized
---

# IsDedekindDomain.HeightOneSpectrum.adicCompletion.instIsModuleTopologyPi

For $v$ fixed, the product topology on $\prod_{w|v}L_w$ is the $K_v$-module topology.

## Depends on

- [IsDedekindDomain.HeightOneSpectrum.adicCompletion.instIsModuleTopology](isdedekinddomain-heightonespectrum-adiccompletio.md)

## Proof

This is a finite product of $K_v$-modules each of which has the $K_v$-module topology by [IsDedekindDomain.HeightOneSpectrum.adicCompletion.instIsModuleTopology](isdedekinddomain-heightonespectrum-adiccompletio.md), and the product topology is the module topology for a finite product of modules each of which has the module topology (this is in mathlib).

## Lean

Formalized as [`IsDedekindDomain.HeightOneSpectrum.adicCompletion.instIsModuleTopologyPi`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/IsDedekindDomain.HeightOneSpectrum.adicCompletion.instIsModuleTopologyPi).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 300](https://github.com/ImperialCollegeLondon/FLT/blob/019805815d7da565ed1e9f427b6fbd0cbc9d00d3/blueprint/src/chapter/AdeleMiniproject.tex#L300)
