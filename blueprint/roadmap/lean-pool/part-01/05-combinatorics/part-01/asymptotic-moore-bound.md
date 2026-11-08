---
declaration: theorem
origin: cited
lean: MooreBound.DegreeDiameter.theorem_1_1
statement: formalized
proof: formalized
---

# Asymptotically attaining the Moore bound

> Proves that, for each fixed positive diameter k, the largest order of a finite simple graph with maximum degree at most d and extended diameter at most k is asymptotic to d^k as d tends to infinity. Constructs regular halved-flag graphs over every finite field, with exact order and diameter, a sharp degree cap, and matching asymptotics through all prime powers. Also proves the corresponding lower-limit bound for the edge extremum defined using line-graph diameter. Reusable infrastructure includes common bases for complete flags, odd-even sorting routes, exact flag enumeration, projective-line completion counts, and bipartite graph expansion. The analytic bridge retains the Wiener-Ikehara and prime-counting dependency closure from the Apache-2.0 PrimeNumberTheoremAnd project. The paper describes AI-assisted formalization supervised by the human authors.

*Quoted from the card [LeanPool/projects/asymptotic-moore-bound.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/asymptotic-moore-bound.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`MooreBound.DegreeDiameter.theorem_1_1`](https://leanpool.github.io/lean-pool/LeanPool/MooreBound/DegreeDiameter/Results.html#MooreBound.DegreeDiameter.theorem_1_1) (theorem; a main declaration), declared in [LeanPool/MooreBound/DegreeDiameter/Results.lean, line 36](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MooreBound/DegreeDiameter/Results.lean#L36): “For each positive natural k, n(k,d)/d^k tends to 1 as the natural degree bound d tends to infinity. Here n(k,d) is the maximum number of vertices of a finite simple graph with maximum degree at most d and extended diameter at most k.”
- [`MooreBound.DegreeDiameter.corollary_1_2`](https://leanpool.github.io/lean-pool/LeanPool/MooreBound/DegreeDiameter/Results.html#MooreBound.DegreeDiameter.corollary_1_2) (theorem), declared in [LeanPool/MooreBound/DegreeDiameter/Results.lean, line 48](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MooreBound/DegreeDiameter/Results.lean#L48): “For each natural ell at least 2, the lower limit of h(ell,d)/d^ell is at least 1. Here h(ell,d) is one plus the maximum number of edges of a finite simple graph with maximum degree at most d whose line graph has extended diameter at most ell.”
- [`MooreBound.DegreeDiameter.proposition_3_1`](https://leanpool.github.io/lean-pool/LeanPool/MooreBound/DegreeDiameter/Proposition31Full.html#MooreBound.DegreeDiameter.proposition_3_1) (theorem), declared in [LeanPool/MooreBound/DegreeDiameter/Proposition31Full.lean, line 77](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MooreBound/DegreeDiameter/Proposition31Full.lean#L77): “For every positive k and prime power q, the concrete halved-flag graph is regular, has order [2k+1]\_q!/(q+1)^k, degree at most (q+1)^k((q+1)^k-1), and extended diameter exactly k. Along all prime powers q tending to infinity, its actual degree divided by this cap and its order divided by the kth power of its actual degree both tend to 1.”
- [`MooreBound.DegreeDiameter.alternating_route`](https://leanpool.github.io/lean-pool/LeanPool/MooreBound/DegreeDiameter/Lemma21.html#MooreBound.DegreeDiameter.alternating_route) (theorem), declared in [LeanPool/MooreBound/DegreeDiameter/Lemma21.lean, line 72](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MooreBound/DegreeDiameter/Lemma21.lean#L72): “Any two complete flags in an n-dimensional vector space over a division ring admit an n-step route that changes only ranks of the prescribed alternating parity at each step.”
- [`MooreBound.prime_between`](https://leanpool.github.io/lean-pool/LeanPool/MooreBound/PrimeNumberTheoremAnd/Consequences.html#MooreBound.prime_between) (theorem), declared in [LeanPool/MooreBound/PrimeNumberTheoremAnd/Consequences.lean, line 1120](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MooreBound/PrimeNumberTheoremAnd/Consequences.lean#L1120): “For every positive real epsilon, every sufficiently large real x admits a prime strictly between x and (1+epsilon)x.”

## Project

- Authors: Wouter Cames van Batenburg, Samuel Korsky, PrimeNumberTheoremAnd contributors.
- Source: *Asymptotically attaining the Moore bound* by Wouter Cames van Batenburg, Samuel Korsky, [arXiv:2608.03965](https://arxiv.org/abs/2608.03965).
- Project repository: [woutercvb/wewantmoore](https://github.com/woutercvb/wewantmoore), at commit [d59bd80e](https://github.com/woutercvb/wewantmoore/tree/d59bd80ea93fabb9faf769e790ab47692645e022).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 05C35, 05B25, 11N05.
- In Lean Pool: [LeanPool/MooreBound](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MooreBound), from the card [LeanPool/projects/asymptotic-moore-bound.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/asymptotic-moore-bound.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/asymptotic-moore-bound.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/asymptotic-moore-bound.yaml)
- [Lean Pool at 2b205bf9: LeanPool/MooreBound](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MooreBound)
