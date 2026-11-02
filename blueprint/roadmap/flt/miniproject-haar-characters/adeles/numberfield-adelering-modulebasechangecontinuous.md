---
declaration: corollary
origin: cited
lean: NumberField.AdeleRing.ModuleBaseChangeContinuousLinearEquiv
statement: formalized
proof: formalized
---

# NumberField.AdeleRing.ModuleBaseChangeContinuousLinearEquiv

If $K$ is a number field and $V$ is an $K$-module, then the natural isomorphism $V\otimes_K\mathbb{A}_K=V\otimes_{\mathbb{Q}}\mathbb{A}_{\mathbb{Q}}$ induced by the natural isomorphism $\mathbb{A}_K=K\otimes_K\mathbb{A}_{\mathbb{Q}}$ is a homeomorphism if the left hand side has the $\mathbb{A}_K$-module topology and the right hand side has the $\mathbb{A}_{\mathbb{Q}}$-module topology.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [IsModuleTopology.continuous\_bilinear\_of\_finite\_left](ismoduletopology-continuous-bilinear-of-finite-l.md)

## Proof

Lemma [IsModuleTopology.continuous\_bilinear\_of\_finite\_left](ismoduletopology-continuous-bilinear-of-finite-l.md) tells us that $V\otimes_K\mathbb{A}_K$ has the $\mathbb{A}_{\mathbb{Q}}$-module topology, and it is easily checked that the isomorphism is $\mathbb{A}_{\mathbb{Q}}$-linear and hence automatically continuous.

Note that in the Lean we prove this for a general extension $L/K$ rather than $K/\mathbb{Q}$.

## Lean

Formalized as [`NumberField.AdeleRing.ModuleBaseChangeContinuousLinearEquiv`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.AdeleRing.ModuleBaseChangeContinuousLinearEquiv).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 763](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L763)
