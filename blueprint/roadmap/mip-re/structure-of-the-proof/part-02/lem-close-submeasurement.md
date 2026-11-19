---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.submeasurement_completion_mass, MIPRE.Introspection.submeasurement_completion_dist, MIPRE.Introspection.submeasurement_completion_dist_avg
statement: formalized
proof: formalized
---

# Completing a nearby submeasurement

Let $A_a^x$ be a PVM, $B_a^x\geq0$ with $\sum_aB_a^x\leq{I}$, and $C_a^x$ a POVM satisfying $C_a^x\geq B_a^x$ pointwise. For a unit bipartite state and an arbitrary question distribution, define

$$
D_\psi(A,B)=\mathbb E_x\sum_a
\|((A_a^x-B_a^x)\otimes{I})\psi\|^2=\delta.
$$

Then $D_\psi(A,C)\leq2\delta+4\sqrt\delta$. In particular, if $D_\psi(A,B)\leq\varepsilon\leq1$, the conclusion is $D_\psi(A,C)\leq6\sqrt\varepsilon$. A coefficient-one square-root bound is not asserted for this literal squared-distance convention.

## Depends on

- [State-dependent POVM distance](../../foundations/part-02/def-state-distance.md)

## Proof depends on

- [Combined $XZ$ point measurements](../../background-results/part-02/lem-qld-combined-points.md)
- [Commutation analysis](../../foundations/part-02/lem-commutation-analysis.md)

## Proof

Using real parts and Cauchy–Schwarz in the outcome-summed state norm, $\mathbb E_x\langle{I}-\sum_aB_a^x\rangle\leq2\sqrt\delta$; here $\sum_a(B_a^x)^2\leq\sum_aB_a^x$ and $\sum_a(A_a^x)^2={I}$. Since $0\leq C_a^x-B_a^x\leq{I}$, $(C_a^x-B_a^x)^2\leq C_a^x-B_a^x$, so $D_\psi(B,C)\leq2\sqrt\delta$. The squared triangle bound gives $D_\psi(A,C)\leq2D_\psi(A,B)+2D_\psi(B,C)$.

## Lean

Formalized as [`MIPRE.Introspection.submeasurement_completion_mass`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.submeasurement_completion_mass), [`MIPRE.Introspection.submeasurement_completion_dist`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.submeasurement_completion_dist), [`MIPRE.Introspection.submeasurement_completion_dist_avg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.submeasurement_completion_dist_avg).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1463](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1463)
