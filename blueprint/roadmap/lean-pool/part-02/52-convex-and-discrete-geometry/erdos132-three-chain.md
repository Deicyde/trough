---
declaration: theorem
origin: cited
lean: Erdos132ThreeChain.nonDiameterSqDists_ne_chain
statement: formalized
proof: formalized
---

# Planar Point Sets Whose Non-Diameter Distances Form a Geometric 3-Chain

> Formalizes a support theorem about planar point sets whose non-diameter squared distances are confined to a geometric progression of ratio three. The chain-quadruple theorem shows that no planar quadruple with all six squared distances in such a chain can span two chain steps, and classifies the seven labelled patterns that do occur: the rhombus of two glued equilateral triangles, in five positions of its long edge, and the equilateral triangle with its centroid, in two. A Gram obstruction then rules out any five-point chain configuration. The lift to n at least thirteen runs through the diameter graph: the Caro--Wei independence bound, proved here, produces an independent five-set once the diameter graph is known to have at most as many edges as the set has points. That edge bound is the Hopf--Pannwitz theorem of 1934, and it already exists in the pool; this project reproves it in its own model as a supporting lemma, claiming no novelty for it, and the overlap is set out in full below. The result is unconditional. There is no prior write-up behind this development. The restriction to ratio 3 is ad hoc: the 3-chain statement was produced by the author's automated research pipeline in August 2026, while the cited source poses the ambient Erdos problem and does not state this restriction or result. This theorem does not resolve Erdos 132, whose distance spectra need not be geometric 3-chains. The descriptive labels used in the Lean docstrings are internal to this development and refer to no numbered result elsewhere. Overlap disclosure. Erdos132ThreeChain.hopfPannwitz is NOT offered as a new result. The pooled project Erdos132N14 already contains the same diameter bound, and the version here exists only so that this project is self-contained. Its statement, verbatim from LeanPool/Erdos132N14/HopfPannwitz.lean, is
>
> theorem diameterEdges_card_le (P : Configuration ι) (S : Finset ι) {d : ℝ} (hd : 0 < d) (hmax : ∀ f ∈ pairs S, P.pairDistance f ≤ d) : (diameterEdges P S d).card ≤ S.card
>
> where, from LeanPool/Erdos132N14/Basic.lean, `Configuration ι` is a structure carrying an injective `point : ι → ℂ`, `pairs S = (S ×ˢ S).filter fun e ↦ e.1 < e.2` for a `LinearOrder ι`, `pairDistance P e = dist (P.point e.1) (P.point e.2)`, and `diameterEdges P S d = (pairs S).filter fun e ↦ P.pairDistance e = d`. The corresponding statement here is
>
> theorem hopfPannwitz {X : Finset Point} {D : ℝ} (hD : IsSqDiameter X D) : ∑ v ∈ X, degree (DiameterAdj D) X v ≤ 2 \* X.card
>
> with `Point = ℝ × ℝ`, `sqDist` the squared Euclidean distance, `DiameterAdj D p q = (p ≠ q ∧ sqDist p q = D)`, `degree adj X v = (X.filter (adj v)).card`, and `IsSqDiameter X D` asserting that `D` is realised by two distinct points of `X` and dominates every squared distance inside `X`. The two are the same mathematical theorem — a positive maximal distance is realised at most as often as there are points — carried by different models: an injective map from a linearly ordered index type into the complex plane, counting a Finset of unordered pairs, against a Finset of points of the real plane, in squared distances and degree-sum form. Neither statement is an instance of the other without a model bridge: a LinearOrder on ℝ × ℝ, a dist-to-sqDist transfer, and a handshake lemma. The proofs differ too, Perles charging there against pendant deletion driven by Cramer's rule here. No project in the pool imports another, and CONTRIBUTING.md records that independence as the property the fast per-project build relies on, so this project reproves the bound rather than importing it. It is a supporting lemma of this development, not one of its results, and it is therefore not listed among the main results below. Two supporting identities also exist elsewhere in the pool. From LeanPool/Erdos97ConvexOctagon/CayleyMenger.lean,
>
> theorem cm4_sqDist_eq_zero (a b c d : Plane) : cm4 (sqDist a b) (sqDist a c) (sqDist a d) (sqDist b c) (sqDist b d) (sqDist c d) = 0
>
> over `Plane = EuclideanSpace ℝ (Fin 2)` is the same four-point Cayley--Menger vanishing as this project's
>
> theorem gramDet_eq_zero (a b c d : Point) : gramDet (sqDist a b) (sqDist a c) (sqDist a d) (sqDist b c) (sqDist b d) (sqDist c d) = 0
>
> over `Point = ℝ × ℝ`; both are one-line `ring` identities in the coordinates. From LeanPool/DistanceGeometry/SchoenbergHard.lean,
>
> theorem schoenberg {D : Matrix (Fin n) (Fin n) ℝ} (hD : IsPreDistMatrix D) : EmbedsIn D k ↔ (centeredGram D).PosSemidef ∧ (centeredGram D).rank ≤ k
>
> characterizes Euclidean distance matrices in general dimension. This project never invokes it: the four-point condition is used directly as a `ring` identity and the five-point obstruction is a sum-of-squares contradiction, so no positive-semidefiniteness criterion is needed.

