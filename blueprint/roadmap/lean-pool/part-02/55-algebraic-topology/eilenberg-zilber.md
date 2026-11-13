---
declaration: def
origin: cited
lean: LeanPool.EilenbergZilber.BisimplicialObject.eilenbergZilber
statement: formalized
---

# Eilenberg–Zilber theorem for bisimplicial objects

> For a bisimplicial object X in an abelian category, constructs a chain homotopy equivalence between the total complex of the alternating face map double complex of X and the alternating face map complex of its diagonal. The equivalence is built from the shuffle map and the Alexander–Whitney map. On normalized complexes, shuffle followed by Alexander–Whitney is the identity, and the other composite is homotopic to the identity via the Eilenberg–Mac Lane recursive homotopy. The result is then transported to the unnormalized complexes along the Moore normalization comparisons. The development includes the combinatorics of (p, q)-shuffles, their signs, and the cancellation of diagonal boundary terms.

*Quoted from the card [LeanPool/projects/eilenberg-zilber.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/eilenberg-zilber.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LeanPool.EilenbergZilber.BisimplicialObject.eilenbergZilber`](https://leanpool.github.io/lean-pool/LeanPool/EilenbergZilber/BisimplicialNormalized.html#LeanPool.EilenbergZilber.BisimplicialObject.eilenbergZilber) (def; a main declaration), declared in [LeanPool/EilenbergZilber/BisimplicialNormalized.lean, line 755](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/EilenbergZilber/BisimplicialNormalized.lean#L755): “For every bisimplicial object X in an abelian category, the total complex of the double complex obtained by taking alternating face map complexes in both simplicial directions is chain homotopy equivalent to the alternating face map complex of the diagonal simplicial object of X.” Its source, as the card gives it: “Generalized Eilenberg–Zilber theorem for bisimplicial objects in an abelian category: Dold–Puppe, "Homologie nicht-additiver Funktoren. Anwendungen", Ann. Inst. Fourier 11 (1961), 201–312, Satz 2.9 (Eilenberg–Zilber–Cartier); the homology-level statement is Weibel, An Introduction to Homological Algebra (1994), Theorem 8.5.1. The product case X\_{p,q} = K_p ⊗ L_q is Eilenberg–Zilber, "On products of complexes", Amer. J. Math. 75 (1953), 200–204.”
- [`LeanPool.EilenbergZilber.BisimplicialObject.eilenbergZilberNormalized`](https://leanpool.github.io/lean-pool/LeanPool/EilenbergZilber/BisimplicialNormalized.html#LeanPool.EilenbergZilber.BisimplicialObject.eilenbergZilberNormalized) (def), declared in [LeanPool/EilenbergZilber/BisimplicialNormalized.lean, line 733](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/EilenbergZilber/BisimplicialNormalized.lean#L733): “The total complex of the bi-normalized Moore double complex of X is chain homotopy equivalent to the normalized Moore complex of the diagonal, via the shuffle and Alexander–Whitney maps; shuffle followed by Alexander–Whitney is the identity.” Its source, as the card gives it: “Eilenberg–Mac Lane, "On the groups H(Π, n), II", Ann. of Math. 60 (1954), 49–139, Theorem 2.1a, stated there for products of complexes and generalized here to an arbitrary bisimplicial object in an abelian category.”

## Project

- Authors: Jeffrey Li.
- Source: [https://github.com/jeffrey-dot-li/lean-homology/tree/40c5aae235b0f499ebfc1e68ce574a62b531203c/HomologyLean/SingularHomology/EilenbergZilberTheorem](https://github.com/jeffrey-dot-li/lean-homology/tree/40c5aae235b0f499ebfc1e68ce574a62b531203c/HomologyLean/SingularHomology/EilenbergZilberTheorem).
- Project repository: [jeffrey-dot-li/lean-homology](https://github.com/jeffrey-dot-li/lean-homology), at commit [40c5aae2](https://github.com/jeffrey-dot-li/lean-homology/tree/40c5aae235b0f499ebfc1e68ce574a62b531203c).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 55U10, 18G30, 18G35.
- In Lean Pool: [LeanPool/EilenbergZilber](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/EilenbergZilber), from the card [LeanPool/projects/eilenberg-zilber.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/eilenberg-zilber.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/eilenberg-zilber.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/eilenberg-zilber.yaml)
- [Lean Pool at 701389c0: LeanPool/EilenbergZilber](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/EilenbergZilber)
