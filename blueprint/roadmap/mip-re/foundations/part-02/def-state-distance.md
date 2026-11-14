---
declaration: definition
origin: cited
lean: MIPRE.stateVec, MIPRE.stateNorm, MIPRE.stateSqNorm, MIPRE.stateDist, MIPRE.IsStateClose, MIPRE.povmStateDist, MIPRE.IsPOVMStateClose, MIPRE.quadForm_eq, MIPRE.stateSqNorm_eq
statement: formalized
---

# State-dependent POVM distance

Let $\mu$ be a distribution on a finite set ${\mathcal{X}}$, let $|\psi\rangle \in \mathbb{C}^{d_\textsc{A}} \otimes \mathbb{C}^{d_\textsc{B}}$, and let $\{A^x\}$, $\{B^x\}$ be families of operators on $\mathbb{C}^{d_\textsc{A}}$. We say $A$ and $B$ are *$\delta$-close on $|\psi\rangle$*, written $A^x \approx_\delta B^x$ when $\mu$ and $|\psi\rangle$ are clear from context, if

$$
\mathop{\mathbb{E}}_{x \sim \mu} \langle\psi| \bigl( (A^x - B^x) \otimes {I}_\textsc{B} \bigr)^\dagger
\bigl( (A^x - B^x) \otimes {I}_\textsc{B} \bigr) |\psi\rangle \;\leq\; \delta\;,
$$

equivalently if $\mathop{\mathbb{E}}_{x\sim\mu} \left\| {((A^x - B^x) \otimes {I}_\textsc{B})|\psi\rangle} \right\|^2 \leq \delta$. For families indexed by answers as well, $\{A^x_a\}$ and $\{B^x_a\}$, the outcome sum sits inside the question average.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.stateVec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.stateVec), [`MIPRE.stateNorm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.stateNorm), [`MIPRE.stateSqNorm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.stateSqNorm), [`MIPRE.stateDist`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.stateDist), [`MIPRE.IsStateClose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsStateClose), [`MIPRE.povmStateDist`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.povmStateDist), [`MIPRE.IsPOVMStateClose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPOVMStateClose), [`MIPRE.quadForm_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.quadForm_eq), [`MIPRE.stateSqNorm_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.stateSqNorm_eq).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 508](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L508)
