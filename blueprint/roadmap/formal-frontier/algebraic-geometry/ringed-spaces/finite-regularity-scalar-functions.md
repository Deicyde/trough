---
declaration: def
origin: cited
lean: FiniteRegularityFunctions.sheaf
statement: formalized
---

# Finite-regularity scalar functions

For a charted space over a nontrivially
normed field, [`FiniteRegularityFunctions.sheaf`](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/RingedSpaces/FiniteRegularityFunctions.lean)
gives chosen-chart `C^r` scalar sections for `r : ℕ` and local stalks without
an `IsManifold` or nonempty-carrier assumption. Smooth sections weaken to
finite order; order zero is naturally isomorphic to the existing continuous
scalar sheaf, including compatible stalk evaluation. Finite-`C^r` maps
[pull sections back](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/RingedSpaces/FiniteRegularityFunctions/Maps.lean) and induce
locally ringed-space morphisms compatible with identity, composition and
both endpoint sheaf comparisons. For an open subtype with its induced charts,
inclusion is an [open immersion](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/RingedSpaces/FiniteRegularityFunctions/OpenImmersion.lean)
of locally ringed spaces; the restriction comparison satisfies both whole-arrow
factorization equations. On a finite-order manifold with the self model
`𝓘(𝕜, E)`, [`localBall`](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/RingedSpaces/FiniteRegularityFunctions/LocalBall.lean)
restricts the chosen chart near any point to a diffeomorphism onto an entire
positive-radius ball in the normed model space. Its locally ringed-space
isomorphism identifies the restricted ambient scalar-function space with
the ball's scalar-function space. See the
[finite-regularity guide](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/docs/finite-regularity-functions.md).

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/README.md#headline-results) of [FormalFrontier/ringed-spaces](https://github.com/FormalFrontier/ringed-spaces) at commit [052015f0](https://github.com/FormalFrontier/ringed-spaces/tree/052015f070ef0b3e42c724eb9a8f9a1a1b916682), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `FiniteRegularityFunctions.sheaf` (def), declared in [RingedSpaces/FiniteRegularityFunctions.lean, line 100](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/RingedSpaces/FiniteRegularityFunctions.lean#L100).

Read from the source at commit [052015f0](https://github.com/FormalFrontier/ringed-spaces/tree/052015f070ef0b3e42c724eb9a8f9a1a1b916682), without running Lean.

## Sources

- [ringed-spaces at 052015f0: README, headline results](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/README.md#headline-results)
- [Source of `FiniteRegularityFunctions.sheaf` in RingedSpaces/FiniteRegularityFunctions.lean](https://github.com/FormalFrontier/ringed-spaces/blob/052015f070ef0b3e42c724eb9a8f9a1a1b916682/RingedSpaces/FiniteRegularityFunctions.lean#L100)
