# HiggsBoson

The folder [Physlib/Particles/StandardModel/HiggsBoson/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson): 3 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Higgs Field* ([Physlib/Particles/StandardModel/HiggsBoson/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/API-map.md)): its Content section, with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

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
> Higgs fields are smooth sections of the Higgs bundle; each has an underlying map to pointwise Higgs values, and every Higgs vector gives a constant field. [\[9\]](basic.md) The components of a Higgs field are smooth, real and imaginary parts alike. [\[10\]](basic.md) The pointwise inner product of two Higgs fields has an explicit expansion, is conjugate symmetric and additive, and is smooth. [\[11\]](basic.md) The pointwise norm squared of a Higgs field is the real part of its inner product with itself, is nonnegative, and is smooth. [\[12\]](basic.md)
>
> … Since the gauge group preserves inner products and norms of Higgs vectors, the pointwise inner product and norm squared of Higgs fields are gauge invariant. [\[5\]](basic.md)
>
> ### The Higgs potential
>
> The Standard Model Higgs potential \{4} has a mass parameter and a quartic coupling, and evaluates smoothly on a Higgs field; negating both parameters negates the potential, and the potential vanishes on the zero field; at each spacetime point it is gauge invariant. [\[14\]](potential.md) Completing the square writes it as a quadratic in the norm squared, whose discriminant is nonnegative and vanishes exactly in a characterized case. [\[15\]](potential.md)
>
> A bounded-below potential has nonnegative quartic coupling, and a positive quartic coupling makes it bounded below. [\[16\]](potential.md) The values it attains, its bounds when the discriminant vanishes, and its minimum for positive and maximum for negative quartic coupling are all determined explicitly. [\[16\]](potential.md)
>
> ### Effective potentials
>
> An effective potential is a function on pointwise Higgs values; when it is gauge invariant it is constant on gauge orbits and so factors through the norm. [\[17\]](effectivepotential.md) An effective potential of bounded mass dimension is polynomial, splits into homogeneous terms of each mass dimension whose odd terms vanish when it is invariant, and is then a sum of powers of the norm. [\[18\]](effectivepotential.md) …

Its references:

> - \{1\} Standard Model gauge group API map — [Physlib/Particles/StandardModel/GaugeGroup/API-map.md](../gaugegroup/README.md)
> - \{2\} Two Higgs Doublet Model API map — [Physlib/Particles/BeyondTheStandardModel/TwoHDM/API-map.md](../../beyondthestandardmodel/twohdm/README.md)
> - \{3\} Spacetime API map — [Physlib/SpaceAndTime/SpaceTime/API-map.md](../../../spaceandtime/spacetime/README.md)
> - \{4\} M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory*, Westview Press (1995), Ch. 20, on gauge theories with spontaneous symmetry breaking.

- [The Higgs field](basic.md)
- [The effective potential of the Higgs field](effectivepotential.md)
- [The potential of the Higgs field](potential.md)
