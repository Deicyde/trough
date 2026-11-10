# 4. Modularity

> **4. Modularity.** `FreyPackage.frey_isModular` follows from `WeierstrassCurve.modularity_of_semistableModel`: every
> integral Weierstrass model with Δ ≠ 0 and no prime dividing both Δ and c₄ (`IsSemistableModel`) is modular
> (`IsModular`: a\_ℓ matches a normalised weight-2 eigenform on some Γ₀(N) at good primes; both in
> `Definitions/Def_FLTPrelim_Modularity.lean`; cusp forms, Γ₀(N) and q-expansions are Mathlib's). The proof is Wiles's:
>
> - one of ρ̄\_{W,3}, ρ̄\_{W,5} is irreducible (`WeierstrassCurve.modThreeOrFiveIrreducible`: if both were reducible W would
>   have a rational 15-isogeny, and `WeierstrassCurve.fifteenIsogenyClassification` pins c₄³/Δ of such a curve to one of
>   four values, none of which a semistable model can have);
> - Langlands-Tunnell in the weight-2, level-conditioned form Wiles uses,
>   `WeierstrassCurve.isResiduallyModular_three_and_noInertiaFixedTorsion_and_not_cube_dvd_of_isSemistableModel`: a
>   weight-one form for the odd octahedral representation lifting ρ̄\_{W,3}
>   (`LanglandsTunnell.exists_isWeightOneChiNegThreeRealized_eq_trace_lift`, for surjective ρ̄₃ with cyclotomic determinant,
>   by Tunnell's argument: monomial automorphy over the subfields cut out by subgroups of GL₂(F₃), cyclic base change,
>   a converse theorem with Rankin-Selberg integrals), then multiplication by the Eisenstein series E₁(1, χ₋₃) and a
>   Deligne-Serre lifting lemma to reach a congruent weight-2 eigenform;
> - two modularity lifting theorems, R = T by Taylor-Wiles patching in Diamond's formulation
>   (`GaloisRep.DeformationRingData`, `CuspForm.HeckeGaloisRepDatum`, `Algebra.PatchingDatum`,
>   `GaloisRep.DeformationRingData.exists_surjective_algHom_of_heckeGaloisRepDatum`):
>   `WeierstrassCurve.modularityLiftingAtConductor_threeFive_of_level_of_inertia_moves_torsion_of_eq_three_of_not_cube_dvd`
>   (p = 3; a condition on inertia-fixed 3-torsion when 9 divides the residual level) and
>   `WeierstrassCurve.modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd` (p ∈ {3, 5}; p² not
>   dividing the residual level);
> - the 3-5 switch `WeierstrassCurve.threeFiveSwitchCurve` (a second semistable model W′ with ρ̄\_{W′,3} irreducible and
>   a\_ℓ(W′) ≡ a\_ℓ(W) (mod 5) at common good primes ℓ ≠ 5, built beneath from a curve with W′[5] ≅ W[5] taken from an
>   explicit family in the `RubinSilverberg` namespace) and `WeierstrassCurve.isResiduallyModularOfLevel_of_switch`.
> If ρ̄\_{W,3} is irreducible, Langlands-Tunnell and lifting at 3; otherwise the switch gives W′, the first case makes
> W′ modular, W is residually modular mod 5, and lifting at 5 finishes.

*Quoted from the route of the proof in [PROOF-PATH.md](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/PROOF-PATH.md) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0.*

The landmarks the repository's web pages place in this step, in the order this step names them, then by name:

- [Modularity](freypackage-frey-ismodular.md)
- [WeierstrassCurve.modularity_of_semistableModel](weierstrasscurve-modularity-of-semistablemodel.md)
- [WeierstrassCurve.modThreeOrFiveIrreducible](weierstrasscurve-modthreeorfiveirreducible.md)
- [WeierstrassCurve.fifteenIsogenyClassification](weierstrasscurve-fifteenisogenyclassification.md)
- [WeierstrassCurve.isResiduallyModular_three_and_noInertiaFixedTorsion_and_not_cube_dvd_of_isSemistableModel](weierstrasscurve-isresiduallymodular-three-and-n.md)
- [LanglandsTunnell.exists_isWeightOneChiNegThreeRealized_eq_trace_lift](langlandstunnell-exists-isweightonechinegthreere.md)
- [GaloisRep.DeformationRingData.exists_surjective_algHom_of_heckeGaloisRepDatum](galoisrep-deformationringdata-exists-surjective.md)
- [WeierstrassCurve.modularityLiftingAtConductor_threeFive_of_level_of_inertia_moves_torsion_of_eq_three_of_not_cube_dvd](weierstrasscurve-modularityliftingatconductor-th.md)
- [WeierstrassCurve.modularityLiftingAtConductor_threeFive_of_level_of_not_sq_dvd_of_not_cube_dvd](weierstrasscurve-modularityliftingatconductor-th-2.md)
- [WeierstrassCurve.threeFiveSwitchCurve](weierstrasscurve-threefiveswitchcurve.md)
- [WeierstrassCurve.isResiduallyModularOfLevel_of_switch](weierstrasscurve-isresiduallymodularoflevel-of-s.md)
- [Algebra.PatchingDatum.nonempty_patchingLevel_bot](algebra-patchingdatum-nonempty-patchinglevel-bot.md)
- [AutomorphicForm.exists_weightOne_cuspForm_of_isCusp_viaCompactCuspNotion](automorphicform-exists-weightone-cuspform-of-isc.md)
- [ResidualGaloisRep.isAbsolutelyIrreducible_of_isIrreducible_of_isOdd](residualgaloisrep-isabsolutelyirreducible-of-isi.md)
- [WeierstrassCurve.exists_forall_not_isRoot_Psi3_specialization](weierstrasscurve-exists-forall-not-isroot-psi3-s.md)
- [WeierstrassCurve.galoisRepIsIrreducible_three_of_forall_eval_Psi3_ne_zero](weierstrasscurve-galoisrepisirreducible-three-of.md)
- [WeierstrassCurve.isModularModelOfLevel_conductorLevel_of_not_cube_dvd_of_modRepIsIrreducible_of_not_sq_dvd](weierstrasscurve-ismodularmodeloflevel-conductor.md)
- [WeierstrassCurve.isModularModelOfLevel_of_patchingDatum](weierstrasscurve-ismodularmodeloflevel-of-patchi.md)
- [WeierstrassCurve.nonempty_deformationRingData_ordinaryCondition_of_isSemistableModel](weierstrasscurve-nonempty-deformationringdata-or.md)
- [WeierstrassCurve.threeFiveAuxiliaryCurveExists](weierstrasscurve-threefiveauxiliarycurveexists.md)
