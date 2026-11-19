---
declaration: lemma
origin: cited
lean: MIPRE.CommutingOperatorStrategy.aliceMeas, MIPRE.CommutingOperatorStrategy.bobMeas, MIPRE.CommutingOperatorStrategy.aliceMeas_op, MIPRE.CommutingOperatorStrategy.bobMeas_op, MIPRE.CommutingOperatorStrategy.correlation_eq_bornProb, MIPRE.CommutingOperatorStrategy.value_eq_povmValue, MIPRE.commutingOperatorValue_eq_iSup_povmValue
statement: formalized
proof: formalized
---

# The commuting-operator value is a supremum of model values

The measurements of a commuting-operator strategy are POVMs in the two algebras of its commuting-operator model (Definition [Bipartite model](def-bipartite-model.md)), its correlation is that model's Born rule, and its value is the model's value of those POVMs. So ${\omega^{\mathrm{co}}}(\mathfrak{G})$ is the supremum, over commuting-operator strategies, of the value of their measurements in their own model.

## Depends on

- [Bipartite model](def-bipartite-model.md)
- [Commuting-operator value](../../parallel-repetition/def-co-value-bipartite.md)

## Proof

The $E^x_a$ lie in the commutant of the $F^y_b$, and are positive and sum to ${I}$ there because they are and do in $B(\mathcal{H})$; the same holds for the $F^y_b$ in the commutant of that commutant. The model's Born probability at $(E^x_a, F^y_b)$ is $\mathrm{Re}\langle \psi, E^x_a F^y_b \psi\rangle$, the correlation, and the value is the same sum of payoffs against the same probabilities.

## Lean

Formalized as [`MIPRE.CommutingOperatorStrategy.aliceMeas`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.aliceMeas), [`MIPRE.CommutingOperatorStrategy.bobMeas`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.bobMeas), [`MIPRE.CommutingOperatorStrategy.aliceMeas_op`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.aliceMeas_op), [`MIPRE.CommutingOperatorStrategy.bobMeas_op`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.bobMeas_op), [`MIPRE.CommutingOperatorStrategy.correlation_eq_bornProb`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.correlation_eq_bornProb), [`MIPRE.CommutingOperatorStrategy.value_eq_povmValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.value_eq_povmValue), [`MIPRE.commutingOperatorValue_eq_iSup_povmValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.commutingOperatorValue_eq_iSup_povmValue).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1222](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1222)
