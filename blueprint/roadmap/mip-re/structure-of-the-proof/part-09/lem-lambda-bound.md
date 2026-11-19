---
declaration: lemma
origin: cited
lean: MIPRE.Halting.lambda_bound, MIPRE.Halting.log_lt_div, MIPRE.Halting.sq_le_two_pow_of_four_le, MIPRE.Halting.four_mul_succ_lt_two_pow
statement: formalized
proof: formalized
---

# A uniform bound on the verifier's parameter

For all integers $C, C' \geq 1$, all $\lambda \geq 4 \max\{ (4C)^{8C},\ C \log C' \}$ and all $n \geq 2$,

$$
C\, (C' \lambda n)^{C} \;\leq\; n^{\lambda} .
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Bound each factor of the left-hand side by a power of $n$ — $C' \leq 2^{\log C' + 1}$, $\lambda \leq 2^{\log \lambda + 1}$, $C \leq 2^{C}$, and $2 \leq n$ — so that the claim reduces to the *linear* inequality $4C + C \log C' + C \log \lambda \leq \lambda$. Two of its three terms are a quarter of $\lambda$ by hypothesis outright. The third, $C \log \lambda \leq \lambda/4$, is the only one with content, and it is $\lambda < 2^{\lambda / 4C}$: writing $q = \lambda / 4C$, the hypothesis $\lambda \geq 4(4C)^{8C}$ gives $q \geq 8C + 4$, and there $4C(q+1) < q^2 \leq 2^q$, the second inequality holding from $q = 4$ on.

## Lean

Formalized as [`MIPRE.Halting.lambda_bound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.lambda_bound), [`MIPRE.Halting.log_lt_div`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.log_lt_div), [`MIPRE.Halting.sq_le_two_pow_of_four_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.sq_le_two_pow_of_four_le), [`MIPRE.Halting.four_mul_succ_lt_two_pow`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.four_mul_succ_lt_two_pow).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 7151](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L7151)
