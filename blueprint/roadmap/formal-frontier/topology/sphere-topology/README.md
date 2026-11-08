# Sphere topology

> Reusable Lean topology and singular homology: fixed points of complex-valued continuous maps on closed balls of nonnegative radius whose sphere-boundary images lie in the ball, with no interior image bound; degree-zero boundary restrictions and non-retraction for the complex closed unit disk; arbitrary-index circle bouquets, inclusions, positive-generator homomorphisms, retractions and generator nonidentity, and a positive-generator-preserving free-group identification with the universal property for group targets in independent universes; jointly injective factor retractions and factorwise T0/T1/T2 classification for arbitrary chosen-point wide pushouts, including empty families; normalization of nowhere-zero continuous fields, identity-to-antipodal homotopies from orthogonal fields, integral subdivision, cover-small chains and two-open Mayer-Vietoris, nonnegative reduced integral homology and degree-zero criteria for path connectedness. Finite-fiber coverings give transfers on all-simplex singular chains and ordinary homology with categorical coefficient objects. Signed-period circle fundamental-group coordinates, generic based lifting, monodromy, maps of covers and deck-group comparisons are supplied by Fundamental Groupoids, their canonical home, and re-exported through deprecated Sphere circle and covering module paths. H-space loop multiplication, circle degree, free homotopy and disk results remain in Sphere; private coordinate and circle H-space checks are in SphereTopologyTest.CircleHSpace. Explicit circle and two-sphere calculations give the antipodal action on H2 of the standard two-sphere and its continuous orthogonal-field hairy-ball theorem. The metric two-sphere lifted to any universe has a non-nullhomotopic identity, distinct identity and north-constant based homotopy classes, and a nontrivial second homotopy group.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/formalization.yaml) of [FormalFrontier/sphere-topology](https://github.com/FormalFrontier/sphere-topology) at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), Apache-2.0.*

22 articles: 5 for highlights of its formalization.yaml whose declarations the scan finds and 17 for headline results in its README whose declaration link names a declaration the scan finds in the linked file. Its other headline results are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/sphere-topology](https://github.com/FormalFrontier/sphere-topology), read at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “agent-reviewed”.
- Automation: agent; tool setup “Lean and Lake with pinned mathlib APIs, compiler feedback and Lean tactics.”
- Automation notes: “Project code, proofs, documentation and metadata are AI-authored. See docs/CREDITS.md for contributor and source-origin attribution. AI authorship does not establish correctness, ownership or redistribution rights; third-party implementation and source assets are not redistributed here.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- [The K-book: An Introduction to Algebraic K-theory](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.pdf), Charles A. Weibel, Complete-book build dated 2013-08-29, Example I.1.2.2 (book; background).
- [A Concise Course in Algebraic Topology](https://www.math.uchicago.edu/~may/CONCISE/ConciseRevised.pdf), J. Peter May, Revised edition, Chapter 1, §§5–7; Chapter 2, §8; Chapter 8, §§1–2, pp. 57–58; Chapter 9, §1, p. 65; Chapter 16, Problem 3 (book; background).

## Builds on

- [Fundamental groupoids](../fundamental-groupoids/README.md) (a Lake dependency, pinned at 24d8b2f4)
- [Group theory](../../group-theory/group-theory/README.md) (a Lake dependency, pinned at 9c060da7)
- [Simplicial objects](../../homological-algebra-and-category-theory/simplicial-objects/README.md) (a Lake dependency, pinned at 143f667b)

## Used by

- [Complex analysis](../../analysis/complex-analysis/README.md)
- [Fundamental groupoids](../fundamental-groupoids/README.md)

## [Brouwer fixed points on complex… to Fundamental groups of…](part-01/README.md)

- [Brouwer fixed points on complex disks](part-01/brouwer-fixed-points-on-complex-disks.md)
- [Hairy-ball theorem for the metric two-sphere](part-01/hairy-ball-theorem-for-the-metric-two-sphere.md)
- [Free fundamental groups of circle bouquets](part-01/free-fundamental-groups-of-circle-bouquets.md)
- [Sphere cogroups and sharp cocommutativity](part-01/sphere-cogroups-and-sharp-cocommutativity.md)
- [Nontrivial second homotopy group of the metric two-sphere](part-01/nontrivial-second-homotopy-group-of-the-metric-t.md)
- [H-space fundamental groups commute](part-01/h-space-fundamental-groups-commute.md)
- [Last-axis one-point compactification coordinates](part-01/last-axis-one-point-compactification-coordinates.md)
- [Finite generalized loops and based sphere-map classes](part-01/finite-generalized-loops-and-based-sphere-map-cl.md)
- [Positive-dimensional spheres as cogroups](part-01/sphere-cogroups-and-sharp-cocommutativity.md)
- [Homotopy groups and the sphere-map group](part-01/homotopy-groups-and-the-sphere-map-group.md)
- [Sharp cocommutativity of sphere cogroups](part-01/sphere-cogroups-and-sharp-cocommutativity.md)
- [Nontrivial second homotopy group of S²](part-01/nontrivial-second-homotopy-group-of-s2.md)
- [Canonical antipodal quotient covering](part-01/canonical-antipodal-quotient-covering.md)
- [Real projective fundamental groups and lifted endpoints](part-01/real-projective-fundamental-groups-and-lifted-en.md)
- [Boundary-only fixed points on complex closed balls](part-01/brouwer-fixed-points-on-complex-disks.md)
- [Embeddings, closed maps and neighborhoods of point-wide-pushouts](part-01/embeddings-closed-maps-and-neighborhoods-of-poin.md)
- [Point-relative equivalences and contractions](part-01/point-relative-equivalences-and-contractions.md)
- [Factor retractions and separation of point-wide-pushouts](part-01/factor-retractions-and-separation-of-point-wide.md)
- [Charts around a common subset](part-01/charts-around-a-common-subset.md)
- [Fundamental groups of factor-plus-core charts](part-01/fundamental-groups-of-factor-plus-core-charts.md)

## [Subfamily retractions and… to Covering-space lifts of…](part-02/README.md)

- [Subfamily retractions and continuous factorization](part-02/subfamily-retractions-and-continuous-factorizati.md)
- [Strict finite-stage factorization of compact homotopies](part-02/strict-finite-stage-factorization-of-compact-hom.md)
- [Arbitrary-index circle bouquets](part-02/arbitrary-index-circle-bouquets.md)
- [Diagonal equivalence for non-antipodal pairs](part-02/diagonal-equivalence-for-non-antipodal-pairs.md)
- [Covering-space lifts of simplices](part-02/covering-space-lifts-of-simplices.md)

## Main results

Its formalization.yaml lists 76 main results, and the scan finds 75 of them declared in the file the yaml gives; they are on their own page, not made articles. The scan does not find `ContinuousMap.normalizeOfNoZero` ([SphereTopology/Homotopy/TangentField.lean](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/TangentField.lean)).

- [Main results](main-results/README.md)
