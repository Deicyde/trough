---
declaration: theorem
origin: cited
lean: PDL.interpolation, PDL.beth
statement: formalized
proof: formalized
---

# Craig interpolation and Beth definability for propositional dynamic logic

> Proves Craig interpolation for full propositional dynamic logic, including tests and Kleene star, by constructing interpolants from uniform cyclic tableaux. Interpolants use only atomic propositions and atomic programs common to the two formulas. The development also proves the local Beth definability property for a propositional letter, and supplies reusable syntax, Kripke semantics, Fischer-Ladner closure, tableau soundness and completeness, finite reachability and game-theoretic infrastructure. The results assert existence; no executable extraction algorithm or complexity bound is claimed. Human contributors and Aristotle jointly developed the formalization. The completeness modules reuse the finite game determinacy theorem already pooled in `LeanPool.Lean4GlCoalgebras` instead of duplicating it.

*Quoted from the card [LeanPool/projects/pdl-craig-interpolation.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/pdl-craig-interpolation.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`PDL.interpolation`](https://leanpool.github.io/lean-pool/LeanPool/PDL/Interpolation/Theorem.html#PDL.interpolation) (theorem; a main declaration), declared in [LeanPool/PDL/Interpolation/Theorem.lean, line 27](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/PDL/Interpolation/Theorem.lean#L27): “If the implication from PDL formula phi to psi is valid in every Kripke model, there exists a PDL formula theta whose atomic proposition and program vocabulary is contained in the intersection of theirs, such that phi implies theta and theta implies psi in every model.”
- [`PDL.beth`](https://leanpool.github.io/lean-pool/LeanPool/PDL/Beth.html#PDL.beth) (theorem; a main declaration), declared in [LeanPool/PDL/Beth.lean, line 29](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/PDL/Beth.lean#L29): “If a PDL formula phi implicitly determines a propositional letter p (all two-letter substitutions agree wherever both substituted formulas hold), there is a formula psi using only phi's vocabulary other than p such that phi entails that p is equivalent to psi.”
- [`PDL.consIffSat`](https://leanpool.github.io/lean-pool/LeanPool/PDL/Completeness/Theorem.html#PDL.consIffSat) (theorem), declared in [LeanPool/PDL/Completeness/Theorem.lean, line 152](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/PDL/Completeness/Theorem.lean#L152): “A free sequent is tableau-consistent if and only if it is satisfiable in a Kripke model.”

## Project

- Authors: PDL formalization contributors.
- Contributors: Malvin Gattinger, Madeleine Gignoux, Noam Cohen, Haitian Wang, Wietse Bosman, Xiaoshuang Yang, Amos Nicodemus, Andrés Goens, DdosSantosGomes, Eshel Yaron, Dionysis Yusofy.
- Source: *Propositional Dynamic Logic has Craig Interpolation: a tableau-based proof* by Manfred Borzechowski, Malvin Gattinger, Helle Hvid Hansen, Revantha Ramanayake, Francisco Trucco Dalmas, Yde Venema, [arXiv:2503.13276](https://arxiv.org/abs/2503.13276).
- Project repository: [m4lvin/lean4-pdl](https://github.com/m4lvin/lean4-pdl), at commit [ec3b050e](https://github.com/m4lvin/lean4-pdl/tree/ec3b050e59cd829a350e92c512951a381a80cddd).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 03B45, 03B70, 03F03.
- In Lean Pool: [LeanPool/PDL](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/PDL), from the card [LeanPool/projects/pdl-craig-interpolation.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/pdl-craig-interpolation.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/pdl-craig-interpolation.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/pdl-craig-interpolation.yaml)
- [Lean Pool at 701389c0: LeanPool/PDL](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/PDL)
