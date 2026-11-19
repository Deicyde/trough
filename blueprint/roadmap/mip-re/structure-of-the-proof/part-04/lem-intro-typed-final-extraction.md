---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.TypedExtraction.cross_check, MIPRE.Introspection.TypedExtraction.condWin_cross_eq, MIPRE.Introspection.TypedExtraction.cross_failure_le, MIPRE.Introspection.TypedExtraction.pairReadout_isPVM, MIPRE.Introspection.TypedExtraction.condWin_cross_readout, MIPRE.Introspection.TypedExtraction.exists_strategy_of_terminal_form, MIPRE.Introspection.TypedExtraction.exists_strategy_of_approx_terminal_form, MIPRE.Introspection.TypedExtraction.exists_strategy_of_state_and_terminal_approx
statement: formalized
proof: formalized
---

# Quantitative extraction from the concrete typed game

The actual cross-introspection test rejects every non-pair constructor and has probability $1/|E|$. Terminal product-form measurements therefore construct an original-game strategy on exactly the auxiliary spaces with failure at most $|E|\varepsilon$. With squared state error $\eta$ and terminal measurement errors $\delta_A,\delta_B$, the proved bound is

$$
|E|(\varepsilon+2\sqrt{\eta})+2\sqrt{\delta_A}+2\sqrt{\delta_B}.
$$

No separate conditional-acceptance premise is assumed. The Pauli extraction and hiding induction must still produce the state and terminal approximations.

## Depends on

- [Exact final strategy extraction](../part-03/lem-intro-final-extraction.md)
- [The parsed introspection decision predicate](../part-02/lem-intro-parsed-predicate.md)
- [Introspection type graph and typed CL family](../part-02/lem-intro-type-presentation.md)
- [Quantitative measurement and state replacement](lem-intro-value-stability.md)
- [Concrete typed sampling and terminal hiding estimates](../part-03/lem-intro-typed-estimates.md)

## Proof depends on

- [Pauli mixing with a retained classical fibre](../part-02/lem-pauli-mixing.md)
- [The register model](../../downstream-results/part-03/lem-register-model.md)

## Proof

Restrict the acceptance sum to the pair constructors using the parsed predicate, identify their Born law with the original CL distribution, and apply the exact auxiliary-strategy extraction. Combine the actual edge failure bound with the proved state and measurement replacement bounds.

## Lean

Formalized as [`MIPRE.Introspection.TypedExtraction.cross_check`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedExtraction.cross_check), [`MIPRE.Introspection.TypedExtraction.condWin_cross_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedExtraction.condWin_cross_eq), [`MIPRE.Introspection.TypedExtraction.cross_failure_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedExtraction.cross_failure_le), [`MIPRE.Introspection.TypedExtraction.pairReadout_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedExtraction.pairReadout_isPVM), [`MIPRE.Introspection.TypedExtraction.condWin_cross_readout`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedExtraction.condWin_cross_readout), [`MIPRE.Introspection.TypedExtraction.exists_strategy_of_terminal_form`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedExtraction.exists_strategy_of_terminal_form), [`MIPRE.Introspection.TypedExtraction.exists_strategy_of_approx_terminal_form`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedExtraction.exists_strategy_of_approx_terminal_form), [`MIPRE.Introspection.TypedExtraction.exists_strategy_of_state_and_terminal_approx`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedExtraction.exists_strategy_of_state_and_terminal_approx).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2608](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2608)
