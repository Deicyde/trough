---
declaration: theorem
origin: cited
lean: NumberField.AdeleRing.instIsModuleTopology
statement: formalized
proof: formalized
---

# NumberField.AdeleRing.baseChange\_moduleTopology

If $K\to L$ is a ring homomorphism between two number fields then the topology on $\mathbb{A}_L$ is the $\mathbb{A}_K$-module topology, where the module structure comes from the natural map $\mathbb{A}_K\to\mathbb{A}_L$.

## Depends on

- [NumberField.AdeleRing.baseChangeEquiv](numberfield-adelering-basechangeequiv.md)

## Proof

Indeed $\mathbb{A}_L\cong L\otimes_K\mathbb{A}_K$ is a homeomorphism, and the right hand side has the $\mathbb{A}_K$-module topology.

## Lean

Formalized as [`NumberField.AdeleRing.instIsModuleTopology`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.AdeleRing.instIsModuleTopology).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 953](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L953)