*Quoted from the card [LeanPool/projects/erdos132-three-chain.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos132-three-chain.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 8 main results, each with its informal statement quoted from the card. The scan finds 8 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`Erdos132ThreeChain.nonDiameterSqDists_ne_chain`](https://leanpool.github.io/lean-pool/LeanPool/Erdos132ThreeChain/Statement.html#Erdos132ThreeChain.nonDiameterSqDists_ne_chain) (theorem; a main declaration), declared in [LeanPool/Erdos132ThreeChain/Statement.lean, line 56](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos132ThreeChain/Statement.lean#L56): “Let n be at least thirteen, let a be positive, and let X be a finite set of points of the real plane with exactly n elements. Suppose D is the squared diameter of X, meaning that D is realised by two distinct points of X and dominates every squared distance inside X. Then for every natural number h, the set of squared distances realised by distinct points of X and different from D is not equal to the geometric 3-chain consisting of a times 3^j for j below h.”
- [`Erdos132ThreeChain.four_chain_adjacent`](https://leanpool.github.io/lean-pool/LeanPool/Erdos132ThreeChain/Support.html#Erdos132ThreeChain.four_chain_adjacent) (theorem), declared in [LeanPool/Erdos132ThreeChain/Support.lean, line 74](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos132ThreeChain/Support.lean#L74): “Let a be positive and let S be a four-element set of points of the real plane such that every squared distance between distinct points of S equals a times a nonnegative power of three. Then there is a positive r, itself equal to a times a nonnegative power of three, for which every squared distance between distinct points of S equals r or 3r.”
- [`Erdos132ThreeChain.pair_classification`](https://leanpool.github.io/lean-pool/LeanPool/Erdos132ThreeChain/FourPoints.html#Erdos132ThreeChain.pair_classification) (theorem), declared in [LeanPool/Erdos132ThreeChain/FourPoints.lean, line 299](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos132ThreeChain/FourPoints.lean#L299): “Let c be positive and let A, B, C, D be points of the real plane with the squared distance from A to B equal to c and every other pairwise squared distance equal to c times a nonnegative power of three. Then each of the four squared distances from A and B to C and to D equals c or 3c, at least one of the two squared distances from A and B to C equals c, likewise for D, the squared distance from C to D equals c or 3c, the squared distance from A to C equals c or that from B to D equals c, the squared distance from B to C equals c or that from A to D equals c, and the whole labelling is one of exactly seven explicit patterns: five with a single edge of squared length 3c, and two in which the three edges of squared length 3c form a triangle.”
- [`Erdos132ThreeChain.no_five_chain_finset`](https://leanpool.github.io/lean-pool/LeanPool/Erdos132ThreeChain/Support.html#Erdos132ThreeChain.no_five_chain_finset) (theorem), declared in [LeanPool/Erdos132ThreeChain/Support.lean, line 134](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos132ThreeChain/Support.lean#L134): “Let a be positive. There is no five-element set of points of the real plane in which every squared distance between distinct points equals a times a nonnegative power of three.”
- [`Erdos132ThreeChain.no_four_on_circle`](https://leanpool.github.io/lean-pool/LeanPool/Erdos132ThreeChain/FivePoints.html#Erdos132ThreeChain.no_four_on_circle) (theorem), declared in [LeanPool/Erdos132ThreeChain/FivePoints.lean, line 64](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos132ThreeChain/FivePoints.lean#L64): “Let c be positive. There are no four points of the real plane, each at squared distance c from a common point, whose six pairwise squared distances all equal c or 3c.”
- [`Erdos132ThreeChain.carowei`](https://leanpool.github.io/lean-pool/LeanPool/Erdos132ThreeChain/CaroWei.html#Erdos132ThreeChain.carowei) (theorem), declared in [LeanPool/Erdos132ThreeChain/CaroWei.lean, line 52](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos132ThreeChain/CaroWei.lean#L52): “Let adj be a symmetric irreflexive relation with decidable adjacency on a type, and let V be a finite set of vertices. Then V has a subset S, no two elements of which are adjacent, whose cardinality is at least the sum over v in V of one divided by one plus the number of neighbours of v inside V.”
- [`Erdos132ThreeChain.exists_independent_five`](https://leanpool.github.io/lean-pool/LeanPool/Erdos132ThreeChain/CaroWei.html#Erdos132ThreeChain.exists_independent_five) (theorem), declared in [LeanPool/Erdos132ThreeChain/CaroWei.lean, line 126](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos132ThreeChain/CaroWei.lean#L126): “Let adj be a symmetric irreflexive relation with decidable adjacency on a type, and let V be a finite set of at least thirteen vertices whose degrees inside V sum to at most twice the cardinality of V. Then V has a five-element subset no two elements of which are adjacent.”
- [`Erdos132ThreeChain.chainTwo_nonDiameter_support`](https://leanpool.github.io/lean-pool/LeanPool/Erdos132ThreeChain/Witnesses.html#Erdos132ThreeChain.chainTwo_nonDiameter_support) (theorem), declared in [LeanPool/Erdos132ThreeChain/Witnesses.lean, line 77](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos132ThreeChain/Witnesses.lean#L77): “There is a five-element set of points of the real plane whose squared diameter is 4 and whose set of non-diameter squared distances is exactly the two-term geometric 3-chain consisting of 1 and 3. The configuration that the headline forbids for at least thirteen points is therefore realisable at five points with chain length two.”

## Project

- Authors: Egor Lyfar.
- Source: *Erdős Problem \#132* by Paul Erdős, János Pach, [https://www.erdosproblems.com/132](https://www.erdosproblems.com/132).
- Project repository: [lyfar/lean-pool](https://github.com/lyfar/lean-pool).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 52C10, 52C35, 05C69.
- In Lean Pool: [LeanPool/Erdos132ThreeChain](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos132ThreeChain), from the card [LeanPool/projects/erdos132-three-chain.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos132-three-chain.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/erdos132-three-chain.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos132-three-chain.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Erdos132ThreeChain](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos132ThreeChain)
