---
declaration: theorem
origin: cited
lean: MIPRE.Tailored.Sofic.value_le_one, MIPRE.Tailored.Sofic.valSof_le_one, MIPRE.Tailored.Sofic.valSof_eq_one_of_hasPerfectZPC, MIPRE.Tailored.Sofic.CII, MIPRE.Tailored.Sofic.gameValue_ge_of_valSof, MIPRE.Tailored.Sofic.gapK, MIPRE.Tailored.Sofic.primrec_gapK, MIPRE.Tailored.Sofic.mainTheoremII
statement: formalized
proof: formalized
---

# Main Theorem II; Theorem I:2126

Let $G$ be a tailored game with answer length $\Lambda$. If $G$ has a perfect ZPC strategy, its associated test has sofic value $1$. If its associated test has sofic value at least $1 - \varepsilon$, then $G$ has synchronous value at least $1 - 600 (\Lambda+1)^4 2^{6(\Lambda+1)} \varepsilon$. So the clauses of Theorem [The sofic value is not approximable; Corollary I:2144, measure-free](thm-sofic-not-approximable.md) hold with the primitive recursive gap $K(\Lambda) = 600 (\Lambda+1)^4 2^{6(\Lambda+1)}$.

## Depends on

- [The associated subgroup test; I:2086](def-assoc-test.md)
- [Perturbing to pass Checks 1–3; Proposition I:2267](prop-assoc-perturb.md)
- [Game value of an action passing Checks 1–3; Proposition I:2279](prop-checks-game-value.md)
- [Completeness: lifting a perfect strategy; Theorem I:2126 (1)](lem-assoc-completeness.md)
- [The sofic value is not approximable; Corollary I:2144, measure-free](thm-sofic-not-approximable.md)

## Proof

Completeness is Lemma [Completeness: lifting a perfect strategy; Theorem I:2126 (1)](lem-assoc-completeness.md), no action having value above $1$. Soundness: for every $\delta > 0$ an action has value at least $1 - \varepsilon - \delta$; perturb it to pass Checks 1–3 (Proposition [Perturbing to pass Checks 1–3; Proposition I:2267](prop-assoc-perturb.md)) and apply Proposition [Game value of an action passing Checks 1–3; Proposition I:2279](prop-checks-game-value.md); then let $\delta \to 0$.

## Lean

Formalized as [`MIPRE.Tailored.Sofic.value_le_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.value_le_one), [`MIPRE.Tailored.Sofic.valSof_le_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.valSof_le_one), [`MIPRE.Tailored.Sofic.valSof_eq_one_of_hasPerfectZPC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.valSof_eq_one_of_hasPerfectZPC), [`MIPRE.Tailored.Sofic.CII`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.CII), [`MIPRE.Tailored.Sofic.gameValue_ge_of_valSof`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.gameValue_ge_of_valSof), [`MIPRE.Tailored.Sofic.gapK`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.gapK), [`MIPRE.Tailored.Sofic.primrec_gapK`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.primrec_gapK), [`MIPRE.Tailored.Sofic.mainTheoremII`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.mainTheoremII).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 338](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L338)
