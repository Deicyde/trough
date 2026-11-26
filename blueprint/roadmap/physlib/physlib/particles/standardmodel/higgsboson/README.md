# HiggsBoson

The folder [Physlib/Particles/StandardModel/HiggsBoson/](https://github.com/leanprover-community/physlib/tree/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Particles/StandardModel/HiggsBoson): 3 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Higgs Field* ([Physlib/Particles/StandardModel/HiggsBoson/API-map.md](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Particles/StandardModel/HiggsBoson/API-map.md)): its Content section, with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### Pointwise Higgs values
>
> The pointwise Higgs values form a two-dimensional complex Euclidean space. [\[1\]](basic.md) They carry an orthonormal basis, and a real mass scale determines a Higgs vector with the expected norm. [\[2\]](basic.md) They correspond to four real scalar coordinates. [\[3\]](basic.md)
>
> The global Standard Model gauge group \{1} acts on them through a representation, given explicitly as a U(1) phase times an SU(2) matrix and compatible with the group law. [\[4\]](basic.md) That representation preserves inner products and norms. [\[5\]](basic.md) Two Higgs vectors lie in the same gauge orbit exactly when they have the same norm. The electromagnetic U(1) leaves the Higgs vacuum (0, v) invariant, and one of its elements removes the phase of the first component. [\[6\]](basic.md) The stability group of a Higgs vector is the gauge group it leaves unbroken: for the vacuum (0, √a) it is SU(3) × U(1)\_EM, for any other nonzero Higgs vector it is a conjugate of this, and the subgroup fixing every Higgs vector is SU(3) × ℤ₆. [\[7\]](basic.md) Pairs of Higgs vectors, with this gauge action, are the configurations of the two Higgs doublet model \{2}.
>
> ### The Higgs bundle and Higgs fields
>
> The Higgs bundle over spacetime \{3} is a smooth vector bundle, currently the trivial bundle with fibre the pointwise Higgs values. [\[8\]](basic.md) …
>
> A Higgs field has a Higgs vector as its value at each spacetime point, and every Higgs vector defines a constant field. [\[9\]](basic.md) The real and imaginary parts of its components are real analytic. [\[10\]](basic.md) The pointwise inner product of two Higgs fields has an explicit expansion, is conjugate symmetric and additive, and is smooth. [\[11\]](basic.md) The squared norm is the real part of the inner product of the field with itself; it is nonnegative and smooth. [\[12\]](basic.md) …
>
> The weak isospin factor SU(2) acts on the two complex components of a Higgs doublet, with the colour and hypercharge factors set to the identity. [\[4\]](basic.md) In the trivial bundle, on a region where the doublet is nowhere zero, a local weak rotation sends it to the neutral representative whose second component is its norm. For a $C^n$ doublet the chosen rotation has $C^n$ matrix entries on the region. [\[13\]](basic.md) This is the scalar part of unitary gauge: the doublet's direction is fixed while its magnitude can vary across spacetime.
>
> On a region where the first of two $C^n$ doublets is nowhere zero, their pointwise squared norms agree exactly when a weak rotation with $C^n$ matrix entries carries the first to the second there. For Higgs fields this gives real analytic matrix entries on that region. \[14\] …
>
> ### The Higgs potential
>
> The Standard Model Higgs potential \{4} has a mass parameter and a quartic coupling, and evaluates smoothly on a Higgs field; negating both parameters negates the potential, and the potential vanishes on the zero field; at each spacetime point it is gauge invariant. [\[15\]](potential.md) Completing the square writes it as a quadratic in the norm squared, whose discriminant is nonnegative and vanishes exactly in a characterized case. [\[16\]](potential.md)
>
> A bounded-below potential has nonnegative quartic coupling, and a positive quartic coupling makes it bounded below. [\[17\]](potential.md) The values it attains, its bounds when the discriminant vanishes, and its minimum for positive and maximum for negative quartic coupling are all determined explicitly. [\[17\]](potential.md)
>
> ### Effective potentials
>
> An effective potential is a function on pointwise Higgs values; when it is gauge invariant it is constant on gauge orbits and so factors through the norm. [\[18\]](effectivepotential.md) An effective potential of bounded mass dimension is polynomial, splits into homogeneous terms of each mass dimension whose odd terms vanish when it is invariant, and is then a sum of powers of the norm. [\[19\]](effectivepotential.md) …

Its references:

> - \{1\} Standard Model gauge group API map — [Physlib/Particles/StandardModel/GaugeGroup/API-map.md](../gaugegroup/README.md)
> - \{2\} Two Higgs Doublet Model API map — [Physlib/Particles/BeyondTheStandardModel/TwoHDM/API-map.md](../../beyondthestandardmodel/twohdm/README.md)
> - \{3\} Spacetime API map — [Physlib/SpaceAndTime/SpaceTime/API-map.md](../../../spaceandtime/spacetime/README.md)
> - \{4\} M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory*, Westview Press (1995), Ch. 20, on gauge theories with spontaneous symmetry breaking.

- [The Higgs field](basic.md)
- [The effective potential of the Higgs field](effectivepotential.md)
- [The potential of the Higgs field](potential.md)
