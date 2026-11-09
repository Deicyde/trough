# 3. Irreducibility

> **3. Irreducibility.** `FreyPackage.Mazur_Frey` proves `GaloisRepIsIrreducible ℚ P.freyCurve P.p`
> (`Definitions/Def_FLTPrelim_GaloisRep.lean`: E\_P[p] is nontrivial with no Galois-stable F\_p-submodule besides 0 and
> itself). The case a ≡ 3 (mod 8) has its own argument at the prime 2 (`FreyPackage.Mazur_Frey_of_a_mod_eight`).
> Otherwise reducibility would give a Galois-stable line with trivial action on the quotient
> (`FreyPackage.frey_reducible_hasCofixedLine`, Serre's observation, using that E\_P has no rational point of order p),
> excluded in three ranges:
>
> - p ≥ 17: `FreyPackage.frey_no_cofixed_large`, Mazur's Eisenstein-ideal argument carried out for this situation
>   (X₀(N), its Jacobian and Néron model, the cuspidal subgroup, the Eisenstein quotient; `ModularCurve` and
>   `AlgebraicGeometry` namespaces; the global input is `WeierstrassCurve.mazurStepThree_not_inZeroComponentAt`). This is
>   by far the largest part of the step.
> - p = 11 (`FreyPackage.frey_no_cofixed_eleven`) and p ∈ {5, 7, 13} (`FreyPackage.frey_no_cofixed_small`) hold
>   vacuously because those exponents are settled outright: `fermatLastTheoremFive` by a self-contained descent in
>   Z[(1+√5)/2]; `fermatLastTheoremSeven`, `…Eleven`, `…Thirteen` by Kummer's theorem for regular primes `flt_regular`
>   (a port of the flt-regular project: cases I and II, Kummer's lemma via Hilbert's theorems 90-94) plus proofs
>   that the rings of integers of the 7th, 11th and 13th cyclotomic fields are principal
>   (`IsCyclotomicExtension.Rat.seven_pid`, `….eleven_pid`, `….thirteen_pid`).

*Quoted from the route of the proof in [PROOF-PATH.md](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/PROOF-PATH.md) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0.*

The landmarks the repository's web pages place in this step, in the order this step names them, then by name:

- [Irreducibility](freypackage-mazur-frey.md)
- [FreyPackage.Mazur_Frey_of_a_mod_eight](freypackage-mazur-frey-of-a-mod-eight.md)
- [FreyPackage.frey_reducible_hasCofixedLine](freypackage-frey-reducible-hascofixedline.md)
- [FreyPackage.frey_no_cofixed_large](freypackage-frey-no-cofixed-large.md)
- [WeierstrassCurve.mazurStepThree_not_inZeroComponentAt](weierstrasscurve-mazurstepthree-not-inzerocompon.md)
- [FreyPackage.frey_no_cofixed_eleven](freypackage-frey-no-cofixed-eleven.md)
- [FreyPackage.frey_no_cofixed_small](freypackage-frey-no-cofixed-small.md)
- [fermatLastTheoremFive](fermatlasttheoremfive.md)
- [fermatLastTheoremSeven](fermatlasttheoremseven.md)
- [flt_regular](flt-regular.md)
- [IsCyclotomicExtension.Rat.seven_pid](iscyclotomicextension-rat-seven-pid.md)
- [ModularCurve.eisensteinQuotientInvariantsFiniteAt_heckeModuleBar](modularcurve-eisensteinquotientinvariantsfinitea.md)
- [ModularCurve.mazurQuotientSpecialization_heckeModuleBar](modularcurve-mazurquotientspecialization-heckemo.md)
