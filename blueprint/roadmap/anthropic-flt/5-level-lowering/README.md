# 5. Level lowering

> **5. Level lowering.** `FreyPackage.level_lowering_to_two`: E\_P modular and ρ̄\_{E\_P,p} irreducible give a nonzero
> `f : CuspForm (CongruenceSubgroup.Gamma0 2) 2`. First `FreyPackage.modularRepOfConductorLevel`: the representation arises
> from a squarefree level supported on the primes dividing abc, "arises from" (`ModularRepOfLevel`,
> `Definitions/Def_FLTPrelim_ModularRep.lean`) being a congruence of traces modulo a prime above p, not an isomorphism
> of representations (this proof re-derives modularity itself, so the `IsModular` hypothesis above is formally
> unused). Then primes are removed one at a time (`FreyPackage.level_lowering_to_two_of_conductorLevel`): an odd
> q ≠ p, at which E\_P[p] is unramified, by `FreyPackage.level_lowering_odd_prime_of_conductorLevel`, Ribet's theorem
> in the form needed (Čerednik-Drinfeld uniformisation, `CerednikDrinfeld` namespace); p itself by
> `FreyPackage.level_lowering_at_p_of_conductorLevel`, the Mazur-Ribet step, using that E\_P[p] is finite at p
> (`FreyCurve.isPeuRamifieeAt_odd_of_integralForm`). Levels 1 and 2 are closed by `ModularForm.S2_Gamma0_one_eq_zero`
> and step 6.

*Quoted from the route of the proof in [PROOF-PATH.md](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/PROOF-PATH.md) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0.*

The landmarks the repository's web pages place in this step, in the order this step names them, then by name:

- [Level lowering](freypackage-level-lowering-to-two.md)
- [FreyPackage.modularRepOfConductorLevel](freypackage-modularrepofconductorlevel.md)
- [FreyPackage.level_lowering_to_two_of_conductorLevel](freypackage-level-lowering-to-two-of-conductorle.md)
- [FreyPackage.level_lowering_odd_prime_of_conductorLevel](freypackage-level-lowering-odd-prime-of-conducto.md)
- [FreyPackage.level_lowering_at_p_of_conductorLevel](freypackage-level-lowering-at-p-of-conductorleve.md)
- [FreyCurve.isPeuRamifieeAt_odd_of_integralForm](freycurve-ispeuramifieeat-odd-of-integralform.md)
- [CuspForm.newformBadPrimeCoeff](cuspform-newformbadprimecoeff.md)
- [FreyPackage.eigenformResidualAttachmentAtFamily](freypackage-eigenformresidualattachmentatfamily.md)
- [FreyPackage.freyGaloisRep_isUnramifiedAt](freypackage-freygaloisrep-isunramifiedat.md)
- [WeierstrassCurve.isResiduallyModularOfLevel_div_of_isUnramifiedAt_sqf](weierstrasscurve-isresiduallymodularoflevel-div.md)
