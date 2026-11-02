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

This is a finite product of $K_v$-modules each of which has the $K_v$-module topology by [Theorem IsDedekindDomain.HeightOneSpectrum.adicCompletion.instIsModuleTopology](isdedekinddomain-heightonespectrum-adiccompletio.md), and the product topology is the module topology for a finite product of modules each of which has the module topology (this is in mathlib).

## Lean

Formalized as [`IsDedekindDomain.HeightOneSpectrum.adicCompletion.instIsModuleTopologyPi`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/IsDedekindDomain.HeightOneSpectrum.adicCompletion.instIsModuleTopologyPi).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 300](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L300)
