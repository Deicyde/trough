---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Co.SymModel.ev_flip, MIPRE.LIDT.Co.SymModel.ev_L_eq_ev_R, MIPRE.LIDT.Co.SymModel.ev_L_mul_R_comm
statement: formalized
proof: formalized
---

# Swap symmetry in a symmetric model

In a symmetric model (Definition [Symmetric models](def-sym-model.md)), $\mathrm{ev}(J X J) = \mathrm{ev}(X)$ for every bounded operator $X$ on $K$. Consequently $\mathrm{ev}(L(x)) = \mathrm{ev}(R(x))$ and $\mathrm{ev}(L(x)\, R(y)) = \mathrm{ev}(L(y)\, R(x))$ for all $x, y \in \mathcal{P}$.

## Depends on

- [Symmetric models](def-sym-model.md)

## Proof

$J$ is isometric and fixes $\Psi$, so $\langle \Psi, J X J \Psi \rangle = \langle J \Psi, J X \Psi \rangle = \langle \Psi, X \Psi \rangle$. The flip carries $L(x)$ to $R(x)$ by definition, and $R(x)$ to $L(x)$ because $J^2 = 1$; so it carries $L(x)\, R(y)$ to $R(x)\, L(y)$, which is $L(y)\, R(x)$ because the two placements commute. The vendored development takes these facts as hypotheses of a symmetric strategy — the swap fixes the state's density, and the state is permutation invariant — and here they are theorems of the model, so the ported statements drop those hypotheses (`planning/c6b-plan.md`, “Port conventions”).

## Lean

Formalized as [`MIPRE.LIDT.Co.SymModel.ev_flip`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.SymModel.ev_flip), [`MIPRE.LIDT.Co.SymModel.ev_L_eq_ev_R`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.SymModel.ev_L_eq_ev_R), [`MIPRE.LIDT.Co.SymModel.ev_L_mul_R_comm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.SymModel.ev_L_mul_R_comm).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3265](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3265)
