---
navigation: transparent
---

# Subfamily retractions and… to Covering-space lifts of…

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/README.md#headline-results) of [FormalFrontier/sphere-topology](https://github.com/FormalFrontier/sphere-topology) at commit [672d46f9](https://github.com/FormalFrontier/sphere-topology/tree/672d46f90cf51cdf3f933248b85c842990ead729), Apache-2.0.*

- [Subfamily retractions and continuous factorization](subfamily-retractions-and-continuous-factorizati.md)
- [Strict finite-stage factorization of compact homotopies](strict-finite-stage-factorization-of-compact-hom.md)
- [Arbitrary-index circle bouquets](arbitrary-index-circle-bouquets.md)
- [Diagonal equivalence for non-antipodal pairs](diagonal-equivalence-for-non-antipodal-pairs.md)

**Continuous hairy-ball theorem for S².**
[`sphere2_exists_zero_of_orthogonal_field`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/HairyBallSphere2.lean)
says every `V : C(sphere2, E3)` pointwise orthogonal to the radius has a zero.
In any real inner-product space, a nowhere-zero continuous orthogonal field
on the metric unit sphere gives an explicit identity-to-antipodal homotopy
([`TangentField`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homotopy/TangentField.lean)), without finite
dimensionality. Only the zero theorem specializes to Euclidean three-space.

**Circle/S² homology and antipodal sign.** Ordered punctures give
`H̃₁(S¹; ℤ) ≅ ℤ` and `H̃₂(S²; ℤ) ≅ ℤ`, in the unit-sphere models in
`EuclideanSpace ℝ (Fin 2)` and `EuclideanSpace ℝ (Fin 3)`
([`Circle`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homology/Singular/Circle.lean),
[`Sphere`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homology/Singular/Sphere.lean)). The circle basis is
upper minus lower; the equator coordinate is ordered `(x,y)`.
[`SphereAntipodal`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homology/Singular/SphereAntipodal.lean)
computes `-id` on ordinary and reduced integral `H₂`, hence multiplication
by `-1` in the fixed integer coordinate and nonhomotopy to identity.

- [Covering-space lifts of simplices](covering-space-lifts-of-simplices.md)

**Finite-fiber covering transfer.** For `p : Y ⟶ X`, `IsCoveringMap p` and
finite point fibers,
[`singularChainComplexTransfer`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homology/Singular/Transfer.lean)
uses coefficient objects in any preadditive category with coproducts indexed
in the space universe; object and morphism universes are independent.
Ordinary homology adds only `CategoryWithHomology` and uses `q : ℕ`.
A simplex maps to the sum of its lifts. Transfer then pushforward is
`d • id` if every point fiber has cardinality `d`; finiteness is a separate
premise. No constant degree, nonemptiness, surjectivity or connectedness is
needed for the construction.

**Subdivision and cover-small chains.** Integral signed subdivision `Sd`
and its support-preserving prism `H` satisfy `∂H + H∂ = id − Sd`
([`Subdivision`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homology/Singular/Subdivision.lean)). For an
open cover, inclusion of finite-support chains small in a cover member is a
quasi-isomorphism
([`SmallChains`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homology/Singular/SmallChains.lean)). Space
and cover-index universes may differ; no global nonemptiness is assumed.
Cover-respecting continuous maps and refinements induce compatible chain maps.

**Ordered ordinary and reduced Mayer–Vietoris.** Two opens covering a space
give difference `(c,−c)` followed by sum, all three successive ordinary
exactness positions, ordered-cover naturality and cover-swap minus sign
([`MayerVietoris`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homology/Singular/MayerVietoris.lean)).
The reduced low-degree boundary uses open-intersection homology and is an
isomorphism when both `H̃₀` and `H̃₁` vanish on each open. The reduced
degree-zero sequence is exact at the biproduct for every two-open cover;
its final map is epic when the intersection is nonempty, not unconditionally
([`ReducedMayerVietoris`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homology/Singular/ReducedMayerVietoris.lean)).

**Components and path connectedness.**
[`Components`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homology/Singular/Components.lean) presents the
augmentation kernel by nonbasepoint path components, with categorical
coefficients. In a preadditive category with the requisite coproducts and
homology, `H₀(X; R) ⟶ R` is invertible exactly when `X` is path connected
if `R` is nonzero; nonemptiness is a conclusion
([`Connectedness`](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/SphereTopology/Homology/Singular/Connectedness.lean)).
For nonempty `X`, integral `H̃₀(X)=0` is equivalent to path connectedness.
Reduced homology is nonnegative, with augmentation kernel in degree zero,
ordinary homology in positive degrees and `H̃₀(∅)=0`; no degree-minus-one
convention is asserted. Contractible-space premises include nonemptiness.

**Covering foundations from Fundamental Groupoids.** The dependency supplies
based unique lifting, monodromy, maps of covers, deck actions and based
equal-image equivalences; Sphere re-exports the five deprecated covering
module paths below. The [guide](https://github.com/FormalFrontier/sphere-topology/blob/672d46f90cf51cdf3f933248b85c842990ead729/docs/guide.md#headline-results) gives the
distinct connectedness and local path connectedness hypotheses for each
result. These are not a general classification of coverings.
