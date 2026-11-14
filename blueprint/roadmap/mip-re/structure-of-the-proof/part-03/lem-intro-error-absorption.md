---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.errorProfile_power, MIPRE.Introspection.exists_errorProfile_power, MIPRE.Introspection.iteratedRoot_eq_rpow, MIPRE.Introspection.errorProfile_iteratedRoot, MIPRE.Introspection.errorProfile_power_of_le, MIPRE.Introspection.errorProfile_scale_input, MIPRE.Introspection.errorProfile_scaled_power, MIPRE.Introspection.state_transfer_loss_le_three_sqrt
statement: formalized
proof: formalized
---

# Absorbing fixed introspection error losses

Write $E(a,b,x,\varepsilon)=a(x^a\varepsilon^b+x^{-b})$. For $x\geq1$, $\varepsilon\geq0$, $C,a\geq0$, $0\lt b\leq1$ and $0\lt r\leq1$, there are explicit $A\geq1$ and $0\lt B\leq1$ such that $C E(a,b,x,\varepsilon)^r\leq E(A,B,x,\varepsilon)$. One can take $A=\max\{1,Ca^r,ar\}$ and $B=br$. This also absorbs any fixed number of square roots and a fixed rescaling of $\varepsilon$, including detyping's factor. For $0\leq\delta\leq1$, the state-transfer loss satisfies $\delta+2\sqrt\delta\leq3\sqrt\delta$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Use subadditivity of the $r$-power on nonnegative sums and monotonicity of powers with base at least one. Each square root multiplies the exponent by $1/2$. Absorb the fixed error rescaling into the coefficient before applying the power bound. These are quantitative closure results; they do not replace the soundness induction that must supply the error estimates.

## Lean

Formalized as [`MIPRE.Introspection.errorProfile_power`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.errorProfile_power), [`MIPRE.Introspection.exists_errorProfile_power`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_errorProfile_power), [`MIPRE.Introspection.iteratedRoot_eq_rpow`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.iteratedRoot_eq_rpow), [`MIPRE.Introspection.errorProfile_iteratedRoot`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.errorProfile_iteratedRoot), [`MIPRE.Introspection.errorProfile_power_of_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.errorProfile_power_of_le), [`MIPRE.Introspection.errorProfile_scale_input`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.errorProfile_scale_input), [`MIPRE.Introspection.errorProfile_scaled_power`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.errorProfile_scaled_power), [`MIPRE.Introspection.state_transfer_loss_le_three_sqrt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.state_transfer_loss_le_three_sqrt).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1830](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1830)
