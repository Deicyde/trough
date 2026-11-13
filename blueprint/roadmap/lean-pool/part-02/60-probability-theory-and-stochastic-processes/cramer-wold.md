---
declaration: theorem
origin: cited
lean: LeanPool.CramerWold.euclideanSpace_measure_eq_of_forall_inner_map_eq
statement: formalized
proof: formalized
---

# The Cramer-Wold theorem

> Formalizes the finite-dimensional Cramer-Wold theorem for measures on Euclidean spaces, with Banach-space continuous-dual generalizations, Hilbert-space inner-product versions, and random-variable law corollaries for identical distributions and `HasLaw`.

*Quoted from the card [LeanPool/projects/cramer-wold.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/cramer-wold.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LeanPool.CramerWold.euclideanSpace_measure_eq_of_forall_inner_map_eq`](https://leanpool.github.io/lean-pool/LeanPool/CramerWold.html#LeanPool.CramerWold.euclideanSpace_measure_eq_of_forall_inner_map_eq) (theorem; a main declaration), declared in [LeanPool/CramerWold.lean, line 153](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CramerWold.lean#L153): “Proves the classical finite-dimensional Cramer-Wold theorem for finite Borel measures on `EuclideanSpace ℝ (Fin n)`, showing equality when all scalar projections have equal pushforward measures.”
- [`LeanPool.CramerWold.measure_eq_of_forall_dual_map_eq`](https://leanpool.github.io/lean-pool/LeanPool/CramerWold.html#LeanPool.CramerWold.measure_eq_of_forall_dual_map_eq) (theorem), declared in [LeanPool/CramerWold.lean, line 51](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CramerWold.lean#L51): “Generalizes the extensionality criterion to finite Borel measures on complete second-countable real normed spaces, using all continuous-linear real projections.”
- [`LeanPool.CramerWold.measure_eq_of_forall_inner_map_eq`](https://leanpool.github.io/lean-pool/LeanPool/CramerWold.html#LeanPool.CramerWold.measure_eq_of_forall_inner_map_eq) (theorem), declared in [LeanPool/CramerWold.lean, line 102](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CramerWold.lean#L102): “Specializes Cramer-Wold extensionality to real Hilbert spaces, using scalar projections of the form `x ↦ ⟪t, x⟫_ℝ`.”
- [`LeanPool.CramerWold.identDistrib_of_forall_dual_comp_identDistrib`](https://leanpool.github.io/lean-pool/LeanPool/CramerWold.html#LeanPool.CramerWold.identDistrib_of_forall_dual_comp_identDistrib) (theorem), declared in [LeanPool/CramerWold.lean, line 209](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CramerWold.lean#L209): “Proves that two finite-measure random variables are identically distributed when every continuous-linear real projection of them is identically distributed.”
- [`LeanPool.CramerWold.identDistrib_of_forall_inner_comp_identDistrib`](https://leanpool.github.io/lean-pool/LeanPool/CramerWold.html#LeanPool.CramerWold.identDistrib_of_forall_inner_comp_identDistrib) (theorem), declared in [LeanPool/CramerWold.lean, line 262](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CramerWold.lean#L262): “Gives the Hilbert-space random-variable version using all scalar inner-product projections.”
- [`LeanPool.CramerWold.hasLaw_of_forall_dual_comp_hasLaw`](https://leanpool.github.io/lean-pool/LeanPool/CramerWold.html#LeanPool.CramerWold.hasLaw_of_forall_dual_comp_hasLaw) (theorem), declared in [LeanPool/CramerWold.lean, line 314](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CramerWold.lean#L314): “Proves that a random variable has a target law when every continuous-linear real projection has the corresponding projected target law.”

## Project

- Authors: Lazar Milikic.
- Source: *Some theorems on distribution functions* by Harald Cramer, Herman Wold, [doi:10.1112/jlms/s1-11.4.290](https://doi.org/10.1112/jlms/s1-11.4.290).
- Project repository: [Lemmy00/lean-pool](https://github.com/Lemmy00/lean-pool).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 60B11, 60E10, 28A33.
- In Lean Pool: [LeanPool/CramerWold](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CramerWold), from the card [LeanPool/projects/cramer-wold.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/cramer-wold.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/cramer-wold.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/cramer-wold.yaml)
- [Lean Pool at 701389c0: LeanPool/CramerWold](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CramerWold)
