# Introduction

This blueprint documents the formalization of **de Finetti's theorem** and the **de Finetti–Ryll-Nardzewski equivalence** for infinite sequences on *standard Borel spaces*.

The main result establishes a three-way equivalence between:

- **Contractable**: All strictly increasing subsequences of equal length have the same distribution
- **Exchangeable**: Distribution invariant under finite permutations
- **Conditionally i.i.d.**: There exists a probability kernel such that finite marginals equal mixtures of product measures

We formalize *all three proofs* from Kallenberg (2005):

1. **Koopman/Ergodic approach** using the Mean Ergodic Theorem
2. **L$^2$ approach** using elementary contractability bounds
3. **Martingale approach** using reverse martingale convergence (after Aldous)
