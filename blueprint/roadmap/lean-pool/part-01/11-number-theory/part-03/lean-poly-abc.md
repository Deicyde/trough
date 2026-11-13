---
declaration: theorem
origin: cited
lean: LeanPolyABC.Polynomial.abc, LeanPolyABC.Polynomial.flt
statement: formalized
proof: formalized
---

# Polynomial ABC (Mason–Stothers) and its corollaries

> Formalizes the Mason–Stothers theorem (the polynomial ABC theorem) and derives the polynomial Fermat's Last Theorem, the Fermat–Catalan inequality, Davenport's theorem, and a no-parametrization corollary.

*Quoted from the card [LeanPool/projects/lean-poly-abc.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/lean-poly-abc.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LeanPolyABC.Polynomial.abc`](https://leanpool.github.io/lean-pool/LeanPool/LeanPolyABC/MasonStothers.html#LeanPolyABC.Polynomial.abc) (theorem; a main declaration), declared in [LeanPool/LeanPolyABC/MasonStothers.lean, line 136](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LeanPolyABC/MasonStothers.lean#L136): “Mason–Stothers — for coprime non-constant polynomials with a+b=c, the max degree is below the degree of the radical of abc.”
- [`LeanPolyABC.Polynomial.flt`](https://leanpool.github.io/lean-pool/LeanPool/LeanPolyABC/Corollaries/FltCatalan.html#LeanPolyABC.Polynomial.flt) (theorem; a main declaration), declared in [LeanPool/LeanPolyABC/Corollaries/FltCatalan.lean, line 233](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LeanPolyABC/Corollaries/FltCatalan.lean#L233): “The polynomial Fermat's Last Theorem — no nontrivial coprime polynomial solutions of aⁿ+bⁿ=cⁿ for n ≥ 3.”
- [`LeanPolyABC.Polynomial.flt_catalan`](https://leanpool.github.io/lean-pool/LeanPool/LeanPolyABC/Corollaries/FltCatalan.html#LeanPolyABC.Polynomial.flt_catalan) (theorem), declared in [LeanPool/LeanPolyABC/Corollaries/FltCatalan.lean, line 211](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LeanPolyABC/Corollaries/FltCatalan.lean#L211): “The polynomial Fermat–Catalan inequality bounding solutions of aᵖ+bᵍ=cʳ.”

## Project

- Authors: Seewoo Lee.
- Source: *Formalization of Polynomial ABC and FLT*, [arXiv:2408.15180](https://arxiv.org/abs/2408.15180).
- Project repository: [seewoo5/lean-poly-abc](https://github.com/seewoo5/lean-poly-abc).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 11C08, 12E05.
- In Lean Pool: [LeanPool/LeanPolyABC](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LeanPolyABC), from the card [LeanPool/projects/lean-poly-abc.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/lean-poly-abc.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/lean-poly-abc.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/lean-poly-abc.yaml)
- [Lean Pool at 701389c0: LeanPool/LeanPolyABC](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LeanPolyABC)
